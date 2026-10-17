#!/usr/bin/env python3
"""Acquire the exact OpenCode source identified in upstream.json."""
from pathlib import Path
import json, re, subprocess

root = Path(__file__).resolve().parent
lock = json.loads((root / "upstream.json").read_text())
commit = lock["commit"]
if not re.fullmatch(r"[0-9a-f]{40}", commit):
    raise SystemExit("Invalid pinned commit")
source = root / "upstream"

def git(*args):
    return subprocess.check_output(["git", "-C", str(source), *args], text=True).strip()

if not source.exists():
    subprocess.run(["git", "clone", "--no-checkout", "--filter=blob:none", lock["repository"], str(source)], check=True)
if git("remote", "get-url", "origin") != lock["repository"]:
    raise SystemExit("Existing checkout has a different origin; preserve it and inspect manually")
# A fresh --no-checkout clone has no worktree yet, so check dirt only after population.
if (source / "LICENSE").exists() and git("status", "--porcelain"):
    raise SystemExit("Existing checkout contains changes; preserve them before switching commits")
if subprocess.run(["git", "-C", str(source), "cat-file", "-e", commit + "^{commit}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode:
    subprocess.run(["git", "-C", str(source), "fetch", "--depth", "1", "origin", commit], check=True)
subprocess.run(["git", "-C", str(source), "checkout", "--detach", commit], check=True)
if git("rev-parse", "HEAD") != commit:
    raise SystemExit("Checkout identity differs")
if "MIT License" not in (source / "LICENSE").read_text():
    raise SystemExit("Expected license notice missing; inspect upstream")
print("Verified OpenCode source:", commit)
print("Source checkout:", source)
print("Build and account authentication remain separate checks.")
