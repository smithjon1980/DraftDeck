---
name: book-to-skills
description: Extract candidate reusable atomic skills and composite workflows from user-supplied books, PDFs, transcripts, and text; emit source manifests, SKILL.md, COMBO.md and references.md without elevating source authority.
version: 0.2.0-candidate
status: SPECIFIED_CANDIDATE
authority_scope: EXTRACTION_AND_DESIGN_ONLY
---

# Book-to-Skills — DraftDeck Intake Option 2

**Activation:** "Activate DraftDeck Intake Protocol. Await source document upload." Activation configures this conversation's workflow; it does not start an autonomous daemon or authorize repository modification. If supplied material is insufficient or unreadable, record HOLD/NOT_ESTABLISHED rather than inventing content.

## Intent and scope
Optional extraction workflow alongside `skills/draftdeck/` (slide production). A book-derived instruction is not a verified capability or authoritative policy. BOSS governance and DraftDeck production doctrine control wherever conflicts arise.

## Intake stages
1. **Intake and L0 identification:** allocate `SOURCE_ID`; capture supplied filename/title, contributor, provenance, observation time, media type, rights/reuse limitations, page/line/timestamp references and SHA-256 only when bytes are actually available. Record `ADMISSION_STATUS=PENDING_AUTHENTICATION` until authorized review.
2. **Source-content congruence gate:** sample front matter, early, middle and late sections; inspect actual rendered pages when parsing is suspicious; compare claimed title, author, subject, chapter structure and dominant content. Look for storefront wrappers, unrelated page fragments, inconsistent subject matter, broken or repeated text and accidental interleaving. SHA-256 identifies the bytes, **not** the work's authenticity. Assign `CONTENT_CONGRUENCE=PASS | HOLD | FAIL`, independent of `ADMISSION_STATUS`. On FAIL, quarantine and record exact page-level evidence; extract zero skills. On HOLD, request a valid source or more visual inspection; do not guess.
3. **Atomic extraction:** isolate single-responsibility, testable operating rules. For each skill specify Goal, Proof, Steps, Boundary, explicit input/output, operational phase, enforcement gate/seam, source references and unverifiable assumptions. Do not conflate author opinion with observed evidence.
4. **Composite design:** only where a process truly spans multiple skills, author `COMBO.md` with dependency ordering, handoff contracts, failure/rollback choices, and who has approval authority. A combo cannot authorize its constituent steps.
5. **Reference isolation:** produce `references.md` holding short context citations, source locations, conflicts, exclusions and permissions separate from executable instructions.
6. **Inspect and package:** ensure every proposed rule maps to grounded source passages or is clearly tagged `DESIGN_INFERENCE`; validate local links, naming, duplicate identifiers, and restrictions. Fail closed on unknown source scope.
7. **Human review:** return candidate package for review. No repo pushes, qualification claims or production use without separate direction.

## Required output
```text
sources/<source-id>/source-manifest.md
skills/<slug>/SKILL.md
skills/<slug>/references.md
workflows/<slug>/COMBO.md   # only if warranted
```
For copy/paste workflows return raw fenced Markdown for each file with its exact repository path. For requested repository commits stage the additions on a review branch; do not silently update `main`.

## Skill file contract
- Goal — one narrow responsibility.
- Proof — observable test conditions including a falsification test.
- Steps — finite, repeatable sequence.
- Boundary — exclusions, risk triggers, escalation/HOLD.
- Metadata — `source_ids`, `operational_phase_tags`, `enforcement_tags`, `trust_class`, `qualification_status`, `test_status`, `authority_scope`, `evidence_refs`.

## Protection
No full-book extraction beyond legitimate access or quotation rights; prefer original procedural abstraction and short supporting quotations. Source ID is not authenticated L0. A source hash proves bytes, not source credibility. Do not claim to have run a test or deposited evidence unless the run/evidence is verified. Preserve LOCATION → ACCOUNTING → ADJUDICATION → AUTHORITY, PRIME handoff and release QA. Keep instructional generation distinct from executable DraftDeck slide production.

## Intake safety prerequisite
No author/title match can be inferred solely from file name, cover art, metadata or a storefront overlay. Source authenticity is distinct from content congruence and rights permission. A clean source can remain PENDING_AUTHENTICATION. If the content is clearly an unrelated collage, `SOURCE_INTEGRITY_HOLD / NO_EXTRACTION` is the only permitted outcome; log SHA-256, inspected page IDs, contamination classes, and next eligible recovery. Never include the rejected text as L0 verified method content.

**Falsification:** A PDF whose sampled chapters are unrelated to its claimed work still causes an executable SKILL.md to be generated or changes the active Skills Library → intake gate FAIL.
