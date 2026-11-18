import json
import glob
import os

shallow_list = []
missing_ww_list = []

for f in sorted(glob.glob('app/content/COS 201/*.json')):
    if 'mock_exams' in f:
        continue
    with open(f, encoding='utf-8') as fp:
        data = json.load(fp)
    for q in data.get('questions', []):
        expl = q.get('explanation', '').strip()
        qid = q.get('id')
        qtype = q.get('type')
        if len(expl.split()) < 10 or 'because it is' in expl.lower():
            shallow_list.append((f, qid, qtype, expl))
        if qtype in ['mcq', 'code_output', 'code_bug'] and q.get('options'):
            ww = q.get('why_wrong', {})
            ans = q.get('answer')
            for i in range(len(q['options'])):
                if i != ans and str(i) not in ww:
                    missing_ww_list.append((f, qid, i, q['options'][i]))

print(f"Shallow explanations count: {len(shallow_list)}")
for item in shallow_list[:15]:
    print(f"  {os.path.basename(item[0])} [{item[1]}]: {item[3]}")

print(f"\nMissing why_wrong count: {len(missing_ww_list)}")
for item in missing_ww_list:
    fname, qid, opt_idx, opt_text = item
    with open(fname, encoding='utf-8') as fp:
        d = json.load(fp)
    q = next(x for x in d['questions'] if x['id'] == qid)
    print(f"  {os.path.basename(fname)} [{qid}] q: '{q['question'][:50]}...' opt {opt_idx}: '{opt_text}' (ans={q['answer']}: '{q['options'][q['answer']]}')")
