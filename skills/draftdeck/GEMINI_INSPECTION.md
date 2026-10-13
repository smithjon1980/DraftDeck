# Gemini Inspection Brief — DraftDeck Canonical Go Pipeline

## Task
Independently audit the complete **active** implementation. Treat this as a code review, not permission to execute unapproved side effects. Do not consult deprecated experiments as working implementations.

## Read in order
1. `skills/draftdeck/SKILL.md`
2. `skills/draftdeck/engine/main.go`
3. `skills/draftdeck/engine/templates/page.html`
4. `skills/draftdeck/engine/scenes/phase1.json`
5. `skills/draftdeck/engine/input.css`
6. `.github/workflows/draftdeck-canonical.yml`
7. `skills/draftdeck/engine/main_test.go`

## Questions requiring evidence
- Does HTML preserve semantic editable text? Does Story stay PNG/WebP and Art HTML/CSS, with no SVG in execution?
- Is Phase 1 output correctly distinguished from Phase 2 composition and Phase 3 acceptance?
- Are content sources genuinely authenticated, or merely labeled?
- Is Story asset loading vulnerable to path traversal, malicious file contents or excessive size?
- Does the page physically render at one 16:9 sheet? Does the PDF have selectable text?
- Does Tailwind scan template classes correctly? Does CSS resolve when opening `output/day-zero.html` from Chromium?
- Is PDF SHA-256 independently matched on the downloaded artifact, not only CI workspace?
- Is the Go supervisor a *real multi-agent* controller? If not, name all gaps.
- Can the QA gate incorrectly report success from PDF signature only?
- Does any obsolete runner still trigger on commits? Identify residual legacy files, but do not delete unrelated repository history.

## Response format
Architecture matrix; file-by-file finding with path/line references; security and visual fidelity defects; reproducible commands; PASS/FAIL/NOT_ESTABLISHED for each phase; severity-ranked repairs. **No invented test results**. Production HOLD.

## Boundary
This is a code-and-evidence inspection packet. Gemini must not amend, merge, deploy, delete, or assert release without explicit authorization.


## Dual-Spark audit extension — 2026-10-13

Read additionally:
8. `skills/draftdeck/dual-spark-handoff/README.md`
9. `skills/draftdeck/dual-spark-handoff/PROMPTS.md`
10. `skills/draftdeck/scene-manifest-001/README.md`
11. `skills/draftdeck/scene-manifest-001/day-zero-manifest-001.json`
12. `skills/draftdeck/scene-manifest-001/validator.go` and `validator_test.go`
13. The **actual checked-in JSON Schema file**, if any; identify its exact location or explicitly mark `scene-schema-v1.json` **MISSING**.

Audit the Dual-Spark claim chain separately:
- Source A: genuine high-fidelity NotebookLM reference inspected, authentic bytes hashed, correct source identity? Do not substitute a low-fidelity DraftDeck PDF.
- Source C: exact authorized instructional copy and version authenticated from actual bytes? Report copyright/permission constraints where known.
- Composite B and brief D: files and dated explicit human creative approval proven, with separately bound hashes? Do not treat this SKILL.md wording as proof of a generated image or approval.
- Supervisor: does any *executed* planner actually read A–D and produce a manifest, or are there only instructions and fixtures? Claim operational status accordingly.
- Manifest: test schema availability, JSON Schema enforcement, Go validator coverage and the **gap between stated versus implemented checks** (notably file signatures, visual letterlessness, semantic accuracy, CSS component sanitation, exact editorial copy, asset path protections and z-order). Explicitly verify the current candidate's null source/reference hashes and approximate positions.
- Workers: confirm real Story/Art/Text role dispatch, provenance and isolation through runnable evidence. A named worker role is not an operating agent.
- Assembly: obtain real Go/Tailwind/Chromium execution logs and PDF; test selectable text, page count/size, overflows and artifact hash independently.
- Fidelity: inspect and compare the **actual final render** to B for visual design, to C for editorial fidelity, and to A for original teaching objective. Quantify only with grounded criteria; if B is missing, aesthetic fidelity is NOT ESTABLISHED.
- Release: identify human authorizing action; passing CI never releases a candidate. Keep `RELEASE_HOLD` absent authenticated approval.

**Review deliverable:** (a) A–D admission matrix; (b) requirements-to-code/validator traceability table; (c) claim-by-claim PASS / FAIL / NOT_ESTABLISHED with evidence; (d) severity-ranked blockers and single-slide proof plan; (e) corrective patch suggestions as a *proposal*, not unilateral implementation. Distinguish code review from tests actually run.
