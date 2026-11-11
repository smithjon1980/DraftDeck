#!/usr/bin/env bash
# DraftDeck Creative Composer — Stage 05 -> Approval Gate 2
# Usage: ./package_approval_gate2.sh [directory-containing-candidates]
# Requirements: bash, Python 3 (standard library only)
set -Eeuo pipefail

if [[ $# -gt 1 ]]; then
  printf 'Usage: %s [candidate-directory]\n' "${0##*/}" >&2
  exit 2
fi
if ! command -v python3 >/dev/null 2>&1; then
  echo 'ERROR: python3 is required for manifest, PNG, checksum, and ZIP validation.' >&2
  exit 2
fi

candidate_dir="${1:-.}"

python3 - "$candidate_dir" <<'PY'
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import struct
import sys
from zipfile import ZipFile, ZIP_DEFLATED

PREFIX = "SCC-02-SLIDE05"
MODEL = "black-forest-labs/FLUX.1-dev"
PROVIDER = "fal-ai"
WIDTH, HEIGHT = 1536, 864  # Exact 16:9; both dimensions divisible by 32
FILE_NAMES = [f"{PREFIX}-stage05-candidate-{i:02d}.png" for i in range(1, 4)]
MANIFEST_NAME = f"{PREFIX}-stage05-manifest.json"
ARCHIVE_NAME = f"{PREFIX}-Approval-Gate-2.zip"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def reject(reason):
    print("STAGE 05 PACKAGE: HOLD — " + reason, file=sys.stderr)
    raise SystemExit(1)


def require(condition, reason):
    if not condition:
        reject(reason)


def sha256_file(path):
    with path.open("rb") as fp:
        digest = hashlib.sha256()
        for chunk in iter(lambda: fp.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_utc_timestamp(value, label):
    require(isinstance(value, str) and bool(value), f"missing {label}")
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        reject(f"invalid {label}: {value!r}")
    require(parsed.tzinfo is not None, f"{label} needs an explicit UTC offset")
    return parsed


def png_dimensions(path):
    with path.open("rb") as fp:
        header = fp.read(24)
    require(len(header) == 24 and header[:8] == PNG_SIGNATURE,
            f"{path.name} is not a PNG file")
    require(header[12:16] == b"IHDR" and struct.unpack(">I", header[8:12])[0] == 13,
            f"{path.name} has an invalid PNG IHDR header")
    return struct.unpack(">II", header[16:24])


source_dir = Path(sys.argv[1]).expanduser().resolve()
require(source_dir.is_dir(), f"candidate directory not found: {source_dir}")
manifest_path = source_dir / MANIFEST_NAME
require(manifest_path.is_file(), f"manifest not found: {manifest_path}")
try:
    with manifest_path.open("r", encoding="utf-8") as fp:
        manifest = json.load(fp)
except (json.JSONDecodeError, UnicodeError, OSError) as exc:
    reject(f"manifest is unreadable: {exc}")

require(manifest.get("schema_version") == "1.0", "unsupported manifest schema version")
require(manifest.get("contract_id") == PREFIX, "contract_id mismatch")
require(str(manifest.get("stage")) == "05", "stage must equal 05")
require(manifest.get("status") == "COMPLETED_WITH_CANDIDATES",
        "manifest is not marked COMPLETED_WITH_CANDIDATES")
require(manifest.get("model") == MODEL and manifest.get("provider") == PROVIDER,
        "model or provider mismatch")
require(manifest.get("output_format") == "png", "output_format must be png")
require(manifest.get("candidate_count") == 3, "candidate_count must be 3")
require(isinstance(manifest.get("prompt"), str) and manifest["prompt"].strip(),
        "locked prompt missing")
require(isinstance(manifest.get("negative_prompt"), str) and manifest["negative_prompt"].strip(),
        "negative prompt missing")
parse_utc_timestamp(manifest.get("generated_at_utc"), "generated_at_utc")

params = manifest.get("common_parameters")
require(isinstance(params, dict), "common_parameters missing")
require(params.get("width") == WIDTH and params.get("height") == HEIGHT,
        f"generator dimensions must be {WIDTH}x{HEIGHT} (exact 16:9)")
require(params.get("negative_prompt") == manifest["negative_prompt"],
        "common_parameters.negative_prompt does not match locked negative_prompt")
base_seed = manifest.get("base_seed")
require(type(base_seed) is int and base_seed >= 0, "base_seed missing/invalid")

candidates = manifest.get("candidates")
require(isinstance(candidates, list) and len(candidates) == 3,
        "exactly 3 candidate records required")

for index, record in enumerate(candidates, start=1):
    expected_name = FILE_NAMES[index - 1]
    expected_seed = base_seed + index - 1
    require(isinstance(record, dict), f"candidate {index}: invalid record")
    require(record.get("index") == index, f"candidate {index}: index mismatch")
    require(record.get("file_name") == expected_name,
            f"candidate {index}: filename mismatch; expected {expected_name}")
    require(record.get("seed") == expected_seed,
            f"candidate {index}: seed must equal {expected_seed}")
    require(record.get("status") == "OK", f"candidate {index}: status is not OK")
    require(type(record.get("http_status")) is int and 200 <= record["http_status"] <= 299,
            f"candidate {index}: no successful HTTP result")
    require(str(record.get("content_type", "")).split(";", 1)[0].strip().lower() == "image/png",
            f"candidate {index}: response was not image/png")
    parse_utc_timestamp(record.get("request_timestamp"), f"candidate {index} request_timestamp")
    parse_utc_timestamp(record.get("response_timestamp"), f"candidate {index} response_timestamp")
    request_params = record.get("request_parameters")
    require(isinstance(request_params, dict), f"candidate {index}: request parameters missing")
    require(request_params.get("seed") == expected_seed,
            f"candidate {index}: request seed mismatch")
    require(request_params.get("width") == WIDTH and request_params.get("height") == HEIGHT,
            f"candidate {index}: request dimensions mismatch")
    for key in ("guidance_scale", "num_inference_steps"):
        require(request_params.get(key) == params.get(key),
                f"candidate {index}: inconsistent {key}")

    image_path = source_dir / expected_name
    require(image_path.is_file(), f"missing image: {image_path}")
    pixel_size = png_dimensions(image_path)
    require(pixel_size == (WIDTH, HEIGHT),
            f"{expected_name}: actual PNG is {pixel_size}, not {WIDTH}x{HEIGHT}")
    actual_size = image_path.stat().st_size
    require(actual_size == record.get("size_bytes"),
            f"{expected_name}: file length does not match manifest")
    actual_hash = sha256_file(image_path)
    require(actual_hash == record.get("sha256", "").lower(),
            f"{expected_name}: SHA-256 mismatch")
    print(f"VALIDATED candidate {index:02d}: seed={expected_seed}, sha256={actual_hash[:16]}…")

archive_path = source_dir / ARCHIVE_NAME
require(not archive_path.exists(),
        f"archive already exists; preserve previous evidence or remove it intentionally: {archive_path}")
temp_path = source_dir / ("." + ARCHIVE_NAME + ".tmp")
require(not temp_path.exists(), f"temporary ZIP already exists: {temp_path}")
try:
    with ZipFile(temp_path, "w", compression=ZIP_DEFLATED, compresslevel=6) as bundle:
        for name in FILE_NAMES:
            bundle.write(source_dir / name, arcname=name)
        bundle.write(manifest_path, arcname=MANIFEST_NAME)
    with ZipFile(temp_path, "r") as bundle:
        expected_members = FILE_NAMES + [MANIFEST_NAME]
        require(bundle.namelist() == expected_members,
                "archive contains unexpected files or missing evidence")
        require(bundle.testzip() is None, "archive failed CRC verification")
    os.replace(temp_path, archive_path)
except BaseException:
    if temp_path.exists():
        temp_path.unlink()
    raise

print(f"\nSTAGED: {archive_path}")
print(f"ARCHIVE_SHA256: {sha256_file(archive_path)}")
print("APPROVAL GATE 2: HOLD — awaiting independent visual inspection and candidate selection")
print("STAGE 06 / FINAL RELEASE: NOT AUTHORIZED")
PY