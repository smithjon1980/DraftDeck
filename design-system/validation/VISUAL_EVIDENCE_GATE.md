# Visual evidence record — candidate gate

This validator adds **metadata structure checks**, not automated judgment of visual quality.

Run:
```sh
python3 design-system/validation/test_visual_evidence.py
python3 design-system/validation/check_visual_evidence.py design-system/validation/visual-evidence-example.json
```

Copy the example JSON into a **private evidence workspace** for real work. Replace the source commit and explicit states; store actual screenshots, story art, reference documents, scripts, logos and difference overlays privately. In public DraftDeck commits, only opaque private evidence IDs or approved provenance identifiers may be recorded.

- Every required artifact and gate must have an explicit `PASS`, `FAIL`, `NOT_TESTED` or `HOLD`.
- `PASS` artifacts require a non-empty private `evidence_ref`; HTTP links are rejected to discourage leakage.
- Layout/export `PASS` requires browser render, side-by-side comparison and difference-annotation evidence records.
- Human approval **cannot** be granted by this tool. All accepted records have `release_state: HOLD` and `human_authorization: PENDING` or `REJECTED`.
- The validator does not open or authenticate evidence, compute image differences, prove accessibility, check logo authenticity, verify adapters or inspect actual rendered quality. Those remain separate procedures under `doctrine/visual-evidence-gate.md`.

This is a review candidate, not a new design master. Keep existing design-contract checks and human signoff intact.
