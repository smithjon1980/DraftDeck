"""Untrusted Render peer canary. No secret and no caller-specified proxy target."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json, os, urllib.request, urllib.error, urllib.parse
from urllib.request import Request

def probe():
    origin=os.environ.get("BOSS_PRIVATE_WORKER_URL","").rstrip("/")
    u=urllib.parse.urlparse(origin)
    if u.scheme!="http" or not u.hostname or u.username or u.password or u.path or u.query or u.fragment:
        return {"mode":"untrusted","status":"UNCONFIGURED"}
    try:
        with urllib.request.urlopen(origin+"/healthz",timeout=4) as r:
            alive=r.status==200
    except Exception:
        return {"mode":"untrusted","status":"UNREACHABLE","network_reachable":False}
    payload=b'{"operation":"synthetic_render","fixture":"BOSS-SYNTHETIC-SIX-FRAME"}'
    req=Request(origin+"/v1/qualification/render",data=payload,headers={"Content-Type":"application/json"},method="POST")
    try:
        with urllib.request.urlopen(req,timeout=4) as r:
            status=r.status
    except urllib.error.HTTPError as e:
        status=e.code
    except Exception:
        return {"mode":"untrusted","status":"ERROR","network_reachable":alive}
    return {"mode":"untrusted","status":"DENIED" if status in (403,413) else "UNEXPECTED","network_reachable":alive,
            "unsigned_svg_operation_http_status":status,"protected_operation_refused":status in (403,413)}

class Handler(BaseHTTPRequestHandler):
    def log_message(self,*_):pass
    def do_GET(self):
        if self.path=="/healthz":
            status,data=200,{"service":"boss-render-untrusted-canary","mode":"test-only"}
        elif self.path=="/probe":
            status,data=200,probe()
        else:
            status,data=404,{"status":"NOT_FOUND"}
        raw=json.dumps(data,sort_keys=True,separators=(",",":")).encode()
        self.send_response(status)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(raw)))
        self.send_header("Cache-Control","no-store")
        self.end_headers()
        self.wfile.write(raw)

def serve():
    p=int(os.environ.get("PORT","10000"))
    ThreadingHTTPServer(("0.0.0.0",p),Handler).serve_forever()
if __name__=="__main__":
    serve()
