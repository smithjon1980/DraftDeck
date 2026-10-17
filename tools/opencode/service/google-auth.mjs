import express from 'express';
import { randomBytes } from 'node:crypto';
import { OAuth2Client } from 'google-auth-library';

const sessionCookie = '__Host-boss_session';
const transactionCookie = '__Host-boss_oauth';
const sessionLifetime = 8 * 60 * 60 * 1000;
const transactionLifetime = 5 * 60 * 1000;
const random = () => randomBytes(32).toString('base64url');
const cookie = (name, value, age) => `${name}=${value}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=${age}`;
function readCookie(req, name) {
  const items = String(req.headers.cookie || '').split(';').map(part => part.trim()).filter(part => part.startsWith(name + '='));
  return items.length === 1 ? items[0].slice(name.length + 1) : '';
}
export function safeReturn(value) {
  if (typeof value !== 'string' || value.length > 2000 || !value.startsWith('/') || /[\\\x00-\x20]/.test(value)) return '/tools/';
  try {
    const url = new URL(value, 'https://internal.invalid');
    const decoded = decodeURIComponent(value);
    if (url.origin !== 'https://internal.invalid' || decoded.startsWith('//') || /[\\\x00-\x20]/.test(decoded) || url.pathname.startsWith('/auth') || url.pathname === '/login') return '/tools/';
    return url.pathname + url.search;
  } catch { return '/tools/'; }
}

