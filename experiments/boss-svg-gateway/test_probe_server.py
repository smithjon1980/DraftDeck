"""Local HTTP tests: probe is healthy but gateway is intentionally never ready."""
import http.client
import json
import threading
import unittest
from http.server import ThreadingHTTPServer
import probe_server


class ProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), probe_server.Handler)
        cls.server.daemon_threads = True
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.server.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)

    def req(self, method, path, body=None):
        conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=3)
        conn.request(method, path, body=body)
        res = conn.getresponse()
        data = res.read()
        info = res.status, dict(res.getheaders()), data
        conn.close()
        return info

    def test_health_is_up_but_not_gateway_ready(self):
        status, headers, raw = self.req("GET", "/healthz")
        self.assertEqual(status, 200)
        self.assertEqual(headers["Cache-Control"], "no-store")
        data = json.loads(raw)
        self.assertFalse(data["gateway_ready"])
        self.assertFalse(data["approval_connected"])
        self.assertFalse(data["custody_connected"])

    def test_readiness_stays_closed(self):
        status, _, raw = self.req("GET", "/readyz")
        self.assertEqual(status, 503)
        self.assertEqual(json.loads(raw)["status"], "NOT_READY")

    def test_protected_dispatch_always_denied(self):
        for content in (b"{}", b'{"approved":true}', b'{"action":"metadata_edit","actor_id":"fake"}'):
            with self.subTest(content=content):
                status, _, raw = self.req("POST", "/v1/svg/dispatch", content)
                self.assertEqual(status, 503)
                self.assertEqual(json.loads(raw)["status"], "DENIED")
                self.assertNotIn(content, raw)

    def test_other_routes_do_not_serve(self):
        for path in ("/", "/docs", "/openapi.json", "/v1/approval", "/v1/custody", "/../../etc/passwd", "/healthz?mode=ready"):
            with self.subTest(path=path):
                self.assertEqual(self.req("GET", path)[0], 404)

    def test_mutating_methods_disabled(self):
        for method in ("PUT", "PATCH", "DELETE"):
            with self.subTest(method=method):
                self.assertEqual(self.req(method, "/healthz")[0], 405)

    def test_head_contains_no_body(self):
        status, headers, raw = self.req("HEAD", "/healthz")
        self.assertEqual(status, 200)
        self.assertEqual(raw, b"")
        self.assertGreater(int(headers["Content-Length"]), 0)


if __name__ == "__main__":
    unittest.main()
