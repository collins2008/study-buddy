import json
import glob
import os
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ENT211_DIR = "app/content/ENT 211"

EXAMINER_ENRICHMENTS = {
    "ent211-fnd-013": "Intrapreneurship (coined by Gifford Pinchot III in 1985) refers to employee-driven entrepreneurship within an established corporate enterprise: an individual acts like an entrepreneur by innovating, championing new business ventures, or developing breakthrough products using the company's financial capital and operational infrastructure. Two fundamental differences: 1) Risk Ownership: The independent entrepreneur personally bears financial and legal bankruptcy risk, while the intrapreneur risks career reputation while the corporation absorbs financial losses; 2) Resource Control: The entrepreneur must raise external capital and build systems from scratch, whereas the intrapreneur leverages established corporate distribution channels, R&D labs, brand equity, and legal resources. (Pinchot, 1985; Nile Lecture Module 1).",
    "ent211-fnd-014": "A calculated risk is an educated business gamble where the entrepreneur conducts market research, feasibility studies, sensitivity analysis, and scenario planning to identify potential failure modes, estimate probabilities, and implement explicit risk-mitigation contingencies before deploying capital. Unlike a gambler who relies on pure chance and games with negative expected value without influence over the outcome, a disciplined entrepreneur proactively influences the probability of success through strategic execution, iterative customer feedback, agility, and hedging techniques. (Knight, 1921; Nile Lecture Module 1).",
    "ent211-thy-015": "In Harvey Leibenstein's (1968) X-efficiency theory, X-inefficiency represents the shortfall in operational efficiency where an established firm fails to produce the maximum possible economic output from its given combination of input resources, typically caused by managerial inertia, lack of market competition, internal organizational friction, and motivational deficits. The entrepreneur acts as an 'input-completer' and 'gap-filler'—identifying slack resources, streamlining operational bottlenecks, introducing competitive incentives, and reorganizing workflows to push the enterprise toward its optimal production frontier. (Leibenstein, 1968; Nile Lecture Module 2)."
}

def enrich_and_fix_ent211():
    files = sorted(glob.glob(os.path.join(ENT211_DIR, "*.json")))
    
    updated_expl = 0
    id_map = {}
    
    for f in files:
        if "mock_exams" in f:
            continue
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            
        modified = False
        for q in data.get("questions", []):
            qid = q.get("id")
            if qid in EXAMINER_ENRICHMENTS:
                q["explanation"] = EXAMINER_ENRICHMENTS[qid]
                updated_expl += 1
                modified = True
            id_map[qid] = q
            
        if modified:
            with open(f, "w", encoding="utf-8") as fp:
                json.dump(data, fp, indent=2, ensure_ascii=False)
                
    # Sync mock_exams.json
    mock_file = os.path.join(ENT211_DIR, "mock_exams.json")
    if os.path.exists(mock_file):
        with open(mock_file, "r", encoding="utf-8") as fp:
            mdata = json.load(fp)
        synced = 0
        for exam in mdata.get("exams", []):
            for q in exam.get("questions", []):
                qid = q.get("id")
                if qid in id_map:
                    src = id_map[qid]
                    q["explanation"] = src["explanation"]
                    if "why_wrong" in src:
                        q["why_wrong"] = src["why_wrong"]
                    synced += 1
        with open(mock_file, "w", encoding="utf-8") as fp:
            json.dump(mdata, fp, indent=2, ensure_ascii=False)
        print(f"Synced {synced} questions in ENT 211 mock_exams.json")

    print(f"Applied {updated_expl} explanation enrichments in ENT 211.")

if __name__ == "__main__":
    enrich_and_fix_ent211()
