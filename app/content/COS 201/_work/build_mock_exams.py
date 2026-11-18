import json
import os

def build_mock_exams():
    content_dir = r'c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content\COS 201'
    topic_files = [
        'data_types_variables.json',
        'operators_expressions.json',
        'control_flow_selection.json',
        'loops_iteration.json',
        'functions_modular.json',
        'arrays_1d_2d.json',
        'pointers_memory.json',
        'strings_char_arrays.json',
        'midterm_past_questions.json'
    ]

    all_questions = []
    for tf in topic_files:
        path = os.path.join(content_dir, tf)
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for q in data.get('questions', []):
                q['topic_slug'] = tf.replace('.json', '')
                all_questions.append(q)

    # Mock Exam 1: 40 questions
    m1_qids = [
        # Topic 1: Data types & variables (4)
        "cos201-dt-001", "cos201-dt-006", "cos201-dt-011", "cos201-dt-020",
        # Topic 2: Operators & expressions (4)
        "cos201-op-001", "cos201-op-007", "cos201-op-012", "cos201-op-021",
        # Topic 3: Control flow (4)
        "cos201-cf-001", "cos201-cf-005", "cos201-cf-009", "cos201-cf-018",
        # Topic 4: Loops (4)
        "cos201-lp-002", "cos201-lp-006", "cos201-lp-010", "cos201-lp-015",
        # Topic 5: Functions (4)
        "cos201-fn-001", "cos201-fn-005", "cos201-fn-009", "cos201-fn-013",
        # Topic 6: Arrays (4)
        "cos201-arr-001", "cos201-arr-005", "cos201-arr-010", "cos201-arr-014",
        # Topic 7: Pointers (4)
        "cos201-ptr-001", "cos201-ptr-005", "cos201-ptr-010", "cos201-ptr-014",
        # Topic 8: Strings (4)
        "cos201-str-001", "cos201-str-005", "cos201-str-009", "cos201-str-013",
        # Topic 9: Actual Midterm Past Questions (8)
        "cos201-mid-003", "cos201-mid-005", "cos201-mid-007", "cos201-mid-015",
        "cos201-mid-019", "cos201-mid-023", "cos201-mid-031", "cos201-mid-039"
    ]

    # Mock Exam 2: 40 questions (distinct set)
    m2_qids = [
        # Topic 1: Data types & variables (4)
        "cos201-dt-003", "cos201-dt-009", "cos201-dt-014", "cos201-dt-025",
        # Topic 2: Operators & expressions (4)
        "cos201-op-003", "cos201-op-009", "cos201-op-016", "cos201-op-024",
        # Topic 3: Control flow (4)
        "cos201-cf-003", "cos201-cf-007", "cos201-cf-014", "cos201-cf-017",
        # Topic 4: Loops (4)
        "cos201-lp-004", "cos201-lp-008", "cos201-lp-014", "cos201-lp-018",
        # Topic 5: Functions (4)
        "cos201-fn-003", "cos201-fn-007", "cos201-fn-010", "cos201-fn-012",
        # Topic 6: Arrays (4)
        "cos201-arr-003", "cos201-arr-008", "cos201-arr-012", "cos201-arr-016",
        # Topic 7: Pointers (4)
        "cos201-ptr-003", "cos201-ptr-008", "cos201-ptr-012", "cos201-ptr-016",
        # Topic 8: Strings (4)
        "cos201-str-003", "cos201-str-007", "cos201-str-011", "cos201-str-015",
        # Topic 9: Actual Midterm Past Questions (8)
        "cos201-mid-009", "cos201-mid-011", "cos201-mid-017", "cos201-mid-021",
        "cos201-mid-025", "cos201-mid-027", "cos201-mid-033", "cos201-mid-035"
    ]

    q_lookup = {q['id']: q for q in all_questions}

    mock1_questions = []
    for qid in m1_qids:
        if qid in q_lookup:
            mock1_questions.append(q_lookup[qid])
        else:
            raise KeyError(f"Error: {qid} not found in q_lookup")

    mock2_questions = []
    for qid in m2_qids:
        if qid in q_lookup:
            mock2_questions.append(q_lookup[qid])
        else:
            raise KeyError(f"Error: {qid} not found in q_lookup")

    mock_exams_data = {
        "course": "COS 201",
        "title": "Computer Programming I (C Language)",
        "exams": [
            {
                "id": "cos201-mock-01",
                "title": "Mock Exam 1: Nile Midterm Official Blueprint Simulator",
                "description": "Standard 40-question midterm simulation adhering to Nile University Department of Software Engineering standards. Covers all 9 topics with proportional weighting.",
                "duration_minutes": 60,
                "total_marks": 40,
                "passing_score": 20,
                "question_count": len(mock1_questions),
                "questions": mock1_questions
            },
            {
                "id": "cos201-mock-02",
                "title": "Mock Exam 2: Deep Tracing & Pointer Mastery Challenge",
                "description": "High-intensity 40-question exam emphasizing code output prediction, pointer indirection, array indexing, and subtle C pitfalls.",
                "duration_minutes": 60,
                "total_marks": 40,
                "passing_score": 24,
                "question_count": len(mock2_questions),
                "questions": mock2_questions
            }
        ]
    }

    out_file = os.path.join(content_dir, 'mock_exams.json')
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(mock_exams_data, f, indent=2)

    print(f"Successfully generated {out_file} with {len(mock_exams_data['exams'])} full mock exams (40 questions each, total {len(mock1_questions) + len(mock2_questions)}).")

if __name__ == '__main__':
    build_mock_exams()
