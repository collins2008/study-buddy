# COS 201 — Topic 4 Inventory: Loops & Iteration (While, Do-While & For)
*Source: C How to Program (Deitel Ch 3.7-3.9, Ch 4.2-4.9) + Nile University Midterm Examination*

---

## 1. Concepts & Definitions
- **Repetition Statements in C**:
  - `while`: Pre-test loop. Evaluates condition before executing body. May execute 0 or more times.
  - `for`: Pre-test loop with built-in initialization, loop-continuation condition, and increment expression:
    `for (initialization; condition; increment) { body }`
  - `do...while`: Post-test loop. Evaluates condition after executing body. Guaranteed to execute at least ONCE. Ends with a mandatory semicolon after `while (condition);`.
- **Counter-Controlled vs Sentinel-Controlled Repetition**:
  - Counter-controlled: Definite repetition known in advance. Uses a control variable, initial value, increment/decrement, and limit condition.
  - Sentinel-controlled: Indefinite repetition terminated by a sentinel (signal / dummy / flag) value indicating end of input (e.g. `-1` or `EOF`).
- **Loop Jump Statements**:
  - `break`: Immediately exits the innermost enclosing loop or switch construct. Control passes to the statement immediately following the loop.
  - `continue`: Skips the remainder of the current iteration body. In `while` and `do...while`, control jumps directly to condition re-evaluation. In `for`, control jumps to the increment expression, then to condition evaluation.
- **Nested Loops**:
  - Outer loop and inner loop iterations. Total inner iterations = outer_iterations * inner_iterations (for rectangular grids).
  - Tracing nested counters and pattern generation (triangles, tables, matrices).
- **Common Loop Traps & Misconceptions**:
  - Off-by-one errors: Using `<=` instead of `<` (or vice-versa), executing one extra or one fewer iteration.
  - Infinite loops: Forgetting to increment the loop control variable inside a `while` loop, or setting an impossible exit condition.
  - Accidental semicolon after loop header:
    - `while (i < 5); { i++; }` creates an infinite loop if `i < 5`, or executes the block once if `i >= 5`.
    - `for (i = 0; i < 5; i++);` terminates the loop empty, and only the subsequent statement runs with `i = 5`.
  - Missing semicolon after `do...while (condition);`: Syntax error.

---

## 2. Past Question Anchors (COS 201 Midterm Type B)
- **Q5**: `while(a < 4){ printf("%d ", a); a++; }` with `a = 1` -> prints `1 2 3 `
- **Q9**: `do { printf("%d ", x); x++; } while(x < 2);` with `x = 0` -> prints `0 1 `
- **Q10**: Loop checking condition before executing body -> `while` (or `for`)
- **Q17**: `for(int i = 0; i < 3; i++){ x += i; }` with `x = 0` -> `x = 3`
- **Q27**: `while(i <= 3){ printf("%d ", i++); }` with `i = 1` -> prints `1 2 3 `
- **Q35**: `for(i = 0; i < 3; i++){ printf("%d ", i * 2); }` -> prints `0 2 4 `
- **Q40**: Terminate loop immediately -> `break`
