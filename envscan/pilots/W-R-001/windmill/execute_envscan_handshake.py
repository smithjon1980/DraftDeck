"""Windmill Python script; bind secret_token to a Windmill encrypted variable, never source-control it."""
import json
import uuid
import urllib.request
import urllib.error
from datetime import datetime, timezone

def call(url, payload, token=None, raw=False, timeout=8):
    data = payload if raw else json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read(16384).decode("utf-8")
            return {"http_status": response.status, "body": json.loads(body)}
    except urllib.error.HTTPError as error:
        raw_body = error.read(16384).decode("utf-8", errors="replace")
        try:
            body = json.loads(raw_body)
        except json.JSONDecodeError:
            body = {"unparsed_response": raw_body[:500]}
        return {"http_status": error.code, "body": body}
    except (urllib.error.URLError, TimeoutError) as error:
        return {"transport_error": type(error).__name__, "detail": str(error.reason if hasattr(error, "reason") else error)[:200]}

def main(base_url: str, secret_token: str):
    if not base_url.startswith("https://"):
        raise ValueError("base_url must use HTTPS")
    if not secret_token:
        raise ValueError("Bind secret_token from an encrypted Windmill variable")
    target = base_url.rstrip("/") + "/api/v1/diagnostic/synthetic-run"
    correlation_id = "WR001_" + uuid.uuid4().hex
    payload = {"correlation_id": correlation_id, "mission_profile": "HANDSHAKE_TEST"}
    probes = {}
    probes["intruder"] = call(target, payload)
    probes["malformed"] = call(target, {"mission_profile": "HANDSHAKE_TEST"}, token=secret_token)
    # Negative transport test targets Windmill runner's local loopback, NOT Railway.
    # ECONNREFUSED is a valid expected transport failure; do not call it a timeout.
    probes["ghost"] = call("http://127.0.0.1:1/api/v1/diagnostic/synthetic-run", payload, token=secret_token, timeout=2)
    probes["authorized"] = call(target, payload, token=secret_token)
    good = probes["authorized"].get("body", {})
    checks = {
      "intruder_401": probes["intruder"].get("http_status") == 401,
      "malformed_400": probes["malformed"].get("http_status") == 400,
      "ghost_transport_error": "transport_error" in probes["ghost"],
      "authorized_200": probes["authorized"].get("http_status") == 200,
      "receipt_matches": good.get("correlation_id") == correlation_id and
                         good.get("mission_profile") == "HANDSHAKE_TEST" and
                         good.get("diagnostic_code") == "E9999_SYNTHETIC" and
                         good.get("outcome") == "EXPECTED_SYNTHETIC_FAILURE" and
                         good.get("synthetic") is True
    }
    return {"test_id": "W-R-001", "at_utc": datetime.now(timezone.utc).isoformat(),
            "correlation_id": correlation_id, "checks": checks,
            "pilot_result": "PASS" if all(checks.values()) else "FAIL",
            "probes": probes, "scope": "Windmill to Railway synthetic boundary only; not independent execution attestation"}
