# COS 201 — Topic 2 Inventory: Operators, Precedence & Expressions
*Source: C How to Program (Deitel Ch 2.5, Ch 3.10-3.13) + Nile University Midterm Examination*

---

## 1. Concepts & Definitions
- **Arithmetic Operators**:
  - Binary addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), remainder/modulus (`%`).
  - Integer Division: When both operands are integers, the fractional part is truncated toward zero (`5 / 2 == 2`). If either operand is floating-point, floating division occurs (`5.0 / 2 == 2.5`).
  - Modulus Operator (`%`): Computes the integer remainder after division (`7 % 4 == 3`, `17 % 5 == 2`). Operands MUST be integral types (illegal with floats).
- **Increment and Decrement Operators**:
  - Unary increment (`++`) and decrement (`--`).
  - Pre-increment (`++x`): Increments the variable first, then evaluates the new value in the expression.
  - Post-increment (`x++`): Evaluates the current value of the variable in the expression first, then increments it.
  - Multiple increments: `x = x + 1;`, `x += 1;`, `++x;`, `x++;` all achieve incrementing by 1 in standalone statements.
- **Assignment Operators**:
  - Simple assignment (`=`): Evaluates right-hand side expression and assigns to left-hand lvalue. Right-to-left associativity.
  - Compound assignment operators: `+=`, `-=`, `*=`, `/=`, `%=`. E.g., `x += 2` is equivalent to `x = x + 2`.
- **Relational and Equality Operators**:
  - Relational: `<` (less than), `<=` (less than or equal to), `>` (greater than), `>=` (greater than or equal to).
  - Equality: `==` (is equal to), `!=` (is not equal to).
  - Common Pitfall: Confusing equality comparison (`==`) with assignment (`=`). `if (x = 5)` assigns 5 to x and evaluates as true.
- **Logical Operators**:
  - Logical AND (`&&`): Evaluates to 1 (true) if and only if both operands are non-zero. Short-circuit: if left operand is 0 (false), right operand is NOT evaluated.
  - Logical OR (`||`): Evaluates to 1 (true) if at least one operand is non-zero. Short-circuit: if left operand is non-zero (true), right operand is NOT evaluated.
  - Logical NOT (`!`): Unary operator; inverts truth value (`!0 == 1`, `!5 == 0`).
- **Conditional / Ternary Operator (`?:`)**:
  - Only ternary operator in C: `condition ? expr1 : expr2`.
  - If condition is true (non-zero), evaluates to expr1; otherwise evaluates to expr2.
  - Example: `max = (a > b) ? a : b;`.
  - Right-to-left associativity for chained ternaries.
- **Bitwise Operators** (Basic awareness):
  - `&` (bitwise AND), `|` (bitwise OR), `^` (bitwise XOR), `~` (bitwise NOT), `<<` (left shift), `>>` (right shift).
- **Operator Precedence & Associativity Hierarchy**:
  1. Parentheses: `()` (Left-to-right)
  2. Unary: `++`, `--`, `+`, `-`, `!`, `sizeof`, `&`, `*` (Right-to-left)
  3. Multiplicative: `*`, `/`, `%` (Left-to-right)
  4. Additive: `+`, `-` (Left-to-right)
  5. Relational: `<`, `<=`, `>`, `>=` (Left-to-right)
  6. Equality: `==`, `!=` (Left-to-right)
  7. Logical AND: `&&` (Left-to-right)
  8. Logical OR: `||` (Left-to-right)
  9. Conditional (Ternary): `?:` (Right-to-left)
  10. Assignment: `=`, `+=`, `-=`, `*=`, `/=`, `%=` (Right-to-left)
  11. Comma: `,` (Left-to-right)

---

## 2. Past Question Anchors (COS 201 Midterm Type B)
- **Q3**: Output of pre-increment `printf("%d", ++x)` where `x=2` -> Output: `3`.
- **Q7**: Output of integer division `printf("%d", a/b)` where `a=5, b=2` -> Output: `2`.
- **Q8**: Comparison operator -> `==`.
- **Q15**: Precedence `printf("%d", a+b*2)` where `a=3, b=4` -> Output: `11`.
- **Q18**: Correct syntax for ternary operator -> `x = a>b ? y : z;`.
- **Q20**: Correct ways to increment by 1 -> `x=x+1;`, `x++;`, `++x;` -> `All of the above`.
- **Q23**: Logical short-circuit `if(x || 1)` where `x=0` -> Output: `True`.
- **Q25**: Ternary evaluation `x>y ? x : y` where `x=2, y=3` -> Output: `3`.
- **Q30**: Modulus operator -> `%`.
- **Q33**: Logical AND `if(x && y)` where `x=1, y=0` -> Output: `No`.
- **Q34**: Increment by 2 -> `x+=2;` and `x=x+2;` -> `Both A and B`.
- **Q39**: Ternary evaluation `x<y ? y : x` where `x=1, y=2` -> Output: `2`.
