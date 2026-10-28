---
name: boss-figma-design-bridge
description: Use optional Figma as a governed design-specification bridge, enforcing exact source/reference/target locks, separate human art and story approval, and React/Tailwind production handoff.
---

# BOSS Figma Design Bridge — v0.3 corrective candidate

Read `AGENTS.md`, `doctrine/figma-design-bridge.md`, `design-system/boss-design-contract.json`, `experiments/episode-zero-seven-phase1/scripts/layouts.mjs`, `.agents/skills/boss-precomposition-human-approval/SKILL.md` and `tools/figma-bridge/check_handoff.mjs`.

1. **SOURCE:** Admit exact private source paragraph IDs/digests, real approved-reference hashes/scopes and the story+medium brief. Never invent missing manuscript, logos or approved illustrations.
2. **ORDER:** For `BOSS.EP00.A01.S01`, qualify opener and closer FIRST. Preapproval Figma `LAYOUT_STUDY` is CAD zoning only. The 7 variant names must originate from `layouts.mjs`, never a newly generated layout or a 17×11 stretch.
3. **ART:** Prepare isolated original artwork with source and preview SHA-256. Operator independently approves ART for the exact source digest, slide, profile and composition ID.
4. **STORY:** Prepare an independent visible causal story and preview; operator separately approves STORY for that *same* source/slide/profile/composition. Neither Figma nor a generated design can mint approvals.
5. **FIGMA:** A composed frame is eligible for candidate review only when both human approvals bind to the exact ART/STORY IDs, source+preview hashes, candidate and target. Bind separately selected design review to the same target; keep editable text and artwork independent.
6. **HANDOFF:** Use `BOSS-FIGMA-BRIDGE-V2` manifest with `target.{kind,section_id,target_id,composition_id,profile,layout_variant,source_digest,paragraph_ids}`. Run `node tools/figma-bridge/check_handoff.mjs <manifest.json>`; V1 manifests cannot be promoted. Interior targets are limited to exactly `BOSS.EP00.A01.S01.P001` through `P025` with matching `paragraph_ids`; `P000/P026/P999` fail. Interior slides require BOTH qualified anchor records with distinct `human_record_ref` values before their gate. These records are structural declarations; authentication is a separate requirement.
7. **WEB:** For `WEB_COMPONENT_SPEC` require distinct contiguous breakpoint bands, with every viewport frame ID declared in `figma.frame_nodes`, and design-spec PASS+evidence refs for reflow, keyboard, focus, accessibility, English/Spanish expansion and interaction states. Actual browser verification after React implementation remains separate.
8. **RELEASE:** React/Tailwind plus native HTML TextLayer remains authoritative. Verify browser render/PDF and target edit-save-reopen against original approved reference, Figma native frame and exact narration. Structural PASS never means human approval, Figma fidelity or production readiness.

Keep proprietary source, artwork, Figma secrets and human approval ledgers outside public GitHub; do not alter the established Railway, Windmill, n8n or GitHub Actions production responsibilities. Missing evidence or unauthorized tool substitution → HOLD.
