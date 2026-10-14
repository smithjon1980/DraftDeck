# BOSS Capability Quadrants — Project-Wide Candidate Crosswalk
Document: BOSS-CAPABILITY-QUADRANTS-CROSSWALK-001
Status: SPECIFIED_CANDIDATE / NOT_TESTED / NO RELEASE AUTHORITY
Scope: SOHO internal tools, Market 7 barbershop reference, Day Zero–Day Seven, Capability Foundry, Book-to-Skills and DraftDeck.
Authority: Phase 1 governing baseline remains unchanged. SEVEN (Survey → Evaluate → Validate → Execute → Normalize), K0–K4, G1–G5 and Zone C prevail.

## Classification and placement
| Lens | Four mutually distinguishable primary functions | Question | Project placement |
|---|---|---|---|
| A — Capability assignment | PEOPLE (human identities/abilities/entitlements); AGENTS (registered delegate identities/roles/scopes); SKILLS (versioned procedures, proof and boundaries); TOOLS (resources/interfaces/actions) | Who acts, by what procedure and authorized tool? | Capability Foundry assignment contract; per-SKILL human_dependency, agent_deliverable, correction_vector; workflow role-to-permission mapping |
| B — Minimum sufficient intervention | SCRIPT (deterministic bounded procedure); PROGRAM (existing reusable application); NARROW AI (task-specific learned inference); GENERAL AI (open-ended model) | What is the least costly sufficient intervention? | Governed discovery/Automation Suitability Gate, technology selection record, Day Zero lesson and SOHO prototype choices |
| C — Operational performance | SOP (prescribed procedure); KPI (continuous health measure); OKR (time-bound improvement goal/results); CAPA (corrective/preventive improvement record) | How is work defined, measured, steered and repaired? | Operator workpapers, business outcomes, Phase 4 VALUE evidence and training exercises |

MECE applies to **primary roles/functions within each lens**, NOT all computing or business phenomena. A script calling an LLM uses GENERAL AI inference despite its script wrapper; tools may be used by people or agents. KPI can be an OKR's key result without becoming the same management function. Manual/no-change is a pre-classification intervention option, not a forced fifth quadrant.

## Workflow correspondence contract
For each workflow step declare: operation_id, human_role, human_ability_requirement, human_entitlement, agent_id and delegated_role (or NONE), skill_id/version, permitted_tools/actions, selected_intervention_class, rejected_alternatives_with_rationale, SOP_id, KPI_measurement_spec, OKR_reference (optional), CAPA_trigger (conditional), source/evidence status, approval_checkpoint, correction_vector, test_status, and governing G1–G5 applicability.

Fail closed on missing authorization, unqualified skill or evidence. Human enthusiasm, prompt instructions or app credentials never confer production authority. Actual technical gates remain UNIMPLEMENTED/NOT_TESTED unless independently demonstrated.

## Market 7 barbershop miniature
People: barber owner establishes operating rules, customer requests booking. Agent: optional assistant proposes a plan and reports limits. Skill: appointment intake/queue estimate. Tools: PocketBase local data, Go and HTMX as suitable, Windmill optional, Railway optional hosting; REA researches permitted public reference flows.
Intervention: existing software/manual first; a deterministic availability check or script before any narrow or general model. SOP: check-in and conflict handling. KPI: observed on-site wait and ETA error (do not mistake estimated savings for actual savings). OKR: a separately declared test-period customer experience goal. CAPA: investigate double-booking or estimate failure; preserve correction and retest. All measures hypothetical until recorded trials.

## New dependency decisions
- Capture quadrants in Candidate Architecture crosswalk, not in Kernel authority declarations.
- DraftDeck Book-to-Skills: extract role/tool/skill relations, intervention class and SOP/KPI/OKR/CAPA implications as **source-derived or BOSS-design-inference** separately.
- Day Zero: manual card sorting and decision exercises before code; Day One–Two only add necessary technology.
- Existing skills are NOT automatically upgraded, qualified or executable by this crosswalk. New template/schema changes require a separate integrity check and human review.
- Preserve rejected alternatives via REJECTED_HYPOTHESIS / SUPERSEDED_CANDIDATE with rationale; no source authority promotion.
- Proposed checks Q-A01 missing entitlement → HOLD; Q-B01 script suffices but general LLM recommended without benefit → reject escalation; Q-C01 KPI without numerator/denominator/window → NOT_ESTABLISHED; Q-C02 CAPA closes without retest evidence → FAIL. All NOT_TESTED.

## Non-displacement
BOSS is the portable governed method, Market 7 its reference implementation, DraftDeck its instructional/design production specialization. The three quadrant lenses are analytical views, NOT new SEVEN phases, architectural layers, a product or new mandatory software stack.
