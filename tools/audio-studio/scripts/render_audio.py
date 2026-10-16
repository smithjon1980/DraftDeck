#!/usr/bin/env python3
"""BOSS-AUDIO-001: submit a fixed, public-safe script directly to Kokoro CPU TTS.

This is a candidate CPU qualification, not an ASR alignment or publishing tool.
The approved source is never generated or edited by this program.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import sys
import traceback

SAMPLE_RATE = 24_000
DEFAULT_VOICE = "af_heart"
FIXTURE_MIN_WORDS = 150
FIXTURE_MAX_WORDS = 200


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_suffix(path.suffix + ".tmp")
    part.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    part.replace(path)


def load_fixture(path: Path) -> tuple[bytes, str, int]:
    raw = path.read_bytes()
    if not raw or b"\x00" in raw:
        raise ValueError("Fixture must be nonempty UTF-8 plain prose")
    source = raw.decode("utf-8", errors="strict")
    # A source Markdown document is used as plain narration only; no headings,
    # lists, front matter, links, or stage directions are authorized in this test.
    if any(line.lstrip().startswith(("#", "- ", "* ", ">", "```")) for line in source.splitlines()):
        raise ValueError("Fixture contains Markdown instructions, not plain spoken prose")
    spoken = source.strip()
    nwords = len(spoken.split())
    if not FIXTURE_MIN_WORDS <= nwords <= FIXTURE_MAX_WORDS:
        raise ValueError(f"Expected {FIXTURE_MIN_WORDS}–{FIXTURE_MAX_WORDS} words, got {nwords}")
    return raw, spoken, nwords


def render(spoken: str, path: Path, voice: str) -> dict:
    # Delayed imports let the preflight run with Python's standard library only.
    import numpy as np
    import soundfile as sf
    from kokoro import KPipeline

    pipeline = KPipeline(lang_code="a")  # US English; CPU selected by workflow
    clips = []
    segment_text = []
    for graphemes, _phonemes, waveform in pipeline(
        spoken, voice=voice, speed=1, split_pattern=r"\n+"
    ):
        if hasattr(waveform, "detach"):
            waveform = waveform.detach().cpu().numpy()
        chunk = np.asarray(waveform, dtype=np.float32).reshape(-1)
        if chunk.size == 0 or not np.isfinite(chunk).all():
            raise RuntimeError("Empty or nonfinite audio segment")
        clips.append(chunk)
        segment_text.append(str(graphemes))

    if not clips:
        raise RuntimeError("Kokoro returned zero audio segments")
    audio = np.concatenate(clips)
    if float(np.max(np.abs(audio))) < 1e-6:
        raise RuntimeError("Synthesized audio is silent")
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.stem + ".tmp.wav")
    sf.write(str(tmp), audio, SAMPLE_RATE, format="WAV", subtype="PCM_16")
    with sf.SoundFile(str(tmp)) as f:
        if f.samplerate != SAMPLE_RATE or f.frames <= 0 or f.channels != 1:
            raise RuntimeError("WAV verification failed")
        frames = int(f.frames)
    tmp.replace(path)
    return {
        "audio_segments": len(clips),
        "tts_segment_graphemes": segment_text,
        "sample_rate_hz": SAMPLE_RATE,
        "frames": frames,
        "duration_seconds": round(frames / SAMPLE_RATE, 3),
        "wav_bytes": path.stat().st_size,
        "wav_sha256": digest(path.read_bytes()),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--voice", default=DEFAULT_VOICE)
    ap.add_argument("--preflight-only", action="store_true")
    args = ap.parse_args()

    record = {
        "case_id": "BOSS-AUDIO-001",
        "status": "NOT_ESTABLISHED",
        "started_at_utc": utc_now(),
        "source": str(args.source),
        "output": str(args.output),
        "voice": args.voice,
        "model_name": "hexgrad/Kokoro-82M",
        "model_revision_pinned": False,
        "runtime": "CPU_candidate",
        "human_listening_verified": False,
        "audio_to_script_alignment_verified": False,
        "release_authorized": False,
        "claims": ["source bytes recorded", "submitted script retained without LLM rewriting"],
    }
    try:
        raw, spoken, words = load_fixture(args.source)
        record.update({
            "source_bytes": len(raw),
            "source_sha256": digest(raw),
            "submitted_text_sha256": digest(spoken.encode("utf-8")),
            "fixture_words": words,
            "fixture_validation": "PASS",
        })
        if args.preflight_only:
            record["status"] = "PREFLIGHT_PASS_NOT_RENDERED"
            return 0
        record["kokoro_package_version"] = importlib.metadata.version("kokoro")
        record["torch_package_version"] = importlib.metadata.version("torch")
        record.update(render(spoken, args.output, args.voice))
        record["status"] = "AUDIO_GENERATED_INSPECTION_PENDING"
        return 0
    except Exception as exc:
        record["status"] = "HOLD"
        record["exception_type"] = type(exc).__name__
        record["exception_message"] = str(exc)
        traceback.print_exc()
        return 1
    finally:
        record["finished_at_utc"] = utc_now()
        write_json(args.manifest, record)
        print(json.dumps({k: record.get(k) for k in (
            "case_id", "status", "source_sha256", "fixture_words",
            "audio_segments", "duration_seconds", "exception_type"
        )}, sort_keys=True), flush=True)


if __name__ == "__main__":
    sys.exit(main())
