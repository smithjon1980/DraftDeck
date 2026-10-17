# BOSS OpenCode service candidate

One service supplies the OpenCode browser interface at `/` and a Streamable HTTP MCP bridge at `/mcp`. Phone and computer browsers use the same workspace and sessions. ChatGPT can call the bridge after an authenticated custom connection is supported and configured in the user's client.

The deployed runtime is pinned to `opencode-ai` 1.19.3, the version verified in the initial trial. The separately pinned OpenCode upstream source in `../upstream.json` is a newer development snapshot and is not built by this Dockerfile. This service is an integration around OpenCode's public API, not a modified OpenCode distribution.

## Interface and credentials

| Route | Purpose | Authentication |
| --- | --- | --- |
| `/` | OpenCode web interface and API | HTTP Basic; default username `opencode` |
| `/mcp` | Four OpenCode tools for ChatGPT or another MCP client | Bearer token |
| `/health` | Boolean backend readiness | Public; no account details |

The service refuses startup unless `OPENCODE_SERVER_PASSWORD` has at least 24 characters, `BOSS_MCP_TOKEN` has at least 32 characters, and their values differ. Set both through the host's secret settings. Do not put credentials in GitHub or chat. `PUBLIC_ORIGIN` is the actual HTTPS origin of the deployment without a trailing slash. It restricts Host and Origin headers for authenticated routes; it is not a substitute for TLS termination.

OpenCode listens on a private loopback port. The gateway alone is exposed. It does not expose an arbitrary proxy target, a raw shell MCP tool, or API routes for changing stored credentials through MCP. The authenticated browser still has OpenCode's full user interface and API.

## Deploy on Railway

1. Use the reviewed DraftDeck branch containing this directory. Create a service from that repository with root directory `tools/opencode/service`; select its Dockerfile.
2. Attach a persistent volume at `/data`. Confirm the runtime user (`node`, UID 1000 in this image) can write to it. The service saves workspace files and XDG configuration, credentials, cache, and session state there. Back up this volume as operational state.
3. Set separate generated values for `OPENCODE_SERVER_PASSWORD` and `BOSS_MCP_TOKEN` in Railway's secret settings. Set `XDG_CONFIG_HOME=/data/config`, `XDG_DATA_HOME=/data/share`, and `XDG_CACHE_HOME=/data/cache` if the host overrides image settings.
4. Generate an HTTPS domain. Set `PUBLIC_ORIGIN` to that exact HTTPS origin, then restart. Set the health check path to `/health`; route the host's assigned `PORT` to the service. The gateway reads `PORT` directly.
5. Open the domain in a browser and sign in with `opencode` and the web password. Connect the chosen model provider using OpenCode's supported sign-in UI. No provider is selected or billed by this source package.
6. Connect Kaggle using its supported OAuth or API-token method. A remote OAuth flow may require a reachable callback; do not assume a localhost callback works from a phone. Complete private notebook access verification before describing Kaggle as connected to the account.
7. Configure the actual deployed `/mcp` HTTPS URL as a custom MCP connection using bearer/API-key authentication where the host client supports it. Store the bearer token in the client's credential field, not a URL or prompt. If the ChatGPT client cannot accept this auth mode or custom connections, use OpenCode's browser interface until a compatible connection is available.

Railway account connection, service provisioning, volume configuration, Docker build, HTTPS access, and phone verification must be tested on the destination host. Local checks do not establish deployment success. Hosting can incur charges; inspect the existing account and service plan before provisioning.

## Local verification

With Node/npm installed:

```sh
npm ci
npm test
```

The smoke check starts a real OpenCode instance with temporary state, verifies unauthenticated rejection, separate web/MCP credentials, cross-origin rejection, SDK-based MCP initialization/tool discovery, backend health, and session creation/readback without invoking a model. Prompt submission with a connected model, permission approval through the browser, and Kaggle downloads need separate live account checks.

For normal local use, set the two secrets in the process environment and choose a writable `BOSS_WORKSPACE`. `PUBLIC_ORIGIN` can be omitted for local terminal-client testing; browser requests with an Origin header are rejected until the real HTTPS origin is configured. XDG variables should point to persistent private directories. Run `npm start`.

## MCP operations

`opencode_status` returns backend health, MCP states, and connected provider IDs. It explicitly leaves private Kaggle access unverified. `opencode_sessions` lists workspace sessions. `opencode_prompt` accepts an explicit work order and returns a new session ID after asynchronous admission; this is not a completion receipt. It can execute tools and modify workspace files, subject to OpenCode's configured permissions. `opencode_session` reads status and recent text for progress review; idle status alone does not prove success. There is no automatic retry of prompt submission because that can duplicate work.

The initial config asks before shell commands, file edits, or unspecified Kaggle operations. Read-only notebook inspection and existing-output downloads are allowed. Permission prompts are handled in the authenticated OpenCode interface; this bridge does not approve them. These controls do not establish sandbox isolation or publication approval.

## First work order

Retrieve existing outputs for `smithjon1980/boss-audio-003-kaggle-setup-repair`; do not regenerate the audio. Download `BOSS_AUDIO_003_RESULTS.zip` into persistent workspace storage, check archive integrity, and verify the three WAV files against recorded hashes. Listening and wording review remain separate from file completion. Do not claim success from a connection indicator or fluent generated response.

## Current boundary

This service does not provide OAuth authorization for ChatGPT, public artifact sharing, a user-friendly download portal, repository synchronization, background scheduling, or production qualification. The initial persistent workspace is empty; clone DraftDeck there separately when code execution against the repository is needed. Keep the OpenCode MIT notice when copying or redistributing the dependency.