export function createGoogleAuth({ env = process.env, now = Date.now, makeClient = options => new OAuth2Client(options) } = {}) {
  const enabled = env.GOOGLE_AUTH_ENABLED === 'true';
  const origin = env.PUBLIC_ORIGIN;
  const allowed = new Set(String(env.GOOGLE_ALLOWED_EMAILS || '').split(',').map(s => s.trim().toLowerCase()).filter(Boolean));
  if (enabled && (!origin || !origin.startsWith('https://') || new URL(origin).origin !== origin || !env.GOOGLE_CLIENT_ID || !env.GOOGLE_CLIENT_SECRET || !allowed.size)) {
    throw new Error('Google login requires PUBLIC_ORIGIN, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET and explicit GOOGLE_ALLOWED_EMAILS');
  }
  const redirectUri = enabled ? origin + '/auth/google/callback' : null;
  const client = enabled ? makeClient({ clientId: env.GOOGLE_CLIENT_ID, clientSecret: env.GOOGLE_CLIENT_SECRET, redirectUri }) : null;
  const sessions = new Map(), transactions = new Map();
  const router = express.Router();
  router.use((_req, res, next) => {
    res.set('Cache-Control', 'private, no-store');
    res.set('Referrer-Policy', 'no-referrer');
    res.set('X-Content-Type-Options', 'nosniff');
    next();
  });
  function prune(map) { for (const [key, value] of map) if (value.expires <= now()) map.delete(key); }
  function authenticate(req) {
    if (!enabled) return null;
    const key = readCookie(req, sessionCookie), session = sessions.get(key);
    if (!session || session.expires <= now() || !allowed.has(session.email)) { if (key) sessions.delete(key); return null; }
    return { email: session.email, subject: session.subject };
  }
  function guard(req, res, next) {
    const identity = authenticate(req);
    if (!identity) return res.sendStatus(401);
    if (!['GET', 'HEAD', 'OPTIONS'].includes(req.method) && req.headers.origin !== origin) return res.sendStatus(403);
    req.googleIdentity = identity;
    next();
  }
  router.get('/login', (req, res) => {
    const returnTo = encodeURIComponent(safeReturn(req.query.return));
    res.set('Content-Security-Policy', "default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'");
    res.type('html').send(`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sign in — BOSS</title><style>body{margin:0;color:#000;background:#fff;font:18px Arial,sans-serif}main{max-width:540px;margin:64px auto;padding:24px;border-top:2px solid #000}h1{font-size:36px}p{line-height:1.6}a{color:#000;display:inline-block;margin:16px 0;padding:16px;border:1px solid #000;text-decoration:none}a:focus-visible{outline:3px solid #00BCEB;outline-offset:4px}small{display:block;line-height:1.5}</style></head><body><main><p>Bioscillate Operating System by Seven</p><h1>Sign in to your tools</h1>${enabled ? `<a href="/auth/google?return=${returnTo}">Continue with Google</a><small>Access is restricted to approved accounts.</small>${authenticate(req) ? '<form method="post" action="/auth/logout"><button type="submit">Sign out of Google session</button></form>' : ''}` : '<p>Google sign-in is awaiting configuration.</p>'}<p><a href="/auth/basic?return=${returnTo}">Use existing password</a></p></main></body></html>`);
  });
  router.get('/auth/google', async (req, res) => {
    if (!enabled) return res.status(503).send('Google sign-in is not configured. Use the existing password login.');
    prune(transactions);
    if (transactions.size >= 500) return res.status(429).send('Please try signing in later.');
    try {
      const { codeVerifier, codeChallenge } = await client.generateCodeVerifierAsync();
      const id = random(), state = random(), nonce = random();
      transactions.set(id, { state, nonce, codeVerifier, returnTo: safeReturn(req.query.return), expires: now() + transactionLifetime });
      res.append('Set-Cookie', cookie(transactionCookie, id, transactionLifetime / 1000));
      res.redirect(303, client.generateAuthUrl({ scope: ['openid', 'email'], state, nonce, code_challenge: codeChallenge, code_challenge_method: 'S256', prompt: 'select_account', access_type: 'online' }));
    } catch { res.status(503).send('Google sign-in could not start. Try again or use the existing password login.'); }
  });
  router.get('/auth/google/callback', async (req, res) => {
    if (!enabled) return res.sendStatus(503);
    const id = readCookie(req, transactionCookie), tx = transactions.get(id);
    transactions.delete(id);
    res.append('Set-Cookie', cookie(transactionCookie, '', 0));
    if (!tx || tx.expires <= now() || typeof req.query.state !== 'string' || req.query.state !== tx.state || typeof req.query.code !== 'string' || req.query.error) return res.status(400).send('Sign-in expired or could not be verified. Start again.');
    try {
      const { tokens } = await client.getToken({ code: req.query.code, codeVerifier: tx.codeVerifier, redirect_uri: redirectUri });
      if (!tokens.id_token) throw new Error('No identity token');
      // Google verifies signature, issuer, audience and token validity. Nonce and local authorization are checked here.
      const ticket = await client.verifyIdToken({ idToken: tokens.id_token, audience: env.GOOGLE_CLIENT_ID });
      const claims = ticket.getPayload();
      const email = String(claims?.email || '').toLowerCase();
      if (!claims?.sub || claims.nonce !== tx.nonce || claims.email_verified !== true || !allowed.has(email) || !Number.isFinite(claims.exp) || claims.exp * 1000 <= now()) return res.status(403).send('This Google account is not authorized.');
      prune(sessions);
      if (sessions.size >= 500) return res.status(429).send('Please try signing in later.');
      // Replace an existing session. Provider tokens are never placed in cookies or retained.
      sessions.delete(readCookie(req, sessionCookie));
      const key = random();
      sessions.set(key, { email, subject: claims.sub, expires: now() + sessionLifetime });
      res.append('Set-Cookie', cookie(sessionCookie, key, sessionLifetime / 1000));
      res.redirect(303, tx.returnTo);
    } catch { res.status(400).send('Google sign-in could not be verified. Start again.'); }
  });
  router.post('/auth/logout', guard, (req, res) => {
    sessions.delete(readCookie(req, sessionCookie));
    res.append('Set-Cookie', cookie(sessionCookie, '', 0));
    res.redirect(303, '/login');
  });
  router.get('/auth/me', guard, (req, res) => res.json(req.googleIdentity));
  return { router, enabled, authenticate, guard };
}
