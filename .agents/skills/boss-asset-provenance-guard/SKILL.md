---
name: boss-asset-provenance-guard
description: Fail-closed content and provenance guard for BOSS image generation, reference reuse, and visual promotion. Run before rendering and again before human review.
---

# BOSS Asset Provenance Guard — candidate v0.1

## Trigger and authority
Mandatory for Episode Zero Storybook art, slide illustrations, image-derived layout variants, and any reference artwork proposed as a visual master. Read AGENTS.md, boss-story-architect, boss-visual-storyboard, doctrine/visual-evidence-gate.md and the locked paragraph manuscript. This skill does not authorize release.

## The failure to prevent
An off-topic generated café scene was praised for composition, then its fictional scene and green palette were promoted into creative authority; an unrelated cat was also carried through. Liking layout never approves narrative objects, colors, characters, wording, or reuse permissions.

## Required manifest, before generating
Each candidate needs machine-readable manifest fields: candidate_id, source_id, source_digest, source_status, reference_assets (each: id, digest, approved_scope from COMPOSITION_ONLY | STYLE_ONLY | CONTENT_APPROVED), required_subjects, forbidden_subjects, allowed_palette, story_brief_id, generation_prompt_digest, output_digest, review_status, and human_approval (nullable with exact digest and scope).
No source or missing manifest -> HOLD. If exact manuscript is unavailable, do not invent its subjects; keep status NOT_TESTED/HOLD.

## Content firewall
- COMPOSITION_ONLY means geometry, placement, visual rhythm, column proportions and whitespace ONLY. Never import a reference's setting, persons, animals, signage, color identity, plot or words.
- STYLE_ONLY may transfer specified techniques but not depicted subjects or brands.
- CONTENT_APPROVED permits only individually enumerated, human-approved objects; cannot override locked manuscript or banned subjects.
- Candidate prompt MUST include approved scenario, required relationships, forbidden extraneous content, canonical Bioscillate palette (white #FFFFFF, cyan #00BCEB, magenta #E30074, black), and a negative list of reference-only subjects.
- Subject detection is a reviewer-assisted semantic check, not a complete deterministic vision guarantee. Every added or ambiguous subject -> HOLD, record visual evidence and seek scoped approval. No silent substitution.
- Test exact paragraph and source before artwork; retain provenance of original prompt, reference images, model/output identifiers, hashes and human decision.

## State machine
SOURCE_PINNED -> REFERENCE_SCOPED -> PROMPT_AUDITED -> GENERATED_CANDIDATE -> SUBJECT_REVIEWED -> DESIGN_REVIEWED -> HUMAN_APPROVED_FOR_NEXT_GATE. Missing evidence, unapproved semantic object, unauthorized palette, or reference scope drift = HOLD. Approval of composition cannot automatically approve scene content; no inherited approval across changed asset digests.
Never self-release or publish. Preserve existing React/Tailwind, Windmill, n8n, Railway and GitHub Actions operations.

## Evidence and handoff
Report: claimed source versus verified evidence; permitted extraction from reference; detected deviations and unknowns; machine-check status; reviewer visual status; candidate digest; next human approval scope. Retain rejected candidates for provenance, but exclude from approved library.
Run `node scripts/check-storybook-asset-manifest.mjs path/to/manifest.json` before design review. Passing this structural check is not proof that image pixels comply.
