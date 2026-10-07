#!/usr/bin/env python3
"""BOSS offline transcription script.

Speech recognition only. Speaker diarization is NOT implemented and no
speaker labels are emitted (see DIARIZATION_STATUS). Verbatim rules:
recognized wording preserved exactly as decoded; timestamps are global
(seconds from start of file).
"""
import argparse
import json
import os
import sys

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

DIARIZATION_STATUS = (
    "not_implemented: this bundle performs speech recognition only; "
    "speaker diarization is not implemented and no speaker labels are "
    "emitted. If diarization is added later, labels must follow first "
    "appearance (VOICE A, VOICE B, ...)."
)


def fmt_ts(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def main() -> int:
    ap = argparse.ArgumentParser(description="Offline Whisper transcription (BOSS bundle)")
    ap.add_argument("audio_path")
    ap.add_argument("output_dir")
    ap.add_argument("--language", default=None, help="e.g. en; default: auto-detect")
    ap.add_argument("--beam-size", type=int, default=5)
    args = ap.parse_args()

    if not os.path.isfile(args.audio_path):
        print(f"ERROR: audio not found: {args.audio_path}", file=sys.stderr)
        return 1
    os.makedirs(args.output_dir, exist_ok=True)

    bundle_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(bundle_dir, "models", "faster-whisper-small")
    if not os.path.isfile(os.path.join(model_path, "model.bin")):
        print(f"ERROR: local model missing at {model_path}", file=sys.stderr)
        return 2

    from faster_whisper import WhisperModel

    print(f"[transcribe] loading local model: {model_path}", file=sys.stderr)
    model = WhisperModel(model_path, device="cpu", compute_type="int8")

    segments_iter, info = model.transcribe(
        args.audio_path,
        language=args.language,
        beam_size=args.beam_size,
        word_timestamps=True,
        vad_filter=True,
    )
    print(f"[transcribe] detected language: {info.language} (p={info.language_probability:.3f})",
          file=sys.stderr)

    segments, full_text = [], []
    for seg in segments_iter:
        words = [
            {"start": round(w.start, 3), "end": round(w.end, 3), "word": w.word}
            for w in (seg.words or [])
        ]
        segments.append({
            "id": seg.id,
            "start": round(seg.start, 3),
            "end": round(seg.end, 3),
            "text": seg.text,
            "words": words,
        })
        full_text.append(seg.text)
        print(f"[{fmt_ts(seg.start)} -> {fmt_ts(seg.end)}]{seg.text}", file=sys.stderr)

    base = os.path.splitext(os.path.basename(args.audio_path))[0]

    payload = {
        "audio_file": os.path.basename(args.audio_path),
        "model": "faster-whisper-small",
        "language": info.language,
        "language_probability": round(info.language_probability, 4),
        "duration_seconds": round(info.duration, 3),
        "diarization": DIARIZATION_STATUS,
        "timestamps": "global (seconds from start of file)",
        "verbatim": "recognized wording preserved exactly as decoded",
        "text": "".join(full_text).strip(),
        "segments": segments,
    }
    json_path = os.path.join(args.output_dir, base + ".json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"[transcribe] wrote: {json_path}", file=sys.stderr)

    md_path = os.path.join(args.output_dir, base + ".md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Transcript — {os.path.basename(args.audio_path)}\n\n")
        f.write("- Model: faster-whisper-small (offline, local)\n")
        f.write(f"- Language: {info.language} (p={info.language_probability:.3f})\n")
        f.write(f"- Duration: {fmt_ts(info.duration)}\n")
        f.write("- Timestamps: global\n")
        f.write("- Verbatim: recognized wording preserved exactly as decoded\n")
        f.write(f"- Speaker diarization: {DIARIZATION_STATUS}\n\n---\n\n")
        for seg in segments:
            f.write(f"**[{fmt_ts(seg['start'])} → {fmt_ts(seg['end'])}]**{seg['text']}\n\n")
    print(f"[transcribe] wrote: {md_path}", file=sys.stderr)
    print("[transcribe] DONE", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
