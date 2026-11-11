---
name: boss-105-gate-coordinator
description: Coordinate BOSS 105-control source-bound human authority, independent narrative/ART/STORY gates, synthetic validation, and fail-closed releases. Skill invocation is not permission.
---

# BOSS 105 Gate Coordinator — candidate v1.0

**Status:** REVIEW_CANDIDATE. Instructions are not authenticated approval, runtime security controls, external custody, or deployment permission.

## Read before acting
1. AGENTS.md, skills/draftdeck/SKILL.md, design-system/boss-design-contract.json.
2. doctrine/boss-105-control-register.md and doctrine/boss-105-authority-medium-custody.md.
3. doctrine/visual-evidence-gate.md, doctrine/production-contract.md and doctrine/release-qa.md.
4. Exact current source-admission record from restricted custody, never a remembered SHA or conversation alone.
5. .agents/skills/boss-story-architect/SKILL.md, then boss-visual-storyboard, boss-art-asset-producer, boss-art-story-reviewer, boss-precomposition-human-approval and boss-editorial-layout-director. Resolve each existing SKILL.md under .agents/skills.
6. Optional Figma bridge is for design review only; it is not release authority.

## Layered process
- Narrative brief/Bridge 1 precedes artwork; writing a brief does NOT authorize dependent STORY-layer image generation.
- Visual storyboard/Bridge 2 and scoped image-medium decision precede ART generation.
- ART is independent, with source and preview SHA-256, original provenance, crop/scale and actual preview. No composited CAD rails, CMYK registration marks, text, logos or story labels embedded.
- Human must expressly approve ART candidate with APPROVE ART <candidate_id>; a restricted independently authenticated ledger must bind source digest, artifact+preview hashes, target ID, profile, composition ID, actor and non-replayable event.
- Only then generate dependent STORY, as a different standalone causal visual with legible meaning absent labels. For EP00/P001A show human purpose and requirements leading toward a proposed campus, with no completed project or authorization claim. STORY cannot be reused ART or a collage of slide composition.
- Human must separately APPROVE STORY <candidate_id> with matching identity and independently authenticated ledger evidence.
- For Episode Zero interior targets, both opener and closer must first be separately accepted with distinct human evidence.
- Composition requires both exact approvals, qualified narration, scoped segmentation, and same-target hashes. Seven layouts exclusively from experiments/episode-zero-seven-phase1/scripts/layouts.mjs. React/Tailwind plus native HTML editorial text are authoritative.
- Verify browser screenshot, copy reconstruction, PDF text selection and visual parity, accessibility, adapter edit-save-reopen; final publication is always a separate human release decision.

## Source integrity and custody
- P001 through P025 are unique and exactly ordered. Keep Git commit, Git blob, raw SHA-256, canonical SHA-256, paragraph-level SHA-256 and remote readback as *distinct fields*.
- Canonical contract BOSS-PARAGRAPHS/1.0 is UTF-8 of each UNCHANGED paragraph, joined by two LF bytes. Do not trim or change whitespace; incompatible canonical versions are not comparable.
- Rejected: missing P025, altered approved text, duplicate IDs, unadmitted source, path traversal, collisions, missing readback or historic version substitutions. Local snapshot claims do not imply remote custody.
- Historical v0.11 sources and component drafts stay intact; the earlier v0.12 P001–P005 remains unrecovered, not silently reconstructed.
- Unpublished manuscript bytes, private previews, authentic ledger records and approval secrets never belong in the public repo.

## Episode-specific medium
- The ten owner-supplied Episode Zero photorealistic references establish visual *direction*, not acceptance of any generated ART. Record a scoped medium decision with owner review evidence.
- Episode 01 Slide 02 keeps its distinct white-ground technical editorial illustration-only contract. Do not silently apply its no-photo restriction to EP00, or authorize photography globally.
- Historical P001A-ART-CANDIDATE-001 remains an unapproved mixed ART+CAD candidate; do not replace or relabel its identity.
- A finished reference compilation is not a license to merge CAD, ART, STORY and native TEXT.

## SEVEN operating sequence
Survey: inspect source, approval, existing skills, actual workflow status and references; preserve unknowns.
Evaluate: scope the lesson, episode, visual medium, teaching story and required comparisons.
Validate: use node --test tools/boss105/test.mjs, the read-only validator and independent medium/source evidence. Tests are synthetic only, not authentic human approval.
Execute: generate one isolated candidate at the currently authorized gate; do not invoke consequential effects on a "proceed" response.
Normalize: record all separate evidence dimensions, reviewer decisions, immutable identities, rejection corrections, defects and review references.

## Security boundaries
- No public manuscript, unpublished visual, actor identity credential, signing secret or private reference in the repository.
- No deployment, paid resource, external protected write, auto archival or publication without separate action-specific authorization.
- Existing OpenBot transport HOLD (unbypassable route, authenticated actor/dot, exact approval replay resistance, durable pre-effect custody, tenant separation, malicious browser/egress) is unaffected.
- Source admission, editorial approval, narrative qualification, ART, STORY, opener, closer, composition, adapter testing and release are independent decisions.
- Synthetic CI runs without secrets under contents: read; its success cannot authenticate a real person.

## Minimum output
Record source identity/status, target+profile, medium evidence, candidate ID, source/art/story/preview hashes, separate structural/editorial/narrative/visual/security/adapter/custody/human states, test run IDs, reviewer and unresolved HOLD items. States are PASS, FAIL, HOLD or NOT_TESTED, never a merged score. The validator cannot inspect visual pixels or verify external custody/ledger; real runs remain HOLD pending that evidence.

**A 105-item control register is not proof of 105 implemented runtime controls.**

