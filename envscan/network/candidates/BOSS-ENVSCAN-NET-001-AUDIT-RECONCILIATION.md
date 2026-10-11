# BOSS ENVSCAN-NET-001 — Independent Audit Reconciliation

**Order:** BOSS-ENVSCAN-NET-001-AUDIT-01  
**Status:** INDEPENDENT REVIEW RECEIVED / AMENDMENTS CANDIDATE / NO DEPLOYMENT AUTHORIZED BY THIS RECORD  
**Review verdict:** ACCEPT WITH AMENDMENTS  
**Basis:** Gemini independent review supplied by project owner; reviewer findings are recorded, not presented as independently tested facts.

## Accepted amendments
- Reduce the first deployment experiment to **Windmill → Railway**. Defer n8n and Bluehost until their functions are justified and an execution boundary is tested.
- Preserve n8n (event/integration gateway) and Bluehost (approved public distribution) as *future topology nodes*, not discarded designs.
- Application-layer routing analogies are structural, not literal Layer 3 routing protocols.
- Require authenticated service-to-service requests, least privilege, bounded retry/idempotency, asynchronous execution support when needed, safe evidence handling and explicit rate-limiting classification.
- Preserve prior Switchboard documentation intact; require explicit reviewed migration before changes to deployed configuration.

## Qualifications and corrections to independent review
1. **Verifier independence:** Windmill checking Railway's response is useful receipt validation but is not fully independent evidence for all assertions. Separate observers/trust domains are required for out-of-band attestations, environment-specific egress tests and public delivery.
2. **Signatures vs execution:** Valid HMAC/JWT establishes request/response authenticity only within its threat model. A hash of a Railway-produced result independently recomputed by Windmill establishes content consistency, not ground truth that execution happened.
3. **Trace semantics:** W3C Trace Context permits a stable trace-id for a trace and new span IDs per operation; trace identifiers must be validated and never treated as authorization or unforgeable proof. Preserve a separate BOSS scan_id, request_id, idempotency key, and immutable original request bytes/digest.
4. **Rate limit:** HTTP 429 shows that a responder rate-limited a request. It may not establish successful authorization or functional availability of the underlying capability. Record RATE_LIMITED with observed scope and unestablished downstream capability.
5. **Errors and causes:** HTTP 401/403 suggests access denial, but 'expired credential' or 'invalid credential' needs more evidence. Timeout establishes an incomplete observation within a defined period, not necessarily non-execution.
6. **Integrity:** Hashes need an authorized, trusted reference. An untrusted publisher can publish matching altered content and hash. Independent read-back establishes destination contents relative to an approved artifact digest.
7. **Scheme:** Example $schema URLs are placeholders and must not be represented as live resolvable schemas.
8. **External host scope:** A Railway probe proves Railway worker properties, not those of ChatGPT/Gemini/Grok. External-host tests require a probe executed through that target host's authorized tools, with externally checkable receipts when feasible.

## Candidate v0.2 pilot boundary
- **Windmill:** orchestration and policy application, request origination, evidence collection.
- **Railway:** authenticated diagnostic test endpoint; deterministic synthetic response and associated server-side receipt.
- **GitHub:** source-controlled specifications (not a diagnostic runtime).
- **Independent verification:** separate logical role, to be implemented and proven for claims requiring independent observations.
- **n8n / Bluehost:** HOLD pending pilot graduation.

### Vertical slice W-R-001 (proposed)
1. Windmill builds a uniquely identified request with scan_id, request_id, timestamp, nonce, mission/profile, schema version and idempotency key.
2. Windmill sends HTTPS request authenticated with scoped key or signed request. Railway validates identity, timestamp freshness, schema and replay control.
3. Railway produces an intentionally simulated failure (E9999_SYNTHETIC), stores its server-side event receipt in a separately inspectable log, and returns typed diagnostic outcome.
4. Windmill checks authenticated response (if configured), schema, echoed correlation fields, expected synthetic code, and bounded completion behavior.
5. A negative test rejects invalid auth, and a second negative test rejects malformed payload before action.
6. Preserve Windmill run ID, Railway execution/log ID, UTC timestamps, trace correlation and hashes of nonsecret request/receipt data.
7. Record claim scope: 'authenticated synthetic handshake observed' only if tests pass. Do not claim universal environment readiness, independent execution attestation, or four-node delivery.

## Promotion gates
CANDIDATE → REVIEWED (architect approval of amendments) → PILOT-VERIFIED (observed live receipts and negative tests) → APPROVED (operations, rollback, security sign-off). This file does not promote any gate.

## Next decisions
- Approve or revise the two-node pilot and credential strategy.
- Confirm actual workspace ownership/endpoints and create least-privilege secrets in platform vaults.
- Choose independent verifier deployment for assertions exceeding Windmill's own trust boundary.
