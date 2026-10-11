#!/usr/bin/env python3
"""Download private, ephemeral HTTPS payload; verify digest before ASR."""
import argparse
import hashlib
import os
import pathlib
import re
import ssl
import sys
import urllib.request

p = argparse.ArgumentParser()
p.add_argument("--output", required=True)
p.add_argument("--expected-sha256", required=True)
a = p.parse_args()
url = os.environ.get("SIGNED_AUDIO_URL", "")
if not re.fullmatch(r"[0-9a-f]{64}", a.expected_sha256):
    sys.exit("INVALID_EXPECTED_SHA256")
if not url.startswith("https://"):
    sys.exit("MISSING_OR_NON_HTTPS_SIGNED_URL")
# Ensure the token never appears in stdout, exception text, or receipts.
output = pathlib.Path(a.output)
output.parent.mkdir(parents=True, exist_ok=True)
digest = hashlib.sha256()
limit = 40 * 1024 * 1024
count = 0
try:
    req = urllib.request.Request(url, headers={"User-Agent": "BOSS-Private-ASR/1"})
    with urllib.request.urlopen(req, timeout=60, context=ssl.create_default_context()) as response:
        if response.geturl().split(":")[0].lower() != "https":
            raise ValueError("REDIRECT_SCHEME_NOT_HTTPS")
        with output.open("wb") as dest:
            os.chmod(output, 0o600)
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                count += len(chunk)
                if count > limit:
                    raise ValueError("MAX_PAYLOAD_EXCEEDED")
                digest.update(chunk)
                dest.write(chunk)
    if count == 0:
        raise ValueError("EMPTY_PAYLOAD")
    if digest.hexdigest() != a.expected_sha256:
        raise ValueError("HASH_MISMATCH")
except Exception:
    output.unlink(missing_ok=True)
    sys.exit("INGRESS_FAILED: inaccessible/expired signed URL, TLS, size, or digest check")
print("INGRESS_SHA256_VERIFIED")
