import os
import sys
import json

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

IFT203_DIR = os.path.abspath("app/content/IFT 203")

TOPIC_FILES = [
    "internet_web_architecture.json",
    "html_structure_semantics.json",
    "html_forms_tables_media.json",
    "css_selectors_typography.json",
    "css_box_model_layout.json",
    "javascript_dom_basics.json",
    "web_security_servers.json"
]

def audit_ift203():
    print("=" * 70)
    print("HOSTILE EXAMINER: AUDITING IFT 203 (WEB TECHNOLOGIES I)")
    print("=" * 70)

    total_questions = 0
    depth_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    type_counts = {}
    shallow_explanations = []
    missing_why_wrong = []
    topic_stats = {}

    for tf in TOPIC_FILES:
        filepath = os.path.join(IFT203_DIR, tf)
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        qs = data.get("questions", [])
        topic_name = tf.replace(".json", "")
        topic_stats[topic_name] = {
            "total": len(qs),
            "l3_l4": 0,
            "case_studies": len(data.get("case_studies", []))
        }

        for q in qs:
            total_questions += 1
            qid = q.get("id")
            diff = q.get("difficulty", 1)
            depth_counts[diff] = depth_counts.get(diff, 0) + 1
            if diff in [3, 4]:
                topic_stats[topic_name]["l3_l4"] += 1
                
            qtype = q.get("type", "unknown")
            type_counts[qtype] = type_counts.get(qtype, 0) + 1
            
            # Check explanation quality
            expl = q.get("explanation", "").strip()
            if len(expl.split()) < 8 or "because it is" in expl.lower():
                shallow_explanations.append((qid, tf, expl))
                
            # Check why_wrong for MCQ
            if qtype in ['mcq', 'calculation', 'multi_select', 'html_render'] and q.get('options'):
                ww = q.get('why_wrong', {})
                ans = q.get('answer')
                opts = q.get('options', [])
                if isinstance(ans, int):
                    for i in range(len(opts)):
                        if i != ans and str(i) not in ww:
                            missing_why_wrong.append((qid, tf, i, opts[i]))

    print(f"Total Questions Audited: {total_questions}")
    print(f"Shallow Explanations: {len(shallow_explanations)}")
    print(f"Missing why_wrong entries: {len(missing_why_wrong)}")
    
    print("\n--- COGNITIVE DEPTH BREAKDOWN ---")
    l3_l4 = depth_counts[3] + depth_counts[4]
    for d in [1, 2, 3, 4]:
        print(f"  Level {d}: {depth_counts[d]} ({depth_counts[d] / total_questions * 100:.1f}%)")
    print(f"  High-Cognitive (L3+L4): {l3_l4} ({l3_l4 / total_questions * 100:.1f}%)")

    print("\n--- TOPIC-BY-TOPIC BREAKDOWN ---")
    for tname, stats in topic_stats.items():
        pct = (stats['l3_l4'] / stats['total'] * 100) if stats['total'] > 0 else 0
        print(f"  {tname:32}: {stats['total']:2} Qs | {stats['l3_l4']:2} L3/L4 ({pct:4.1f}%) | {stats['case_studies']} Case Studies")

    if shallow_explanations:
        print(f"\n--- SAMPLE SHALLOW EXPLANATIONS ({len(shallow_explanations)}) ---")
        for qid, tf, expl in shallow_explanations[:10]:
            print(f"  [{qid}] ({tf}): {expl}")

    if missing_why_wrong:
        print(f"\n--- SAMPLE MISSING WHY_WRONG ENTRIES ({len(missing_why_wrong)}) ---")
        for qid, tf, opt_i, opt_text in missing_why_wrong[:10]:
            print(f"  [{qid}] ({tf}) opt {opt_i}: '{opt_text}'")

    return {
        "total": total_questions,
        "depth": depth_counts,
        "shallow": shallow_explanations,
        "missing_ww": missing_why_wrong,
        "topics": topic_stats
    }

if __name__ == "__main__":
    audit_ift203()
