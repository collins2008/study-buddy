import json
import glob
import os

for f in sorted(glob.glob('app/content/IFT 203/*.json')):
    if 'mock_exams' in f:
        continue
    with open(f, encoding='utf-8') as fp:
        d = json.load(fp)
    for q in d['questions']:
        expl = q.get('explanation', '').strip()
        if len(expl.split()) < 8 or 'because it is' in expl.lower():
            print(f"{os.path.basename(f)} | {q['id']} | {q['question'][:40]} | {expl}")
