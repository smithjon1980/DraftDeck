# BOSS OKF Knowledge-Retrieval Qualification — candidate

**Status:** Experimental. **Authority:** Read-only. **Production:** HOLD.

## Five qualification gates

1. **Source ledger:** Record only public-safe decisions and evidence as Google OKF v0.2 Markdown concepts; maintain source URLs, lifecycle status, and explicit uncertainty.
2. **Deterministic baseline:** Query the records using an auditable token-ranking method and return source locations, not generated answers.
3. **Semantic challenger:** Compare local FastEmbed + Qdrant (in-memory, no server or credentials) against the baseline on the same questions.
4. **Evidence tests:** Evaluate top-1 retrieval, missing-source refusal, contradiction handling, and no inferred release approval; review before adopting semantic retrieval.
5. **ChatGPT access:** After review, design authenticated read-only retrieval through an approved connector/tool. This candidate does not wire a live ChatGPT connector.

## Scope and safety

- GitHub remains the record of source truth. OKF is an **index**, not a new approval authority.
- The public repo may contain **only public-safe** records. Do not add private chats, transcripts, credentials, human approver identities, manuscripts, tenant data, or sensitive operational evidence.
- Source references do not constitute human review. We intentionally omit `verified` until independent confirmation.
- Indexes may go stale; production status must be rechecked at the source before consequential use.
- No endpoint, daemon, secrets, customer data, deployment, production route, or expensive service is created.
- Work is isolated from Render private worker qualification (draft PR #107).

## Run the deterministic test

```bash
python -m pip install -r experiments/boss-knowledge-pilot/requirements.txt
python -m unittest discover -s experiments/boss-knowledge-pilot -p 'test_*.py' -v
python experiments/boss-knowledge-pilot/query.py "Why is OpenBot production integration on hold?"
```

## Optional semantic experiment (local CPU, model download on first run)

```bash
python -m pip install "qdrant-client[fastembed]>=1.14.2"
python experiments/boss-knowledge-pilot/query.py "What tests still block deployment?" --method semantic
```

The semantic runner uses Qdrant in-memory. It downloads an open embedding model when run for the first time; model acquisition and model/license reviews are separate admission gates. It is **not** run automatically in the baseline CI.

## Current source corpus

- [PR #95](okf/records/pr-95.md): OpenBot/OpenDots cross-policy synthetic trial, reproduced bypass, draft hold.
- [PR #106](okf/records/pr-106.md): merged health-only Render gateway and isolated CI evidence.
- [PR #107](okf/records/pr-107.md): draft private SVG worker qualification, live Render test unverified.

## Acceptance criteria

- Pass schema and source-link checks for every seeded concept.
- Retrieve PR #95 for the direct-route bypass and PR #107 for private worker qualification.
- Never present `merged`, `healthy`, or `CI pass` as authorization for protected production execution.
- Require an external source URL for each answer-worthy record; return no records for unrelated questions rather than fabricate evidence.
- Compare an explicit golden-question set before recommending the semantic mode.
- Preserve current React/Tailwind, Windmill, n8n, Railway, Render and GitHub Actions operations.

Sources: [current OKF v0.2 specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md); [Qdrant local mode](https://github.com/qdrant/qdrant-client); [FastEmbed/Qdrant guide](https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/).
