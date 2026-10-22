#!/usr/bin/env python3
"""Supply-chain integrity tests for candidate external skills; no skill execution."""
import hashlib
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCES = {
 ".agents/skills/webapp-testing/SKILL.md": "4726215301db64a0cc4d41fc3219c61f37a30f4a",
 ".agents/skills/webapp-testing/scripts/with_server.py": "431f2eba16b268b7f3e2ae4daae9db41c0289b6d",
 ".agents/skills/webapp-testing/LICENSE.txt": "4f881c52d1f72f4cfb720e339e2d35c3058d01a9",
 ".agents/skills/diagnosing-bugs/SKILL.md": "d039541ddd1c46e6ddbd662fe99d49b686fc5e12",
 ".agents/skills/diagnosing-bugs/scripts/hitl-loop.template.sh": "243198464a8401a7ba1d63b3708fa43c3d067665",
 ".agents/skills/diagnosing-bugs/LICENSE": "f1dd2c09108dde1a5f56097cee8461b3ea834499",
}
def git_blob_sha(blob: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(blob)).encode() + b"\0" + blob).hexdigest()

def admissible_bytes(path: str, data: bytes) -> bool:
    return git_blob_sha(data) == SOURCES[path]

class ExternalSkillAdmission(unittest.TestCase):
    def test_upstream_blob_integrity(self):
        for path, expected in SOURCES.items():
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file(), path)
                self.assertEqual(git_blob_sha((ROOT / path).read_bytes()), expected)

    def test_negative_fixture_modified_skill_rejected(self):
        path = ".agents/skills/webapp-testing/SKILL.md"
        blob = (ROOT / path).read_bytes()
        self.assertFalse(admissible_bytes(path, blob + b"\n# unauthorized edit\n"))

    def test_skill_identity(self):
        for skill in ("webapp-testing", "diagnosing-bugs"):
            value = (ROOT / ".agents/skills" / skill / "SKILL.md").read_text(encoding="utf-8")
            self.assertRegex(value, rf"\A---\nname:\s*{re.escape(skill)}\s*\n")

    def test_existing_governance(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8").lower()
        self.assertIn("human", agents)
        self.assertIn("two-bridge", agents)

if __name__ == "__main__":
    unittest.main()
