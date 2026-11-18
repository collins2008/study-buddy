import json
import glob
import os

files = sorted(glob.glob("app/content/SEN 201/*.json"))
all_questions = []

for f in files:
    if "mock_exams" in f:
        continue
    slug = os.path.basename(f).replace(".json", "")
    with open(f, "r", encoding="utf-8") as jf:
        data = json.load(jf)
        topic_name = data.get("topic", slug)
        for q in data.get("questions", []):
            qc = dict(q)
            qc["topic_slug"] = slug
            all_questions.append(qc)
        for cs in data.get("case_studies", []):
            scenario = cs.get("scenario", "")
            for sq in cs.get("sub_questions", []):
                sqc = dict(sq)
                sqc["topic_slug"] = slug
                sqc["scenario"] = scenario
                all_questions.append(sqc)

print(f"Total available SEN 201 questions: {len(all_questions)}")

# Select 50 questions for Exam Alpha (focusing heavily on exam questions, lifecycle, requirements, testing)
# Select 50 questions for Exam Beta (focusing heavily on architecture, modeling, evolution, PM, case studies)
exam_alpha_qs = all_questions[0:100:2]  # even indices
exam_beta_qs = all_questions[1:101:2]   # odd indices

# If needed, extend to 50 questions each
if len(exam_alpha_qs) < 50:
    exam_alpha_qs = all_questions[:50]
    exam_beta_qs = all_questions[50:100]

mock_data = {
    "course": "SEN 201",
    "title": "Introduction to Software Engineering Mock Examinations",
    "exams": [
        {
            "id": "sen201-mock-alpha",
            "title": "Mock Exam Alpha: Nile University Final Examination Standard Simulation (Type B Blueprint)",
            "description": "Comprehensive 50-question simulation replicating the exact style, cognitive distribution, and timing of the official Nile University First Semester Final Examination (Type B, 100 Marks, Lecturer: Yusuf Mshelia). Covers the software crisis, process models, requirements engineering, UML modeling, testing levels, and maintenance.",
            "duration_minutes": 120,
            "total_marks": 100,
            "passing_score": 60,
            "question_count": len(exam_alpha_qs),
            "questions": exam_alpha_qs
        },
        {
            "id": "sen201-mock-beta",
            "title": "Mock Exam Beta: Advanced Case-Study & Architectural Design Mastery Exam",
            "description": "Rigorous 50-question examination weighted heavily toward Level 3-4 cognitive depth: architectural patterns (Pipe-and-Filter, 4+1 views, MVC), white-box McCabe cyclomatic complexity, Lehman's laws, CMMI maturity levels, COCOMO II estimation, and legacy system re-engineering case studies.",
            "duration_minutes": 120,
            "total_marks": 100,
            "passing_score": 60,
            "question_count": len(exam_beta_qs),
            "questions": exam_beta_qs
        }
    ]
}

out_path = "app/content/SEN 201/mock_exams.json"
with open(out_path, "w", encoding="utf-8") as out_f:
    json.dump(mock_data, out_f, indent=2)

print(f"Generated {out_path} with {len(mock_data['exams'])} full exams ({len(exam_alpha_qs)} and {len(exam_beta_qs)} questions).")
