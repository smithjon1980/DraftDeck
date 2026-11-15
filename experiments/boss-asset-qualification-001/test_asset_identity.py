"""BOSS synthetic asset identity qualification; no production assets or network access."""
import hashlib
import unittest

APPROVED_REVISION = "129a3e0849d87df98289087262ade051073e791f"
PARAGRAPH = "BOSS.EP00.A01.S01.P001"
EXPECTED_IMAGE = b"synthetic-single-illustration-fixture-v1"
ASSET_ID = "BOSS.EP00.A01.S01.P001.ILLUSTRATION.001"
MANIFEST = {
    "paragraph_id": PARAGRAPH,
    "manuscript_commit": APPROVED_REVISION,
    "asset_id": ASSET_ID,
    "asset_type": "single_illustration",
    "sha256": hashlib.sha256(EXPECTED_IMAGE).hexdigest(),
    "approval_status": "approved",
}

def inspect(manifest, candidate, payload):
    checks = {
        "paragraph_id": candidate.get("paragraph_id") == manifest["paragraph_id"],
        "manuscript_commit": candidate.get("manuscript_commit") == manifest["manuscript_commit"],
        "asset_id": candidate.get("asset_id") == manifest["asset_id"],
        "asset_type": candidate.get("asset_type") == manifest["asset_type"],
        "sha256": hashlib.sha256(payload).hexdigest() == manifest["sha256"],
        "approval_status": candidate.get("approval_status") == manifest["approval_status"],
    }
    return ("PASS" if all(checks.values()) else "REJECT", checks)

class TestSyntheticAssetQualification(unittest.TestCase):
    def candidate(self, **changes):
        return {**MANIFEST, **changes}

    def test_exact_registered_asset_passes(self):
        self.assertEqual(inspect(MANIFEST, self.candidate(), EXPECTED_IMAGE)[0], "PASS")

    def test_collage_substitution_rejected(self):
        status, checks = inspect(MANIFEST, self.candidate(asset_type="storyboard_collage",
            asset_id="STORYBOARD.MONTAGE.001"), b"synthetic-collage")
        self.assertEqual(status, "REJECT")
        self.assertFalse(checks["asset_type"])

    def test_wrong_revision_rejected(self):
        self.assertEqual(inspect(MANIFEST, self.candidate(manuscript_commit="unauthorized"), EXPECTED_IMAGE)[0], "REJECT")

    def test_altered_payload_rejected(self):
        status, checks = inspect(MANIFEST, self.candidate(), b"tampered")
        self.assertEqual(status, "REJECT")
        self.assertFalse(checks["sha256"])

    def test_unapproved_artwork_rejected(self):
        self.assertEqual(inspect(MANIFEST, self.candidate(approval_status="WIP"), EXPECTED_IMAGE)[0], "REJECT")

if __name__ == "__main__":
    unittest.main(verbosity=2)
