# COS 201 — Topic 5 Inventory: Functions, Parameters & Modular Design
*Source: C How to Program (Deitel Ch 5.1-5.14) + Nile University Midterm Examination*

---

## 1. Concepts & Definitions
- **Modular Programming**:
  - Dividing a large program into smaller, manageable, reusable modules (functions).
  - Benefits: software reusability, easier debugging, localized error scope, abstraction.
- **Function Structure**:
  - Return-value-type function-name (parameter-list) { definitions and statements }
  - `void` return type: Indicates the function returns no value to the caller.
  - `void` parameter list: e.g. `int main(void)` indicates the function accepts no parameters.
- **Function Declarations (Prototypes) vs Definitions**:
  - Prototype: `return_type name(param_type1, param_type2);` tells the compiler the function signature before its first call. Enables compiler argument type-checking and implicit type coercion.
  - Definition: Contains the actual implementation and code body `{ ... }`.
- **Argument Passing Mechanism (Pass-by-Value)**:
  - In C, all scalar arguments are passed **by value** (a copy of the argument value is passed to the parameter).
  - Changes made to parameter variables inside the function have ZERO effect on the caller's original variables.
  - To simulate pass-by-reference and modify caller variables, pointers (addresses) must be explicitly passed.
- **Return Statement**:
  - `return expression;` in functions with non-void return types.
  - `return;` or simply falling off the closing brace `}` in void functions.
  - Functions can return primitive types, pointers, structures, but CANNOT return arrays directly (return pointer instead).
- **Variable Scope and Storage Duration**:
  - Block scope: Variables declared inside a block are accessible only within that block.
  - File scope: Variables declared outside any function (globals) are accessible by all functions in the file.
  - Automatic storage duration: Default for local variables; created upon entering block, destroyed upon exit.
  - Static storage duration: Global variables and local variables declared with `static`. Local static variables retain their values between function calls!
- **Recursion**:
  - A function that calls itself directly or indirectly.
  - Base case: Halts recursion.
  - Recursive call / step: Moves toward base case. Missing base case results in infinite recursion and stack overflow.

---

## 2. Past Question Anchors (COS 201 Midterm Type B)
- **Q6**: Valid way to define a function returning void -> `void func() {}`
- **Q28**: Truth about functions in C -> `Functions help in modular programming`
- Pass-by-value modification immutability tests.
- Static local variable accumulation across function invocations.
- Function prototype matching and return type mismatch checks.
