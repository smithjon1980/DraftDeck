---
name: boss-art-story-reviewer
description: Reject incorrect image medium and missing story meaning before BOSS slides reach browser/PDF acceptance. Verifies native art/logo/text separation and source-grounded storytelling; never grants human design approval.
---

# BOSS Art & Story Reviewer — style, substance, source and export

Read `AGENTS.md`, `doctrine/visual-evidence-gate.md`, and active BOSS Story Architect, Visual Storyboard and Art Asset Producer instructions.

## Gate 0 — visual medium (human-visible inspection)
For Episode 01 Slide 02, **reject photography, photorealistic people, dark cinematic/neon HUDs, generic stock-photo side-by-side layouts, generic icon dashboards, and charts posing as story scenes**. Accept only for further assessment a white-ground **technical editorial illustration** with actual process/story mechanisms and limited cyan/magenta/black detail. Classifying a PHOTO as EDITORIAL_ILLUSTRATION in a JSON manifest does not make it so. Compare the actual pixels against the approved brief; if no reviewer inspected the medium, record NOT_TESTED.

## Gate 1 — narrative adequacy
At minimum connect the **Main Street Copy** physical/digital facility to a bounded work requirement, actual or explicitly hypothetical output, stage-specific evidence and correct custody semantics. A generated label does not prove UPS Ground or FedEx Ground acceptance; an acceptance scan does not prove recipient delivery, and delivery does not prove profit. The current approved illustration plan does NOT prove that a V4 spoken script has been reviewed verbatim. Do not infer factual metrics. If removing labels destroys every cue of what actually happens, mark FAIL. Compare source teaching assertion to scene, and separate proposed creative devices from approved copy.

## V4 version and case integrity
The user authorized the V4 spoken rewrite on 2026-10-22. Compare each slide to the **V4 manuscript's own exact paragraph IDs and SHA**, not older pitch text, V1 hashes, or V3 candidate transcripts. Check the current Slide 02 **rendering-vs-reality** mapping, not the retired networking pitch. The shop has separate intake, print, inspect, pack, route, custody and delivery stages. `PARCELS` is architecture; `PRIME` is governed work handoff. A source image and a manifest cannot certify visual or commercial truth. Do not publish unapproved narration in GitHub.

## Gate 2 — separate layers/structural checks
On the rendered single-slide HTML run `python tools/visual-poc/check_story_layers.py RENDERED.html STORY_MANIFEST.json`. Require the distinct original-logo and story-illustration bytes for the current bounded gate; check the exact native headline, two bridges, source identity, and native reflection question. Record the separate new BOSS wordmark as an explicitly selected candidate identity asset; do not confuse it with original Bioscillate logo or story art. This script detects presence and hashes, not stylistic quality or source truth.

## Gate 3 — actual output
Render Chromium at 1920×1080 and inspect font/asset loads, protected crop regions, dense illustration detail, native HTML text, correct BOSS wordmark treatment, and CAD/ISO-informed white layout. Rasterize PDF at matched dimensions, compare actual pixels and legibility; do not fix a weak image by PNG re-encoding. Verify target editor edit/save/reopen separately.

## Gate 4 — human decision
Record PASS/FAIL/NOT_TESTED for medium, narrative, copy, logo and wordmark provenance, artwork detail, browser parity, PDF parity, destination layers, and explicit human selection. A numerical pixel diff or a machine-ready report is not artwork approval. No explicit human review → HOLD.
