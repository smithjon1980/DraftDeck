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
