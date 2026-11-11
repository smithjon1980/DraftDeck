# BOSS OpenCode service candidate

The service supplies an OpenCode browser interface, an authenticated MCP bridge, and an artifact retrieval desk. It uses the existing Railway service and persistent `/data` volume. The runtime remains pinned to `opencode-ai` 1.19.3; the separately recorded upstream source snapshot is not built by this Dockerfile.

## Access

| Route | Purpose | Authentication |
| --- | --- | --- |
| `/` | OpenCode interface and native API | HTTP Basic, username `opencode` by default |
| `/artifacts` | Existing-output retrieval, verification records, individual WAV downloads | Same HTTP Basic credentials |
| `/mcp` | Six BOSS/OpenCode tools | Separate bearer token |
| `/health` | Boolean backend readiness | Public; no account details |

The native OpenCode browser API also uses `/mcp`. Requests authenticated with browser credentials are forwarded to that native API; bearer requests go to the BOSS bridge.

Set distinct `OPENCODE_SERVER_PASSWORD` (at least 24 characters) and `BOSS_MCP_TOKEN` (at least 32 characters) through the host's secret settings. `PUBLIC_ORIGIN` must equal the deployment's HTTPS origin without a trailing slash. Only the gateway port is public; OpenCode listens on loopback. Browser operations with a different Origin are rejected. These application controls do not establish operating-system sandbox isolation.

## Artifact retrieval

Open `/artifacts`, enter a Kaggle API token beginning with `KGAT`, then select **Retrieve and verify** for `smithjon1980/boss-audio-003-kaggle-setup-repair`. The worker requests the existing `BOSS_AUDIO_003_RESULTS.zip` through Kaggle's official MCP `download_notebook_output` tool. It never starts the notebook or invokes a model. A token entered in the portal stays in process memory until restart; it is not written to a file, browser storage, logs, URLs, or manifests. To retain it across restarts, the owner can set `KAGGLE_API_TOKEN` in Railway's secret settings instead.

Credential configured is not equivalent to private account access verified. Private retrieval must pass with the user's credential. The implementation accepts one supported HTTPS download address returned by Kaggle; it does not guess a file endpoint when the response is unsupported. Redirect hosts are checked, and the Kaggle credential is sent only to Kaggle's own hostname, never an external storage host.

The trial limits are 50 MB compressed archive, 100 MB total expanded contents, 32 MB per entry, and 5,000 entries. The worker checks available storage before admission, allows one active retrieval at a time, rejects unsafe paths, symlinks and encrypted archives, verifies entry CRCs, and hashes retained files. Archive buffers are bounded by the compressed limit. Only WAV entries are extracted to generated local names; the original ZIP is retained. Completed records and audio live in the persistent workspace's `artifacts` directory. No files are automatically deleted to make room.

For the named trial, all three WAVs must match the hashes printed in the completed `boss-audio-003-kaggle-setup-repair.ipynb` output supplied in the session on October 16, 2026. The expected filenames are `smoke_generated.wav`, `solo_generated.wav`, and `deep_dive_generated.wav`. Missing, duplicated, changed, or additional WAVs prevent verified completion. Other notebooks using the same package filename receive archive checks without this trial-specific comparison. CRCs and hashes establish file integrity and identity; listening, wording, and publication checks remain separate and pending.

A restart converts unfinished records to `INTERRUPTED` and preserves their evidence; it does not retry or claim delivery. Download and audio-player URLs use the same private browser credentials and support ordinary file transfer. They are not public share links or automatic ChatGPT file attachments.

## MCP tools

- `opencode_status`: backend health, MCP states, connected model provider IDs. Private Kaggle access remains explicitly unverified.
- `opencode_sessions`: recent sessions in the configured workspace.
- `opencode_prompt`: admit an explicit work order asynchronously; may execute tools and modify files, requires a connected model provider, and does not imply completion.
- `opencode_session`: inspect progress and recent text; idle does not mean success.
- `boss_artifacts`: list retained artifact jobs and authenticated download links.
- `boss_retrieve_audio`: start the bounded existing-output retrieval directly, without a model or OpenCode prompt. Requires a credential configured in the portal or host secrets.

The bridge does not approve OpenCode permission requests. Initial configuration asks before shell commands, edits, and unspecified Kaggle operations. It allows read-only notebook inspection and existing-output downloads. The authenticated browser exposes OpenCode's own interface and native APIs.

## Deployment

Use the repository's `tools/opencode/service` directory as the Docker build root. Mount persistent storage at `/data`, set the two service credentials, and set `PUBLIC_ORIGIN` after generating the HTTPS hostname. Railway passes `PORT`; the gateway reads it directly. The container entrypoint initializes volume directory ownership then runs as `node`.

The image defines `XDG_CONFIG_HOME=/data/config`, `XDG_DATA_HOME=/data/share`, and `XDG_CACHE_HOME=/data/cache`. The persistent workspace defaults to `/data/workspace`. Confirm backups and persistence on the destination host. No model provider is selected or billed by this package; connect the chosen provider through OpenCode before using prompt execution. Kaggle authentication for the artifact worker is separate from OpenCode's own Kaggle MCP configuration.

A custom ChatGPT MCP connection uses the deployed `/mcp` URL and bearer authentication where supported by the user's client. Plugin creation, server health, and tool discovery do not establish that the host has completed this authentication.

## Verification

Run `npm ci` and `npm test` with Node/npm and Python 3 installed. Tests start a real OpenCode process using isolated temporary state, exercise authenticated portal access and MCP discovery, inspect sessions, and verify ZIP extraction, corrupt-file rejection, unsafe-path rejection, source mismatch handling, and interrupted-record recovery. They do not invoke a model or access a user's Kaggle account. Test data and generated credentials are discarded afterward.

A live deployment additionally requires terminal Railway `SUCCESS`, public health and authentication checks, private Kaggle retrieval, actual downloads, and phone/browser inspection. Mark each limit explicitly. Keep the upstream MIT notice when copying or redistributing OpenCode. The PR does not merge itself or authorize publication of retrieved content.
