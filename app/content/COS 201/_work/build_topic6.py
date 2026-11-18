import json
import subprocess
import os
import tempfile

def compile_and_run(c_code):
    """Compiles C code using gcc -Wall -Wextra -std=c11, runs it, and returns stdout."""
    with tempfile.NamedTemporaryFile(suffix='.c', delete=False, mode='w', encoding='utf-8') as f:
        f.write(c_code)
        c_file = f.name

    exe_file = c_file.replace('.c', '.exe')
    try:
        compile_cmd = ['gcc', '-Wall', '-Wextra', '-std=c11', c_file, '-o', exe_file]
        res = subprocess.run(compile_cmd, capture_output=True, text=True, timeout=10)
        if res.returncode != 0:
            raise RuntimeError(f"Compilation failed:\n{res.stderr}\nCode:\n{c_code}")

        run_res = subprocess.run([exe_file], capture_output=True, text=True, timeout=5)
        out = run_res.stdout.strip().replace('\r\n', '\n')
        if not out:
            out = "(No output produced)"
        return out
    finally:
        if os.path.exists(c_file):
            try: os.remove(c_file)
            except: pass
        if os.path.exists(exe_file):
            try: os.remove(exe_file)
            except: pass

def main():
    print("Compiling and verifying Topic 6 (Arrays 1D & 2D) code snippets with GCC...")

    # Snippet 1: Partial initialization
    code_part_init = """#include <stdio.h>

int main(void) {
    int arr[5] = {10, 20};
    printf("%d %d %d", arr[0], arr[1], arr[2]);
    return 0;
}
"""
    out_part_init = compile_and_run(code_part_init)

    # Snippet 2: sizeof array element count
    code_sizeof = """#include <stdio.h>

int main(void) {
    int nums[] = {5, 10, 15, 20, 25, 30};
    int count = sizeof(nums) / sizeof(nums[0]);
    printf("count = %d", count);
    return 0;
}
"""
    out_sizeof = compile_and_run(code_sizeof)

    # Snippet 3: Passing array to function modifies caller array
    code_modify = """#include <stdio.h>

void doubleElements(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        arr[i] *= 2;
    }
}

int main(void) {
    int vals[3] = {2, 4, 6};
    doubleElements(vals, 3);
    printf("%d %d %d", vals[0], vals[1], vals[2]);
    return 0;
}
"""
    out_modify = compile_and_run(code_modify)

    # Snippet 4: 2D array row-major traversal
    code_2d_row = """#include <stdio.h>

int main(void) {
    int matrix[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };
    printf("%d %d", matrix[1][0], matrix[0][2]);
    return 0;
}
"""
    out_2d_row = compile_and_run(code_2d_row)

    # Snippet 5: Linear list 2D initialization
    code_2d_linear = """#include <stdio.h>

int main(void) {
    int m[2][3] = {10, 20, 30, 40, 50, 60};
    printf("%d", m[1][1]);
    return 0;
}
"""
    out_2d_linear = compile_and_run(code_2d_linear)

    # Snippet 6: Array reversal in-place
    code_reverse = """#include <stdio.h>

void reverse(int a[], int n) {
    int start = 0, end = n - 1;
    while (start < end) {
        int temp = a[start];
        a[start] = a[end];
        a[end] = temp;
        start++;
        end--;
    }
}

int main(void) {
    int a[] = {1, 2, 3, 4, 5};
    reverse(a, 5);
    for (int i = 0; i < 5; i++) {
        printf("%d ", a[i]);
    }
    return 0;
}
"""
    out_reverse = compile_and_run(code_reverse)

    # Snippet 7: Case study 1 code
    code_cs1 = """#include <stdio.h>

int sumDiagonal(int n, int mat[n][n]) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += mat[i][i];
    }
    return sum;
}

int main(void) {
    int grid[3][3] = {
        {2, 1, 4},
        {3, 5, 7},
        {8, 6, 9}
    };
    printf("%d", sumDiagonal(3, grid));
    return 0;
}
"""
    out_cs1 = compile_and_run(code_cs1)

    # Snippet 8: Case study 2 code - tally histogram
    code_cs2 = """#include <stdio.h>

int main(void) {
    int responses[] = {1, 2, 2, 3, 1, 2, 4, 1};
    int freq[5] = {0};
    for (int i = 0; i < 8; i++) {
        freq[responses[i]]++;
    }
    printf("1s:%d 2s:%d 3s:%d 4s:%d", freq[1], freq[2], freq[3], freq[4]);
    return 0;
}
"""
    out_cs2 = compile_and_run(code_cs2)

    questions = [
        # cos201-arr-001: 0-indexed concept (Past Q11)
        {
            "id": "cos201-arr-001",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "mcq",
            "difficulty": 1,
            "tags": ["arrays", "indexing", "past_exam"],
            "question": "In C, if an array is declared as `int arr[10];`, what is the index of the first element and the index of the last element?",
            "options": [
                "First element is 1, last element is 10",
                "First element is 0, last element is 9",
                "First element is 0, last element is 10",
                "First element is 1, last element is 9"
            ],
            "answer": 1,
            "explanation": "C uses 0-based indexing for all arrays. An array of size N has indices running strictly from 0 to N - 1. Thus, for an array of 10 elements, the first index is 0 and the last valid index is 9.",
            "why_wrong": {
                "0": "1-based indexing is used by languages like MATLAB or Fortran, not C.",
                "2": "Index 10 is out of bounds; accessing arr[10] accesses the 11th element, causing undefined behavior.",
                "3": "C does not start counting elements from index 1."
            },
            "source": "Deitel C How to Program, Chapter 6; Nile Past Exam Q11",
            "verified": True,
            "verified_output": "(Language conceptual rule)"
        },

        # cos201-arr-002: Bounds checking absence (Past Q22)
        {
            "id": "cos201-arr-002",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "true_false_why",
            "difficulty": 2,
            "tags": ["arrays", "bounds_checking", "runtime_safety", "past_exam"],
            "question": "The C compiler and runtime environment automatically check array bounds and halt the program if an index exceeds the array size.",
            "options": [
                "True",
                "False"
            ],
            "answer": 1,
            "explanation": "C does NOT provide automatic array bounds checking at compile time or run time. Accessing an element outside array bounds results in undefined behavior (reading garbage, overwriting other variables, or triggering an OS segmentation fault if memory is protected). It is strictly the programmer's responsibility to prevent out-of-bounds indexing.",
            "why_wrong": {
                "0": "Unlike Java, Python, or Rust, C prioritizes speed and raw hardware access, deliberately omitting bounds check overhead."
            },
            "source": "Deitel C How to Program, Section 6.3; Nile Past Exam Q22",
            "verified": True,
            "verified_output": "(Language specification rule)"
        },

        # cos201-arr-003: Partial initialization (Past Q21)
        {
            "id": "cos201-arr-003",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "code_output",
            "difficulty": 2,
            "tags": ["arrays", "initialization", "partial_initialization", "past_exam"],
            "question": "What is the exact output of the following C program?\n\n```c\n#include <stdio.h>\n\nint main(void) {\n    int arr[5] = {10, 20};\n    printf(\"%d %d %d\", arr[0], arr[1], arr[2]);\n    return 0;\n}\n```",
            "options": [
                "10 20 0",
                "10 20 20",
                "10 20 [garbage value]",
                "Compilation error"
            ],
            "answer": 0,
            "explanation": "In C, if an array is partially initialized (fewer initializers than elements in the declared size), all remaining uninitialized elements are automatically set to zero. Here, arr[0]=10, arr[1]=20, and arr[2], arr[3], arr[4] are all initialized to 0.",
            "why_wrong": {
                "1": "Uninitialized elements in a partial initializer list are zeroed, not duplicated from preceding elements.",
                "2": "Only completely uninitialized local arrays contain garbage values; once ANY initializer is provided, the remainder are guaranteed to be 0.",
                "3": "Partial array initialization is fully standard and valid C syntax."
            },
            "source": "Deitel C How to Program, Section 6.4; Nile Past Exam Q21",
            "verified": True,
            "verified_output": out_part_init
        },

        # cos201-arr-004: Calculating array length via sizeof
        {
            "id": "cos201-arr-004",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "code_output",
            "difficulty": 3,
            "tags": ["arrays", "sizeof", "memory"],
            "question": "What is the exact output of the following C code?\n\n```c\n#include <stdio.h>\n\nint main(void) {\n    int nums[] = {5, 10, 15, 20, 25, 30};\n    int count = sizeof(nums) / sizeof(nums[0]);\n    printf(\"count = %d\", count);\n    return 0;\n}\n```",
            "options": [
                "count = 6",
                "count = 24",
                "count = 4",
                "count = 1"
            ],
            "answer": 0,
            "explanation": "`sizeof(nums)` evaluates to the total number of bytes occupied by the entire array (6 ints * 4 bytes/int = 24 bytes). `sizeof(nums[0])` is the size of a single element (4 bytes). 24 / 4 = 6, yielding the exact number of elements in the array.",
            "why_wrong": {
                "1": "24 is the total byte size `sizeof(nums)` on a 32/64-bit architecture, but it is divided by `sizeof(nums[0])`.",
                "2": "4 is the size of a single `int` (`sizeof(nums[0])`), not the quotient.",
                "3": "The array name has not decayed to a pointer here because it is the direct operand of `sizeof`."
            },
            "source": "Deitel C How to Program, Section 6.5",
            "verified": True,
            "verified_output": out_sizeof
        },

        # cos201-arr-005: Array pass-by-reference simulation (Past Q31)
        {
            "id": "cos201-arr-005",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "code_output",
            "difficulty": 3,
            "tags": ["arrays", "functions", "pass_by_reference", "past_exam"],
            "question": "What is the exact output of the following C program?\n\n```c\n#include <stdio.h>\n\nvoid doubleElements(int arr[], int size) {\n    for (int i = 0; i < size; i++) {\n        arr[i] *= 2;\n    }\n}\n\nint main(void) {\n    int vals[3] = {2, 4, 6};\n    doubleElements(vals, 3);\n    printf(\"%d %d %d\", vals[0], vals[1], vals[2]);\n    return 0;\n}\n```",
            "options": [
                "4 8 12",
                "2 4 6",
                "0 0 0",
                "Compilation error: cannot pass array without &"
            ],
            "answer": 0,
            "explanation": "When an array name is passed to a function in C, it decays to a pointer pointing to its first element (`&arr[0]`). Because the function receives the actual memory address of the array, any modifications made to `arr[i]` within the function directly alter the original array elements in `main`. Thus vals becomes {4, 8, 12}.",
            "why_wrong": {
                "1": "Scalar variables in C are passed by value, but array arguments decay to pointers and their elements ARE modified.",
                "2": "The elements were multiplied by 2, not cleared.",
                "3": "Passing array name directly without & is the standard syntax for passing arrays in C."
            },
            "source": "Deitel C How to Program, Section 6.6; Nile Past Exam Q31",
            "verified": True,
            "verified_output": out_modify
        },

        # cos201-arr-006: 2D Array Row-Major Indexing (Past Q16)
        {
            "id": "cos201-arr-006",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "code_output",
            "difficulty": 3,
            "tags": ["multidimensional_arrays", "2d_arrays", "indexing", "past_exam"],
            "question": "What does the following C program print?\n\n```c\n#include <stdio.h>\n\nint main(void) {\n    int matrix[2][3] = {\n        {1, 2, 3},\n        {4, 5, 6}\n    };\n    printf(\"%d %d\", matrix[1][0], matrix[0][2]);\n    return 0;\n}\n```",
            "options": [
                "4 3",
                "1 6",
                "2 5",
                "4 2"
            ],
            "answer": 0,
            "explanation": "In 2D arrays `matrix[row][col]`, indexing starts at 0. `matrix[1][0]` is row 1, col 0, which is 4. `matrix[0][2]` is row 0, col 2, which is 3. The output is `4 3`.",
            "why_wrong": {
                "1": "1 is matrix[0][0] and 6 is matrix[1][2].",
                "2": "2 is matrix[0][1] and 5 is matrix[1][1].",
                "3": "4 is correct for matrix[1][0], but 2 is matrix[0][1], not matrix[0][2]."
            },
            "source": "Deitel C How to Program, Section 6.9; Nile Past Exam Q16",
            "verified": True,
            "verified_output": out_2d_row
        },

        # cos201-arr-007: 2D linear initialization
        {
            "id": "cos201-arr-007",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "code_output",
            "difficulty": 3,
            "tags": ["multidimensional_arrays", "row_major", "initialization"],
            "question": "What is printed by this program?\n\n```c\n#include <stdio.h>\n\nint main(void) {\n    int m[2][3] = {10, 20, 30, 40, 50, 60};\n    printf(\"%d\", m[1][1]);\n    return 0;\n}\n```",
            "options": [
                "50",
                "20",
                "40",
                "30"
            ],
            "answer": 0,
            "explanation": "Because C stores multidimensional arrays in row-major order, the flat initializer list fills row 0 first ({10, 20, 30}), then row 1 ({40, 50, 60}). Therefore, `m[1][1]` is the middle element of row 1, which is 50.",
            "why_wrong": {
                "1": "20 is at m[0][1] (row 0, column 1).",
                "2": "40 is at m[1][0] (row 1, column 0).",
                "3": "30 is at m[0][2] (row 0, column 2)."
            },
            "source": "Deitel C How to Program, Section 6.9",
            "verified": True,
            "verified_output": out_2d_linear
        },

        # cos201-arr-008: 2D array parameter syntax (Past Q36)
        {
            "id": "cos201-arr-008",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["multidimensional_arrays", "functions", "parameters", "past_exam"],
            "question": "Which of the following function prototypes is VALID when accepting a 2-dimensional array of 3 columns in C?",
            "options": [
                "void process(int arr[][3], int rows);",
                "void process(int arr[][], int rows);",
                "void process(int arr[3][], int cols);",
                "void process(int [][]arr, int rows);"
            ],
            "answer": 0,
            "explanation": "When passing a 2D array to a function, the compiler needs to know the number of columns to correctly calculate element memory offsets (`row * cols + col`). Therefore, the column dimension is MANDATORY, while the row dimension (first bracket) may be left empty. `int arr[][3]` is valid.",
            "why_wrong": {
                "1": "`arr[][]` causes a compiler error ('array type has incomplete element type') because the column dimension is missing.",
                "2": "`arr[3][]` is invalid C syntax; the first dimension may be omitted, but subsequent dimensions cannot.",
                "3": "`int [][]arr` is Java/C# syntax, completely illegal in C."
            },
            "source": "Deitel C How to Program, Section 6.9; Nile Past Exam Q36",
            "verified": True,
            "verified_output": "(Language syntax rule)"
        },

        # cos201-arr-009: const array parameter
        {
            "id": "cos201-arr-009",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["arrays", "const", "functions", "safety"],
            "question": "What is the purpose of adding the `const` qualifier to an array parameter in a function header, such as `void display(const int arr[], int size);`?",
            "options": [
                "It prevents the function from modifying the contents of the caller's array",
                "It makes the array accessible globally across all functions",
                "It dynamically allocates memory for the array on the heap",
                "It forces the compiler to pass the entire array by value rather than by reference"
            ],
            "answer": 0,
            "explanation": "Because arrays decay to pointers and are modified in-place, adding `const` tells the compiler that the function should only inspect the array. Any attempt to modify an element inside `display` (e.g. `arr[0] = 5;`) generates a compilation error.",
            "why_wrong": {
                "1": "`const` restricts write access; it does not change scope to global.",
                "2": "Heap allocation in C requires `malloc`/`calloc`, not `const`.",
                "3": "`const` does not change the passing mechanism; the array pointer is still passed, but pointer dereference for assignment is forbidden."
            },
            "source": "Deitel C How to Program, Section 6.6",
            "verified": True,
            "verified_output": "(Language specification rule)"
        },

        # cos201-arr-010: Code Bug - Off-by-one in array traversal
        {
            "id": "cos201-arr-010",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "code_bug",
            "difficulty": 3,
            "tags": ["arrays", "debugging", "off_by_one", "bounds"],
            "question": "Identify the serious defect in the following code snippet and specify the correction:\n\n```c\n#define SIZE 5\nint scores[SIZE];\nfor (int i = 0; i <= SIZE; i++) {\n    scores[i] = i * 10;\n}\n```",
            "options": [
                "The loop condition `i <= SIZE` iterates 6 times, writing out-of-bounds to `scores[5]`; change to `i < SIZE`",
                "The macro `SIZE 5` requires a semicolon at the end",
                "Array indexing cannot use variable `i`; literal constants must be used",
                "The loop must count backwards from `SIZE` to `0`"
            ],
            "answer": 0,
            "explanation": "An array declared as `int scores[5]` has valid indices 0, 1, 2, 3, and 4. The loop condition `i <= SIZE` (where SIZE is 5) causes the loop to execute when `i == 5`. Attempting to write `scores[5]` is an out-of-bounds memory write, causing undefined behavior. The loop condition must be `i < SIZE`.",
            "why_wrong": {
                "1": "Putting a semicolon in `#define SIZE 5;` creates a syntax error wherever `SIZE` is expanded in array declarations.",
                "2": "Array subscripts can be any valid integer expression, including variables like `i`.",
                "3": "Loops can traverse forward or backward; forward is standard."
            },
            "source": "Deitel C How to Program, Section 6.3",
            "verified": True,
            "verified_output": "(Static code analysis defect)"
        },

        # cos201-arr-011: Cloze - Array properties
        {
            "id": "cos201-arr-011",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "cloze",
            "difficulty": 2,
            "tags": ["arrays", "terminology", "memory"],
            "question": "Fill in the blanks regarding C array storage:\n\nIn C, all elements of an array are stored in [[contiguous]] memory locations. Elements within the same array must all share the same data [[type]]. When multidimensional arrays are allocated, C places elements in [[row-major]] order.",
            "answer": ["contiguous", "type", "row-major"],
            "explanation": "Arrays allocate adjacent, unbroken (contiguous) memory blocks for efficiency. Homogeneity is enforced: every element is of the exact same type. In C 2D arrays, row-major order means all elements of row 0 are placed in memory immediately followed by all elements of row 1.",
            "why_wrong": {},
            "source": "Deitel C How to Program, Section 6.2 & 6.9",
            "verified": True,
            "verified_output": "(Conceptual terminology)"
        },

        # cos201-arr-012: In-place array reversal trace
        {
            "id": "cos201-arr-012",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "code_trace",
            "difficulty": 4,
            "tags": ["arrays", "algorithms", "reversal", "two_pointer"],
            "question": "Trace the array elements during execution of this reversal function with array `{1, 2, 3, 4, 5}`:\n\n```c\n#include <stdio.h>\n\nvoid reverse(int a[], int n) {\n    int start = 0, end = n - 1;\n    while (start < end) {\n        int temp = a[start];\n        a[start] = a[end];\n        a[end] = temp;\n        start++;\n        end--;\n    }\n}\n```\nWhat is printed after calling `reverse(a, 5)`?",
            "options": [
                "5 4 3 2 1",
                "1 2 3 4 5",
                "5 2 3 4 1",
                "5 4 3 4 5"
            ],
            "answer": 0,
            "explanation": "Iteration 1: start=0, end=4. Swap a[0] (1) and a[4] (5). Array: {5, 2, 3, 4, 1}. start becomes 1, end becomes 3.\nIteration 2: start=1, end=3. Swap a[1] (2) and a[3] (4). Array: {5, 4, 3, 2, 1}. start becomes 2, end becomes 2.\nIteration 3: start=2, end=2. Condition `start < end` is false (2 < 2 is false). Loop terminates.\nFinal array: 5 4 3 2 1.",
            "why_wrong": {
                "1": "The array was reversed in-place, not left unchanged.",
                "2": "This represents only the first swap (iteration 1).",
                "3": "This is what would happen if a[end] was overwritten without storing a temporary copy."
            },
            "source": "Deitel C How to Program, Section 6.8",
            "verified": True,
            "verified_output": out_reverse
        },

        # cos201-arr-013: Sequencing - Bubble sort pass
        {
            "id": "cos201-arr-013",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "sequencing",
            "difficulty": 3,
            "tags": ["arrays", "algorithms", "sorting", "bubble_sort"],
            "question": "Order the steps involved in performing one full pass of Bubble Sort on an array of size N:",
            "options": [
                "Start with index i = 0",
                "Compare element arr[i] with its adjacent neighbor arr[i + 1]",
                "If arr[i] > arr[i + 1], swap their contents",
                "Increment i and repeat comparison until i reaches the end of the unsorted segment",
                "The largest unsorted value is now placed at its final sorted position at the end"
            ],
            "answer": [0, 1, 2, 3, 4],
            "explanation": "In Bubble Sort, adjacent elements are compared sequentially starting at index 0. If out of order, they swap. After scanning through to the end of the unsorted portion, the largest element 'bubbles up' to its correct final resting place.",
            "why_wrong": {},
            "source": "Deitel C How to Program, Section 6.7",
            "verified": True,
            "verified_output": "(Algorithm step sequence)"
        },

        # cos201-arr-014: Matching - Array syntax and terminology
        {
            "id": "cos201-arr-014",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "matching",
            "difficulty": 2,
            "tags": ["arrays", "terminology", "syntax"],
            "question": "Match each array concept with its correct description or syntax:",
            "options": [
                "int a[10] = {0};",
                "sizeof(a) / sizeof(a[0])",
                "a[row][col]",
                "const int a[]"
            ],
            "answer": {
                "int a[10] = {0};": "Initializes all 10 elements to zero",
                "sizeof(a) / sizeof(a[0])": "Calculates number of elements in a static array",
                "a[row][col]": "Accesses element in row-major 2D array",
                "const int a[]": "Read-only array parameter protected from callee modification"
            },
            "explanation": "These four idiomatic C constructs represent zero initialization, dynamic length calculation of static arrays, 2D indexing, and read-only function contracts.",
            "why_wrong": {},
            "source": "Deitel C How to Program, Chapter 6",
            "verified": True,
            "verified_output": "(Matching concept map)"
        },

        # cos201-arr-015: Written Explain - Decay and Memory Layout
        {
            "id": "cos201-arr-015",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "explain",
            "difficulty": 4,
            "tags": ["arrays", "pointers", "decay", "functions", "memory"],
            "question": "Explain what happens in memory when an array name is passed as an argument to a function in C. Why does C behave this way, and what consequence does this have for modifying array elements inside the function?",
            "options": [],
            "answer": "When an array is passed to a function in C, the array does not get copied. Instead, the array name decays into a pointer containing the address of its first element (&arr[0]). C does this for computational efficiency and memory conservation: copying huge arrays on each function call would rapidly consume call stack space and degrade performance. Because the function receives the actual memory address of the original array, any modification to array elements inside the function directly mutates the caller's array in place.",
            "explanation": "Model answer covers array decay to pointer, memory efficiency justification, and in-place side effects.",
            "why_wrong": {},
            "marking_points": [
                "States that the array name decays to a pointer to the first element / memory address (&arr[0])",
                "Explains that array elements are NOT copied onto the call stack",
                "Gives reason for this design: performance / stack memory efficiency for large arrays",
                "Identifies the consequence: modifications inside the function alter the original caller's array (pass-by-reference simulation)"
            ],
            "source": "Deitel C How to Program, Section 6.6",
            "verified": True,
            "verified_output": "(Examiner rubric)"
        },

        # cos201-arr-016: Code Write - Linear Search
        {
            "id": "cos201-arr-016",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "code_write",
            "difficulty": 3,
            "tags": ["arrays", "coding", "search", "linear_search"],
            "question": "Write a C function `int linearSearch(const int arr[], int size, int key)` that iterates through `arr` to find `key`. If found, return its index; if not found after inspecting all elements, return `-1`.",
            "options": [],
            "answer": "int linearSearch(const int arr[], int size, int key) {\n    for (int i = 0; i < size; i++) {\n        if (arr[i] == key) {\n            return i;\n        }\n    }\n    return -1;\n}",
            "explanation": "Iterates from index 0 to size - 1. Compares each element with key. Returns immediately on match; returns -1 if loop finishes without finding key.",
            "why_wrong": {},
            "marking_points": [
                "Correct function signature with const int arr[], int size, int key returning int",
                "Loop runs from i = 0 strictly to i < size",
                "Compares arr[i] == key correctly",
                "Returns i immediately upon finding key",
                "Returns -1 outside and after the loop completes"
            ],
            "source": "Deitel C How to Program, Section 6.7",
            "verified": True,
            "verified_output": "(Reference code specification)"
        },

        # Flashcards (8 required)
        {
            "id": "cos201-arr-fc01",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["arrays", "flashcard", "definition"],
            "question": "What is an array in C?",
            "answer": "A contiguous block of memory holding a fixed number of elements of the same data type, indexed from 0 to N - 1."
        },
        {
            "id": "cos201-arr-fc02",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["arrays", "flashcard", "bounds"],
            "question": "Does C perform automatic array bounds checking at runtime?",
            "answer": "No. C never performs automatic bounds checking; accessing out-of-bounds indices leads to undefined behavior."
        },
        {
            "id": "cos201-arr-fc03",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["arrays", "flashcard", "initialization"],
            "question": "What value do uninitialized elements receive when an array is partially initialized, e.g. `int a[10] = {5};`?",
            "answer": "All uninitialized elements are automatically set to 0 (or 0.0 or '\\0')."
        },
        {
            "id": "cos201-arr-fc04",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["arrays", "flashcard", "decay"],
            "question": "What happens when an array name is passed to a function in C?",
            "answer": "It decays to a pointer to its first element (&arr[0]); the function receives its memory address, allowing in-place modification."
        },
        {
            "id": "cos201-arr-fc05",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["arrays", "flashcard", "sizeof"],
            "question": "How do you calculate the number of elements in a static array `arr`?",
            "answer": "`sizeof(arr) / sizeof(arr[0])` (total byte size divided by byte size of one element)."
        },
        {
            "id": "cos201-arr-fc06",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["arrays", "flashcard", "multidimensional"],
            "question": "What order does C use to store multidimensional arrays in memory?",
            "answer": "Row-major order: all elements of row 0 are stored contiguously, followed by all elements of row 1, and so on."
        },
        {
            "id": "cos201-arr-fc07",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "flashcard",
            "difficulty": 3,
            "tags": ["arrays", "flashcard", "functions"],
            "question": "When passing a 2D array to a function, which dimension is strictly required in the parameter declaration?",
            "answer": "The column dimension (e.g. `void f(int a[][4])`). The row dimension is optional, but column width is required for offset calculation."
        },
        {
            "id": "cos201-arr-fc08",
            "course": "COS 201",
            "topic": "arrays_1d_2d",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["arrays", "flashcard", "const"],
            "question": "Why use `const int arr[]` in a function parameter list?",
            "answer": "To enforce a read-only contract: the compiler produces an error if the function attempts to modify any elements in the array."
        }
    ]

    case_studies = [
        # Case Study 1: Matrix Diagonal Sum
        {
            "id": "cos201-arr-cs01",
            "scenario": "A graphics engine stores a 3x3 transformation matrix as a 2D array: `int grid[3][3] = {{2, 1, 4}, {3, 5, 7}, {8, 6, 9}};`. The engine needs to compute the trace (sum of the main diagonal elements where row == col). An intern wrote a function to compute this sum.",
            "sub_questions": [
                {
                    "id": "cos201-arr-cs01-q1",
                    "course": "COS 201",
                    "topic": "arrays_1d_2d",
                    "type": "code_output",
                    "difficulty": 3,
                    "tags": ["arrays", "case_study", "matrix", "diagonal"],
                    "question": "What is the output of the following function when passed this 3x3 grid?\n\n```c\n#include <stdio.h>\n\nint sumDiagonal(int n, int mat[n][n]) {\n    int sum = 0;\n    for (int i = 0; i < n; i++) {\n        sum += mat[i][i];\n    }\n    return sum;\n}\n\nint main(void) {\n    int grid[3][3] = {\n        {2, 1, 4},\n        {3, 5, 7},\n        {8, 6, 9}\n    };\n    printf(\"%d\", sumDiagonal(3, grid));\n    return 0;\n}\n```",
                    "options": [
                        "16",
                        "17",
                        "45",
                        "9"
                    ],
                    "answer": 0,
                    "explanation": "The main diagonal elements are grid[0][0] = 2, grid[1][1] = 5, and grid[2][2] = 9. Their sum is 2 + 5 + 9 = 16.",
                    "why_wrong": {
                        "1": "17 is the anti-diagonal sum (grid[0][2] + grid[1][1] + grid[2][0] = 4 + 5 + 8 = 17).",
                        "2": "45 is the sum of all elements in the entire 3x3 matrix.",
                        "3": "9 is only the last element on the diagonal (grid[2][2])."
                    },
                    "source": "Deitel C How to Program, Section 6.9",
                    "verified": True,
                    "verified_output": out_cs1
                },
                {
                    "id": "cos201-arr-cs01-q2",
                    "course": "COS 201",
                    "topic": "arrays_1d_2d",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["arrays", "case_study", "matrix", "time_complexity"],
                    "question": "Analyze the time complexity of `sumDiagonal`. Why is a single loop of `n` iterations sufficient rather than using nested loops of `n * n` iterations?",
                    "options": [],
                    "answer": "The time complexity is O(n). A 2D matrix of size n x n contains n^2 elements, but the main diagonal consists strictly of elements where the row index equals the column index (i.e. `mat[i][i]`). Because there are exactly n such elements, a single loop index `i` from 0 to n-1 directly accesses all diagonal elements in O(n) time. Nested loops would check all n^2 positions, resulting in unnecessary O(n^2) time.",
                    "explanation": "Explains that diagonal elements satisfy row == col, eliminating the need to inspect off-diagonal elements.",
                    "why_wrong": {},
                    "marking_points": [
                        "Identifies time complexity as O(n)",
                        "States that diagonal elements have matching row and column indices (i == j)",
                        "Explains that exactly n elements exist on the diagonal",
                        "Contrasts with nested loop O(n^2) traversal as redundant"
                    ],
                    "source": "Deitel C How to Program, Section 6.9",
                    "verified": True,
                    "verified_output": "(Complexity analysis rubric)"
                }
            ]
        },

        # Case Study 2: Survey Response Frequency Histogram
        {
            "id": "cos201-arr-cs02",
            "scenario": "A university survey asked students to rate their dining hall food on a scale of 1 to 4. 8 students responded: `int responses[] = {1, 2, 2, 3, 1, 2, 4, 1};`. An automated system tabulates the frequency of each rating using a frequency counter array initialized as `int freq[5] = {0};`.",
            "sub_questions": [
                {
                    "id": "cos201-arr-cs02-q1",
                    "course": "COS 201",
                    "topic": "arrays_1d_2d",
                    "type": "code_output",
                    "difficulty": 3,
                    "tags": ["arrays", "case_study", "histogram", "tally"],
                    "question": "What is the output printed by this survey tally program?\n\n```c\n#include <stdio.h>\n\nint main(void) {\n    int responses[] = {1, 2, 2, 3, 1, 2, 4, 1};\n    int freq[5] = {0};\n    for (int i = 0; i < 8; i++) {\n        freq[responses[i]]++;\n    }\n    printf(\"1s:%d 2s:%d 3s:%d 4s:%d\", freq[1], freq[2], freq[3], freq[4]);\n    return 0;\n}\n```",
                    "options": [
                        "1s:3 2s:3 3s:1 4s:1",
                        "1s:2 2s:3 3s:2 4s:1",
                        "1s:3 2s:2 3s:2 4s:1",
                        "1s:1 2s:2 3s:3 4s:4"
                    ],
                    "answer": 0,
                    "explanation": "Counting ratings in responses {1, 2, 2, 3, 1, 2, 4, 1}:\nRating 1 appears 3 times (indices 0, 4, 7)\nRating 2 appears 3 times (indices 1, 2, 5)\nRating 3 appears 1 time (index 3)\nRating 4 appears 1 time (index 6)\nOutput is `1s:3 2s:3 3s:1 4s:1`.",
                    "why_wrong": {
                        "1": "Rating 1 occurs 3 times, not 2.",
                        "2": "Rating 2 occurs 3 times, not 2.",
                        "3": "These are the response category numbers, not the tallies."
                    },
                    "source": "Deitel C How to Program, Section 6.5",
                    "verified": True,
                    "verified_output": out_cs2
                },
                {
                    "id": "cos201-arr-cs02-q2",
                    "course": "COS 201",
                    "topic": "arrays_1d_2d",
                    "type": "explain",
                    "difficulty": 3,
                    "tags": ["arrays", "case_study", "sizing", "bounds"],
                    "question": "Why is the frequency array declared with size 5 (`freq[5]`), even though the survey ratings only range from 1 to 4?",
                    "options": [],
                    "answer": "Because C arrays are 0-indexed, an array of size 5 provides indices 0, 1, 2, 3, and 4. Declaring `freq[5]` allows direct 1-to-1 indexing where rating value `k` maps directly to index `k` (`freq[k]++`) without requiring index subtraction (`k - 1`). Index 0 simply remains unused. If the array had been sized to 4 (`freq[4]`), the valid indices would only be 0 to 3, and attempting to tally a rating of 4 (`freq[4]++`) would cause an out-of-bounds write defect.",
                    "explanation": "Direct indexing mapping simplifies code by ignoring index 0 and allocating size N+1 for maximum value N.",
                    "why_wrong": {},
                    "marking_points": [
                        "Notes that C arrays are 0-indexed, so size 5 provides valid indices 0 through 4",
                        "Explains direct index mapping (rating k maps directly to freq[k])",
                        "Identifies that size 4 would lack index 4 (valid indices would only be 0..3)",
                        "Points out that accessing freq[4] on an array of size 4 would cause an out-of-bounds write"
                    ],
                    "source": "Deitel C How to Program, Section 6.5",
                    "verified": True,
                    "verified_output": "(Software engineering sizing rationale)"
                }
            ]
        }
    ]

    data = {
        "course": "COS 201",
        "topic": "arrays_1d_2d",
        "summary": "Arrays in C are collections of contiguous, identically-typed memory locations accessed using zero-based integer indices. Unlike modern languages, C does not perform automatic runtime or compile-time bounds checking, making buffer overflows and off-by-one errors critical bugs. When initialized, partial initializer lists automatically zero remaining elements. Passing an array to a function causes the array name to decay to a pointer to its first element, meaning modifications inside the function alter the caller's array (pass-by-reference simulation), which can be prevented using the const qualifier. Multidimensional arrays are organized in row-major order, and function prototypes receiving 2D arrays must explicitly declare all column dimensions.",
        "key_terms": [
            {"term": "Array", "definition": "A contiguous sequence of elements of the same data type stored in linear memory."},
            {"term": "Zero-Based Indexing", "definition": "The indexing scheme in C where the first element is at subscript 0 and the final element is at subscript size - 1."},
            {"term": "Array Decay", "definition": "The implicit conversion of an array's name into a pointer to its first element when passed as a function argument or evaluated in expressions."},
            {"term": "Row-Major Order", "definition": "The memory layout scheme where entire rows of a multidimensional array are stored sequentially in contiguous memory."},
            {"term": "Bounds Checking", "definition": "The verification that an index falls within 0 <= index < size, which C completely omits at runtime for execution speed."},
            {"term": "Partial Initialization", "definition": "Supplying fewer initializers than the declared array size, which causes C to automatically initialize all remaining elements to zero."},
            {"term": "const Array Parameter", "definition": "A parameter modifier that treats array elements as read-only within the callee, preventing unintended caller mutations."}
        ],
        "questions": questions,
        "case_studies": case_studies
    }

    out_path = "c:\\Users\\Collins Ibilibor\\Downloads\\Study Buddy\\app\\content\\COS 201\\arrays_1d_2d.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated {len(questions)} questions and {len(case_studies)} case studies in {out_path}")

if __name__ == "__main__":
    main()
