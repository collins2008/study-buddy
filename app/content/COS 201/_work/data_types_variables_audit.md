# COS 201 — Topic 1 Hostile Examiner Audit
**Topic:** Data Types, Variables & Declarations
**Total Questions Evaluated:** 35 items + 2 multi-part case study scenarios (5 sub-questions) = 40 total questions

---

## 1. Examiner Adversarial Checks
| Question ID | Question Type | Pass/Fail | Hostile Examiner Evaluation & Verification |
|-------------|---------------|-----------|---------------------------------------------|
| `cos201-dt-001` | MCQ | PASS | Directly matches Midterm Q1. 'float x();' verified as function declaration. Unambiguous. |
| `cos201-dt-002` | MCQ | PASS | Directly matches Midterm Q2. 'printf' and 'main' distractors verified as non-keywords. |
| `cos201-dt-003` | MCQ | PASS | Matches Midterm Q24. Evaluates comma-separated single-statement declarations. |
| `cos201-dt-004` | MCQ | PASS | Matches Midterm Q26. Preprocessor macro syntax strictly checked against semicolon misuse. |
| `cos201-dt-005` | MCQ | PASS | Matches Midterm Q38. Confirmed that both 'const int' and '#define' define integer constants. |
| `cos201-dt-006` | Code Output | PASS | GCC 15.2.0 verified output: `5, 2.0`. Truncation vs rounding trap tested cleanly. |
| `cos201-dt-007` | Code Output | PASS | GCC 15.2.0 verified output: `13`. Classic macro precedence without parentheses tested. |
| `cos201-dt-008` | Code Output | PASS | GCC 15.2.0 verified output: `D 68`. Char integral arithmetic verified against ASCII table. |
| `cos201-dt-009` | Code Output | PASS | GCC 15.2.0 verified output: `26 10`. 0x1A (hex) and 012 (octal) literal parsing verified. |
| `cos201-dt-010` | Code Output | PASS | GCC 15.2.0 verified output: `1`. sizeof(char) == 1 guaranteed by ISO standard. |
| `cos201-dt-011` | Code Output | PASS | GCC 15.2.0 verified output: `"A\B"`. Escape sequence quotes and backslashes verified. |
| `cos201-dt-012` | MCQ | PASS | Evaluates identifier rule starting with digit (`3rd_student`). |
| `cos201-dt-013` | MCQ | PASS | Tests unsigned vs signed range and bit-representation. |
| `cos201-dt-014` | True/False/Why | PASS | Evaluates identifier starting with underscore vs number with dual justification. |
| `cos201-dt-015` | Type Answer | PASS | Tests single character specifier `%c`. |
| `cos201-dt-016` | Type Answer | PASS | Tests scanf double specifier `%lf`. |
| `cos201-dt-017` | Code Bug | PASS | Tested with GCC. Missing `&age` in scanf correctly flagged. |
| `cos201-dt-018` | Cloze | PASS | Tests `int`, `float`, `const` keywords. |
| `cos201-dt-019` | Matching | PASS | 4 distinct type/modifier pairs accurately linked. |
| `cos201-dt-020` | Sequencing | PASS | Chronological lifecycle of a variable verified. |
| `cos201-dt-021` | Explain | PASS | Explicit marking points for #define vs const int verified. |
| `cos201-dt-022` | Code Write | PASS | GCC verified reference solution outputs `Total: 562.50`. |
| `cos201-dt-023` | Code Output | PASS | GCC verified output: `30 5`. Value assignment isolation confirmed. |
| `cos201-dt-024` | Code Output | PASS | GCC verified output: `-128`. Signed char two's complement rollover confirmed. |
| `cos201-dt-025` | MCQ | PASS | Uninitialized chained declaration compilation error confirmed. |
| `cos201-dt-026` | Code Output | PASS | GCC verified output: `4 2`. sizeof('A') == 4 in C vs sizeof("A") == 2 confirmed. |
| `cos201-dt-027` | MCQ | PASS | Lowercase hex `%x` conversion specifier confirmed. |
| `cos201-dt-fc01..08` | Flashcards | PASS | 8 key definitions aligned with Nile syllabus. |
| `cos201-dt-cs01` | Case Study (3 Qs) | PASS | Student Bursary billing scenario; GCC verified integer division truncation (Ratio: 0.00). |
| `cos201-dt-cs02` | Case Study (2 Qs) | PASS | Embedded microcontroller register scenario; unsigned range and signed rollover verified. |

---

## 2. Coverage & Difficulty Balance
- **Total Questions in Topic:** 35 single questions + 5 sub-questions across 2 case studies = 40 items.
- **Difficulty 3 & 4 (Apply / Analyze):** 18 items (45.0% of total) -> Exceeds 30% requirement.
- **Verification Status:** 100% of code snippets compiled with `gcc -Wall -Wextra -std=c11` and outputs recorded.
- **Audit Verdict:** APPROVED. Ready for index update.
