# BOSS 105 — synthetic gate utility

**Candidate, not production authorization.** This directory holds a Node.js 24 stdlib-only, read-only structural validator and synthetic test suite for source, medium, ART/STORY, scoped approval tokens and composition preconditions.

## Run
- node --test tools/boss105/test.mjs
- node tools/boss105/validate.mjs path/to/synthetic-manifest.json

Exit codes: 0 = structural PASS; 2 = FAIL; 3 = HOLD (including every unverified real-human/custody release path). The JSON stdout is a machine-readable result.

Input includes:
- schema BOSS-105/1.0; mode SYNTHETIC or REAL; explicit run stage;
- source with repo, safe relative path, Git commit/blob, **separate** raw SHA-256 and canonical SHA-256, serialization BOSS-PARAGRAPHS/1.0, P001..P025 text and individual hashes;
- target with episode, section, slide ID, output profile, composition ID, scoped medium and decision reference;
- checks for structural, editorial, visual, adapter, security and human decision using PASS/FAIL/HOLD/NOT_TESTED;
- separately hashed ART and STORY assets and previews, source digest binding, isolation declarations, source provenance and declared dimensions;
- synthetic-only approval fixtures, not genuine signatures/ledger receipts;
- optional exact narration and seven-layout composition declarations.

## Important limits
1. The validator reads supplied manifest data; it does not fetch GitHub, authenticate an approval, inspect pixels, inspect browser/PDF output, confirm a hash against original binary artwork, or open a production secret store.
2. In SYNTHETIC mode, fixture approvals simulate matching scope for **regression tests only**. A synthetic PASS must never be interpreted as human acceptance.
3. REAL mode intentionally returns HOLD, even with apparently valid hashes, until an independent source readback, authenticated restricted approval ledger, visual inspection and secure execution gateway are integrated and tested.
4. RELEASE_CANDIDATE always returns HOLD; no model/manifest can mint release authority.
5. Existing true production workflows, approved scripts, custody archives and visual masters are not changed.
6. The 105-point register tracks requirements, not implementation proof. Each independently verified enforcement point needs its own run and evidence references.

## Synthetic negative cases
The test suite covers missing P025, late/duplicate numbering, changed paragraph bytes, wrong canonical format, unsafe paths, candidate layer contamination, wrong medium/episode, misleading completed-campus claim, missing/mismatched ART or STORY approvals, wrong target/profile/composition, candidate reuse after hash change, unqualified narrative, unaccepted opener/closer, noneditable/changed composition copy, unknown layout, consequential effects and attempts to promote self-authored approval.

## Remaining integration work
- Authenticated real approval ledger adapter with non-replayable actor/dot identity.
- Actual remote source custody readback/atomic archive adapter.
- Real ART/STORY pixel reviewer and exact preview hash evidence.
- Browser renderer and native text round-trip, PDF parity, destination edit-save-reopen.
- Security gateway route enforcement and malicious egress/tenant negative tests.
- Approved operator-scoped medium record and narrative qualification for the exact current manuscript.
- Real run receipts for workflows, VTracer and final human release.

The review branch tests must execute under contents: read with no repository writing, external effect, manuscript, private art or approval credentials.



## Additional read-only checks
- Local source identity: node tools/boss105/readback.mjs SOURCE_ROOT RELATIVE_SOURCE_PATH RAW_SHA256 GIT_BLOB_SHA. Computes raw SHA-256 and the Git SHA-1 blob object ID from actual local bytes; rejects traversal, missing files, external symlinks and mismatches. PASS means **LOCAL_ONLY**, not GitHub, Google Drive or archive readback.
- Signed claim scope: tools/boss105/approval-claim.mjs exports canonicalApprovalClaim and verifySignedClaim for Ed25519 verification against a separately provided public trust anchor. Checks source/target/asset/preview/profile/composition/gate, expiry and local duplicate events. Even a cryptographically valid claim returns **HOLD** until the real authenticated human ledger, actor-to-key trust, external custody and durable replay check are established.
- Tests dynamically create synthetic temporary source fixtures and ephemeral Ed25519 key pairs; no authentic private keys or protected manuscripts are stored or fetched.

Never reuse the test key, test event IDs, or test-only approvals for a real production decision.
