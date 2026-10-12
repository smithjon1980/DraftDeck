# BOSS AudioWorks — Modular Audio Stack (Candidate v0.1)

**Status:** design and repository integration recorded; execution is PAUSED at user request. **Do not merge PR #42 based on these documents.**

## Principle
A **stack** is a collection of specialized tools connected through explicit interfaces and governed by shared evidence contracts. A **primary** is the preferred implementation for one capability; a **failover** is a distinct method invoked only when a documented trigger occurs. Two tools present in a repository are not a tested failover pair.

Each external project is upstream-owned. Link/pin dependencies; do not fork upstream without a necessary patch. Record upstream revision, licenses, model-access requirements and runtime constraints before deployment. Licenses of code and model weights may differ.

## Tool registry
| Stage | Primary | Failover / companion | Notes |
|---|---|---|---|
| Compression, codec conversion and segmentation | FFmpeg (https://github.com/FFmpeg/FFmpeg) | Audacity manual editing (https://github.com/audacity/audacity) | Audacity is an operator path, not unattended CLI equivalence |
| Speech activity detection | Silero VAD (https://github.com/snakers4/silero-vad) | FFmpeg energy/silence detection + manual listening | VAD is an optional analysis aid; cannot justify omitting low-energy speech |
| Transcription ASR | whisper.cpp (https://github.com/ggml-org/whisper.cpp) | faster-whisper (https://github.com/SYSTRAN/faster-whisper) | Current CI verifies only synthetic input on whisper.cpp |
| ASR + word alignment | WhisperX (https://github.com/m-bain/whisperX) | whisper.cpp or faster-whisper timestamps + manual alignment | Alignment is not verbatim correction |
| Acoustic speaker diarization | pyannote.audio (https://github.com/pyannote/pyannote-audio) | WhisperX diarization integration, then manual speaker audit | WhisperX may itself use pyannote: not an independent model fallback |
| Human transcript editing | Subtitle Edit (https://github.com/SubtitleEdit/subtitleedit) | Audacity and text editor / direct audio replay | Operator intervention; document edits and ambiguities |
| Rendering / verification | BOSS voiceover-transcription-diarization skill | Manual review of source audio + structured receipt | Neither ASR nor diarization alone establishes accuracy |

## Architecture boundaries
- Original audio is immutable evidence master: sha256, duration, sample rate and lineage.
- Compressed/normalized audio is a **derivative**, not replacement. Lossy compression may remove fillers, sibilants or quiet speech.
- VAD must never silently delete presumed nonspeech segments. Keep offsets and explicit coverage.
- ASR produces text hypotheses; alignment maps times; diarization produces anonymous acoustic clusters; human review establishes accuracy.
- Diarization labels sorted by first audible appearance: VOICE A, VOICE B, etc. Never infer speaker names, gender, personal identity or roles.
- Preserve fillers, repairs, repeated phrases, crosstalk and uncertain boundaries. Never clean up silently.
- Do not automatically accept a fallback whose output differs. Record the divergence for inspection.

## Mandatory failover contract
1. Probe selected engine and model (availability, exact revision, execution permissions, resource budget).
2. Attempt primary once; capture exit code, stderr digest and elapsed time.
3. Trigger failover only for explicit cause (missing dependency, crash, OOM, timeout, corrupt output, incompatible audio).
4. Run fallback on the **same authenticated source** or a declared derivative; record input sha256 and parameters.
5. Verify artifact presence, nonempty text, monotonically increasing timestamp offsets and complete coverage; do not assume accuracy.
6. Emit receipt with `stage`, `attempted_engine`, `fallback_engine`, `trigger`, `model_revision`, `source_sha256`, `result`, `human_review`.
7. If no working backend is available, stop with `NOT_ESTABLISHED`, never invent a transcript.

## Operational selection by device
- CPU-only: FFmpeg → whisper.cpp (small/base model) → optional pyannote only if system can support it; manual speaker marking is permitted but explicitly manual.
- GPU available and proper model access: FFmpeg → WhisperX (+ faster-whisper underneath) → pyannote acoustic diarization → Subtitle Edit inspection.
- Offline strict privacy: FFmpeg / local whisper.cpp / local Audacity / local Subtitle Edit; models downloaded and approved in advance. Do not imply pyannote model access is universally offline without prior authentication/cache.

## Release gates
G0 source authenticated; G1 processing receipt; G2 ASR executed; G3 timestamp coverage; G4 speaker change evidence; G5 verbatim review against audio; G6 authorized Markdown export.
**Present release status:** G2 passed only for generated synthetic audio. Real-source G0–G6 not established. PR #42 DRAFT/HOLD.
