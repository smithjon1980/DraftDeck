import json,subprocess,unittest,tempfile,pathlib
from importlib.machinery import SourceFileLoader
m=SourceFileLoader("gate","tools/boss-slide-handoff/validate.py").load_module()
def base():
 return dict(contract="BOSS-SLIDE-HANDOFF-V1",section_id="DAYZERO-STUDIO01",slide_ids=list(range(5,12)),source_sha256="a"*64,source_class="PRIVATE_UNPUBLISHED",source_location_class="PRIVATE_LIBRARY",private_evidence_ref="private:fixture",dispatch_state="HOLD",openbot_mode="enforce",mandatory_gateway_verified=False,audit_fail_closed=False,human_selection="PENDING",human_release="PENDING",publish_state="NOT_PUBLISHED")
class GateTests(unittest.TestCase):
 def test_private_hold(self):self.assertEqual(m.check(base()),[])
 def test_block_unverified_dispatch(self):
  b=base();b["dispatch_state"]="SANDBOX_ONLY";self.assertTrue(m.check(b))
 def test_block_dry_run(self):
  b=base();b.update(dispatch_state="AUTHORIZED",mandatory_gateway_verified=True,audit_fail_closed=True,human_release="APPROVED",openbot_mode="dry-run");self.assertTrue(m.check(b))
 def test_block_fake_release(self):
  b=base();b["publish_state"]="RELEASED";self.assertTrue(m.check(b))
 def test_block_private_public(self):
  b=base();b["source_location_class"]="PUBLIC_REPOSITORY";self.assertTrue(m.check(b))
 def test_block_missing_integrity(self):
  b=base();b["source_sha256"]="not-a-hash";self.assertTrue(m.check(b))
 def test_block_duplicate_slides(self):
  b=base();b["slide_ids"]=[5,5];self.assertTrue(m.check(b))
 def test_human_selected_not_human_released(self):
  b=base();b["human_selection"]="APPROVED";b["publish_state"]="RELEASED";self.assertTrue(m.check(b))
if __name__=="__main__":unittest.main()
