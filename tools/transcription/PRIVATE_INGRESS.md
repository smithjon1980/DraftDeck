# Private audio ingress — Option 1

State: IMPLEMENTED IN BRANCH; NOT YET END-TO-END EXECUTED.

Workflow: `.github/workflows/whisper-private-ingress.yml`.

1. Store the audio in private object storage (for example S3 or compatible storage) and issue a **short-lived HTTPS GET signed URL**. Do not publish the URL in chat, GitHub issues, commits, manual workflow inputs, or logs.
2. In GitHub → DraftDeck → Settings → Secrets and variables → Actions, configure `WHISPER_SIGNED_AUDIO_URL` with that URL. The secret must be updated whenever the URL expires. GitHub secrets are stored persistently, so remove or replace it after use.
3. Calculate SHA-256 from the exact original audio bytes. The expected hash is not secret.
4. On the feature branch, manually dispatch `Whisper private signed URL ingress` with `source_id` and `sha256`. Trigger immediately while the URL is valid.
5. The runner retrieves via HTTPS, imposes a 40 MB limit, validates the hash, and stops before ASR on failure. Raw bytes are temporary and never uploaded as an artifact. The artifact contains only transcript text, SRT, and a redacted receipt. Retention is 7 days.

Security limitations: signed GET URLs are bearer credentials; repository collaborators with secret-management access may be able to modify workflow code to exfiltrate a secret, so restrict who can edit and dispatch the workflow. A repository secret on a public repo is not equivalent to a one-time ephemeral secret. For stronger isolation, migrate to a protected Environment secret with approval and an isolated runner. Do not dispatch unreviewed workflow changes with privileged secrets.

SRT is not speaker diarization. The resulting text remains an ASR candidate, with verbatim accuracy and VOICE A/B diarization marked NOT ESTABLISHED. A human or verified acoustic model must validate speech, speaker changes, and exact words.

No cloud presigned URL issuer or GitHub secret-management operation is presently exposed in the connected tools. Until one is provisioned, this implementation cannot complete the real recording test. Never replace it with a publicly accessible permanent file link.
