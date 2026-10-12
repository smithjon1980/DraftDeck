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
