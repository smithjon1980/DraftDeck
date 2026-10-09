# BOSS / DraftDeck Agentic Operations Manual
**Target:** Autonomous Code Agents (Codex, etc.) operating in this repository.
**Project:** BOSS · Episode 01 — The Pitch
**Status:** Canonical Directives — Strict Compliance Required

## 1. Master Design Standards & Visual Authority
This project uses a precise, information-dense technical operating interface aesthetic. It is inspired by the Tesla Model Y center touchscreen UI combined with CAD/ISO technical drafting. 
*   **Canvas:** Fixed `1920x1080` (16:9) logical canvas. Must scale dynamically via CSS transforms to fit the viewport. Do not use `h-screen` or `vw/vh` as structural constraints for the internal slide grid.
*   **Background:** Pure White (`#FFFFFF`).
*   **Geometry:** 1px hairline borders (`border-black`), measured padding, strict grid alignments. No rounded corners, drop shadows, or thick decorative borders.
*   **Typography:** Black native HTML text (`h1`, `h2`, `p`, `span`). No canvas drawing for text. No SVG text.
*   **Brand Colors:** Cyan (`#00BCEB`) and Magenta (`#E30074`) reserved exclusively for the canonical bioscillate logo and highly selective emphasis. No generic Tailwind colors (e.g., `cyan-500`) without verifying hex matches. 
*   **Prohibited Metaphors:** No sparse marketing website aesthetics, giant empty hero sections, or generic SaaS feature cards.

## 2. The Production Workflow
1.  **Code Generation:** Agents develop React/Tailwind components in this repository.
2.  **Static HTML/CSS:** The React output must be capable of rendering as clean, discrete HTML/CSS static files.
3.  **Hosting:** Static files and image assets (logos) are hosted on a public HTTPS endpoint (e.g., Vercel, GitHub Pages).
4.  **Canva Import:** The public URL is imported into Canva to generate an editable design.

## 3. Canva Integration Test Results & Limits
*   **Requirement:** Canva's import engine requires a public HTTPS URL. Local file uploads of HTML/CSS are currently unsupported for automated agentic integration.
*   **Fidelity:** Native HTML text elements (`<h1>`, `<div>` text) and `<img>` tags successfully import as editable, movable Canva elements. 
*   **Structural Conversion:** CSS borders and flexbox grids convert into absolute-positioned shapes and lines. They lose responsive CSS properties but remain editable.
*   **Strict Prohibition:** Do NOT use full-slide SVGs, PNGs, JPEGs, or PDFs as workarounds to force visual fidelity. The layout must rely on native DOM elements to ensure downstream editability.

## 4. Known Failures to Avoid
*   **Failure:** Generating a single SVG that looks like a slide. *Correction:* Use HTML/Tailwind `div` structures.
*   **Failure:** Using `h-screen` which causes layout clipping on different monitors. *Correction:* Use a fixed `1920px` by `1080px` wrapper with a `transform: scale()` CSS hook.
*   **Failure:** Inventing placeholder data. *Correction:* Preserve missing values explicitly as `[UNKNOWN]`, `null`, or use the exact provided instructional text.

## 5. Current Milestone
**Deliverable:** Build the React/Tailwind browser preview for **Slides 01, 02, and 06** only.
*   Construct the `SlideCanvas`, `TopMetadataRail` (with canonical logo), `SplitPanelLayout`, and `SequenceDiagram` components.
*   Prove the CAD/ISO geometry and pure-white/black aesthetic without generating the remaining 9 slides.
*   Await human visual approval before expanding the slide deck.

## Two-bridge transformation contract — 2026-10-09

Apply this sequence before composing a NotebookLM-inspired DraftDeck slide:

1. Inspect the actual NotebookLM output visually. Record the source file/page, teaching point, story/metaphor, artwork, relationships, copy provenance, and unknowns. Treat it as the first creative spark, not automatically as approved copy or an exact-composition mandate. Do not substitute a logo, diagnostic, conflicting deck, or rejected candidate for this source.
2. Bridge 1 — NotebookLM to reimagined story: write a source-grounded creative brief that reimagines how the teaching point is communicated. Document what is preserved, what changes, and why. Preserve exact required copy; label proposed copy and new artwork as candidates. Derive the creative prompt from this story, rather than merely arranging extracted text.
3. Bridge 2 — reimagined story to target visual system: translate that concept into the project's approved interface theme. For Episode 01, use the information-dense Tesla Model Y center touchscreen influence, CAD/ISO geometry, and original cyan/magenta/black bioscillate artwork. Do not import another BOSS palette or erase story artwork merely to simplify implementation.
4. Write every image/concept prompt bottom-to-top: background/art foundation; story artwork; structural geometry; original brand assets; primary live-text plan; annotations/supporting text; footer/metadata. Describe each layer's purpose, placement, dependencies, and provenance. Adapt the stack explicitly when the story requires it. Name applicable standards precisely (e.g. ISO 128-2:2022-informed line conventions, W3C CSS Grid, WCAG 2.2 AA contrast). Distinguish project/design tokens from standards requirements; never claim compliance from a prompt or raster render.
5. Hand off both bridge records, exact-copy manifest, ordered layer plan, original assets, candidate status, and acceptance checks. Ideogram is optional creative exploration; Codex can implement the bridged concept directly. Provider choice does not remove either bridge.
6. Build the selected concept in React/Tailwind, compile static HTML/CSS, and retain editorial text as native selectable HTML. Keep logo and story artwork separate. Never flatten the whole production slide or use SVG text as its editorial layer.
7. Inspect actual rendered output for story correspondence, exact copy, original asset preservation, hierarchy, geometry, clipping, and readability. Keep build/text-selection checks separate from visual acceptance. Present proposed deltas for human selection without treating silence as approval. Missing NotebookLM source blocks source-grounded completion, but does not block infrastructure, evidence inventory, or handoff preparation; mark it [UNKNOWN] and do not invent it.

## Four-candidate comparison

After both bridges, produce four meaningfully different composition candidates from the same source-grounded story and exact-copy manifest. Vary visual storytelling, hierarchy, and arrangement within the approved frame; do not vary facts, required wording, brand identity, or evidence limits. Use A–D identifiers. Codex may render four candidates sequentially; this instruction does not require parallel agents or four external image-generation calls.

Evaluate each actual render using a comparison matrix: source/story correspondence; Bridge 1 preservation and creative deltas; Bridge 2 theme fidelity; exact-copy accuracy; original logo/artwork provenance; layer/editability integrity; hierarchy/readability; geometry/clipping. Record PASS/FAIL/NOT TESTED plus concrete evidence. Treat invented facts, missing required copy, substituted logo, or flattened production text as hard failures. Recommend the strongest eligible candidate and explain tradeoffs; keep selection and approval distinct. Human selection governs the final visual master. Do not silently promote the evaluator's recommendation to approval. If none passes, repair the concrete failures rather than selecting a failed candidate by relative score.

## Import evidence correction
Discover the current Canva import schema. A local HTML design_file route has been observed; public HTTPS is not a universal requirement. Treat the earlier section 3 claims as historical reported evidence, not a guarantee. Verify destination editability and visual fidelity separately before claiming success.
