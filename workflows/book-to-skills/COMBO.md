# COMBO — Book-to-Skills Intake
Status: SPECIFIED_CANDIDATE / NOT_TESTED

## Routing map
```text
SOURCE RECEIVED
  ↓ fingerprint + identity claim
SOURCE MANIFEST (PENDING AUTHENTICATION)
  ↓ content congruence inspection: opening / middle / ending / visuals
CONTENT_GATE PASS? — NO → HOLD / QUARANTINE / NO EXTRACTION
  ↓ YES: preserve page/line/time anchors
ATOMIC SKILL EXTRACTION
  ↓ unique responsibilities and falsification conditions
SKILL.md + references.md (one per skill)
  ↓ only if multi-skill dependencies exist
COMBO.md (ordered handoff with HOLD paths)
  ↓ mechanical inspection
HUMAN REVIEW → CANDIDATE ARTIFACTS
```

## Handoffs
- Intake → Extract: source ID, exact locations, scope, confidence, admission status.
- Extract → Compose: declared skill inputs/outputs, prerequisites, failure paths, shared authority checks.
- Compose → Inspect: artifact paths, referenced evidence, source coverage, unresolved questions.
- Inspect → Review: candidate inventory, gaps, claims requiring verification; no automated promotion.

## Rejection and rollback
If source is coherent but not authenticated, continue in research-only mode, not governing L0. If claimed authorship and actual content are incongruent, immediately reject extraction and quarantine the source identification. If source text is incomplete, use HOLD for affected skills. If instructions conflict, preserve both with contradiction record and request authoritative resolution before implementation. Never overwrite a separately authored skill by name collision.

## Acceptance criteria
Only CONTENT_GATE PASS documents proceed to extraction. Every skill has Goal/Proof/Steps/Boundary and explicit trust/status. Every COMBO step targets an existing declared skill. Every nontrivial extracted claim has a source anchor or DESIGN_INFERENCE label. No production release or GitHub mutation is implied by chat activation.
