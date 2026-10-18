import json
import unittest
from pathlib import Path
from evaluate import load_responses, score

BASE = Path(__file__).parent
CASES = json.loads((BASE / 'cases.json').read_text())['cases']

class TestScorer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Generate deterministic controls in memory if not present.
        expected = {}
        bad = {}
        for c in CASES:
            ref = c['reference']
            expected[c['id']] = {'case_id':c['id'], 'decision':ref['decision'],
                 'route':ref.get('route','NONE'), 'defects':ref.get('required_defects', []),
                 'evidence_ids':list(c['evidence'])[:1]}
            bad[c['id']] = {'case_id':c['id'], 'decision':'PASS', 'route':'RAILWAY',
                 'defects':[], 'evidence_ids':['made_up_source']}
        cls.expected = expected
        cls.bad = bad

    def test_expected_oracle_controls_pass(self):
        out = score(CASES, self.expected)
        self.assertEqual(out['passed'], len(CASES))
        self.assertEqual(out['false_passes'], 0)

    def test_bad_control_does_not_pass(self):
        out = score(CASES, self.bad)
        self.assertEqual(out['passed'], 0)
        self.assertGreater(out['false_passes'], 0)
        self.assertEqual(out['fabricated_evidence_ids'], len(CASES))

    def test_refusal_not_success(self):
        preds = dict(self.expected)
        preds['V01'] = {'case_id':'V01', 'decision':'REFUSE', 'defects':[], 'evidence_ids':[]}
        out = score(CASES, preds)
        self.assertEqual(out['passed'], len(CASES)-1)
        self.assertEqual(out['refusals_or_missing'], 1)

    def test_refusal_not_even_when_gold_hold(self):
        preds = dict(self.expected)
        preds['R05'] = {'case_id':'R05', 'decision':'REFUSE', 'route':'NONE',
                        'defects':[], 'evidence_ids':[]}
        self.assertEqual(score(CASES, preds)['passed'], len(CASES)-1)

    def test_no_response_not_success(self):
        preds = dict(self.expected)
        preds.pop('E01')
        out = score(CASES, preds)
        self.assertEqual(out['passed'], len(CASES)-1)
        self.assertEqual(out['refusals_or_missing'], 1)

if __name__ == '__main__':
    unittest.main()
