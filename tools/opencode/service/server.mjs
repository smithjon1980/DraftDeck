import express from 'express';
import { createArtifacts } from './artifacts.mjs';
import { createInternalTools } from './internal-tools.mjs';
import { createGoogleAuth } from './google-auth.mjs';
import { createSlideStudio } from './slide-studio.mjs';
import http from 'node:http';
import crypto from 'node:crypto';
import { mkdir, copyFile } from 'node:fs/promises';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import httpProxy from 'http-proxy';
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { CallToolRequestSchema, ListToolsRequestSchema } from '@modelcontextprotocol/sdk/types.js';

const root = path.dirname(fileURLToPath(import.meta.url));
const password = process.env.OPENCODE_SERVER_PASSWORD;
const token = process.env.BOSS_MCP_TOKEN;
if (!password || password.length < 24 || !token || token.length < 32 || password === token) {
  throw new Error('Configure distinct OPENCODE_SERVER_PASSWORD (24+ characters) and BOSS_MCP_TOKEN (32+ characters)');
}
const username = process.env.OPENCODE_SERVER_USERNAME || 'opencode';
const basic = `Basic ${Buffer.from(`${username}:${password}`).toString('base64')}`;
const bearer = `Bearer ${token}`;
const publicOrigin = process.env.PUBLIC_ORIGIN;
if (publicOrigin && (new URL(publicOrigin).origin !== publicOrigin || !publicOrigin.startsWith('https://'))) {
  throw new Error('PUBLIC_ORIGIN must be an HTTPS origin without a trailing slash');
}
const port = Number(process.env.PORT || 8080);
const backendPort = Number(process.env.OPENCODE_INTERNAL_PORT || 4096);
const backend = `http://127.0.0.1:${backendPort}`;
const workspace = path.resolve(process.env.BOSS_WORKSPACE || '/data/workspace');
await mkdir(workspace, { recursive: true });

