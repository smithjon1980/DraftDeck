# Layer Specialist Contracts — candidate v0.1

**Story Agent:** Given a story brief, permitted references, safe-zone geometry and exclusions, create narrative image asset (PNG/WebP), versioned prompt, provenance and hash. No meaningful text, numbers, diagram labels or changing lesson doctrine.

**Art Agent:** Given anchor IDs, relationship graph, system tokens and constraints, produce editable diagram components as art.json (SVG optional), with positions, shapes, arrows and IDs. Do not rasterize or invent authoritative words. Text Agent supplies visible labels.

**Text Agent:** Given pinned authenticated source sections and fixed text-region IDs, produce text.json with verbatim authorized copy, semantic hierarchy and typography intentions. Never invent facts, modify art or render copy into pixels.

**Assembly Worker:** Deterministic software, not an autonomous editor. Validate declared layer outputs and hashes; place Story below Art below editable Text in React/HTML/CSS. Generate browser preview and Chromium PDF; record PDF hash and build provenance.

**Independent QA Worker:** Compare all source text to emitted PDF, validate geometry/clipping, page dimensions, image rights, layer collisions, contrast, and preview versus approved reference. Return PASS / FAIL / NOT_ESTABLISHED with evidence. QA may reject but never approve release.

## Isolation and retry
Worker outputs go to runs/<run_id>/layers/<layer>/<attempt>/. Submitted outputs are immutable. Retrying creates another attempt, capped at two. Supervisor may not blend incomplete results, edit verified inputs invisibly, or return a production link without authorized release and verified persistent storage.