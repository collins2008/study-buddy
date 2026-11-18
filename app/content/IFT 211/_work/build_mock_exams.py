import json
import os

def build_mock_exams():
    content_dir = r'c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content\IFT 211'
    topic_files = [
        'number_systems.json',
        'arithmetic_complements.json',
        'bcd_gray_ascii.json',
        'boolean_algebra_theorems.json',
        'logic_gates_universal.json',
        'combinational_circuits.json',
        'karnaugh_maps.json',
        'past_exam_synthesis.json'
    ]

    q_dict = {}
    for tf in topic_files:
        path = os.path.join(content_dir, tf)
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for q in data.get('questions', []):
                q['topic_slug'] = tf.replace('.json', '')
                q_dict[q['id']] = q

    # Mock Exam 1: 30 questions
    m1_qids = [
        # Number Systems (4)
        "ift211-ns-001", "ift211-ns-005", "ift211-ns-009", "ift211-ns-013",
        # Arithmetic & Complements (4)
        "ift211-ac-001", "ift211-ac-004", "ift211-ac-007", "ift211-ac-011",
        # BCD, Gray & ASCII (4)
        "ift211-cd-001", "ift211-cd-003", "ift211-cd-006", "ift211-cd-009",
        # Boolean Algebra (4)
        "ift211-ba-001", "ift211-ba-004", "ift211-ba-007", "ift211-ba-010",
        # Logic Gates & Universal (4)
        "ift211-lg-001", "ift211-lg-003", "ift211-lg-006", "ift211-lg-010",
        # Combinational Circuits (4)
        "ift211-cc-001", "ift211-cc-004", "ift211-cc-007", "ift211-cc-010",
        # Karnaugh Maps (3)
        "ift211-km-001", "ift211-km-003", "ift211-km-005",
        # Past Exam Synthesis (3)
        "ift211-pe-001", "ift211-pe-004", "ift211-pe-006"
    ]

    # Mock Exam 2: 30 distinct questions
    m2_qids = [
        # Number Systems (4)
        "ift211-ns-003", "ift211-ns-007", "ift211-ns-011", "ift211-ns-015",
        # Arithmetic & Complements (4)
        "ift211-ac-002", "ift211-ac-005", "ift211-ac-008", "ift211-ac-012",
        # BCD, Gray & ASCII (4)
        "ift211-cd-002", "ift211-cd-004", "ift211-cd-008", "ift211-cd-010",
        # Boolean Algebra (4)
        "ift211-ba-002", "ift211-ba-005", "ift211-ba-008", "ift211-ba-009",
        # Logic Gates & Universal (4)
        "ift211-lg-002", "ift211-lg-004", "ift211-lg-007", "ift211-lg-009",
        # Combinational Circuits (4)
        "ift211-cc-002", "ift211-cc-005", "ift211-cc-009", "ift211-cc-011",
        # Karnaugh Maps (3)
        "ift211-km-002", "ift211-km-004", "ift211-km-008",
        # Past Exam Synthesis (3)
        "ift211-pe-002", "ift211-pe-003", "ift211-pe-007"
    ]

    # Verify all IDs exist
    for qid in m1_qids:
        if qid not in q_dict:
            raise KeyError(f"Mock 1 Question ID not found: {qid}")
    for qid in m2_qids:
        if qid not in q_dict:
            raise KeyError(f"Mock 2 Question ID not found: {qid}")

    exam_payload = {
        "course": "IFT 211",
        "title": "Digital Logic and Design — Mock Examination Series",
        "exams": [
            {
                "id": "ift211-mock-01",
                "title": "Mock Exam Alpha: Full 60-Mark Final Examination Standard Simulation",
                "description": "Comprehensive simulation reflecting the official Nile University First Semester Final Exam format. Features 30 multi-part calculation and design questions weighted across binary/hex conversions, signed 2's complement arithmetic, ASCII byte stream decoding, universal NAND/NOR synthesis, full adders, ripple delays, and K-map 4-corner wraps.",
                "duration_minutes": 90,
                "total_marks": 60,
                "passing_score": 30,
                "question_count": len(m1_qids),
                "questions": [q_dict[qid] for qid in m1_qids]
            },
            {
                "id": "ift211-mock-02",
                "title": "Mock Exam Beta: Advanced Challenge & Multi-Topic Mastery Simulation",
                "description": "High-rigor exam simulation emphasizing analytical speed and edge-case mastery: 1's complement end-around carries, fractional binary conversions, multi-variable De Morgan theorems, priority encoder arbitration, signed ALU overflow flags (V = C7 ⊕ C8), and BCD don't-care K-map optimization.",
                "duration_minutes": 90,
                "total_marks": 60,
                "passing_score": 30,
                "question_count": len(m2_qids),
                "questions": [q_dict[qid] for qid in m2_qids]
            }
        ]
    }

    out_file = os.path.join(content_dir, 'mock_exams.json')
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(exam_payload, f, indent=2)

    print(f"Successfully generated {out_file} with 2 full exams ({len(m1_qids)} Qs and {len(m2_qids)} Qs).")

if __name__ == '__main__':
    build_mock_exams()
