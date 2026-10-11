# BOSS-D0-WF-001 — Foundry Phase 1 PoC

**Status:** Source files committed; no Windmill or n8n installation, API credential provisioning, workflow import, test execution or deployment has occurred. PR #42 remains draft/HOLD.

## What exists
- `patterns/source-admission.pattern.json` — authenticated-source, hash comparison, fail-closed contract.
- `patterns/evidence-receipt.pattern.json` — receipt structure and clear separation of claims.
- `poc/n8n-source-admission.poc.json` — candidate inactive n8n workflow: Manual Trigger → Google Drive Download → Code Hash Check + static admission receipt.
- `windmill/compile_n8n_poc.py` — minimal Windmill Python compiler. Dry-run is default. n8n API draft creation requires `dry_run=False` AND `approved_for_draft_create=True`, and credentials supplied securely at execution time.

## PoC fixture
Drive file ID: `13DEHx7la7LrgAZ3vHLm46sTXiqV1f7nC`.
Expected SHA-256: `c03ab480fbfd836e5db6670440f9734220e3edb842a7e7379bf87905f7dc8544`.

## Important integration constraints
1. **No secrets in JSON**. Bind authorized n8n Google Drive credential in the n8n environment only. Windmill n8n API credential must come from Windmill secret/resource, not source-controlled JSON.
2. The candidate n8n Code node uses Node's `crypto` built-in via `require`; self-hosted n8n Code node environments may require `N8N_NODE_FUNCTION_ALLOW_BUILTIN=crypto`. Validate availability and hardening before importing.
3. The candidate Google Drive node's parameters and binary data helper are not yet verified against an installed n8n version. Perform a version-specific inactive import and non-production fixture run. No claim of production portability.
4. The receipt is constructed **after** byte inspection; the expected hash is not itself evidence of successful download. The output remains `SOURCE_ADMITTED_ONLY` even when integrity matches.
5. **Security gate still needed:** the compiler currently performs topology and fixture checks only; it is NOT a general security validator for arbitrary community workflow JSON. Do not pass untrusted upstream workflows to it directly. Build a strict canonical node-parameter allowlist and inspect all imported JS before allowing any deployment.
6. The upstream library is a discovery source, NOT an admitted pattern: https://github.com/Zie619/n8n-workflows . Pin upstream revision, scan node behavior and licenses before deriving production patterns.
7. Importing this workflow through n8n API requires n8n instance URL and a restricted API key. The PoC does not run the workflow or activate it.

## Protocol
Prompt → Select Pattern → Compile → Inspect → Test → Authorize → Deploy.
The current branch has reached **Candidate Compilation Source**, not runtime inspection or test. User authorization covers creating this PoC, not enabling automatic audio workflows.

## Suggested next operator check
Connect a test n8n instance, validate the JSON against its version, bind read-only Google Drive credentials, and import inactive. Do not connect production triggers.
