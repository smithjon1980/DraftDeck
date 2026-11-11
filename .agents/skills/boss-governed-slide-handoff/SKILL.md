---
name: boss-governed-slide-handoff
description: Route private Day Zero/episode slide candidates through source admission, OpenDots preparation, mandatory OpenBot/BOSS policy evaluation, independent visual checks, and explicit human selection/release. Use for any request to push a section or deck through the agent pipeline.
---

# BOSS Governed Slide Handoff — isolated candidate

## Authority
Read `AGENTS.md`, `skills/draftdeck/SKILL.md`, `.agents/skills/boss-editorial-layout-director/SKILL.md`, `.agents/skills/boss-art-story-reviewer/SKILL.md`, and the latest verified gateway CI result. This skill augments those creative/review instructions; it does not certify, deploy, or modify OpenBot/OpenDots.

## SEVEN execution
**Survey:** Resolve requested slide range from a verified source asset. Extract privately, enumerate slide IDs, and hash the original file and every selected slide's structured source. Never infer manuscript status from slide headings. Source of truth stays in a private owner-controlled location, not a public PR.

**Evaluate:** Record whether current source is unpublished, exact-copy approved, art approved, and permitted for external service ingestion. Default private. No unpublished bytes, image embeds, filenames containing personal secrets, or tokens in public GitHub actions artifacts.

**Validate:** Produce a manifest using `schemas/boss-slide-handoff.schema.json` and run `python3 tools/boss-slide-handoff/validate.py MANIFEST.json`. The manifest must identify a bounded section, recorded source hash, source location class, private evidence pointer, OpenDots preparation, OpenBot policy mode, audit requirement, and independent human review/release gates. A pass only means structural readiness.

**Execute:** OpenDots may prepare candidates only in an isolated authorized workspace. All browser/file/shell/MCP actions must pass a **non-bypassable** OpenBot/BOSS enforcement boundary. If this boundary is not proven with actual transport and network controls, set `dispatch_state=HOLD`; do not upload or dispatch the real slide payload. Policy dry-run, absent policy, audit outage, or ambiguous actor → deny. No synthetic approval key may stand in for a human decision.

**Normalize:** Compare source hashes, native selectable text, art/source provenance, 1920×1080 CSS geometry, actual browser render, PDF parity, and target edit/save/reopen independently. Never equate static tests to visual acceptance.

## Ownership and release
OpenDots = bounded organizer/preparator; OpenBot = mandatory authorization execution gate; DraftDeck = source/renderer; human owner = candidate selection and release authority. Keep operational actions distinct: prepared → technically validated → visually reviewed → human selected → human authorized for destination → released with receipt. Merely saying "proceed" with testing does not approve publication. For all gaps report FAIL/HOLD/NOT_TESTED, link evidence and preserve existing stack.

## Current known stop
Merged PR #96 isolated bridge tests passed but showed direct-route bypass; PR #99 gateway-hardening trial recorded 11/12 tests passing, with an audit-error surfacing assertion failing and negative control still reproducing bypass. **Runtime dispatch of unpublished Studio 01 remains HOLD** until independently verified closure.
