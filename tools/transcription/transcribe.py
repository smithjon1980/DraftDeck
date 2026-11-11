#!/usr/bin/env python3
"""Raw, auditable whisper.cpp ASR candidate generation (not diarization)."""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def run(cmd):
    return subprocess.run([str(x) for x in cmd], check=True, capture_output=True, text=True)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, type=Path)
    p.add_argument("--model", default="base.en")
    p.add_argument("--out-dir", type=Path, required=True)
    args = p.parse_args()
    source = args.input.resolve()
    if not source.is_file():
        sys.exit("SOURCE_NOT_FOUND")
    ffmpeg = shutil.which("ffmpeg")
    ffprobe = shutil.which("ffprobe")
    exe = ROOT / "vendor/whisper.cpp/build/bin/whisper-cli"
    model = ROOT / f"vendor/whisper.cpp/models/ggml-{args.model}.bin"
    if not ffmpeg or not ffprobe:
        sys.exit("FFMPEG_NOT_PRESENT")
    if not exe.is_file():
        sys.exit("ASR_BACKEND_UNAVAILABLE: run bootstrap-whisper.sh")
    if not model.is_file():
        sys.exit("MODEL_NOT_PRESENT: run bootstrap-whisper.sh")
    out = args.out_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)
    wav = out / (source.stem + ".normalized.wav")
    prefix = out / (source.stem + ".asr")
    meta = json.loads(run([ffprobe, "-v", "error", "-show_format", "-of", "json", source]).stdout)
    duration = float(meta["format"]["duration"])
    run([ffmpeg, "-y", "-i", source, "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", wav])
    command = [exe, "-m", model, "-f", wav, "-l", "en", "-otxt", "-osrt", "-of", prefix]
    subprocess.run([str(v) for v in command], check=True)
    txt = Path(str(prefix) + ".txt")
    srt = Path(str(prefix) + ".srt")
    if not txt.is_file() or not srt.is_file() or not txt.read_text(encoding="utf-8").strip():
        sys.exit("ASR_OUTPUT_INVALID")
    digest = hashlib.file_digest(source.open("rb"), "sha256").hexdigest()
    rev = ROOT / "WHISPER_UPSTREAM_COMMIT"
    receipt = {
        "source": str(source), "sha256": digest, "duration_seconds": duration,
        "upstream_commit": rev.read_text().strip() if rev.is_file() else "NOT_ESTABLISHED",
        "model": str(model), "engine": str(exe),
        "raw_text": str(txt), "timestamped_srt": str(srt),
        "diarization": "NOT_ESTABLISHED",
        "content_verification": "HOLD",
        "command": [str(x) for x in command],
    }
    (out / (source.stem + ".asr-receipt.json")).write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))

if __name__ == "__main__":
    main()
