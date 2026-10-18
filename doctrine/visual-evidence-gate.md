# BOSS Visual Evidence Gate — v0.1 candidate

**Status:** PROPOSED; no visual master is approved by this document. Applies to new DraftDeck teaching-slide candidates and, once an output profile is ratified, to landscape, portrait, and square infographic candidates. Does not retroactively certify historical examples.

## Non-negotiable source sequence

1. Preserve the authoritative lesson/source content, approved identity, source art, and provenance.
2. Record the **two bridges**: source → reimagined teaching story → Bioscillate art/story design. A generic technical layout is not a replacement for approved storytelling.
3. Obtain concept selection **before** implementation. Where there is no approved reference, label all candidate renders **CONCEPT — REFERENCE NOT APPROVED** and prohibit release approval.
4. Rebuild with distinct artwork, CAD framing, story/callouts and native HTML editorial text. **Do not use SVG-based slide construction or SVG text as a shortcut for the art-first concept.** An independently sourced vector artwork asset is not itself permission to redraw the slide as a schematic.
5. Render the actual implementation in a browser at its specified output dimensions, then capture a full-resolution PNG; do not substitute a code preview, PDF text extraction, or image-generator mockup.

## Mandatory per-candidate visual-evidence bundle

- `candidate_id`, source commit/build ID, profile and exact render dimensions, original artwork and logo identities/hashes, source-copy manifest and reference provenance.
- Approved reference image or explicit `REFERENCE_UNAPPROVED` state, plus an actual browser screenshot captured at the same geometry.
- **Side-by-side reference/render comparison**, optionally an overlay or perceptual diff; annotate changes to composition, story artwork, callouts, typography, grid, title block, branding, notes/reflection and reading hierarchy. Pixel similarity alone cannot prove storytelling fidelity.
- Independent evidence that editorial copy is real, selectable HTML text and artwork/callouts are separate objects. For target editors, record a separate imported-file layer inspection and edit-save-reopen test.
- PASS / FAIL / NOT_TESTED for source-copy fidelity, story/art match, logo, CAD, legibility/contrast, clipping/collisions, browser behavior, adapter fidelity and target editability. Record screenshot paths, run ID, tool versions and known limitations.
- Reviewer decision: `PENDING`, `REJECTED`, or `APPROVED_FOR_NEXT_GATE`; include reviewer identity, date/time, exact candidate hash and scope. No silence-as-consent, inferred approval, or automated release.

## CAD drawing-profile inspection

For CAD-framed DraftDeck candidates, visually verify an unobtrusive **visible drafting grid**, measured inner border and zone markers, anchored technical callouts and a **title plate/title block** that includes sheet ID, sheet title, revision, product identity, date and status. Use `NTS` (not to scale) for conceptual artwork rather than inventing engineering dimensions. A white canvas with hairline rules *without* the grid and title plate is **FAIL: CAD COMPOSITION**. Keep grid contrast subtle enough not to obscure the focal art or live copy. Describe the style as **ANSI/ISO-informed**, never standards-certified without a separate conformance assessment.

## Release state machine and failures

`SOURCE_VERIFIED → CONCEPT_SELECTED → BUILT → STRUCTURAL_TESTED → VISUAL_EVIDENCE_CAPTURED → HUMAN_VISUAL_REVIEWED → ADAPTER_TESTED → HUMAN_RELEASE_AUTHORIZED`.

Each arrow requires evidence for its own gate. A FAIL or missing mandatory artifact means `HOLD` and rerender. A passing visual review never implies Canva editability; an adapter import never implies release authorization. `APPROVED_FOR_NEXT_GATE` is not authorization to publish.

## Automated enforcement scope

A machine-readable bundle manifest and negative fixtures should be validated in CI before candidate review. This validates **presence, structure and referential consistency**, never the visual quality of the rendered pixels. A separate human review must inspect the images. No existing build is deemed compliant merely because these rules are written.

## Tool screening rule

YouTube demos and open-source repos are **candidates, not evidence**. Require verified project URL, license, maintenance, security posture, cost/runtime requirements, and a local benchmark against this gate. Prioritize tools that improve source capture, browser screenshot/diff, CAD geometry, editing, infographic profiles or repeatability. Avoid duplicative or unmaintained plugins.