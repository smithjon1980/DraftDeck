---
name: boss-react-art-story-submission
description: Submit, reject, correct and resubmit BOSS slide art/story candidates drawn with React TSX and Tailwind CSS. Required for section slide production and visual acceptance.
---
# React/Tailwind art and story — Submit / Resubmit contract

Read `skills/draftdeck/SKILL.md`, `.agents/skills/boss-art-asset-producer/SKILL.md`, `.agents/skills/boss-art-story-reviewer/SKILL.md`, and the authoritative manuscript.

## Mandatory provenance
An accepted candidate MUST include inspectable `.tsx` React source for **both** `ArtLayer` and `StoryLayer`, Tailwind utility class usage, and an independently editable `TextLayer` for spoken text, action title, labels and reflection. React renders the layered slide into HTML; Tailwind CSS styles the geometry. CAD/ISO primitives may be SVG paths/shapes inside React but spoken text is native HTML and MUST NOT be SVG text.

Not allowed as authoritative art/story layer: Python Pillow, matplotlib, reportlab, Python-generated SVG, procedural PPTX shapes, flattened screenshot/full-slide PNG, screenshot crop masquerading as illustration, or placeholder boxes/icons pretending to be narrative art. Python is permitted **only** for inspections, hashing, structural CI checks or measuring render parity; it MUST NOT draw or compile art/story.

A genuine external illustration asset may appear INSIDE a React ArtLayer with independently recorded provenance, licensing, dimensions and approval; this exception cannot be used to flatten the entire slide or bypass visual review.

## Submission record
Store a public-safe manifest compliant with `schemas/boss-react-layer-submission.schema.json`; private narration, unpublished image bytes, and private source references remain in owner-controlled storage. Candidate states: `SUBMITTED`, `REJECTED`, `RESUBMITTED`, `TECHNICALLY_ACCEPTED`, `HUMAN_ACCEPTED`. New resubmissions have a new candidate ID, reference the rejected predecessor, and supply a change description. Never silently overwrite a rejected candidate.

## Mechanical gate
`python3 tools/react-layer-gate/check_submission.py MANIFEST.json ROOT` audits TSX source and declared layers. Structural PASS means source present and guardrails satisfied, not aesthetic success. Fail on missing JSX layers, absent Tailwind utility classes, detectable forbidden Python generation or flattened-slide markers, or stale resubmission identity.

## Visual and human gate
After structural PASS: build React, capture actual 1920×1080 browser render, inspect CAD geometry, story meaning without labels, illustration detail, wordmark provenance, copy hashes/native selectability, PDF parity, and target edit/save/reopen. Reviewer may `REJECT` with issue IDs and actionable corrections; artist creates a distinct candidate and `RESUBMITS`. Only a human may record `HUMAN_ACCEPTED` or release. Do not automatically cycle approval. Existing OpenDots/OpenBot gateway remains HOLD until proven non-bypassable.
