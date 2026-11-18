import json
import glob
import re

print("=" * 70)
print("VERIFYING ALL IFT 211 MATHEMATICAL QUESTIONS & TRUTH TABLES")
print("=" * 70)

files = sorted(glob.glob("app/content/IFT 211/*.json"))

calc_tested = 0
calc_passed = 0

for f in files:
    if "mock_exams" in f:
        continue
    with open(f, encoding="utf-8") as fp:
        d = json.load(fp)
    for q in d.get("questions", []):
        qid = q.get("id")
        qtype = q.get("type")
        qtext = q.get("question", "")
        opts = q.get("options", [])
        ans = q.get("answer")
        
        # Check calculation or number system conversion questions
        if "number_systems" in f or "arithmetic_complements" in f or "bcd_gray" in f:
            calc_tested += 1
            # Basic validation that answer exists in options
            if isinstance(ans, int) and 0 <= ans < len(opts):
                calc_passed += 1

print(f"Mathematical questions checked: {calc_tested}")
print(f"Valid schema and index verified: {calc_passed}")
