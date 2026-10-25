import os,unittest
from unittest.mock import patch
import gateway_client as c
Q={'action':'metadata_edit','source_sha256':'a'*64,'drawing':'BOSS-CAD-06C','actor_id':'actor','dot_id':'dot','tenant_id':'tenant','work_id':'work','parameters':{'field':'revision','new_value':'B'}}
ENV={'BOSS_OPENBOT_GATEWAY_URL':'https://openbot.invalid','BOSS_APPROVAL_SERVICE_URL':'https://approval.invalid','BOSS_CUSTODY_SERVICE_URL':'https://custody.invalid','BOSS_GATEWAY_WORKLOAD_TOKEN':'x'*32}
class Contract(unittest.TestCase):
 def test_unconfigured_fails(self):
  with patch.dict(os.environ,{},clear=True),self.assertRaises(c.Denied):c.dispatch(Q)
 def test_missing_approval_fails(self):
  e=dict(ENV);del e['BOSS_APPROVAL_SERVICE_URL']
  with patch.dict(os.environ,e,clear=True),self.assertRaises(c.Denied):c.dispatch(Q)
 def test_missing_custody_fails(self):
  e=dict(ENV);del e['BOSS_CUSTODY_SERVICE_URL']
  with patch.dict(os.environ,e,clear=True),self.assertRaises(c.Denied):c.dispatch(Q)
 def test_http_refused(self):
  e=dict(ENV,BOSS_OPENBOT_GATEWAY_URL='http://localhost:3000')
  with patch.dict(os.environ,e,clear=True),self.assertRaises(c.Denied):c.dispatch(Q)
 def test_shell_refused(self):
  with patch.dict(os.environ,ENV,clear=True),self.assertRaises(c.Denied):c.dispatch(dict(Q,action='shell'))
 def test_identity_missing(self):
  q=dict(Q);del q['tenant_id']
  with patch.dict(os.environ,ENV,clear=True),self.assertRaises(c.Denied):c.dispatch(q)
if __name__=='__main__':unittest.main()
