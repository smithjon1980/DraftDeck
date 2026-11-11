# BOSS release gate v0.3 — candidate

This is the **schema-reconciled follow-up**, not a replacement for historical v0.1/v0.2 fixture files.

Run locally after installing Python `jsonschema`: `python gate.py`.

The inputs contain **evidence IDs**, not proof: the test resolver uses invented records only to exercise branches. For real Windmill use, resolve against a trusted server-side source with issuer, workflow binding, integrity, freshness, permissions and expiry. Client-supplied risk tier, specialist requirement and approval request ID are not authoritative.

## Windmill flow contract (NOT DEPLOYED)
1. Validate v0.3 input schema and record safe error receipt on failure.
2. Fetch trusted evidence independently; raise a terminal hold on missing IPOS evidence, verified claim/receipt contradiction, missing specialist acceptance, or privacy failure. Do not catch-and-continue into deployment.
3. Recheck human-approved risk assessment and referral obligations; the test gate does not validate these.
4. On eligibility, **pause** using an authenticated Windmill approval step and verify actor identity, scope, action digest and approved request in backend records.
5. Only a separate privileged executor may deploy following trusted approval recheck. Test release must write a mock marker, not perform actual external changes.
6. Confirm the four blocked fixture runs have *no downstream release marker*, and preserve redacted run receipts.

A Windmill approval event is not necessarily an immutable cryptographic signature. Neither eligibility nor self-reported approval equals release authorization. No live Windmill test or production deployment has occurred.
