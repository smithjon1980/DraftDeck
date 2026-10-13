---
name: draftdeck
description: Governed Dual-Spark instructional visual artifact workflow: human-approved NotebookLM-to-composite ideation, supervising-agent Scene Manifest planning, Go/Tailwind/Chromium deterministic assembly, independently verified visual fidelity and human release. Story PNG/WebP, Art HTML/CSS, Text semantic HTML; no SVG, React or Canva execution route.
---

# DraftDeck — Canonical Dual-Spark Production Process

**Status: CANDIDATE / PRODUCTION RELEASE HOLD.** This skill describes the intended pipeline; documentation does not prove a working agent runtime, schema validation, reference admission, visual fidelity or human release. The currently verified low-fidelity wireframe milestone is historical technical evidence, not visual acceptance.

## One production route; no historical fallback
The active executable candidate is `skills/draftdeck/engine/` with `.github/workflows/draftdeck-canonical.yml`. Superseded experiments are not fallback implementations. Production constraints: **no SVG in source, output, conversion, icons or intermediates; no React, Canvas-flattened teaching text, Canva or PowerPoint.** Use Go `html/template`, Tailwind CSS, and Chromium PDF export. Story uses raster PNG/WebP, Art uses permitted semantic HTML/CSS, and Text uses native semantic HTML.

## Dual-Spark distinction: designing is not manufacturing
- **Spark 01 / Reference A:** the genuine NotebookLM instructional image, grounded in authoritative course material (**Reference C**).
- **Spark 02 / Reference B:** a **fully composed visual reimagination** produced in the learner's chosen image-capable AI tool from A and the creative prompt. Creative generation can include provisional typography and illustrative elements; do not impose HTML layer-manufacturing constraints on this image.
- **Reference D:** a written creative handoff explaining teaching objective, story/metaphor, visual hierarchy and relationships, source-preserving choices, creative deltas and unknowns.
- **Human selection:** the operator examines and explicitly accepts or rejects B and D. Silence is not approval.
- **Production:** the supervising agent receives **A, approved B, authenticated C and approved D** and compiles a scene plan/manifest; the separate workers manufacture the scoped components. B is the approved *visual target*, **not** an acceptable flattened final slide. C remains the *authority for exact instructional copy*; any words in B are provisional unless independently supported by C.

The learner acts as creative director during reimagination and as systems architect during governed manufacturing. This is a teaching model and not proof that automated workers are wired into the repository.

## Phase 0 — Ideation and source admission (outside the engine)
**Input:** authentic A and C, with byte-level SHA-256 and provenance records. A NotebookLM image or screenshot must be the genuine source, not a previously generated low-fidelity DraftDeck PDF, extrapolated description or unrelated reference. Record filename, byte hash, publisher/author or Notebook provenance, source-text/version, rights, date and permitted use.

