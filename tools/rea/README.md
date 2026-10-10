# REA tool adapter — BOSS / DraftDeck Day Zero

**Status: repository MCP configuration committed; live tool execution NOT YET VERIFIED.**

REA (Reverse Engineer Anything) is an optional, bounded *Day Zero* investigation instrument. The aim is to **audit the evidence chain and solve for an unknown within IPOS**, not to master professional reverse engineering. The upstream `morluto/rea` library is MIT licensed. This adapter pins `rea-agents@6.3.0` rather than copying its source.

## Seven-stage learning progression

1. **Observe:** With an approved, locally available DraftDeck-owned sample, describe an observable feature or failure; do not guess why it happens.
2. **Describe:** Map Input (selected HTML/JS), Process (browser scripting and any tool inspection), Output (interactive checklist and its reported behavior), Storage (source/version and saved evidence).
3. **Diagnose:** Identify Scenario B (process unknown) or Scenario C (unsatisfactory output). Distinguish KNOWN, INFERRED, UNKNOWN, and NOT ESTABLISHED.
4. **Hypothesize:** Write two plausible explanations, explaining which observable evidence would help distinguish them.
5. **Test:** Start with static inspection of our own `examples/interactive-checklist/index.html`. If a compatible agent is connected, ask it to invoke REA and return the exact tool and evidence references. Do not execute untrusted programs.
6. **Measure:** Independently evaluate the *tool/system evidence* (what was actually inspected) and the *learner's audit* (whether their classification was accurate). Do not mark unsupported findings as verified.
7. **Document:** Save invocation parameters, output, evidence references, unknowns, and human review decision separately from the production source.

### Two participation paths

**A. Manual no-installation path (default beginner experience):** Open the GitHub source for `examples/interactive-checklist/index.html` and observe the existing checklist in a browser if available. Identify the inputs, process clues (event listeners, DOM updates), outputs (progress and copied text), and what cannot be determined from the evidence provided. Fill in the IPOS worksheet and Evidence Chain Audit. Learners need no Node installation, MCP connection, or programming skills.

**B. Optional live tool-call demonstration (instructor/advanced participant):** An instructor or equipped learner uses a compatible coding agent that can access a local REA MCP server and an authorized test asset. This is a live demonstration of an AI calling an external tool—not a requirement for finishing Day Zero.

## Running the integrated tool (optional)

Requires Node.js 22.19+ (Node 22), 24.11+ (Node 24), or Node 26+ and npm; an MCP-capable agent for tool calling. A root `.mcp.json` defines `rea` using a pinned package, but **not every client loads that file** and a server definition alone is not a live connection.

```sh
cd tools/rea
npm install
npm run rea:help
# Static scan of the OWNED sample; run from tools/rea
npm run rea:static -- ../../examples/interactive-checklist --json
```

For MCP configuration in a supported local client (example: Codex CLI), first preview the changes from the repository root:
```sh
npx --yes rea-agents@6.3.0 setup --client codex --dry-run --json
# Review the change plan, then choose whether to apply:
npx --yes rea-agents@6.3.0 setup --client codex
```
Use the relevant client identifier if different; restart/reconnect the client. `npm run rea:mcp` starts a stdio server awaiting a compatible client, not a publicly accessible API. Hosted ChatGPT and Bluehost All-Access do not become connected merely because this configuration is committed.

**Before reporting success:** record the precise MCP tool name advertised by the live client, its input schema, actual arguments, response, timestamps, and errors. A CLI static-analysis success is *not* proof of MCP tool calling.

## Evidence Chain Audit

Record the following **system-level** observations separately from **learner performance**:
- Source availability: available / unavailable / not established
- Retrieval: relevant material surfaced / partly surfaced / not surfaced / not applicable
- Interpretation: accurate / partly accurate / inaccurate / not applicable
- Citation/evidence support: supports claim / partly supports / does not support / no citation to assess
- Uncertainty calibration: appropriate / overconfident / excessively hedged / not applicable

If a source is unavailable, do not count downstream checks as failures when they cannot be assessed. Judge learner performance against a reviewed reference key; a flawed tool response may be correctly identified by the learner.

## IPOS evidence manifest

Store `tool_name`, `tool_version`, `repository_commit`, `artifact_identifier`, `artifact_digest`, `invocation_method` (MCP/CLI/manual), `input_parameters`, `start_time`, `end_time`, `exit_status`, `output_reference`, `limitations`, `reviewer`, `approval_state`. Do not store secrets. Preserve originals and hashes before producing derived interpretations.

## Safety and release conditions

Use only owned or explicitly authorized software. No DRM bypass, license circumvention, or unauthorized access. Treat all inspected content as untrusted. Runtime capture may execute target software with your privileges: **REA is not a sandbox**. Keep dynamic execution disabled for this Day Zero exercise.

Verification gates:
1. Repository configuration exists — **committed in this PR**.
2. Dependency install / CLI help — **not yet independently verified**.
3. REA MCP tool listed by a connected agent — **not yet verified**.
4. Static scan of the safe checklist asset succeeds — **not yet verified**.
5. Learner evidence audit and human review — **pending**.

**Tool declared ≠ tool connected ≠ tool invoked ≠ evidence verified ≠ learning established.**

Day One retains formal workflow orchestration, API construction, and Windmill implementation as a separate later learning path.
