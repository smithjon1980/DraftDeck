---
name: cash-payback-stress-screen
description: Independent BOSS candidate workpaper inspired by high-level topics in a user-supplied 2025 private-volume business book.
version: 0.2.0-candidate
source_ids: [HORMOZI-100M-LOST-CHAPTERS-2025-001]
operational_phase_tags: [EVALUATION]
enforcement_tags: [G2, G5]
trust_class: RESTRICTED_SOURCE_RESEARCH
qualification_status: SPECIFIED_CANDIDATE
test_status: NOT_TESTED
authority_scope: RESEARCH_ONLY
evidence_refs: []
human_dependency: "Human provides context and authorization for Stress-test whether a small-business promotional offer can repay acquisition spend without a liquidity shortfall.; reviews proposed outcome before any external effect"
agent_deliverable: "Human-readable cash-payback-stress-screen review workpaper with evidence, assumptions, alternatives, unresolved questions, proposed result and corrections diff"
correction_vector: "Authenticated human REJECT/correction: persist HUMAN_OVERRIDE with exact permitted correction, invalidate relevant semantic cache (SEAM-B01 proposed), append a new source-linked L1 derivative/digest, block stale active envelope until revalidation"
---

# Cash Payback Stress Screen

## Goal
Stress-test whether a small-business promotional offer can repay acquisition spend without a liquidity shortfall.

## Proof
A cash-flow scenario exposes the earliest break-even date, minimum balance and downside scenario; insufficient data produces HOLD.

## Steps
1. Set acquisition outlays and collection delays.
2. estimate conservative contribution receipts.
3. model cancellations and refunds.
4. compare with available funds and fallback manual baseline.
5. require review before external offer.

## Boundary
Prospective receipts never become CASH_YIELD_VERIFIED; zero-payback promise forbidden.

## Inputs and outputs
Input: authorized and minimized first-party business data or synthetic lab records, declared source provenance, and permissible scope.
Output: a self-contained BOSS research workpaper with assumptions, metrics, declared uncertainty and a qualified recommendation or HOLD.

## Falsification
Any required economic, authorization or independent evidence operand absent → HOLD / NOT_ESTABLISHED. Any asserted settled financial outcome without independently reconcilable records → G5_HOLD.

## Source context
Source ID HORMOZI-100M-LOST-CHAPTERS-2025-001; topic area: Section B, printed pp.53–66. The steps are original BOSS design, not a reproduction or official implementation of the author's text.

## Cash preservation gate — candidate enforcement contract
Bind the proposed acquisition spending decision to the Phase 4 VALUE ledger; record a fixed 30-day cohort/window, **realized settled collections** within that window, attributable CAC committed/paid, and incurred/contractually unavoidable fulfillment costs during the same window. For comparable evidence:
`NET_30D_CASH_CONTRIBUTION = REALIZED_30D_COLLECTIONS - CAC_30D - FULFILLMENT_CASH_OUTFLOW_30D`.
The supervisor requests `CASH_NEGATIVE_TRIP` when this value is negative. The *design* shall place the affected campaign in HOLD before any additional automated paid spend or discount issuance. Explicit human Zone C deficit acceptance may authorize a bounded experiment only after cash reserves, obligations, exposure ceiling, period and compensating operating plan are reviewed. That authorization is not evidence the plan is profitable.

Keep `LTGP` (cohort lifetime gross profit), `CAC`, accounting contribution margin, realized cash receipts, refunds, prepaid balances and payable timing separate. An accrual-cost comparison is not automatically a cash comparison. Where only estimated figures are available use `FORECAST_CASH_DEFICIT_HOLD`, not a claim that actual cash has gone negative. Missing amounts/cohort alignment → `HOLD / NOT_ESTABLISHED`.

**Runtime state:** BROKER TRIP, ROUTING FREEZE and LEDGER SINK **NOT_IMPLEMENTED / NOT_TESTED**; this SKILL.md is not a deployed circuit breaker.

**Falsification:** A negative reconciled 30-day cash contribution permits another automated campaign charge or unbounded discount issue → FAIL.

## Human–Agent interface candidate
Human dependency: Human provides context and authorization for Stress-test whether a small-business promotional offer can repay acquisition spend without a liquidity shortfall.; reviews proposed outcome before any external effect.
Agent deliverable: Human-readable cash-payback-stress-screen review workpaper with evidence, assumptions, alternatives, unresolved questions, proposed result and corrections diff.
Correction: Authenticated human REJECT/correction: persist HUMAN_OVERRIDE with exact permitted correction, invalidate relevant semantic cache (SEAM-B01 proposed), append a new source-linked L1 derivative/digest, block stale active envelope until revalidation.
If operation exceeds the explicitly approved Equivalence Set or financial limit, require `ZONE_C_ESCALATION_REQUIRED` and prevent dispatch. No runtime implementation or probe qualification is claimed.
