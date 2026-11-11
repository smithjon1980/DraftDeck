#!/usr/bin/env python3
"""Review-only BOSS diagram model-response gate. No model calls or publication.

JSON Schema verifies structure. The checks here validate literal IDs and routing.
They do NOT assert diagram compilation, source-truth, MECE coverage, visual
quality, rendered editability, external ISO/OMG conformance, or human approval.
"""
import copy
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

BASE = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((BASE / name).read_text(encoding="utf-8"))


def inspect_one(doc, router, schema):
    errors = []
    check = Draft202012Validator(schema)
    errors.extend("SCHEMA:" + error.message for error in check.iter_errors(doc))
    route = next((r for r in router["routes"] if r["intent"] == doc.get("intent")), None)
    if not route:
        errors.append("NO_ROUTE")
    else:
        if doc.get("semantic_standard") != route["semantic_standard"]:
            errors.append("SEMANTIC_ROUTING_MISMATCH")
        if doc.get("renderer") != route["renderer"]:
            errors.append("RENDERER_ROUTING_MISMATCH")
    known_refs = set(doc.get("source_refs", []))
    ids = [n.get("id") for n in doc.get("nodes", []) if isinstance(n, dict)]
    if len(ids) != len(set(ids)):
        errors.append("DUPLICATE_NODE_ID")
    for n in doc.get("nodes", []):
        if not isinstance(n, dict):
            continue
        if not set(n.get("evidence_refs", [])).issubset(known_refs):
            errors.append("FABRICATED_NODE_EVIDENCE_ID:" + str(n.get("id")))
    for edge in doc.get("edges", []):
        if not isinstance(edge, dict):
            continue
        if edge.get("from") not in ids or edge.get("to") not in ids:
            errors.append("UNRESOLVED_EDGE_ENDPOINT")
        if not set(edge.get("evidence_refs", [])).issubset(known_refs):
            errors.append("FABRICATED_EDGE_EVIDENCE_ID")
    source_code = doc.get("source_code", "")
    if any(token in source_code.lower() for token in ["<script", "<iframe", "<svg", "<html"]):
        errors.append("UNAPPROVED_INLINE_MARKUP")
    if doc.get("intent") == "mece_issue_tree" and doc.get("mece_verified"):
        errors.append("MECE_CANNOT_SELF_ATTEST")
    return sorted(set(errors))


def test_pack():
    router = load("diagram-routing.v0.1.json")
    schema = load("diagram-spec.schema.json")
    positive = load("diagram-spec.synthetic.example.json")
    Draft202012Validator.check_schema(schema)
    assert len(router["routes"]) >= 9
    allowed = [r["intent"] for r in router["routes"]]
    assert len(allowed) == len(set(allowed)), "duplicate route"
    assert not inspect_one(positive, router, schema), inspect_one(positive, router, schema)
    controls = []
    def defect(label, change, expected):
        d = copy.deepcopy(positive)
        change(d)
        errors = inspect_one(d, router, schema)
        assert expected in errors, (label, errors)
        controls.append(label)
    defect("unlisted_renderer",lambda x:x.update(renderer="unknown"),"RENDERER_ROUTING_MISMATCH")
    defect("fabricated_node_evidence",lambda x:x["nodes"][0].update(evidence_refs=["EVIDENCE_NOT_PROVIDED"]),"FABRICATED_NODE_EVIDENCE_ID:A")
    defect("broken_edge",lambda x:x["edges"][0].update(to="UNDECLARED"),"UNRESOLVED_EDGE_ENDPOINT")
    defect("wrong_semantics",lambda x:x.update(semantic_standard="UML_2_5_1_SEQUENCE"),"SEMANTIC_ROUTING_MISMATCH")
    defect("inline_script",lambda x:x.update(source_code="<script>alert('no')</script>"),"UNAPPROVED_INLINE_MARKUP")
    print(json.dumps({"status":"PASS","synthetic_valid_example":1,"negative_controls_detected":controls,
                      "diagram_compilation":"NOT_TESTED","visual_review":"NOT_TESTED",
                      "model_inference":"NOT_EXECUTED","standards_conformance":"NOT_ESTABLISHED"}))


if __name__ == "__main__":
    try:
        test_pack()
    except Exception as exc:
        print("FAIL: " + str(exc), file=sys.stderr)
        raise SystemExit(1)
