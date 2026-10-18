#!/usr/bin/env python3
"""Positive/negative scorer controls are NOT outputs from Muse or any model."""
import json
from pathlib import Path
path = Path(__file__).parent
cases = json.loads((path/'cases.json').read_text())['cases']
with (path/'control_expected.jsonl').open('w') as f:
    for c in cases:
        ref = c['reference']
        row = {'case_id':c['id'], 'decision':ref['decision'],
               'route':ref.get('route', 'NONE'), 'defects':ref.get('required_defects', []),
               'evidence_ids':list(c['evidence'])[:1], 'explanation':'Synthetic control; NOT a model response'}
        f.write(json.dumps(row)+'\n')
with (path/'control_intentionally_bad.jsonl').open('w') as f:
    for c in cases:
        row = {'case_id':c['id'], 'decision':'PASS', 'route':'RAILWAY',
               'defects':[], 'evidence_ids':['made_up_source'], 'explanation':'Deliberately bad control'}
        f.write(json.dumps(row)+'\n')
print('Generated control response files (not model outputs)')
