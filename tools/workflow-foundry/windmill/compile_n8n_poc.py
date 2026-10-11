# Windmill script candidate for BOSS-D0-WF-001.
# Load workflow JSON from a pinned GitHub path in the calling Windmill flow.
# No credentials are injected into generated JSON.
import copy, hashlib, json, re
from urllib.parse import urlparse
import requests

REQUIRED_ID="13DEHx7la7LrgAZ3vHLm46sTXiqV1f7nC"
REQUIRED_SHA="c03ab480fbfd836e5db6670440f9734220e3edb842a7e7379bf87905f7dc8544"

def compile_candidate(template: dict) -> dict:
    workflow=copy.deepcopy(template)
    if workflow.get("active") is not False:
        raise ValueError("Foundry gate: template must be inactive")
    nodes=workflow.get("nodes",[])
    kinds={n.get("type") for n in nodes}
    required={"n8n-nodes-base.manualTrigger","n8n-nodes-base.googleDrive","n8n-nodes-base.code"}
    if not required.issubset(kinds) or len(nodes)!=3:
        raise ValueError("Foundry gate: unexpected node topology")
    names={n.get("name") for n in nodes}
    if names!={"Manual Test Trigger","Get Authorized Drive Audio","Verify SHA256 + Emit HOLD Receipt"}:
        raise ValueError("Foundry gate: node names differ from approved candidate")
    if any(n.get("credentials") for n in nodes):
        raise ValueError("Foundry gate: credential bindings must be approved separately")
    serialized=json.dumps(workflow,sort_keys=True)
    if REQUIRED_ID not in serialized or REQUIRED_SHA not in serialized:
        raise ValueError("Foundry gate: source coordinates do not match authorized fixture")
    # Minimal API payload: n8n create workflow accepts name, nodes, connections, settings.
    return {k:workflow[k] for k in ("name","nodes","connections","settings")}

def main(template: dict, n8n_base_url: str="", n8n_api_key: str="", dry_run: bool=True, approved_for_draft_create: bool=False):
    candidate=compile_candidate(template)
    payload=json.dumps(candidate,sort_keys=True)
    receipt={"order":"BOSS-D0-WF-001","result":"COMPILED_CANDIDATE",
             "sha256":hashlib.sha256(payload.encode()).hexdigest(),
             "source_file_id":REQUIRED_ID,"source_sha256":REQUIRED_SHA,
             "target_status":"INACTIVE","execution_authorized":False}
    if dry_run:
        receipt["deployment"]="NOT_REQUESTED"
        return {"receipt":receipt,"n8n_workflow_payload":candidate}
    if not approved_for_draft_create:
        raise ValueError("Foundry gate: no explicit draft-creation authorization")
    url=urlparse(n8n_base_url)
    if url.scheme!="https" or not url.netloc or url.username or url.password:
        raise ValueError("Foundry gate: HTTPS n8n host required")
    if not n8n_api_key:
        raise ValueError("Foundry gate: missing n8n API key")
    # Do not return or print authorization header. Import without activating.
    r=requests.post(n8n_base_url.rstrip("/")+"/api/v1/workflows",
        headers={"X-N8N-API-KEY":n8n_api_key,"Content-Type":"application/json"},
        json=candidate,timeout=30)
    if r.status_code not in (200,201):
        raise RuntimeError("n8n draft create failed (status %d)" % r.status_code)
    obj=r.json()
    if obj.get("active") is True:
        raise RuntimeError("n8n response indicates unexpected activation")
    receipt["deployment"]="DRAFT_CREATED_UNTESTED"
    receipt["n8n_workflow_id"]=obj.get("id")
    return {"receipt":receipt}
