import json,unittest,importlib.util
from pathlib import Path
p=Path("tools/react-layer-gate/check_submission.py")
s=importlib.util.spec_from_file_location("gate",p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
ROOT=Path(".")
def fixture():return json.loads(Path("examples/react-layer-submission/manifest.json").read_text())
class Check(unittest.TestCase):
 def test_valid(self):self.assertEqual(m.inspect(fixture(),ROOT),[])
 def test_python(self):
  x=fixture();x["generator_files"]=["render.py"];self.assertTrue(m.inspect(x,ROOT))
 def test_resubmit_requires_lineage(self):
  x=fixture();x["status"]="RESUBMITTED";self.assertTrue(m.inspect(x,ROOT))
 def test_no_fake_release(self):
  x=fixture();x["release_authorized"]=True;self.assertTrue(m.inspect(x,ROOT))
 def test_art_source_required(self):
  x=fixture();x["art_origin"]="PYTHON";self.assertTrue(m.inspect(x,ROOT))
 def test_missing_source(self):
  x=fixture();x["source_file"]="examples/react-layer-submission/missing.tsx";self.assertTrue(m.inspect(x,ROOT))
if __name__=="__main__":unittest.main()
