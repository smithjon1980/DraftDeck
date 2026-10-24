import json,unittest,importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location("gate","tools/precomposition-gate/check.py");m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def base():
 x=dict(contract="BOSS-PRECOMPOSE-V1",stage="PRECOMPOSITION",slide_id="D0-05",section_id="STUDIO01",art_id="ART-C1",story_id="STORY-C1",art_sha256="a"*64,story_sha256="b"*64,composition_target="D0-05-1920x1080",approval_verified_by_trusted_service=False,production_release_authorized=False,approvals=[])
 return x
class Test(unittest.TestCase):
 def test_pending_denied(self):self.assertTrue(m.check(base()))
 def test_fake_approved_without_attestation_denied(self):
  x=base()
  for layer,cid,sha in [("ART","ART-C1","a"*64),("STORY","STORY-C1","b"*64)]:
   x["approvals"].append(dict(layer=layer,candidate_id=cid,source_sha256=sha,slide_id="D0-05",section_id="STUDIO01",composition_target="D0-05-1920x1080",decision="APPROVED",reviewer_kind="HUMAN",reviewer_id="owner",preview_sha256="c"*64,evidence_ref="private:ledger/123"))
  self.assertTrue(m.check(x))
 def test_changed_hash_denied(self):
  x=base();x["art_sha256"]="invalid";self.assertTrue(m.check(x))
 def test_release_denied(self):
  x=base();x["production_release_authorized"]=True;self.assertTrue(m.check(x))
 def test_no_model_approval(self):
  x=base();x["approvals"]=[dict(layer="ART",reviewer_kind="AGENT")];self.assertTrue(m.check(x))
if __name__=="__main__":unittest.main()
