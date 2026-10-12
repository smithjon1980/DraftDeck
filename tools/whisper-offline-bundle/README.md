# Offline Whisper Transcription Bundle (Python 3.12)

Portable, fully offline speech-to-text for the ChatGPT Work workspace.
No system installation, no administrator access, no internet access.

- Runtime: bundled CPython 3.12.12 (Linux x86_64) — system Python is never used
- Engine: faster-whisper 1.2.1 + ctranslate2 4.8.2 + PyAV 14.2.0 (pinned; av 19+ breaks faster-whisper's decode call)
- Model: faster-whisper-small, complete and local
- ffmpeg/ffprobe: bundled with all shared libraries
- Launcher: `transcribe.sh` — sets HF_HUB_OFFLINE=1, uses `python -S`
- Outputs: timestamped `<name>.json` + `<name>.md`, verbatim wording, global timestamps, word-level timestamps in JSON
- Speaker diarization: NOT IMPLEMENTED — stated explicitly in every output; no speaker labels are fabricated (first-appearance VOICE A/B rule documented for any future diarization)
- Proven by an offline self-test run in a scrubbed environment (`env -i`)

## For ChatGPT: how and where to find this bundle

1. Everything tracked in git lives in this directory:
   `tools/whisper-offline-bundle/` in `smithjon1980/DraftDeck`.
2. The binary archive is too large for a single repository file, so it is
   distributed as 8 numbered parts delivered alongside the repo
   (Kimi chat file delivery; ask Jonathan if you do not have them):
   `whisper-offline-bundle-py312.tar.gz.part-000` … `part-007`
   plus `ARCHIVE.sha256` (also committed here — see below).
3. Reassemble, verify, extract:

```sh
cat whisper-offline-bundle-py312.tar.gz.part-* > whisper-offline-bundle-py312.tar.gz
sha256sum -c ARCHIVE.sha256   # must report OK; the expected hash is pinned below
tar -xzf whisper-offline-bundle-py312.tar.gz
cd whisper-offline-bundle-py312
./check_bundle.sh             # self-check: runtime, libraries, model, ffmpeg
./transcribe.sh <audio_path> <output_dir>
```

4. Full usage, offline guarantees, transcription rules, and the self-test
   procedure are documented in `README.bundle.md` (the README shipped inside
   the archive).

## Pinned archive integrity

SHA-256 of the complete reassembled `whisper-offline-bundle-py312.tar.gz`:

```
90ea15df5ba7971e579bf1f35462c1d1bcc31913103081c7b3401ee3b3d316ff
```

`ARCHIVE.sha256` in this directory carries the same pin in `sha256sum -c`
format. `CHECKSUMS.sha256` (per-file, 4839 entries) ships inside the archive.

## Self-test expectation

Running `./transcribe.sh test/test_audio.mp3 test/out --language en` on the
bundled test audio must produce, word-for-word:

> Package operations govern how AI work is received, inspected, transformed, and released.

## Target use

Transcribe `Governing_AI_Work_with_Package_Operations.m4a` (~20:59) offline,
then use the transcript to adjust the 13-slide Package_Operations deck.
The transcript is SOURCE-lane material: route it through `02_WIP`, promote
only reviewed outputs to `03_FINALS`.
