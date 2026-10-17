import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, writeFile, rm } from 'node:fs/promises';
import { spawn } from 'node:child_process';
import { randomBytes } from 'node:crypto';
import os from 'node:os';
import path from 'node:path';
import net from 'node:net';

async function freePort() {
  const server = net.createServer();
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const port = server.address().port;
  await new Promise(resolve => server.close(resolve));
  return port;
}

test('Google session reaches real gateway tools and native OpenCode APIs without exposing backend credentials', { timeout: 120000 }, async () => {
  const directory = await mkdtemp(path.join(os.tmpdir(), 'boss-google-gateway-'));
  const port = await freePort(), backendPort = await freePort();
  const base = `http://127.0.0.1:${port}`, origin = `https://127.0.0.1:${port}`;
  const password = randomBytes(32).toString('hex'), token = randomBytes(32).toString('hex');
  const preload = path.join(directory, 'fixture-provider.mjs');
  // Only this child test process uses a fixture provider. Production has no bypass flag or fixture issuer.
  await writeFile(preload, `import {OAuth2Client} from ${JSON.stringify(import.meta.resolve('google-auth-library'))};
import {generateKeyPairSync,sign} from 'node:crypto';
const {privateKey,publicKey}=generateKeyPairSync('rsa',{modulusLength:2048});
const encode=x=>Buffer.from(JSON.stringify(x)).toString('base64url');
const original=OAuth2Client.prototype.generateAuthUrl;
OAuth2Client.prototype.generateAuthUrl=function(options){this.fixtureNonce=options.nonce;return original.call(this,options)};
OAuth2Client.prototype.getToken=async function(){const timestamp=Math.floor(Date.now()/1000);const body=encode({alg:'RS256',kid:'fixture'})+'.'+encode({iss:'https://accounts.google.com',aud:'fixture-client',sub:'fixture-owner',email:'owner@example.com',email_verified:true,iat:timestamp,exp:timestamp+3600,nonce:this.fixtureNonce});return {tokens:{id_token:body+'.'+sign('RSA-SHA256',Buffer.from(body),privateKey).toString('base64url')}}};
OAuth2Client.prototype.getFederatedSignonCertsAsync=async()=>({certs:{fixture:publicKey.export({type:'spki',format:'pem'})}});
`);
  const child = spawn(process.execPath, ['--import', preload, 'server.mjs'], {
    env: { ...process.env, GOOGLE_AUTH_ENABLED: 'true', GOOGLE_CLIENT_ID: 'fixture-client', GOOGLE_CLIENT_SECRET: 'fixture-secret', GOOGLE_ALLOWED_EMAILS: 'owner@example.com', PUBLIC_ORIGIN: origin, OPENCODE_SERVER_PASSWORD: password, BOSS_MCP_TOKEN: token, PORT: String(port), OPENCODE_INTERNAL_PORT: String(backendPort), BOSS_WORKSPACE: path.join(directory, 'workspace'), XDG_DATA_HOME: path.join(directory, 'data'), XDG_CONFIG_HOME: path.join(directory, 'config'), XDG_CACHE_HOME: path.join(directory, 'cache') },
    stdio: 'ignore',
  });
  const request = (url, options = {}) => fetch(base + url, { ...options, redirect: 'manual' });
  const cookieOf = (r, name) => r.headers.getSetCookie().find(v => v.startsWith(name + '='))?.split(';')[0];
  try {
    let ready = false;
    for (let i = 0; i < 160; i++) {
      try { if ((await request('/health')).ok) { ready = true; break; } } catch {}
      if (child.exitCode !== null) throw Error('Google gateway exited');
      await new Promise(resolve => setTimeout(resolve, 250));
    }
    assert.ok(ready);
    const unauthenticated = await request('/tools/atlas/', { headers: { Accept: 'text/html' } });
    assert.equal(unauthenticated.status, 303); assert.match(unauthenticated.headers.get('location'), /^\/login/);
    const start = await request('/auth/google');
    const state = new URL(start.headers.get('location')).searchParams.get('state');
    const callback = await request('/auth/google/callback?code=fixture&state=' + state, { headers: { Cookie: cookieOf(start, '__Host-boss_oauth') } });
    assert.equal(callback.status, 303);
    const session = cookieOf(callback, '__Host-boss_session'); assert.ok(session);
    for (const url of ['/tools/', '/tools/atlas/', '/artifacts/', '/global/health', '/mcp']) {
      const response = await request(url, { headers: { Cookie: session } });
      assert.equal(response.status, 200, url);
      const body = await response.text(); assert.ok(!body.includes(password) && !body.includes(token));
    }
    const identity = await request('/auth/me', { headers: { Cookie: session } });
    assert.equal((await identity.json()).subject, 'fixture-owner');
    assert.equal((await request('/session', { method: 'POST', headers: { Cookie: session, Origin: 'https://untrusted.example', 'Content-Type': 'application/json' }, body: '{}' })).status, 403);
    assert.equal((await request('/auth/logout', { method: 'POST', headers: { Cookie: session, Origin: origin } })).status, 303);
    assert.equal((await request('/tools/', { headers: { Cookie: session } })).status, 401);
    const basic = 'Basic ' + Buffer.from('opencode:' + password).toString('base64');
    assert.equal((await request('/tools/', { headers: { Authorization: basic } })).status, 200, 'Basic recovery still works');
  } finally {
    child.kill('SIGTERM');
    await new Promise(resolve => { if (child.exitCode !== null) return resolve(); child.once('exit', resolve); setTimeout(() => { child.kill('SIGKILL'); resolve(); }, 7000).unref(); });
    await rm(directory, { recursive: true, force: true });
  }
});
