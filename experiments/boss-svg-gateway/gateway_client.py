"""Intent-only gateway client, fail closed; NOT a live OpenBot connection."""
import hashlib,json,os,ssl,urllib.parse,urllib.request
class Denied(Exception):pass
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':')).encode()
def service(name):
 u=urllib.parse.urlparse(os.getenv(name,''))
 if u.scheme!='https' or not u.netloc or u.username or u.password or u.fragment or u.query:raise Denied('SERVICE_MISSING:'+name)
 return u.geturl().rstrip('/')
def dispatch(request):
 keys={'action','source_sha256','drawing','actor_id','dot_id','tenant_id','work_id','parameters'}
 if set(request)!=keys or request['action'] not in ('inspect','export_png','export_pdf','metadata_edit'):raise Denied('BAD_REQUEST')
 if any(not isinstance(request[k],str) or not request[k].strip() for k in keys-{'action','parameters'}):raise Denied('IDENTITY_REQUIRED')
 if not isinstance(request['parameters'],dict):raise Denied('INVALID_PARAMETERS')
 gateway=service('BOSS_OPENBOT_GATEWAY_URL')
 service('BOSS_APPROVAL_SERVICE_URL');service('BOSS_CUSTODY_SERVICE_URL')
 token=os.getenv('BOSS_GATEWAY_WORKLOAD_TOKEN','')
 if len(token)<24:raise Denied('NO_WORKLOAD_IDENTITY')
 class NoRedirect(urllib.request.HTTPRedirectHandler):
  def redirect_request(self,*a):raise Denied('REDIRECT_REFUSED')
 dest=gateway+'/v1/svg/dispatch'
 req=urllib.request.Request(dest,canonical(request),headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'},method='POST')
 opener=urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl.create_default_context()),NoRedirect())
 try:
  with opener.open(req,timeout=8) as resp:
   if resp.url!=dest:raise Denied('REDIRECT_REFUSED')
   raw=resp.read(262145)
   if len(raw)>262144:raise Denied('RESPONSE_TOO_LARGE')
   result=json.loads(raw)
 except Exception as exc:raise Denied('REMOTE_GATEWAY_UNAVAILABLE') from exc
 if not isinstance(result,dict) or result.get('contract')!='BOSS-SVG-GOVERNED-V1':raise Denied('INVALID_CONTRACT')
 if result.get('request_sha256')!=hashlib.sha256(canonical(request)).hexdigest():raise Denied('WRONG_OPERATION')
 if result.get('status') not in ('DENIED','PENDING_HUMAN','COMPLETED'):raise Denied('INVALID_STATUS')
 if result['status']=='COMPLETED' and not all(result.get(k) for k in ('gateway_decision_id','custody_receipt_id','output_sha256')):raise Denied('CUSTODY_MISSING')
 return result
