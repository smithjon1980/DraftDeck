# Source-content congruence control — decision record
Status: SPECIFIED_CANDIDATE / NOT_TESTED
Cause: Intake 06 showed a hashable PDF can be a storefront-wrapped collage unrelated to its claimed work.

## State model
RECEIVED → IDENTIFIED → CONTENT_INSPECTED → CONTENT_PASS / CONTENT_HOLD / CONTENT_FAIL.
CONTENT_PASS → pending independent provenance/authentication, rights, and ordinary skill extraction.
CONTENT_HOLD → no extraction until further inspection.
CONTENT_FAIL → QUARANTINED / NO_EXTRACTION; preserve fingerprint and reason, never active L0.
Each transition requires page-anchored evidence and a human-review correction path.

## Separate assertions
1. Source digest: which bytes?
2. Content congruence: is content coherent with declared title and subject?
3. Source authenticity: is the work genuinely sourced/attributed?
4. Rights: what material may be reused?
5. Skill qualification: has the extracted capability been tested?
All five are distinct and none imply the others.

## Proposed candidate probe
INGEST-CONGRUENCE-001: feed the rejected intake 06 fixture; require CONTENT_FAIL, quarantine record and zero derived skills. Feed coherent-but-unverified document; require CONTENT_PASS and PENDING_AUTHENTICATION rather than VERIFIED L0. Both cases NOT_TESTED as automated runtime tests.
