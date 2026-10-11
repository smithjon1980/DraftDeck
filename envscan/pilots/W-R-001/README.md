# BOSS ENVSCAN W-R-001 — Windmill ↔ Railway Synthetic Boundary

**Order:** BOSS-ENVSCAN-W-R-001  
**Status:** SOURCE CANDIDATE / NO WORKSPACES OR LIVE EXECUTION VERIFIED  
**Scope:** Four controlled tests of the Windmill–Railway service boundary. Neither n8n nor Bluehost is deployed as part of this pilot.

## Files
- `railway/server.js`: Node/Express test endpoint with bearer-token check, strict request validation, 1.5-second synthetic execution delay and sanitized receipt.
- `railway/package.json`: minimal Node dependency/start configuration.
- `windmill/execute_envscan_handshake.py`: four-probe Windmill Python job with explicit evaluations.

## Provisioning (not executed)
1. Confirm access and ownership of Windmill and Railway accounts/workspaces.
2. Deploy the `railway/` directory as a Railway service. Provide a random high-entropy `ENVSCAN_WINDMILL_SECRET` secret in Railway's service variables. Do not expose it in GitHub, code, logs or public documentation.
3. In Windmill, create an encrypted secret variable holding the matching value; bind it to `secret_token` when running the Python script. Supply the real Railway public HTTPS base URL in `base_url`, without the endpoint path.
4. Run the Windmill script manually. Confirm the four checks, matching `correlation_id` and Railway server log event; retain run ID, UTC time, deployed revision and sanitized output.
5. Repeat after correcting any missing credentials or network configuration. Approve recurring execution only after negative and positive controls pass.

## Test matrix
| Probe | Input | Expected result | Interpretation |
|---|---|---|---|
| Intruder | No bearer token | 401 | Rejected by endpoint |
| Malformed | Authorized but required correlation_id missing | 400 | Contract rejected before execution |
| Ghost | Closed local loopback port on Windmill runtime | Transport error (typically connection refused) | Transport failure handling demonstrated; **not** proof that Railway is down |
| Authorized | Valid bearer and schema | 200 + E9999_SYNTHETIC | Controlled, expected negative diagnostic outcome |

The model-supplied dossier requested a timeout on an inactive/wrong port. A wrong port often produces *connection refused* immediately rather than timeout; this script asserts a **transport error**, without inventing its cause. A separate delayed/timeout injection can be introduced later.

## Evidence and acceptance
A PASS returned by the script is **not** sufficient for PILOT-VERIFIED. Reviewer must inspect the Windmill run, Railway service logs, deployment identity, each HTTP result, and match scan/correlation records. This is a two-node authenticated test and not independent proof of external AI-host capabilities.

`E9999_SYNTHETIC` is test-only and must never be counted as an actual production incident. The server returns a synthetic failure in its JSON body with HTTP 200 to distinguish successful transport from the intentionally negative diagnostic condition.

**Security:** secret must not be supplied as a visible run argument or included in screenshots; use Windmill encrypted variable bindings. This initial bearer-token demo does not yet implement HMAC request signing, replay detection, idempotency or independent verifier controls; those remain explicit advancement gates.
