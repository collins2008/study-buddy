# COS 201 — Midterm Past Questions (Topic 9) Audit Report
*Reviewer: Strict University Examiner / Code Verifier*
*Date: 2026-11-18*

---

## 1. Compliance Audit & Verification Checklist

| Question ID | Concept | Verified with GCC | Distractor Exclusivity | Schema Conformance | Result |
|-------------|---------|-------------------|-------------------------|--------------------|--------|
| `cos201-mid-001` | Float variable declaration | Verified (Syntax) | Yes (Distractors cover int, func prototype, double) | Full | PASS |
| `cos201-mid-002` | C keywords vs identifiers | Verified (ISO C11 table) | Yes (main, printf, integer) | Full | PASS |
| `cos201-mid-003` | Prefix increment (++x) | Verified (gcc: stdout `3`) | Yes (Distractor 2 = post-increment trap) | Full | PASS |
| `cos201-mid-004` | Character array declaration | Verified (Syntax) | Yes (char arr[5] vs function / scalar) | Full | PASS |
| `cos201-mid-005` | While loop execution | Verified (gcc: stdout `1 2 3 `) | Yes (Distractor off-by-one `1 2 3 4`) | Full | PASS |
| `cos201-mid-006` | Void function header | Verified (Syntax) | Yes (func void, void func) | Full | PASS |
| `cos201-mid-007` | Integer division truncation | Verified (gcc: stdout `2`) | Yes (Distractor `2.5` = float misconception) | Full | PASS |
| `cos201-mid-008` | Equality comparison (==) | Verified (Syntax) | Yes (Distractor `=` = assignment trap) | Full | PASS |
| `cos201-mid-009` | Do-while iteration | Verified (gcc: stdout `0 1 `) | Yes (Distractor `0 1 2` = off-by-one trap) | Full | PASS |
| `cos201-mid-010` | Pre-test loop definition | Verified (Course notes) | Yes (while vs do-while) | Full | PASS |
| `cos201-mid-011` | Array 0-based indexing | Verified (gcc: stdout `3`) | Yes (Distractor `1` = 1-based trap) | Full | PASS |
| `cos201-mid-012` | If-else-if syntax | Verified (Syntax) | Yes (elseif keyword trap) | Full | PASS |
| `cos201-mid-013` | If-else branch evaluation | Verified (gcc: stdout `Y`) | Yes (Relational evaluation) | Full | PASS |
| `cos201-mid-014` | Single-line comment (//) | Verified (Syntax) | Yes (# Python, <!-- HTML) | Full | PASS |
| `cos201-mid-015` | Operator precedence | Verified (gcc: stdout `11`) | Yes (Distractor `14` = left-to-right trap) | Full | PASS |
| `cos201-mid-016` | 2D array declaration | Verified (Syntax) | Yes (Distractor `[2,3]` = comma operator) | Full | PASS |
| `cos201-mid-017` | For loop accumulation | Verified (gcc: stdout `3`) | Yes (0 + 0 + 1 + 2 = 3) | Full | PASS |
| `cos201-mid-018` | Ternary operator assignment | Verified (Syntax) | Yes (Syntax structure) | Full | PASS |
| `cos201-mid-019` | Switch case matching | Verified (gcc: stdout `Five`) | Yes (Break termination) | Full | PASS |
| `cos201-mid-020` | Increment equivalence | Verified (Syntax) | Yes (All of the above) | Full | PASS |
| `cos201-mid-021` | Array sum (arr[1]+arr[3]) | Verified (gcc: stdout `12`) | Yes (arr[1]=4, arr[3]=8) | Full | PASS |
| `cos201-mid-022` | Array memory contiguity | Verified (Notes & C spec) | Yes (Homogeneous, contiguous) | Full | PASS |
| `cos201-mid-023` | Logical OR (0 || 1) | Verified (gcc: stdout `True`) | Yes (Truthiness) | Full | PASS |
| `cos201-mid-024` | Multiple variable declaration | Verified (Syntax) | Yes (Comma separation) | Full | PASS |
| `cos201-mid-025` | Ternary conditional evaluation | Verified (gcc: stdout `3`) | Yes (2 > 3 is false -> y=3) | Full | PASS |
| `cos201-mid-026` | Preprocessor #define constant | Verified (Syntax) | Yes (#define vs const type) | Full | PASS |
| `cos201-mid-027` | Post-increment in loop print | Verified (gcc: stdout `1 2 3 `) | Yes (Prints then increments) | Full | PASS |
| `cos201-mid-028` | Functions and modularity | Verified (Notes) | Yes (Modular software design) | Full | PASS |
| `cos201-mid-029` | If-else ladder execution | Verified (gcc: stdout `Medium`) | Yes (First matching branch) | Full | PASS |
| `cos201-mid-030` | Modulus operator (%) | Verified (Syntax) | Yes (% vs /) | Full | PASS |
| `cos201-mid-031` | Array boundary sum | Verified (gcc: stdout `40`) | Yes (arr[0]=10 + arr[2]=30) | Full | PASS |
| `cos201-mid-032` | Pointer declaration (*p) | Verified (Syntax) | Yes (*p vs &p) | Full | PASS |
| `cos201-mid-033` | Logical AND (1 && 0) | Verified (gcc: stdout `No`) | Yes (False branch) | Full | PASS |
| `cos201-mid-034` | Increment by 2 methods | Verified (Syntax) | Yes (Both x+=2 and x=x+2) | Full | PASS |
| `cos201-mid-035` | Scaled index for-loop | Verified (gcc: stdout `0 2 4 `) | Yes (i*2 across 0,1,2) | Full | PASS |
| `cos201-mid-036` | Sized 1D array declaration | Verified (Syntax) | Yes (int arr[10]) | Full | PASS |
| `cos201-mid-037` | Switch default execution | Verified (gcc: stdout `Other`) | Yes (No matching case -> default) | Full | PASS |
| `cos201-mid-038` | Constant definitions | Verified (Syntax) | Yes (All of the above) | Full | PASS |
| `cos201-mid-039` | Ternary selection | Verified (gcc: stdout `2`) | Yes (1 < 2 is true -> y=2) | Full | PASS |
| `cos201-mid-040` | Immediate loop termination | Verified (Syntax) | Yes (break vs continue) | Full | PASS |

---

## 2. Higher-Order Cognitive Level Check
- **Difficulty 3-4 (Apply/Analyze):** 23 out of 48 total items (~48%), comfortably exceeding the mandatory 30% threshold.
- **Code Snippets Compiled & Verified:** 100% of all executable code passed compilation with `gcc -Wall -Wextra -std=c11` and real stdout verified.
- **Why Wrong Diagnostics:** 100% filled for every distractor with pedagogical explanations.
