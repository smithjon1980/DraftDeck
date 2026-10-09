# DraftDeck process-learning record — 9 October 2026
Author and final authority: Jonathan Smith
Record prepared by: ChatGPT/Codex assistant
Status: archived exchange and evidence; corrective workflow proposed; implementation not declared approved.

## Why this record exists
Jonathan's instruction, preserved verbatim:
> Thank you for that correction, but there is a method to my madness. When I speak on what I think happened, you correct me, and these corrections need to be archived for the record, because when we get the process right, we will have a history of what went wrong. The more frustrated I am, the more teachable it's going to be in the future. I'm going through all of the headache so the future learner doesn't have to.

The exchange is process-development material. Preserve the operator's experience, the hypothesis, the inspection, the correction, and the remaining failure together.
Frustration is part of the reported user experience; it does not establish a technical cause. A corrected hypothesis does not invalidate the observed poor result.
The educational aim is to reduce repeatable learner friction through documented checks and reusable guidance. That aim is author-stated; learner benefit has not yet been evaluated.

## Incident DD-20261009-01: “It has been wrapped in SVG again”
Trigger: Jonathan supplied candidate slide images and questioned whether the slide had again been wrapped in SVG despite the React/Tailwind requirement.
Observed experience: the output resembled the previously rejected drafting/table treatment.
Initial technical hypothesis: the entire slide was implemented as SVG.
Inspection: repository source in PR #38 at commit `e71a2ed846039abb574d37fc81ef50906b7e1ea0`.

### Evidence
- `examples/boss-episode-01/src/components.jsx`: SlideCanvas returns a native HTML section; metadata uses a header and paragraphs; the logo is a separate img; sequence nodes use ol/li/h2.
- `examples/boss-episode-01/src/main.jsx`: title, comparison copy and footers use native headings and paragraphs.
- `examples/boss-episode-01/src/styles.css`: imports Tailwind and implements most composition measurements through named CSS selectors.
- `examples/boss-episode-01/package.json`: includes React, React DOM, Vite, Tailwind and the Tailwind Vite plugin.

Source links:
- https://github.com/smithjon1980/DraftDeck/blob/e71a2ed846039abb574d37fc81ef50906b7e1ea0/examples/boss-episode-01/src/components.jsx
- https://github.com/smithjon1980/DraftDeck/blob/e71a2ed846039abb574d37fc81ef50906b7e1ea0/examples/boss-episode-01/src/main.jsx
- https://github.com/smithjon1980/DraftDeck/blob/e71a2ed846039abb574d37fc81ef50906b7e1ea0/examples/boss-episode-01/src/styles.css

### Correction and scope
The inspected slide implementation is native React/HTML/CSS, not a full-slide SVG.
Screenshots alone cannot establish the underlying rendering technology.
This inspection did not execute a new browser session, inspect the current Canva DOM, or establish destination editability.
Using React/Tailwind does not establish visual quality; mostly handwritten CSS is not itself an implementation failure.
Do not generalize this finding to every older artifact or other AI platform.

### Remaining design findings
Based on the supplied candidate images, the assistant identified:
- Slide 01: large logo treatment and headline wrapping that strands “Skill.” on a separate line.
- Slide 02: large header bands, repetitive horizontal rules, and hierarchy that reads as a basic ruled document.
- Partitioning is present; the intended premium Tesla Model Y touchscreen composition was not convincingly demonstrated.

These are visual-review judgments, not measured usability results or a proven software root cause.
Jonathan's response remained a rejection of the result; correcting the SVG hypothesis did not approve the design.

### Assistant accountability
The assistant acknowledged that its earlier handoff supplied content and constraints without sufficiently concrete composition direction.
That is a contributing-process interpretation, not a controlled causal finding.
The assistant must retain its own incomplete handoff and premature confidence as part of the history.

### Proposed repair
Preserve exact candidate copy, native text, and the original logo. Rework typography, spacing, logo scale, header density and panel hierarchy.
Show one revised Slide 02 browser composition first. Verify technology and visual design as separate checks.
Status: proposed; no repaired render or author approval is established by this record.

## Related process corrections already encountered
| Issue | Earlier assumption or failure | Correction/evidence | Remaining limit |
| --- | --- | --- | --- |
| Asset transfer | Local ZIP download link was presented as usable but failed for Jonathan | Original ZIP was committed to main at 5bf0beb; Git blob matched local bytes | Other-session checkout must still obtain the file |
| Content identity | Episode 01 orientation candidate could be confused with the Pitch milestone | Orientation ZIP contains Sequence/Precedence/Grouping; current Pitch candidate set is 01/02/06 | Approved rendered master remains unresolved |
| Logo recovery | Canonical logo was treated as unavailable in the initial handoff | Supplied cyan/magenta/black image recovered, visually inspected, committed unchanged at 3588407 | Equivalence to Gemini's differently named 40871_78a41e.jpg remains UNKNOWN |
| Specification status | Complete Visual Authority Spec was initially not recovered | Gemini text and candidate copy committed at b96b358 with provenance and reported approval labels | Original approval receipt and governing renders were not supplied |
| Canva route | Public HTTPS was presented as universally required | Current connected schema also accepts a local design_file; diagnostic import success was reported in the earlier session | Tool availability differs by session; geometry and destination editability need actual inspection |
| Quality claims | Passing geometry checks could be treated as design fidelity | Source compliance, visual review, destination inspection and human approval are distinct | Current visual implementation remains unapproved |

Supporting records:
- `episode01/reference/ASSET_HANDOFF.md`
- `episode01/reference/GEMINI_RECONCILIATION.md`
- `episode01/reference/Visual_Authority_Spec_v1.0.md`
- `episode01/reference/slide-copy.candidate.json`

## Reusable learner procedure — proposed
1. Record what appeared wrong in the operator's own words.
2. Separate that observation from the suspected technical cause.
3. Inspect the evidence needed to test the cause: source for implementation, browser for layout, destination for editability.
4. State the correction narrowly, with artifact revision and limits.
5. Preserve any unresolved design or usability failure after correcting the hypothesis.
6. Convert the finding into a prevention check and a bounded repair.
7. Record repair execution, new evidence and human review separately when they occur.

Suggested fields for future incidents:
incident ID; date; author statement; trigger; observed result; hypothesis; artifact revision; inspection method; finding; correction; remaining problem; assistant contribution; proposed prevention; repair status; approval scope.

## Archive boundary
This record preserves the supplied exchange and the source inspection already performed. It does not create an approval, merge PR #38, amend the visual spec, or claim the process is now validated.
Future incidents should be appended as dated entries rather than erasing earlier mistakes.
