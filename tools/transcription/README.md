# BOSS / DraftDeck — Transcription Tool

Status: **Candidate; integration and end-to-end test pending**.

This tool belongs beside the Command Kit as a reusable **speech-decoding capability**. It does not replace governance, transcription skill instructions, or a speech-model binary.

## Source and custody

- Upstream: https://github.com/ggml-org/whisper.cpp
- License: MIT; preserve notices in upstream distribution.
- Upstream is **not vendored** here. Bootstrap clones an explicitly selected release/ref and records the resulting commit SHA.
- Model weights are downloaded separately. They are **not** committed into DraftDeck.
- Uploaded recording stays local to the operator unless a separate remote handoff is authorized.
- GitHub storage is not a running transcription environment.

## Workflow

`MEDIA → PROBE → NORMALIZE → CHUNK → ASR → TIMESTAMPS → DIARIZE → VERIFY → RENDER → DELIVER`

Local whisper.cpp performs **ASR**, not guaranteed multi-speaker diarization. Do not label a two-speaker transcript verified until a distinct diarization and listening pass is complete. Never manufacture speech or speaker identity.

## Bootstrap (Linux/macOS with git, cmake, ffmpeg, Python 3)

```bash
bash tools/transcription/bootstrap-whisper.sh v1.8.2 base.en
```

For a different upstream release, supply an explicit ref; verify that the ref exists before trusting it. The bootstrap script records `WHISPER_UPSTREAM_COMMIT` and installs into `tools/transcription/vendor/whisper.cpp` (ignored by Git).

## First test

```bash
python3 tools/transcription/transcribe.py --input /path/to/recording.m4a --model base.en --out-dir /path/to/output
```

This generates a raw TXT and timestamped SRT as **ASR candidates**, plus a JSON receipt recording source hash, runtime, model path, engine commit and command. These are not the final verbatim, speaker-diarized Markdown artifact.

## Verification gate

Confirm source start and ending, all chunks (if chunking becomes necessary), timestamps, repeated voices, fillers, no hallucinated wording, human review, and consistent VOICE A/B labels. Until those are satisfied: `TRANSCRIPT_CONTENT_VERIFICATION=HOLD`.

Future work: reproducible CI smoke test; source-specific chunk offsets; a true diarization backend; full voiceover renderer; optional GPU/remote runners. Avoid claiming any of these exist yet.
