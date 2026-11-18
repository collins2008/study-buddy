# COS 201 — Topic 1 Inventory: Data Types, Variables & Declarations
*Source: C How to Program (Deitel & Deitel, Ch. 2 & Ch. 3) + Nile University Midterm Type B*

---

## 1. Concepts & Definitions
- **Variable**: A named memory location that can store a value which may be modified during program execution.
- **Identifier**: A series of characters (letters, digits, underscores) used to name variables, functions, and symbols.
  - Rule 1: Must begin with a letter or an underscore `_`. Cannot begin with a digit.
  - Rule 2: Case-sensitive (`total`, `Total`, and `TOTAL` are three distinct identifiers).
  - Rule 3: Cannot be a reserved C keyword (e.g. `int`, `return`, `float`, `for`).
  - Rule 4: Standard C library identifiers (like `printf`, `scanf`, `main`) are valid identifiers syntactically, but are NOT keywords. Redefining them causes link or runtime errors.
- **Data Types (Basic / Primitive in C)**:
  - `int`: Whole numbers, typically 4 bytes (32 bits) on modern architectures, format `%d` or `%i`.
  - `float`: Single-precision floating-point number (at least 6 decimal digits precision, typically 4 bytes), format `%f`.
  - `double`: Double-precision floating-point number (at least 15 decimal digits precision, typically 8 bytes), format `%lf` (in scanf) or `%f` / `%lf` (in printf).
  - `char`: Single byte character, stored as ASCII integer code (e.g. `'A'` is 65), format `%c`.
  - Modifiers: `signed`, `unsigned`, `short`, `long`, `long long`.
- **Declaration vs Definition vs Initialization**:
  - Declaration: Introduces an identifier and its type to the compiler.
  - Definition: Allocates storage in memory for the variable.
  - Initialization: Assigns an initial value at the time of definition (e.g., `int count = 0;`).
  - Uninitialized local variables contain garbage values (undefined contents).
- **Multiple Variable Declaration**:
  - Comma-separated: `int x, y, z;` (valid).
  - Initialization of multiple: `int x = 1, y = 2, z = 3;` (valid).
  - Chained assignment in declaration: `int x = y = z = 5;` is INVALID if `y` and `z` are not yet declared.
- **Constants in C**:
  - `#define` preprocessor macro: `#define PI 3.14159` (no semicolon, textual substitution before compilation, does not consume variable storage).
  - `const` type qualifier: `const int MAX = 100;` or `int const MAX = 100;` (read-only variable, checked by compiler, enforces type safety).
  - Literal constants: Integer literals (`42`, `0x2A`, `052`), float literals (`3.14`, `3.14f`), character literals (`'A'`), string literals (`"Hello"`).
- **Format Conversion Specifiers**:
  - `%d` / `%i`: signed decimal integer
  - `%u`: unsigned decimal integer
  - `%f`: floating-point (fixed decimal)
  - `%lf`: double precision floating point (in `scanf`)
  - `%c`: single character
  - `%s`: string (null-terminated sequence of characters)
  - `%x` / `%X`: hexadecimal representation
  - `%p`: pointer address

---

## 2. Common Examiner Traps & Misconceptions (Exam-Realistic)
1. **Keyword confusion**: Mistaking `main`, `printf`, `scanf`, `include` for C keywords. They are NOT keywords. Keywords include `return`, `sizeof`, `typedef`, `struct`, `const`, `void`.
2. **Declaration syntax**: `float x();` is a function declaration returning float, NOT a variable declaration.
3. **Macro definition syntax**: Writing `#define PI = 3.14;` or `constant PI 3.14` instead of `#define PI 3.14`.
4. **Multiple declarations**: Writing `int x; y; z;` or `int x y z;` instead of `int x, y, z;`.
5. **Integer truncation**: Initializing `int a = 5.9;` truncates to `5` without rounding.
6. **Character arithmetic**: `'A' + 1` produces `'B'` (or integer 66).
7. **Ampersand in scanf**: `scanf("%d", &x)` requires the address operator `&` for primitive scalar variables.

---

## 3. Past Question Anchors (COS 201 Midterm Type B)
- **Q1**: Correct declaration of float: `float x;`
- **Q2**: Valid C keyword: `return` (distractors: `main`, `printf`, `integer`)
- **Q4**: Character array declaration: `char arr[5];`
- **Q24**: Multiple variable declaration: `int x, y, z;`
- **Q26**: Defining a constant: `#define PI 3.14`
- **Q38**: Declaring a constant integer: `const int x=5;`, `int const x;`, `#define x 5` (all valid mechanisms)
