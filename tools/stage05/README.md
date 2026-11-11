# SCC-02-SLIDE05 — Stage 05 GitHub Actions trial

**Status:** PR candidate. Human approval is required before merging or running inference. No live FLUX.1-dev result has been verified.

## Scope and contract

This experimental implementation is confined to `SCC-02-SLIDE05`, based on **Enterprise AI Operations Manual, page 05**. It generates three text-free candidate visual backgrounds, not editable DOM slides. Approved scene: human-operated print-proof registration bench, polished blank packet, authoritative blank binder/tray, misregistered analog alignment pins, unengaged manual verification lever. CAD/ISO, pure white, cyan/magenta/black only. Instructional invariant: **divergence AND missing verification**. No robotic machinery, screens, automated scanners, labels or typography.

Files:
- `.github/workflows/draftdeck-stage05.yml` — manual-only `workflow_dispatch`.
- `tools/stage05/main.go` — three inference requests, telemetry, 1536×864 PNG validation and SHA-256 records.
- `tools/stage05/run_stage05.sh` — fail-closed runner.
- `tools/stage05/package_approval_gate2.sh` — independent validation and ZIP packaging.

## Feature branch activation limitation

**This PR targets `feature/creative-composer-trial` only.** GitHub requires a `workflow_dispatch` workflow file to exist on the **default branch** to appear under Actions with a **Run workflow** button. Merging this PR into the experimental branch alone **does not activate that UI trigger**. Installing the workflow on `main`, or changing the repository default branch, requires separate authorization. Do not merge to main implicitly.

GitHub documentation: https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow

## Later manual activation steps (after separately authorized default-branch registration)

1. Accept model access and licensing terms for `black-forest-labs/FLUX.1-dev`, and confirm provider credits. Model is under a non-commercial license; do not presume rights for commercial use.
2. Repository **Settings → Secrets and variables → Actions → New repository secret**: add `HF_TOKEN` with Inference Providers permission. Never commit or paste its value into workflow files or a PR.
3. In **Actions**, select **DraftDeck - Stage 05 Artwork Candidates → Run workflow**, choose the approved branch and use `base_seed=42` (generates seeds 42, 43 and 44).
4. Download the `SCC-02-SLIDE05-Approval-Gate-2` Actions artifact. Its inner ZIP contains three native PNGs and `SCC-02-SLIDE05-stage05-manifest.json`.
5. Inspect three images independently. Human review selects one at Approval Gate 2; no automatic Stage 06 handoff.

## Provider interoperability limitation

The Go HTTP target `https://router.huggingface.co/fal-ai/models/black-forest-labs/FLUX.1-dev` is not yet verified against a live inference response. Providers may return JSON/URLs or reject particular request parameters. The Go client fails closed on non-native-PNG responses or geometry mismatches and records the failure. Fix transport incompatibilities only through a reviewed change; do not treat an error response as successful artwork.

## Security and authority boundary

- Minimal permissions: `contents: read`. No PR-triggered secret exposure, push, auto-merge, artwork selection or release.
- GitHub Actions secrets reduce credential exposure but are not a mathematical security guarantee. Restrict who can alter workflows and run sensitive branches.
- Byte-level hashes verify recorded artifacts against the manifest, not their artistic correctness or model origin independently.
- Partial/failed generation produces diagnostics, **not** an Approval Gate 2 ZIP.
- Final release and Stage 06 remain HOLD pending later human decisions.
