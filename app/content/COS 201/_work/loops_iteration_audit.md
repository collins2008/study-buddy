# COS 201 — Topic 4 Hostile Examiner Audit
**Topic:** Loops: While, Do-While & For
**Total Questions Evaluated:** 27 items + 2 multi-part case study scenarios (3 sub-questions) = 30 total questions

---

## 1. Examiner Adversarial Checks
| Question ID | Question Type | Pass/Fail | Hostile Examiner Evaluation & Verification |
|-------------|---------------|-----------|---------------------------------------------|
| `cos201-lp-001` | Code Output | PASS | Matches Midterm Q5. GCC verified output: `1 2 3 `. Loop boundary condition verified. |
| `cos201-lp-002` | Code Output | PASS | Matches Midterm Q9. GCC verified output: `0 1 `. Post-test do-while execution verified. |
| `cos201-lp-003` | MCQ | PASS | Matches Midterm Q10. Verified pre-test vs post-test definition. |
| `cos201-lp-004` | Code Output | PASS | Matches Midterm Q17. GCC verified output: `3`. For-loop accumulator trace verified. |
| `cos201-lp-005` | Code Output | PASS | Matches Midterm Q27. GCC verified output: `1 2 3 `. While loop with post-increment printf verified. |
| `cos201-lp-006` | Code Output | PASS | Matches Midterm Q35. GCC verified output: `0 2 4 `. Loop counter multiplier verified. |
| `cos201-lp-007` | MCQ | PASS | Matches Midterm Q40. Verified 'break' terminates loop immediately. |
| `cos201-lp-008` | Code Output | PASS | GCC verified output: `1 2 4 5 `. Continue skipping iteration 3 verified. |
| `cos201-lp-009` | Code Output | PASS | GCC verified output: `Run10`. Guaranteed single execution of do-while confirmed. |
| `cos201-lp-010` | Code Bug | PASS | Stray semicolon null statement creating infinite loop verified. |
| `cos201-lp-011` | Code Output | PASS | GCC verified output: `1224`. Nested loop grid product verified. |
| `cos201-lp-012` | Code Output | PASS | GCC verified output: `11 21 31 `. Break scoping inside nested loop confirmed. |
| `cos201-lp-013` | Code Output | PASS | GCC verified output: `7 5 3 1 `. Step decrement loop trace verified. |
| `cos201-lp-014` | Type Answer | PASS | 'continue' keyword identified. |
| `cos201-lp-015` | Cloze | PASS | Keywords `do-while`, `break`, `continue` accurately tested. |
| `cos201-lp-016` | Matching | PASS | 4 core loop constructs mapped. |
| `cos201-lp-017` | Sequencing | PASS | 5 sequential steps of for-loop execution order verified. |
| `cos201-lp-018` | Code Write | PASS | GCC verified reference solution outputs `Factorial: 120`. |
| `cos201-lp-019` | Explain | PASS | Model answer and marking criteria for while vs do-while. |
| `cos201-lp-fc01..08`| Flashcards | PASS | 8 loop operational definitions verified. |
| `cos201-lp-cs01` | Case Study (2 Qs) | PASS | Nile ATM PIN verification lockout; do-while and break verified. |
| `cos201-lp-cs02` | Case Study (1 Q) | PASS | Telecom packet reader; sentinel-controlled accumulation verified. |

---

## 2. Coverage & Difficulty Balance
- **Total Questions in Topic:** 27 items + 3 sub-questions across 2 case studies = 30 items.
- **Difficulty 3 & 4 (Apply / Analyze):** 13 items (43.3% of total) -> Exceeds 30% requirement.
- **Verification Status:** 100% of code snippets compiled with `gcc -Wall -Wextra -std=c11` and outputs recorded.
- **Audit Verdict:** APPROVED. Ready for index update.
