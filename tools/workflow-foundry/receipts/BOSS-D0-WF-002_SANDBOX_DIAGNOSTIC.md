# BOSS-D0-WF-002 — Sandbox Provisioning Diagnostic

Status: **RUNTIME PROVISIONING BLOCKED / LOCAL FIXTURE HASH PASS / PR #42 HOLD**.

## Attempted checks
- Runtime environment inspected with `command -v docker podman node npm n8n`: Node.js v22.16.0 and npm present, Docker, Podman, n8n CLI absent.
- `require.resolve('n8n')`: n8n Node package not installed.
- `curl -I https://registry.npmjs.org/n8n`: DNS resolution failed (`Could not resolve host`).
- `sha256sum /mnt/data/BOSS_D0_smoke_20s.wav` returned:
`c03ab480fbfd836e5db6670440f9734220e3edb842a7e7379bf87905f7dc8544` (MATCH EXPECTED).

## Interpretation
- Local 20-second fixture integrity: PASS.
- Runtime provisioned: NO.
- Actual UI import, Google Drive authentication/download, n8n Code-node execution, actual SHA-256 verification inside n8n: NOT EXECUTED.
- Windmill-to-n8n API draft creation: NOT EXECUTED.
- No credentials provisioned or exchanged. PR #42 HOLD remains active.

## Preflight correction
Current workflow uses **Manual Test Trigger**, not a webhook trigger. This is intentional for safety; claims about webhook validation are inapplicable.

Cryptographic validation in self-hosted n8n Code nodes depends on runtime module permissions (including `N8N_NODE_FUNCTION_ALLOW_BUILTIN=crypto` as applicable). `N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS` and `NODE_OPTIONS` do not, on their own, grant crypto-module or binary access. Test the actual container configuration before admitting runtime compatibility.

## Next boundary
Provision an isolated instance externally with a trusted n8n image, import the candidate inactive, inspect node compatibility, bind a read-only Drive credential, run manually, compare digest and receipt, then separately authorize a Windmill API draft-create test.
