#!/usr/bin/env python3
"""Guard HAVE terminology and manuscript custody. Not visual or release verification."""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANONICAL = "HAVE — Human Authority, Verified Execution"
NOTICE = "doctrine/human-authority-verified-evidence.md"

def main():
    errors = []
    for path in ("AGENTS.md", "README.md", "doctrine/README.md", NOTICE):
        if CANONICAL not in (ROOT / path).read_text(encoding="utf-8"):
            errors.append(f"{path}: canonical HAVE wording missing")
    manuscript = (ROOT / "manuscripts/day-zero/CANDIDATE-006-100-paragraphs.txt").read_text(encoding="utf-8")
    labels = [int(m.group(1)) for m in re.finditer(r"(?m)^(\d{3})\.\s", manuscript)]
    if labels != list(range(1, 101)):
        errors.append("Day Zero manuscript paragraph sequence must remain 001–100")
    if "HAVE — Human Authority, Verified Execution — is not a slogan" not in manuscript:
        errors.append("Authorized paragraph 100 wording missing")
    record = (ROOT / "governance/approvals/APPROVED-EDITORIAL-006.md").read_text(encoding="utf-8")
    if "2026-11-14" not in record or CANONICAL not in record:
        errors.append("Approval record missing dated HAVE amendment")
    process = subprocess.run(["git", "grep", "-n", "-i", "-E", r"humans[ -]in[ -]the[ -]lead", "--", "."],
                             cwd=ROOT, capture_output=True, text=True)
    if process.returncode not in (0, 1):
        errors.append("git grep failed: " + process.stderr)
    for line in process.stdout.splitlines():
        path = line.split(":", 1)[0]
        if path != NOTICE:
            errors.append(f"Retired branding in tracked file: {path}")
    if "DO NOT USE" not in (ROOT / NOTICE).read_text(encoding="utf-8"):
        errors.append("Retired-brand history notice missing")
    if errors:
        print("HAVE_CONTRACT_HOLD")
        print("\n".join(errors))
        return 1
    print("HAVE_TEXT_AND_CUSTODY_PASS; visual fidelity and publication NOT TESTED")
    return 0

if __name__ == "__main__":
    sys.exit(main())
