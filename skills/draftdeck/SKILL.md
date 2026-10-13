---
name: draftdeck
description: Canonical phase-gated instructional visual artifact builder: Go supervisor/assembly, Tailwind CSS, Chromium PDF; Story PNG/WebP, Art HTML/CSS, Text semantic HTML; no SVG or React, no Canva pipeline.
---

# DraftDeck — Canonical Production Process

**Candidate, not released.** Phase 1 low-fidelity structure execution has passed prior GitHub Actions trials. Phase 2 requires an actual raster Story asset and an Art component. Phase 3 is independent high-fidelity QA plus explicit human release authority.

## One process — no historical fallback
Only the code in `skills/draftdeck/engine/` and workflow `.github/workflows/draftdeck-canonical.yml` is the *active DraftDeck execution candidate*. Superseded experiments are not fallback implementations. No SVG source, output, conversion, icons or intermediate files; no React, Canvas flattening, Canva or PowerPoint.

## Lifecycle
**Phase 1 / WIREFRAME:** supervisor checks scene contract; Text layer establishes live headings, copy, page geometry and a structural PDF. Story and Art may be missing. Structural pass does NOT constitute visual approval.

**Phase 2 / LAYERED COMPOSITION:** supervisor receives one genuine PNG/WebP Story asset, HTML/CSS Art components and semantic Text content; treats worker outputs as separately scoped, immutable, provenance-bearing inputs. No autonomous image model or task-dispatch service is presently wired into the engine. Missing required layers or invalid assets → HOLD. Render via Go html/template + Tailwind + Chromium.

**Phase 3 / HIGH FIDELITY:** independent reference comparison, overflow and clipping tests, exact source text, contrast and visual inspection, hashes, licensing, storage read-back, and explicit human release. Never self-certify. Production RELEASE_HOLD until proof exists.

## Execution
GitHub Actions is the candidate execution environment. `engine/main.go` reads a structured JSON scene, performs layer separation and exclusions, assembles deterministic HTML, invokes Chromium to write PDF, and creates a hash evidence manifest. Run `go test ./...` and compile Tailwind CSS first; use `scenes/phase1.json` for the verified wireframe milestone.

## Inspector handoff
Read `GEMINI_INSPECTION.md`, audit **all** canonical files, inspect the actual PDF artifact, and report supported PASS/FAIL/NOT_ESTABLISHED. Do not interpret a successful workflow as visual fidelity or operational autonomous agents. Do not publish or overwrite on inspection.
