import json
import os

topics = [
    "it_foundations_building_blocks.json",
    "computer_hardware_architecture.json",
    "operating_systems_software.json",
    "networking_ip_addressing.json",
    "computer_evolution_generations.json"
]

all_questions = []
base_dir = os.path.join("app", "content", "IFT 205")

for t in topics:
    p = os.path.join(base_dir, t)
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)
        for q in data.get("questions", []):
            all_questions.append(q)
        for cs in data.get("case_studies", []):
            for sq in cs.get("sub_questions", []):
                all_questions.append(sq)

print(f"Total collected questions for IFT 205: {len(all_questions)}")

# Split into two balanced sets of 35 questions each
# Mock Alpha: even index elements; Mock Beta: odd index elements
alpha_qs = [q for i, q in enumerate(all_questions) if i % 2 == 0][:35]
beta_qs = [q for i, q in enumerate(all_questions) if i % 2 == 1][:35]

mock_data = {
    "course": "IFT 205",
    "title": "IFT 205: Introduction to Information Technology — Mock Examinations",
    "exams": [
        {
            "id": "ift205-mock-alpha",
            "title": "Mock Exam Alpha: IT Foundations, Hardware & Operating Systems",
            "description": "Standard university midterm simulation covering IT building blocks, Von Neumann architecture, CPU machine cycle, memory hierarchy, RAM/ROM, SSD/HDD comparisons, 3-2-1 backup rule, and clean OS installation.",
            "duration_minutes": 60,
            "total_marks": 70,
            "passing_score": 40,
            "question_count": len(alpha_qs),
            "questions": alpha_qs
        },
        {
            "id": "ift205-mock-beta",
            "title": "Mock Exam Beta: Networking, IPv4 Addressing & Computer Evolution",
            "description": "Comprehensive semester examination testing Local Area Networks ('LAN does not require internet'), topologies, switches vs routers, bandwidth vs latency, full IPv4 Classes (A to E) with subnet masks, computer generations, and enterprise classification.",
            "duration_minutes": 60,
            "total_marks": 70,
            "passing_score": 40,
            "question_count": len(beta_qs),
            "questions": beta_qs
        }
    ]
}

out_path = os.path.join(base_dir, "mock_exams.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(mock_data, f, indent=2)

print(f"Generated {out_path} with 2 full exams (Alpha: {len(alpha_qs)} Qs, Beta: {len(beta_qs)} Qs).")
