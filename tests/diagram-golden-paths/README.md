# BOSS diagram engine samples — NOT YET VERIFIED GOLDENS

The two sources and one slide manifest are **synthetic teaching data only** for Main Street Copy, not customer records and not approved narrated copy. Their filenames are not a claim of rendered fidelity.

- `main-street-copy-intake.mmd`: Mermaid simple flow with visible HOLD and correction.
- `main-street-copy-clarification.puml`: PlantUML sequence with fictional customer, counter operator, work order and production.
- `example-slide.json`: schema-valid, deliberately `NOT_TESTED` proposal that refers to a future `diagrams/` runtime path. This directory is the source example library, not the deployed diagram directory.

**Current CI:** schema structure, routing, safe palette, initial QA state and negative fixtures. **Not yet executed in CI:** Mermaid/PlantUML actual parsing, diagrams as pixels, accessibility, editable labels, business semantic completeness, actual React rendering, approvals, or provider inference.

Next promotion requires installed pinned engines, compiled outputs, actual browser screenshots, baseline comparison and reviewed semantic evidence. The file name `golden-paths` is a target classification, not a certified current state.
