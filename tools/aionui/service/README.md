# Private BOSS AionUi pilot

Pinned AionUi source c140550d04e44f3d6f8a9830b40ae56e4689a977 (2.2.2); pinned AionCore v0.2.2 archive with a checked SHA-256; OpenCode CLI 1.19.3. No upstream source modifications. Upstream Apache notices are retained in the image. The upstream desktop Dockerfile is not used.

The public Node gateway protects every app/API/asset/stream/WebSocket route. `/health` is public and reports backend readiness only. Owner Google sign-in is performed by the existing BOSS gateway, followed by a 60-second, state-bound, one-use code exchanged server-to-server. The pilot rechecks the explicit owner email and creates a Secure/HttpOnly/SameSite=Lax session. No Google tokens or client secret enter this service. A restart requires signing in again.

AionCore runs on loopback without `--local`. Its own password is generated into a mode-0600 file on the volume and provisioned through the official CLI's stdin. The authenticated gateway uses its backend token internally; the browser receives no backend password/token. Child processes do not inherit the BOSS handoff secret. CSRF and WebSocket origin checks apply at the public boundary. This is an owner-only staging pilot, not a multi-user platform or a completed security audit.

`/pilot` offers the workspace, the existing OpenCode status, and `/deck`. The deck supports native text editing with explicit server saves, serialized writes, an exact revision precondition, and atomic replacement. Save does not regenerate PDF or JSON. Artwork is raster and separate from text. The pilot does not establish arbitrary visual slide layout editing. Seed content is uploaded once using a distinct machine-authorized endpoint and is deliberately absent from this public repository.

The 500 MB `/data` volume holds state, workspace, logs, cache, generated backend credential and OpenCode config/share. Install/provider operations may need more capacity; no model credentials are preconnected. No claim of a successful inference task follows from installation or a health response.

Required environment: `BOSS_AUTH_ISSUER` (existing BOSS HTTPS origin), `BOSS_AIONUI_BRIDGE_SECRET` (32+ random characters), `GOOGLE_ALLOWED_EMAIL` (owner), `PUBLIC_ORIGIN` (pilot HTTPS origin; or Railway public-domain environment), `PORT=8080`. Existing BOSS needs the same bridge secret and `BOSS_AIONUI_ORIGIN` set to the exact pilot origin. Credentials belong in Railway variables only.

Local verification: `node --test tests/pilot.mjs` covers handoff/replay/expiry, owner restriction, anonymous and cross-origin rejection, stale saves and restart persistence. Existing Google and slide tests are run separately. The preceding upstream evaluation built the actual frontend and verified authenticated backend/proxy endpoints; its remote NIC test failed in this environment. Browser/mobile editing and real Google handoff require a live signed-in test. Deployment and live-test evidence must be recorded separately.
