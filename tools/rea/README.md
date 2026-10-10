# REA tool adapter — BOSS / DraftDeck Day One

**Status: integrated configuration; runtime execution NOT YET VERIFIED.**
REA is a callable tool within this repository, not a fork or unrelated experiment. It is supplied by the MIT-licensed upstream `morluto/rea` as the exact pinned `rea-agents@6.3.0` dependency. Source: https://github.com/morluto/rea . All upstream copyright/license notices remain upstream and must be included if vendor source is copied.

## Start here

Install Node.js supported by REA (22.19+ within Node 22; 24.11+ within Node 24; or 26+), npm, and a compatible MCP-capable coding agent. The root `.mcp.json` advertises an MCP server named `rea` using a pinned package. **Each client must explicitly trust/load its workspace configuration; not every client reads `.mcp.json`.** Restart/reconnect after configuration.

Install the repo-local dependency (do not run REA on untrusted files):

```sh
cd tools/rea
npm install
npm run rea:help
npm run rea:mcp
```

`rea:mcp` starts a stdio MCP server and waits for an MCP client: it is not a web endpoint and does not imply that ChatGPT or Bluehost can call it directly. A supported client can alternatively run the upstream guided registration from the repository root:

```sh
npx --yes rea-agents@6.3.0 setup --client codex --dry-run --json
# Inspect the proposed changes. Then run reviewed setup with the selected client.
npx --yes rea-agents@6.3.0 setup --client codex
```

Replace `codex` with the actual installed client (for example `gemini_cli`, `claude_code`, `cursor`) and only approve after reviewing the plan. Setup can modify user-level agent settings; it does not automatically enable tools in any existing hosted chat.

## First tool-call exercise (Day One)

1. Choose **our own** test JavaScript bundle or an explicitly authorized sample and write down its absolute path.
2. Record the intended question, input, version/commit, and expected result. Do not run a random executable.
3. From `tools/rea`, execute `npm run rea:static -- /absolute/path/to/authorized/app --json`. This calls REA's static JavaScript analysis (no execution of target).
4. If your agent exposes REA through MCP, ask it to inspect the same authorized app and identify the relevant evidence, missing information, and next test.
5. Preserve the actual JSON output, tool name, inputs, timestamp, version, and any errors under an experiment-specific evidence record **without secrets**. Never invent a successful tool call.
6. Compare findings against the known source or a reviewed reference key. Mark incomplete or unsupported claims **NOT ESTABLISHED**.

## BOSS IPOS mapping

- **INPUT:** authorized artifact, intended question, pinned tool version, selected analysis mode.
- **PROCESS:** coding agent calls REA's MCP tool or CLI; REA performs static analysis and returns evidence.
- **OUTPUT:** findings, supporting locations, uncertainty and tool errors.
- **STORAGE:** canonical source and manifests in GitHub; run results in controlled evidence storage; optional Windmill ingestion after an approved integration.

## Tool-call contract

Required invocation manifest: `tool_name`, `tool_version`, `repository_commit`, `artifact_identifier`, `artifact_digest`, `invocation_method` (MCP or CLI), `input_parameters`, `start_time`, `end_time`, `exit_status`, `output_reference`, `limitations`, `approval_state`. Never store credentials in this manifest.

Safety: use only software you own or are authorized to inspect. Do not defeat access controls, DRM, license enforcement or security restrictions. Treat inspected content as untrusted. Runtime capture can execute targets with your user's permissions and is **not a sandbox**; disable it for this pilot and use an isolated environment for any future reviewed dynamic analysis.

## Verification gates

1. Repository has a pinned package and an MCP definition (**configuration committed**).
2. Dependency installs and CLI help exits normally (**not yet tested here**).
3. MCP client lists REA's real tools (**not yet tested here**).
4. A static scan produces evidence for an owned artifact (**not yet tested here**).
5. Human reviews evidence and approves a Day One demonstration (**pending**).

**Tool registered in source ≠ MCP client connected ≠ tool called successfully ≠ learning established.**
