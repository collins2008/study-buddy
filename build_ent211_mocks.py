import json
import glob

all_q_files = glob.glob("app/content/ENT 211/*.json")
all_questions = []

for fpath in sorted(all_q_files):
    if "mock_exams" in fpath:
        continue
    data = json.load(open(fpath, encoding="utf-8"))
    for q in data.get("questions", []):
        all_questions.append(q)
    for cs in data.get("case_studies", []):
        for sq in cs.get("sub_questions", []):
            sq_copy = dict(sq)
            sq_copy["question"] = f"[Case Scenario: {cs['scenario'][:160]}...]\n\n{sq['question']}"
            all_questions.append(sq_copy)

print(f"Total ENT 211 questions collected: {len(all_questions)}")

mock1_qs = []
mock2_qs = []

for idx, q in enumerate(all_questions):
    if idx % 2 == 0 and len(mock1_qs) < 30:
        mock1_qs.append(q)
    elif idx % 2 == 1 and len(mock2_qs) < 30:
        mock2_qs.append(q)

remaining = [q for q in all_questions if q not in mock1_qs and q not in mock2_qs]
while len(mock1_qs) < 30 and remaining:
    mock1_qs.append(remaining.pop(0))
while len(mock2_qs) < 30 and remaining:
    mock2_qs.append(remaining.pop(0))

mock_exams = [
    {
        "id": "ent211-mock-1",
        "title": "ENT 211 Entrepreneurship & Innovation — Midterm Examination Mock 1",
        "description": "Standard Nile University midterm exam simulation covering entrepreneurship foundations, value creation loop, Peter Drucker's opportunity principle, Schumpeter's Five New Combinations, Frank Knight's Risk vs Uncertainty, invention vs innovation, five types of innovation, and Nigerian industrial exemplars (Aliko Dangote, Tony Elumelu, Ibukun Awosika).",
        "duration_minutes": 60,
        "total_marks": 60,
        "questions": mock1_qs
    },
    {
        "id": "ent211-mock-2",
        "title": "ENT 211 Entrepreneurship & Innovation — Midterm Examination Mock 2",
        "description": "Advanced analytical exam simulation covering David McClelland's n-Ach, Max Weber's cultural thesis, Everett Hagen's status withdrawal, Harvey Leibenstein's X-inefficiency, Saras Sarasvathy's Effectuation (Bird in Hand, Affordable Loss, Lemonade), Clayton Christensen's Disruptive Innovation, PESTEL environmental scanning, and Six Pillars of Feasibility assessment.",
        "duration_minutes": 60,
        "total_marks": 60,
        "questions": mock2_qs
    }
]

with open("app/content/ENT 211/mock_exams.json", "w", encoding="utf-8") as f:
    json.dump(mock_exams, f, indent=2, ensure_ascii=False)

print(f"Mock 1: {len(mock1_qs)} Qs, Mock 2: {len(mock2_qs)} Qs saved to mock_exams.json!")
