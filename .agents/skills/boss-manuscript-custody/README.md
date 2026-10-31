# BOSS Manuscript Custody — corrective candidate v0.2

**Disposition:** staged on a feature branch for controlled review; live manuscript custody remains HOLD. No automatic GitHub archival is active.

## Files
- `SKILL.md` — skill entry point and authority rules.
- `scripts/archive.py` — synthetic local and gated private-GitHub custody verifier.
- `tests/test_archive.py` — synthetic-only test suite; no unpublished text.
- `templates/MEMORY_INDEX_TEMPLATE.md` — neutral placeholder; NEVER a live index.

## Synthetic-only qualification
Run `python3 -m unittest discover -s .agents/skills/boss-manuscript-custody/tests -v` from the repository root.

Example command (only with your own synthetic /tmp files):
```sh
python3 .agents/skills/boss-manuscript-custody/scripts/archive.py \
  --mode synthetic-local --synthetic \
  --source /tmp/boss-synthetic.md --root /tmp/boss-custody-test \
  --id BOSS.EP00.A01.S01 --revision v0.2 \
  --expected-start 1 --expected-end 3 \
  --approvals-json /tmp/boss-synthetic-approvals.json
```

## Distinct digest scopes
`BOSS-CANONICAL-PARAGRAPHS-V1` is a precisely specified JSON-over-numbered-paragraphs algorithm with UTF-8 and LF normalization. Do not equate its hashes with historical BOSS canonical hashes without a proof of equivalence. Raw Markdown SHA-256 is independent.

## Operational limitation
A `REMOTE_ARCHIVED_VERIFIED` response demonstrates remote byte custody and an independent readback receipt, **not human approval**. The remote adapter uses `gh api` and has only been tested with synthetic mock transport. Configuration, branch controls, authenticated actor checks, and end-to-end private GitHub qualification are required before real manuscript data can be used.

A failed source/manifest/receipt transaction may leave a partially committed revision; this remains HOLD until manually reconciled. No GitHub Action is installed that automatically archives every hash. Human segmentation, ART, STORY, layout, production, and publication gates remain separate.
