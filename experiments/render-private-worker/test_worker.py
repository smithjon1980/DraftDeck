import hashlib,http.client,hmac,json,os,secrets,threading,time,unittest
from http.server import ThreadingHTTPServer
from unittest.mock import patch
import worker_server as w

KEY = "synthetic-gateway-key-"+"A"*40
class Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.env=patch.dict(os.environ, {w.KEY_NAME:KEY})
  cls.env.start()
  cls.s=ThreadingHTTPServer(("127.0.0.1",0),w.Handler)
  cls.s.daemon_threads=True
  cls.port=cls.s.server_address[1]
  cls.th=threading.Thread(target=cls.s.serve_forever,daemon=True);cls.th.start()
 @classmethod
 def tearDownClass(cls):
  cls.s.shutdown();cls.s.server_close();cls.th.join();cls.env.stop()
 def call(self,path=w.ROUTE,req=None,proof=False,signature=None,method="POST"):
  if req is None:req={"operation":"synthetic_render","fixture":w.FIXTURE_ID,"nonce":secrets.token_hex(20),"issued_at":int(time.time()),"caller":"gateway-test-only"}
  body=w.canonical(req)
  h={"Content-Type":"application/json"}
  if proof:h["X-BOSS-Test-Signature"]=w.expected_sig(req)
  if signature is not None:h["X-BOSS-Test-Signature"]=signature
  c=http.client.HTTPConnection("127.0.0.1",self.port,timeout=70)
  c.request(method,path,body=body if method=="POST" else None,headers=h)
  r=c.getresponse();data=r.read();status=r.status;c.close()
  return status,json.loads(data),req
 def test_health_never_claims_gateway_ready(self):
  s,b,_=self.call(path="/healthz",method="GET")
  self.assertEqual(s,200);self.assertFalse(b["gateway_ready"])
 def test_direct_call_without_proof_denied(self):
  s,b,_=self.call();self.assertEqual(s,403);self.assertEqual(b["status"],"DENIED")
 def test_forged_proof_denied(self):
  self.assertEqual(self.call(signature="0"*64)[0],403)
 def test_expired_intent_denied(self):
  req={"operation":"synthetic_render","fixture":w.FIXTURE_ID,"nonce":secrets.token_hex(20),"issued_at":int(time.time())-300,"caller":"gateway-test-only"}
  self.assertEqual(self.call(req=req,proof=True)[0],403)
 def test_wrong_fixture_denied(self):
  req={"operation":"synthetic_render","fixture":"user-approved.svg","nonce":secrets.token_hex(20),"issued_at":int(time.time()),"caller":"gateway-test-only"}
  self.assertEqual(self.call(req=req,proof=True)[0],403)
 def test_unknown_command_denied(self):
  req={"operation":"execute_shell","fixture":w.FIXTURE_ID,"nonce":secrets.token_hex(20),"issued_at":int(time.time()),"caller":"gateway-test-only"}
  self.assertEqual(self.call(req=req,proof=True)[0],403)
 def test_replay_denied_even_after_valid_signature(self):
  s,b,req=self.call(proof=True)
  self.assertEqual(s,200,str(b))
  self.assertEqual(b["status"],"SYNTHETIC_RENDER_OK")
  self.assertEqual(b["frame_count"],6)
  self.assertEqual(len(b["png_sha256"]),64)
  self.assertEqual(self.call(req=req,proof=True)[0],409)
 def test_wrong_route_denied(self):
  self.assertEqual(self.call(path="/v1/svg/execute",proof=True)[0],404)
 def test_no_secret_refuses_signed_ops(self):
  with patch.dict(os.environ,{w.KEY_NAME:""},clear=False):
   self.assertEqual(self.call(proof=False)[0],403)
 def test_secret_validation(self):
  with patch.dict(os.environ,{w.KEY_NAME:"bad"}),self.assertRaises(RuntimeError):w.key_bytes()
 def test_fixture_contains_six_panels(self):
  self.assertEqual(w.fixture_svg().count('id="PANEL_'),6)
if __name__=="__main__":unittest.main()
