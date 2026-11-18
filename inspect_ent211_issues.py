import json

fnames = [
    'app/content/ENT 211/entrepreneurship_core_concepts.json',
    'app/content/ENT 211/entrepreneurship_theories.json'
]

ids_to_check = ['ent211-fnd-013', 'ent211-fnd-014', 'ent211-thy-015']

for fname in fnames:
    with open(fname, encoding='utf-8') as f:
        d = json.load(f)
    for q in d['questions']:
        if q['id'] in ids_to_check:
            print(f"=== {q['id']} ===")
            print("Question:", q['question'])
            print("Answer:", q['options'][q['answer']])
            print("Current expl:", q['explanation'])
