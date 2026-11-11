# Windmill · BOSS Tool Readiness Observatory (Candidate v0.1)

**Purpose:** Re-run actual environmental and REA CLI readiness tests, then ask several LLMs to interpret the *same frozen evidence record*. Repeat for each new open-source tool, daily, weekly or monthly as approved.

**State:** SOURCE COMMITTED; Windmill deployment NOT CONNECTED; runtime execution NOT VERIFIED.

## Existing project context
REA adapter: `tools/rea/`; PR #39 (Day Zero); sample `examples/interactive-checklist/index.html`. This adds an independent Windmill path to the BOSS Tool Readiness Gateway without changing canonical doctrine.

## Initial trial — keep dimensions separate
1. Deploy `rea_readiness.py` as Windmill Python script on a worker with subprocess access. Mount a clean, pinned checkout of DraftDeck at the designated path. Do not give the job production credentials.
2. First run `main(repository_root="/workspace/DraftDeck", execute_cli=False)`: report environment, versions, source digests, and explicit NOT_EXECUTED flags.
3. Provision approved pinned dependencies on a disposable worker. Then `execute_cli=True` to inspect **our own checklist**. Check the real exit code and preserve raw stdout/stderr.
4. MCP gate is not implemented in this initial script. A successful CLI scan is NOT a successful MCP call. Build a separately reviewed MCP client handshake, tools/list and approved read-only invocation before marking that gate verified.
5. Route immutable output JSON to secure run storage and database; retain original artifact and run ID.

## Multi-model interpretation flow (subsequent Windmill flow)
- Freeze an evidence packet generated from a single *actual* execution run; hash and version it.
- Select configured provider resource (Windmill supports multiple model providers), model identifier, prompt version, repeat index and visible parameters. Keep secrets in Windmill Resources.
- Run the same analysis prompt against each model, independently; never mix model responses with tool execution logs.
- Preserve **verbatim** responses, provider response metadata, provider errors, effective displayed versions and timestamps.
- Generate blinded copies and score evidence discipline, diagnostic quality, instruction fidelity, and actionability independently. Human reference key and reviewer adjudication remain separate.
- Produce a status-change summary (previous run vs current), mark UNKNOWN/NOT_EXECUTED/FAILED distinctly. Publish only approved reports.

## Database schema
Use `tool_observatory_schema.sql` in a workspace-scoped PostgreSQL database. Windmill Data Tables or a configured Postgres resource can host relational records; initialize schema with authorization. Never store raw API keys.

## Suggested cadence (Windmill Schedules)
- **On demand:** first evaluation of any new tool or new version.
- **Daily:** check registered critical integration's lightweight read-only readiness and drift; no destructive runtime capture.
- **Weekly:** bounded CLI/MCP tests on owned fixtures, version & evidence comparisons.
- **Monthly:** human-reviewed multi-model re-evaluation, rubric agreement and curriculum amendment proposals.

A schedule is a planned capability, not an active one. Create in Windmill and capture schedule/run IDs after connection. Tool output and LLM judgment are separate assessment tracks. Daily checks should skip expensive multi-LLM calls unless change detection or approved evaluation cadence warrants them.
