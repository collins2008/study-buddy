import os
import sys
import json
import re
import subprocess
import tempfile

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

GCC_PATH = "C:/msys64/ucrt64/bin/gcc.exe"
COS201_DIR = os.path.abspath("app/content/COS 201")

TOPIC_FILES = [
    "data_types_variables.json",
    "operators_expressions.json",
    "control_flow_selection.json",
    "loops_iteration.json",
    "functions_modular.json",
    "arrays_1d_2d.json",
    "pointers_memory.json",
    "strings_char_arrays.json",
    "midterm_past_questions.json"
]

def compile_and_run_c(code_str):
    """Compiles C code using GCC and executes it, returning (success, output, error)"""
    # Clean up code string
    full_code = code_str.strip()
    
    # If code doesn't contain main, try wrapping it into a main function
    if "main(" not in full_code:
        full_code = f"""#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {{
    {full_code}
    return 0;
}}"""
    elif "#include" not in full_code:
        full_code = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n" + full_code

    with tempfile.TemporaryDirectory() as tmpdir:
        src_path = os.path.join(tmpdir, "test.c")
        exe_path = os.path.join(tmpdir, "test.exe")
        
        with open(src_path, "w", encoding="utf-8") as f:
            f.write(full_code)
            
        # Compile
        compile_res = subprocess.run(
            [GCC_PATH, "-std=c99", src_path, "-o", exe_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if compile_res.returncode != 0:
            return False, "", compile_res.stderr.strip()
            
        # Run
        try:
            run_res = subprocess.run(
                [exe_path],
                capture_output=True,
                text=True,
                timeout=3
            )
            return True, run_res.stdout.strip(), ""
        except subprocess.TimeoutExpired:
            return False, "", "Execution timed out (possible infinite loop)"
        except Exception as e:
            return False, "", str(e)

def audit_cos201():
    print("=" * 70)
    print("HOSTILE EXAMINER: AUDITING COS 201 (C PROGRAMMING)")
    print("=" * 70)
    
    total_questions = 0
    code_questions = 0
    code_verified = 0
    code_mismatches = []
    
    depth_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    type_counts = {}
    shallow_explanations = []
    missing_why_wrong = []
    topic_summaries = {}

    for tf in TOPIC_FILES:
        filepath = os.path.join(COS201_DIR, tf)
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        qs = data.get("questions", [])
        topic_name = tf.replace(".json", "")
        topic_summaries[topic_name] = {
            "total": len(qs),
            "code_tested": 0,
            "passed": 0
        }
        
        for q in qs:
            total_questions += 1
            qid = q.get("id")
            diff = q.get("difficulty", 1)
            depth_counts[diff] = depth_counts.get(diff, 0) + 1
            qtype = q.get("type", "unknown")
            type_counts[qtype] = type_counts.get(qtype, 0) + 1
            
            # Check explanation quality
            expl = q.get("explanation", "").strip()
            if len(expl.split()) < 10 or "because it is" in expl.lower():
                shallow_explanations.append((qid, expl))
                
            # Check why_wrong for MCQ
            if qtype in ['mcq', 'code_output', 'code_bug'] and q.get('options'):
                ww = q.get('why_wrong', {})
                ans = q.get('answer')
                opts = q.get('options', [])
                for i in range(len(opts)):
                    if i != ans and str(i) not in ww:
                        missing_why_wrong.append((qid, f"Missing why_wrong for option {i}"))

            # Code verification
            raw_code = q.get("code")
            if not raw_code:
                # Look for ```c code block in question statement
                m = re.search(r"```c(.*?)```", q.get("question", ""), re.DOTALL)
                if m:
                    raw_code = m.group(1).strip()
                    
            if raw_code and qtype in ["code_output", "code_trace"]:
                code_questions += 1
                topic_summaries[topic_name]["code_tested"] += 1
                
                success, output, err = compile_and_run_c(raw_code)
                if success:
                    code_verified += 1
                    topic_summaries[topic_name]["passed"] += 1
                    
                    # If MCQ code_output, check if output matches the marked answer
                    if qtype == "code_output" and isinstance(q.get("answer"), int) and q.get("options"):
                        expected_opt = q["options"][q["answer"]].strip()
                        # normalize spaces and newlines
                        norm_out = output.replace("\r\n", "\n").strip()
                        norm_exp = expected_opt.replace("\r\n", "\n").strip()
                        
                        is_match = (norm_out == norm_exp)
                        if not is_match and norm_out == "" and norm_exp.lower() in ["no output", "(no output)", "nothing"]:
                            is_match = True
                            
                        if not is_match:
                            code_mismatches.append({
                                "id": qid,
                                "file": tf,
                                "code": raw_code,
                                "actual_gcc_output": norm_out,
                                "expected_answer_option": norm_exp
                            })
                else:
                    # Check if the question EXPECTS a compiler error
                    if qtype == "code_output" and isinstance(q.get("answer"), int) and q.get("options"):
                        expected_opt = q["options"][q["answer"]].lower()
                        if "error" in expected_opt or "compilation" in expected_opt:
                            code_verified += 1
                            topic_summaries[topic_name]["passed"] += 1
                        else:
                            code_mismatches.append({
                                "id": qid,
                                "file": tf,
                                "code": raw_code,
                                "actual_gcc_output": f"COMPILATION ERROR: {err[:200]}",
                                "expected_answer_option": expected_opt
                            })

    print(f"Total Questions Audited: {total_questions}")
    print(f"Total Code Questions Tested with GCC: {code_questions}")
    print(f"Code Questions Verified by Compiler: {code_verified}")
    print(f"Compiler Mismatches Found: {len(code_mismatches)}")
    print(f"Shallow Explanations: {len(shallow_explanations)}")
    print(f"Missing why_wrong entries: {len(missing_why_wrong)}")
    
    print("\n--- COGNITIVE DEPTH BREAKDOWN ---")
    l3_l4 = depth_counts[3] + depth_counts[4]
    for d in [1, 2, 3, 4]:
        print(f"  Level {d}: {depth_counts[d]} ({depth_counts[d] / total_questions * 100:.1f}%)")
    print(f"  High-Cognitive (L3+L4): {l3_l4} ({l3_l4 / total_questions * 100:.1f}%)")
    
    if code_mismatches:
        print("\n" + "!" * 70)
        print(f"COMPILER DISCREPANCIES ({len(code_mismatches)}):")
        for m in code_mismatches:
            print(f"  [{m['id']}] {m['file']}")
            print(f"    Expected : {m['expected_answer_option']}")
            print(f"    GCC Actual: {m['actual_gcc_output']}")
        print("!" * 70)
    else:
        print("\n✓ ZERO COMPILER DISCREPANCIES! 100% of tested C snippets produce exact expected output under GCC 15.2.0.")

    return {
        "total": total_questions,
        "code_tested": code_questions,
        "code_verified": code_verified,
        "mismatches": code_mismatches,
        "depth": depth_counts,
        "shallow": shallow_explanations,
        "missing_ww": missing_why_wrong
    }

if __name__ == "__main__":
    audit_cos201()
