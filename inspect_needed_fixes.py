import json

fnames = [
    'app/content/COS 201/loops_iteration.json',
    'app/content/COS 201/midterm_past_questions.json',
    'app/content/COS 201/operators_expressions.json',
    'app/content/COS 201/data_types_variables.json'
]

ids_to_check = [
    'cos201-dt-010', 'cos201-lp-004', 'cos201-mid-003', 'cos201-mid-007',
    'cos201-mid-011', 'cos201-mid-017', 'cos201-mid-023', 'cos201-mid-025',
    'cos201-mid-033', 'cos201-mid-039', 'cos201-op-001', 'cos201-op-003',
    'cos201-op-008', 'cos201-op-009', 'cos201-op-011', 'cos201-op-013'
]

for fname in fnames:
    with open(fname, encoding='utf-8') as f:
        d = json.load(f)
    for q in d['questions']:
        if q['id'] in ids_to_check:
            print(f"=== {q['id']} ({fname}) ===")
            code = q.get('code')
            if not code:
                print("Question:", q.get('question'))
            else:
                print("Code:\n", code)
            print("Options:", q.get('options'))
            print("Answer:", q.get('answer'))
            print("Why Wrong:", q.get('why_wrong'))
            print()
