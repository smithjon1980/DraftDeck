---
name: lead-stage-definition
description: Research-only BOSS adaptation of sketches in Alex Hormozi's $100M Journal.
version: 0.2.0-candidate
source_ids: [HORMOZI-100M-JOURNAL-2023-001]
operational_phase_tags: [DISCOVERY]
enforcement_tags: [G1]
trust_class: UNVERIFIED_EXPLORATORY_SOURCE
qualification_status: SPECIFIED_CANDIDATE
test_status: NOT_TESTED
authority_scope: RESEARCH_ONLY
evidence_refs: []
human_dependency: "Human supplies evidence and business context for Define distinct lifecycle states and denominators for a small-business acquisition funnel. and explicitly reviews any proposed external action"
agent_deliverable: "Human-readable lead-stage-definition decision workpaper: facts, assumptions, evidence references, conflicts, suggested action, rejected alternatives, and review diff"
correction_vector: "Authenticated human correction/REJECT channel: record HUMAN_OVERRIDE with exact authorized correction, invalidate affected semantic cache (proposed SEAM-B01), derive new L1 digest preserving history, hold stale envelopes pending confirmation"
---

# Lead Stage Definition

## Goal
Define distinct lifecycle states and denominators for a small-business acquisition funnel.

## Proof
Each transition has event evidence, qualification condition, actor and observable time; prevent counting inquiry as paid conversion.

## Steps
1. Choose minimal states.
2. define event-based entry/exit.
3. separate raw, engaged, qualified, sold.
4. log invalid transitions.
5. test sample cases.

## Boundary
Do not treat marketing reach as lead or lead as customer. No hidden personal-data collection.

## Inputs and outputs
Input: inspected journal pages and source-linked business context.
Output: an original, bounded, independently reviewable candidate artifact.

## Source provenance
HORMOZI-100M-JOURNAL-2023-001; journal pp. 67–78 and pp. 125–131 (qualification, stages and Core Four diagrams). The journal is exploratory and its drawings are not independently validated operational procedures.

## Falsification
A proposed capability with ungrounded labels, missing denominators, unsupported profit claims or omitted authority boundaries is rejected/HOLD instead of promoted.

## Mandatory authoritative transition contract
For the proposed small-office prototype, PocketBase is the **selected candidate Authoritative State Service**, not yet a verified running production state service. A state transition from `ENGAGED_PROSPECT` to `QUALIFIED_LEAD` requires a deterministic eligible event (e.g., verified intake-form submission or a booking receipt), stable `event_id`, `idempotency_key`, `source_id`, `actor_id`, `from_state`, `to_state`, `event_time`, `receipt_digest`, `qualification_rule_version`, and an explicit authorization decision. Events must be authenticated and validated against the declared rule; mere existence of a form submission does not prove suitability, consent or a sale.

An LLM-generated sentiment score, classifier label or persuasive message is NEVER sufficient to advance the authoritative stage. PocketBase persistence must not be considered an independent cryptographic receipt merely because an event row exists. Conflicting replay or duplicate keys are refused or routed to reconciliation; uncertain side effects follow `UNCERTAIN → REQUIRES_RECONCILIATION`, never blind retry.

**Current status:** schema requirement only; PocketBase transaction hooks, atomic idempotency and independent evidence sink remain **NOT_IMPLEMENTED / NOT_TESTED**. No live customer identities or automated funnel execution are authorized.

## Human–Agent interface candidate
Human dependency: Human supplies evidence and business context for Define distinct lifecycle states and denominators for a small-business acquisition funnel. and explicitly reviews any proposed external action.
Agent deliverable: Human-readable lead-stage-definition decision workpaper: facts, assumptions, evidence references, conflicts, suggested action, rejected alternatives, and review diff.
Correction: Authenticated human correction/REJECT channel: record HUMAN_OVERRIDE with exact authorized correction, invalidate affected semantic cache (proposed SEAM-B01), derive new L1 digest preserving history, hold stale envelopes pending confirmation.
When requested action exceeds the explicit Equivalence Set or financial authority, require `ZONE_C_ESCALATION_REQUIRED` and no dispatch. Documentation only; NOT_IMPLEMENTED / NOT_TESTED.

## Three-Quadrant Conformity (Candidate)
- **A — Assignment:** Human entitlement and ability: NOT_ESTABLISHED until operator provides evidence; agent role: DESIGN_ASSISTANT_ONLY; skill: `lead-stage-definition`; tool access: NONE_ASSUMED. Check the existing `human_dependency`, `agent_deliverable`, and `correction_vector` fields.
- **B — Minimum sufficient intervention:** Evaluate manual/no-change, SCRIPT, PROGRAM, NARROW_AI and GENERAL_AI in that order subject to suitability; selected class NOT_ESTABLISHED until the specific task is scoped; record rejected alternatives.
- **C — Operational performance:** SOP reference: CANDIDATE_ONLY; KPI definition/baseline/denominator/window: NOT_ESTABLISHED; OKR reference: OPTIONAL/NOT_ESTABLISHED; CAPA: record observed defect, correction authority, retest evidence and outcome. Never treat an untested KPI as a measured improvement.
- **Stop rule:** missing entitlement, material evidence, valid intervention economics or authorization -> HOLD. This overlay does not authorize execution or imply operational qualification.
