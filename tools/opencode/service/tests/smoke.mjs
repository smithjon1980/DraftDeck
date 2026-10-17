import test from 'node:test';
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { randomBytes } from 'node:crypto';
import { mkdtemp, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import net from 'node:net';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

async function freePort() {
  const server = net.createServer();
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const port = server.address().port;
  await new Promise(resolve => server.close(resolve));
  return port;
}

test('real OpenCode gateway: authentication, MCP discovery, backend status, and session reads', { timeout: 120000 }, async () => {
  const directory = await mkdtemp(path.join(os.tmpdir(), 'boss-opencode-'));
  const password = randomBytes(32).toString('hex');
  const token = randomBytes(32).toString('hex');
  const port = await freePort();
  const backendPort = await freePort();
  const url = `http://127.0.0.1:${port}`;
  const child = spawn(process.execPath, ['server.mjs'], {
    env: { ...process.env, OPENCODE_SERVER_PASSWORD: password, BOSS_MCP_TOKEN: token, OPENCODE_SERVER_USERNAME: 'opencode', PUBLIC_ORIGIN: '', PORT: String(port), OPENCODE_INTERNAL_PORT: String(backendPort), BOSS_WORKSPACE: path.join(directory, 'workspace'), XDG_DATA_HOME: path.join(directory, 'data'), XDG_CONFIG_HOME: path.join(directory, 'config'), XDG_CACHE_HOME: path.join(directory, 'cache') },
    stdio: 'ignore',
  });
  const client = new Client({ name: 'boss-verification', version: '0.1.0' });
  try {
    let ready = false;
    for (let attempt = 0; attempt < 120; attempt++) {
      try { const response = await fetch(`${url}/health`); if (response.ok) { ready = true; break; } } catch {}
      if (child.exitCode !== null) throw new Error('Gateway exited before readiness');
      await new Promise(resolve => setTimeout(resolve, 250));
    }
    assert.ok(ready, 'OpenCode health becomes ready');
    assert.equal((await fetch(url)).status, 401);
    assert.equal((await fetch(`${url}/mcp`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: '{}' })).status, 401);
    assert.equal((await fetch(`${url}/mcp`, { method: 'POST', headers: { Authorization: `Bearer ${password}`, 'Content-Type': 'application/json' }, body: '{}' })).status, 401, 'web password cannot authorize MCP');
    assert.equal((await fetch(url, { headers: { Authorization: `Basic ${Buffer.from(`opencode:${password}`).toString('base64')}`, Origin: 'https://untrusted.example' } })).status, 403);
    const transport = new StreamableHTTPClientTransport(new URL(`${url}/mcp`), { requestInit: { headers: { Authorization: `Bearer ${token}` } } });
    await client.connect(transport);
    const tools = await client.listTools();
    assert.deepEqual(tools.tools.map(tool => tool.name).sort(), ['boss_artifacts', 'boss_retrieve_audio', 'opencode_prompt', 'opencode_session', 'opencode_sessions', 'opencode_status']);
    const result = await client.callTool({ name: 'opencode_status', arguments: {} });
    assert.ok(!result.isError, JSON.stringify(result));
    const status = JSON.parse(result.content[0].text);
    assert.equal(status.health.healthy, true);
    assert.equal(status.private_kaggle_access, 'NOT_VERIFIED');
    const basic = `Basic ${Buffer.from(`opencode:${password}`).toString('base64')}`;
    assert.equal((await fetch(`${url}/artifacts`)).status, 401);
    const portal = await fetch(`${url}/artifacts/`, { headers: { Authorization: basic } });
    assert.equal(portal.status, 200);
    assert.match(await portal.text(), /Artifact desk/);
    const nativeMcp = await fetch(`${url}/mcp`, { headers: { Authorization: basic } });
    assert.equal(nativeMcp.status, 200, 'Native OpenCode MCP API remains reachable with browser credentials');
    const artifactState = await client.callTool({ name: 'boss_artifacts', arguments: {} });
    assert.ok(!artifactState.isError);
    const blockedRetrieval = await client.callTool({ name: 'boss_retrieve_audio', arguments: { reference: 'smithjon1980/boss-audio-003-kaggle-setup-repair' } });
    assert.equal(blockedRetrieval.isError, true, 'Missing Kaggle credential blocks retrieval');
    const created = await fetch(`${url}/session`, { method: 'POST', headers: { Authorization: basic, 'Content-Type': 'application/json' }, body: JSON.stringify({ title: 'Bridge verification; no model invocation' }) });
    assert.ok(created.ok);
    const session = await created.json();
    const listing = await client.callTool({ name: 'opencode_sessions', arguments: {} });
    assert.ok(JSON.parse(listing.content[0].text).some(item => item.id === session.id));
    const detail = await client.callTool({ name: 'opencode_session', arguments: { session_id: session.id } });
    assert.ok(!detail.isError, JSON.stringify(detail));
    assert.equal(JSON.parse(detail.content[0].text).session_id, session.id);
    const invalid = await client.callTool({ name: 'opencode_prompt', arguments: { prompt: ' ' } });
    assert.equal(invalid.isError, true);
  } finally {
    await client.close().catch(() => {});
    child.kill('SIGTERM');
    await new Promise(resolve => child.exitCode !== null ? resolve() : child.once('exit', resolve));
    await rm(directory, { recursive: true, force: true });
  }
});
