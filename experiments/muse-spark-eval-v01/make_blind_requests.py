#!/usr/bin/env python3
"""Export public-safe synthetic model inputs without ground truth or filename clues.

The output is JSONL containing base64 PNGs and must stay local, not in GitHub.
No provider calls are made. The image bytes are in the image_data_url field.
"""
import argparse
import base64
import json
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cases', type=Path, default=Path(__file__).with_name('cases.json'))
    ap.add_argument('--output', type=Path, default=Path(__file__).with_name('blind_requests.jsonl'))
    args = ap.parse_args()
    root = args.cases.resolve().parent
    cases = json.loads(args.cases.read_text(encoding='utf-8'))['cases']
    with args.output.open('w', encoding='utf-8') as f:
        for c in cases:
            x = {'case_id':c['id'], 'category':c['category'], 'prompt':c['prompt'],
                 'evidence':c['evidence'], 'response_schema':{
                    'decision':['PASS','FAIL','HOLD'],
                    'route':['GITHUB_ACTIONS','WINDMILL','KAGGLE','RAILWAY','NONE'],
                    'defects':'list of code strings', 'evidence_ids':'list of provided evidence IDs',
                    'explanation':'grounded, concise text'}}
            if 'fixture' in c:
                fp=(root/c['fixture']).resolve()
                if not fp.is_relative_to(root):
                    raise ValueError('Fixture escaped source directory')
                b=fp.read_bytes()
                x['image_data_url']='data:image/png;base64,'+base64.b64encode(b).decode('ascii')
            line=json.dumps(x,separators=(',',':'))
            f.write(line+'\n')
    print('Wrote',len(cases),'blind, synthetic requests. No model calls were made.')

if __name__=='__main__':
    main()
