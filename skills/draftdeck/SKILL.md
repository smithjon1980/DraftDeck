---
name: draftdeck
description: Governed three-phase visual-production skill for 16:9 instructional slides and infographics. Phase 1 builds an editable Go-template/Tailwind/Chromium wireframe; Phase 2 composes isolated Story (PNG/WebP), Art (HTML/CSS), and Text (semantic HTML) layers; Phase 3 independently verifies fidelity, integrity and authorized release. No SVG, React, Canva or PowerPoint in the active rendering pipeline.
---

# DraftDeck — Governed Visual Production (candidate rebuild)

**Status:** Candidate skill specification. Phase 1 Go + Tailwind + Chromium GitHub Actions execution **passed**. Phase 2 generative workers and Phase 3 full visual acceptance are **NOT ESTABLISHED**. Production release **HOLD**.

## Authority and prerequisites
- Read actual source documents and *render the visual reference*, not just extracted words. Preserve exact authorized wording and scene meaning. Mark unverified source/provenance NOT_ESTABLISHED.
- Follow BOSS: **Manual First. Automated Second. Governed Always.** SEVEN: Survey → Evaluate → Validate → Execute → Normalize.
- The supplied reference is visual authority. Do not replace its layout with generic cards simply because they're easier to render. Preserve the approved logistics metaphor: data is cargo; humans senders/receivers; agents couriers; models freight; verification proof of delivery. No retired aviation/travel metaphor.
- Main branch and public releases are out of scope without explicit authorization. Prototyping approval is **not** release authorization.
- Distinguish **design phases** (maturity) from **agent roles** (responsibility).

## Approved active technology
- **Execution environment:** GitHub Actions (isolated candidate branch).
- **Control / assembly:** Go standard library, `html/template`, typed manifests and explicit worker interfaces.
- **Layout:** Tailwind CSS compiled to static CSS; standard HTML/CSS components; **no React runtime**.
- **Render:** headless Chromium HTML → PDF, plus PNG preview when available.
- **Story:** independent PNG or WebP asset with source/prompt/provenance record; no embedded meaningful text.
- **Art:** independent editable HTML/CSS geometry (shapes, rails, linework, connectors, layout tokens), optional raster illustration when specifically needed.
- **Text:** exact, semantic live HTML text and traceable structured data.
- **Forbidden in the active pipeline:** SVG **at any stage**, SVG markup, SVG assets or icons, SVG conversion, React dependency, Canvas flattening of authoritative copy, PowerPoint and Canva-import dependency. A legacy asset sitting in the archive does not authorize reuse.
- Chromium's PDF output may internally contain vector objects; that does not constitute an SVG file or an SVG intermediate. Do not falsely claim a PDF contains no vector graphics.

## Phase gates
### Phase 1 — LOW-FIDELITY WIREFRAME
Goal: establish content hierarchy, approved copy, layout areas, exact 16:9 geometry, page count, spacing, basic responsive/print constraints and repeatable Chromium export.
Outputs: Go scene data, rendered HTML, compiled CSS, PDF, PDF SHA-256, run/commit IDs, evidence manifest, wireframe preview.
Gate: GitHub Actions completes, dimensions/page count/text presence/overflow checks run, no SVG in authored source or generated assets. State **P1_TECHNICAL_PASS** is *not* design acceptance. **Missing Story and Art at Phase 1 is expected**, not evidence of Phase 2 completion.

### Phase 2 — LAYERED VISUAL COMPOSITION
Goal: visually complete the approved wireframe without losing its semantic text.
Supervisor defines one signed/pinned scene contract: source references, canvas, z-order, safe zones, exact copy IDs, typography, brand tokens, layer owners, and disallowed content.
- Story Agent: create **text-free** conceptual visual (PNG/WebP). No instructional lettering baked into pixels.
- Art Agent: produce **HTML/CSS** diagram and structure components. No SVG and no rewriting copy.
- Text Agent: deliver grounded, editable HTML/JSON copy and typographic intent. No raster text.
- Assembly Worker (deterministic Go templates + Tailwind): assemble white base → Story → Art → Text; Chrome preview + PDF; record source/output hashes.
Agents may be model-backed later; mock fixtures do not count as live generative workers.
Gate: each worker's isolated output verified, complete Story/Art/Text visible, editable text preserved, alignment and collisions inspected. Otherwise return **P2_HOLD** with per-layer repair scope; max two repair attempts, then human review.

### Phase 3 — HIGH-FIDELITY VERIFICATION & RELEASE
Goal: independent QA against the actual reference and source.
Verify image/reference composition, typography, contrast, brand identity, precise words, page size and number, bleed/overflow, layer isolation, text selection/extraction, provenance/licensing, SHA-256 integrity, artifact existence, reproducible build evidence and read-back from destination storage.
Independent QA emits PASS / FAIL / NOT_ESTABLISHED with screenshots/logs; supervisor cannot certify itself. Release requires explicit human approval **and** independently checked persistent storage URL. GitHub Actions artifacts expire and do not satisfy durable delivery.
Gate: **P3_ACCEPTED** only after measured QA + authorized human approval + stable storage verification; otherwise **RELEASE_HOLD**.

## Execute
1. Survey sources and chosen reference; pin Git SHA, input hashes, acceptance criteria. If uncertain, HOLD.
2. Evaluate design: plan the scene and route to Phase 1, not automatically to Phase 2/3.
3. Validate manifests, canvas 16:9, original wording, licensed assets and no-SVG policy before work starts.
4. Execute phase-appropriate, narrowly scoped specialist tasks using immutable per-run/per-attempt layer output paths.
5. Render with the Go + Tailwind + Chromium candidate workflow; capture HTML/CSS/PDF/manifests in GitHub Actions artifacts.
6. Inspect the **actual rendered pages**. CI PASS does not mean visual fidelity PASS.
7. Record independent validation, repair only failed layers where safe, and normalize evidence/release disposition.

## Repo references
- Current execution candidate: `experiments/boss-go-tailwind-001/` and `.github/workflows/draftdeck-go-tailwind-trial.yml`.
- Candidate layer architecture: `experiments/boss-agent-swarm-001/SUPERVISOR.md`, `AGENTS.md` and `docs/LAYERED-SWARM-SPEC-001.md`. Legacy contracts mentioning SVG are **superseded** by this skill and must be rebuilt before use.
- Verification and phase gates: `references/verified-pipeline.md`.
- Legacy Python/Canva entry points are retired from the active workflow. Git history preserves prior experiments; don't silently invoke them.

**Output contract:** Every report identifies the current phase, verified steps, missing layer(s), QA limits, branch/SHA, and exact HOLD or release status. Never call a bare wireframe a high-fidelity design.
