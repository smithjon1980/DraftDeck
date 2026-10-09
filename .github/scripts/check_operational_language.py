"""Check tracked copy and source for common violations of operational language."""

from pathlib import Path
import re
import subprocess


SUFFIXES = {".md", ".markdown", ".py", ".html", ".htm", ".css"}
META_FILES = {
    ".github/scripts/check_operational_language.py",
    ".github/scripts/test_operational_language.py",
}
CONTRACT_FILES = {
    "design-system/editorial-components.md",
    "skills/draftdeck/references/editorial-components.md",
}
# Exact policy examples only; the remainder of each contract is protected.
COMPARISON_ROWS = {
    '| “The AI hallucinated.” | “The output contains an unsupported claim.” |',
    '| “The AI brain.” | “The model” or “processing system.” |',
    '| “The AI understood the assignment.” | “The output satisfied the stated requirements.” |',
    '| “The AI decided to release it.” | “The system applied a release rule,” or “the authorized person approved release.” |',
}
PATTERNS = (
    ("unsupported-output euphemism", re.compile(r"\bhallucinat\w*", re.I)),
    ("human anatomy", re.compile(r"\bai(?:['’]s)?[\s-]+brain\b", re.I)),
    (
        "human mental state or agency",
        re.compile(
            r"\b(?:the\s+)?(?:ai|model)\s+"
            r"(?:wants?|wanted|understands?|understood|knows?|knew|"
            r"decides?|decided|thinks?|thought|believes?|believed|"
            r"intends?|intended)\b",
            re.I,
        ),
    ),
)


def findings(path: str, text: str) -> list[tuple[int, str, str]]:
    """Return line, rule and phrase; preserve offsets while masking policy rows."""
    if path in META_FILES:
        return []
    lines = text.splitlines(keepends=True)
    if path in CONTRACT_FILES:
        lines = [
            re.sub(r"[^\r\n]", " ", line)
            if line.strip() in COMPARISON_ROWS else line
            for line in lines
        ]
    protected = "".join(lines)
    # Formatting must not hide a phrase. Keep offsets/newlines for diagnostics.
    markup = r"</?[a-zA-Z][^>]*>|[*`]" if Path(path).suffix.lower() in {
        ".md", ".markdown", ".html", ".htm"
    } else r"[*`]"
    protected = re.sub(
        markup,
        lambda match: re.sub(r"[^\r\n]", " ", match.group()),
        protected,
    )
    result = []
    for rule, pattern in PATTERNS:
        for match in pattern.finditer(protected):
            line = protected.count("\n", 0, match.start()) + 1
            result.append((line, rule, " ".join(match.group().split())))
    return sorted(result)


def main() -> int:
    root = Path(subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], text=True
    ).strip())
    paths = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=root
    ).decode().split("\0")
    failed = False
    checked = 0
    for path in paths:
        if not path or Path(path).suffix.lower() not in SUFFIXES or path in META_FILES:
            continue
        checked += 1
        for line, rule, phrase in findings(path, (root / path).read_text(encoding="utf-8")):
            # Avoid printing whole HTML/Python lines that may contain image data.
            print(f"{path}:{line}: {rule}: {phrase}")
            failed = True
    if failed:
        print("Operational language guard failed. Describe the operation, evidence, and accountable human.")
        return 1
    print(f"Operational language guard passed: {checked} tracked text files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
