#!/usr/bin/env python3
"""Smoke-test public demo API using only a generic synthesized WAV.

This is an upstream-demo feasibility check, NOT pinned model benchmarking.
No BOSS narration, private audio or credentials are sent.
"""
import json
import os
import sys
from pathlib import Path

SPACE = "hugging-apps/granite-speech-5-0-2b"
REF = "The shipping label does not prove delivery. The package requires independent inspection."
OUT = Path("granite_public_space_smoke.json")

def record(**extra):
    result={"space":SPACE,"expected_model_family":"Granite Speech 5.0 2B",
            "dataset":"PUBLIC_GENERIC_SYNTHETIC","reference":REF,
            "owner_unpublished_content":False,**extra}
    OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print(json.dumps(result,indent=2,ensure_ascii=False),flush=True)

def main():
    from gradio_client import Client, handle_file
    import re
    import time
    wav=Path("public_synthetic_16k.wav")
    if not wav.exists():
        raise FileNotFoundError("Public-only WAV missing")
    print("Inspecting public Space API (no private data)",flush=True)
    client=Client(SPACE,verbose=False)
    available=client.view_api(return_format="dict")
    endpoints=available.get("named_endpoints",{})
    candidates=[]
    for name,info in endpoints.items():
        p=info.get("parameters",[])
        n=[z for z in p if "audio" in (str(z.get("component",""))+" "+str(z.get("label",""))).lower()]
        if len(n)==1: candidates.append((name,info,n[0]))
    if not candidates:
        record(status="BLOCKED_NO_COMPATIBLE_AUDIO_ENDPOINT",
               visible_endpoint_names=list(endpoints))
        return
    name,info,audio=candidates[0]
    params=info.get("parameters",[])
    payload=[]
    for p in params:
        component=str(p.get("component","")).lower()
        label=str(p.get("label","")).lower()
        if p is audio:
            payload.append(handle_file(str(wav.resolve())))
        elif "textbox" in component or "prompt" in label:
            payload.append("transcribe the speech with proper punctuation and capitalization.")
        elif p.get("parameter_has_default", False):
            payload.append(p.get("parameter_default"))
        elif "checkbox" in component:
            payload.append(False)
        elif "dropdown" in component or "radio" in component:
            if p.get("default") is not None: payload.append(p["default"])
            elif p.get("choices"): payload.append(p["choices"][0])
            else:
                record(status="BLOCKED_UNSUPPORTED_INPUT",endpoint=name,reason=str(p)[:700])
                return
        elif p.get("default") is not None:
            payload.append(p["default"])
        else:
            record(status="BLOCKED_UNSUPPORTED_INPUT",endpoint=name,reason=str(p)[:700])
            return
    print("Calling upstream Space named endpoint (public fixture only): "+name,flush=True)
    start=time.monotonic()
    try:
        reply=client.predict(*payload,api_name=name)
        elapsed=time.monotonic()-start
        text=reply if isinstance(reply,str) else json.dumps(reply,ensure_ascii=False)
        record(status="DEMO_RETURNED_OUTPUT",endpoint=name,
               demo_reported_version_unverified=True,
               processing_seconds=round(elapsed,3),
               hypothesis=text[:4000],keyword_bias_tested=False,
               production_accuracy_verified=False)
    except Exception as exc:
        record(status="BLOCKED_DEMO_CALL",endpoint=name,error=type(exc).__name__,
               detail=str(exc)[:500])
if __name__=="__main__":
    try: main()
    except Exception as exc:
        record(status="BLOCKED_PROBE",error=type(exc).__name__,detail=str(exc)[:500])
