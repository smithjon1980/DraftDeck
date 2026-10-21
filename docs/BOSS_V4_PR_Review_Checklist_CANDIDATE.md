# BOSS V4 Consulting Agency Architecture — review only

## Purpose
Propose an **Engagement-centric Consulting Operating System**: six bounded digital Consulting Practices; Work Commissions, PRIME handoffs, Evidence Chain; and separately authenticated human decisions. This PR is **not** architecture ratification, product implementation, legal credentialing, or permission to release.

## Included changes
- `doctrine/BOSS_V4_CONSULTING_AGENCY_ARCHITECTURE_CANDIDATE.md`: complete authored V4 proposal.
- `schemas/work-commission-v4.schema.json`: candidate JSON Schema 2020-12 from §6.
- `docs/BOSS_V4_State_Machines_CANDIDATE.md`: proposed Engagement and Commission state diagrams.
- `tests/work-commission-v4/`: synthetic valid sample, six rejected-shape fixtures, test runner and boundary README.

## Explicitly excluded
No V3 Episode 01 text/audio changes, UI changes, production credentials, client information, API activation, CI configuration, release, or deployment. `doctrine/README.md` stays unchanged. Historical candidates retain historical scope.

## Acceptance review (V4 §14)
- [ ] **Scope custody:** Unknown/unauthorized sources and tool requests cannot be accessed; schema declarations do not grant permissions.
- [ ] **Work identity:** Durable commission/engagement IDs and idempotency rules reject duplicate external actions.
- [ ] **Handoff:** PRIME package, destination, digests, receipt, independent inspection and final authority are distinct.
- [ ] **Failure semantics:** Unknown, NOT_ESTABLISHED and failed observed tests cannot be conflated.
- [ ] **Evidence:** Shared model/source agreement cannot masquerade as independent corroboration.
- [ ] **Human authority:** Models and receiving practices cannot self-authorize business release.
- [ ] **Change control:** Replaced sources/artifacts invalidate digest-bound acceptance for changed scope.
- [ ] **Knowledge custody:** Cross-client retrieval, unapproved retention and expired source reuse are blocked.
- [ ] **Economics:** Software completion is not proof of customer demand, profit or ROI.
- [ ] **Professional ethics:** Conflicts, legal/permission limits and potential harm support HOLD/decline decisions.
- [ ] **Recovery:** ZIP conflicts, corrupted audio, retry hazards and cancellation must be tested negatively.
- [ ] **UX:** An authorized reviewer can locate evidence and unresolved conditions behind any recommendation.
- [ ] **States:** Review the proposed diagrams' HOLD/resume, escalation, rejection, cancellation, acceptance and authority transitions.
- [ ] **Schema evolution:** `v4-candidate-1` is a proposed structural contract; extensions/migrations need approval.

## Validation record
**Local structural fixtures:** 1 synthetic valid sample and 6 intentionally invalid samples passed the candidate schema checks. **Not established:** live orchestration, runtime policy enforcement, authenticated identity, actual source custody, state transition correctness, CI or deployment. No Section 14 production implementation test is claimed passed.

## Decisions requested
1. Ratify/revise/reject ontology, states and Work Commission fields.
2. Identify owners of execution policy, tenant/source controls, human decision records and release gates.
3. Commission a separate implementation plan only after V4 scope is approved.

**State:** CANDIDATE_PENDING_HUMAN_REVIEW · **Release:** HOLD · **Merge:** human review only.
