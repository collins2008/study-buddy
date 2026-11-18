# COS 201 — Topic 3 Hostile Examiner Audit
**Topic:** Control Flow: If-Else & Switch-Case
**Total Questions Evaluated:** 26 items + 2 multi-part case study scenarios (3 sub-questions) = 29 total questions

---

## 1. Examiner Adversarial Checks
| Question ID | Question Type | Pass/Fail | Hostile Examiner Evaluation & Verification |
|-------------|---------------|-----------|---------------------------------------------|
| `cos201-cf-001` | MCQ | PASS | Directly matches Midterm Q12. 'elseif' distractor verified as non-C syntax. |
| `cos201-cf-002` | Code Output | PASS | Directly matches Midterm Q13. GCC verified output: `Y`. False relational branch confirmed. |
| `cos201-cf-003` | Code Output | PASS | Matches Midterm Q19. GCC verified output: `Five`. Clean break matching verified. |
| `cos201-cf-004` | Code Output | PASS | Matches Midterm Q29. GCC verified output: `Medium`. If-else if ladder evaluation verified. |
| `cos201-cf-005` | Code Output | PASS | Matches Midterm Q37. GCC verified output: `Other`. Switch default branch execution verified. |
| `cos201-cf-006` | Code Output | PASS | GCC verified output: `2 3 D`. Sequential switch fallthrough without break verified. |
| `cos201-cf-007` | Code Output | PASS | GCC verified output: `(No output produced)`. Dangling else binding to nearest if confirmed. |
| `cos201-cf-008` | Code Output | PASS | GCC verified output: `Greater`. Null statement semicolon trap verified. |
| `cos201-cf-009` | MCQ | PASS | Prohibition of float in switch expressions confirmed per ISO C 6.8.4.2. |
| `cos201-cf-010` | MCQ | PASS | Prohibition of variable in case labels confirmed. |
| `cos201-cf-011` | Code Output | PASS | GCC verified output: `Beta`. Intentional fallthrough for character cases ('b', 'B') verified. |
| `cos201-cf-012` | Code Output | PASS | GCC verified output: `NonZero`. Negative integer truthiness confirmed. |
| `cos201-cf-013` | Type Answer | PASS | 'break' keyword identified as switch jump terminator. |
| `cos201-cf-014` | Cloze | PASS | Keywords `if`, `switch`, `default` accurately tested. |
| `cos201-cf-015` | Matching | PASS | 4 core selection statements accurately mapped. |
| `cos201-cf-016` | Sequencing | PASS | Top-to-bottom short-circuit ladder sequence confirmed. |
| `cos201-cf-017` | Code Write | PASS | GCC verified reference solution outputs `Delete`. |
| `cos201-cf-018` | Explain | PASS | Model answer and marking criteria for dangling-else problem. |
| `cos201-cf-fc01..08`| Flashcards | PASS | 8 core selection definitions verified. |
| `cos201-cf-cs01` | Case Study (2 Qs) | PASS | Campus access turnstile; switch fallthrough and stacked cases verified. |
| `cos201-cf-cs02` | Case Study (1 Q) | PASS | Hospital emergency triage; compound if-else ladder verified. |

---

## 2. Coverage & Difficulty Balance
- **Total Questions in Topic:** 26 items + 3 sub-questions across 2 case studies = 29 items.
- **Difficulty 3 & 4 (Apply / Analyze):** 13 items (44.8% of total) -> Exceeds 30% requirement.
- **Verification Status:** 100% of code snippets compiled with `gcc -Wall -Wextra -std=c11` and outputs recorded.
- **Audit Verdict:** APPROVED. Ready for index update.