function matches(actual, expected) {
  const a = Buffer.from(actual || '');
  const b = Buffer.from(expected);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

async function api(route, method = 'GET', body) {
  const result = await fetch(`${backend}${route}`, {
    method,
    headers: { Authorization: basic, 'Content-Type': 'application/json' },
    body: body === undefined ? undefined : JSON.stringify(body),
    signal: AbortSignal.timeout(15000),
  });
  if (!result.ok) throw new Error(`OpenCode API returned HTTP ${result.status}`);
  if (result.status === 204) return null;
  return result.json();
}

const artifacts = await createArtifacts({ dataDirectory: process.env.BOSS_ARTIFACT_DIRECTORY || path.join(workspace, 'artifacts'), page: path.join(root, 'artifacts.html'), publicOrigin });

const tools = [
  ...artifacts.tools,
  {
    name: 'opencode_status', description: 'Check OpenCode health, MCP connection states, and connected model provider IDs. Does not prove private Kaggle access.',
    inputSchema: { type: 'object', properties: {}, additionalProperties: false },
    annotations: { readOnlyHint: true },
  },
  {
    name: 'opencode_sessions', description: 'List up to 20 recent OpenCode sessions in the configured BOSS workspace.',
    inputSchema: { type: 'object', properties: {}, additionalProperties: false },
    annotations: { readOnlyHint: true },
  },
  {
    name: 'opencode_prompt', description: 'Create a session and submit an explicit user-authorized work order asynchronously. May execute tools and modify workspace files. Requires a connected model provider. Use opencode_session to inspect progress; accepted does not mean completed.',
    inputSchema: { type: 'object', properties: { prompt: { type: 'string', minLength: 1, maxLength: 20000 }, title: { type: 'string', minLength: 1, maxLength: 120 } }, required: ['prompt'], additionalProperties: false },
    annotations: { readOnlyHint: false, destructiveHint: true, idempotentHint: false },
  },
  {
    name: 'opencode_session', description: 'Read status and the latest text messages for one OpenCode session. Tool output and generated text require independent verification.',
    inputSchema: { type: 'object', properties: { session_id: { type: 'string', pattern: '^[A-Za-z0-9_-]+$' } }, required: ['session_id'], additionalProperties: false },
    annotations: { readOnlyHint: true },
  },
];

async function call(name, args = {}) {
  if (!args || typeof args !== 'object' || Array.isArray(args)) throw new Error('Arguments must be an object');
  if (name === 'opencode_status') {
    const [health, mcp, providers] = await Promise.all([api('/global/health'), api('/mcp'), api('/provider')]);
    return { health, mcp, connected_providers: providers.connected || [], private_kaggle_access: 'NOT_VERIFIED' };
  }
  if (name === 'opencode_sessions') {
    const sessions = await api('/session');
    return sessions.slice(0, 20).map(({ id, title, time }) => ({ id, title, time }));
  }
  if (name === 'opencode_prompt') {
    if (typeof args.prompt !== 'string' || !args.prompt.trim() || args.prompt.length > 20000) throw new Error('Prompt must contain 1–20000 characters');
    if (args.title !== undefined && (typeof args.title !== 'string' || !args.title.trim() || args.title.length > 120)) throw new Error('Title must contain 1–120 characters');
    const providers = await api('/provider');
    if (!providers.connected?.length) throw new Error('Connect your chosen model provider in OpenCode before submitting work');
    const session = await api('/session', 'POST', { title: args.title || 'BOSS work order' });
    await api(`/session/${encodeURIComponent(session.id)}/prompt_async`, 'POST', { parts: [{ type: 'text', text: args.prompt }] });
    return { session_id: session.id, status: 'ACCEPTED', execution_verified: false };
  }
  if (name === 'opencode_session') {
    if (typeof args.session_id !== 'string' || !/^[A-Za-z0-9_-]+$/.test(args.session_id)) throw new Error('Invalid session ID');
    const id = encodeURIComponent(args.session_id);
    const [session, statuses, messages] = await Promise.all([api(`/session/${id}`), api('/session/status'), api(`/session/${id}/message?limit=10`)]);
    return { session_id: session.id, title: session.title, status: statuses[session.id] || { type: 'idle' }, messages: messages.slice(-10).map(({ info, parts }) => ({ role: info.role, error: info.error, text: parts.filter(p => p.type === 'text').map(p => p.text).join('\n').slice(0, 20000) })), note: 'Idle status alone does not establish successful completion.' };
  }
  if (artifacts.tools.some(tool => tool.name === name)) return artifacts.call(name, args);
  throw new Error('Unknown tool');
}

function createMcp() {
  const server = new Server({ name: 'boss-opencode', version: '0.1.0' }, { capabilities: { tools: {} } });
  server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools }));
  server.setRequestHandler(CallToolRequestSchema, async ({ params }) => {
    try { return { content: [{ type: 'text', text: JSON.stringify(await call(params.name, params.arguments)) }] }; }
    catch (error) { return { isError: true, content: [{ type: 'text', text: error.message }] }; }
  });
  return server;
}

