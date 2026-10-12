---
name: value-equation-assessment
description: Candidate value equation assessment procedure abstracted independently from a user-supplied Ukrainian translation of Alex Hormozi's $100M Offers.
version: 0.2.0-candidate
source_ids: [HORMOZI-100M-OFFERS-2021-UK-001]
operational_phase_tags: [EVALUATION]
enforcement_tags: [G1, G5]
trust_class: UNVERIFIED_COMMERCIAL_METHOD
qualification_status: SPECIFIED_CANDIDATE
test_status: NOT_TESTED
authority_scope: RESEARCH_ONLY
evidence_refs: []
human_dependency: "Human supplies evidence and business context for Evaluate offer desirability with four explicitly separate buyer perceptions. and explicitly reviews any proposed external action"
agent_deliverable: "Human-readable value-equation-assessment decision workpaper: facts, assumptions, evidence references, conflicts, suggested action, rejected alternatives, and review diff"
correction_vector: "Authenticated human correction/REJECT channel: record HUMAN_OVERRIDE with exact authorized correction, invalidate affected semantic cache (proposed SEAM-B01), derive new L1 digest preserving history, hold stale envelopes pending confirmation"
---

# Value Equation Assessment

## Goal
Evaluate offer desirability with four explicitly separate buyer perceptions.

## Proof
Record desired outcome, perceived likelihood, expected delay and required effort; flag unsupported assumptions.

## Steps
1. Interview intended buyers.
2. score four perceptions qualitatively.
3. identify high-friction factors.
4. propose small experiments.
5. compare changes with initial baseline.

## Foundry-aligned likelihood and time/effort evidence
The source-derived **Value Equation** is a perceived-value heuristic, not an observed statistical law. The BOSS-adapted operational-likelihood field MUST reference the Capability Foundry Dual Evidence Profile (DEP), if admitted and available. A Lens B probe pass rate may be reported as `passes / eligible_trials` ONLY with declared test suite, version, environment, selection/exclusion criteria, sample size, failures, confidence limitations and scope. It is **not a general probability of customer success** or a substitute for customer-perceived confidence. If DEP is absent, set `OPERATIONAL_LIKELIHOOD=NOT_ESTABLISHED`; do not insert a marketing percentage. Lens A research is separate.

For the DFW barbershop/loctician hybrid scheduling **candidate**, measure `on_site_wait_minutes`, `remote_queue_minutes`, `total_elapsed_minutes`, `arrival_variance`, and `customer_interaction_steps` from timestamped actual or synthetic test events. Compare against a declared manual/appointment baseline under comparable conditions. Dynamic wait estimates alone do not establish that physical waiting, total delay or effort decreased; customer travel, missed slots and queue estimation errors remain in the denominator. Label synthetic results SIMULATED and unsupported comparisons HOLD.

**Falsification:** A zero-failure probe sample is advertised as 100% customer success, or a revised ETA is claimed as saved minutes without measured arrival/service events → `G5_HOLD`.

## Boundary
This is perceived-value reasoning, not a validated economic ROI formula; never convert it into CASH_YIELD_VERIFIED.

## Inputs and outputs
Input: documented business context, source-bound discovery notes, and authorized scope.
Output: an independently authored candidate workpaper with source references, assumptions and unresolved items.

## Source location
pages 49–58; HORMOZI-100M-OFFERS-2021-UK-001. Source content is an author's commercial methodology, **not** independently verified BOSS evidence. The operational procedure here is an original BOSS adaptation, not reproduced book text.

## Falsification specimen
A proposal containing a material unproven commercial claim, missing necessary operand, or unauthorized execution attempt must be flagged HOLD / NOT_ESTABLISHED rather than promoted to an approved deliverable.

## Human–Agent interface candidate
Human dependency: Human supplies evidence and business context for Evaluate offer desirability with four explicitly separate buyer perceptions. and explicitly reviews any proposed external action.
Agent deliverable: Human-readable value-equation-assessment decision workpaper: facts, assumptions, evidence references, conflicts, suggested action, rejected alternatives, and review diff.
Correction: Authenticated human correction/REJECT channel: record HUMAN_OVERRIDE with exact authorized correction, invalidate affected semantic cache (proposed SEAM-B01), derive new L1 digest preserving history, hold stale envelopes pending confirmation.
When requested action exceeds the explicit Equivalence Set or financial authority, require `ZONE_C_ESCALATION_REQUIRED` and no dispatch. Documentation only; NOT_IMPLEMENTED / NOT_TESTED.
