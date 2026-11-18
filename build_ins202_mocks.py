import json
import glob

# Load all questions from INS 202 topics
all_q_files = glob.glob("app/content/INS 202/*.json")
all_questions = []

for fpath in sorted(all_q_files):
    if "mock_exams" in fpath:
        continue
    data = json.load(open(fpath, encoding="utf-8"))
    for q in data.get("questions", []):
        all_questions.append(q)
    for cs in data.get("case_studies", []):
        for sq in cs.get("sub_questions", []):
            # Include case study context in question text for mock exam
            sq_copy = dict(sq)
            sq_copy["question"] = f"[Case Scenario: {cs['scenario'][:160]}...]\n\n{sq['question']}"
            all_questions.append(sq_copy)

print(f"Total INS 202 questions collected: {len(all_questions)}")

# Split into two balanced 35-question mock exams
# We want representation from all 7 topics and balanced difficulty (high L3-L4)
mock1_qs = []
mock2_qs = []

for idx, q in enumerate(all_questions):
    if idx % 2 == 0 and len(mock1_qs) < 35:
        mock1_qs.append(q)
    elif idx % 2 == 1 and len(mock2_qs) < 35:
        mock2_qs.append(q)

# If either needs more to reach 35
remaining = [q for q in all_questions if q not in mock1_qs and q not in mock2_qs]
while len(mock1_qs) < 35 and remaining:
    mock1_qs.append(remaining.pop(0))
while len(mock2_qs) < 35 and remaining:
    mock2_qs.append(remaining.pop(0))

mock_exams = [
    {
        "id": "ins202-mock-1",
        "title": "INS 202 Human-Computer Interaction — Comprehensive Midterm Mock 1",
        "description": "Standard university midterm simulation covering HCI goals (Safety, Utility, Efficiency, Effectiveness, Usability), Interaction vs Interface, Cognitive Psychology (Miller 7+/-2, Gestalt, Fitts's Law), UCD & Prototyping (Low vs High fidelity, Think Aloud), Evaluation (Nielsen heuristics, Likert scales), Information Architecture, and Universal Design / Accessibility (WCAG 2.1 POUR).",
        "duration_minutes": 60,
        "total_marks": 70,
        "questions": mock1_qs
    },
    {
        "id": "ins202-mock-2",
        "title": "INS 202 Human-Computer Interaction — Comprehensive Midterm Mock 2",
        "description": "Advanced exam simulation focusing on deep application and analytical case studies: Usability specifications (Performance vs Preference divergence), Expert inspection curves (Nielsen 3-5 evaluators), Cognitive Walkthrough, Card Sorting (Open vs Closed), Visual Organization (Proximity, Alignment, Contrast), and Emerging Interfaces (VUI cognitive load, VR simulator sickness, 6 DoF, Gorilla arm).",
        "duration_minutes": 60,
        "total_marks": 70,
        "questions": mock2_qs
    }
]

with open("app/content/INS 202/mock_exams.json", "w", encoding="utf-8") as f:
    json.dump(mock_exams, f, indent=2, ensure_ascii=False)

print(f"Mock 1: {len(mock1_qs)} Qs, Mock 2: {len(mock2_qs)} Qs saved to mock_exams.json!")
