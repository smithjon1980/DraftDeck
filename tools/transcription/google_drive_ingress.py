#!/usr/bin/env python3
"""Authenticated Google Drive media retrieval. Never prints credentials or payload."""
import argparse, hashlib, json, os, pathlib, re, sys
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--file-id",required=True)
    p.add_argument("--expected-sha256",required=True)
    p.add_argument("--output",required=True)
    args=p.parse_args()
    if not re.fullmatch(r"[a-zA-Z0-9_-]{10,120}", args.file_id):
        sys.exit("INVALID_DRIVE_FILE_ID")
    if not re.fullmatch(r"[0-9a-f]{64}", args.expected_sha256):
        sys.exit("INVALID_SHA256")
    secret=os.environ.get("GOOGLE_DRIVE_SA_JSON","")
    if not secret:
        sys.exit("MISSING_DRIVE_CREDENTIAL_SECRET")
    try:
        info=json.loads(secret)
        if info.get("type")!="service_account":
            raise ValueError("NOT_SERVICE_ACCOUNT")
        credentials=service_account.Credentials.from_service_account_info(
            info,scopes=["https://www.googleapis.com/auth/drive.readonly"])
        session=AuthorizedSession(credentials)
        url="https://www.googleapis.com/drive/v3/files/"+args.file_id
        output=pathlib.Path(args.output)
        output.parent.mkdir(parents=True,exist_ok=True)
        size=0
        digest=hashlib.sha256()
        with session.get(url,params={"alt":"media","supportsAllDrives":"true"},timeout=90,stream=True) as response:
            if response.status_code!=200:
                raise ValueError("DRIVE_API_FETCH_FAILED")
            with output.open("wb") as f:
                os.chmod(output,0o600)
                for chunk in response.iter_content(chunk_size=1024*1024):
                    if not chunk: continue
                    size+=len(chunk)
                    if size>40*1024*1024: raise ValueError("SIZE_LIMIT")
                    digest.update(chunk)
                    f.write(chunk)
        if not size or digest.hexdigest()!=args.expected_sha256:
            raise ValueError("HASH_OR_EMPTY")
    except Exception:
        if "output" in locals(): output.unlink(missing_ok=True)
        sys.exit("DRIVE_INGRESS_FAILED: permissions, credentials, transport, size or checksum")
    print("DRIVE_INGRESS_SHA256_VERIFIED")
if __name__=="__main__":
    main()
