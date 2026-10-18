# BOSS React Library Policy — v0.1 (PROPOSED)

**Scope:** DraftDeck's 16:9 slides, responsive lesson interfaces, future landscape/portrait/square infographics, and the separate 11 × 17 in print publication. **Authority:** `design-system/boss-design-contract.json` and `doctrine/visual-evidence-gate.md` override library defaults. This policy grants **no** visual or release approval.

**Design principle:** **One source. Multiple delivery formats. One visual quality standard.** Third-party packages may provide accessibility, behaviors, preview/testing, or pagination. **They may not author BOSS visual identity, substitute generic UI for approved art, or bypass human approval.** Maintain original Bioscillate cyan/magenta/black branding, editorial typography, source-provenant concept artwork, and subtle CAD grid, zones, callouts, and title plate. No SVG-based slide construction; keep editorial text native and selectable, separate from artwork. Do not presume ANSI/ISO certification.

## Admissible GitHub references (not installed or approved)

| Role | Candidate | License reported by project | Allowed use |
| --- | --- | --- | --- |
| Interactive headless controls | [Radix Primitives](https://github.com/radix-ui/primitives) | MIT | Keyboard/focus/dialog/menu behavior with BOSS-owned CSS |
| Alternative interactive controls | [React Aria](https://github.com/adobe/react-spectrum) | Apache-2.0 | Accessible interaction patterns and i18n; no imported visual theme |
| Alternative interactive controls | [Base UI](https://github.com/mui/base-ui) | MIT | Unstyled controls with BOSS-owned CSS |
| Component inspection | [Storybook](https://github.com/storybookjs/storybook) | MIT | Isolated component review, documented variants, regression evidence |
| Print pagination experiment | [Paged.js](https://github.com/pagedjs/pagedjs) | MIT | Browser paged-media experiment for 11 × 17 in; **not** a printer/prepress certification |

**Choose one** headless interaction library per proof-of-concept implementation after testing; do not install or blend all three by default. Static editorial content needs no component library. Storybook is a development tool; Paged.js is a print-layout tool, **not** a React design-system replacement.

## Adoption gates

1. **Provenance and rights:** Record upstream repository, exact package/version, dated license/NOTICE review, dependency tree, security advisories, maintenance, and commercial-use obligations. No copying reference artwork or themes without separate rights verification.
2. **Technical fit:** Demonstrate React/build compatibility, keyboard and screen-reader operation, focus states, semantic HTML, text editability, deterministic builds, font availability, and reasonable bundle/runtime cost. Test against the existing BOSS token and content contracts; document unsupported behavior.
3. **Visual independence:** Render with BOSS source art and typography. No forced component styling, decorative cards, generic wireframes, SVG slide text, or substituted logo. Compare actual browser pixels with the human-selected editorial concept.
4. **Output evidence:** Record real 1920 × 1080 slide and true 11 × 17 in print-page geometry separately; annotate grid, title block, callouts, clipping, color and legibility. Test Paged.js page breaks, live text and exported PDF dimensions. Press bleed, binding allowances, color management and final PDFs require the chosen printer's specification and physical proof.
5. **Human release boundary:** Structural checks and screenshots permit review **only**. Record `PASS`/`FAIL`/`NOT_TESTED` per gate and an explicit human selection; Canva/import editability and print acceptance are separate. Missing evidence is **HOLD**.

**First PoC:** One art-first BOSS editorial scene expressed as a 16:9 teaching slide and an **independently composed** 11 × 17 in magazine page; add one accessible navigation/control using a single headless candidate. Prove source → story/art → HTML layers → browser capture → print PDF against the same source manifest. Hold infographic formats for the next measured adapter test.

**Status:** POLICY PROPOSED, CANDIDATES NOT INSTALLED, PoC NOT YET QUALIFIED. Update this policy only through reviewed, versioned changes.
