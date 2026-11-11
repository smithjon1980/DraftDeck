"""INERT six-frame Inkscape qualification worker. No user asset input; not a production SVG adapter."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import hashlib, hmac, json, os, secrets, shutil, subprocess, tempfile, threading, time
from pathlib import Path

PORT_DEFAULT = "10000"
ROUTE = "/v1/qualification/render"
KEY_NAME = "BOSS_SYNTHETIC_GATEWAY_KEY"
FIXTURE_ID = "BOSS-SYNTHETIC-SIX-FRAME"
NONCES = set()
LOCK = threading.Lock()
MAX_BODY = 2048

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()

def key_bytes():
    raw = os.environ.get(KEY_NAME, "")
    if len(raw) < 32:
        raise RuntimeError("A unique test-only secret >=32 characters is required")
    return raw.encode()

def expected_sig(body, secret=None):
    return hmac.new(secret or key_bytes(), b"POST\n" + ROUTE.encode() + b"\n" + canonical(body), hashlib.sha256).hexdigest()

def fixture_svg():
    items = []
    for n in range(6):
        x = 90 + (n % 3) * 580
        y = 150 + (n // 3) * 390
        items.append(f'<g id="PANEL_{n+1:02}"><rect x="{x}" y="{y}" width="520" height="330" fill="none" stroke="#111827" stroke-width="3"/></g>')
    return '<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><rect width="1920" height="1080" fill="white"/>' + "".join(items) + "</svg>"

def native_render():
    if shutil.which("inkscape") is None:
        raise RuntimeError("Real Inkscape executable is required")
    with tempfile.TemporaryDirectory(prefix="boss-render-synthetic-") as d:
        svg, png = Path(d)/"fixture.svg", Path(d)/"render.png"
        svg.write_text(fixture_svg(), encoding="utf-8")
        subprocess.run(["inkscape", str(svg), "--export-filename=" + str(png), "--export-width=1920", "--export-height=1080"],
                       check=True, capture_output=True, timeout=60)
        data = png.read_bytes()
        if not data.startswith(b"\x89PNG\r\n\x1a\n") or len(data)<1024:
            raise RuntimeError("Real Inkscape export failed validation")
        return {"png_sha256": hashlib.sha256(data).hexdigest(), "png_bytes": len(data), "frame_count": 6, "source": FIXTURE_ID}

class Handler(BaseHTTPRequestHandler):
    server_version = "BOSS-Private-Worker-Qualification"
    sys_version = ""
    def log_message(self, *_):
        pass
    def reply(self, status, obj):
        b = canonical(obj)
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(b)
    def do_GET(self):
        if self.path=="/healthz":
            return self.reply(200, {"service":"boss-private-svg-qualification","test_only":True,"health":"ok","gateway_ready":False})
        return self.reply(404, {"status":"NOT_FOUND"})
    def do_POST(self):
        if self.path!=ROUTE:
            return self.reply(404, {"status":"NOT_FOUND"})
        try:
            n=int(self.headers.get("Content-Length", "-1"))
        except ValueError:
            n=-1
        if n<1 or n>MAX_BODY:
            return self.reply(413, {"status":"DENIED","reason":"BODY_LIMIT"})
        raw=self.rfile.read(n)
        try:
            req=json.loads(raw)
            if not isinstance(req,dict) or set(req)!={"operation","fixture","nonce","issued_at","caller"}:
                raise ValueError()
            if req["operation"]!="synthetic_render" or req["fixture"]!=FIXTURE_ID or req["caller"]!="gateway-test-only":
                raise ValueError()
            if not isinstance(req["nonce"],str) or not (24<=len(req["nonce"])<=80):
                raise ValueError()
            t=req["issued_at"]
            if not isinstance(t,int) or abs(int(time.time())-t)>30:
                raise ValueError()
        except (ValueError,TypeError):
            return self.reply(403, {"status":"DENIED","reason":"INVALID_INTENT"})
        sig=self.headers.get("X-BOSS-Test-Signature", "")
        try:
            good=hmac.compare_digest(sig, expected_sig(req))
        except RuntimeError:
            good=False
        if not good:
            return self.reply(403, {"status":"DENIED","reason":"MISSING_GATEWAY_PROOF"})
        with LOCK:
            if req["nonce"] in NONCES:
                return self.reply(409, {"status":"DENIED","reason":"REPLAY"})
            NONCES.add(req["nonce"])  # Local ephemeral negative-control only; not durable custody.
        try:
            return self.reply(200, {"status":"SYNTHETIC_RENDER_OK", **native_render()})
        except Exception:
            return self.reply(503, {"status":"DENIED","reason":"NATIVE_RENDER_UNAVAILABLE"})
    def do_PUT(self):
        return self.reply(405, {"status":"METHOD_NOT_ALLOWED"})
    do_DELETE=do_PUT
    do_PATCH=do_PUT

def serve():
    key_bytes()   # fail boot without test-only credential
    if shutil.which("inkscape") is None:
        raise RuntimeError("Real Inkscape must be installed")
    port=int(os.environ.get("PORT",PORT_DEFAULT))
    if not 1<=port<=65535:
        raise ValueError("Invalid port")
    server=ThreadingHTTPServer(("0.0.0.0",port),Handler)
    server.daemon_threads=True
    server.serve_forever()

if __name__=="__main__":
    serve()
