# Response → Human Judgment → Outcome Record v0.1

Copy for each new case under cases/. Do not claim a complete raw transcript exists without seeing it.

---
record_id: RL-000
version: 0.1.0-candidate
status: CANDIDATE
date: YYYY-MM-DD
topic: example
prompt_id: PL-000 or UNKNOWN
prompt_match: EXACT_VERIFIED | THEME_LINK_ONLY | NOT_ESTABLISHED
response_origin: GEMINI_EXPORT_VERIFIED | USER_RELAYED_RESPONSE | UNKNOWN
raw_response_location: PRIVATE_ARCHIVE_POINTER_OR_NOT_STORED
raw_response_sha256: NOT_COMPUTED
publication_class: PUBLIC_GENERICIZED_CASE
authorizing_human_decision: PENDING
execution_status: NOT_ESTABLISHED
---

## 1. Source and original task
Question being asked; exactly which input was supplied to the model; status if the exact prompt bytes are not available.

## 2. Response
Literal attributed excerpt **only if present** and allowable, or labeled summary. Include critique/alternatives and response ID. Do not treat an assistant's paraphrase as original Gemini language.

## 3. Human-in-the-loop turn
What the human accepted, challenged, rejected, or asked to constrain. Capture human authority as explicit, not model assumed.

## 4. Operational plan
What was proposed because of the feedback; identify dependencies, stop conditions and change of direction.

## 5. Actual evidence
Repository commit/link, executed test, measured result, source file, or NOT_ESTABLISHED. A commit documenting a plan does not prove the plan ran.

## 6. Lesson
What the case teaches about constraints, disciplined selection, feedback and verification. Distinguish useful scope-specific decision from an alleged universal truth.

## 7. Open issues
Contradictions and next falsifiable experiment, verification requirements, provenance gaps, private/public boundaries.

## 8. Curriculum exercise
Ask the learner to identify an initial constraint, the response, the human decision, one evidence gap, and an improvement that can actually be tested.

## 9. Revision history
Record upgrades separately. Verify exact prompt → response pairing before setting prompt_match EXACT_VERIFIED.
