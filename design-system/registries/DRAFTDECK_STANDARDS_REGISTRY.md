# DraftDeck Standards Registry
**Version:** 1.0.0  
**Profile:** BOSS Day Zero, Episode 01  
**Status:** CANDIDATE — commit records the proposed controls; it does not supersede existing canonical doctrine.

## 1. Operational mandate
DraftDeck operates as a reference-first reconstruction compiler. Each visual mechanism and editable text element must trace to an approved reference or explicit design decision. Generic substitutions are forbidden. Rendering and adapter output are not evidence of instructional fidelity.

## 2. Five authorities
1. **Engineering standards:** ISO 5457 and ASME Y14.2 are adapted drawing-convention references, not a claim of formal conformance.
2. **Interface design:** fluid-constrained grid, named layout zones, typography sizes and text-flow constraints.
3. **Story:** preserve subjects, actors, direction and the four original workstation relationships on EP01/S01.
4. **Editorial:** approved copy and punctuation as editable native text; visible corrections recorded.
5. **Constitutional controls:** three layers ART / STORY / TEXT; KEEP / REIMAGINE / DISCARD; reference-versus-render compare before release.

## 3. Traceability contract
Every processed element requires `element_id`, `layer`, `governing_standard`, `design_token`, `source_reference`, `salvage_classification`, `mandatory_relationships`, `forbidden`, and `acceptance_test`. The JSON file is the machine-readable contract. Verbal acceptance tests are not automatically executable: runtime validation and image comparison are separate gates.

## 4. Dependency & precedence
Existing `doctrine/production-contract.md`, `doctrine/composition-standard.md`, and `skills/draftdeck/SKILL.md` remain canonical unless formally amended. This candidate applies only to the explicit `boss-day-zero-ep01` profile and does not alter the flagship visual standard.

## 5. Reconciliation before promotion
| Item | Existing core doctrine | Candidate values | Gate |
|---|---|---|---|
| Palette | #FFFFFF, #1A1A1A, #B34700, #DEDEDE | #FFFFFF, #000000, #00FFFF, #FF00FF | Verify logo asset and authorize scoped palette |
| Typography | Georgia, Courier New, Arial | Inter, Fira Code | Approve the Episode 01 type profile |
| Line weights | 1pt, 0.5pt, 0.25pt | 2px, 1px, 0.5px | Normalize units at 1920×1080 |
| Standard references | Adapted CAD/ISO vocabulary | ISO 5457 / ASME Y14.2 | Define applicable clauses; don't claim certification |
| Exact copy | Theory Master and approved slide corrections | "YOU ALREADY MOVE INFORMATION" | Compare against exact source and verify correction |
| Story provenance | NotebookLM PDF Slide 01 | Four-node workstation scene | Pin local asset ID/hash for machine comparison |

## 6. Release gates
**ADMIT** source/reference → **EXTRACT** ART/STORY/TEXT → **CLASSIFY** each element → **ASSEMBLE** using native editable layout → **COMPARE** reference and render → **VERIFY** text collisions, story fidelity, and adapter edits → **AUTHORIZE** release.

Current status: `COMMITTED_CANDIDATE` does **not** mean `RENDER_VERIFIED` or `RELEASED`.
