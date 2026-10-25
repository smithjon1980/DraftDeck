#!/usr/bin/env python3
"""Read-only OKF query pilot. No model-generated answers or writes."""
import argparse
import json
import re
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE / "okf"
STOP = {"a", "and", "are", "at", "do", "for", "how", "in", "is", "it", "of", "on", "our", "the", "to", "we", "what", "why"}
MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def tokens(s):
    return [t for t in re.findall(r"[a-z0-9]+", s.casefold()) if t not in STOP]


def load_records(root=ROOT):
    records = []
    for path in sorted((root / "records").glob("*.md")):
        data = path.read_text(encoding="utf-8")
        if not data.startswith("---\n") or "\n---\n" not in data[4:]:
            raise ValueError(f"invalid OKF frontmatter: {path.name}")
        front, body = data[4:].split("\n---\n", 1)
        meta = yaml.safe_load(front)
        if not isinstance(meta, dict) or not meta.get("type"):
            raise ValueError(f"missing concept type: {path.name}")
        sources = meta.get("sources", [])
        if not sources or not all(isinstance(s, dict) and str(s.get("resource", "")).startswith("https://github.com/") for s in sources):
            raise ValueError(f"missing allowed evidence source: {path.name}")
        records.append({
            "id": path.stem, "title": meta.get("title", path.stem),
            "description": meta.get("description", ""), "tags": meta.get("tags", []),
            "status": meta.get("status", "unknown"), "verified": bool(meta.get("verified")),
            "sources": [s["resource"] for s in sources],
            "body": body,
        })
    return records


def lexical(query, records, limit=3):
    q = set(tokens(query))
    if not q:
        return []
    out = []
    for record in records:
        head = tokens(record["title"] + " " + record["description"] + " " + " ".join(record["tags"]))
        body = tokens(record["body"])
        weight = sum((4 * head.count(t)) + body.count(t) for t in q)
        if weight > 0:
            out.append((weight, record))
    out.sort(key=lambda pair: (-pair[0], pair[1]["id"]))
    return [format_record(r, float(score)) for score, r in out[:limit]]


def format_record(rec, score):
    return {"id": rec["id"], "title": rec["title"], "score": score,
            "record_status": rec["status"], "independently_verified": rec["verified"],
            "sources": rec["sources"], "excerpt": rec["description"]}


def semantic(query, records, limit=3):
    # Opt-in only: FastEmbed may download a public model on first use.
    from qdrant_client import QdrantClient, models
    client = QdrantClient(":memory:")
    client.set_model(MODEL)
    texts = [r["title"] + "\n" + r["description"] + "\n" + r["body"] for r in records]
    name = "boss_okf_trial"
    client.create_collection(name, vectors_config=models.VectorParams(
        size=client.get_embedding_size(MODEL), distance=models.Distance.COSINE))
    client.upload_collection(name, vectors=[models.Document(text=t, model=MODEL) for t in texts],
                             ids=list(range(1, len(texts) + 1)))
    result = client.query_points(name, query=models.Document(text=query, model=MODEL), limit=limit).points
    return [format_record(records[p.id - 1], float(p.score)) for p in result]


def main():
    parser = argparse.ArgumentParser(description="BOSS read-only evidence retrieval")
    parser.add_argument("question")
    parser.add_argument("--method", choices=("lexical", "semantic"), default="lexical")
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args()
    if args.limit < 1 or args.limit > 20:
        parser.error("limit must be between 1 and 20")
    records = load_records()
    results = semantic(args.question, records, args.limit) if args.method == "semantic" else lexical(args.question, records, args.limit)
    print(json.dumps({"mode": args.method, "answer_generated": False,
                      "warning": "Index is secondary; verify source status before action.",
                      "results": results}, indent=2))


if __name__ == "__main__":
    main()
