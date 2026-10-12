# BOSS Commercial Release Gateway — deterministic fixture suite

Status: CANDIDATE. Uses existing `governance/specs/boss-release-gate.schema.json`.

Run from repository root after installing `jsonschema`: `python governance/tests/commercial-release/validate.py`.

| Fixture | Expected evaluator result |
|---|---|
| 01 Golden path | ELIGIBLE_FOR_INDEPENDENT_EVIDENCE_REVIEW |
| 02 Anti-hallucination | RELEASE_BLOCKED_EVIDENCE_DEFICIT |
| 03 Unsigned handoff | RELEASE_BLOCKED_PENDING_SPECIALIST |
| 04 Privacy deficit | RELEASE_BLOCKED_PRIVACY_VIOLATION |

**Important:** The current schema cannot express specific `data_retention_schedule`, `minimization_tags` or `engineering_signoff` fields. The negative fixtures therefore encode these as absent/UNKNOWN control *evidence*, not literal missing schema fields. The evaluator cannot prove a submitted PASS is truthful. All `fixture://` references are intentionally fake. The golden path is never an authorization for deployment. A trusted evidence resolver, verified human approvals and actual Windmill stop/hold behavior remain separate gates.

Windmill has NOT executed these fixtures. Local deterministic evaluation and production enforcement are separate evidence categories.
