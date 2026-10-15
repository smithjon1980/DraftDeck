# DraftDeck Creative Composer · Candidate Trial

**Route:** draftdeck-creative-recomposition-v1-candidate
**State:** STAGED FOR ONE-SLIDE VALIDATION · NOT EXECUTED · RELEASE_HOLD
**Repository branch:** feature/creative-composer-trial

This directory specifies a new **Retell or Reimagine** pipeline for original instructional presentations and infographics inspired by NotebookLM Sparks. It does not ask workers to trace the source page, reconstruct the exact reference layout or promote Spark claims into doctrine.

| File | Function |
| --- | --- |
| SKILL.md | Seven stages, three human gates and manufacturing boundaries |
| SUPERSESSION_CROSSWALK.md | Scopes conflicting legacy specifications for this experiment without deleting them |
| schemas/slide_creative_contract.yaml | **Upstream-only** editorial/art-direction template, may contain creative prompt |
| schemas/restricted_manufacturing_handoff.yaml | Illustrative minimal manufacturing carrier, with invalid placeholders until actual authorization |
| schemas/restricted_manufacturing_handoff.schema.json | Machine-readable positive allowlist for actual downstream packets |
| VALIDATION_PLAN.md | One-slide end-to-end acceptance and negative tests |

**Important:** The document named `slide_creative_contract.yaml` is **not** the restricted manufacturing handoff; it includes an artwork brief and must remain upstream. The separate handoff schema prevents accidental promotion of prompts, the original NotebookLM file and rejected assets. A schema is not a substitute for runtime ACLs, path access isolation, human authority or observed testing.

Legacy skill and doctrine files on inherited branches remain unchanged. Project-level promotion requires a later explicit decision and coherent rebuild of conflicting central routing, workflows and QA.
