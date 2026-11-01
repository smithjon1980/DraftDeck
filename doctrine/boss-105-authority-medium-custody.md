# BOSS 105 — authority, medium, custody and evidence contract v1.0

**Status:** REVIEW_CANDIDATE · **User action:** upgrade implementation requested, **not** blanket ART/STORY approval, deployment or publication.

## Decision-rights matrix

| Gate | Precondition | Human decision required | What automation may do | Evidence |
|---|---|---|---|---|
| Source admission | exact source bytes, verified repo/ref/path/blob and unrestricted legal access | SOURCE_ADMIT source ID | compute/harden hashes, reject mismatches | readback + immutable source record |
| Editorial | 25 exact paragraphs + reviewed copy identity | APPROVE EDITORIAL candidate ID | compare and record findings | source + explicit human declaration |
| Narrative qualification | approved exact source | QUALIFY NARRATIVE candidate ID | report continuity, accuracy, pacing, issues | paragraph-level QA, read-through |
| Medium selection | episode, target and reference scope | APPROVE MEDIUM candidate ID | render isolated medium proposals | scoped review identity |
| ART | admitted source, story brief, medium, isolated asset | APPROVE ART candidate ID | generate isolated candidates and objective tests | source/preview hashes + genuine human inspection |
| STORY | ART human accepted for same target | APPROVE STORY candidate ID | propose independent causal visual and hidden-label test | separate source/preview hashes + genuine human inspection |
| Opener | separately grounded anchor record | APPROVE OPENER candidate ID | layout study and tests only | approved anchor scope |
| Closer | separately grounded anchor record | APPROVE CLOSER candidate ID | layout study and tests only | approved anchor scope |
| Segmentation | narrative-qualified source and new authorization | AUTHORIZE SEGMENTATION source ID | exact split with reconstruction proof | source round-trip digest |
| Composition | exact qualified copy, matching ART+STORY and anchors | AUTHORIZE COMPOSITION target | build native text + approved artwork | linked approval ledger identities |
| Final layout | rendered browser/PDF and adapter proof | ACCEPT LAYOUT candidate ID | compare render, text and PDFs | human reviewer + test receipts |
| Publication/production | all prior gates + secure transport/custody | RELEASE target/digest/action | only perform expressly authorized effect | authenticated action-specific event and post-effect custody |

Generic "proceed" is never an implied approval of any gate. A human conversational command is evidence of *declaration*, not proof of ledger custody or authenticated actor identity. The independent approval service must attest actor, event uniqueness, scope, exact hashes, validity/expiry and replay resistance. CI and models cannot mint human authority. A rejection makes a new candidate ID and digest; older approvals do not carry forward.

## State and identity model

Use distinct, never silently promoted fields: source custody, editorial, narrative, medium, ART, STORY, opener, closer, segmentation, composition, structural, visual, adapter, security, final release. Each dimension has PASS, FAIL, HOLD or NOT_TESTED and its own evidence references. For runs distinguish CONFIGURED, DISPATCHED, COMPLETED and OUTCOME_ACCEPTED.

Candidate identity is immutable. A suggested opaque ID format is BOSS.EP00.A01.S01.P001A.ART.C002; hashes and target fields, not ID spelling alone, prove binding. Audit and invalidate on source, paragraph, medium, dimensions, crop, preview, asset, profile, target or composition changes.

### Digest separation
- Git commit SHA: 40-hex commit object ID.
- Git blob SHA: 40-hex blob object ID; not SHA-256.
- Raw SHA-256: exact file bytes.
- Paragraph SHA-256: exact UTF-8 text bytes of that paragraph, no automatic normalization.
- Canonical paragraph serialization BOSS-PARAGRAPHS/1.0: exact UTF-8 text of P001..P025 joined with two LF characters, no trailing LF, no trimming or NFC transformation.
- Canonical SHA-256: digest of that exact serialization.
- Remote readback: independent compare to remote bytes and ref after actual authorized writes. A stored hash string or commit message is not a readback.

This contract does not claim to recover the historical missing v0.12 P001–P005 or reinterpret v0.11 custody as a production master. The reported APPROVED-EDITORIAL-001 source must be independently recovered and read back against its actual repository/ref before real generation.

## Archive safety requirements

All executable file operations must occur under an explicitly allowed archive root. Reject absolute paths, traversal, symlinks that escape root, malformed Unicode/control bytes, and collisions; allocate candidate paths once and use fsync+atomic rename with no-overwrite semantics where appropriate. Preserve approved revisions and all component drafts. Use manifest-before-effect custody and exact remote readback for every authorized archival write. A local filesystem check does not establish GitHub or Google Drive persistence.

