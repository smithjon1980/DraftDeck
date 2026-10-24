#!/usr/bin/env python3
"""Static-only guard. Does not draw, render or compile slide layers."""
import json, re, sys
from pathlib import Path
def inspect(m,root):
 e=[]
 if m.get("contract")!="BOSS-REACT-LAYERS-V1": e.append("contract")
 if m.get("status") not in {"SUBMITTED","REJECTED","RESUBMITTED","TECHNICALLY_ACCEPTED","HUMAN_ACCEPTED"}: e.append("status")
 if not m.get("candidate_id"):e.append("candidate_id")
 if m.get("status")=="RESUBMITTED" and (not m.get("supersedes") or m.get("supersedes")==m.get("candidate_id") or not m.get("change_summary")):e.append("resubmit ancestry and correction required")
 src=m.get("source_file","")
 if not isinstance(src,str) or not src.endswith(".tsx") or src.startswith("/") or ".." in Path(src).parts:e.append("source must be relative .tsx");return e
 p=(root/src)
 if not p.is_file():e.append("source missing");return e
 s=p.read_text(encoding="utf-8")
 for token in ("ArtLayer","StoryLayer","TextLayer"):
  if not re.search(r"(?:function|const|export\s+function)\s+"+token+r"\b",s):e.append("missing React component "+token)
  if not re.search(r"<"+token+r"\b",s):e.append("not assembled "+token)
 if not re.search(r"className\s*=\s*[\"'`]",s):e.append("missing Tailwind className")
 if not re.search(r"\b(?:absolute|relative|grid|flex|inset-0|w-full|h-full|text-|border-)\b",s):e.append("missing Tailwind layout utilities")
 if re.search(r"<text(?:\s|>)|dangerouslySetInnerHTML|data:image/|toDataURL\(|<canvas\b",s,re.I):e.append("flattened or SVG text/canvas forbidden")
 for f in m.get("generator_files",[]):
  if not isinstance(f,str) or f.lower().endswith(".py"):e.append("Python art/story generator forbidden")
 if m.get("art_origin")!="REACT_TSX" or m.get("story_origin")!="REACT_TSX" or m.get("text_origin")!="NATIVE_HTML":e.append("layer origin mismatch")
 if m.get("human_approved") is not False and m.get("status")!="HUMAN_ACCEPTED":e.append("human approval cannot be inferred")
 if m.get("release_authorized") is not False:e.append("release cannot be authorized by structural submission")
 return e
if __name__=="__main__":
 try:
  manifest=json.loads(Path(sys.argv[1]).read_text())
  errors=inspect(manifest,Path(sys.argv[2]))
 except (IndexError,ValueError,OSError) as x:print("FAIL",x);sys.exit(2)
 print("PASS: structural React/Tailwind source gate; visual/human review NOT TESTED" if not errors else "FAIL: "+"; ".join(errors))
 sys.exit(bool(errors))
