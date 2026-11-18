# Topic Inventory: COS 201 — Topic 7: Pointers & Memory Management

## 1. Core Concepts & Definitions
- **Pointer:** A variable whose value is the memory address of another variable.
- **Address-of Operator (`&`):** A unary operator that yields the memory address of its operand (operand must be an lvalue). E.g. `&count`.
- **Dereferencing / Indirection Operator (`*`):** A unary operator that accesses or mutates the value stored at the memory address pointed to by the pointer. E.g. `*ptr = 25;`.
- **NULL Pointer:** A pointer that points to nothing (address 0 / implementation-defined null memory location). Defined in `<stddef.h>` and `<stdio.h>`. Dereferencing NULL causes an immediate crash (segmentation fault).
- **Void Pointer (`void *`):** A generic pointer type that can hold the address of any object type without explicit casting. Cannot be directly dereferenced or used in pointer arithmetic without typecasting.

## 2. Pointer Declaration & Initialization
- **Syntax:** `type *ptrName;` E.g. `int *p;` (declares `p` as a pointer to `int`).
- **Multiple Declarations Trap:** `int* p1, p2;` declares `p1` as `int*`, but `p2` as regular `int`! Correct: `int *p1, *p2;`.
- **Initialization:** Must be initialized to an address (`&x`), `NULL`, or `0`. Uninitialized pointers ("wild pointers") hold random addresses; writing to them causes catastrophic memory corruption.
- **Dangling Pointer:** A pointer that continues pointing to memory that has been freed or an out-of-scope stack frame.

## 3. Pass-by-Reference Simulation with Pointers
- C functions are strictly pass-by-value.
- To simulate pass-by-reference (allowing a function to modify caller variables), the caller passes the addresses (`&x, &y`), and the function accepts pointer parameters (`int *a, int *b`).
- Classic Swap:
  ```c
  void swap(int *a, int *b) {
      int temp = *a;
      *a = *b;
      *b = temp;
  }
  ```

## 4. Pointer Arithmetic
- Adding an integer `k` to pointer `p` advances the address by `k * sizeof(*p)` bytes.
  - E.g., if `int *p` is at address `1000`, and `sizeof(int) == 4`, `p + 1` evaluates to address `1004`, NOT `1001`.
- Subtracting two pointers of the same type (`p2 - p1`) gives the number of elements between them, yielding type `ptrdiff_t`.
- Relational operators (`<`, `<=`, `>`, `>=`) compare memory addresses (valid only within the same array or one past the end).

## 5. Pointers and Arrays Equivalence
- Array name `arr` evaluates to `&arr[0]`.
- Array subscription is pure syntactic sugar for pointer offset dereferencing:
  `arr[i]` is identical to `*(arr + i)`.
- By commutativity of addition: `*(i + arr)` is also identical, meaning `i[arr]` is syntactically valid in C!
- Difference between array and pointer:
  - An array name is a **constant pointer**; it cannot be reassigned (`arr = ptr;` is illegal).
  - A pointer variable has its own separate memory location and can be incremented (`ptr++`), whereas `arr++` is illegal.

## 6. Const Qualifiers with Pointers
- **Pointer to Constant (`const int *p` or `int const *p`):** The data pointed to cannot be modified (`*p = 10;` is an error), but the pointer itself can point elsewhere (`p = &y;` is allowed). Read: "pointer to const int".
- **Constant Pointer (`int * const p`):** The pointer cannot change where it points (`p = &y;` is an error), but the data it points to CAN be modified (`*p = 10;` is allowed). Must be initialized when declared. Read: "const pointer to int".
- **Constant Pointer to Constant (`const int * const p`):** Neither the address nor the data can be altered.

## 7. Dynamic Memory Management Basics
- `<stdlib.h>` functions:
  - `malloc(size_t size)`: Allocates `size` bytes of uninitialized memory. Returns `void *`, or `NULL` if allocation fails.
  - `calloc(size_t num, size_t size)`: Allocates and clears memory to zero.
  - `free(void *ptr)`: Releases allocated heap memory back to the operating system.
  - Memory leak occurs when allocated memory is never freed before losing all pointers to it.