const app = express();
const google = createGoogleAuth();
function browserAuthenticated(req) { return matches(req.headers.authorization, basic) || !!google.authenticate(req); }
function browserGuard(req, res, next) {
  if (matches(req.headers.authorization, basic)) return next();
  if (google.authenticate(req)) return google.guard(req, res, next);
  if (google.enabled && req.headers.accept?.includes('text/html')) return res.redirect(303, '/login?return=' + encodeURIComponent(req.originalUrl));
  return res.status(401).set('WWW-Authenticate', 'Basic realm="BOSS OpenCode", charset="UTF-8"').end();
}
app.disable('x-powered-by');
app.use((req, res, next) => {
  if (req.path === '/health' && req.method === 'GET') return next();
  if (req.headers.origin && req.headers.origin !== publicOrigin) return res.sendStatus(403);
  if (publicOrigin && req.headers.host !== new URL(publicOrigin).host) return res.sendStatus(403);
  next();
});
app.get('/health', async (_req, res) => {
  try { const health = await api('/global/health'); res.status(health.healthy ? 200 : 503).json({ healthy: !!health.healthy }); }
  catch { res.status(503).json({ healthy: false }); }
});
app.use(google.router);
app.get('/auth/basic', (req, res) => {
  if (!matches(req.headers.authorization, basic)) return res.status(401).set('WWW-Authenticate', 'Basic realm="BOSS OpenCode", charset="UTF-8"').end();
  res.redirect(303, '/tools/');
});
app.use('/mcp', (req, res, next) => {
  // OpenCode's browser client also uses /mcp; Basic auth targets its native API.
  if (matches(req.headers.authorization, basic)) return proxy.web(req, res, { headers: { Authorization: basic } });
  if (google.authenticate(req)) return google.guard(req, res, () => proxy.web(req, res, { headers: { Authorization: basic } }));
  if (!matches(req.headers.authorization, bearer)) return res.status(401).set('WWW-Authenticate', 'Bearer realm="boss-opencode"').end();
  next();
}, express.json({ limit: '64kb' }));
app.post('/mcp', async (req, res) => {
  const server = createMcp();
  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined, enableJsonResponse: true });
  res.on('close', () => { void transport.close(); void server.close(); });
  try { await server.connect(transport); await transport.handleRequest(req, res, req.body); }
  catch { if (!res.headersSent) res.status(500).json({ error: 'MCP request failed' }); }
});
app.all('/mcp', (_req, res) => res.sendStatus(405));

app.use('/tools/slides', browserGuard, await createSlideStudio({ directory: path.join(workspace, 'slide-studio'), root }));
app.use('/tools', browserGuard, createInternalTools(root));

app.use('/artifacts', browserGuard, artifacts.router);

const proxy = httpProxy.createProxyServer({ target: backend, ws: true });
proxy.on('error', (_error, _req, res) => {
  if (typeof res.writeHead === 'function' && !res.headersSent) res.writeHead(502);
  res.end();
});
app.use(browserGuard, (req, res) => proxy.web(req, res, { headers: { Authorization: basic } }));
const listener = http.createServer(app);
listener.on('upgrade', (req, socket, head) => {
  if (!browserAuthenticated(req) || (google.authenticate(req) && req.headers.origin !== publicOrigin) || (req.headers.origin && req.headers.origin !== publicOrigin) || (publicOrigin && req.headers.host !== new URL(publicOrigin).host)) {
    socket.end('HTTP/1.1 401 Unauthorized\r\nConnection: close\r\n\r\n'); return;
  }
  proxy.ws(req, socket, head, { headers: { Authorization: basic } });
});

const configPath = path.join(workspace, 'opencode.json');
try { await copyFile(path.join(root, 'runtime-config.json'), configPath, 1); }
catch (error) { if (error.code !== 'EEXIST') throw error; }
const binary = process.env.OPENCODE_BIN || path.join(root, 'node_modules/.bin/opencode');
const childEnvironment = { ...process.env, OPENCODE_CONFIG: configPath };
delete childEnvironment.GOOGLE_CLIENT_SECRET;
const child = spawn(binary, ['web', '--hostname', '127.0.0.1', '--port', String(backendPort)], {
  cwd: workspace, env: childEnvironment, stdio: ['ignore', 'inherit', 'inherit'],
});
child.on('error', () => { console.error('Could not start OpenCode'); listener.close(); process.exitCode = 1; });
child.on('exit', code => { listener.close(); process.exitCode = code || 0; });
for (const signal of ['SIGTERM', 'SIGINT']) process.on(signal, () => {
  child.kill(signal); listener.close(); setTimeout(() => process.exit(0), 5000).unref();
});
listener.listen(port, '0.0.0.0', () => console.log(`BOSS OpenCode gateway listening on port ${port}`));
