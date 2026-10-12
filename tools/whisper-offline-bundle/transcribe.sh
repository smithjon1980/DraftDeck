#!/bin/sh
# BOSS offline transcription launcher.
# Uses only the bundled runtime, bundled libraries, and bundled model.
# No system installation, no administrator access, no internet access.
set -eu

BUNDLE_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"

export LD_LIBRARY_PATH="$BUNDLE_DIR/runtime/libs${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export PYTHONPATH="$BUNDLE_DIR/runtime/lib-python3.12:$BUNDLE_DIR/pylibs"
export PYTHONNOUSERSITE=1
export PYTHONDONTWRITEBYTECODE=1
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export PATH="$BUNDLE_DIR/bin:$PATH"

PY="$BUNDLE_DIR/runtime/python3.12"
if [ ! -x "$PY" ]; then
  echo "ERROR: bundled Python runtime not found at $PY" >&2
  echo "Re-extract the archive preserving file structure." >&2
  exit 2
fi

if [ "$#" -lt 2 ]; then
  echo "Usage: ./transcribe.sh <audio_path> <output_dir> [--language en] [--beam-size 5]" >&2
  exit 1
fi

# -S: skip 'site' (no system site-packages); PYTHONPATH above supplies everything.
exec "$PY" -S "$BUNDLE_DIR/transcribe.py" "$@"
