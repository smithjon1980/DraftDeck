"""Candidate gate; simulated resolver does NOT confer trusted authorization."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator
HERE=Path(__file__).parent
SCHEMA=json.loads((HERE/"boss-release-gate-v03.schema.json").read_text())
class Hold(RuntimeError): pass
class Resolver:
    def __init__(self, records): self.records=records
    def get(self, ref): return self.records.get(ref)
def evaluate(p, resolver):
    if list(Draft202012Validator(SCHEMA).iter_errors(p)): raise Hold("RELEASE_BLOCKED_SCHEMA")
    for node,ref in p["ipos"].items():
        r=resolver.get(ref)
        if not r or r.get("kind")!="ipos" or r.get("node")!=node or r.get("verified") is not True: raise Hold("RELEASE_BLOCKED_EVIDENCE_DEFICIT")
    receipt=resolver.get(p["claim"]["execution_receipt_id"])
    if not receipt or receipt.get("kind")!="execution" or receipt.get("verified") is not True or receipt.get("outcome") not in ("SUCCESS","FAILURE"): raise Hold("RELEASE_BLOCKED_EVIDENCE_DEFICIT")
    if receipt["outcome"]!=p["claim"]["asserted_outcome"]: raise Hold("RELEASE_BLOCKED_SPLIT_SIGNAL")
    for key in ("retention","minimization"):
        r=resolver.get(p["controls"][key]["evidence_id"])
        if not r or r.get("kind")!=key or r.get("verified") is not True: raise Hold("RELEASE_BLOCKED_PRIVACY_VIOLATION")
    ir=resolver.get(p["controls"]["incident_route"]["evidence_id"])
    if not ir or ir.get("kind")!="incident_route" or ir.get("verified") is not True: raise Hold("RELEASE_BLOCKED_CONTROL")
    sp=p["controls"]["specialist"]
    if sp["required"] or p["risk_tier"] in ("T3","T4"):
        r=resolver.get(sp["evidence_id"])
        if not r or r.get("kind")!="specialist" or r.get("verified") is not True: raise Hold("RELEASE_BLOCKED_PENDING_SPECIALIST")
    return "RELEASE_ELIGIBLE_FOR_TRUSTED_AUTHORIZATION_CHECK"

def test():
    records={**{"evidence_"+n:{"kind":"ipos","node":n,"verified":True} for n in ("input","process","output","storage")},**{n+"_ok":{"kind":n,"verified":True} for n in ("retention","minimization","incident_route","specialist")}, "execution_ok":{"kind":"execution","outcome":"SUCCESS","verified":True},"execution_forbidden":{"kind":"execution","outcome":"FAILURE","verified":True}}
    expected={"01_golden_path":"RELEASE_ELIGIBLE_FOR_TRUSTED_AUTHORIZATION_CHECK","02a_evidence_deficit":"RELEASE_BLOCKED_EVIDENCE_DEFICIT","02b_split_signal_error":"RELEASE_BLOCKED_SPLIT_SIGNAL","03_unsigned_handoff":"RELEASE_BLOCKED_PENDING_SPECIALIST","04_privacy_deficit":"RELEASE_BLOCKED_PRIVACY_VIOLATION"}
    for name,target in expected.items():
        p=json.loads((HERE/(name+".json")).read_text())
        try: actual=evaluate(p,Resolver(records))
        except Hold as e: actual=str(e)
        assert actual==target,(name,actual,target)
        print(name,actual,"PASS")
    print("5/5 deterministic local classifications; Windmill live enforcement NOT ESTABLISHED")
if __name__=="__main__": test()
