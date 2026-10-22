# BOSS / DraftDeck operating instructions — v0.1 review candidate

Scope: current BOSS Episode 01, Day Zero slides and corresponding instructional interface output. This file identifies project constraints; it does not override human approval. The active candidate source is design-system/boss-design-contract.json and the design-system/ directory. Historical demonstration files retain historical scope.

## Episode 01 print-specific candidate (2026-10-18)

For the **proposed** 17 × 11 inch landscape narration-first Episode 01 magazine, review `episode01/EP01_NARRATION_FIRST_PRINT_PARITY_CANDIDATE.md` **in addition to** these operating instructions. It defines a separate print profile and candidate-script-to-approved-exact-copy boundary. It does not revise the 1920 × 1080 slide profile, qualify prior proofs, or authorize release. Do not promote the new manuscript to verified recorded transcript before an audio comparison, or imply that a proposed 48-page issue is finished.

## Identity and visuals
- Brand identity: Bioscillate Operating System by Seven. For the current illustrative concept, the owner selected the NEW cyan/magenta/black **BOSS wordmark**. Preserve that selection as a named candidate visual asset with its own provenance; do not invent a production hash or silently substitute the older wave/diamond logo. Keep older source logos intact as historical assets until separately reviewed.
- White (#FFFFFF) canvas, black editorial text, canonical cyan (#00BCEB) and magenta (#E30074) brand colors. No borrowed orange core accent or substituted logo profile for current work.
- Slide canvas: exactly 1920 x 1080 logical pixels, CSS-scaled to viewer size. Do not use h-screen/vh as structural slide geometry.
- Interface influence: Tesla Model Y center touchscreen information architecture + CAD/ISO-informed drafting precision; no generic SaaS cards, gradients, decorative rounded corners, or heavy shadows.
- Text remains native HTML, not SVG text, canvas text, or baked into a rasterized full slide. Artwork and text remain separate layers.
- Website and lesson interface must reflow; print requires separate dimensions. Do not conflate slides with a responsive web page.
- Current case: **Main Street Copy**, a fictional neighborhood copy/print/pack/ship shop. Copy → Pack → Ship and UPS Ground/FedEx Ground carrier processes are CURRENT instructional metaphors. Historical aviation and older convenience-retail framing are not current creative authority. Read `doctrine/main-street-copy-case-model.md`. Carrier prices, eligible destinations, deadlines and claims of delivery require real verification.

## Current reference business
- Main Street Copy: customer intake and bounded job ticket → copy/print → inspect → pack → carrier choice and explicit human release → ground-network handoff → tracking/delivery evidence. A label is not delivery proof.
- Preserve **PARCELS** as architectural responsibilities (Platform, Attachment, Routing, Carriage, Exchange, Language, Service), **PRIME** as governed work handoff (Package, Route, Inspect, Move, Establish Delivery). They are not the same as the shop's physical stages.

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

## External skill discovery (find-skills)
- Project-scoped discovery skill: `.agents/skills/find-skills/SKILL.md`; its pinned upstream and license are recorded in `.agents/skills/find-skills/BOSS_ADMISSION.md`.
- This skill may identify *candidate* external skills. A recommendation or installer command is **not** source admission, execution authorization, a design-contract amendment, or release approval.
- Inspect candidate repository/ref, license, permissions, dependencies, security posture, and runtime compatibility; isolate testing before adoption. Never auto-install all matches or run remote installation as part of discovery without authorization.
- Existing BOSS instructions and the two-bridge visual evidence gate take precedence over third-party skill advice. No general skill can replace human visual or publication approval.
