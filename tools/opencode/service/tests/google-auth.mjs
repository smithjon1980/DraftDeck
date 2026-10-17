import test from 'node:test';
import assert from 'node:assert/strict';
import express from 'express';
import { OAuth2Client } from 'google-auth-library';
import { generateKeyPairSync, sign } from 'node:crypto';
import { createGoogleAuth, safeReturn } from '../google-auth.mjs';

test('return URLs remain local and malformed destinations do not escape the tools hub', () => {
  for (const value of ['//evil.example', '/\\evil.example', '/%2f%2fevil.example', '/auth/google', '/login', 'https://evil.example', '/%0d%0aLocation:bad']) assert.equal(safeReturn(value), '/tools/');
  assert.equal(safeReturn('/tools/atlas/?q=pump'), '/tools/atlas/?q=pump');
});

test('Google login remains disabled without setup and requires a complete explicit configuration', () => {
  assert.equal(createGoogleAuth({ env: {} }).enabled, false);
  assert.throws(() => createGoogleAuth({ env: { GOOGLE_AUTH_ENABLED: 'true' } }), /explicit GOOGLE_ALLOWED_EMAILS/);
});

test('official Google verifier rejects altered signatures, wrong audience and issuer', async () => {
  const { privateKey, publicKey } = generateKeyPairSync('rsa', { modulusLength: 2048 });
  const client = new OAuth2Client({ clientId: 'test-client' });
  client.getFederatedSignonCertsAsync = async () => ({ certs: { test: publicKey.export({ type: 'spki', format: 'pem' }) } });
  const encode = value => Buffer.from(JSON.stringify(value)).toString('base64url');
  const issue = changes => {
    const timestamp = Math.floor(Date.now() / 1000);
    const content = encode({ alg: 'RS256', kid: 'test' }) + '.' + encode({ iss: 'https://accounts.google.com', aud: 'test-client', sub: 'owner', iat: timestamp, exp: timestamp + 3600, ...changes });
    return content + '.' + sign('RSA-SHA256', Buffer.from(content), privateKey).toString('base64url');
  };
  const valid = issue({});
  assert.equal((await client.verifyIdToken({ idToken: valid, audience: 'test-client' })).getPayload().sub, 'owner');
  await assert.rejects(client.verifyIdToken({ idToken: issue({ aud: 'other-client' }), audience: 'test-client' }));
  await assert.rejects(client.verifyIdToken({ idToken: issue({ iss: 'https://evil.example' }), audience: 'test-client' }));
  const parts = valid.split('.'); parts[1] = encode({ sub: 'attacker' });
  await assert.rejects(client.verifyIdToken({ idToken: parts.join('.'), audience: 'test-client' }));
});

test('callback binding, allowlist, nonce, expiry, session lifecycle and CSRF guards', async () => {
  let clock = Date.now(), nonce, claimsOverride = {}, failVerification = false, exchanges = 0;
  const origin = 'https://internal.example';
  const env = { GOOGLE_AUTH_ENABLED: 'true', PUBLIC_ORIGIN: origin, GOOGLE_CLIENT_ID: 'test-client', GOOGLE_CLIENT_SECRET: 'test-secret', GOOGLE_ALLOWED_EMAILS: 'owner@example.com' };
  const google = createGoogleAuth({ env, now: () => clock, makeClient: options => {
    const actual = new OAuth2Client(options);
    return {
      generateCodeVerifierAsync: () => actual.generateCodeVerifierAsync(),
      generateAuthUrl: params => { nonce = params.nonce; return actual.generateAuthUrl(params); },
      getToken: async options => { exchanges++; assert.ok(options.codeVerifier.length >= 43); assert.equal(options.redirect_uri, origin + '/auth/google/callback'); return { tokens: { id_token: 'provider-test-token' } }; },
      verifyIdToken: async ({ audience }) => { assert.equal(audience, env.GOOGLE_CLIENT_ID); if (failVerification) throw new Error('invalid provider token'); return { getPayload: () => ({ sub: 'owner-subject', email: 'owner@example.com', email_verified: true, exp: clock / 1000 + 3600, nonce, ...claimsOverride }) }; },
    };
  } });
  const app = express(); app.use(google.router); app.get('/private', google.guard, (_req, res) => res.send('private content'));
  const server = app.listen(0, '127.0.0.1');
  await new Promise(resolve => server.once('listening', resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  const request = (url, options = {}) => fetch(base + url, { ...options, redirect: 'manual' });
  const cookieOf = (res, prefix) => res.headers.getSetCookie().find(c => c.startsWith(prefix + '='))?.split(';')[0];
  async function begin() {
    const response = await request('/auth/google?return=%2Ftools%2Fatlas%2F');
    assert.equal(response.status, 303);
    const authorization = new URL(response.headers.get('location'));
    assert.equal(authorization.origin, 'https://accounts.google.com');
    assert.equal(authorization.searchParams.get('code_challenge_method'), 'S256');
    assert.equal(authorization.searchParams.get('scope'), 'openid email');
    return { state: authorization.searchParams.get('state'), cookie: cookieOf(response, '__Host-boss_oauth') };
  }
  const callback = (tx, state = tx.state) => request('/auth/google/callback?code=test-code&state=' + encodeURIComponent(state), { headers: { cookie: tx.cookie } });
  try {
    assert.equal((await request('/private')).status, 401);
    let tx = await begin();
    assert.equal((await callback(tx, 'wrong-state')).status, 400);
    assert.equal(exchanges, 0);
    assert.equal((await callback(tx)).status, 400, 'transaction is single use');
    tx = await begin();
    assert.equal((await request('/auth/google/callback?code=test-code&state=' + tx.state)).status, 400, 'state alone cannot replace browser binding');
    assert.equal((await callback(tx)).status, 303);

    for (const overrides of [{ email: 'other@example.com' }, { email_verified: false }, { nonce: 'wrong-nonce' }, { exp: 1 }, { sub: '' }]) {
      claimsOverride = overrides; tx = await begin(); assert.equal((await callback(tx)).status, 403);
    }
    claimsOverride = {}; failVerification = true; tx = await begin(); assert.equal((await callback(tx)).status, 400);
    failVerification = false;
    tx = await begin(); clock += 6 * 60 * 1000; assert.equal((await callback(tx)).status, 400, 'expired sign-in rejected');
    tx = await begin(); const response = await callback(tx);
    assert.equal(response.status, 303); assert.equal(response.headers.get('location'), '/tools/atlas/');
    const session = cookieOf(response, '__Host-boss_session');
    assert.ok(session);
    assert.match(response.headers.getSetCookie().join(';'), /HttpOnly; Secure; SameSite=Lax/);
    assert.ok(!session.includes('owner') && !session.includes('provider-test-token'));
    assert.equal((await request('/private', { headers: { cookie: session } })).status, 200);
    assert.equal((await request('/private', { headers: { cookie: session + 'tampered' } })).status, 401);
    assert.equal((await request('/auth/logout', { method: 'POST', headers: { cookie: session, origin: 'https://evil.example' } })).status, 403);
    assert.equal((await request('/auth/logout', { method: 'POST', headers: { cookie: session, origin } })).status, 303);
    assert.equal((await request('/private', { headers: { cookie: session } })).status, 401);
    tx = await begin(); const next = await callback(tx); clock += 9 * 60 * 60 * 1000;
    assert.equal((await request('/private', { headers: { cookie: cookieOf(next, '__Host-boss_session') } })).status, 401, 'session expires');
  } finally { server.closeAllConnections(); await new Promise(resolve => server.close(resolve)); }
});
