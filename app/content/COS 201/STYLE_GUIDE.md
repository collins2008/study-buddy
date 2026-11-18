# COS 201 — Computer Programming I (C Language)
## Exam Style Guide & Pedagogical Blueprint
*Derived directly from Nile University 2024/2025 Midterm Examination (Type B) & Department of Software Engineering Standards*

---

## 1. Exam Structure & Profile
- **Assessment Type**: Midterm Examination (Type B) + Final Examination
- **Time Allocated**: 60 minutes for Midterm (40 questions); 2 hours for Final
- **Format**: 100% Multiple Choice Questions (single answer, 4 choices A/B/C/D) supplemented in finals by practical code writing/tracing.
- **Cognitive Weighting**:
  - **~45% Code Output & Tracing**: Short, compact C snippets (4-8 lines) testing exact execution behavior.
  - **~30% Syntax & Declarations**: Identification of valid C syntax, keyword recognition, valid declarations, operator usage.
  - **~25% Conceptual & Rules**: Memory layout, short-circuit evaluation, operator precedence, pass-by-value, array properties.

---

## 2. Command Words & Phrasing Patterns (Exact Nile University Phrasing)
All generated questions for COS 201 must match the lecturer's precise phrasing:
- *"Which of the following is the correct way to declare a ...?"* (e.g. float variable, character array, 2D array, pointer)
- *"Which of the following is a valid C keyword?"*
- *"What will be the output of the following code?"*
- *"Which of the following is used to ...?"* (e.g. compare two values, terminate a loop immediately, calculate modulus)
- *"Which loop is best suited when the condition is checked ...?"*
- *"Which of the following statements about ... is TRUE?"* (e.g. arrays, functions, pointers)
- *"Which of the following is the correct syntax for ... in C?"* (e.g. if-else if-else, ternary operator)

---

## 3. Recurring Examiner Traps & Misconceptions
The Nile University examiner systematically tests specific C pitfalls:
1. **Integer Division vs Float Division**: `5 / 2` evaluates to `2`, NOT `2.5`.
2. **Pre-increment vs Post-increment**: `++x` updates before use; `x++` evaluates before increment.
3. **Array Zero-Indexing & Memory Contiguity**: Indices strictly run from `0` to `N-1`. Elements are contiguous in memory.
4. **Missing `break` in `switch` statements**: Fallthrough execution.
5. **Short-Circuit Evaluation in Logical Operators**: In `x || 1` or `x && y`, second operand evaluation depends on truthiness.
6. **Ternary Operator Precedence & Syntax**: `condition ? expr1 : expr2`.
7. **Pointers Syntax**: `int *p;` vs address-of `&` vs dereference `*`.
8. **Loop Boundary Off-by-One**: `for(i=0; i<3; i++)` runs 3 times (0, 1, 2), not 4.
9. **C Keywords vs Library Functions**: `printf` and `main` are NOT C keywords; `return`, `int`, `while`, `break` are keywords.

---

## 4. Code Verification Rule (Zero-Tolerance)
Every C snippet featured in any question must:
1. Be compiled using `gcc -Wall -Wextra -std=c11`.
2. Be executed on real hardware.
3. Have its exact standard output recorded in `verified_output`.
4. If a snippet exhibits Undefined Behavior (UB), it must be explicitly framed as an analysis of undefined/unspecified behavior, never assumed.

---

## 5. Question Schema Alignment
Every question generated must feature:
- 4 clear, mutually exclusive options (A, B, C, D)
- `why_wrong` populated for every distractor explaining the precise conceptual misunderstanding
- `source` referencing the textbook chapter/section or specific past paper question
- Difficulty strictly mapped: Level 1 (Recall), Level 2 (Understand), Level 3 (Apply/Trace), Level 4 (Analyze/Find Bug)
