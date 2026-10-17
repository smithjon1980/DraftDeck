# Google sign-in activation

The implementation is ready for an owner-created Google OAuth client. It stays disabled unless `GOOGLE_AUTH_ENABLED=true`. Current Basic authentication and the separate MCP bearer token continue to work.

## Register the Google application

1. Open [Google Auth Platform](https://console.cloud.google.com/auth/overview) in the Google account that will own the application. Select an existing project or create `BOSS Internal Tools`.
2. Configure branding as **BOSS Internal Tools**. For a personal Gmail account use an External audience. If the app remains in Testing, add the exact intended account as a test user. Request only `openid` and `email` for this login; no Drive, Gmail, Kaggle or Cloud administration access is needed.
3. Create a **Web application** OAuth client. Register this exact authorized redirect URI:

   `https://boss-opencode-production.up.railway.app/auth/google/callback`

4. Store the client ID and secret directly in the Railway service variables below. Do not put them in GitHub, a notebook, HTML, or chat. The login uses the server authorization-code flow, so no browser JavaScript origin registration is needed for this implementation.

## Railway variables

Service: **BOSS OpenCode**, production, project **skillful-liberation**.

| Variable | Value |
| --- | --- |
| `GOOGLE_CLIENT_ID` | Web application's client ID |
| `GOOGLE_CLIENT_SECRET` | Web application's client secret |
| `GOOGLE_ALLOWED_EMAILS` | Exact verified Google email allowed to enter; comma-separated only if additional accounts are explicitly authorized |
| `GOOGLE_AUTH_ENABLED` | `true`, after all required settings above exist |
| `PUBLIC_ORIGIN` | Existing value: `https://boss-opencode-production.up.railway.app` |

No account spelling is assumed. Enter the exact email displayed for the Google account you intend to use. An email hint or the account currently signed into Railway does not substitute for this explicit access decision. Do not use `*` or a whole Gmail domain as the allowlist.

Keep `OPENCODE_SERVER_PASSWORD` and `BOSS_MCP_TOKEN`. Google sign-in provides a browser session; the gateway supplies the backend password to OpenCode on the server side. The MCP bearer credential remains separate and is never returned to the browser.

## Session and access behavior

- Google verifies identity-token signatures, issuer, audience and token validity using its official Node library. The app checks the nonce, verified email, nonempty subject, expiry and exact allowlist.
- Sign-in transactions use PKCE S256, a random state and nonce, plus a five-minute browser-binding cookie. Callback state alone cannot admit a session. Transactions are single use.
- Session cookies are opaque, Secure, HttpOnly, SameSite=Lax and scoped to the host. Provider access/refresh/identity tokens are not stored in browser cookies or retained as sessions.
- One service instance holds a bounded in-memory session store. Sessions expire after eight hours, logout revokes the session, and a service restart signs users out. For multiple replicas, replace the memory store with a shared server-side session store before scaling.
- Cookie-authenticated writes and WebSocket connections require the configured same origin. Native OpenCode HTTP and WebSocket proxy requests receive the backend authorization header server-side.
- Basic login remains as an explicit recovery path. A browser that has cached Basic credentials can still use that path after ending a Google session. Review removal only after real Google access is verified.

## Acceptance before declaring Google sign-in live

1. Deploy the Google-login code with all settings configured. Confirm Railway SUCCESS and `/health` 200.
2. Open `/login` in a fresh browser session and use Continue with Google.
3. Confirm the approved account can access the hub, full atlas, artifact desk and OpenCode browser APIs without a Basic-password prompt. Check actual downloads and OpenCode's live connection.
4. Confirm another Google account is denied. Check logout and expiry. Preserve Basic recovery until these checks pass.

Tests exercise the application callback/session controls with a simulated Google token exchange. They do not establish that a real Google client, consent screen or account has been configured. Real account sign-in remains pending until the owner completes Google registration.

Primary references: [Google OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect), [Google's Node authentication library](https://github.com/googleapis/google-auth-library-nodejs).
