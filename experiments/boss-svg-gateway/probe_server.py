"""Render network/health probe only; never authorize or dispatch an SVG operation."""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HEALTH = {"service": "boss-svg-probe", "mode": "test-only", "health": "ok",
          "gateway_ready": False, "approval_connected": False, "custody_connected": False}
NOT_READY = {"service": "boss-svg-probe", "mode": "test-only",
             "status": "NOT_READY", "reason": "NO_POLICY_GATEWAY_OR_PROTECTED_SERVICES"}
DENIED = {"service": "boss-svg-probe", "mode": "test-only",
          "status": "DENIED", "reason": "PROTECTED_OPERATIONS_DISABLED"}
MISSING = {"status": "NOT_FOUND"}
METHOD = {"status": "METHOD_NOT_ALLOWED"}


class Handler(BaseHTTPRequestHandler):
    server_version = "BOSS-Health-Probe"
    sys_version = ""
    protocol_version = "HTTP/1.0"

    def log_message(self, fmt, *args):
        # No body, URLs, or headers written to logs; never echo a request.
        pass

    def send_json(self, status, body, head=False):
        payload = json.dumps(body, separators=(",", ":"), sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Connection", "close")
        self.end_headers()
        if not head:
            self.wfile.write(payload)
        self.close_connection = True

    def do_GET(self):
        if self.path == "/healthz":
            return self.send_json(200, HEALTH)
        if self.path == "/readyz":
            return self.send_json(503, NOT_READY)
        return self.send_json(404, MISSING)

    def do_HEAD(self):
        if self.path == "/healthz":
            return self.send_json(200, HEALTH, head=True)
        if self.path == "/readyz":
            return self.send_json(503, NOT_READY, head=True)
        return self.send_json(404, MISSING, head=True)

    def do_POST(self):
        # Never read, forward, store, parse or execute request bodies.
        if self.path == "/v1/svg/dispatch":
            return self.send_json(503, DENIED)
        return self.send_json(404, MISSING)

    def do_PUT(self):
        return self.send_json(405, METHOD)

    def do_PATCH(self):
        return self.send_json(405, METHOD)

    def do_DELETE(self):
        return self.send_json(405, METHOD)


def serve():
    port = int(os.environ.get("PORT", "10000"))
    if not 1 <= port <= 65535:
        raise ValueError("Invalid PORT")
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    server.daemon_threads = True
    server.serve_forever(poll_interval=0.2)


if __name__ == "__main__":
    serve()
