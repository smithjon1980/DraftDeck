---
name: draftdeck
description: Governed BOSS instructional media pipeline—from grounded teaching story and independent artwork to native HTML/CSS layers, browser/PDF evidence, and explicit human approval. Applies to Episode 01, Day Zero and related web/print instructional surfaces.
---

# DraftDeck — creative-production and visual-evidence skill (candidate rebuild)

## Read first
`AGENTS.md`; `design-system/boss-design-contract.json`; `doctrine/production-contract.md`; `doctrine/reference-render-protocol.md`; `doctrine/visual-evidence-gate.md`; `doctrine/release-qa.md`.

The following **active project-scoped skills** now define the upstream creative handoff:
- `.agents/skills/boss-story-architect/SKILL.md` — source evidence → operational teaching story (Bridge 1).
- `.agents/skills/boss-visual-storyboard/SKILL.md` — teaching story → meaningful art-led/narrative-led/hybrid composition (Bridge 2).
- `.agents/skills/boss-art-asset-producer/SKILL.md` — independent traceable story illustration, verified original logo, crop/resolution records.
- `.agents/skills/boss-art-story-reviewer/SKILL.md` — structural completeness first; actual visual storytelling review second.

Supporting references: `references/editorial-composition.md` (editorial hierarchy), `references/web-engineering.md` (React/Tailwind, tokens, accessibility, separate slide/web/print profiles), `references/visual-acceptance.md` (browser/reference/PDF checks). Historical `references/verified-pipeline.md` applies only to its historical adapter experiment.

These skills are not new source authority. The design contract, verified source material and humans control identity, facts and release. Legacy Episode 01 reference skill updates are historical and **do not supersede** this rebuilt workflow.

## Mandatory SEVEN execution
**Survey** — Pin source/page/timestamp and exact-copy status, approved/candidate reference, business teaching assertion, available source illustrations, original brand asset, audience, profile and target. NotebookLM is a creative spark, never verified fact by itself. Missing inputs become UNKNOWN, not invented.

**Evaluate** — Invoke Story Architect to describe the concrete situation, actors, real operational change, resulting proof, learner observation and reflection question. Invoke Visual Storyboard to specify the relationships that the actual illustration must show. Select story-dominant art, narration-dominant art, or hybrid based on meaning—not a universal box layout. Four A–D variants only at a requested comparison stage.

**Validate** — Before production require a complete Bridge 1/2 record, exact copy manifest, intended story-art identity/provenance or explicit HOLD, original logo hash, protected crop regions and acceptance criteria. A logo is not a story illustration; a table or CAD grid does not substitute for missing scene artwork. Separate rights/status uncertainty from visual merit.

**Execute** — Art Asset Producer preserves or creates the substantive independent illustration. Then compose it in React/Tailwind with CAD/ISO-informed frame, canonical white/black/cyan/magenta brand, original logo, native/selectable editorial HTML, contextual annotations, and the actual learner reflection. The 1920×1080 logical slide scales as a unit; responsive web reflows and print has its own separately approved geometry. A concept PNG may contain provisional text; the production slide must rebuild approved copy as HTML and keep artwork separate.

**Normalize by evidence** — Render the **actual selected slide** in a real browser and capture full-resolution PNG and rendered single-slide HTML. Run `tools/visual-poc/check_story_layers.py` with an authored story-layer manifest to detect absent artwork, logo substitutions and unfinished reflection. Run existing design/brand/evidence checks separately. Compare real artwork/reference and browser/PDF images side by side; failure in semantic artwork, technical export, source copy or adapter editability are different failures. Preserve the minimum failing fixture and corrected re-test.

**Human boundaries** — Source concept review, visual selection, target-editor edit/save/reopen, and final release require their own explicit evidence and decisions. Machine-ready ≠ visually faithful ≠ approved. Never silently publish, import, select a failed winner or infer approval from silence.

## Non-negotiables
- Identity: **Bioscillate Operating System by Seven**; preserve the original sourced logo. White #FFFFFF, black #000000, cyan #00BCEB, magenta #E30074. Historical alternate palettes and retired metaphors are not current design authority.
- Strong visual story artwork, not generic boxes, decorative icon clusters or an empty brand-only slide. A source-traceable independent illustration is a distinct production layer.
- Required teaching text is native HTML: not SVG text, canvas text or a full-slide raster. A standalone illustration asset may be raster or vector if provenance and destination fidelity support it.
- No false compliance claim from CAD/ISO visual influence; no fidelity claim from DPI alone; no source approval claim from generated model output.
- Preserve manuscript/script integrity and confidential unpublished inputs. Do not place owner-only art, video transcripts, source PDFs or rendered drafts in public GitHub/CI evidence unless separately authorized.

## Per-candidate output
Record candidate ID, profile/dimensions, source/copy provenance, Bridge 1 story brief, Bridge 2 storyboard, separate asset source/hash/status, exact logo SHA and story-image SHA, crop and resolution assessment, reflection-question status, HTML source/render hash, browser capture, browser↔PDF comparison, source-art-to-scene comparison, visual gate states PASS/FAIL/NOT_TESTED, adapter results, unresolved issues, and exact human decision/scope.

## Fail closed
- Source/reference unverifiable → **HOLD: SOURCE**.
- No independent story illustration or incomplete relationship → **FAIL: ART/STORY**.
- Placeholder reflection/rewritten required copy → **FAIL: EDITORIAL**.
- Browser output diverges from candidate or source art → **FAIL: VISUAL**.
- Destination editing untested → **NOT_TESTED: ADAPTER**.
- No explicit human authorization → **HOLD: RELEASE**.

A strong brand-consistent diagram without the teaching illustration is still a failed teaching slide. The correct next operation is source/creative repair, not repeated PDF re-encoding.
