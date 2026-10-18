# DraftDeck

DraftDeck prepares layered, editable instructional presentations and visual evidence from approved source material. Current BOSS work uses the original Bioscillate Operating System by Seven identity, information-dense Tesla-screen-inspired hierarchy, CAD/ISO-informed geometry, and human approval boundaries.

**Current candidate contract:** design-system/boss-design-contract.json (not released or human-approved). Read AGENTS.md and design-system/README.md before generating a new Episode 01 or Day Zero design.

## Current operating boundaries
- Source and explicit approved design rules govern output; a rendered image or PDF is not automatically editable.
- Default slide canvas: 1920 x 1080 with native HTML editorial text and separately sourced artwork. Mobile web content must reflow rather than shrink a fixed slide.
- NotebookLM-to-story and story-to-design bridges precede source-grounded production.
- Automated tests may qualify structural correctness; actual render inspection, destination-specific tests, and human release authorization remain separate.
- Original cyan/magenta/black branding must not be overwritten by historical demonstration palettes.

## Repository orientation
- design-system/: current visual contract, tokens, components, and validation.
- doctrine/: mixed history and ongoing production/evidence principles. Read doctrine/README.md for current versus historical scope.
- renderer/: renderer roadmap and compatibility notes.
- skills/draftdeck/: build instructions and reference-implementation tooling.
- examples/: historical and experimental demonstrations, not automatically current brand authority.
- .github/workflows/: independently scoped validation and generation workflows.

Existing historical example decks, old ontology documents, and experimental feature branches are intentionally retained in Git. Their presence is not a claim that their design decisions are approved for the current BOSS release. The active design contract is a review candidate pending an authoritative logo asset and human-approved reference render.
