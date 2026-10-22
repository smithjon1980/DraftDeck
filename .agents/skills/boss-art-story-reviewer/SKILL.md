---
name: boss-art-story-reviewer
description: Review source-story-art completeness for BOSS editorial slides before browser-to-PDF parity testing or visual approval. Use to detect logo-only screens, placeholder reflection copy, untraceable art, invented causal stories, and artwork lost between stages.
---

# BOSS Art & Story Reviewer — two independent gates

Read \`AGENTS.md\`, \`doctrine/visual-evidence-gate.md\`, and \`skills/draftdeck/references/visual-acceptance.md\`.

## First gate: structural handoff
Run \`python tools/visual-poc/check_story_layers.py RENDERED_SLIDE.html STORY_MANIFEST.json\` on **the actual rendered single-slide HTML**, not source JSX or all slides combined. Require a real story illustration distinct from the canonical logo, matching hashes for the logo and story asset, complete Bridge 1/2 declarations, an actual learner reflection question, and live editorial text. No story asset or unknown reflection question is a HOLD. Store missing evidence rather than fabricating it.

## Second gate: semantic and visual review
Visually inspect the real slide and original source/reference side by side: Can the learner identify the required relationship from the drawing? Are the business objects, actions, constraints and consequences present? Did source-to-story transformation invent factual evidence? Did an asset get cropped or rasterized incorrectly? Are the drawing, logo, editable text and CAD framing distinguishable? Capture a specific difference record and per-gate PASS/FAIL/NOT_TESTED.

Only after both gates should the existing browser-to-PDF fidelity, target editability and explicit human release checks proceed. Structural success is not visual approval, human signoff or publication authorization.
