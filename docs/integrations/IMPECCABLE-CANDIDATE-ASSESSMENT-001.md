# Impeccable → DraftDeck: Candidate Integration Decision
Status: EVALUATED / DESIGN_CANDIDATE / NOT_INSTALLED / NOT_TESTED
Upstream: https://github.com/pbakaus/impeccable (Paul Bakaus), verified from upstream README 2026-10-12.
User-provided evidence: timecoded video transcript [00:00:00–00:11:07], secondary source, not runtime testing.
Upstream claimed capabilities: 24 commands, 61 deterministic detectors, product/design context files, local visual iteration, LLM critique complement, Apache-2.0. These counts are upstream claims and may change.

## Governing decision
Do not replace DraftDeck or its React/HTML-CSS/source-first workflow. Use Impeccable as **optional non-authoritative inspection tooling**. Source-authoritative files in doctrine/, design-system/, supplied reference and visual authority specifications outrank Impeccable defaults and generated PRODUCT.md/DESIGN.md. New files are derived candidate indexes, not independently authenticated governing sources.

## Existing conflicts
- DraftDeck's core Composition Standard explicitly uses Arial body, Georgia display, Courier New metadata; Impeccable discourages Arial. Exempt on approved declared profile.
- DraftDeck core requires #FFFFFF ground, #1A1A1A near-black, #DEDEDE technical drafting gray, #B34700 restricted accent; Impeccable advocates tinted neutrals and discourages pure black/gray. Approved colors override upstream house-style checks.
- Reference composition and live-text editability are release-critical; passing 61 detector checks cannot establish either reference fidelity or Canva/Adobe adapter editability.
- No aviation themes, no generic nested-card redesign; preserve shipping-and-receiving visual ontology.

## Additive tool evaluation
1. **PRODUCT.md as compiled context:** extract audience, purpose, use case, brand constraints, rights/proof requirements from authenticated project sources, with source links, unknown markers, and human approval; do not overwrite a canonical BOSS source.
2. **DESIGN.md as compiled visual context:** extract exact tokens, font exceptions, declared visual profile, source reference precedence and approved component geometry. Explicitly preserve user-supplied BOSS logo colors and chosen layout specs for the particular project.
3. **Offline deterministic detection:** run isolated local CLI scan on known DraftDeck HTML output; capture version, rule IDs, false positives, raw JSON and page/asset refs. Configure documented ignores with justification only for doctrinal conflicts.
4. **Advisory critique:** optional model-generated comments and browser visual variants follow deterministic baseline; human adjudicates design direction.
5. **QA integration:** map accepted findings to existing release-qa and reference-render verification, with source edits and rebuild. Never edit generated outputs as the durable fix.

## Security / provenance gate
Do NOT execute `npx impeccable install`, its hooks, postinstall hooks, launcher downloads, or live-edit validation command against trusted worktrees merely because the transcript says it is easy. Inspect pin/release, package, executable provenance, license/NOTICE, dependencies, network behavior and project hooks. Trial in a disposable branch/container and only with explicit operator authorization. Upstream warns that live-mode commands may run repository scripts with user permissions. No current tool installation or proof of quality improvements.

## Proposed controls
DESIGN-IMP-001: known valid DraftDeck profile reports no unapproved required-font/color rewrites.
DESIGN-IMP-002: altered nested-card/low-contrast fixture is detected if a corresponding rule exists; confirm exact rule from pinned engine (not assumed).
DESIGN-IMP-003: passing detector checks with flattened/uneditable text still fails DraftDeck release QA.
DESIGN-IMP-004: visual changes to generated HTML without canonical source update fail the rebuild/reproducibility check.
DESIGN-IMP-005: no code hooks or network downloads without a recorded human permission, separate from text inspection.
All NOT_TESTED.

## Fit to three quadrants
A: Human design authority; agent prepares reports; DraftDeck skill applies; Impeccable CLI is TOOL, not authority.
B: SCRIPT/PROGRAM deterministic check first, general AI critique only for qualitative defects. Avoid token use on deterministic failures.
C: SOP build→lint→render→visual compare→adapter editability→human review; KPI defect escape count/time and false-positive rate with measured baselines; OKR optional; CAPA source correction and rerun.

Disposition: ADAPT CANDIDATE; NO INSTALL; NO PRODUCTION RELEASE.
