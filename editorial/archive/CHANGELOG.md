# Bioscillate Artifact Change Log

Append-only chronological record. Never delete or rewrite previous entries. Archival is separate from editorial approval and production release.

## 2026-11-05 — ARCHIVE-BOOTSTRAP-001
- Scope: Day Zero historical manuscript archive
- Change: Created dedicated GitHub archival branch and initial archive inventory.
- Reason: Preserve all candidates, including rejected, unapproved, and superseded work.
- Status: IN PROGRESS; original manuscripts not yet committed.
- Approval: NOT REQUESTED.
- Evidence: `editorial/archive/README.md` on `archive/editorial-history-2026-11-05`.

## Entry schema
`timestamp | artifact_id | version_from | version_to | change_summary | rationale | author | commit_sha | sha256 | validation | editorial_decision | release_decision`

Record changes in new entries; do not rewrite old history. Never infer approval from a successful commit.

## 2026-11-05 — ARCHIVE-TRANSFER-002
- Change: Committed four recovered Day Zero manuscript candidates to archival branch.
- Candidate commits: `3577d9c`, `9338e4b`, `8e6ac15`, `e123fb8`.
- Editorial status: Historical candidates, not automatically approved.
- Validation pending: Original byte/line-ending and SHA-256 verification; archival workflow automation; PR review.
