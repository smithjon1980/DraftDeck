#!/usr/bin/env python3
"""Fail-closed structural admission of slide handoff metadata. Never reads private payload."""
import json, re, sys
from pathlib import Path
REQUIRED={"contract","section_id","slide_ids","source_sha256","source_class","source_location_class","private_evidence_ref","dispatch_state","openbot_mode","mandatory_gateway_verified","audit_fail_closed","human_selection","human_release","publish_state"}
def check(m):
    problems=[]
    if not isinstance(m,dict): return ["manifest must be object"]
    missing=REQUIRED-set(m)
    if missing: problems.append("missing keys: "+",".join(sorted(missing)))
    if set(m)-REQUIRED: problems.append("unknown keys")
    if m.get("contract")!="BOSS-SLIDE-HANDOFF-V1": problems.append("contract mismatch")
    ids=m.get("slide_ids")
    if not isinstance(ids,list) or not ids or any(type(x)!=int or x<1 for x in ids) or len(ids)!=len(set(ids)):problems.append("invalid slide IDs")
    if not re.fullmatch(r"[a-f0-9]{64}",str(m.get("source_sha256",""))):problems.append("bad source hash")
    for field,allowed in {
      "source_class":{"PRIVATE_UNPUBLISHED","PUBLIC_SYNTHETIC","APPROVED_FOR_DISTRIBUTION"},
      "source_location_class":{"PRIVATE_LIBRARY","PRIVATE_DRIVE","LOCAL_PRIVATE","PUBLIC_REPOSITORY"},
      "dispatch_state":{"HOLD","SANDBOX_ONLY","AUTHORIZED"},
      "openbot_mode":{"enforce","dry-run","absent"},
      "human_selection":{"PENDING","APPROVED"},"human_release":{"PENDING","APPROVED"},
      "publish_state":{"NOT_PUBLISHED","RELEASED"}
    }.items():
      if m.get(field) not in allowed:problems.append("invalid "+field)
    for field in ("section_id","private_evidence_ref"):
      if not isinstance(m.get(field),str) or not m[field].strip():problems.append("missing "+field)
    for field in ("mandatory_gateway_verified","audit_fail_closed"):
      if type(m.get(field))!=bool:problems.append("invalid "+field)
    if m.get("source_class")=="PRIVATE_UNPUBLISHED" and m.get("source_location_class")=="PUBLIC_REPOSITORY":problems.append("private source cannot be public")
    if m.get("dispatch_state")!="HOLD" and (m.get("openbot_mode")!="enforce" or not m.get("mandatory_gateway_verified") or not m.get("audit_fail_closed")):problems.append("dispatch requires enforced verified gateway and fail-closed audit")
    if m.get("dispatch_state")=="AUTHORIZED" and m.get("human_release")!="APPROVED":problems.append("authorized dispatch requires human release")
    if m.get("publish_state")=="RELEASED" and (m.get("human_selection")!="APPROVED" or m.get("human_release")!="APPROVED" or m.get("dispatch_state")!="AUTHORIZED"):problems.append("release requires human authorization and dispatch approval")
    return problems
if __name__=="__main__":
    try: manifest=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (IndexError, OSError,ValueError) as e: print("FAIL:",e);sys.exit(2)
    errors=check(manifest)
    print("FAIL: "+"; ".join(errors) if errors else "PASS: metadata validation only; NO execution/release approval")
    sys.exit(bool(errors))
