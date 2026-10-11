# BOSS-D0-NLM-005 — NotebookLM Theory Source Handoff

STATUS: PREPARED — SOURCE INGESTION NOT EXECUTED; GENERATION HOLD
SOURCE_CLASS: A-TIER CANDIDATE THEORY ONLY
RESEARCH_BOUNDARY: No simulated learner event constitutes empirical evidence.

## Goal
Prepare one fresh NotebookLM notebook for the seven Day Zero v2.0 Theory Masters, without historical source contamination. Existing theory scripts are preserved without additions. This handoff does not authorize audio generation or publication.

## Required operator gates
1. Retrieve this branch and record its **actual immutable commit SHA**. Do not treat a moving feature branch as an immutable source snapshot.
2. Run `python3 curriculum/day-zero/verify_a_tier.py` against that same checkout. Proceed only on seven PASS results and no mismatches.
3. Review the seven A-tier texts and the candidate `source-whitelist.candidate.json` for subject-matter authority. Their current embedded label is "Candidate training material; not a controlled release." Hash verification cannot change that label. Obtain explicit source-admission approval.
4. Create a **new** notebook (or identify a known empty notebook) for this approved source set. Before writing, record notebook identity and present source inventory. If it contains obsolete source material, use a fresh notebook rather than assuming unchecked sources cannot influence generation.
5. Import **only** the seven files on the whitelist, in EP01–EP07 order, using the actual pinned GitHub content or individually verified exported Markdown files. Do not import this handoff, the manifest, B-tier lab, C-tier simulation, S01–S04 provisional reconstruction, or archived podcast.
6. Inspect NotebookLM's actual inventory for precisely the seven expected titles and content. Compare beginning, middle and ending anchors in **each** source; confirm no extras and no unapproved substitutions. Keep separate receipts for `UPLOADED`, `READABLE`, `CONTENT_INSPECTED`, `ADMITTED`.
7. Keep all media generation on HOLD until explicitly authorized. NotebookLM does not expose a documented SHA-256 integrity claim solely by displaying a source title; do not report destination byte-level parity without an actual byte export/hash.

## Exact seven theory sources
| EP | Display title | Repository path |
|---|---|---|
| 01 | You Already Move Information | `curriculum/day-zero/episodes/EP01/EP01_A_Theory_Master.md` |
| 02 | BOSS and the Two Governed Boundaries | `curriculum/day-zero/episodes/EP02/EP02_A_Theory_Master.md` |
| 03 | From Request to Accountable Package | `curriculum/day-zero/episodes/EP03/EP03_A_Theory_Master.md` |
| 04 | Admission Before Capability | `curriculum/day-zero/episodes/EP04/EP04_A_Theory_Master.md` |
| 05 | PRIME, Candidate Output and Release | `curriculum/day-zero/episodes/EP05/EP05_A_Theory_Master.md` |
| 06 | From One Package to Network Accountability | `curriculum/day-zero/episodes/EP06/EP06_A_Theory_Master.md` |
| 07 | Ready for Module 01 | `curriculum/day-zero/episodes/EP07/EP07_A_Theory_Master.md` |

## Prompt for a human operating Gemini/NotebookLM
Use only the seven separately supplied, hash-verified A-tier Markdown source files in the attached whitelist. Read and report their exact titles, EP identifiers, opening and closing content, and whether any source is missing or unreadable. Before importing, report the target notebook identity and current source inventory. Do not silently create duplicate notebooks, overwrite existing sources, or substitute older drafts. If you have actual access to the NotebookLM import interface, import only the approved whitelist and return a destination inventory; otherwise explicitly report that the files are **prepared but not imported**. Do not generate audio, slides, or infographics. Do not treat simulated narratives or predicted learner outcomes as observations.

## Receipt schema
- ORDER: BOSS-D0-NLM-005
- SOURCE_BRANCH_AND_COMMIT: [verified full SHA]
- SOURCE_MANIFEST_CHECK: PASS / FAIL / NOT_EXECUTED
- AUTHORIZED_SOURCE_SET: seven A-tier entries
- NOTEBOOK_ID: [actual or UNKNOWN]
- PRE_IMPORT_SOURCE_COUNT: [actual or UNKNOWN]
- IMPORT_ATTEMPTED: YES / NO
- IMPORTED_SOURCE_TITLES: [observed values]
- CONTENT_CHECKED_SOURCES: [observed count 0–7]
- EXTRA_SOURCES: [observed names or UNKNOWN]
- DESTINATION_VERIFICATION: PASS / PARTIAL / FAILED / NOT_ESTABLISHED
- MEDIA_GENERATION: HOLD
- EXCEPTIONS: [explicit]
- NEXT_AUTHORIZATION: [human decision]

## Separate continuation
B-tier practical labs and C-tier clearly tagged hypothetical scenarios can be admitted to their own lab/production notebook only after distinct review and scope authorization. Never mix them with the seven-source Theory-only notebook.
