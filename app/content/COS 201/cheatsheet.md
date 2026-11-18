# COS 201 — Computer Programming I (C Language)
## Ultimate Last-Minute Exam Revision Cheatsheet
*Nile University of Nigeria — Department of Software Engineering*

---

### 1. Data Types, Memory Sizes & Format Specifiers
| Type | Typical Size (C11/x86-64) | Value Range | Format Specifier | Conversion / Notes |
| :--- | :--- | :--- | :--- | :--- |
| `char` | 1 byte (8 bits) | -128 to 127 | `%c` / `%d` | ASCII integer representation (`'A'` = 65, `'a'` = 97, `'0'` = 48) |
| `int` | 4 bytes (32 bits) | -2,147,483,648 to 2,147,483,647 | `%d` or `%i` | Truncates fractions automatically on division |
| `unsigned int` | 4 bytes (32 bits) | 0 to 4,294,967,295 | `%u` | Wrap-around modulo $2^{32}$ on overflow |
| `float` | 4 bytes (32 bits) | ~6 decimal digits precision | `%f` | Standard single-precision IEEE 754 |
| `double` | 8 bytes (64 bits) | ~15 decimal digits precision | `%lf` (`%f` in printf) | Default for literal decimals like `3.14` |
| `size_t` | 8 bytes | Unsigned address width | `%zu` | Return type of `sizeof` and `strlen` |
| `pointer` | 4 bytes (32-bit) / 8 bytes (64-bit) | Memory address | `%p` | Address of object |

---

### 2. Operator Precedence & Associativity (Top to Bottom)
| Rank | Category | Operators | Associativity | Key Exam Pitfall |
| :---: | :--- | :--- | :---: | :--- |
| **1** | Postfix | `()` `[]` `->` `.` `x++` `x--` | Left $\to$ Right | Evaluates current value **first**, then increments |
| **2** | Unary (Prefix) | `++x` `--x` `+` `-` `!` `~` `*` `&` `sizeof` | **Right $\to$ Left** | Increments **before** value is used in expression |
| **3** | Multiplicative | `*` `/` `%` | Left $\to$ Right | `%` applies only to integers! (e.g. `5 % 2 = 1`) |
| **4** | Additive | `+` `-` | Left $\to$ Right | `a + b * 2` evaluates `b * 2` first! |
| **5** | Shift | `<<` `>>` | Left $\to$ Right | Bitwise shifts |
| **6** | Relational | `<` `<=` `>` `>=` | Left $\to$ Right | `1 < x < 5` evaluates `(1 < x) < 5` (always true!) |
| **7** | Equality | `==` `!=` | Left $\to$ Right | Do not confuse `==` (comparison) with `=` (assignment) |
| **8** | Bitwise AND | `&` | Left $\to$ Right | Masks bits |
| **9** | Bitwise XOR | `^` | Left $\to$ Right | Inverts matching bits |
| **10** | Bitwise OR | `\|` | Left $\to$ Right | Sets bits |
| **11** | Logical AND | `&&` | Left $\to$ Right | **Short-circuits**: stops if left operand is 0 |
| **12** | Logical OR | `\|\|` | Left $\to$ Right | **Short-circuits**: stops if left operand is non-zero |
| **13** | Ternary (Conditional) | `? :` | **Right $\to$ Left** | `x = cond ? val_if_true : val_if_false;` |
| **14** | Assignment | `=` `+=` `-=` `*=` `/=` `%=` | **Right $\to$ Left** | Evaluates right side completely first |
| **15** | Comma | `,` | Left $\to$ Right | Discards left, returns right value |

---

### 3. Nile Examiner Traps (The 10 Golden Rules)

1. **Integer Division Truncation:**
   * `5 / 2` evaluates to `2` (NOT `2.5`).
   * To get `2.5`, at least one operand must be a float: `5.0 / 2` or `(float)5 / 2`.
2. **Pre-increment vs Post-increment:**
   * `int x = 2; printf("%d", ++x);` $\to$ Prints `3` (increments to 3 first).
   * `int x = 2; printf("%d", x++);` $\to$ Prints `2` (increments to 3 after printing).
3. **Array Zero-Indexing:**
   * An array `int arr[3] = {10, 20, 30};` has valid indices `0`, `1`, `2`.
   * `arr[0] = 10`, `arr[1] = 20`, `arr[2] = 30`.
   * Accessing `arr[3]` is an **out-of-bounds bug** (Undefined Behavior).
4. **Switch Fall-Through (Missing `break`):**
   * If a `case` lacks a `break;`, execution waterfalls straight through into subsequent cases regardless of their labels until a `break` or `}` is hit!
5. **C Keywords vs Identifiers:**
   * `return`, `int`, `while`, `break`, `switch`, `case`, `default`, `for`, `float`, `char` are reserved C keywords.
   * `main`, `printf`, `scanf`, `include`, `integer` are **NOT** keywords (`main` is a function identifier, `printf` is a library function).
6. **Logical Short-Circuit Evaluation:**
   * `0 && (++x)` $\to$ Left is false, so `++x` is **never executed**. `x` does not change.
   * `1 || (++x)` $\to$ Left is true, so `++x` is **never executed**.
7. **Array Decay in Functions:**
   * When `int arr[10]` is passed into `void func(int a[])`, `a` decays to a pointer (`int *`).
   * Inside `func`, `sizeof(a)` evaluates to pointer size (4 or 8 bytes), NOT 40 bytes! You must always pass array size explicitly.
8. **Pointers Syntax (`*` vs `&`):**
   * Declaration: `int *p;` (`p` is a pointer to an integer).
   * Address-of: `p = &x;` (stores the address of `x` in `p`).
   * Dereference: `*p = 50;` (mutates the value at the memory address pointed to by `p`).
9. **String Null-Terminator (`'\0'`):**
   * `"Nile"` has 4 visible letters, but occupies **5 bytes** in memory: `'N'`, `'i'`, `'l'`, `'e'`, `'\0'`.
   * `strlen("Nile")` = `4` (counts characters before `\0`).
   * `sizeof("Nile")` = `5` (counts total allocated bytes including `\0`).
10. **Ternary Operator:**
    * Syntax: `cond ? expr1 : expr2;`
    * Example: `x = 2 > 3 ? 2 : 3;` $\to$ `(2 > 3)` is false, so `3` is returned.

---

### 4. Essential Code Skeletons

#### Standard Function Prototype & Definition
```c
#include <stdio.h>

// 1. Prototype declaration
int addNumbers(int a, int b);

int main(void) {
    int sum = addNumbers(10, 25);
    printf("Sum = %d\n", sum);
    return 0; // standard clean termination
}

// 2. Function definition
int addNumbers(int a, int b) {
    return a + b;
}
```

#### Safe Loop Patterns
```c
// Pre-test for-loop (count-controlled)
for (int i = 0; i < N; i++) {
    // runs N times: 0 to N-1
}

// Pre-test while loop (condition-controlled)
while (condition) {
    // may execute 0 times if condition initially false
}

// Post-test do-while loop
do {
    // guaranteed to execute AT LEAST ONCE
} while (condition);
```

#### Pointer Arithmetic & Array Equivalence
```c
int arr[3] = {10, 20, 30};
int *p = arr; // equivalent to p = &arr[0]

// The following 4 expressions evaluate to the exact same element:
// 1. arr[1]
// 2. *(arr + 1)
// 3. p[1]
// 4. *(p + 1)
```
