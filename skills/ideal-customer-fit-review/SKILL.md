---
name: ideal-customer-fit-review
description: Independent BOSS candidate workpaper inspired by high-level topics in a user-supplied 2025 private-volume business book.
version: 0.2.0-candidate
source_ids: [HORMOZI-100M-LOST-CHAPTERS-2025-001]
operational_phase_tags: [DISCOVERY]
enforcement_tags: [G1, G2]
trust_class: RESTRICTED_SOURCE_RESEARCH
qualification_status: SPECIFIED_CANDIDATE
test_status: NOT_TESTED
authority_scope: RESEARCH_ONLY
evidence_refs: []
human_dependency: "Human supplies evidence and business context for Identify a serviceable buyer group using relevant behavior and business need, not protected characteristics. and explicitly reviews any proposed external action"
agent_deliverable: "Human-readable ideal-customer-fit-review decision workpaper: facts, assumptions, evidence references, conflicts, suggested action, rejected alternatives, and review diff"
correction_vector: "Authenticated human correction/REJECT channel: record HUMAN_OVERRIDE with exact authorized correction, invalidate affected semantic cache (proposed SEAM-B01), derive new L1 digest preserving history, hold stale envelopes pending confirmation"
---

# Ideal Customer Fit Review

## Goal
Identify a serviceable buyer group using relevant behavior and business need, not protected characteristics.

## Proof
A proposed buyer profile cites observed customer needs, cost to serve, retention cohorts and explicit exclusions; sparse cohorts marked inconclusive.

## Steps
1. Gather consented first-party business needs.
2. compare customer problem and delivery fit.
3. inspect retention and cohort denominators.
4. propose one reversible targeting experiment.
5. review for unfair exclusion.

## Boundary
Do not collect political affiliation, family status or sensitive traits for eligibility. Do not treat top spenders as inherently best customers.

## Inputs and outputs
Input: authorized and minimized first-party business data or synthetic lab records, declared source provenance, and permissible scope.
Output: a self-contained BOSS research workpaper with assumptions, metrics, declared uncertainty and a qualified recommendation or HOLD.

## Falsification
Any required economic, authorization or independent evidence operand absent → HOLD / NOT_ESTABLISHED. Any asserted settled financial outcome without independently reconcilable records → G5_HOLD.

## Source context
Source ID HORMOZI-100M-LOST-CHAPTERS-2025-001; topic area: Your First Avatar, printed pp.3–9. The steps are original BOSS design, not a reproduction or official implementation of the author's text.

## G2 zero-inference qualification boundary — candidate enforcement contract
The permissible automated input is a purpose-limited, consented, business-relevant event record, such as a validated transaction receipt, booking frequency, requested service or explicit service need. Define an allowlist of fields and remove demographic and protected-characteristic data, inferred proxies, unnecessary location granularity, free-text sensitive attributes and hidden model embeddings before routing to any evaluator. No model may infer age, race, ethnicity, political affiliation, religion, disability, family status or another sensitive status to qualify or exclude a customer. Record the permitted purpose and basis for processing.

**Important:** Removing explicit demographics alone does NOT ensure bias-free outcomes—transaction patterns, service types and postal regions can also act as proxies. Use outcome monitoring and proportional fairness review. Some geographic or demographic data may be required by law or for service-area feasibility: handle those via separate authorized deterministic rules and minimum-necessary controls, not a blanket prohibition on operational geography. Missing consent, unapproved schema or inferred sensitive attribute → `G2_HOLD`.

**Runtime state:** data minimization and model-gateway filtering are **SPECIFIED / NOT_IMPLEMENTED**. No live customer segmentation.

**Falsification:** A classification can be influenced by protected/sensitive fields or covert proxies outside the explicit input allowlist → FAIL.

## Human–Agent interface candidate
Human dependency: Human supplies evidence and business context for Identify a serviceable buyer group using relevant behavior and business need, not protected characteristics. and explicitly reviews any proposed external action.
Agent deliverable: Human-readable ideal-customer-fit-review decision workpaper: facts, assumptions, evidence references, conflicts, suggested action, rejected alternatives, and review diff.
Correction: Authenticated human correction/REJECT channel: record HUMAN_OVERRIDE with exact authorized correction, invalidate affected semantic cache (proposed SEAM-B01), derive new L1 digest preserving history, hold stale envelopes pending confirmation.
When requested action exceeds the explicit Equivalence Set or financial authority, require `ZONE_C_ESCALATION_REQUIRED` and no dispatch. Documentation only; NOT_IMPLEMENTED / NOT_TESTED.

## Three-Quadrant Conformity (Candidate)
- **A — Assignment:** Human entitlement and ability: NOT_ESTABLISHED until operator provides evidence; agent role: DESIGN_ASSISTANT_ONLY; skill: `ideal-customer-fit-review`; tool access: NONE_ASSUMED. Check the existing `human_dependency`, `agent_deliverable`, and `correction_vector` fields.
- **B — Minimum sufficient intervention:** Evaluate manual/no-change, SCRIPT, PROGRAM, NARROW_AI and GENERAL_AI in that order subject to suitability; selected class NOT_ESTABLISHED until the specific task is scoped; record rejected alternatives.
- **C — Operational performance:** SOP reference: CANDIDATE_ONLY; KPI definition/baseline/denominator/window: NOT_ESTABLISHED; OKR reference: OPTIONAL/NOT_ESTABLISHED; CAPA: record observed defect, correction authority, retest evidence and outcome. Never treat an untested KPI as a measured improvement.
- **Stop rule:** missing entitlement, material evidence, valid intervention economics or authorization -> HOLD. This overlay does not authorize execution or imply operational qualification.
