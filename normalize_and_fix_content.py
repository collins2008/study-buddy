import os
import sys
import json
import re

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CONTENT_DIR = os.path.abspath("app/content")
INDEX_PATH = os.path.join(CONTENT_DIR, "index.json")

def normalize_all():
    print("--- 1. Fixing INS 202 user_centered_development typo ---")
    ucd_path = os.path.join(CONTENT_DIR, "INS 202", "user_centered_development.json")
    with open(ucd_path, "r", encoding="utf-8") as f:
        ucd_data = json.load(f)
        
    for cs in ucd_data.get("case_studies", []):
        if cs.get("id") == "ins202-ucd-cs1":
            for sq in cs.get("sub_questions", []):
                if sq.get("id") == "ins202-ucd-cs2-q2":
                    sq["id"] = "ins202-ucd-cs1-q2"
                    print("  ✓ Corrected ins202-ucd-cs2-q2 in CS1 to ins202-ucd-cs1-q2")
                    
    with open(ucd_path, "w", encoding="utf-8") as f:
        json.dump(ucd_data, f, indent=2, ensure_ascii=False)
        
    print("\n--- 2. Fixing SEN 201 project_management_metrics duplicate IDs ---")
    pmm_path = os.path.join(CONTENT_DIR, "SEN 201", "project_management_metrics.json")
    with open(pmm_path, "r", encoding="utf-8") as f:
        pmm_data = json.load(f)
        
    old_to_new_ids = {}
    for q in pmm_data.get("questions", []):
        old_id = q["id"]
        new_id = old_id.replace("sen201-pm-", "sen201-pmm-")
        old_to_new_ids[old_id] = new_id
        q["id"] = new_id
        
    for cs in pmm_data.get("case_studies", []):
        old_cs_id = cs["id"]
        cs["id"] = old_cs_id.replace("sen201-pm-", "sen201-pmm-")
        for sq in cs.get("sub_questions", []):
            old_sq_id = sq["id"]
            new_sq_id = old_sq_id.replace("sen201-pm-", "sen201-pmm-")
            old_to_new_ids[old_sq_id] = new_sq_id
            sq["id"] = new_sq_id
            
    with open(pmm_path, "w", encoding="utf-8") as f:
        json.dump(pmm_data, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Replaced {len(old_to_new_ids)} sen201-pm- IDs with sen201-pmm- in project_management_metrics.json")
    
    # Update index.json
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        idx_data = json.load(f)
        
    for c in idx_data.get("courses", []):
        if c["code"] == "SEN 201":
            for t in c.get("topics", []):
                if t["slug"] == "project_management_metrics":
                    t["question_ids"] = [old_to_new_ids.get(qid, qid) for qid in t.get("question_ids", [])]
                    print("  ✓ Updated question_ids in index.json for SEN 201 project_management_metrics")
                    
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(idx_data, f, indent=2, ensure_ascii=False)
        
    # Update SEN 201 mock_exams.json if old IDs referenced
    sen_mock_path = os.path.join(CONTENT_DIR, "SEN 201", "mock_exams.json")
    if os.path.exists(sen_mock_path):
        with open(sen_mock_path, "r", encoding="utf-8") as f:
            mock_data = json.load(f)
        for ex in mock_data.get("exams", []):
            for mq in ex.get("questions", []):
                if mq.get("id") in old_to_new_ids:
                    mq["id"] = old_to_new_ids[mq["id"]]
        with open(sen_mock_path, "w", encoding="utf-8") as f:
            json.dump(mock_data, f, indent=2, ensure_ascii=False)
        print("  ✓ Updated SEN 201 mock_exams.json with new IDs")

    print("\n--- 3. Normalizing Question Schemas Across All Topics ---")
    fixed_mcq_answers = 0
    fixed_why_wrongs = 0
    fixed_tfs = 0
    fixed_clozes = 0
    fixed_matchings = 0
    fixed_sequencings = 0
    fixed_calcs = 0
    
    for root, _, files in os.walk(CONTENT_DIR):
        for fname in files:
            if not fname.endswith(".json") or fname == "index.json":
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            modified = False
            
            # Helper to normalize question object
            def normalize_q(q):
                nonlocal fixed_mcq_answers, fixed_why_wrongs, fixed_tfs
                nonlocal fixed_clozes, fixed_matchings, fixed_sequencings, fixed_calcs
                q_mod = False
                qtype = q.get("type")
                
                # A. MCQ & options-based questions
                if qtype in ['mcq', 'code_output', 'code_bug', 'code_trace', 'calculation', 'diagram_label', 'html_render']:
                    opts = q.get("options")
                    if isinstance(opts, list) and len(opts) >= 2:
                        ans = q.get("answer")
                        if isinstance(ans, str):
                            # Try exact match
                            if ans in opts:
                                q["answer"] = opts.index(ans)
                                q_mod = True
                                fixed_mcq_answers += 1
                            elif ans.strip() in [o.strip() for o in opts]:
                                for i, o in enumerate(opts):
                                    if o.strip() == ans.strip():
                                        q["answer"] = i
                                        q_mod = True
                                        fixed_mcq_answers += 1
                                        break
                            else:
                                # Try parseInt
                                try:
                                    parsed = int(ans)
                                    if 0 <= parsed < len(opts):
                                        q["answer"] = parsed
                                        q_mod = True
                                        fixed_mcq_answers += 1
                                except ValueError:
                                    pass
                                    
                        # Normalize why_wrong keys to string indices "0", "1", "2", etc.
                        ww = q.get("why_wrong")
                        if isinstance(ww, dict):
                            new_ww = {}
                            for k, v in ww.items():
                                if k in opts:
                                    new_ww[str(opts.index(k))] = v
                                elif k.isdigit():
                                    new_ww[k] = v
                                else:
                                    # Fallback check
                                    for idx, opt in enumerate(opts):
                                        if opt.strip() == k.strip():
                                            new_ww[str(idx)] = v
                                            break
                            if new_ww and new_ww != ww:
                                q["why_wrong"] = new_ww
                                q_mod = True
                                fixed_why_wrongs += 1
                                
                    elif qtype == 'calculation' and (not opts or len(opts) < 2):
                        # Numerical calculation
                        if "tolerance" not in q:
                            q["tolerance"] = 0.01
                            q_mod = True
                            fixed_calcs += 1

                # Multi-select: ensure both answer and answers exist
                elif qtype == "multi_select":
                    ans = q.get("answer") or q.get("answers")
                    if isinstance(ans, list):
                        q["answer"] = ans
                        q["answers"] = ans
                        q_mod = True

                # Type answer: ensure accepted_answers exists
                elif qtype in ["type_answer", "code_fill"]:
                    if not q.get("accepted_answers"):
                        ans = q.get("answer")
                        if isinstance(ans, str) and ans.strip():
                            q["accepted_answers"] = [ans.strip()]
                            q_mod = True
                        elif isinstance(ans, list):
                            q["accepted_answers"] = [str(x).strip() for x in ans if str(x).strip()]
                            q_mod = True
                            
                # B. True False Why
                elif qtype == "true_false_why":
                    # Special case: if answer is string starting with False: or True: and options exist
                    ans = q.get("answer")
                    opts = q.get("options")
                    if isinstance(ans, str) and opts and len(opts) >= 2:
                        # Convert to mcq
                        q["type"] = "mcq"
                        if ans in opts:
                            q["answer"] = opts.index(ans)
                        else:
                            q["answer"] = 0
                        ww = q.get("why_wrong") or {}
                        new_ww = {}
                        for k, v in ww.items():
                            if k in opts:
                                new_ww[str(opts.index(k))] = v
                            elif k.isdigit():
                                new_ww[k] = v
                        q["why_wrong"] = new_ww
                        q_mod = True
                    elif q.get("answer") is None and q.get("tf_answer") is not None:
                        q["answer"] = q["tf_answer"]
                        q_mod = True
                        fixed_tfs += 1
                        
                # C. Cloze
                elif qtype == "cloze":
                    if not q.get("blanks") and not q.get("accepted_answers"):
                        ans = q.get("answer")
                        if isinstance(ans, list):
                            q["blanks"] = ans
                            q_mod = True
                            fixed_clozes += 1
                        elif isinstance(ans, str):
                            # split semicolons or commas
                            parts = [p.strip() for p in ans.replace(";", ",").split(",") if p.strip()]
                            if parts:
                                q["blanks"] = parts
                                q_mod = True
                                fixed_clozes += 1
                                
                # D. Matching
                elif qtype == "matching":
                    if not q.get("pairs"):
                        ans = q.get("answer")
                        opts = q.get("options")
                        pairs = []
                        if isinstance(ans, list) and len(ans) > 0 and isinstance(ans[0], dict) and "left" in ans[0]:
                            pairs = ans
                        elif isinstance(ans, dict):
                            pairs = [{"left": k, "right": v} for k, v in ans.items()]
                        elif isinstance(opts, list) and isinstance(ans, list) and len(opts) == len(ans):
                            pairs = [{"left": l, "right": r} for l, r in zip(opts, ans)]
                        elif isinstance(ans, str):
                            items = [i.strip() for i in ans.replace(";", ",").split(",") if i.strip()]
                            for item in items:
                                if ":" in item:
                                    l, r = item.split(":", 1)
                                    pairs.append({"left": l.strip(), "right": r.strip()})
                                elif "->" in item:
                                    l, r = item.split("->", 1)
                                    pairs.append({"left": l.strip(), "right": r.strip()})
                        if pairs:
                            q["pairs"] = pairs
                            q_mod = True
                            fixed_matchings += 1
                            
                # E. Sequencing
                elif qtype == "sequencing":
                    if not q.get("steps") and isinstance(q.get("options"), list):
                        q["steps"] = q["options"]
                        q_mod = True
                        fixed_sequencings += 1

                return q_mod

            # Run normalization on all questions and case study sub_questions
            for q in data.get("questions", []):
                if normalize_q(q):
                    modified = True
                    
            for cs in data.get("case_studies", []):
                for sq in cs.get("sub_questions", []):
                    if normalize_q(sq):
                        modified = True
                        
            # If mock exams format
            for ex in data.get("exams", []):
                for mq in ex.get("questions", []):
                    if normalize_q(mq):
                        modified = True
                        
            if modified:
                with open(fpath, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    
    print(f"  Fixed MCQ string answers    : {fixed_mcq_answers}")
    print(f"  Fixed why_wrong index keys  : {fixed_why_wrongs}")
    print(f"  Fixed True/False answers    : {fixed_tfs}")
    print(f"  Fixed Cloze blanks          : {fixed_clozes}")
    print(f"  Fixed Matching pairs        : {fixed_matchings}")
    print(f"  Fixed Sequencing steps      : {fixed_sequencings}")
    print(f"  Fixed Calculation tolerance : {fixed_calcs}")
    print("\n✓ Normalization complete!")

if __name__ == "__main__":
    normalize_all()
