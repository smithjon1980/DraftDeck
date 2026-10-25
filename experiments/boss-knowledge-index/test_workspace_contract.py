import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent

class PersonalWorkspaceBoundaryCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = json.loads((ROOT / "workspace_contract.json").read_text(encoding="utf-8"))

    def test_private_workspace_separate(self):
        self.assertEqual(cls_store := self.policy["private_workspace"]["storage"], "separate_private_local_space")
        self.assertEqual(self.policy["private_workspace"]["test_data"], "fictional_only")

    def test_unreviewed_content_cannot_auto_publish(self):
        self.assertIs(self.policy["private_workspace"]["automatic_public_git_sync"], False)
        self.assertIs(self.policy["admission"]["automated_promotion"], False)
        self.assertEqual(self.policy["admission"]["required_gates"],
                         ["classification","redaction","source_trace","human_selection","pr_review"])

    def test_read_only_no_live_connector(self):
        self.assertEqual(self.policy["retrieval"]["default"], "read_only")
        self.assertIs(self.policy["retrieval"]["private_note_ingestion"], False)
        self.assertIs(self.policy["retrieval"]["chatgpt_connector_active"], False)
        self.assertIs(self.policy["retrieval"]["production_write_authorized"], False)

    def test_no_unapproved_release(self):
        self.assertIs(self.policy["private_workspace"]["deployment_authorized"], False)
        self.assertIs(self.policy["publication"]["conversation_transcript_publication_authorized"], False)
        self.assertIs(self.policy["publication"]["private_manuscript_publication_authorized"], False)

if __name__ == "__main__":
    unittest.main()
