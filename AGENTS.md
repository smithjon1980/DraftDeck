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
