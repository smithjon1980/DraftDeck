# BOSS — Separate art and story selection before composition

**Status:** CANDIDATE FOR OWNER APPROVAL. This doctrine applies to new or rebuilt Episode 01, Day Zero and Studio slide production. It does not retroactively authorize or release any slide.

## Failure prompting rebuild
The owner rejected the illustrated shop slide identified as **05/60 · Digital Property, Submission 03** on 2026-10-24. The compiled page replaced the teaching relationship with generic isometric equipment and four static blocks. The words "HUMAN REVIEW REQUIRED" on that already assembled page did not satisfy the required **independent art and story selection before composition**.

**Decision:** `REJECTED_FOR_COMPOSITION`; existing output must not be repurposed as an art master, layout template or approved story source. Preserve the rejected evidence and candidate ID for traceability; do not silently delete the record or stamp approval.

## Correct production architecture
1. **Source + lesson brief:** identify exact-current manuscript status, scope, learning objective, evidence boundaries, brand identity asset and reference provenance. For the trust-first V6 text candidate, exact new wording remains separate from V4 historical approval unless owner locks it.
2. **ART ONLY:** supply clean standalone technical-editorial illustration candidates with working React/Tailwind `ArtLayer.tsx` source and matching isolated full-resolution browser screenshots. No title rail, narrator text, reflection card or preassembled composite. Explain what each candidate depicts. A scene that is just shop furniture is rejected.
3. **ART HUMAN SELECTION:** owner explicitly chooses or rejects an exact source SHA + preview SHA and candidate ID. Selection recorded in trusted owner-controlled custody. If rejected, artist submits a new candidate with a supersession reference.
4. **STORY ONLY:** present separate `StoryLayer.tsx` source and rendered isolated browser screenshot showing the actual lesson mechanism: input -> operation/change -> inspection -> evidence -> recipient; avoid using mere labels as a substitute. For Slide 05, show what makes the shop's operation productive and what constitutes proof; not a numbered prose list on the side.
5. **STORY HUMAN SELECTION:** owner explicitly chooses/rejects the exact story candidate/source/preview digests. Art approval never means story approval, and story approval never means composite approval. The selected story must correspond to the selected art.
6. **TECHNICAL/EVIDENCE:** independently qualify technical drawings, proven versus hypothetical operations, claims, case labels, source notes, and custody distinctions. Maintain editable CAD/ISO-informed detail; no invented measured performance.
7. **NATIVE MANUSCRIPT + INSTRUCTION:** verify the separately locked paragraph mapping, live React/HTML text and reflection question; no SVG/native-text flattening. Protect complete copy outside public repo.
8. **ONLY NOW COMPOSE:** combine separately selected source layers in React/Tailwind, render at 1920 × 1080, verify brand asset, readability, visual fidelity, exact narration source hashes, and PDF/editability.
9. **HUMAN COMPOSITE DECISION + RELEASE:** user may reject final composition despite both art/story selections. CI structural checks are not human approval. No self-authorized release.

## Fail-closed production rules
- **Blocked before both independent human selections:** full composite rendering, PDF compilation, slide deck assembly, batch generation, and promotion of this slide into Studio or episode production.
- **Allowed before selections:** source inspection, brief/storyboard drafts and **isolated** art or story React/Tailwind browser previews for actual human selection, with visible candidate ID/status.
- **Blocked substitutes:** generic Python-compiled isometric blocks, placeholder icons, rasterized manuscript, screenshot crops treated as source art, imagined logos, reused historical render or a narrative that only emerges when every label is read.
- **Human is an authorization role, not an image layer.** Technical/evidence and text are additional separately verifiable sources.
- **Source and review receipts must be bound to exact candidate ID, slide ID, source SHA, preview SHA, and the separately recorded human review.** A JSON `human_approved:true`, a generated approval card, a named reviewer in a PR or a green test cannot authenticate a human.
- The companion Node verifier `tools/visual-gate/check_precomposition.mjs` checks **hash consistency only**. Its success explicitly says `compiled_slide_permitted:false` and `external_reviewer_identity_verified:false`. Only an actual authenticated human approval service or configured protected CI environment may grant the separate pre-composite authorization; these controls are NOT currently provisioned by this candidate PR.
- Failures, unknowns and missing receipts mean `HOLD`; silence is never consent.

## Review items shown to the owner (before composition)
For **Art**: four visually distinct options only if requested, isolated screenshot, teaching relationship, source provenance and exact React component. Art makes sense with ALL editorial text hidden.

For **Story**: corresponding alternative stage transitions / human actions / exception and verification, isolated screenshot and React component. Story conveys the business problem even without bullet prose.

For **Technical/evidence**: labelled facts/proposals and sources; no invented measurements, status or deployment outcomes.

**Next operator action:** produce ONLY isolated source-backed art/story review candidates and obtain owner's explicit choices before invoking the final compositor. Do not assume this documentation change counts as art or story acceptance.
