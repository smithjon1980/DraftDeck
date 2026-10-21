# BOSS V4 Work Commission schema — candidate

Derived from Section 6 of `doctrine/BOSS_V4_CONSULTING_AGENCY_ARCHITECTURE_CANDIDATE.md`. The JSON Schema uses draft 2020-12, consistent with DraftDeck's existing schema convention.

## Run structural checks

```bash
python -m pip install 'jsonschema>=4.18,<5'
python tests/work-commission-v4/test_schema.py
```

Fixtures: one unexecuted, synthetic Main Street Copy draft and six intentionally invalid specimens. Tests establish shape validation only; they are **not** Section 14 runtime acceptance tests.

## Trust boundary

- `authority_ref` and `inputs[].authorized` are untrusted assertions, not authenticated decisions or evidence of rights.
- `HUMAN-SCOPE-APPROVAL-PENDING` is intentionally valid only as a *draft reference*, not a permission token.
- `sandbox://candidate-output` is an illustrative pseudolocation, not a real write grant.
- A structurally valid payload can still be unauthorized, out of scope, wrong for its tenant, factually unsupported, or unsafe.
- Never promote `INSPECTED_ACCEPTABLE` into human release authorization without a separately authenticated, digest-bound decision.
- Commission state transitions, permission allowlists, source custody, actual file content, idempotency, recovery, tenant isolation, and reviewer identity need runtime enforcement.
- No CI wiring or production behavior is installed by this candidate.
