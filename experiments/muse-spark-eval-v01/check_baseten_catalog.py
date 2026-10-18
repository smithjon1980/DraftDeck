#!/usr/bin/env python3
"""Read-only Baseten Model API catalog authentication check.

Default: no network, no secret inspection.
--check: ONE authenticated GET https://inference.baseten.co/v1/models
Never calls chat/completions, deploys models, or changes workspace settings.
Prints no secret, request body, response body, or response headers.
A catalog success proves access to THIS endpoint, not inference authorization,
budget enforcement, or the availability of a particular paid model.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

CATALOG_URL = "https://inference.baseten.co/v1/models"
MAX_RESPONSE_BYTES = 2_000_000


class NoRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        raise ValueError("Redirect not allowed for authenticated catalog request")


def probe(api_key, *, opener=None):
    if not api_key or not api_key.strip():
        return {"status": "HOLD", "reason": "MISSING_SECRET"}
    if "\n" in api_key or "\r" in api_key:
        return {"status": "HOLD", "reason": "INVALID_SECRET_FORMAT"}
    req = urllib.request.Request(
        CATALOG_URL,
        headers={"Authorization": "Bearer " + api_key, "Accept": "application/json"},
        method="GET",
    )
    caller = opener or urllib.request.build_opener(NoRedirects())
    try:
        with caller.open(req, timeout=12) as response:
            status = response.status
            raw = response.read(MAX_RESPONSE_BYTES + 1)
        if status != 200:
            return {"status": "HOLD", "reason": "UNEXPECTED_HTTP_STATUS"}
        if len(raw) > MAX_RESPONSE_BYTES:
            return {"status": "HOLD", "reason": "RESPONSE_TOO_LARGE"}
        data = json.loads(raw)
        if not isinstance(data, dict) or not isinstance(data.get("data"), list):
            return {"status": "HOLD", "reason": "UNKNOWN_CATALOG_FORMAT"}
        items = data["data"]
        ids = [v["id"] for v in items if isinstance(v, dict) and isinstance(v.get("id"), str)]
        muse_ids = [model_id for model_id in ids if "muse" in model_id.casefold() and "spark" in model_id.casefold()]
        return {
            "status": "PASS",
            "meaning": "KEY_ACCEPTED_FOR_CATALOG_ONLY",
            "catalog_count": len(ids),
            "muse_spark_listed": bool(muse_ids),
            "muse_spark_id": muse_ids[:2],
            "model_inference": "NOT_EXECUTED",
            "billing_cap": "NOT_VERIFIED",
        }
    except urllib.error.HTTPError as exc:
        reasons = {401: "UNAUTHORIZED_OR_REVOKED", 403: "FORBIDDEN_OR_INSUFFICIENT_SCOPE",
                   404: "CATALOG_ENDPOINT_NOT_FOUND", 429: "RATE_LIMITED"}
        return {"status": "HOLD", "reason": reasons.get(exc.code, "PROVIDER_HTTP_ERROR"),
                "http_status": exc.code}
    except (urllib.error.URLError, TimeoutError, ValueError, json.JSONDecodeError):
        return {"status": "HOLD", "reason": "NETWORK_OR_RESPONSE_ERROR"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Explicitly send one authenticated read-only GET")
    args = parser.parse_args()
    if not args.check:
        print(json.dumps({"status": "NO_NETWORK",
                          "method": "GET", "endpoint": CATALOG_URL,
                          "model_inference": "NOT_EXECUTED"}))
        return
    result = probe(os.environ.get("BASETEN_API_KEY", ""))
    print(json.dumps(result, sort_keys=True))
    if result["status"] != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
