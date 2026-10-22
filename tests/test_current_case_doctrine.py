#!/usr/bin/env python3
"""Public-safe regression checks for current BOSS art/story doctrine.

Checks repository instructions only. Never imports private Episode 01 scripts.
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = [
    "skills/draftdeck/SKILL.md",
    ".agents/skills/boss-story-architect/SKILL.md",
    ".agents/skills/boss-visual-storyboard/SKILL.md",
    ".agents/skills/boss-art-asset-producer/SKILL.md",
    ".agents/skills/boss-art-story-reviewer/SKILL.md",
]

class CurrentCaseTests(unittest.TestCase):
    def test_current_contract_supports_document_shipping_case(self):
        d=json.loads((ROOT/"design-system/boss-design-contract.json").read_text())
        self.assertEqual(d["current_reference_case"]["name"], "Main Street Copy")
        self.assertEqual(d["authority"]["narration_revision"].split(";")[0], "AUTHORIZED_TO_DRAFT_V4")
        self.assertEqual(d["authority"]["art_technical_plan"], "OWNER_ACCEPTED_2026-10-22")
        self.assertIn("UPS Ground",d["current_reference_case"]["carrier_examples"])
        self.assertIn("FedEx Ground",d["current_reference_case"]["carrier_examples"])
        self.assertEqual(d["current_reference_case"]["carrier_selection"],"alternatives_not_simultaneous")
        self.assertIn("parcel",d["rules"]["metaphors"].lower())
        self.assertIn("HUMAN",d["authority"]["final_visual_approval"].upper())

    def test_skills_use_main_street_copy_not_old_market(self):
        for path in SKILLS:
            with self.subTest(path=path):
                s=(ROOT/path).read_text()
                self.assertIn("Main Street Copy",s)
                self.assertNotIn("Market Seven",s)

    def test_revised_transcript_does_not_inherit_old_audio_approval(self):
        s=(ROOT/"AGENTS.md").read_text()
        self.assertIn("V4",s)
        self.assertIn("fresh author read-through/hash lock",s)
        self.assertIn("not",s.lower())
        self.assertIn("private",s.lower())
        self.assertIn("not", (ROOT/"doctrine/main-street-copy-case-model.md").read_text().lower())

    def test_distinguish_carrier_label_custody_and_delivery(self):
        s=(ROOT/"doctrine/main-street-copy-case-model.md").read_text().lower()
        for word in ("label", "custody", "delivery","ups ground","fedex ground","prime","parcels"):
            self.assertIn(word,s)
        self.assertIn("not",s)

    def test_contract_requires_native_text_and_white_ground(self):
        d=json.loads((ROOT/"design-system/boss-design-contract.json").read_text())
        self.assertEqual(d["brand"]["ground"],"#FFFFFF")
        self.assertIn("native HTML",d["rules"]["editable_editorial_text"])
        self.assertIn("technical editorial illustration",d["rules"]["story_medium"])

if __name__ == "__main__":
    unittest.main()