**Action:** run [the learner's creative prompt](dual-spark-handoff/PROMPTS.md) through a selected image-capable tool; retain original A, generated B, source C, and brief D as four distinct files. Document changes and unsupported copy. Obtain human acceptance of **B and D**.

**Gate:** authenticated A/C, recorded B/D and affirmative human creative approval before manufacturing planning. If A or C is missing or unverified, keep **SOURCE_ADMISSION_HOLD**; preparing templates and candidate architecture is allowed, but do not claim that Spark 01 executed.

## Phase 1 — Supervising-agent scene planning (no artistic invention)
**Input:** the four admitted references and the operator's constraints.

**Action:** inspect A and B visually; ground teaching meaning and exact required text against C; use D to map interpretation decisions. The supervisor outputs a machine-readable scene manifest plus a claim/evidence ledger and worker contracts. Do not delegate freeform restyling. Record common coordinate system (candidate manifest currently 1600×900 px, top-left origin), bounded element boxes, IDs, permitted design tokens, semantic relationships, z-index, exact source-copy mapping, asset references with hashes and reference versions.

**Schema gate:** the desired contract is `scene-schema-v1.json`; **that file was not present in `scene-manifest-001/` at the 2026-10-13 audit**. The extant `scene-manifest-001/validator.go` checks a bounded subset (1600×900 containment, known art tokens/components, ID/link uniqueness, reserved layer z-index bands, and byte-level hashes for the reference and source files when supplied). Its tests are not proof of complete JSON Schema conformance, image-text separation, semantic validity, actual visual fidelity or production readiness. Do not describe the manifest as fully validated against an unavailable specification.

**Gate:** a real versioned schema and validator implementation must agree and pass negative as well as positive tests; authenticated file hashes must resolve against real bytes; worker scopes and exact source copy must be accepted; otherwise **MANIFEST_HOLD**. Existing `scene-manifest-001/day-zero-manifest-001.json` is **CANDIDATE_NOT_AUTHENTICATED**: approximated coordinates and null reference/source hashes are not admitted ground truth.

## Phase 2 — Worker manufacturing and deterministic assembly
The supervisor provides each specialist only the necessary bounded contract and does not itself paint or render.

- **STORY worker:** creates/identifies separated PNG/WebP illustration assets, free from baked instructional text in production. Log file path, bytes, hashes and provenance. Verify actual raster type, not filename only.
- **ART worker:** produces allowed HTML/CSS geometry, connectors, annotations and design components consistent with B, constrained by permitted tokens and approved component registry. No SVG.
- **TEXT worker:** produces native, selectable semantic HTML containing exact source-grounded copy from C, with IDs, hierarchy, provenance and declared geometry. No unsupported rewritten image text.

The Go engine validates inputs to the extent implemented, assembles HTML through templates and Tailwind, and uses Chromium to render a PDF with a content/hash evidence record. The existence of role definitions does **not** establish an operational multi-agent dispatcher. Invalid or missing assets, copy or provenance → **ASSEMBLY_HOLD**.

## Phase 3 — Independent verification and human release
Independent reviewer compares the actual rendered output with **B for approved narrative, geometry, hierarchy and appearance**, **C for exact facts/copy**, and **A for retained teaching objective and source-boundary fidelity**. Inspect actual page(s), readability, text selection, clipping/overflow, contrasts, image separation, source SHA-256, asset rights, output hash and evidence storage/read-back. Record numerical tolerances **only when defined in the approved verification contract**; do not fabricate pixel-match scores or claim pixel-identical style.

Record each gate as PASS / FAIL / NOT_ESTABLISHED and link to actual evidence. Build success, JSON parsing, Go unit tests, a valid PDF signature or a pleasant reference image **never** independently establish fidelity. Gemini may critique and improve the candidate process but is not a replacement for human release. **RELEASE_HOLD** persists until explicit human authorization.

## Historical milestone mapping
The previously named **Phase 1 / WIREFRAME** is retained as an earlier demonstrated infrastructure milestone. It is **not** the newly defined Phase 1 **Scene Planning**, and must not be promoted to the visual master. Existing low-fidelity Phase 2 fixtures also do not establish autonomous worker execution or reference correspondence.

## Current execution and inspection
For active code, use `engine/main.go`, templates, `engine/scenes/`, and the workflow `.github/workflows/draftdeck-canonical.yml`. Run `go test ./...`, inspect actual source, engine and PDF bytes, and test with authentically admitted inputs. For candidate scene extraction, read `scene-manifest-001/README.md` and `validator.go`; do not assume the manifest and engine share the same fully implemented schema.

See [Dual-Spark handoff](dual-spark-handoff/README.md) for the exact artifact packet and [copyable prompts](dual-spark-handoff/PROMPTS.md) for the learner and supervisor. Give Gemini `GEMINI_INSPECTION.md` and independent evidence. Do not publish, merge, deploy or overwrite on inspection alone.

## Mandatory four-option Spark 02 gate — audit amendment 2026-10-13

The image-capable model must return **four distinct, independently addressable candidate images**, A/B/C/D, based on the **same authenticated NotebookLM page A** and its specific teaching objective. A collage/contact sheet of four thumbnail designs is not four output assets. A visually plausible image of the wrong source, or an infographic about DraftDeck itself, is **REJECTED_WRONG_SUBJECT** and must not be counted as a creative candidate.

Each candidate must have its own recorded bytes, SHA-256 and concise visual rationale. Archive the exact operator-visible creative prompt and generator/tool identity, generated candidates, all failures, prompt iteration and reference-page identity. Do not claim access to a hidden provider prompt or random seed where not supplied.

**Human creative approval requires an explicit selection and rationale**: identify the chosen candidate; why its hero, hierarchy, visual relationships and narrative teach the specific lesson better than the other three; approved differences from A; requested corrections; decision timestamp. Preserve the rejected alternatives for research. A passing generator call is not a human decision.

The supervising planner must emit the **tripartite packet**: `scene-manifest.json`, `narrative-brief.md` and `worker-criteria.md`, plus a provenance/evidence ledger. Negative worker constraints must be verified in code; prompts alone cannot enforce them. SHA-256 establishes byte identity, not source truth, human approval or visual equivalence. A PDF with selectable text is not automatically a native editable slide or certified PDF-editor editability; check the required destination behavior separately.

**Manual simulation is next:** one authorized reference slide → four separate image candidates → human selection with rationale → manual tripartite packet → validator → one real Go assembly render → independent QA → release authorization. On failed reference matching, stop at CREATIVE_GENERATION_HOLD. Never silently substitute a different NotebookLM source.
