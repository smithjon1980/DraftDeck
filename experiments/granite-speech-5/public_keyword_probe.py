#!/usr/bin/env python3
"""Public BOSS terminology probe; uses only newly authored generic synthetic speech.

Never sends unpublished narrated paragraphs. Hosted demo backend is not pinned.
"""
import json
from pathlib import Path
import re
import time

MODEL_DEMO="hugging-apps/granite-speech-5-0-2b"
REF="Bioscillate uses IPOS, PARCELS, and PRIME at Main Street Copy."
TERMS=["Bioscillate","IPOS","PARCELS","PRIME","Main Street Copy"]
OUT=Path("granite_public_keyword_probe.json")

def tokens(text):
    return re.findall(r"[a-z0-9]+",text.lower())
def wer(reference,hypothesis):
    x,y=tokens(reference),tokens(hypothesis)
    prev=list(range(len(y)+1))
    for i,a in enumerate(x,1):
        nxt=[i]
        for j,b in enumerate(y,1):
            nxt.append(min(prev[j]+1,nxt[-1]+1,prev[j-1]+(a!=b)))
        prev=nxt
    return round(prev[-1]/max(1,len(x)),4)

def main():
    from gradio_client import Client,handle_file
    wav=Path("public_terms_16k.wav")
    result={"demo":MODEL_DEMO,"model_revision":"UNVERIFIED_PUBLIC_DEMO",
            "fixture":"PUBLIC_SYNTHETIC_NEW_SENTENCE","reference":REF,
            "private_user_content":False,"conditions":[],"status":"NOT_COMPLETED"}
    try:
        client=Client(MODEL_DEMO,verbose=False)
        for name,hints in [("ordinary",""),("keyword_bias",", ".join(TERMS))]:
            start=time.monotonic()
            try:
                response=client.predict(
                    handle_file(str(wav.resolve())),
                    "Transcribe (punctuated & capitalized)",
                    "transcribe the speech with proper punctuation and capitalization.",
                    "English",hints,api_name="/transcribe")
                output=response if isinstance(response,str) else str(response)
                result["conditions"].append({"setting":name,"keyword_hints":hints,
                  "hypothesis":output,"wer":wer(REF,output),
                  "duration_seconds":round(time.monotonic()-start,3)})
            except Exception as exc:
                result["conditions"].append({"setting":name,"status":"BLOCKED",
                   "error":type(exc).__name__,"detail":str(exc)[:400]})
                break
        result["status"]="PAIRED_DEMO_OBSERVED" if len(result["conditions"])==2 and all("hypothesis" in x for x in result["conditions"]) else "INCOMPLETE"
    except Exception as exc:
        result["status"]="BLOCKED_CONNECT"
        result["error"]=type(exc).__name__
        result["detail"]=str(exc)[:400]
    OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print(json.dumps(result,indent=2,ensure_ascii=False),flush=True)
if __name__=="__main__":
    main()
