#!/usr/bin/env python3
"""Offline scoring for candidate model responses; never calls a model or network."""
import argparse
import json
from collections import Counter
from pathlib import Path

DECISIONS = {'PASS', 'FAIL', 'HOLD'}
ROUTES = {'GITHUB_ACTIONS', 'WINDMILL', 'KAGGLE', 'RAILWAY', 'NONE'}


def score(cases, responses):
    expected_ids = {c['id'] for c in cases}
    unknown = sorted(set(responses) - expected_ids)
    details = []
    totals = Counter()
    for c in cases:
        pred = responses.get(c['id'])
        valid = isinstance(pred, dict) and pred.get('decision') in DECISIONS
        if valid:
            valid = isinstance(pred.get('evidence_ids'), list) and isinstance(pred.get('defects'), list)
        if valid and c['category'] == 'routing':
            valid = pred.get('route') in ROUTES
        refusal = pred is None or (isinstance(pred, dict) and pred.get('decision') in (None, 'REFUSE', 'ABSTAIN'))
        if refusal:
            totals['refusals_or_missing'] += 1
        if not valid:
            totals['invalid_or_missing'] += 1
        ref = c['reference']
        allowed_evidence = set(c.get('evidence', {}).keys())
        provided = set(pred.get('evidence_ids', [])) if valid and all(isinstance(z, str) for z in pred.get('evidence_ids', [])) else set()
        unsupported = sorted(provided - allowed_evidence)
        absent_proof = bool(allowed_evidence and not provided)
        outcome = bool(valid and pred['decision'] == ref['decision'])
        route_ok = c['category'] != 'routing' or (valid and pred.get('route') == ref.get('route'))
        defects = set(pred.get('defects', [])) if valid and all(isinstance(z, str) for z in pred.get('defects', [])) else set()
        required_defects = set(ref.get('required_defects', []))
        defect_ok = required_defects.issubset(defects)
        grounded = not unsupported and not absent_proof
        passed = outcome and route_ok and defect_ok and grounded
        if not passed:
            totals['failed'] += 1
        if valid and pred['decision'] == 'PASS' and ref['decision'] != 'PASS':
            totals['false_passes'] += 1
        if unsupported:
            totals['fabricated_evidence_ids'] += 1
        if valid and outcome:
            totals['decision_correct'] += 1
        if c['category'] == 'routing' and route_ok:
            totals['routing_correct'] += 1
        if passed:
            totals['passed'] += 1
        totals['by_category_' + c['category']] += 1
        details.append({'id': c['id'], 'category': c['category'], 'pass': passed,
                        'expected': ref['decision'], 'actual': pred.get('decision') if isinstance(pred, dict) else None,
                        'route_ok': route_ok, 'missing_required_defects': sorted(required_defects - defects),
                        'unsupported_evidence_ids': unsupported, 'evidence_missing': absent_proof,
                        'refusal_or_missing': refusal})
    n = len(cases)
    return {'status': 'TEST_ONLY_NO_MODEL_INFERENCE', 'count': n,
            'passed': totals['passed'], 'accuracy_all_cases': round(totals['passed'] / n, 4) if n else None,
            'decision_correct': totals['decision_correct'],
            'false_passes': totals['false_passes'],
            'refusals_or_missing': totals['refusals_or_missing'],
            'fabricated_evidence_ids': totals['fabricated_evidence_ids'],
            'invalid_or_missing': totals['invalid_or_missing'],
            'unknown_case_ids': unknown, 'details': details}


def load_responses(path):
    records = {}
    for i, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            continue
        x = json.loads(line)
        if not isinstance(x, dict) or 'case_id' not in x:
            raise ValueError('line %s missing case_id' % i)
        if x['case_id'] in records:
            raise ValueError('duplicate case_id %r' % x['case_id'])
        records[x['case_id']] = x
    return records


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--cases', type=Path, default=Path(__file__).with_name('cases.json'))
    p.add_argument('--predictions', type=Path, required=True)
    p.add_argument('--output', type=Path)
    p.add_argument('--require-all-pass', action='store_true')
    args = p.parse_args()
    cases = json.loads(args.cases.read_text(encoding='utf-8'))['cases']
    report = score(cases, load_responses(args.predictions))
    s = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(s + '\n', encoding='utf-8')
    print(s)
    if args.require_all_pass and (report['passed'] != report['count'] or report['unknown_case_ids']):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
