# DraftDeck Commander's Kit — Windmill integration (candidate)

This directory registers **seven open-source visual-processing tool options** for the central DraftDeck project. It does **not** vendor third-party code, install binaries, connect Windmill, or claim tested execution.

## Tools

| ID | Purpose | Invocation surface |
| --- | --- | --- |
| vtracer | Raster → color SVG tracing | CLI |
| opencv | Geometry/image analysis | Python |
| sam2 | Semantic/object segmentation | Python model & weights |
| tesseract | OCR for auditing baked-in text | CLI |
| potrace | Black-and-white vector tracing | CLI |
| imagemagick | Raster preparation | CLI |
| resvg | SVG raster/render validation | CLI |

See `tool-registry.json` for upstream references and installation probes. Tool availability is **unverified**, not active. SAM 2 also needs appropriate model weights; installation alone is not a completed integration. Before enabling each adapter, review its license and dependencies and pin versions. No secrets or upstream source trees belong in this registry.

## Windmill contract

`windmill/commanders_kit.py` exposes a Windmill-compatible `main(tool_id, operation, slide_id, source_ref, layer_manifest, execute=False)`. It returns a structured, fail-closed **plan** with explicit eligibility checks. It **does not execute external commands**. This is a discoverable starter interface, not a deployed Windmill flow; connect and authenticate Windmill separately. Tool IDs and operations must be allowlisted before an execution adapter is created.

## Global three-layer rule (Pre-Spark v1.1 candidate)

For **every** BOSS image-related prompt and slide, require separately specified: (1) background/CAD geometry, (2) artwork/story **without baked-in instructional text**, (3) separately editable typography including labels, citations and annotations. Text must be edited in native DraftDeck/Canva elements. OCR does not reconstruct editable text; vector tracing does not reconstruct the original design layers. Missing text manifest or edits that flatten instructional text fail release.

Each slide must provide `slide_id`, `source_ref`, `background_geometry`, `art_story`, and `editable_typography`. Post-Spark must verify source correspondence, legibility, absence of baked-in instructional text, layer independence, and Canva editability by actual inspection rather than by a visual-only screenshot.

## Governance

This branch is a proposal. Existing DraftDeck production files are not changed. Human approval, input provenance, isolated execution, no unrestricted shell, resource limits, and verification logs are required before activating tool calls. Keep the existing BOSS logo palette (cyan/magenta/black) and the approved Tesla touchscreen/CAD-ISO design as project visual rules; third-party tools do not change doctrine.
