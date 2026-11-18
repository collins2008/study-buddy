# Topic Inventory: COS 201 — Topic 6: Arrays (1D and 2D)

## 1. Core Concepts & Definitions
- **Array:** A group of contiguous memory locations, each holding a value of the exact same data type.
- **Index / Subscript:** An integer expression enclosed in brackets `[]` denoting an element's position. In C, arrays are always **0-indexed** (first element is `arr[0]`, last is `arr[size - 1]`).
- **Array Element:** A distinct memory slot accessible via `arrayName[subscript]`. Behaves as an lvalue (can be assigned to unless marked `const`).
- **Row-Major Order:** In C, multidimensional arrays are laid out in contiguous memory sequentially row-by-row (row 0 fully stored, then row 1, etc.).
- **Array Decay:** When passed to a function or used in most expressions, the name of an array decays into a pointer to its first element (`&arr[0]`).
- **Decay Exceptions:** Array name does NOT decay when used with `sizeof`, `&` (address-of), or string literal initializing an array.

## 2. Declarations, Sizing & Memory Layout
- **Syntax:** `type arrayName[arraySize];` E.g. `int scores[10];`.
- **Memory Consumption:** Total bytes allocated = `arraySize * sizeof(type)`. E.g., for `int a[5];` on 32/64-bit systems where `sizeof(int) == 4`, total size is 20 bytes.
- **Dynamic Sizing / `sizeof` idiom:** `size_t n = sizeof(arr) / sizeof(arr[0]);` calculates the number of elements in a static array.
- **Garbage Values:** Uninitialized local arrays contain arbitrary indeterminate ("garbage") values.

## 3. Initialization Rules
- **Full Initializer List:** `int a[5] = {10, 20, 30, 40, 50};`
- **Partial Initialization:** If fewer initializers are provided than the array size, remaining elements are automatically initialized to `0` (or `0.0` or `'\0'`).
  - Example: `int a[5] = {1, 2};` -> `a[0]=1, a[1]=2, a[2]=0, a[3]=0, a[4]=0`.
  - Zeroing idiom: `int a[100] = {0};` sets all 100 elements to 0.
- **Implicit Sizing:** `int a[] = {5, 10, 15};` -> compiler allocates exactly 3 elements.
- **Excess Initializers:** Providing more initializers than declared array size triggers a compiler error/warning (`excess elements in array initializer`).

## 4. Bounds Checking & Common Traps
- **No Bounds Checking:** C does **not** check array bounds at compile time (unless static analysis detects constant index) or run time. Accessing `a[5]` on an array of size 5 compiles, leading to reading/writing out-of-bounds memory (segmentation fault or silent memory corruption).
- **Off-by-One Error:** Looping with `for (int i = 0; i <= size; i++)` instead of `i < size`.
- **Negative Indices:** While C pointer arithmetic allows `p[-1]`, accessing negative index on array `arr[-1]` reads memory before the array buffer.

## 5. Multidimensional Arrays (2D Arrays)
- **Syntax:** `type arrayName[numRows][numCols];`
- **Initialization:**
  - Grouped by rows: `int m[2][3] = {{1, 2, 3}, {4, 5, 6}};`
  - Linear list: `int m[2][3] = {1, 2, 3, 4, 5, 6};` (fills row 0 first, then row 1).
  - Partial 2D: `int m[2][3] = {{1}, {4, 5}};` -> row 0 has `1, 0, 0`; row 1 has `4, 5, 0`.
- **Memory Mapping Formula:** For `int a[R][C]`, element `a[i][j]` is located at byte offset:
  `base_address + (i * C + j) * sizeof(type)`.
- **Function Parameter Requirement:** When declaring a 2D array parameter in a function header, the column dimension is **mandatory**:
  - Valid: `void printMatrix(int m[][3], int rows);`
  - Invalid: `void printMatrix(int m[][], int rows);` (Compile error: array type has incomplete element type).

## 6. Arrays and Functions
- **Pass-by-Reference Simulation:** Arrays are passed by address (decay to pointer). Any modification inside the callee modifies the caller's array directly.
- **`const` Array Parameter:** Using `const int a[]` protects the array elements from being modified inside the function (compiler error if assignment attempted).
- **Passing Individual Elements:** Passing `arr[i]` passes a single value by value, NOT by reference.

## 7. Algorithms & Patterns
- Finding maximum and minimum in an array.
- Computing sum and average.
- Linear search (scanning elements sequentially).
- In-place array reversal using two pointers/indices.
- Matrix addition and transpose.
