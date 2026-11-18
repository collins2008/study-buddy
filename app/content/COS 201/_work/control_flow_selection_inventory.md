# COS 201 — Topic 3 Inventory: Control Flow (If-Else & Switch-Case)
*Source: C How to Program (Deitel Ch 3.3-3.7, Ch 4.5-4.8) + Nile University Midterm Examination*

---

## 1. Concepts & Definitions
- **Selection Statements in C**:
  - Single-selection: `if` statement.
  - Double-selection: `if...else` statement.
  - Multiple-selection: `if...else if...else` ladder and `switch` statement.
- **`if` and `if...else` Semantics**:
  - Condition: Any scalar expression evaluating to non-zero (true) or zero (false).
  - Null statement: A stray semicolon immediately following `if (condition);` creates an empty body, causing the intended block to always execute.
  - Compound statements (blocks): Grouping statements with `{ ... }`. Without braces, only the single immediately following statement is part of the if/else branch.
- **The Dangling Else Ambiguity**:
  - In nested if-else structures without braces, the C compiler pairs an `else` with the *closest preceding unmatched `if`*, regardless of indentation.
  - Braces `{}` resolve the ambiguity explicitly.
- **`switch` Multiple-Selection Statement**:
  - Structure:
    ```c
    switch (integral_expression) {
        case constant1:
            // statements
            break;
        case constant2:
            // statements
            break;
        default:
            // default statements
            break;
    }
    ```
  - Expression restriction: The controlling expression MUST evaluate to an integer type (`int`, `char`, `short`, `long`, `enum`). Floating-point types (`float`, `double`) and strings are strictly prohibited.
  - Case labels: Must be constant integer expressions (e.g. `case 1:`, `case 'A':`, `case 2 + 3:`). Variables (e.g. `case x:`) are compile-time errors. Duplicate case values are illegal.
  - Fall-through: If a `break` statement is omitted, execution flows sequentially into the following case(s) regardless of their labels until a `break` or the end of the switch is encountered.
  - `default` label: Executes if no `case` label matches. Optional. Can appear anywhere in the switch body, though typically placed at the end.

---

## 2. Past Question Anchors (COS 201 Midterm Type B)
- **Q12**: Correct syntax for if-else if-else -> `if(condition){} else if(condition){} else{}`
- **Q13**: Basic double selection `if(x>y) printf("X"); else printf("Y");` -> prints `Y`
- **Q19**: Matching switch with break `case 5: printf("Five"); break;` -> prints `Five`
- **Q29**: If-else if ladder evaluation `x=5 -> x>10 (F), x>3 (T)` -> prints `Medium`
- **Q37**: Switch default execution when no case matches `x=3` -> prints `Other`
- Missing break fallthrough: `case 1: case 2: ...`
