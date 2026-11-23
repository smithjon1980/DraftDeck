import pathlib
import unittest
import json
import sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from export_penpot_tokens import render_tokens, CSS, CONTRACT

class PenpotInteropTests(unittest.TestCase):
    def setUp(self):
        self.css=CSS.read_text()
        self.contract=json.loads(CONTRACT.read_text())
    def test_all_canonical_tokens_exported_exactly(self):
        result=render_tokens(self.css,self.contract)
        brand=result["Global"]["boss"]["color"]
        self.assertEqual(brand["background"]["$value"],"#FFFFFF")
        self.assertEqual(brand["ink"]["$value"],"#000000")
        self.assertEqual(brand["cyan"]["$value"],"#00BCEB")
        self.assertEqual(brand["magenta"]["$value"],"#E30074")
        self.assertTrue(all(v["$type"]=="color" and "$description" in v for v in brand.values()))
        slide=result["Global"]["boss"]["slide"]
        self.assertEqual(slide["width"]["$value"],"1920px")
        self.assertEqual(slide["height"]["$value"],"1080px")
    def test_missing_cyan_rejected(self):
        with self.assertRaisesRegex(ValueError,"TOKEN_PARITY_FAIL"):
            render_tokens(self.css.replace("--boss-color-brand-cyan: #00BCEB;",""),self.contract)
    def test_wrong_magenta_rejected(self):
        with self.assertRaisesRegex(ValueError,"TOKEN_PARITY_FAIL"):
            render_tokens(self.css.replace("#E30074","#A44411"),self.contract)
    def test_wrong_dimensions_rejected(self):
        with self.assertRaisesRegex(ValueError,"DIMENSION_PARITY_FAIL"):
            render_tokens(self.css.replace("--boss-canvas-width: 1920px;","--boss-canvas-width: 1280px;"),self.contract)
    def test_contract_mismatch_rejected(self):
        self.contract["brand"]["cyan"]="#00FF00"
        with self.assertRaisesRegex(ValueError,"TOKEN_PARITY_FAIL"):
            render_tokens(self.css,self.contract)

if __name__=="__main__":unittest.main()
