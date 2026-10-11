# BOSS ENVSCAN — Switchboard Operator

**Order:** BOSS-ENVSCAN-002  
**Status:** TOPOLOGY DECLARED / NO ACTIVE CIRCUITS VERIFIED

## Mission
Provide an auditable configuration and routing boundary between n8n (communications), Windmill (diagnostic orchestration), Railway (execution), and Bluehost (artifact delivery), using GitHub as the non-secret source of truth.

## Authority and trust boundaries
The manifest describes intended topology, not live network state. Credentials are **not** stored or routed through GitHub. `secret_ref` entries are symbolic references only; actual credentials must remain in the secret manager of the service that consumes them. Do not build a central plaintext vault or an endpoint that redistributes secrets. Prefer narrow-scoped service credentials with rotation, access logs, and explicit owner approval.

## Circuit table
| Circuit | Direction | Purpose | Contract |
|---|---|---|---|
| R01 | n8n → Windmill | Trigger diagnostic | diagnostic-request.v1 |
| R02 | Windmill → Railway | Execute probe | probe-request.v1 |
| R03 | Railway → Windmill | Execution receipt | execution-receipt.v1 |
| R04 | Windmill → Bluehost | Approved artifact upload | artifact-manifest.v1 |
| R05 | Windmill → n8n | Verification notification | diagnostic-outcome.v1 |

## Required custody fields
Each request carries `scan_id`, `request_id`, `mission_profile`, `target_execution_environment`, `issued_at_utc`, and the schema version. Each subsequent receipt appends its own immutable event ID, timestamp, actor/service identifier, result, and evidence reference. Preserve the original request hash. Never promote a claimed success to VERIFIED without inspectable evidence.

## Protocol translation
Use explicit versioned JSON schemas for requests and receipts. Route names above are *contract identifiers*, not claims that implementations exist. A future provisioner validates schema conformance, response authentication, timeouts, idempotency, and error classification at every edge. Secure file transfer to Bluehost requires an independently verified public or authorized read-back and hash match.

## Synthetic T001 acceptance
E9999 is reserved in this test as a **synthetic** diagnostic outcome. The test passes only if the expected failure is observed and the artifact is delivered and read back correctly. A network timeout, authentication denial, or upload failure is an *unexpected workflow failure*, not successful simulation.

## Required provisioning procedure
1. Verify the actual four workspaces and ownership; do not invent URL endpoints.
2. Configure service-specific least-privilege secrets outside the repository.
3. Provision endpoints and fill non-secret manifest fields via reviewed changes.
4. Validate R01 through R05 independently with safe test payloads.
5. Execute an end-to-end T001 transaction and preserve verifier receipts.
6. Authorize scheduled monitoring only after evidence proves each boundary.

**Security boundary:** This switchboard is a connection registry and protocol controller, not a license to bypass the hosts' network or credential restrictions.
