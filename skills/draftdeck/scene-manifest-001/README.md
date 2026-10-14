# Scene Manifest 001 — Candidate inventory and validator

Scope: **manual reference extraction + static validation only**. No Chromium job is triggered by these files.

The `day-zero-manifest-001.json` inventory represents the currently known semantic elements of the high-fidelity reference, including diagram labels, arrows, delivery state, HOLD branch, rails and four panels. All pixel coordinates are **candidate approximations**, not measured from an authenticated original. Existing reference_sha256 supplied in discussion is not admitted until checked against exact bytes. No raster Story asset is claimed to exist.

Go validators: `ValidateBounds`, `ValidateTokens`, `ValidateLinks`, `ValidateLayers`, `ValidateProvenance`. Tests cover rejection of bad bounds, IDs, links, tokens, layer ordering and missing provenance. Validation deliberately returns HOLD without genuine reference/source file hashes.

This does not implement compositor or multi-agent runtime. No SVG. No production authorization.
