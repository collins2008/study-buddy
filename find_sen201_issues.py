import json
import glob
import os

shallow_list = []
missing_ww_list = []

for f in sorted(glob.glob('app/content/SEN 201/*.json')):
    if 'mock_exams' in f:
        continue
    with open(f, encoding='utf-8') as fp:
        data = json.load(fp)
    for q in data.get('questions', []):
        expl = q.get('explanation', '').strip()
        qid = q.get('id')
        qtype = q.get('type')
        if len(expl.split()) < 8 or "because it is" in expl.lower():
            shallow_list.append((f, qid, qtype, expl))
        if qtype in ['mcq', 'calculation', 'multi_select'] and q.get('options'):
            ww = q.get('why_wrong', {})
            ans = q.get('answer')
            if isinstance(ans, int):
                for i in range(len(q['options'])):
                    if i != ans and str(i) not in ww:
                        missing_ww_list.append((f, qid, i, q['options'][i], ans, q['options'][ans]))

print(f"Shallow explanations ({len(shallow_list)}):")
for f, qid, qt, expl in shallow_list:
    print(f"  {os.path.basename(f)} [{qid}] ({qt}): {expl}")

print(f"\nMissing why_wrong ({len(missing_ww_list)}):")
for f, qid, opt_i, opt_t, ans_i, ans_t in missing_ww_list:
    print(f"  {os.path.basename(f)} [{qid}] opt {opt_i}: '{opt_t}' (correct: opt {ans_i} '{ans_t}')")
