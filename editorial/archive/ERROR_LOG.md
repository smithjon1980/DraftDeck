# Bioscillate Error and Incident Log

This log records observed failures, impact, evidence, diagnosis, corrective actions, and verification. Entries are append-only; corrections must be new entries. Do not confuse GitHub API failures with network/authentication outages.

## ERR-2026-11-05-001 — GitHub contents API create-file conflict

- **Observed:** 2026-11-05, America/Chicago (exact request timestamp not captured).
- **Component:** GitHub connector, `create_file`.
- **Repository:** `smithjon1980/DraftDeck`.
- **Branch:** `archive/editorial-history-2026-11-05`.
- **Path:** `editorial/archive/README.md`.
- **Severity:** Recoverable write failure.
- **Reported API response:** HTTP 422, `"sha" wasn't supplied`.
- **Trigger:** A create-file operation was attempted for a path that already existed.
- **Diagnosis:** Existing-file conflict / wrong write operation. This is **not evidence of GitHub connectivity or authentication failure**.
- **Impact:** Attempted create failed; archive README was already present. The four historical manuscript contents remain uncommitted.
- **Verification:** Subsequent `fetch_file` read the existing README, and `create_file` successfully committed `editorial/archive/CHANGELOG.md` as commit `f9b0cdc54685d9473346ad476a18bc35a6d445c0`.
- **Corrective action:** Fetch/check file existence and current blob SHA before writes. Use `create_file` only for absent paths; use `update_file` with current SHA for intended updates. For immutable candidate archives, create new uniquely named paths instead of replacing previous versions.
- **Status:** API write path verified functional; preventive automation **not yet implemented or tested**.
- **Follow-up:** Add idempotency and conflict tests to archival workflow; finish committing recovered historical manuscripts; record checksums and provenance; human review before merge.
