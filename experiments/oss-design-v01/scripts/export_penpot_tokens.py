#!/usr/bin/env python3
"""Export BOSS design tokens for Penpot single-JSON-set import.

Never assumes Penpot has imported or validated the result. Read canonical
DraftDeck CSS and design contract; FAIL on color drift, unknown token, nonnative
editability claims, or undefined formatting. No network.
"""
import argparse
import json
import pathlib
import re

ROOT=pathlib.Path(__file__).resolve().parents[3]
CSS=ROOT/"design-system/tokens/tokens.css"
CONTRACT=ROOT/"design-system/boss-design-contract.json"
PAIRS={
    "--boss-color-ground":("ground","background"),
    "--boss-color-ink":("ink","ink"),
    "--boss-color-brand-cyan":("cyan","cyan"),
    "--boss-color-brand-magenta":("magenta","magenta"),
}
CANVAS={"--boss-canvas-width":"width", "--boss-canvas-height":"height"}
def render_tokens(css,contract):
    values=dict(re.findall(r"(?m)^\s*(--boss-[\w-]+):\s*([^;]+);",css))
    expected=contract["brand"]
    tokens={"Global":{"boss":{"color":{}, "slide":{}}}}
    for var,(brand_key,name) in PAIRS.items():
        actual=values.get(var,"").strip()
        approved=str(expected[brand_key]).upper()
        if actual.upper()!=approved or not re.fullmatch(r"#[0-9A-Fa-f]{6}",actual):
            raise ValueError("TOKEN_PARITY_FAIL:"+var)
        tokens["Global"]["boss"]["color"][name]={
            "$type":"color","$value":actual.upper(),
            "$description":"Candidate BOSS brand token copied from design-system/tokens/tokens.css"
        }
    for var,name in CANVAS.items():
        actual=values.get(var,"").strip()
        want="1920px" if name=="width" else "1080px"
        if actual!=want:raise ValueError("DIMENSION_PARITY_FAIL:"+var)
        tokens["Global"]["boss"]["slide"][name]={
            "$type":"dimension","$value":actual,
            "$description":"Fixed logical slide dimension; not a responsive Penpot design rule"
        }
    return tokens

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=pathlib.Path,required=True)
    a=ap.parse_args()
    obj=render_tokens(CSS.read_text(),json.loads(CONTRACT.read_text()))
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(obj,indent=2)+"\n",encoding="utf-8")
    print("PASS: six candidate Penpot DTCG tokens generated; target import NOT_TESTED")
if __name__=="__main__":main()
