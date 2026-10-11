#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REF="${1:-v1.8.2}"
MODEL="${2:-base.en}"
DEST="$ROOT/vendor/whisper.cpp"
for tool in git cmake ffmpeg; do
  command -v "$tool" >/dev/null || { echo "MISSING_DEPENDENCY: $tool" >&2; exit 2; }
done
if [[ ! "$MODEL" =~ ^(tiny|base|small|medium)(\.en)?$|^large-(v1|v2|v3|v3-turbo)$ ]]; then
  echo "UNSUPPORTED_MODEL: $MODEL" >&2
  exit 2
fi
if [[ ! -d "$DEST/.git" ]]; then
  mkdir -p "$(dirname "$DEST")"
  git clone https://github.com/ggml-org/whisper.cpp.git "$DEST"
fi
git -C "$DEST" fetch --tags origin
git -C "$DEST" checkout --detach "$REF"
git -C "$DEST" rev-parse HEAD | tee "$ROOT/WHISPER_UPSTREAM_COMMIT"
cmake -S "$DEST" -B "$DEST/build" -DCMAKE_BUILD_TYPE=Release
cmake --build "$DEST/build" --config Release -j 2
bash "$DEST/models/download-ggml-model.sh" "$MODEL"
[[ -s "$DEST/models/ggml-$MODEL.bin" ]] || { echo "MODEL_NOT_PRESENT" >&2; exit 3; }
"$DEST/build/bin/whisper-cli" --help >/dev/null 2>&1 || true
echo "Whisper bootstrap complete. Version evidence in WHISPER_UPSTREAM_COMMIT."
