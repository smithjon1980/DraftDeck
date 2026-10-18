import contextlib
import io
import json
import os
import sys
import unittest
import urllib.error
from unittest.mock import patch
import check_baseten_catalog as cat

class FakeResponse:
    status=200
    def __init__(self, payload):
        self.payload=payload
    def read(self, max_bytes):
        return self.payload
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return False

class FakeOpener:
    def __init__(self, data):
        self.data=data
        self.requests=[]
    def open(self, req, timeout):
        self.requests.append((req, timeout))
        return FakeResponse(self.data)

class TestCatalogCheck(unittest.TestCase):
    def test_no_network_by_default(self):
        with patch.object(sys, "argv", ["check_baseten_catalog.py"]), \
             patch("check_baseten_catalog.urllib.request.build_opener") as network, \
             contextlib.redirect_stdout(io.StringIO()) as stdout:
            cat.main()
            network.assert_not_called()
            self.assertIn("NO_NETWORK", stdout.getvalue())

    def test_read_only_request_and_minimal_output(self):
        opener=FakeOpener(json.dumps({"data":[{"id":"meta-models/muse-spark-open"},
                                               {"id":"another-model"}]}).encode())
        result=cat.probe("dummy-test-secret", opener=opener)
        self.assertEqual(result["status"], "PASS")
        self.assertTrue(result["muse_spark_listed"])
        self.assertEqual(result["model_inference"], "NOT_EXECUTED")
        req,timeout=opener.requests[0]
        self.assertEqual(req.get_method(), "GET")
        self.assertEqual(req.full_url, cat.CATALOG_URL)
        self.assertLessEqual(timeout, 12)
        self.assertNotIn("dummy-test-secret", json.dumps(result))

    def test_missing_key_holds_without_network(self):
        with patch("check_baseten_catalog.urllib.request.build_opener") as network:
            self.assertEqual(cat.probe("")["status"],"HOLD")
            network.assert_not_called()

    def test_invalid_key_format_holds(self):
        self.assertEqual(cat.probe("unsafe\nheader")["reason"],"INVALID_SECRET_FORMAT")

    def test_bad_structure_not_accepted(self):
        result=cat.probe("dummy",opener=FakeOpener(b'{"models":[]}'))
        self.assertEqual(result["reason"],"UNKNOWN_CATALOG_FORMAT")

    def test_http_unauthorized_is_reported_safely(self):
        class Reject:
            def open(self, req, timeout):
                raise urllib.error.HTTPError(req.full_url, 401,
                    "secret-provider-message", None, None)
        result=cat.probe("dummy", opener=Reject())
        self.assertEqual(result["reason"], "UNAUTHORIZED_OR_REVOKED")
        self.assertNotIn("secret-provider-message", json.dumps(result))

    def test_no_inference_path_in_catalog_url(self):
        self.assertTrue(cat.CATALOG_URL.endswith("/v1/models"))
        self.assertNotIn("completions", cat.CATALOG_URL)
        self.assertEqual(cat.MAX_RESPONSE_BYTES, 2_000_000)

if __name__=="__main__":
    unittest.main()
