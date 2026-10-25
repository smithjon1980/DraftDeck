"""Run against the built Docker container; fail if protected route accepts anything."""
import http.client
import json
import os
import time

host = os.environ.get("BOSS_PROBE_HOST", "127.0.0.1")
port = int(os.environ.get("BOSS_PROBE_PORT", "17896"))


def call(method, path, body=None):
    c = http.client.HTTPConnection(host, port, timeout=3)
    c.request(method, path, body=body)
    r = c.getresponse()
    result = (r.status, dict(r.getheaders()), r.read())
    c.close()
    return result


for attempt in range(30):
    try:
        status, headers, raw = call("GET", "/healthz")
        if status == 200:
            break
    except (ConnectionError, OSError, TimeoutError):
        pass
    time.sleep(1)
else:
    raise AssertionError("Docker service never became healthy")

assert headers["Cache-Control"] == "no-store"
d = json.loads(raw)
assert d["mode"] == "test-only"
assert d["gateway_ready"] is False and d["approval_connected"] is False and d["custody_connected"] is False
assert call("GET", "/readyz")[0] == 503
assert json.loads(call("POST", "/v1/svg/dispatch", b'{"approved":true}')[2])["status"] == "DENIED"
assert call("POST", "/v1/svg/dispatch", b'{"action":"export_pdf"}')[0] == 503
assert call("GET", "/v1/svg/dispatch")[0] == 404
assert call("GET", "/")[0] == 404
assert call("DELETE", "/v1/svg/dispatch")[0] == 405
print("CONTAINER_SMOKE_PASS: health alive; gateway intentionally not ready; protected dispatch denied.")
