#!/usr/bin/env python3
"""CI-only precomposition gate. Reads approval ledger exports; cannot grant approval."""
import json,sys,re,hashlib
from pathlib import Path
HEX=re.compile(r"^[0-9a-f]{64}$")
def check(v):
 errors=[]
 if v.get("contract")!="BOSS-PRECOMPOSE-V1":errors.append("contract")
 for key in ("slide_id","section_id","art_id","story_id","art_sha256","story_sha256","composition_target"):
  if not isinstance(v.get(key),str) or not v[key].strip():errors.append("missing "+key)
 for k in ("art_sha256","story_sha256"):
  if not HEX.fullmatch(str(v.get(k,""))):errors.append("invalid "+k)
 if v.get("stage")!="PRECOMPOSITION":errors.append("stage")
 approvals=v.get("approvals")
 if not isinstance(approvals,list):return errors+["approvals required"]
 for layer in ("ART","STORY"):
  matches=[x for x in approvals if isinstance(x,dict) and x.get("layer")==layer]
  if len(matches)!=1:errors.append("one "+layer+" approval required");continue
  a=matches[0]
  for k,expected in (("candidate_id",v.get("art_id" if layer=="ART" else "story_id")),("source_sha256",v.get("art_sha256" if layer=="ART" else "story_sha256")),("slide_id",v.get("slide_id")),("section_id",v.get("section_id")),("composition_target",v.get("composition_target"))):
   if a.get(k)!=expected:errors.append(layer+" mismatch "+k)
  if a.get("decision")!="APPROVED":errors.append(layer+" not approved")
  if a.get("reviewer_kind")!="HUMAN" or a.get("reviewer_id") in ("",None,"agent","system"):errors.append(layer+" lacks human reviewer")
  if not isinstance(a.get("evidence_ref"),str) or not a["evidence_ref"].startswith("private:"):errors.append(layer+" lacks private evidence ref")
  if not isinstance(a.get("preview_sha256"),str) or not HEX.fullmatch(a["preview_sha256"]):errors.append(layer+" lacks verified preview hash")
  if a.get("source")=="CI_GENERATED":errors.append(layer+" CI self-approval")
 if v.get("approval_verified_by_trusted_service") is not True:errors.append("trusted out-of-band human verification required")
 if v.get("production_release_authorized") is not False:errors.append("precomposition cannot authorize release")
 return errors
if __name__=="__main__":
 try: x=json.loads(Path(sys.argv[1]).read_text())
 except (IndexError,OSError,ValueError) as e:print("HOLD:",e);sys.exit(2)
 issues=check(x)
 print("HOLD: "+"; ".join(issues) if issues else "ELIGIBLE FOR COMPOSITION (manifest consistency only; trusted verifier must independently attest approvals)")
 sys.exit(bool(issues))
