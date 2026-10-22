---
name: boss-story-architect
description: Rebuild the teaching story from admitted BOSS source evidence before generating artwork or arranging slide copy. Use when a slide lacks visual meaning, requires a scenario, or the NotebookLM-to-story bridge is incomplete.
---

# BOSS Story Architect — source to teachable relationship

## Authority
Read `AGENTS.md`, `skills/draftdeck/SKILL.md`, `skills/draftdeck/references/editorial-composition.md`, `design-system/boss-design-contract.json`. The current contract overrides historical Episode 01 reference skill updates. This skill creates **candidate briefs**, never authorizes release.

## Survey
Admit a source record: stable source ID, page/timestamp or lesson reference, evidence state, exact-copy boundary, requested lesson outcome and unresolved claims. NotebookLM and video summaries are sparks, not independent evidence. Preserve approved script text verbatim; distinguish recorded copy from working copy.

## Bridge 1: teaching story
Specify the claim and contrast the learner must understand, the actors and concrete business objects, a beginning/change/outcome sequence, the action that proves the claim, what would make the claim false, and the learner's observable takeaway. For the current reference, use **Main Street Copy**, a hypothetical neighborhood copy/print/pack/ship operator. The Art & Technical Plan is user accepted; V4 narration can be revised but exact new wording must be reviewed and pinned before voicing. Read `doctrine/main-street-copy-case-model.md`. No grocery POS example or invented shipment/revenue figures.

**Example for Episode 01 Slide 02 (CANDIDATE, not approved):** **Current Slide 02 is an architectural rendering versus a real operating facility,** not an earlier networking pitch. Show a proposed Main Street Copy shop site and its future digital operating facility (domain/address, compute/facility, software/equipment) while clearly labeling that construction and execution remain NOT ESTABLISHED. Align the image to V4 P001–P004 and its exact new hash, never to a historical pitch slide. For the later case, show job ticket, copy/print, inspect, pack, and an eligible UPS Ground OR FedEx Ground handoff as distinct hypothetical processes.

## Deliverable
Return a compact `story_brief` with:
- `source_id`, `source_state`, `copy_provenance`, `exact_headline`
- `teaching_assertion`, `story_mechanism`, `learner_observation`
- `scene_actions`, `required_visible_relationships`, `facts_vs_proposals`
- `reflection_question` and its review state
- `UNKNOWN` fields explicitly; never turn them into invented approval

## Story rejection
Reject generic boxes, icons or decorative arrangements as substitutes for the actual operational relationship. Reject artwork briefs that a learner cannot interpret without reading every word. Never claim a concept brief is approved source or final artwork.

Handoff to `boss-visual-storyboard`; do not skip directly from source paragraphs to CSS layout.
