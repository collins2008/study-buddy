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
    print("Compiling and verifying Topic 7 (Pointers & Memory) code snippets with GCC...")

    # Snippet 1: Pointer swap simulation
    code_swap = """#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int x = 10, y = 20;
    swap(&x, &y);
    printf("x=%d y=%d", x, y);
    return 0;
}
"""
    out_swap = compile_and_run(code_swap)

    # Snippet 2: Pointer arithmetic offset
    code_arith = """#include <stdio.h>

int main(void) {
    int arr[] = {10, 20, 30, 40, 50};
    int *p = arr;
    p += 2;
    printf("%d", *p);
    return 0;
}
"""
    out_arith = compile_and_run(code_arith)

    # Snippet 3: Dereferencing and mutation
    code_deref = """#include <stdio.h>

int main(void) {
    int val = 5;
    int *ptr = &val;
    *ptr = *ptr * 4;
    printf("val=%d *ptr=%d", val, *ptr);
    return 0;
}
"""
    out_deref = compile_and_run(code_deref)

    # Snippet 4: Array subscription equivalence *(arr + i)
    code_equiv = """#include <stdio.h>

int main(void) {
    int a[4] = {100, 200, 300, 400};
    int sum = *(a + 1) + *(a + 3);
    printf("%d", sum);
    return 0;
}
"""
    out_equiv = compile_and_run(code_equiv)

    # Snippet 5: Pointer post-increment in loop
    code_inc = """#include <stdio.h>

int main(void) {
    int nums[] = {3, 7, 11};
    int *ptr = nums;
    int total = *ptr++;
    total += *ptr;
    printf("%d", total);
    return 0;
}
"""
    out_inc = compile_and_run(code_inc)

    # Snippet 6: Dynamic allocation malloc and free
    code_malloc = """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = (int *)malloc(3 * sizeof(int));
    if (p == NULL) return 1;
    p[0] = 5; p[1] = 10; p[2] = 15;
    printf("%d", p[0] + p[1] + p[2]);
    free(p);
    return 0;
}
"""
    out_malloc = compile_and_run(code_malloc)

    # Snippet 7: Case study 1 - pointer-based string traversal
    code_cs1 = """#include <stdio.h>

int countVowels(const char *s) {
    int count = 0;
    while (*s != '\\0') {
        if (*s == 'a' || *s == 'e' || *s == 'i' || *s == 'o' || *s == 'u') {
            count++;
        }
        s++;
    }
    return count;
}

int main(void) {
    char word[] = "university";
    printf("%d", countVowels(word));
    return 0;
}
"""
    out_cs1 = compile_and_run(code_cs1)

    # Snippet 8: Case study 2 - dynamic array copy
    code_cs2 = """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int src[3] = {11, 22, 33};
    int *dest = malloc(3 * sizeof(int));
    if (!dest) return 1;
    for (int i = 0; i < 3; i++) {
        *(dest + i) = *(src + i) + 1;
    }
    printf("%d %d %d", dest[0], dest[1], dest[2]);
    free(dest);
    return 0;
}
"""
    out_cs2 = compile_and_run(code_cs2)

    questions = [
        # cos201-ptr-001: Past Q32 pointer declaration
        {
            "id": "cos201-ptr-001",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "mcq",
            "difficulty": 1,
            "tags": ["pointers", "declaration", "syntax", "past_exam"],
            "question": "In the declaration `int *ptr;`, what does `*` signify and what does `ptr` store?",
            "options": [
                "`*` indicates ptr is a pointer variable, and ptr stores the memory address of an integer",
                "`*` is the multiplication operator, initializing ptr to 0",
                "`*` indicates ptr stores a floating-point number",
                "`*` indicates ptr is a constant variable that cannot be changed"
            ],
            "answer": 0,
            "explanation": "In a declaration, the asterisk `*` indicates that the variable being declared is a pointer. Here, `int *ptr;` designates `ptr` as a variable capable of storing the memory address of an integer.",
            "why_wrong": {
                "1": "In a type declaration, `*` is a type modifier designating pointer type, not arithmetic multiplication.",
                "2": "`int *` indicates a pointer to an `int`, not a float.",
                "3": "Pointers are mutable by default; making a pointer constant requires the `const` keyword."
            },
            "source": "Deitel C How to Program, Section 7.3; Nile Past Exam Q32",
            "verified": True,
            "verified_output": "(Language specification rule)"
        },

        # cos201-ptr-002: Address-of vs dereference operators
        {
            "id": "cos201-ptr-002",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["pointers", "operators", "address_of", "dereference"],
            "question": "Which unary operator is used to obtain the memory address of a variable, and which unary operator accesses the value at that memory address?",
            "options": [
                "`&` obtains the address; `*` accesses the value (dereferencing)",
                "`*` obtains the address; `&` accesses the value",
                "`%` obtains the address; `->` accesses the value",
                "`sizeof` obtains the address; `&` accesses the value"
            ],
            "answer": 0,
            "explanation": "`&` is the address-of operator, returning the memory address of its operand. `*` is the indirection or dereferencing operator, returning an lvalue representing the data stored at the pointer's target address.",
            "why_wrong": {
                "1": "This reverses the two operators: `&` is address-of, `*` is dereference.",
                "2": "`%` is modulus; `->` is structure member pointer operator.",
                "3": "`sizeof` returns the byte size of a type or variable, not its memory address."
            },
            "source": "Deitel C How to Program, Section 7.3",
            "verified": True,
            "verified_output": "(Language specification rule)"
        },

        # cos201-ptr-003: Pointer dereference and mutation
        {
            "id": "cos201-ptr-003",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "code_output",
            "difficulty": 2,
            "tags": ["pointers", "dereference", "mutation"],
            "question": "What is the exact output of the following C code snippet?\n\n```c\n#include <stdio.h>\n\nint main(void) {\n    int val = 5;\n    int *ptr = &val;\n    *ptr = *ptr * 4;\n    printf(\"val=%d *ptr=%d\", val, *ptr);\n    return 0;\n}\n```",
            "options": [
                "val=20 *ptr=20",
                "val=5 *ptr=20",
                "val=20 *ptr=5",
                "val=5 *ptr=5"
            ],
            "answer": 0,
            "explanation": "`ptr` holds the memory address of `val` (`&val`). Modifying `*ptr = *ptr * 4;` alters the memory location where `val` lives, setting it to 5 * 4 = 20. Because `val` and `*ptr` refer to the exact same memory location, both evaluate to 20.",
            "why_wrong": {
                "1": "Assigning through `*ptr` directly modifies `val` in place.",
                "2": "Both `val` and `*ptr` reference the exact same memory cell.",
                "3": "The multiplication `*ptr * 4` was successfully executed and stored."
            },
            "source": "Deitel C How to Program, Section 7.3",
            "verified": True,
            "verified_output": out_deref
        },

        # cos201-ptr-004: Pass-by-reference swap
        {
            "id": "cos201-ptr-004",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "code_output",
            "difficulty": 3,
            "tags": ["pointers", "functions", "pass_by_reference", "swap"],
            "question": "What does the following program print?\n\n```c\n#include <stdio.h>\n\nvoid swap(int *a, int *b) {\n    int temp = *a;\n    *a = *b;\n    *b = temp;\n}\n\nint main(void) {\n    int x = 10, y = 20;\n    swap(&x, &y);\n    printf(\"x=%d y=%d\", x, y);\n    return 0;\n}\n```",
            "options": [
                "x=20 y=10",
                "x=10 y=20",
                "x=10 y=10",
                "x=20 y=20"
            ],
            "answer": 0,
            "explanation": "By passing the addresses of x and y (`&x, &y`) into pointer parameters `int *a, int *b`, the `swap` function dereferences the pointers to exchange the values in `main`'s stack frame. Thus `x` becomes 20 and `y` becomes 10.",
            "why_wrong": {
                "1": "Values would remain unchanged only if passed by value (`void swap(int a, int b)`) without pointers.",
                "2": "The temp variable preserves `*a` before overwriting it, so neither value is lost.",
                "3": "`y` received the original value of `x` (10), not 20."
            },
            "source": "Deitel C How to Program, Section 7.4",
            "verified": True,
            "verified_output": out_swap
        },

        # cos201-ptr-005: Pointer arithmetic byte scaling
        {
            "id": "cos201-ptr-005",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["pointers", "pointer_arithmetic", "scaling", "memory"],
            "question": "On a computer where `sizeof(int)` is 4 bytes, if pointer `p` holds the memory address `0x1000`, what address does the expression `p + 3` evaluate to?",
            "options": [
                "0x100C (or 0x1000 + 12 bytes)",
                "0x1003 (or 0x1000 + 3 bytes)",
                "0x1007 (or 0x1000 + 7 bytes)",
                "0x1010 (or 0x1000 + 16 bytes)"
            ],
            "answer": 0,
            "explanation": "Pointer arithmetic in C is automatically scaled by the size of the underlying data type. Incrementing a pointer `p` of type `T*` by integer `k` adds `k * sizeof(T)` bytes to the memory address. Here, `3 * sizeof(int) = 3 * 4 = 12 bytes` (which is `0xC` in hexadecimal), so the resulting address is `0x100C`.",
            "why_wrong": {
                "1": "Pointer arithmetic does not advance by raw single bytes unless `p` is a `char*`.",
                "2": "7 bytes is an arbitrary number with no relationship to 4-byte integers.",
                "3": "16 bytes corresponds to adding 4 integers, not 3."
            },
            "source": "Deitel C How to Program, Section 7.6",
            "verified": True,
            "verified_output": "(Pointer arithmetic specification rule)"
        },

        # cos201-ptr-006: Pointer arithmetic array access
        {
            "id": "cos201-ptr-006",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "code_output",
            "difficulty": 3,
            "tags": ["pointers", "pointer_arithmetic", "arrays"],
            "question": "What is the output of the following C code?\n\n```c\n#include <stdio.h>\n\nint main(void) {\n    int arr[] = {10, 20, 30, 40, 50};\n    int *p = arr;\n    p += 2;\n    printf(\"%d\", *p);\n    return 0;\n}\n```",
            "options": [
                "30",
                "20",
                "40",
                "10"
            ],
            "answer": 0,
            "explanation": "`p` initially points to `arr[0]` (10). Doing `p += 2;` moves the pointer forward by 2 elements, pointing to `arr[2]`. Dereferencing `*p` yields 30.",
            "why_wrong": {
                "1": "20 is arr[1], reached by `p += 1`.",
                "2": "40 is arr[3], reached by `p += 3`.",
                "3": "10 is the initial element arr[0] before `p += 2`."
            },
            "source": "Deitel C How to Program, Section 7.6",
            "verified": True,
            "verified_output": out_arith
        },

        # cos201-ptr-007: Array subscription equivalence *(a + i)
        {
            "id": "cos201-ptr-007",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "code_output",
            "difficulty": 3,
            "tags": ["pointers", "arrays", "equivalence"],
            "question": "What is the exact output of the following program?\n\n```c\n#include <stdio.h>\n\nint main(void) {\n    int a[4] = {100, 200, 300, 400};\n    int sum = *(a + 1) + *(a + 3);\n    printf(\"%d\", sum);\n    return 0;\n}\n```",
            "options": [
                "600",
                "400",
                "500",
                "300"
            ],
            "answer": 0,
            "explanation": "In C, `*(a + i)` is completely identical to `a[i]`. Thus `*(a + 1)` is `a[1]` (200), and `*(a + 3)` is `a[3]` (400). `sum = 200 + 400 = 600`.",
            "why_wrong": {
                "1": "400 is just a[3] alone.",
                "2": "500 would be a[0] + a[3] (100 + 400).",
                "3": "300 is a[0] + a[1] (100 + 200)."
            },
            "source": "Deitel C How to Program, Section 7.7",
            "verified": True,
            "verified_output": out_equiv
        },

        # cos201-ptr-008: const pointer vs pointer to const
        {
            "id": "cos201-ptr-008",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "mcq",
            "difficulty": 4,
            "tags": ["pointers", "const", "syntax", "types"],
            "question": "Consider the declarations:\n1) `const int *ptr1;`\n2) `int * const ptr2 = &x;`\nWhich statement accurately describes their mutability?",
            "options": [
                "`ptr1` is a pointer to constant integer (the data cannot change, but the pointer can point elsewhere); `ptr2` is a constant pointer (the address cannot change, but the data can be modified)",
                "`ptr1` is a constant pointer; `ptr2` is a pointer to a constant integer",
                "Both `ptr1` and `ptr2` prevent modifications to both the address and the integer value",
                "Neither declaration enforces any restriction in standard C"
            ],
            "answer": 0,
            "explanation": "Rule: read declarations right-to-left. `const int *ptr1` -> `ptr1` is a pointer to `int const` (data is constant: `*ptr1 = 5;` is illegal, but `ptr1 = &y;` is legal). `int * const ptr2` -> `ptr2` is a `const` pointer to `int` (pointer is constant: `ptr2 = &y;` is illegal, but `*ptr2 = 5;` is legal).",
            "why_wrong": {
                "1": "This reverses the two meanings.",
                "2": "To freeze both pointer and data, one must write `const int * const ptr`.",
                "3": "`const` is strictly enforced by the C compiler, causing compilation errors on violation."
            },
            "source": "Deitel C How to Program, Section 7.5",
            "verified": True,
            "verified_output": "(Language specification rule)"
        },

        # cos201-ptr-009: Multiple pointer declaration syntax pitfall
        {
            "id": "cos201-ptr-009",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["pointers", "declaration", "syntax", "pitfall"],
            "question": "What are the data types of variables `p1` and `p2` in the declaration statement `int* p1, p2;`?",
            "options": [
                "`p1` is a pointer to `int` (`int*`), while `p2` is a normal integer (`int`)",
                "Both `p1` and `p2` are pointers to `int` (`int*`)",
                "Both `p1` and `p2` are normal integers (`int`)",
                "The statement produces a syntax compilation error in C"
            ],
            "answer": 0,
            "explanation": "In C, the asterisk binds to the variable identifier, not the type specifier. Therefore, `int* p1, p2;` declares `p1` as an `int*` and `p2` as an ordinary `int`. To declare both as pointers, each must have an asterisk: `int *p1, *p2;`.",
            "why_wrong": {
                "1": "A common student misconception: the asterisk does NOT distribute across comma-separated declarators.",
                "2": "`p1` has an asterisk prefixing its name, so it is definitely a pointer.",
                "3": "The statement is completely valid C syntax."
            },
            "source": "Deitel C How to Program, Section 7.3",
            "verified": True,
            "verified_output": "(Language syntax rule)"
        },

        # cos201-ptr-010: Post-increment dereference *ptr++
        {
            "id": "cos201-ptr-010",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "code_output",
            "difficulty": 4,
            "tags": ["pointers", "precedence", "dereference", "post_increment"],
            "question": "What is printed by the following code?\n\n```c\n#include <stdio.h>\n\nint main(void) {\n    int nums[] = {3, 7, 11};\n    int *ptr = nums;\n    int total = *ptr++;\n    total += *ptr;\n    printf(\"%d\", total);\n    return 0;\n}\n```",
            "options": [
                "10",
                "6",
                "14",
                "18"
            ],
            "answer": 0,
            "explanation": "In `*ptr++`, postfix `++` has higher precedence than `*`. Postfix `++` increments `ptr` to point to the next element (`nums[1]`), but the expression yields the original pointer value prior to increment. Thus `*ptr++` dereferences `nums[0]` (3). After this statement, `ptr` points to `nums[1]`. Next, `total += *ptr;` adds `nums[1]` (7) to total (3). `3 + 7 = 10`.",
            "why_wrong": {
                "1": "6 would happen if `*ptr` was incremented rather than the pointer address (`(*ptr)++`).",
                "2": "14 would be 7 + 7.",
                "3": "18 would be 7 + 11."
            },
            "source": "Deitel C How to Program, Section 7.6",
            "verified": True,
            "verified_output": out_inc
        },

        # cos201-ptr-011: malloc, checking NULL, and free
        {
            "id": "cos201-ptr-011",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "code_output",
            "difficulty": 3,
            "tags": ["pointers", "memory", "malloc", "free"],
            "question": "What does the following dynamic memory program output?\n\n```c\n#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    int *p = (int *)malloc(3 * sizeof(int));\n    if (p == NULL) return 1;\n    p[0] = 5; p[1] = 10; p[2] = 15;\n    printf(\"%d\", p[0] + p[1] + p[2]);\n    free(p);\n    return 0;\n}\n```",
            "options": [
                "30",
                "15",
                "0",
                "Segmentation fault"
            ],
            "answer": 0,
            "explanation": "`malloc(3 * sizeof(int))` allocates heap memory for 3 integers. `p` can be accessed using standard array subscription notation `p[i]`. The sum is 5 + 10 + 15 = 30. `free(p)` deallocates the heap block cleanly.",
            "why_wrong": {
                "1": "15 is just p[2], not the sum.",
                "2": "malloc does not zero memory, but elements were explicitly assigned 5, 10, 15.",
                "3": "malloc successfully allocates 12 bytes; NULL is not returned under normal operating conditions."
            },
            "source": "Deitel C How to Program, Section 7.11",
            "verified": True,
            "verified_output": out_malloc
        },

        # cos201-ptr-012: Cloze - Pointers and Memory
        {
            "id": "cos201-ptr-012",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "cloze",
            "difficulty": 2,
            "tags": ["pointers", "cloze", "operators"],
            "question": "Complete the statements on pointer operators and memory:\n\nThe [[&]] operator is known as the address-of operator. The [[*]] operator performs indirection or dereferencing. A pointer initialized to [[NULL]] points to no valid memory address. When dynamically allocated heap memory is no longer needed, it must be returned using the [[free]] function to avoid memory leaks.",
            "answer": ["&", "*", "NULL", "free"],
            "explanation": "`&` yields the memory address, `*` accesses the value stored at that address, `NULL` represents a safe unassigned pointer state, and `free()` deallocates heap memory.",
            "why_wrong": {},
            "source": "Deitel C How to Program, Chapter 7",
            "verified": True,
            "verified_output": "(Conceptual terminology)"
        },

        # cos201-ptr-013: Sequencing - Dynamic allocation lifecycle
        {
            "id": "cos201-ptr-013",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "sequencing",
            "difficulty": 3,
            "tags": ["pointers", "memory", "malloc", "lifecycle"],
            "question": "Arrange the standard sequence of operations for safely using dynamically allocated memory in C:",
            "options": [
                "Declare a pointer variable (e.g. `int *ptr = NULL;`)",
                "Call `malloc()` or `calloc()` to allocate required bytes on the heap",
                "Verify whether the returned pointer is `NULL` before using it",
                "Read from and write to the allocated memory buffer",
                "Call `free(ptr)` to release the heap memory",
                "Set `ptr = NULL;` to avoid a dangling pointer"
            ],
            "answer": [0, 1, 2, 3, 4, 5],
            "explanation": "Best practice lifecycle: declare pointer -> allocate -> NULL check -> use buffer -> free -> zero pointer to prevent dangling pointer access.",
            "why_wrong": {},
            "source": "Deitel C How to Program, Section 7.11",
            "verified": True,
            "verified_output": "(Lifecycle sequence)"
        },

        # cos201-ptr-014: Matching - Pointer expressions
        {
            "id": "cos201-ptr-014",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "matching",
            "difficulty": 3,
            "tags": ["pointers", "syntax", "matching"],
            "question": "Match each pointer expression with its precise meaning:",
            "options": [
                "&var",
                "*ptr",
                "ptr + 1",
                "const int *p"
            ],
            "answer": {
                "&var": "Memory address of variable var",
                "*ptr": "Value stored at address in ptr",
                "ptr + 1": "Address of the next element scaled by data type size",
                "const int *p": "Pointer to read-only integer data"
            },
            "explanation": "These four expressions embody address-of, dereferencing, pointer arithmetic scaling, and pointer-to-constant qualifiers.",
            "why_wrong": {},
            "source": "Deitel C How to Program, Chapter 7",
            "verified": True,
            "verified_output": "(Concept map)"
        },

        # cos201-ptr-015: Written Explain - Dangling Pointer vs Memory Leak
        {
            "id": "cos201-ptr-015",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "explain",
            "difficulty": 4,
            "tags": ["pointers", "memory", "dangling_pointer", "memory_leak"],
            "question": "Compare and contrast a 'dangling pointer' and a 'memory leak' in C. Explain how each occurs, the risks associated with each, and how a programmer prevents them.",
            "options": [],
            "answer": "A dangling pointer occurs when a pointer still holds the memory address of a block of memory that has already been deallocated (e.g. freed via free() or a stack variable whose scope has ended). Dereferencing a dangling pointer can cause memory corruption or crashes. It is prevented by setting pointers to NULL immediately after freeing them.\n\nA memory leak occurs when dynamically allocated memory on the heap is no longer freed, and the program loses all pointer references to that address. The operating system cannot reclaim that heap memory until the process terminates. If leaks accumulate, available RAM is exhausted. It is prevented by pairing every malloc/calloc call with a corresponding free() call before the pointer goes out of scope.",
            "explanation": "Contrasts dangling pointers (holding deallocated address) with memory leaks (failing to deallocate unreferenced memory).",
            "why_wrong": {},
            "marking_points": [
                "Defines dangling pointer: pointer retaining address of deallocated/freed memory",
                "Explains consequences of dangling pointer (crashes, undefined behavior, corruption) and prevention (setting to NULL after free)",
                "Defines memory leak: allocated heap memory never freed after losing its referencing pointer",
                "Explains consequences of memory leak (RAM consumption, crash from out-of-memory) and prevention (pairing every malloc with free)"
            ],
            "source": "Deitel C How to Program, Section 7.11",
            "verified": True,
            "verified_output": "(Examiner rubric)"
        },

        # cos201-ptr-016: Code Write - Pointer-based array sum
        {
            "id": "cos201-ptr-016",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "code_write",
            "difficulty": 3,
            "tags": ["pointers", "coding", "pointer_arithmetic"],
            "question": "Write a C function `int sumArrayPtr(const int *start, int size)` that computes and returns the sum of all elements using pure pointer arithmetic (advancing a pointer with `*start` and `start++`), without using the array subscript bracket notation `[]`.",
            "options": [],
            "answer": "int sumArrayPtr(const int *start, int size) {\n    int sum = 0;\n    const int *end = start + size;\n    while (start < end) {\n        sum += *start;\n        start++;\n    }\n    return sum;\n}",
            "explanation": "Advances pointer `start` through memory until it reaches `start + size`. Accumulates `*start` into sum.",
            "why_wrong": {},
            "marking_points": [
                "Correct function header returning int with const int *start and int size",
                "Initializes sum accumulator variable to 0",
                "Advances pointer using start++ or *(start + i)",
                "Avoids array subscript bracket [] notation",
                "Returns the computed sum correctly"
            ],
            "source": "Deitel C How to Program, Section 7.7",
            "verified": True,
            "verified_output": "(Reference code specification)"
        },

        # Flashcards (8 required)
        {
            "id": "cos201-ptr-fc01",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["pointers", "flashcard", "definition"],
            "question": "What is a pointer in C?",
            "answer": "A variable whose value is the memory address of another variable or object.",
            "explanation": "A variable whose value is the memory address of another variable or object."
        },
        {
            "id": "cos201-ptr-fc02",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["pointers", "flashcard", "operators"],
            "question": "What does the unary operator `&` do in C?",
            "answer": "It is the address-of operator; it evaluates to the memory address of its operand.",
            "explanation": "It is the address-of operator; it evaluates to the memory address of its operand."
        },
        {
            "id": "cos201-ptr-fc03",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["pointers", "flashcard", "operators"],
            "question": "What does the unary operator `*` do when applied to a pointer variable?",
            "answer": "It is the dereference (or indirection) operator; it accesses or modifies the value stored at the address pointed to.",
            "explanation": "It is the dereference (or indirection) operator; it accesses or modifies the value stored at the address pointed to."
        },
        {
            "id": "cos201-ptr-fc04",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["pointers", "flashcard", "arithmetic"],
            "question": "How does pointer arithmetic scale when adding an integer `k` to pointer `p` of type `T*`?",
            "answer": "The memory address advances by `k * sizeof(T)` bytes, moving forward by `k` elements.",
            "explanation": "The memory address advances by `k * sizeof(T)` bytes, moving forward by `k` elements."
        },
        {
            "id": "cos201-ptr-fc05",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["pointers", "flashcard", "null"],
            "question": "What is `NULL` in C pointers?",
            "answer": "A macro defined in `<stddef.h>` representing address 0, indicating that the pointer does not point to any valid object.",
            "explanation": "A macro defined in `<stddef.h>` representing address 0, indicating that the pointer does not point to any valid object."
        },
        {
            "id": "cos201-ptr-fc06",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "flashcard",
            "difficulty": 3,
            "tags": ["pointers", "flashcard", "const"],
            "question": "What is the difference between `const int *p` and `int * const p`?",
            "answer": "`const int *p` has constant data (cannot mutate *p); `int * const p` has a constant address (cannot change p to point elsewhere).",
            "explanation": "`const int *p` has constant data (cannot mutate *p); `int * const p` has a constant address (cannot change p to point elsewhere)."
        },
        {
            "id": "cos201-ptr-fc07",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["pointers", "flashcard", "dangling"],
            "question": "What is a dangling pointer?",
            "answer": "A pointer that points to memory that has been freed or deallocated, leading to undefined behavior if dereferenced.",
            "explanation": "A pointer that points to memory that has been freed or deallocated, leading to undefined behavior if dereferenced."
        },
        {
            "id": "cos201-ptr-fc08",
            "course": "COS 201",
            "topic": "pointers_memory",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["pointers", "flashcard", "memory_leak"],
            "question": "What causes a memory leak in C?",
            "answer": "Dynamically allocating memory via `malloc`/`calloc` and failing to call `free()` before all pointers referencing that block are lost.",
            "explanation": "Dynamically allocating memory via `malloc`/`calloc` and failing to call `free()` before all pointers referencing that block are lost."
        }
    ]

    case_studies = [
        # Case Study 1: Pointer string traversal
        {
            "id": "cos201-ptr-cs01",
            "scenario": "A text processing utility traverses strings using a `const char *` pointer without using array index brackets or the `strlen` library function. The programmer implemented `countVowels` to scan characters sequentially until reaching the null terminator `\\0`.",
            "sub_questions": [
                {
                    "id": "cos201-ptr-cs01-q1",
                    "course": "COS 201",
                    "topic": "pointers_memory",
                    "type": "code_output",
                    "difficulty": 3,
                    "tags": ["pointers", "case_study", "strings", "traversal"],
                    "question": "What is the output of this program when counting vowels in `\"university\"`?\n\n```c\n#include <stdio.h>\n\nint countVowels(const char *s) {\n    int count = 0;\n    while (*s != '\\0') {\n        if (*s == 'a' || *s == 'e' || *s == 'i' || *s == 'o' || *s == 'u') {\n            count++;\n        }\n        s++;\n    }\n    return count;\n}\n\nint main(void) {\n    char word[] = \"university\";\n    printf(\"%d\", countVowels(word));\n    return 0;\n}\n```",
                    "options": [
                        "4",
                        "3",
                        "5",
                        "10"
                    ],
                    "answer": 0,
                    "explanation": "In 'university', the vowels are 'u', 'i', 'e', and 'i' (the 'y' is treated as consonant by this function). There are exactly 4 matches. Output is 4.",
                    "why_wrong": {
                        "1": "Misses one of the two 'i's in 'university'.",
                        "2": "5 would count 'y' as a vowel, which is not in the condition.",
                        "3": "10 is the total length of the string 'university'."
                    },
                    "source": "Deitel C How to Program, Section 7.8",
                    "verified": True,
                    "verified_output": out_cs1
                },
                {
                    "id": "cos201-ptr-cs01-q2",
                    "course": "COS 201",
                    "topic": "pointers_memory",
                    "type": "explain",
                    "difficulty": 3,
                    "tags": ["pointers", "case_study", "const", "safety"],
                    "question": "Explain why `countVowels` declares its parameter as `const char *s` rather than `char *s`. What would happen if the function body attempted `*s = 'X';`?",
                    "options": [],
                    "answer": "`countVowels` only needs to read the string characters to tally vowels; it should not modify the caller's string. Declaring `const char *s` enforces a read-only contract. If the function attempted `*s = 'X';`, the C compiler would issue a compilation error ('assignment of read-only location'), catching the unintentional modification at compile time.",
                    "explanation": "const char * provides read-only access and guarantees compiler protection against accidental writes.",
                    "why_wrong": {},
                    "marking_points": [
                        "Identifies read-only intent: function only inspects characters without mutating them",
                        "States that const enforces compiler-level contract",
                        "Explicitly notes that attempting `*s = 'X'` produces a compiler error",
                        "Explains that const allows caller to pass string literals safely"
                    ],
                    "source": "Deitel C How to Program, Section 7.5",
                    "verified": True,
                    "verified_output": "(Language safety explanation)"
                }
            ]
        },

        # Case Study 2: Dynamic Allocation & Offset Arithmetic
        {
            "id": "cos201-ptr-cs02",
            "scenario": "A numerical library copies and increments an array of 3 integers on the heap using `malloc()` and pointer offset notation `*(dest + i)`.",
            "sub_questions": [
                {
                    "id": "cos201-ptr-cs02-q1",
                    "course": "COS 201",
                    "topic": "pointers_memory",
                    "type": "code_output",
                    "difficulty": 3,
                    "tags": ["pointers", "case_study", "malloc", "heap"],
                    "question": "What is printed by this heap allocation program?\n\n```c\n#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    int src[3] = {11, 22, 33};\n    int *dest = malloc(3 * sizeof(int));\n    if (!dest) return 1;\n    for (int i = 0; i < 3; i++) {\n        *(dest + i) = *(src + i) + 1;\n    }\n    printf(\"%d %d %d\", dest[0], dest[1], dest[2]);\n    free(dest);\n    return 0;\n}\n```",
                    "options": [
                        "12 23 34",
                        "11 22 33",
                        "12 22 33",
                        "0 0 0"
                    ],
                    "answer": 0,
                    "explanation": "Each element `*(src + i)` is incremented by 1 and written to `*(dest + i)`. 11+1=12, 22+1=23, 33+1=34. `dest[0], dest[1], dest[2]` prints `12 23 34`.",
                    "why_wrong": {
                        "1": "Elements were incremented by 1, not copied verbatim.",
                        "2": "All 3 elements in the loop are incremented, not just index 0.",
                        "3": "dest was populated with the computed values before printing."
                    },
                    "source": "Deitel C How to Program, Section 7.11",
                    "verified": True,
                    "verified_output": out_cs2
                },
                {
                    "id": "cos201-ptr-cs02-q2",
                    "course": "COS 201",
                    "topic": "pointers_memory",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["pointers", "case_study", "malloc", "memory_leak"],
                    "question": "What defect would be introduced if the `free(dest);` statement was omitted, and why is the `if (!dest)` check mandatory after calling `malloc()`?",
                    "options": [],
                    "answer": "Omitting `free(dest)` causes a heap memory leak: the 12 bytes allocated for `dest` remain allocated on the heap until the process exits. If this logic was inside a loop or server process running continuously, heap memory would gradually deplete.\n\nThe `if (!dest)` check is mandatory because `malloc()` returns `NULL` if system memory is exhausted. If `malloc` fails and returns `NULL`, attempting to write to `*(dest + i)` dereferences a NULL pointer, causing an immediate segmentation fault and process crash.",
                    "explanation": "Explains memory leak hazard and NULL pointer dereference crash on allocation failure.",
                    "why_wrong": {},
                    "marking_points": [
                        "Identifies omitting free() as a memory leak on the heap",
                        "Explains cumulative impact: heap exhaustion in long-running programs",
                        "Explains why NULL check is required: malloc returns NULL upon allocation failure",
                        "Explicitly states that dereferencing a NULL pointer triggers a segmentation fault / crash"
                    ],
                    "source": "Deitel C How to Program, Section 7.11",
                    "verified": True,
                    "verified_output": "(Defect analysis rubric)"
                }
            ]
        }
    ]

    data = {
        "course": "COS 201",
        "topic": "pointers_memory",
        "summary": "Pointers in C are variables that store the memory addresses of other variables. The address-of operator (&) extracts a variable's address, while the dereferencing operator (*) accesses or mutates the value residing at that address. While C is strictly pass-by-value, passing pointer addresses allows functions to simulate pass-by-reference and modify caller variables in place. Pointer arithmetic advances memory addresses scaled by the byte size of the pointed-to type. Array subscription arr[i] is completely equivalent to *(arr + i). To ensure safety, const qualifiers can create pointers to constant data (read-only) or constant pointers (fixed address). Dynamic memory allocation on the heap via malloc and calloc requires defensive NULL validation and mandatory deallocation with free() to eliminate dangling pointers and memory leaks.",
        "key_terms": [
            {"term": "Pointer", "definition": "A variable holding the memory address of another variable."},
            {"term": "Address-of Operator (&)", "definition": "A unary operator yielding the memory address of an lvalue."},
            {"term": "Dereference Operator (*)", "definition": "A unary operator accessing the data stored at the memory location in a pointer."},
            {"term": "Pointer Arithmetic", "definition": "Advancing or rewinding pointers scaled automatically by sizeof(type)."},
            {"term": "NULL Pointer", "definition": "A pointer assigned address 0, designating that it points to no valid memory."},
            {"term": "Dangling Pointer", "definition": "A pointer referencing deallocated or out-of-scope memory."},
            {"term": "Memory Leak", "definition": "Heap memory allocated via malloc/calloc that is never freed before losing its referencing pointer."}
        ],
        "questions": questions,
        "case_studies": case_studies
    }

    out_path = "c:\\Users\\Collins Ibilibor\\Downloads\\Study Buddy\\app\\content\\COS 201\\pointers_memory.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated {len(questions)} questions and {len(case_studies)} case studies in {out_path}")

if __name__ == "__main__":
    main()
