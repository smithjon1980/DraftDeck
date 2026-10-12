---
name: ethical-risk-reversal
description: Candidate evidence-constrained risk reversal procedure abstracted independently from a user-supplied Ukrainian translation of Alex Hormozi's $100M Offers.
version: 0.2.0-candidate
source_ids: [HORMOZI-100M-OFFERS-2021-UK-001]
operational_phase_tags: [EVALUATION]
enforcement_tags: [G2, G4, SEAM-D01]
trust_class: UNVERIFIED_COMMERCIAL_METHOD
qualification_status: SPECIFIED_CANDIDATE
test_status: NOT_TESTED
authority_scope: RESEARCH_ONLY
evidence_refs: []
---

# Evidence-Constrained Risk Reversal

## Goal
Design a lawful, supportable guarantee or service assurance aligned to deliverable reality.

## Proof
Terms specify measurable trigger, remedies, exclusions, evidence and fulfillment capacity; misleading promises rejected.

## Steps
1. Enumerate buyer risk.
2. match each risk to a verifiable control.
3. calculate refund/fulfillment exposure.
4. draft plain-language terms.
5. obtain appropriate review before publication.

## Guarantee-to-recovery correspondence (design contract)
Map each guarantee to an explicit `promise_id`, measurable trigger, supporting receipt, expiry, jurisdiction/contract terms, allowed remedy, responsible owner, customer consent, compensation authorization scope, maximum exposure and reconciliation path. Align to Phase 3 `UNCERTAIN → REQUIRES_RECONCILIATION` and open `SEAM-D01`. A failed or uncertain execution is **not always a failed promised business outcome**, and compensation must not be based on an ambiguous write.

For deterministic, reversible, previously authorized cases, the design MAY propose an idempotent compensating action (e.g., voiding an internal provisional reservation) with a stable operation ID, preconditions, deduplication and independent evidence. For refunds, customer communication, paid ledger mutation, externally visible rebooking or irreversible effects, require the appropriate approved payment/authority gate and verified original outcome; use `COMPENSATION_HOLD / MANUAL_RECONCILIATION` when the downstream state is uncertain or authorization is absent. Compensation is a **new transaction**, not rollback magic. No universal automatic refund or booking change is authorized.

**Falsification:** Lost confirmation produces duplicate refunds, a customer is reassigned without authorization, or a guarantee fires while delivery status is UNCERTAIN → design FAIL. There is no implemented broker, compensation hook or live transaction in this revision.

## Boundary
No impossible guarantee, artificial scarcity or unsupported income claims. Human review required before legal/commercial use.

## Inputs and outputs
Input: documented business context, source-bound discovery notes, and authorized scope.
Output: an independently authored candidate workpaper with source references, assumptions and unresolved items.

## Source location
pages 85–105; HORMOZI-100M-OFFERS-2021-UK-001. Source content is an author's commercial methodology, **not** independently verified BOSS evidence. The operational procedure here is an original BOSS adaptation, not reproduced book text.

## Falsification specimen
A proposal containing a material unproven commercial claim, missing necessary operand, or unauthorized execution attempt must be flagged HOLD / NOT_ESTABLISHED rather than promoted to an approved deliverable.
