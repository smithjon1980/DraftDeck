# BOSS personal knowledge workspace — integration candidate

Status: **CANDIDATE / NOT INSTALLED / NO AUTOMATED SYNC**.
Package: [BOSS knowledge-index upgrade](README.md).

## Two stores, complementary responsibilities

**Personal workspace (private):** A SilverBullet workspace is the operator's draft notebook for thoughts, professional development, research, transcripts and Academy ideas. It is not a public source of truth and must not be assumed verified.

**Project index (public-safe):** Google OKF-format records in this repository are limited to reviewed, admissible evidence pointers and test-only fixtures. GitHub PRs and run logs remain the underlying evidence. A search result is not an approval.

## Seven-gate upgrade

1. Register verified source URLs and observed lifecycle status as provenance-linked records.
2. Evaluate **SilverBullet** using a separate, locally controlled workspace containing **fictional test data only**; verify Markdown round-tripping, links/backlinks, tags, mobile access, and backup recovery.
3. Design an explicit **human-reviewed transfer**: capture → classify → redact → source-check → select excerpts → PR review → publish. Do not directly sync a personal vault to a public repository.
4. Qualify deterministic keyword and identifier search as a traceable baseline.
5. Compare opt-in FastEmbed/Qdrant semantic retrieval against the baseline, then hybrid retrieval if results justify it. No shared or hosted database is required for a local test.
6. Evaluate freshness, missing evidence, status contradictions, and explicit dependency edges before introducing a graph retrieval server.
7. Gate any ChatGPT read-only connection on authenticated access, citation quality, tenant isolation where relevant, and owner approval. No protected write routes or production release.

## SilverBullet evaluation checklist (proposed, not yet verified by deployment)

- Local/private Markdown remains readable without SilverBullet.
- Import/export preserves documents and links with no unexpected transformations.
- Backups restore expected versions and edits are not silently lost.
- Mobile access and network exposure use appropriate authentication and TLS.
- Space scripting and extensions are treated as executable code and reviewed.
- An unreleased personal note cannot appear in the public knowledge index.
- An explicitly reviewed excerpt retains a traceable original source URL and the distinction between observation and recommendation.

## Publication boundary

The **entire voice conversation is not an approved public artifact**. Do not commit its raw transcript, private plans, unreleased instructional scripts, identities, secrets or customer data to the public DraftDeck repository. For Academy use, create a separate redacted lesson only after owner review. Tests here exercise **policy declarations**, not a deployed security boundary.

## Decision

**Evaluate SilverBullet; do not deploy or operate it yet.** Keep this separate from current Render/Railway/Windmill/n8n services. No new credential, server, Docker container, connector or private data ingestion is authorized by this document.

Useful upstream references: [SilverBullet source](https://github.com/silverbulletmd/silverbullet), [documentation](https://silverbullet.md/), [current Google OKF repository](https://github.com/GoogleCloudPlatform/open-knowledge-format).
