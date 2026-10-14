---
name: business-stage-evidence-classifier
description: Original BOSS candidate procedure informed by user-supplied $100M Scaling Roadmap.
version: 0.1.0-candidate
source_ids: [HORMOZI-SCALING-ROADMAP-COMBINED-001]
operational_phase_tags: [DISCOVERY]
enforcement_tags: [G1, G2]
trust_class: UNVERIFIED_COMMERCIAL_METHOD
qualification_status: SPECIFIED_CANDIDATE
test_status: NOT_TESTED
authority_scope: RESEARCH_ONLY
evidence_refs: []
human_dependency: "Human provides context and authorization for Assess current business constraints across ten source-defined maturity stages instead of inferring maturity from company size.; reviews proposed outcome before any external effect"
agent_deliverable: "Human-readable business-stage-evidence-classifier review workpaper with evidence, assumptions, alternatives, unresolved questions, proposed result and corrections diff"
correction_vector: "Authenticated human REJECT/correction: persist HUMAN_OVERRIDE with exact permitted correction, invalidate relevant semantic cache (SEAM-B01 proposed), append a new source-linked L1 derivative/digest, block stale active envelope until revalidation"
---

# Business Stage Evidence Classifier

## Goal
Assess current business constraints across ten source-defined maturity stages instead of inferring maturity from company size.

## Proof
Record stage hypothesis, observed problem, business metrics, customer and delivery proof, source anchors and gaps; label UNKNOWN when evidence absent.

## Steps
1. Inspect source stage questions.
2. gather actual operating data.
3. classify dominant constraint.
4. distinguish revenue and headcount from maturity evidence.
5. get human review.
6. document uncertainty.

## Boundary
Roadmap stages are advisory descriptions, not validated universal thresholds; stage classification does not grant BOSS execution authority.

## Inputs and outputs
Input: relevant, authorized small-business observations or synthetic lab records.
Output: a bounded, source-linked candidate workpaper with evidence status and HOLD conditions.

## Falsification
If the workpaper advances a stage or promotes execution without the stated proof, or converts illustrative estimates into verified sales, income or success, return `G5_HOLD / NOT_ESTABLISHED`.

## Source
HORMOZI-SCALING-ROADMAP-COMBINED-001; Stage overview PDF pp.2, 23; stage plates pp.3,24,55,83,108,134,160,186,213. Stage-specific claims outside the inspected parts must be checked against the PDF before use.

## Human–Agent interface candidate
Human dependency: Human provides context and authorization for Assess current business constraints across ten source-defined maturity stages instead of inferring maturity from company size.; reviews proposed outcome before any external effect.
Agent deliverable: Human-readable business-stage-evidence-classifier review workpaper with evidence, assumptions, alternatives, unresolved questions, proposed result and corrections diff.
Correction: Authenticated human REJECT/correction: persist HUMAN_OVERRIDE with exact permitted correction, invalidate relevant semantic cache (SEAM-B01 proposed), append a new source-linked L1 derivative/digest, block stale active envelope until revalidation.
If operation exceeds the explicitly approved Equivalence Set or financial limit, require `ZONE_C_ESCALATION_REQUIRED` and prevent dispatch. No runtime implementation or probe qualification is claimed.

## Three-Quadrant Conformity (Candidate)
- **A — Assignment:** Human entitlement and ability: NOT_ESTABLISHED until operator provides evidence; agent role: DESIGN_ASSISTANT_ONLY; skill: `business-stage-evidence-classifier`; tool access: NONE_ASSUMED. Check the existing `human_dependency`, `agent_deliverable`, and `correction_vector` fields.
- **B — Minimum sufficient intervention:** Evaluate manual/no-change, SCRIPT, PROGRAM, NARROW_AI and GENERAL_AI in that order subject to suitability; selected class NOT_ESTABLISHED until the specific task is scoped; record rejected alternatives.
- **C — Operational performance:** SOP reference: CANDIDATE_ONLY; KPI definition/baseline/denominator/window: NOT_ESTABLISHED; OKR reference: OPTIONAL/NOT_ESTABLISHED; CAPA: record observed defect, correction authority, retest evidence and outcome. Never treat an untested KPI as a measured improvement.
- **Stop rule:** missing entitlement, material evidence, valid intervention economics or authorization -> HOLD. This overlay does not authorize execution or imply operational qualification.
