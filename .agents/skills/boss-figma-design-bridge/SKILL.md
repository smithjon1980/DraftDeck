---
name: boss-figma-design-bridge
description: Governed optional Figma design-specification and component-handoff bridge for BOSS Storybook slides and responsive Bioscillate web experiences. Use only after source/reference admission, with independently approved art and story before full composition.
---

# BOSS Figma Design Bridge — candidate v0.1

## Position in the existing system
Read `AGENTS.md`, `design-system/boss-design-contract.json`, `doctrine/figma-design-bridge.md`, `doctrine/visual-evidence-gate.md`, `.agents/skills/boss-precomposition-human-approval/SKILL.md`, and `.agents/skills/boss-react-art-story-submission/SKILL.md`. Figma is an **optional editable design/specification workspace**. It does NOT replace GitHub as the source of versioned rules, React/Tailwind as production components, or Windmill, n8n, Railway and GitHub Actions as execution infrastructure. No automatic Figma-to-production publishing.

## Entry gates — fail closed
1. Admit exact source copy (stable manuscript ID/revision, paragraph IDs and text digests), approved visual references with SHA-256 and approved **scope**: `COMPOSITION_ONLY`, `STYLE_ONLY`, or enumerated `CONTENT_APPROVED`. No reference or no source digest => HOLD.
2. Read the story bridge and storyboard before selecting a composition. The current Day Zero Section 01 candidate is `BOSS.EP00.A01.S01 v0.7` (HAVE: Human Authority, Verified Execution); use its source-lock and P001–P025. Earlier "The Work Must Survive the Conversation" images are references, not the new narration or new story setting.
3. Lock exact brand palette #FFFFFF (ground), #000000 (ink), #00BCEB (cyan), #E30074 (magenta), approved identity assets and CAD/ISO-informed hairline/title-block hierarchy. No generic palette, invented logo, stock collage, dark theme or baked manuscript text.
4. Distinguish two Figma modes:
   - `LAYOUT_STUDY`: an **uncomposed** CAD/design exploration with placeholders explicitly labeled nonproduction. Permitted before art/story approval, never promoted to a completed slide or release proof.
   - `COMPOSITION_HANDOFF`: full art + story + text specification only after separate human ART and STORY approvals tied to the exact hashes, slide ID and visual target, plus a locked source transcript. Approval evidence must originate from the operator, not from Figma or a model.
5. For web `WEB_COMPONENT_SPEC`, approved design tokens, user flows and content are required. A Figma screen is not a functional, accessible, deployed website.

## Seven variants and target profiles
- For Episode Zero's SEVEN experiment reuse the **exact seven named, independently placed layout plans** in `experiments/episode-zero-seven-phase1/scripts/layouts.mjs`. All plans provide illustration, analytical framework, verbatim narration, reflection and notes. The five user-supplied image references are scoped inputs; 5 references × 7 layouts = 35 **comparative studies**, not 35 approved original artworks.
- The SEVEN experiment's **17 × 11 in** page is its own profile. The production slide is **1920 × 1080 px (16:9)**: recompose intentionally; do not stretch 17:11 to 16:9 or claim geometry parity by scaling.
- For responsive web establish independent desktop, tablet and mobile frames. Record tested breakpoint ranges, typography, content reflow, interactive states, bilingual English/Spanish expansion and keyboard focus behavior. Never resize a fixed slide into a mobile site.
- Figma tokens/components are a **projection** of GitHub BOSS source tokens; change the authoritative design token contract via governed Git workflow rather than silent edits in a Figma file.

## Figma output and developer handoff
- Record source/ref hashes, Figma file key + exact frame/node IDs and version/link, output target, composition variant, token snapshot and native-text/art/story separation evidence; do not claim the generated Figma design used reference pixels unless the originals were actually uploaded and verified.
- Preserve `ArtLayer`, `StoryLayer`, `TextLayer` as discrete responsibilities at implementation. Independent original artwork may be placed as a traceable asset inside React `ArtLayer`. Editorial text MUST be native HTML, not Figma raster, SVG text or canvas.
- Rebuild the specification in React/Tailwind; do not promote auto-generated code or flattened exports without review. Capture actual 1920×1080 Chromium render for slides, multiple real browser widths for web. Compare reference ↔ Figma frame ↔ React render with annotated differences.
- Run existing source-copy, layer-origin, clipping, responsive/accessibility and PDF/adapter tests. Figma editable layers prove only Figma editability; Canva, Adobe, browser, or other destination edit-save-reopen need distinct tests.
- Save only **public-safe** manifests and skill rules to public GitHub. Unpublished manuscript bytes, reference artwork and Figma sharing links exposing private content stay owner-controlled. Apply least-privilege connection permissions and confirm paid generation cost/plan before invoking.
- Report `PASS`, `FAIL`, `NOT_TESTED` separately for source digest, visual reference, token equality, variant geometry, art approval, story approval, native text, browser parity, web accessibility, target editor and human release. Any missing evidence = HOLD.

## Human controls
Figma can prepare candidates; it cannot mint ART/STORY approvals, satisfy manuscript author confirmation, merge a PR, bypass protected transport, or release production. The operator separately chooses art, story, composed slide/web screens and public release. Previous automatically generated Figma presentation candidates are **not** accepted visual masters merely because they exist.
