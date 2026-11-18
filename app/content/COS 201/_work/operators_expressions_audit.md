# COS 201 — Topic 2 Hostile Examiner Audit
**Topic:** Operators, Precedence & Expressions
**Total Questions Evaluated:** 33 items + 2 multi-part case study scenarios (5 sub-questions) = 38 total questions

---

## 1. Examiner Adversarial Checks
| Question ID | Question Type | Pass/Fail | Hostile Examiner Evaluation & Verification |
|-------------|---------------|-----------|---------------------------------------------|
| `cos201-op-001` | Code Output | PASS | Matches Midterm Q3. GCC verified output: `3`. Pre-increment behavior verified. |
| `cos201-op-002` | Code Output | PASS | GCC verified output: `2 3`. Post-increment deferred evaluation verified. |
| `cos201-op-003` | Code Output | PASS | Matches Midterm Q7. GCC verified output: `2`. Truncation in integer division confirmed. |
| `cos201-op-004` | MCQ | PASS | Matches Midterm Q8. Confirmed `==` for comparison vs `=` assignment. |
| `cos201-op-005` | Code Output | PASS | Matches Midterm Q15. GCC verified output: `11`. Precedence `*` over `+` confirmed. |
| `cos201-op-006` | MCQ | PASS | Matches Midterm Q18. Syntax for ternary operator verified. |
| `cos201-op-007` | MCQ | PASS | Matches Midterm Q20. Confirmed all three forms (`x=x+1`, `x++`, `++x`) increment by 1. |
| `cos201-op-008` | Code Output | PASS | Matches Midterm Q23. GCC verified output: `True`. Logical OR with 1 confirmed. |
| `cos201-op-009` | Code Output | PASS | Matches Midterm Q25. GCC verified output: `3`. Ternary branch selection confirmed. |
| `cos201-op-010` | MCQ | PASS | Matches Midterm Q30. `%` operator as modulus confirmed. |
| `cos201-op-011` | Code Output | PASS | Matches Midterm Q33. GCC verified output: `No`. Logical AND with 0 confirmed. |
| `cos201-op-012` | MCQ | PASS | Matches Midterm Q34. Confirmed `Both A and B` for increment by 2. |
| `cos201-op-013` | Code Output | PASS | Matches Midterm Q39. GCC verified output: `2`. Ternary evaluation confirmed. |
| `cos201-op-014` | Code Output | PASS | GCC verified output: `a=0 b=5`. Short-circuit skipping `++b` verified. |
| `cos201-op-015` | Code Output | PASS | GCC verified output: `-3 3`. Negative operand modulus rules in C99 verified. |
| `cos201-op-016` | Code Bug | PASS | GCC verified output: `Active`. Accidental assignment in if condition verified. |
| `cos201-op-017` | Calculation | PASS | Mathematical and precedence order verification of `2 + 3*4 - 8/2%3 = 13`. |
| `cos201-op-018` | Cloze | PASS | Tests `%`, `==`, `!` operators. |
| `cos201-op-019` | Matching | PASS | Precedence & associativity groupings accurately mapped. |
| `cos201-op-020` | Sequencing | PASS | Step-by-step unparenthesized vs parenthesized evaluation steps verified. |
| `cos201-op-021` | Code Write | PASS | GCC verified reference solution outputs `Max: 72`. |
| `cos201-op-022` | Explain | PASS | Model answer and marking criteria for pre vs post increment. |
| `cos201-op-023` | Code Output | PASS | GCC verified output: `InRange`. Relational chaining `(10 < x < 20)` trap confirmed. |
| `cos201-op-024` | Code Output | PASS | GCC verified output: `1 0`. Bitwise vs logical operator distinction confirmed. |
| `cos201-op-025` | MCQ | PASS | Modulus restriction to integer types confirmed. |
| `cos201-op-fc01..08`| Flashcards | PASS | 8 core operational definitions confirmed. |
| `cos201-op-cs01` | Case Study (3 Qs) | PASS | Grading calculation; compound assignment precedence, nested ternary, short-circuit verified. |
| `cos201-op-cs02` | Case Study (2 Qs) | PASS | Robotics motor controller; modulus loop periodicity and speed increment verified. |

---

## 2. Coverage & Difficulty Balance
- **Total Questions in Topic:** 33 single items + 5 sub-questions across 2 case studies = 38 items.
- **Difficulty 3 & 4 (Apply / Analyze):** 19 items (50.0% of total) -> Exceeds 30% requirement.
- **Verification Status:** 100% of code snippets compiled with `gcc -Wall -Wextra -std=c11` and outputs recorded.
- **Audit Verdict:** APPROVED. Ready for index update.
