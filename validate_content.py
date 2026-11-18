import os
import sys
import json

REQUIRED_TOPIC_FIELDS = ['course', 'topic', 'summary', 'key_terms', 'questions', 'case_studies']
REQUIRED_Q_FIELDS = ['id', 'course', 'topic', 'type', 'difficulty', 'tags', 'question', 'explanation']
VALID_TYPES = [
    'mcq', 'multi_select', 'true_false_why', 'type_answer', 'cloze', 'matching',
    'sequencing', 'flashcard', 'explain', 'case_study', 'code_output', 'code_bug',
    'code_fill', 'code_write', 'code_trace', 'html_render', 'calculation', 'diagram_label'
]

def validate_topic_file(file_path):
    print(f"Validating {file_path}...")
    errors = []
    warnings = []

    if not os.path.exists(file_path):
        return [f"File not found: {file_path}"], []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return [f"JSON Parse Error: {e}"], []

    for field in REQUIRED_TOPIC_FIELDS:
        if field not in data:
            errors.append(f"Missing top-level field: '{field}'")

    questions = data.get('questions', [])
    case_studies = data.get('case_studies', [])

    if not questions and not case_studies:
        errors.append("No questions or case studies found in topic!")

    # Check key_terms
    terms = data.get('key_terms', [])
    if len(terms) < 5:
        warnings.append(f"Topic has only {len(terms)} key terms (recommend at least 5)")

    # Validate questions
    seen_ids = set()
    diff_counts = {1: 0, 2: 0, 3: 0, 4: 0}

    for idx, q in enumerate(questions):
        qid = q.get('id', f'unknown-{idx}')
        if qid in seen_ids:
            errors.append(f"Duplicate question id: {qid}")
        seen_ids.add(qid)

        for qf in REQUIRED_Q_FIELDS:
            if qf not in q or q[qf] is None:
                errors.append(f"Q {qid}: Missing required field '{qf}'")

        qtype = q.get('type')
        if qtype not in VALID_TYPES:
            errors.append(f"Q {qid}: Unknown type '{qtype}'")

        diff = q.get('difficulty')
        if diff not in [1, 2, 3, 4]:
            errors.append(f"Q {qid}: Invalid difficulty '{diff}' (must be 1-4)")
        else:
            diff_counts[diff] += 1

        if qtype in ['mcq', 'multi_select', 'code_output']:
            opts = q.get('options', [])
            if not opts or len(opts) < 2:
                errors.append(f"Q {qid} ({qtype}): Options list must have at least 2 choices")
            if 'answer' not in q:
                errors.append(f"Q {qid} ({qtype}): Missing 'answer'")

        # Check code verification for C code questions
        if q.get('code') and q.get('course') == 'COS 201':
            if q.get('verified') is not True:
                warnings.append(f"Q {qid}: C code question not marked verified: true")
            if 'verified_output' not in q or q['verified_output'] == '':
                warnings.append(f"Q {qid}: C code question missing verified_output")

    # Check apply/analyze percentage (Levels 3 & 4)
    total_q = len(questions)
    if total_q > 0:
        high_diff = diff_counts[3] + diff_counts[4]
        high_diff_pct = (high_diff / total_q) * 100
        if high_diff_pct < 30.0:
            warnings.append(f"Higher-order difficulty (L3-L4) is {high_diff_pct:.1f}% (target >= 30%)")

    return errors, warnings

def validate_all(content_root):
    total_errors = 0
    total_warnings = 0
    total_questions = 0

    index_path = os.path.join(content_root, 'index.json')
    if not os.path.exists(index_path):
        print("ERROR: content/index.json does not exist!")
        return 1

    with open(index_path, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    for course in index_data.get('courses', []):
        ccode = course.get('code')
        for topic in course.get('topics', []):
            rel_file = topic.get('file')
            full_path = os.path.join(content_root, rel_file)
            if not os.path.exists(full_path):
                continue
            errs, warns = validate_topic_file(full_path)
            if errs:
                print(f"[FAIL] {rel_file}: {len(errs)} ERRORS")
                for e in errs:
                    print(f"   - {e}")
                total_errors += len(errs)
            else:
                print(f"[PASS] {rel_file}: ALL CHECKS PASSED")

            if warns:
                for w in warns:
                    print(f"   [WARN] {w}")
                total_warnings += len(warns)

            # Count questions
            try:
                with open(full_path, 'r', encoding='utf-8') as tf:
                    t_data = json.load(tf)
                    total_questions += len(t_data.get('questions', []))
            except:
                pass

    print(f"\nSummary: {total_questions} questions verified. {total_errors} errors, {total_warnings} warnings.")
    return total_errors

if __name__ == '__main__':
    base_dir = r"c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content"
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    res = validate_all(base_dir)
    sys.exit(0 if res == 0 else 1)
