#!/bin/sh
# BOSS offline bundle self-check.
# Verifies: bundled runtime, bundled libraries, bundled model, ffmpeg/ffprobe.
# Makes no changes; exits 0 if the bundle is ready, non-zero otherwise.
set -u

BUNDLE_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
FAIL=0

ok()   { echo "  OK   $1"; }
bad()  { echo "  FAIL $1"; FAIL=1; }

echo "[1/4] Bundled Python runtime"
PY="$BUNDLE_DIR/runtime/python3.12"
if [ -x "$PY" ]; then
  VER="$(LD_LIBRARY_PATH="$BUNDLE_DIR/runtime/libs" "$PY" -S -c 'import sys; print(".".join(map(str, sys.version_info[:3])))' 2>/dev/null)"
  if [ -n "$VER" ]; then ok "python $VER (bundled, no system install)"; else bad "runtime exists but failed to start"; fi
else
  bad "runtime/python3.12 missing or not executable"
fi

echo "[2/4] Bundled libraries (faster-whisper stack)"
LD_LIBRARY_PATH="$BUNDLE_DIR/runtime/libs" \
PYTHONPATH="$BUNDLE_DIR/runtime/lib-python3.12:$BUNDLE_DIR/pylibs" \
PYTHONNOUSERSITE=1 "$PY" -S - <<'EOF' 2>/dev/null && ok "faster-whisper + ctranslate2 + av import cleanly" || bad "library import failed (pylibs incomplete?)"
import faster_whisper, ctranslate2, av, tokenizers, numpy
EOF

echo "[3/4] Bundled Whisper model"
MODEL="$BUNDLE_DIR/models/faster-whisper-small"
M_OK=1
for f in config.json model.bin tokenizer.json vocabulary.txt; do
  [ -s "$MODEL/$f" ] || { bad "models/faster-whisper-small/$f missing"; M_OK=0; }
done
[ "$M_OK" = 1 ] && ok "faster-whisper-small model complete (local, offline)"

echo "[4/4] FFmpeg / FFprobe"
FF="$BUNDLE_DIR/bin/ffmpeg"; FP="$BUNDLE_DIR/bin/ffprobe"
export LD_LIBRARY_PATH="$BUNDLE_DIR/runtime/libs${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
if [ -x "$FF" ] && "$FF" -version >/dev/null 2>&1; then ok "bundled ffmpeg works"
elif command -v ffmpeg >/dev/null 2>&1; then ok "system ffmpeg found (fallback; note: decoding normally uses bundled PyAV anyway)"
else bad "no working ffmpeg (PyAV in pylibs still handles common formats: wav/mp3/m4a/flac/ogg)"
fi
if [ -x "$FP" ] && "$FP" -version >/dev/null 2>&1; then ok "bundled ffprobe works"
elif command -v ffprobe >/dev/null 2>&1; then ok "system ffprobe found (fallback)"
else echo "  WARN ffprobe not available (not required for transcription)"; fi

echo
if [ "$FAIL" = 0 ]; then
  echo "CHECK PASSED - bundle is ready for offline transcription."
  echo "Run:  ./transcribe.sh <audio_path> <output_dir>"
else
  echo "CHECK FAILED - see FAIL lines above; re-extract the archive."
fi
exit "$FAIL"
