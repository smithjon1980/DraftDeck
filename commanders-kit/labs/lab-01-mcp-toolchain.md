# Lab 01 — Build and Verify an MCP Toolchain

**Candidate replacement for previous Day Zero tool-handoff assignments. Not released until live proof is recorded.**

## Goal
Students demonstrate that an authorized AI client discovers **Windmill MCP tools**, requests each of the seven allowed DraftDeck operations, and obtains verifiable output artifacts. Distinguish MCP transport/discovery, Windmill orchestration, tool execution and human governance.

## Acceptance evidence per tool
Capture: UTC timestamp; Windmill workspace and deployment environment (no secrets); Git SHA and pinned binary/library/model version; MCP discovery tool name and parameter schema; request ID; scoped input artifact hash; operation request; Windmill run ID and trace; actual tool version/probe; output artifact hash; independent output validation; fail/blocked cases and reason.

## Seven live positive tests
1. **OpenCV:** inspect a synthetic geometry fixture; return measurable dimensions.
2. **ImageMagick:** transform a controlled raster fixture; validate output metadata.
3. **resvg:** render known SVG artwork; validate output image.
4. **Tesseract:** audit text in an example *flattened* image; record OCR uncertainties; never treat OCR as editable source text.
5. **Potrace:** trace a monochrome bitmap to vector; verify vector can render.
6. **VTracer:** trace a color raster to SVG; verify SVG can render.
7. **SAM 2:** segment a sample object with the required model weights; verify mask dimensions and provenance. Separate large model setup from lighter utilities.

## Negative tests
- Missing background/art/typography layer → denied before any tool runs.
- Unknown operation or tool name → denied.
- Tool not installed or model weights missing → BLOCKED, not success.
- Untrusted path, malformed file, oversized asset or unauthorized destination → denied.
- Flattened output cannot be called 'Canva editable'.

## Promotion rules
A PLAN_ONLY reply, 200 HTTP status, or workflow success with no output proof is NOT a live tool pass. Log each tool's state: REGISTERED, INSTALLED, EXPOSED_IN_MCP, INVOKED, ARTIFACT_VERIFIED. Only verified tools may be described as live. Require 7/7 separately verified, plus one end-to-end chained flow, before replacing previous assignments. Keep the BOSS release separate from test-only deployment.

## Prerequisites
Windmill workspace and reachable MCP endpoint, authentication configured outside Git; workers with isolated runtime and correct dependencies, model weights for SAM 2, bounded input/output storage, appropriate user approvals, and observability retained. Use pinned versions and review licenses. Do not place tokens in repo or examples.
