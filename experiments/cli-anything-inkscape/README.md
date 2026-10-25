# BOSS CAD-06C · CLI-Anything pilot (isolated)
Status: CANDIDATE. Production integration and release HOLD.

## Test split
1. **Private local source test** runs the actual approved SVG via native Inkscape 1.4, checks 1920×1080 output, six immutable viewports, vector/text preservation, and whitelisted metadata-only copy edit. These private bytes never enter GitHub.
2. **Public synthetic upstream E2E** installs an immutable CLI-Anything Inkscape harness at commit `34f519533bc175d2fe287ab8316b0dd99bb9cc43` and actual Inkscape, creates and edits a synthetic harness JSON document, exports real outputs, verifies PDF/PNG/SVG, and attempts the unsupported direct SVG open as a required negative control.

## Known source-level limitations
The upstream Inkscape harness maintains its own `.inkscape-cli.json` model; its `document open` expects JSON, not native SVG. `export png` renders with Pillow rather than actual Inkscape; PDF invokes the native Inkscape binary. Consequently the current harness is **NOT** qualified for lossless editing of approved BOSS SVG grids and is **NOT** approved as the sole renderer.

## Security boundaries
No actual private BOSS SVG, art, manuscript, real networked agency, secrets, or production writes in GitHub. GitHub CI PASS proves only isolated test outcomes. The OpenBot mandatory runtime gateway is still not qualified for unrestricted CLI execution. Do not let an agent install arbitrary hub packages, execute shell commands, overwrite approved assets, mint human approval, or release.
