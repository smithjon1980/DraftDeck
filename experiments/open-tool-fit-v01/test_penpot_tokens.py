"""Offline Penpot DTCG token contract test.

Static format and source parity only. This does NOT prove an actual Penpot
import, edit, export or integration. No network, credentials or paid calls.
"""
import copy
import json
import pathlib
import re
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[2]
TOKENS=ROOT/"experiments/open-tool-fit-v01/penpot-boss-tokens.json"
CANON=ROOT/"design-system/tokens/tokens.css"
PALETTE={
 "ground":("--boss-color-ground","#FFFFFF"),
 "ink":("--boss-color-ink","#000000"),
 "cyan":("--boss-color-brand-cyan","#00BCEB"),
 "magenta":("--boss-color-brand-magenta","#E30074"),
}

def validate(tokens,css):
    failures=[]
    if set(tokens)!={"BOSS"}:
        failures.append("TOKEN_SET_MUST_BE_BOSS")
        return failures
    actual=tokens["BOSS"].get("color",{})
    if set(actual)!=set(PALETTE):
        failures.append("COLOR_TOKEN_SET_MISMATCH")
    for k,(var,expected) in PALETTE.items():
        item=actual.get(k,{})
        if item.get("$type")!="color" or item.get("$value")!=expected:
            failures.append("DTCG_COLOR_MISMATCH:"+k)
        cssmatch=re.search(r"(?m)^\s*"+re.escape(var)+r":\s*([^;]+);",css)
        if not cssmatch or cssmatch.group(1).strip()!=expected:
            failures.append("CANONICAL_CSS_MISMATCH:"+k)
    dim=tokens["BOSS"].get("dimension",{})
    for k,expected in (("slideWidth",1920),("slideHeight",1080)):
        d=dim.get(k,{})
        if d.get("$type")!="dimension" or d.get("$value")!={"value":expected,"unit":"px"}:
            failures.append("DIMENSION_TOKEN_MISMATCH:"+k)
    return failures

class TestPenpotCandidate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(TOKENS.read_text(encoding="utf8"))
        cls.css=CANON.read_text(encoding="utf8")
    def test_penpot_formatted_token_set_parity(self):
        self.assertEqual(validate(self.data,self.css),[])
    def test_unapproved_colors_cannot_pass(self):
        data=copy.deepcopy(self.data)
        data["BOSS"]["color"]["cyan"]["$value"]="#00284D"
        self.assertIn("DTCG_COLOR_MISMATCH:cyan",validate(data,self.css))
    def test_wrong_slide_size_fails(self):
        data=copy.deepcopy(self.data)
        data["BOSS"]["dimension"]["slideWidth"]["$value"]["value"]=1632
        self.assertIn("DIMENSION_TOKEN_MISMATCH:slideWidth",validate(data,self.css))
    def test_missing_color_fails(self):
        data=copy.deepcopy(self.data)
        del data["BOSS"]["color"]["magenta"]
        self.assertIn("COLOR_TOKEN_SET_MISMATCH",validate(data,self.css))
    def test_no_secret_material_or_logo_replacement(self):
        raw=TOKENS.read_text(encoding="utf8")
        for marker in ("API_KEY","Authorization:","private_key","logoSource","waveform"):
            self.assertNotIn(marker,raw)

if __name__=="__main__":
    unittest.main(verbosity=2)
