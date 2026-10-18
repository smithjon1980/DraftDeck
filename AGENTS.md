# BOSS / DraftDeck operating instructions — v0.1 review candidate

Scope: current BOSS Episode 01, Day Zero slides and corresponding instructional interface output. This file identifies project constraints; it does not override human approval. The active candidate source is design-system/boss-design-contract.json and the design-system/ directory. Historical demonstration files retain historical scope.

## Identity and visuals
- Brand: Bioscillate Operating System by Seven. Original canonical logo artwork only. The logo source SHA is not yet established; never invent or substitute it.
- White (#FFFFFF) canvas, black editorial text, canonical cyan (#00BCEB) and magenta (#E30074) brand colors. No borrowed orange core accent or substituted logo profile for current work.
- Slide canvas: exactly 1920 x 1080 logical pixels, CSS-scaled to viewer size. Do not use h-screen/vh as structural slide geometry.
- Interface influence: Tesla Model Y center touchscreen information architecture + CAD/ISO-informed drafting precision; no generic SaaS cards, gradients, decorative rounded corners, or heavy shadows.
- Text remains native HTML, not SVG text, canvas text, or baked into a rasterized full slide. Artwork and text remain separate layers.
- Website and lesson interface must reflow; print requires separate dimensions. Do not conflate slides with a responsive web page.
- Legacy transport and aviation metaphors are retired for contemporary instructional releases, though historical artifacts may remain archived.

## Editorial two-bridge process
1. Inspect the actual source/reference visually. Log file, page, teaching point, story art, exact copy, source status, and unresolved fields. NotebookLM output is a spark, not a new authority.
2. Bridge 1: reimagine the source into a grounded teaching story. Separate preserved evidence and exact copy from candidate creative departures.
3. Bridge 2: translate the story into the approved BOSS interface hierarchy and original brand. Do not turn a missing logo or source into invented artwork.
4. Plan layers from artwork foundation through story, structural geometry, source brand elements, live primary text, supporting annotations, and reflection/notes footer.
5. Provide the bridges, source manifest, copy manifest, candidate status, acceptance criteria, and provenance to the implementer.
6. Implement the candidate as React/Tailwind where specified; emit discrete static HTML/CSS with editable native text. Do not make SVG or a flattened image the editorial layer.
7. Visually inspect actual render and source/copy/geometry correspondence; test adapter import separately.

## Candidate comparison and approval
- Produce four distinct A–D arrangements only when requested for an approved comparison stage. Do not change facts, exact copy, brand identity, or evidence status between variants.
- Score actual renders on story fidelity, copy, logo, geometry, editability, accessibility and clarity using PASS / FAIL / NOT TESTED with evidence.
- No eligible candidate = HOLD and repair, not a relative winner.
- Generation success, visual recommendation, human selection, and authorized release are four distinct states. Silence is not authorization.

## Source and build boundaries
- Authoritative copy/geometry lives in versioned source. Rebuild generated output; do not hand-edit derivatives and claim the source was updated.
- CI checks structure and contracts; only actual render inspection validates visual fidelity. Hands-on adapter editing is a separate higher-level test.
- Confirm the current Canva import API/schema for the target. Historical routes are not universal guarantees and do not automatically verify current destination editability.
- Preserve missing evidence explicitly as UNKNOWN or NOT_ESTABLISHED, including actual human approval and unverified import fidelity.
