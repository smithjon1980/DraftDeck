# DraftDeck skill-failure escalation — REA + Windmill
Status: SPECIFIED_CANDIDATE / NOT_CONNECTED / NOT_EXECUTED
Scope: Chromium → PDF → Canva adapter calibration and reusable DraftDeck skill failure recovery.
Authority: existing BOSS G1–G5, SEVEN, Zone C, production HOLD and source-first contract prevail. This is not a new architecture layer.

## Responsibilities
- SKILL.md: primary bounded procedure and its expected assertions.
- Windmill (candidate orchestrator): receives *structured* test results and routes states, logging immutable run identifiers and artifact digests. Windmill is not presently connected here.
- REA (candidate investigator): examines *permitted* source code, local observable behavior, and controlled Chromium/Canva test fixtures to propose a cause and repair. Not connected here and no reverse-engineering job has run.
- Human: approves candidate source edits, external side effects, credentials, data transfer and any release or escalation beyond read-only analysis.

## Escalation contract
RECEIVED → SKILL_RUN → VERIFY.
On PASS: require independently checked assertions, then REVIEW; do not infer visual or Canva editability from mere PDF availability.
On deterministic FAIL: record test input, expected vs actual, browser/PDF/Canva comparison, source commit, rule id, environment, trace and bounded retry eligibility.
A single retry is allowed ONLY if transient, demonstrated safe and idempotent; no blind re-import into Canva (new design is a side effect) or replacement of canonical files.
Repeatable failure → REA_DIAGNOSIS_REQUESTED. Investigate without writing the authorized source; compare candidate mechanisms with evidence; produce minimal corrective patch and falsification fixtures.
Windmill may queue approved test-only jobs after authenticated configuration; never authorize actions based on a model suggestion.
Diagnostic uncertainty, credentials absent, privacy boundary or insufficient evidence → HUMAN_REVIEW / HOLD.
Human-authorized repair in experimental branch → REBUILD → CHROMIUM_QA → CANVA_IMPORT_TEST → TEXT_FIDELITY_QA → VISUAL_QA → HUMAN_REVIEW.
No silent production promotion, no automatic canonical design edits, no uncapped remediation loop.

## Failure evidence envelope
```json
{
  "run_id": "example-only",
  "phase": "CANVA_TEXT_FIDELITY",
  "skill_id": "draftdeck",
  "source_commit": "NOT_ESTABLISHED",
  "input_artifact_sha256": "NOT_ESTABLISHED",
  "reference_artifact_sha256": "NOT_ESTABLISHED",
  "environment": {"chromium_version": "UNKNOWN", "adapter": "Canva"},
  "expected": "spaces and typography preserved",
  "observed": "missing spaces in sample sentence",
  "evidence_refs": [],
  "failure_class": "REPRODUCIBLE_TEXT_MAPPING",
  "retry_allowed": false,
  "escalation": "REA_CANDIDATE",
  "authorization": "HUMAN_REVIEW_REQUIRED",
  "state": "HOLD"
}
```

## Initial calibration task
Grounding: Canva Calibration Sheet 001 user screenshot shows gray overall canvas, correctly colored opaque samples, merged words in the introductory paragraph, and overlapping elements in typography/CSS sections. Canva's text inspection confirms individually addressable TEXT elements. The black original slide and gray calibration canvas are different observations; do not assume one cause without isolating.
Tests: (1) full-page explicit white printable rectangle vs body CSS background; (2) word spacing and text container trials; (3) heading/body overlap across PDF and Canva; (4) full source→PDF→Canva roundtrip with extracted text comparison and visual human review.
Pass only when both independent object editability and source-exact text, positioning, background fidelity meet agreed criteria.

## Deferred configuration
Windmill: workspace URL, authenticated connection, job permissions, secrets policy, branch-specific testing environment and evidence storage are all NOT_ESTABLISHED.
REA: exact REA installation/repository/version, permitted examination targets and tool entrypoint NOT_ESTABLISHED.
Do not claim REA/Windmill was executed or connected.
