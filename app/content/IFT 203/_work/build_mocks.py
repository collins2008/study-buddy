import json
import glob
import os

files = sorted(glob.glob("app/content/IFT 203/*.json"))
all_questions = []

for f in files:
    if "mock_exams" in f:
        continue
    slug = os.path.basename(f).replace(".json", "")
    with open(f, "r", encoding="utf-8") as jf:
        data = json.load(jf)
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

print(f"Total available IFT 203 questions: {len(all_questions)}")

# Split 40 questions into Exam Alpha and 40 questions into Exam Beta
exam_alpha_qs = all_questions[0:80:2]  # 40 questions
exam_beta_qs = all_questions[1:81:2]   # 40 questions

mock_data = {
    "course": "IFT 203",
    "title": "Introduction to Web Technology Mock Examinations",
    "exams": [
        {
            "id": "ift203-mock-alpha",
            "title": "Mock Exam Alpha: Web Fundamentals & HTML5/CSS3 Mastery Simulation",
            "description": "Comprehensive 40-question examination testing Internet vs WWW architecture, semantic HTML5 document structures, forms with binary file uploads, tables with colspan/rowspan math, and CSS box-model geometry.",
            "duration_minutes": 90,
            "total_marks": 100,
            "passing_score": 60,
            "question_count": len(exam_alpha_qs),
            "questions": exam_alpha_qs
        },
        {
            "id": "ift203-mock-beta",
            "title": "Mock Exam Beta: Client-Server Architecture, DOM & Web Engineering Simulation",
            "description": "Rigorous 40-question examination weighted heavily toward Level 3-4 cognitive depth: CSS specificity calculations, Flexbox responsive alignment, DOM event delegation, client-side XSS security, HTTP status code diagnostics, and reverse proxy timeouts.",
            "duration_minutes": 90,
            "total_marks": 100,
            "passing_score": 60,
            "question_count": len(exam_beta_qs),
            "questions": exam_beta_qs
        }
    ]
}

out_path = "app/content/IFT 203/mock_exams.json"
with open(out_path, "w", encoding="utf-8") as out_f:
    json.dump(mock_data, out_f, indent=2)

print(f"Generated {out_path} with {len(mock_data['exams'])} full exams ({len(exam_alpha_qs)} and {len(exam_beta_qs)} questions).")
