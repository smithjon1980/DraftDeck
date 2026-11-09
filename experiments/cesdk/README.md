# CE.SDK one-slide qualification — isolated experiment

Status: TEST DESIGN / NOT EXECUTED
Scope: BOSS visual editing and PDF vector fidelity; no production pipeline changes.

## Baseline
- Existing React/Tailwind, Windmill, n8n, Railway, GitHub Actions, and Inkscape workflows remain unchanged.
- No manuscript, protected source, or approved design is modified.
- Test with one representative 1920×1080 slide using four independent layers: CAD, Art, Story, Text.
- Use synthetic text and artwork until an approved source asset is selected.
- Do not use the previous pixelated PDF as proof of the root cause; compare source vector and rendered output.

## Experiment sequence
1. Confirm CE.SDK web editor can initialize with the installed package and license mode.
2. Import or reconstruct a four-layer synthetic scene with a hairline CAD grid, vector story artwork, art imagery, and native editable text.
3. Save the editable CE.SDK scene, reopen, and change text without changing protected geometry.
4. Export PDF and SVG; compare at 100%, 200%, 400%, and print resolution. Check whether vector artwork survives, whether text is selectable in PDF, and whether text becomes paths in SVG.
5. Evaluate PDF/X-4 CMYK using an authorized trial license and appropriate ICC profile, if available.
6. Test protection: attempt to edit locked CAD/Art/Story elements through editor UI and API. UI locks are not authorization enforcement; protected changes must also be rejected by a separate trusted validator.
7. Capture export logs, screenshots, input hashes, artifact hashes, SDK version, environment, and human visual review.
8. Record PASS / FAIL / BLOCKED per criterion; keep production integration on HOLD until human review.

## Hard gates
- No unexpected rasterization of SVG story or CAD layers.
- Native editable text in the working CE.SDK scene.
- PDF readability and vector fidelity not worse than the approved baseline.
- Print profile and PDF/X validation evidenced rather than assumed.
- Protected source files unchanged; no direct publish or protected write path.
- License and commercial feasibility assessed before adoption.

## Current evidence
Documentation review only. No CE.SDK runtime execution, visual output, export, license validation, or human approval has yet been performed.

## Documentation
- https://img.ly/docs/cesdk/react/get-started/react/quickstart-r1q2w3/
- https://img.ly/docs/cesdk/js/what-is-cesdk-2e7acd/
- https://img.ly/whats-new/
