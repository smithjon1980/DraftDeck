# Figma Design Bridge — governed v0.3 corrective candidate

**Status:** CANDIDATE_FOR_REVIEW. Rebuilt from the merged v0.1 requirements and the original four review findings and three additional fail-open probes. This file is NOT merged doctrine, production qualification or release approval.

## Authority
GitHub holds authoritative tokens, source manifests, seven layout definitions and versioned rules. Figma is an optional design-specification and component-handoff workspace. React/Tailwind produces the real editable slide/web output. Windmill, n8n, Railway and GitHub Actions keep their existing responsibilities. The human operator grants independent art, story, composed-design and final release approvals. Figma and CI cannot mint approvals.

## Mandatory Episode Zero order
1. Admit the exact private v0.7 manuscript with 25 paragraph digests plus five actual reference hashes/scope and story bridge. The old “Work Must Survive the Conversation” wording and scenes are **reference-only**, not current source.
2. Qualify the **Section 01 opener and closer** before any P001–P025 interior slide. Uncomposed Figma LAYOUT_STUDY can explore CAD zone geometry before art/story approval, but cannot be represented as completed art.
3. Produce genuinely independent text-free ArtLayer and preview. Human approves its exact asset+preview hashes for the identified target. Separately submit a causal StoryLayer and obtain its own exact-target approval. Missing approval or changed source = HOLD.
4. Optional Figma COMPOSITION_HANDOFF may combine source-locked text specification, independently accepted art/story, seven approved layout family and proper tokens. It does not make final source, authorize release or replace production React/HTML.
5. Inspect reference ↔ Figma native frame ↔ actual React/Tailwind browser render, exact manuscript-to-DOM parity, CAD border/rail and illustration meaning. Browser/PDF parity, downstream editor edit-save-reopen and human publication are independently checked.
6. Only after **both** anchor approvals linked to this manuscript source may interior paragraph layout pilots begin.

## v0.3 exact handoff binding
Contract `BOSS-FIGMA-BRIDGE-V2` requires a `target` with: `kind`, `section_id`, `target_id`, `composition_id`, `profile`, `layout_variant`, `source_digest`, and `paragraph_ids`. It must agree with the candidate's source and target profile. An opener/closer has no individual paragraph ID; each interior slide must use its matching P### ID. For current Section 01 the ONLY valid interior IDs are `P001` through `P025` (inclusive); `P000`, `P026`, `P999`, or any other target MUST fail closed. An `INTERIOR` record must reference both opener/closer next-stage human approvals matching the source digest, and those two anchors MUST have distinct `human_record_ref` values. The structural presence and distinctness of references never authenticates the approvals.

For `COMPOSITION_HANDOFF`, each distinct Art and Story acceptance record must match the corresponding named layer's candidate ID, source asset and preview SHA-256, same composition candidate, same source/target/variant/profile/paragraph IDs and a separate human record reference. A composed-design acceptance record is likewise candidate and target bound. V1 manifests must be migrated; no grandfathered `HANDOFF_READY` approval.

The v0.3 validator derives palette values from `design-system/boss-design-contract.json`, derives seven names from `experiments/episode-zero-seven-phase1/scripts/layouts.mjs`, and checks `design-system/tokens/tokens.css` against that authority. Original SEVEN 17×11 geometry and a 1920×1080 screen composition are separate output profiles; never stretch the former to the latter. Reference-only imagery must not silently import old subjects, setting, labels, or typography.

## WEB_COMPONENT_SPEC — independent web track
A Figma web component study is not a functioning website. A `HANDOFF_READY` *design specification* must include three contiguous non-overlapping mobile/tablet/desktop breakpoint bands with unique native frame IDs and widths tested inside each band. Every viewport `frame_node_id` MUST be a member of the exact `figma.frame_nodes` declared on the same handoff candidate; existence of node IDs and real Figma frame fidelity remain independently unverified. Record design-stage PASS+evidence references for responsive reflow, keyboard navigation expectations, visible focus treatment, accessibility review, English expansion, Spanish expansion and interaction states. The REAL React/browser accessibility, focus behavior, form handling, localization and mobile testing remain separate downstream gates. Do not call static fields a successful live browser test or proof of Figma-to-React fidelity.

## Security and release
Public PRs may contain rules, synthetic tests, public-safe hashes and scoped IDs. Do not upload unpublished manuscript text, original art bytes, approval-signing secrets, private evidence or restricted Figma URLs. No Figma paid generation or wider connection permissions without authorization. Structural PASS is neither proof that the cited human ledger exists nor proof that pixels match. No actual Figma or React pilot is qualified by this documentation alone. **HOLD** where evidence or approval is missing.
