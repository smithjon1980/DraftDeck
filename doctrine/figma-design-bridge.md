# Figma Design Bridge — governed integration candidate v0.1

**Status:** CANDIDATE_FOR_REVIEW. **Intent:** incorporate Figma as an optional reference-anchored *design specification and component system* for both Day Zero editorial slides and future responsive web development. No changes to the existing execution stack or public release authority.

## Rationale
Prior slide experiments repeatedly substituted generic wireframes, shortened copy, and generated collages for approved design assets. A Figma project can offer independently editable layers, component variants, constraints and visual review before coding. That is useful only when the **source, reference, story, palette and human approvals** remain upstream. Figma is not the art provider, manuscript authority, code repository, deployment target, or evidence of production feature parity.

## Where Figma belongs
```text
Operator-approved mission / EXACT SOURCE + version + SHA-256
    -> reference admission & scope: actual pixels + SHA-256
    -> story bridge / storytelling brief / illustration medium decision
    -> CAD & SEVEN layout studies (optional Figma LAYOUT_STUDY; no approved art implied)
    -> external or qualified original ART source -> HUMAN APPROVE ART
    -> independent causal STORY layer          -> HUMAN APPROVE STORY
    -> Figma COMPOSITION_HANDOFF (optional design frame and shared UI specification)
    -> React/Tailwind ArtLayer + StoryLayer + native HTML TextLayer
    -> browser screenshot + text hash + visual comparison + editability/accessibility
    -> independent final human release decision
```

**Web branch:** source-locked product requirements + brand tokens + accessible interaction model -> Figma `WEB_COMPONENT_SPEC` for navigation, forms, component variants and responsive frames -> React/Tailwind implementation -> browser keyboard/contrast/mobile/Spanish tests -> human review -> existing Railway/Windmill/n8n/GitHub Actions path. Web design studies do NOT authorize live POS writes, production deployment or account actions.

## Non-negotiable conversion contract
1. **Identity and tokens:** only `design-system/boss-design-contract.json` and approved canonical source assets determine `#FFFFFF/#000000/#00BCEB/#E30074`; no alternative visual-brand generator. Figma variables must be compared with GitHub tokens. A hex match is not a logo proof.
2. **Precise geometry:** seven named SEVEN layouts from `experiments/episode-zero-seven-phase1/scripts/layouts.mjs`, each retaining illustration, framework, narration, reflection and notes. 17×11-inch experiments and 1920×1080 slide renders are independently composed output profiles. Responsive web is not a scaled slide.
3. **Source text:** exact paragraph bytes and hashes govern React HTML text. A Figma design may mirror copy for review but cannot overwrite or rephrase it. Compare actual DOM to the source.
4. **Art:** source-traceable independent illustration; never export a flattened full-slide raster as the art layer or mistake a generated frame for a production illustration.
5. **Story:** causal sequence (business purpose → specialist task → evidence) that remains understandable when all labels are hidden. No diagram-only substitute.
6. **Approval:** ART and STORY separately accepted before full composition. Review a `LAYOUT_STUDY` before approvals only as a layout study; it cannot masquerade as composed content.
7. **Verification:** approved reference ↔ Figma frame ↔ browser screenshot side by side; log deltas and source hashes. Check native editable text, art layer, responsive accessibility and actual target-editor edit-save-reopen independently. CI validates structure, never qualitative storytelling.
8. **Custody/security:** private manuscript and unapproved art stay in owner-controlled storage. Figma external sharing and connection access must be explicitly scoped. Public PR must not leak original source bytes, tokens, approval secrets or unpublished previews.

## Figma artifact modes and promotion
| Mode | Allowed output | May advance when |
|---|---|---|
| `LAYOUT_STUDY` | CAD frame / SEVEN option / text reservation only | Reference and source IDs present; labeled `CONCEPT` |
| `COMPOSITION_HANDOFF` | Approved art and story placed as independently editable frame elements | Correct operator ART+STORY approval records bound to candidate hashes |
| `WEB_COMPONENT_SPEC` | Website flows, component library, breakpoint and state specifications | Product design review; still no code/deployment authority |

All modes are **candidates**. Promotion to `HANDOFF_READY` is evidence-based; it is not `HUMAN_RELEASE_AUTHORIZED`. Missing approval or token/source mismatch → `HOLD`.

## Immediate bounded qualification (no scope creep)
Use the already-supplied five Storybook visual references and the source-locked Episode Zero Section 01 v0.7 manuscript in **private** storage. Build the Section 01 opener and closer first, select a layout reference for each, apply the seven variant layouts as controlled studies only where meaningful, and compare exported Figma native layers against actual React render. Avoid the generated 25/20-image Figma candidates as authoritative: their existence does not establish 27-slide count, correct art, source parity, editability or approval. Only after anchor acceptance should the remaining 25 slides be qualified.

## Acceptance / exit criteria for adopting the Figma bridge
- Reference/hash and exact source manifest PASS; no external copy substitution.
- Native components, measured geometry and brand token parity PASS.
- Art and story independently accepted for the precise target and digest before full composition.
- React/HTML native text reconstructs each source paragraph exactly; browser render visual comparison inspected.
- Web test: meaningful desktop/tablet/mobile reflow, keyboard, visual focus, and English/Spanish content expansion.
- Figma design alone never constitutes an approved source asset, a shipped website, an editable Canva/Adobe export, or a public release.
- No modification of existing React/Tailwind, Windmill, n8n, Railway or GitHub Actions production responsibility.

**Release authority: HUMAN ONLY.** A tool evaluation or positive screenshot is never publication consent.
