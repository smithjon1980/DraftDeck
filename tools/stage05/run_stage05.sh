#!/usr/bin/env bash
# DraftDeck Stage 05: manual candidate generation and fail-closed packaging.
set -Eeuo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
[[ -n "${HF_TOKEN:-}" ]] || { echo 'HOLD: missing HF_TOKEN' >&2; exit 2; }
command -v go >/dev/null || { echo 'HOLD: Go missing' >&2; exit 2; }
command -v python3 >/dev/null || { echo 'HOLD: Python 3 missing' >&2; exit 2; }
go run main.go
bash ./package_approval_gate2.sh .
