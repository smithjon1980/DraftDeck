# DraftDeck — Phase-Gated Pipeline and Evidence (candidate rebuild)

## What has been established
- Earlier HTML → Canva experimentation demonstrated some editable elements and highlighted serious visual-fidelity problems. It is **historical research only**; Canva is not in the current renderer.
- Node/Playwright/Chromium produced genuine PDFs in prior isolated candidate trials; those do not establish a live generative swarm.
- **Go + Tailwind + Chromium GitHub Actions run 38345114996**, job 115124603718, completed with all job steps successful; generated PDF reported 54,822 bytes and SHA-256 `da6ef261573b1bed2d980dd8eedf4565402d327e32d23f6aa2b859ad58b1f375`; a CI artifact was uploaded. User inspected `day-zero.pdf` and classified it as a **low-fidelity wireframe because the Story and Art layers were missing**.
- Those checks establish **Phase 1 execution**, NOT high-fidelity completion, independent visual reference acceptance, fully autonomous agents, or durable delivery.

## Phase 1: structure / LOW FIDELITY
Test question: Can Go create semantic HTML from governed source data, Tailwind compile styles, and Chromium export a structurally valid, single-page 16:9 PDF?
Evidence: `day-zero.html`, `styles.css`, `day-zero.pdf`, `manifest.json`, GitHub Actions logs, provenance, screenshots.
Decision: **P1_TECHNICAL_PASS** when checks pass; **P1_HOLD** when they fail. Retain a visual review record; do not invent a Story asset.

## Phase 2: composition / MEDIUM TO HIGH FIDELITY CANDIDATE
Test question: Can independently scoped Story, Art, and Text specialist workers produce assets and components that Go assembles without cross-layer modification?
Story = PNG/WebP, text-free. Art = HTML/CSS editable diagram and spatial structure, no SVG. Text = exact semantic HTML/structured copy. Assembly = deterministic Go template/Tailwind CSS. PDF/preview = Chromium.
Evidence: scene contract, role assignments, independent layer hashes, visible composite, text edit/select test, repair ledger. Must inspect resulting actual page. **P2_HOLD** until all required layers are present.

## Phase 3: QA / HIGH FIDELITY RELEASE
Test question: Does output match reference sufficiently, survive PDF QA, and qualify for approved, durable delivery?
Evidence: reference-versus-output screenshots, exact-copy report, contrast/clipping/overflow checks, text extraction, copyright/asset rights, integrity hashes, human approval and persistent storage read-back.
**RELEASE_HOLD** until every required gate passes.

## Forbidden paths and meanings
- NO SVG files, tags, icons, format conversions, or intermediate exports.
- No React build/runtime, Canva conversion, or PowerPoint.
- Do not treat CSS-drawn art as a completed generated illustration if Story is absent.
- Do not label a GitHub Actions green check as visual acceptance.
- Do not label a seven-day Actions artifact link as persistent storage.
- Do not label deterministic fixture nodes 'live AI agents'.

## Migration guidance
Existing `skills/draftdeck/scripts/build_slide.py` was a Canva/SVG-capable Python experiment. It is retired from production. The Go experiment remains **candidate**, not automatically a production replacement. The integration of true Story/Art/Text workers in Go and full visual QA remains open.
