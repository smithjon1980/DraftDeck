# BOSS AudioWorks — Authenticated Google Drive Ingress (Option 2)

Status: **candidate committed, credentials unprovisioned; execution HOLD**.

This replaces the Option 1 signed-URL ingestion path in `.github/workflows/whisper-private-ingress.yml`.

## Exact validation input
- Google Drive file ID: `13DEHx7la7LrgAZ3vHLm46sTXiqV1f7nC`
- Expected SHA-256: `c03ab480fbfd836e5db6670440f9734220e3edb842a7e7379bf87905f7dc8544`
- Folder: `BOSS_COMMAND_KIT/04_Original_Audio`
- Drive file is private; do not use a public share link.

## Administrative provisioning REQUIRED (not completed)
1. In Google Cloud Console, choose/create a project, enable the **Google Drive API**, create a dedicated service account for BOSS ASR.
2. Share **only** the `04_Original_Audio` Drive folder with that service-account email as **Viewer** (not Editor). The folder must grant that account access; scopes alone do **not** limit visibility to that folder. The `drive.readonly` OAuth scope can access other files explicitly shared with the account, so enforce isolation through sharing and a dedicated service account. Verify Google account sharing policy allows it.
3. For this initial version, create a service-account JSON key, then configure `BOSS_DRIVE_SA_JSON` in GitHub > DraftDeck > Settings > Secrets and variables > Actions (prefer a protected Environment secret and environment-scoped job for production). **Never put the key in a workflow input, chat message, repo file, or output log.** Rotate/delete the key after test. Workload Identity Federation should replace long-lived JSON keys for production.
4. GitHub Actions > `Whisper authenticated Drive ingress` > Run workflow on feature branch, with non-secret inputs:
   - `drive_file_id=13DEHx7la7LrgAZ3vHLm46sTXiqV1f7nC`
   - `sha256=c03ab480fbfd836e5db6670440f9734220e3edb842a7e7379bf87905f7dc8544`
5. Inspect workflow result and `whisper-private-asr-evidence` artifact. The script does not log service-account credentials or binary media. Receipt excludes private storage URL and credential.
6. Keep PR #42 as DRAFT/HOLD until actual source ingress and content audit pass.

## Mechanism
- Install `google-auth` and `requests` on runner.
- `tools/transcription/google_drive_ingress.py` loads `GOOGLE_DRIVE_SA_JSON` secret, authenticates with Drive API, fetches file bytes using `files.get?alt=media`, limits payload to 40 MiB and verifies exact source SHA-256.
- On error, delete partial file, report `DRIVE_INGRESS_FAILED` without printing secret values.
- Only after integrity PASS, run `whisper.cpp` ASR; upload text, SRT and redacted receipt, never WAV.
- The 20-second test is an original media extract from a longer recording; it is the **source for this test** but not the full recording master.

## Security note
A JSON-key repository secret can be exploited if an attacker may edit and run workflows with access to that secret. Restrict write/Actions rights, review the workflow and use protected environments. For release, migrate to OIDC-based Workload Identity Federation to eliminate exported private keys.

## Evidence boundary
A successful download + transcription demonstrates real-source ASR execution, **not** verbatim fidelity or speaker diarization. No automated speaker-label claim without acoustic evidence. Existing synthetic CI run 38106021386 is not a substitute.
