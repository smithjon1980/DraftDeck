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
3.  **Hosting:** Public HTTPS hosting is an optional preview/import route (e.g., Vercel, GitHub Pages); an approved hosting destination is currently unknown.
4.  **Canva Import:** After creative approval, use the available connector's supported source argument. The reported connector schema accepts either an absolute local artifact path in `design_file` or a public HTTPS `url`, never both. Verify actual connector availability and behavior before importing.

## 3. Canva Integration Test Results & Limits
*   **Evidence correction:** A prior session reports a successful local HTML import at 1920×1080 with sixteen accessible text-containing elements. This session has not independently reproduced that result. Public HTTPS is not a universal requirement for the reported local-file route.
*   **Fidelity:** Text editability, image independence, logo fidelity, and visual placement must be checked on the actual imported design. Historical import success is not creative approval.
*   **Structural Conversion:** Conversion of CSS borders, grids, and flex layouts to independently editable Canva shapes is unverified. Do not claim it without inspecting the result.
*   **Page structure:** Static HTML imports require top-level `section[data-document-role="page"]` elements with no nested page containers.
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

## 6. Current Composition Candidate Inputs
* Jonathan Smith is creative director and final approver. The first logo-free candidate was rejected.
* Read `episode01/reference/GEMINI_RECONCILIATION.md`, then `Visual_Authority_Spec_v1.0.md` and `slide-copy.candidate.json`, supplied at main commit b96b358.
* Use exact candidate wording for Slides 01, 02, and 06. This supersedes the previously unresolved copy fields. No rendered slide approval is established.
* Use `episode01/assets/brand/bioscillate-original-supplied.jpg` unchanged. A reduced lockup is not supplied; scaled full-logo rail usage is a documented candidate proposal.
* No governing rendered reference or additional illustration was supplied. Compose from the textual spec and label geometry/fonts as proposed; do not claim reproduction of an approved image.
* Root black-text rule remains the default; the supplied Slide 02 candidate specifically requests a gray Network-Driven Opportunity header. Apply grayscale only to that header.
* Slide 01 footer and internal metadata remain unknown. Slide 06 participants, message labels, arrow directions, and decision gates remain unknown; use the five exact ordered labels without inventing protocol semantics.
* The Sequence/Precedence/Grouping ZIP is an unapproved orientation reference, not the Pitch copy source.
* Show actual browser renders before requesting creative approval. Discrete static HTML and Canva verification follow author approval.
