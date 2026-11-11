# Precomposition gate — adversarial qualification
Scope: Synthetic test of the actual merged `tools/precomposition-gate/check.py` (PR #103). No private slides or art involved.

## Expected findings
- Absent, rejected, changed, cross-slide or model-labeled approvals are structurally denied.
- **Critical negative control:** a caller able to edit its own manifest can set `approval_verified_by_trusted_service=true`, assert `reviewer_kind=HUMAN` and fabricate `private:` refs. The current structural checker then produces no errors. There is no real reviewer authentication, signatures or independent trust-anchor verification here.
- A positive CI result here tests detection of that limitation, **not** authorization security.
- No composer invocation is wired into this repository gate. Therefore the claimed mandatory stop is doctrine + metadata validation, not proven execution enforcement.

## Decision
**HOLD** actual composition, approve neither the previous stick figures nor the box-based art, and keep Studio 01/02 drafts private. A separate trusted reviewer UI / signing authority must bind slide, asset SHA, preview SHA, composition target and one-time human decisions. The composer must verify such receipts outside user-controlled manifests and prohibit an ungated execution path. Repeat tests against the actual composer before calling this qualified.

## No operational changes
No production stack mutation, tokens, credentialed services, hidden content or human approval generated.
