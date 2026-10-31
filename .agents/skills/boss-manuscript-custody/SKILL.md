---
name: boss-manuscript-custody
description: Source-bound archiving and retrieval protocol for BOSS manuscripts, hashes, editorial decisions and future ChatGPT context handoffs.
---

# BOSS Manuscript Memory and Custody — candidate v0.2 (HOLD)

## When to trigger
When the operator asks to save, revise, hash, archive, compare, approve, resume, or retrieve an Episode manuscript, or when an authorized manuscript-production workflow is configured to call the custody script. A skill file alone is **not** an automatic trigger. Configure GitHub Actions only through a separate authorized change.

## Non-negotiable boundary
- **Public DraftDeck** may contain only generic skill code and synthetic tests. Never store unpublished manuscript, live memory index, private source pointers, approval secrets, or private evidence here.
- **Private GitHub storage** must be independently authenticated and verified. Privacy unknown, public, missing permission, missing expected paragraph, or incomplete readback -> **HOLD**.
- Do not invent an approval: record status claims as claims, require scoped evidence, and never imply approval authority was verified because a hash matched.
- Do not infer that a local SHA-256 establishes GitHub custody. GitHub commit SHA, raw UTF-8 SHA-256, canonical paragraph SHA-256, and final remote readback SHA-256 are distinct.
- A failed remote manifest write may leave a source-only commit, which is *not* a complete archive. Reconcile it before retrying.

## Source ingestion and archival
1. Fetch the exact versioned source, not a summary or an AI reconstruction.
2. Require an **explicit exact paragraph range**, e.g. 001–025. Partial manuscripts require their own stated exact range and explicit editorial status. Confirm titles if a title contract is supplied.
3. Validate revisions, manuscript ID, paragraph identifiers, duplicate/missing first/interior/last and title identity. Treat directory components as untrusted input.
4. Validate structured decision evidence against the precise paragraph scope. `APPROVAL_CLAIM` is explicitly *not* `APPROVED` and remains `approval_authority_verified=false` until a separate authenticated authority check exists.
5. For local synthetic qualification, use `--mode synthetic-local --synthetic`; outputs have status `LOCAL_VERIFIED_GITHUB_HOLD` regardless of hash results.
6. For eventual real custody, use `--mode private-github` only after authorized private repository, branch, actor, access, and production security review. Verify GitHub visibility before any upload. Commit immutable Markdown, read it back at a committed SHA, commit its manifest, independently read back both, then commit a separate readback receipt and verify all three files at that receipt commit.
7. Only a fully verified remote response `REMOTE_ARCHIVED_VERIFIED` establishes *remote-byte custody*; it does **not** approve the content. Always report paragraph-level editorial status separately.
8. Record exact paths and digests from verified responses in the **private** memory index. On resumption retrieve the index and only the needed verified source ranges; never treat a context summary as an authority.
9. Segmentation, ART, STORY, layout, print and publication still require independent human authorization.

## Memory guide
The private index must contain document ID, exact version, source path, raw digest, canonical digest **and algorithm/version**, remote commit and readback result, approval claims/evidence, open blockers, and next permitted step. It must not contain assumed statuses or stale v0.12 examples copied from a template. GitHub search + source selection economizes model context; it does not enlarge the underlying context window.

## Security qualification
All testing before approval uses synthetic-only text. Test missing terminal paragraph, shifted start, unsupported approvals, symlink and traversal paths, public/unknown repo visibility, no push permission, source/manifest readback mismatch, duplicate revision and partial remote failure. The companion Python script is an **uninstalled review candidate**; do not run it on real manuscript without explicit qualification.
