"""Adversarial qualification against the actual merged checker. No approvals minted."""
import unittest,importlib.util,copy
spec=importlib.util.spec_from_file_location("gate","tools/precomposition-gate/check.py")
gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)
def base():
 x={"contract":"BOSS-PRECOMPOSE-V1","stage":"PRECOMPOSITION","slide_id":"D0-05","section_id":"STUDIO01","art_id":"ART-1","story_id":"STORY-1","art_sha256":"a"*64,"story_sha256":"b"*64,"composition_target":"D0-05-1920x1080","approval_verified_by_trusted_service":False,"production_release_authorized":False,"approvals":[]}
 for layer,cid,h in (("ART","ART-1","a"*64),("STORY","STORY-1","b"*64)):
  x["approvals"].append({"layer":layer,"candidate_id":cid,"source_sha256":h,"slide_id":"D0-05","section_id":"STUDIO01","composition_target":"D0-05-1920x1080","decision":"APPROVED","reviewer_kind":"HUMAN","reviewer_id":"claimed-owner","evidence_ref":"private:claimed","preview_sha256":"c"*64})
 return x
class Qualification(unittest.TestCase):
 def test_missing_evidence_is_denied(self):
  x=base();x["approvals"]=[];self.assertTrue(gate.check(x))
 def test_pending_human_verification_is_denied(self):self.assertTrue(gate.check(base()))
 def test_rejected_art_denied(self):
  x=base();x["approval_verified_by_trusted_service"]=True;x["approvals"][0]["decision"]="REJECTED";self.assertTrue(gate.check(x))
 def test_modified_art_bytes_denied(self):
  x=base();x["approval_verified_by_trusted_service"]=True;x["art_sha256"]="d"*64;self.assertTrue(gate.check(x))
 def test_modified_story_bytes_denied(self):
  x=base();x["approval_verified_by_trusted_service"]=True;x["story_sha256"]="d"*64;self.assertTrue(gate.check(x))
 def test_wrong_slide_denied(self):
  x=base();x["approval_verified_by_trusted_service"]=True;x["slide_id"]="D0-06";self.assertTrue(gate.check(x))
 def test_self_approval_label_denied(self):
  x=base();x["approval_verified_by_trusted_service"]=True;x["approvals"][0]["reviewer_kind"]="AGENT";self.assertTrue(gate.check(x))
 def test_unapproved_release_denied(self):
  x=base();x["approval_verified_by_trusted_service"]=True;x["production_release_authorized"]=True;self.assertTrue(gate.check(x))
 def test_negative_control_manifest_can_forge_trusted_boolean(self):
  x=base();x["approval_verified_by_trusted_service"]=True
  # EXPECTED VULNERABILITY: claimed human metadata and a JSON boolean suffice for eligibility.
  # This is not a successful authorization. Any PASS here confirms external enforcement is mandatory.
  self.assertEqual(gate.check(x),[],"Unexpected: checker no longer accepts forged attestation; revisit negative control")
if __name__=="__main__":unittest.main()
