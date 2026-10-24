---
name: boss-react-art-story-submission
description: Enforce separate human selections of BOSS art and story React/Tailwind candidates before full slide composition; preserve rejection/resubmission identity, editable narration and distinct release gates.
---

# BOSS React Art & Story — pre-composition human control

Read `AGENTS.md`, `doctrine/boss-precomposition-human-selection.md`, `.agents/skills/boss-art-asset-producer/SKILL.md`, `.agents/skills/boss-art-story-reviewer/SKILL.md`, `.agents/skills/boss-story-architect/SKILL.md` and exact CURRENT narration source/status. Older script approvals or historical art renders never inherit authority for current slide text.

## Human selection is BEFORE the compositor
The process is **brief → isolated ART candidates → owner selects art → isolated STORY candidates → owner selects story → technical/evidence and native text → React composition → owner inspects composite → separate release authorization**.

Neither standalone art nor standalone story review should arrive already embedded in a finished slide. The renderer may draw and screenshot individual candidate layers in a browser before selection. It **must not compile the final combined slide, PDF or episode batch** until the human has separately selected **both** layers. Human review is an authorization boundary, not an aesthetic decoration or another DOM component. `HUMAN REVIEW REQUIRED` printed on an already composed slide is not approval.

The current 05/60 Digital Property / Submission 03 is **REJECTED_FOR_COMPOSITION** as a visual teaching candidate. Do not reuse its generic shop boxes as approved art or story.

## Required source and preview
- One separate inspectable `ArtLayer.tsx` and one separate `StoryLayer.tsx` with actual React/Tailwind classes. Their independently rendered browser previews must be separate files and distinct visual selections, not one compiled slide crop.
- Art must communicate the actual shop operation without any labels. Story must communicate a bounded problem, transition, evidence, and distinction between proposal/inspection/success. No generic equipment arranged as decoration or repetitive four-step label list counted as story.
- Technical/evidence annotations, editable manuscript text, approved/selected wordmark asset and reflection prompts are separate sources attached **after** independent art and story selection.
- Protect narration bytes, source assets, and review screenshots in owner-approved private custody; public GitHub may contain only generic schemas, skills and synthetic tests.

## Review records and source binding
Each of the two decisions has its own `slide_id`, `candidate_id`, source SHA-256, preview SHA-256, reviewer account, external authenticated review reference, and exact explicit outcome (`APPROVE_ART` / `APPROVE_STORY` or REJECT). A rejection creates a new candidate ID and `supersedes` link on resubmission. Original rejected proof remains in the review record.

`node tools/visual-gate/check_precomposition.mjs ROOT MANIFEST.json REVIEWS.json` checks file presence, hashes, distinct React layers, and the declared receipts; **it cannot authenticate that review was done by a human and it NEVER authorizes a composite**. It returns `compiled_slide_permitted:false` even for structural PASS. Do not use a self-authored JSON decision, PR label, model output or CI pass as a human signature. Enforce the real approval with an owner-controlled authenticated review/CI environment outside the source tree. If not configured, production must HOLD.

## No Python art/story compositor
Prohibited as authoritative visual layers: Python Pillow, matplotlib, reportlab, Python-generated SVG, procedural PPTX shapes, flattened screenshot/full-slide PNG, clipped existing art, SVG text, canvas-rendered narration or placeholder geometry standing in for illustration. Python may inspect, hash or test; React/Tailwind source must draw the art and story (or contain an individually approved, provenance-qualified illustration asset).

After both selections, compile using React components and separately preserved native HTML `TextLayer`. Verify actual 1920×1080 Chromium render, screenshot and art source parity, technical source claims, logo asset provenance, exact copy hashes, PDF fidelity, editing and readability. All composite and release decisions remain **separate human gates**; no model self-approval.

If art or story is weak, absent, unreviewed, rewritten, or visually rejected: **HOLD, REBUILD, and RESUBMIT only the rejected layer for human selection; do not hide it behind typography or compile a substitute.**
