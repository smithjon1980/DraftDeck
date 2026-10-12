# BOSS audio integration roadblocks — October 2026

Status: Archived for operator continuity and candidate Day Zero lessons. Transcription automation PAUSED by user request. PR #42 draft/HOLD.

- Historical multipart Whisper bundle did not transfer automatically into the new conversation runtime. A reusable skill alone did not provide a working executable or model.
- Local environment could decode M4A but could not fetch the upstream GitHub code via git clone. Separate media decoding from speech recognition.
- Hosted GitHub Actions run 38106021386 successfully installed and executed whisper.cpp on synthesized speech, producing candidate TXT, SRT and receipt. This test did not establish real-sample fidelity or speaker diarization.
- The real 20-second recording was prepared but lacked an approved private ingestion path. A signed-URL GitHub Actions workflow and SHA-256 gate were added to PR #42; credential provisioning and real transfer remain unverified.
- SRT word timestamps do not constitute acoustic speaker identity. Label VOICE A/B only from acoustic evidence and review.
- WhisperX speaker diarization may depend on pyannote; alternative front ends are not necessarily independent failover engines.
- NotebookLM ingestion should admit approved current doctrine while keeping historical superseded drafts in a separate archive.
- User elected to pause automated transcription; when supplied, an externally generated transcript can be inspected without pretending it was produced by our runner.

Open gates: verify each adapter license and model usage terms; pin exact versions; test primary and alternative implementations on real authorized input; preserve original recording; audit speaker changes, fillers, and timestamps; authorize final Markdown only after source comparison.

Operational rule: no new transcription execution, credential provisioning, or PR merge solely because this archive was committed.
