# Visual evidence manifest gate — execution candidate

This adds a machine-readable review-bundle **metadata** validator for the existing [visual evidence protocol](../../doctrine/visual-evidence-gate.md). It does not replace `check_contract.py`, `check_brand_proof.py`, `render_local_proof.py`, Playwright, or human page inspection.

## Local execution

```sh
python -m unittest discover -s tests -p 'test_evidence_manifest.py' -v
python tools/visual-poc/check_evidence_manifest.py /PRIVATE/evidence/manifest.json --evidence-root /PRIVATE/evidence
```

Use these manifest keys: `candidate_id`, `source_commit`, `profile`, `source_reference`, `dimensions: {width,height}`, `reference_status`, `artifacts`, `checks`, and `human_review`. Artifact keys: `source_manifest`, `copy_manifest`, `browser_render`, `comparison`, `difference_annotations`, `native_text_art_evidence`. If reference is approved, add `approved_reference`. Checks: `source_copy`, `story_art`, `logo`, `cad`, `legibility_contrast`, `clipping_collisions`, `browser_behavior`, `adapter_fidelity`, `target_editability`; each check is `PASS`, `FAIL`, or `NOT_TESTED`. Human review is `PENDING`, `REJECTED` or `APPROVED_FOR_NEXT_GATE`, with reviewer/date/hash/scope for the last state.

Exit status: 0 = metadata eligible for *next gate*, 1 = invalid metadata, 2 = valid but HOLD. **Even status 0 does not prove a pixel match, adapter editability, actual approval authenticity, or authorize publication.** Metadata is untrusted and must be correlated with actual evidence and independent human review. Keep private artwork, exact scripts, screenshots and logos outside public repository and CI logs.

### Missing validations (intentionally not claimed)

No cryptographic evidence-content validation; no image comparison; no HTML DOM/layer verification; no browser version binding; no secure reviewer signature; no CI deployment gate integration. Those remain distinct follow-up work, not implicit passes.
