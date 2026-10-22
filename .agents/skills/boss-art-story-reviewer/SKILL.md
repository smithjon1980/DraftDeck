---
name: boss-art-story-reviewer
description: Review source-story-art completeness for BOSS editorial slides before browser-to-PDF parity testing or visual approval. Use to detect logo-only screens, placeholder reflection copy, untraceable art, invented causal stories, and artwork lost between stages.
---

# BOSS Art & Story Reviewer — two independent gates

Read `AGENTS.md`, `doctrine/visual-evidence-gate.md`, and `skills/draftdeck/references/visual-acceptance.md`.

## First gate: structural handoff
Run `python tools/visual-poc/check_story_layers.py RENDERED_SLIDE.html STORY_MANIFEST.json` on **the actual rendered single-slide HTML**, not source JSX or all slides combined. Require a real story illustration distinct from the canonical logo, matching hashes for the logo and story asset, complete Bridge 1/2 declarations, an actual learner reflection question, and live editorial text. No story asset or unknown reflection question is a HOLD. Store missing evidence rather than fabricating it.

## Second gate: semantic and visual review
Visually inspect the real slide and original source/reference side by side: Can the learner identify the required relationship from the drawing? Are the business objects, actions, constraints and consequences present? Did source-to-story transformation invent factual evidence? Did an asset get cropped or rasterized incorrectly? Are the drawing, logo, editable text and CAD framing distinguishable? Capture a specific difference record and per-gate PASS/FAIL/NOT_TESTED.

Only after both gates should the existing browser-to-PDF fidelity, target editability and explicit human release checks proceed. Structural success is not visual approval, human signoff or publication authorization.

## Intermediate gate: measured artwork quality
After structural completeness, inspect actual browser image metrics and run `python tools/visual-poc/check_story_art_resolution.py BROWSER_IMAGE_METRICS.json`. Generate that JSON from live DOM image element dimensions and computed `object-fit`; do not supply claimed sizes from a design prompt. One rendered story-art element must have at least one source pixel per displayed CSS pixel along the effective crop/stretch axis. Report below-threshold input as **HOLD: ART RESOLUTION**. This does not prove sharpness, genuine high-frequency detail or source quality.

## Test 06 warning
A small crop from a visually persuasive generated full slide can pass logo/artifact hash and reflection structure yet fail the story mechanism and effective resolution. The illustrator must deliver separate scene artwork showing the required operational causal event. Structural READY is not a human visual acceptance result, including when all editorial copy is native and the PDF looks similar.
