# Visual acceptance — inspect the artifact, not the success message

**Status:** candidate guidance governed by `doctrine/visual-evidence-gate.md`.

## Per-candidate evidence
Record source and copy manifests, reference status, image and logo identities/hashes, source commit, capture dimensions, browser build/versions, actual browser PNG, approved-reference comparison (or explicit HOLD), annotated differences, native editorial text/art layers, CAD grid/title-block inspection, readability, accessibility, adapter outcome and human decision.

## Browser → export parity
1. Render the candidate in its intended browser at fixed slide dimensions or an explicitly selected web/print profile.
2. Capture reference browser PNG after fonts and images load; log device scale and viewport.
3. Export the **same source** to PDF using the intended page size and print CSS.
4. Rasterize PDF at matched comparison dimensions and align/crop only documented page margins.
5. Generate side-by-side and difference/overlay image; report rendering and content differences separately.
6. Inspect typography, logo, key artwork, captions, callouts, grid/title plate and footer by eye. Numeric pixel differences alone are insufficient.
7. When image seems pixelated, distinguish low-resolution embedded bitmap, interpolation/scaling, and intrinsically simplified/missing source art. Re-encoding a weak diagram to PNG cannot reconstruct the original composition.

## Gates and authorization
Use `python tools/visual-poc/check_evidence_manifest.py <manifest> --evidence-root <private-dir>` for structural bundle checks. Exit 0 means metadata eligible for next gate only; 2 means valid HOLD; 1 means invalid. Existing `check_contract.py` and `check_brand_proof.py` remain separate checks. Never place private evidence into public workflow logs. PASS / FAIL / NOT_TESTED are not interchangeable. A human reviewer must see the actual image and explicitly approve exact candidate, scope and next action.

## Failure-driven normalization
For each regression add a short failure specimen, suspected cause, test demonstrating the correction, boundary not tested, and a reusable negative fixture where safe. Retain reference hash and capture environment for comparisons. If the correct reference is unavailable, choose **HOLD** rather than comparing against an invented approximation.
