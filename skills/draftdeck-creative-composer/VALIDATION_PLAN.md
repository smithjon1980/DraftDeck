# DraftDeck Creative Composer — First Vertical Slice Validation Plan

**Status:** PLAN ONLY · NO ARTWORK GENERATED · NO END-TO-END RUN · NOT A RELEASE
**Scope:** One authentic NotebookLM slide/page or infographic Spark, one original 16:9 editable DraftDeck composition.

## Test preconditions
1. Actual NotebookLM reference supplied or authenticated; accessible page/file and digest, rights, issue source manifest and approved exact instructional wording.
2. A human decides on individual proposition/expression items (ACCEPT / REJECT / AMEND), rather than auto-promoting a Spark's contents.
3. Gate 1 approval for complete upstream Slide Creative Contract; no artwork generation before authorization.
4. Generate actual bounded Retell or Reimagine candidate images; human selects one at Gate 2; record real hash and rationale.
5. Build a manufacturer-only packet and prove it validates against the allowlisted JSON Schema. Explicitly test that adding `artwork_brief_prompt`, `raw_notebooklm_pdf`, `prompt_history`, `unselected_candidates`, or other unknown keys fails schema validation.
6. Manufacture original React/Tailwind HTML with separate artwork and editable instructional copy, not a composite image. Render in Chromium.
7. Independent QA captures: approved claim/copy match; new creative-contract correspondence; overflow/font/layer inspection; explicit text-edit → save → reload → retained-string test in the declared editable target; source/asset hashes; human review.
8. Gate 3 release decision remains distinct; anything prior to actual human approval is `RELEASE_HOLD`.

## Scored evidence matrix (each separately reported)

| Test ID | Evidence and pass condition | Initial state |
| --- | --- | --- |
| SRC-01 | Admitted authentic Spark with stable identity, rights state and source/claim locators | NOT_EXECUTED |
| GOV-01 | Human source selections and provenance for propositions and expressions | NOT_EXECUTED |
| GATE-01 | Recorded human creative direction approval | NOT_EXECUTED |
| IMG-01 | Original text-free candidate artwork and human selection receipt; bytes hashed | NOT_EXECUTED |
| GATE-02 | Human artifact selection distinct from creative contract approval | NOT_EXECUTED |
| BND-01 | Only allowlisted manufacturer fields; negative injection tests reject upstream-only fields | NOT_EXECUTED |
| WEB-01 | Independent artwork and exact text in a functional React/Tailwind 16:9 scene | NOT_EXECUTED |
| QA-01 | Meaning/copy verified from accepted sources, no invented statistics or claims | NOT_EXECUTED |
| QA-02 | Visual judged against new approved treatment (not source pixel parity) | NOT_EXECUTED |
| QA-03 | Actual independent text edit/save/reopen persisted with no artwork flattening | NOT_EXECUTED |
| GATE-03 | Separate human release authorization after inspecting QA | NOT_EXECUTED |

A render, passed JSON Schema, SVG file, or green workflow is not sufficient to infer an approved presentation or completed DraftDeck workflow. If a tool, authentic source or approval is missing, mark the applicable test NOT_ESTABLISHED / HOLD.

## Follow-on milestones
Only after single-slide verification: (a) multi-slide deck with consistent component reuse and unique source IDs; (b) editable infographic from the same accepted proposition ledger; (c) exports and reopening checks for whichever target authoring formats the human specifically requests. Keep production branches untouched until a separate adoption decision.
