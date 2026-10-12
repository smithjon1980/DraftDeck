---
name: market-demand-screen
description: Candidate market demand screening procedure abstracted independently from a user-supplied Ukrainian translation of Alex Hormozi's $100M Offers.
version: 0.1.0-candidate
source_ids: [HORMOZI-100M-OFFERS-2021-UK-001]
operational_phase_tags: [DISCOVERY]
enforcement_tags: [G1]
trust_class: UNVERIFIED_COMMERCIAL_METHOD
qualification_status: SPECIFIED_CANDIDATE
test_status: NOT_TESTED
authority_scope: RESEARCH_ONLY
evidence_refs: []
human_dependency: "Human supplies evidence and business context for Find a demonstrably reachable buyer segment experiencing an urgent problem. and explicitly reviews any proposed external action"
agent_deliverable: "Human-readable market-demand-screen decision workpaper: facts, assumptions, evidence references, conflicts, suggested action, rejected alternatives, and review diff"
correction_vector: "Authenticated human correction/REJECT channel: record HUMAN_OVERRIDE with exact authorized correction, invalidate affected semantic cache (proposed SEAM-B01), derive new L1 digest preserving history, hold stale envelopes pending confirmation"
---

# Market Demand Screening

## Goal
Find a demonstrably reachable buyer segment experiencing an urgent problem.

## Proof
Offer only where demand signals, buyer access, ability to pay and identifiable need have evidence.

## Steps
1. Survey: define buyer.
2. gather dated buyer signals and alternative offers.
3. separate willingness to pay from actual orders.
4. reject unsupported market rankings.
5. register a testable segment hypothesis..

## Boundary
Do not assume the most affluent or largest market is viable; if buyer evidence missing, HOLD.

## Inputs and outputs
Input: documented business context, source-bound discovery notes, and authorized scope.
Output: an independently authored candidate workpaper with source references, assumptions and unresolved items.

## Source location
pages 29–37; HORMOZI-100M-OFFERS-2021-UK-001. Source content is an author's commercial methodology, **not** independently verified BOSS evidence. The operational procedure here is an original BOSS adaptation, not reproduced book text.

## Falsification specimen
A proposal containing a material unproven commercial claim, missing necessary operand, or unauthorized execution attempt must be flagged HOLD / NOT_ESTABLISHED rather than promoted to an approved deliverable.

## Human–Agent interface candidate
Human dependency: Human supplies evidence and business context for Find a demonstrably reachable buyer segment experiencing an urgent problem. and explicitly reviews any proposed external action.
Agent deliverable: Human-readable market-demand-screen decision workpaper: facts, assumptions, evidence references, conflicts, suggested action, rejected alternatives, and review diff.
Correction: Authenticated human correction/REJECT channel: record HUMAN_OVERRIDE with exact authorized correction, invalidate affected semantic cache (proposed SEAM-B01), derive new L1 digest preserving history, hold stale envelopes pending confirmation.
When requested action exceeds the explicit Equivalence Set or financial authority, require `ZONE_C_ESCALATION_REQUIRED` and no dispatch. Documentation only; NOT_IMPLEMENTED / NOT_TESTED.

## Three-Quadrant Conformity (Candidate)
- **A — Assignment:** Human entitlement and ability: NOT_ESTABLISHED until operator provides evidence; agent role: DESIGN_ASSISTANT_ONLY; skill: `market-demand-screen`; tool access: NONE_ASSUMED. Check the existing `human_dependency`, `agent_deliverable`, and `correction_vector` fields.
- **B — Minimum sufficient intervention:** Evaluate manual/no-change, SCRIPT, PROGRAM, NARROW_AI and GENERAL_AI in that order subject to suitability; selected class NOT_ESTABLISHED until the specific task is scoped; record rejected alternatives.
- **C — Operational performance:** SOP reference: CANDIDATE_ONLY; KPI definition/baseline/denominator/window: NOT_ESTABLISHED; OKR reference: OPTIONAL/NOT_ESTABLISHED; CAPA: record observed defect, correction authority, retest evidence and outcome. Never treat an untested KPI as a measured improvement.
- **Stop rule:** missing entitlement, material evidence, valid intervention economics or authorization -> HOLD. This overlay does not authorize execution or imply operational qualification.
