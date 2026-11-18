# Audit Report: COS 201 Topic 5 — Functions & Modular Programming

## 1. Topic Overview
- **Course:** COS 201 (Computer Programming I / C)
- **Topic:** Functions & Modular Programming (`functions_modular`)
- **JSON File:** `app/content/COS 201/functions_modular.json`
- **Total Questions:** 21 standard questions + 2 scenario case studies (3 sub-questions) = 24 items
- **Flashcards:** 8 key terms covered
- **Difficulty 3-4 (Apply/Analyze):** 11 / 24 (45.8%) -> Exceeds minimum 30% requirement

## 2. Past Exam Alignment (Nile Midterm Type B)
- **Direct Past Exam Match:**
  - Past Exam Question 2 ("Which keyword is used to exit from a function and optionally return a value?") -> Directly addressed in `cos201-fn-001` (type_answer / MCQ `return`) and `cos201-fn-fc06`.
- **Core Curricular Coverage:**
  - Function prototypes vs definitions (necessity before `main` when declared below).
  - Pass-by-value semantics: formal parameters receive copies, modifications inside function body do not alter caller's arguments.
  - Return types and `void` functions (attempting to assign or return values).
  - Scope and storage durations: local automatic variables (`auto`) vs `static` persistence across invocations vs file-scope global variables.
  - Recursion: base case necessity, recursive progression, factorial / countdown stack frames, and stack overflow conditions.
  - Standard library functions in `<math.h>` (`sqrt`, `pow`, `abs`/`fabs`) and `<stdlib.h>` (`rand`, `srand`).

## 3. GCC Verification Status
- **Compiler:** `gcc.exe (Rev13, MSYS2) 15.2.0` with `-Wall -Wextra -std=c11`
- **Verification Rate:** 100% of executable code questions compiled and executed in Windows MSYS2 GCC environment.
- **Verified Outputs:**
  - `cos201-fn-003` (Pass-by-value immutability): Output `10` verified.
  - `cos201-fn-006` (Static local variable accumulation): Output `1 2 3` verified.
  - `cos201-fn-007` (Recursive countdown function): Output `3 2 1 blastoff!` verified.
  - `cos201-fn-008` (Recursive factorial base case): Output `24` verified.
  - `cos201-fn-009` (Global vs Local scope shadowing): Output `5 20` verified.
  - `cos201-fn-cs01-q1` (Pass-by-value swap defect): Output `x=10, y=20` verified.
  - `cos201-fn-cs02-q1` (Fibonacci recursion trace): Output `8` verified.

## 4. Misconception and Option Quality Audit
- All MCQs feature fully justified distractor rationale in `why_wrong`.
- No throwaway answers like "All of the above" or "None of the above".
- Specific common student misconceptions probed:
  - Believing pass-by-value changes caller variables.
  - Confusing static local variables with reinitialized local variables.
  - Forgetting the recursive base case leading to infinite recursion.
  - Believing function prototypes must have matching parameter names rather than just types.

## 5. Audit Verdict: PASSED
Ready for student practice and inclusion in master index.