No manuscript body, restricted identity, credentials, private reviewer event, unpublished art or private Figma asset is admitted to the public code repository. The new validator and tests use fabricated paragraphs exclusively.

## Episode medium boundary

| Scope | Current direction | Authority | Gate |
|---|---|---|---|
| Episode Zero, Section 01, P001A | Photorealistic executive and hypothetical Texas corporate-campus narrative, matching owner-provided references | Requested visual direction, not image acceptance | A separate owner-scoped medium record and visual review |
| Episode 01 Slide 02 | White-ground CAD-informed technical editorial illustration; no photo/corporate stock imagery | Existing DraftDeck candidate contract and skill | Preserve until independently changed |
| Other targets | Unknown | Never inherit either visual policy by accident | HOLD pending target decision |

Keep rejected mixed P001A-ART-CANDIDATE-001 as historical evidence, not isolated ART. Its exact private image and reference hashes require restricted custody. New candidates must first make the visual **medium** unambiguous, then keep CAD separate from ART; STORY must not be a compilation of slide scenes.

The hypothetical campus is not a project claim: proposal or rendering does not establish a building permit, contract award, financed construction, shipment, tenant occupancy or completed delivery. Preserve stated initial approximately 4,000-person scenario and possible expansion toward 10,000 *as hypothetical narrative quantities* only if admitted exact copy substantiates them.

## Narrative-to-production separation

Source → exact source admission → story architect brief (Bridge 1) → visual story/medium decision (Bridge 2) → ART candidate → human ART → dependent STORY candidate → human STORY → opener+closer anchors → narrative qualification + authorized fresh segmentation → editable React/Tailwind composition → actual browser/PDF/adapter inspection → independent release.

Narrative qualification (oral pacing, didactic accuracy, executive→architect→developer→Main Street Copy→carrier→receiving-office continuity, execution between authorization and review, RQ vs governed operations separation) must precede segmentation. Creative visual directions cannot change exact source words. For paragraph fragments, only split at sentence boundaries while preserving all whitespace and exact reading order. v0.8 110-unit segmentation is historical, not an inherited authorization.

## Security and runtime separation

The provided real-production gateway HOLD evidence remains unresolved: a synthetic 7/7 does not prove unbypassable network enforcement; all protected writes still require authenticated actor/dot identity, exact digest human approval + replay protection, durable pre-effect custody, tenant separation and malicious browser/egress testing. Distinguish containment from reversal; retries require real idempotency keys and reconciled external effects. No automated commit, paid infrastructure, deployment, publication, carrier action, real payment or supplier order may be performed by this proposal or synthetic CI.

## Evidence package format

Store a restricted index with candidate ID; exact source/ref/commit/blob; separate raw/canonical and paragraph digests; episode/section/target/profile/composition; visual-medium decision; art/story asset+preview digests; source/brand reference provenance; all gate states; human decision record references (never signing material); review findings/severity/closure; browser screenshot dimensions; PNG/SVG/PDF metrics; native text proof; destination edit-save-reopen results; workflow config/run IDs; unresolved holds and release authority.

Until an evidence-backed runtime gate reports its outcome, use NOT_TESTED. A structural check does not confer editorial, visual, adapter, security, economic or production approval.

## Skill dependency graph

AGENTS + design contract → BOSS-105 Gate Coordinator → Story Architect → Visual Storyboard + Medium → Art Asset Producer → Art & Story Reviewer → Precomposition Human Approval (ART then STORY) → Opener/Closer Human Review → Editorial Layout Director → React/Tailwind → Browser/PDF/Adapter Tests → Human Release.

Optional Figma design bridge only after admissible scoped input; it cannot replace the renderer or ledger. The BOSS NotebookLM Source Stager supplies grounded candidate material but cannot authorize final manuscript source status.

## Verification boundary for this implementation

- Implemented in this PR: explicit control register, a bounded coordinator skill, structural source/ART/STORY validator, synthetic regression fixtures, and read-only CI configuration.
- Not established by a document/validator alone: 105 operational enforcement points, real authenticated ledger, source remote readback, visual medium acceptance, narrative qualification, proof of original layer isolation in pixels, PDF/browser acceptance, source-to-prod orchestration, transport non-bypassability, or release.
- Protect existing main until review, negative tests, independent verification, and explicit operator merge decision.

