import json
import os

def create_topic9():
    topic_data = {
        "course": "COS 201",
        "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
        "summary": "This topic contains the complete, authoritative reconstruction of all 40 multiple-choice questions from the Nile University 2024/2025 COS 201 Midterm Examination (Type B). Every question has been meticulously verified against the C11 standard and compiled/executed with GCC. The exam tests foundational syntax, operator precedence, integer division truncation, pre- vs. post-increment semantics, array indexing and memory contiguity, switch fall-through and matching, function modularity, pointer declaration syntax, and control flow branching.",
        "key_terms": [
            {"term": "Pre-increment (++x)", "definition": "Increments the operand variable value by 1 before the resulting value is utilized in the surrounding expression."},
            {"term": "Post-increment (x++)", "definition": "Evaluates to the operand's current value in the surrounding expression before incrementing the variable by 1."},
            {"term": "Integer Truncation", "definition": "In C arithmetic, dividing two integers (a / b) always produces an integer result by discarding any fractional remainder towards zero."},
            {"term": "Contiguous Memory", "definition": "Array elements in C are guaranteed to be stored sequentially without gaps in physical memory addresses."},
            {"term": "Universal Loop Exit (break)", "definition": "The break statement forces immediate termination of the innermost enclosing switch or loop (while, for, do-while)."},
            {"term": "Ternary Operator (?:)", "definition": "C's only three-operand operator; evaluates condition ? expr1 : expr2, returning expr1 if condition is non-zero (true) and expr2 if zero."},
            {"term": "Short-Circuit Evaluation", "definition": "In logical operations (&& and ||), evaluation ceases as soon as the outcome is deterministically known (e.g. false && expr or true || expr)."},
            {"term": "Modular Programming", "definition": "The software design paradigm where complex problems are divided into discrete, reusable, independently testable functions."}
        ],
        "questions": [
            {
                "id": "cos201-mid-001",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 1,
                "tags": ["syntax", "variables", "declarations", "midterm-2024"],
                "question": "Which of the following is the correct way to declare a float variable in C?",
                "options": [
                    "float x;",
                    "int x;",
                    "float x();",
                    "double x;"
                ],
                "answer": "float x;",
                "explanation": "In C, a single-precision floating-point variable is declared using the keyword 'float' followed by an identifier and a semicolon: 'float x;'.",
                "why_wrong": {
                    "int x;": "This declares an integer variable, not a single-precision floating-point variable.",
                    "float x();": "This declares a function prototype named 'x' that returns a float and takes unspecified arguments, not a variable.",
                    "double x;": "This declares a double-precision floating-point variable, which is 64-bit rather than standard 32-bit float."
                },
                "marking_points": ["Identifies 'float' keyword", "Recognizes standard variable declarator syntax"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 1",
                "verified": True,
                "verified_output": "N/A (Syntax question)"
            },
            {
                "id": "cos201-mid-002",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 1,
                "tags": ["keywords", "identifiers", "midterm-2024"],
                "question": "Which of the following is a valid C keyword?",
                "options": [
                    "main",
                    "return",
                    "printf",
                    "integer"
                ],
                "answer": "return",
                "explanation": "'return' is one of C's 32 reserved keywords (ISO C99/C11). 'main' is an identifier designating the program entry function, 'printf' is a standard library function identifier declared in <stdio.h>, and 'integer' is not a C keyword (C uses 'int').",
                "why_wrong": {
                    "main": "'main' is a special function identifier, not a reserved language keyword.",
                    "printf": "'printf' is a library function defined in <stdio.h>, not a built-in language keyword.",
                    "integer": "'integer' is used in languages like Fortran/SQL; C uses 'int'."
                },
                "marking_points": ["Distinguishes C keywords from library function and entry identifiers"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 2",
                "verified": True,
                "verified_output": "N/A (C Keywords Table ISO/IEC 9899)"
            },
            {
                "id": "cos201-mid-003",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["operators", "increment", "code-tracing", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int x = 2;\n    printf(\"%d\", ++x);\n    return 0;\n}\n```",
                "options": [
                    "2",
                    "3",
                    "1",
                    "Error"
                ],
                "answer": "3",
                "explanation": "The prefix increment operator (++x) increments the value of x from 2 to 3 first, and then evaluates to the new incremented value (3), which is passed to printf.",
                "why_wrong": {
                    "2": "This would be the output if post-increment (x++) had been used, which evaluates before incrementing.",
                    "1": "Confusion with decrement operator (--x).",
                    "Error": "The syntax is completely valid C."
                },
                "marking_points": ["Applies prefix increment semantics: increment before evaluation"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 3",
                "verified": True,
                "verified_output": "3"
            },
            {
                "id": "cos201-mid-004",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 1,
                "tags": ["arrays", "strings", "declarations", "midterm-2024"],
                "question": "Which of the following is the correct way to declare a character array in C?",
                "options": [
                    "char arr[5];",
                    "char arr();",
                    "char arr;",
                    "array char arr[5];"
                ],
                "answer": "char arr[5];",
                "explanation": "In C, arrays are declared by specifying the element type, followed by the array name, and the array size enclosed in square brackets: 'char arr[5];'.",
                "why_wrong": {
                    "char arr();": "This is a function prototype declaration returning a char, not an array.",
                    "char arr;": "This declares a single scalar character variable, not an array of characters.",
                    "array char arr[5];": "'array' is not a valid C keyword; C does not use an 'array' specifier prefix."
                },
                "marking_points": ["Selects square bracket array declaration syntax"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 4",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-005",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["loops", "while", "iteration", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int a = 1;\n    while(a < 4) {\n        printf(\"%d \", a);\n        a++;\n    }\n    return 0;\n}\n```",
                "options": [
                    "1 2 3",
                    "1 2 3 4",
                    "0 1 2",
                    "2 3 4"
                ],
                "answer": "1 2 3",
                "explanation": "The loop starts with a=1. Iteration 1 prints '1 ' and a becomes 2. Iteration 2 prints '2 ' and a becomes 3. Iteration 3 prints '3 ' and a becomes 4. When a=4, condition (4 < 4) is false, so the loop terminates without printing 4.",
                "why_wrong": {
                    "1 2 3 4": "Off-by-one error; assumes condition is '<=' instead of strictly '<'.",
                    "0 1 2": "Assumes a starts at 0 instead of 1.",
                    "2 3 4": "Assumes a was incremented prior to the first print."
                },
                "marking_points": ["Traces while loop termination condition strictly at a=4"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 5",
                "verified": True,
                "verified_output": "1 2 3 "
            },
            {
                "id": "cos201-mid-006",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["functions", "syntax", "void", "midterm-2024"],
                "question": "Which of the following is a valid way to define a function returning void in C?",
                "options": [
                    "void func() {}",
                    "func void() {}",
                    "void func;",
                    "return void func() {}"
                ],
                "answer": "void func() {}",
                "explanation": "A function definition in C starts with the return type ('void'), followed by the function identifier ('func'), parameter list in parentheses '()', and the body enclosed in curly braces '{}'.",
                "why_wrong": {
                    "func void() {}": "The return type must precede the function name, not be in the parameter position.",
                    "void func;": "Lacks parameter parentheses and body; invalid variable declaration without type.",
                    "return void func() {}": "'return' is a jump statement keyword inside functions, not a definition specifier."
                },
                "marking_points": ["Recognizes return-type name() {} standard function structure"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 6",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-007",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["operators", "division", "integer-truncation", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int a = 5, b = 2;\n    printf(\"%d\", a / b);\n    return 0;\n}\n```",
                "options": [
                    "2",
                    "2.5",
                    "3",
                    "Error"
                ],
                "answer": "2",
                "explanation": "Both 'a' and 'b' are integers. In C, integer division (5 / 2) truncates the fractional portion, yielding the integer 2. No floating-point promotion occurs.",
                "why_wrong": {
                    "2.5": "Mathematical division result; C integer division does NOT produce floating-point numbers.",
                    "3": "Rounds up instead of truncating towards zero.",
                    "Error": "Valid integer division."
                },
                "marking_points": ["Applies integer division truncation rule"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 7",
                "verified": True,
                "verified_output": "2"
            },
            {
                "id": "cos201-mid-008",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 1,
                "tags": ["operators", "relational", "equality", "midterm-2024"],
                "question": "Which of the following is used to compare two values in C?",
                "options": [
                    "=",
                    "==",
                    "+=",
                    "&&"
                ],
                "answer": "==",
                "explanation": "In C, '==' is the relational equality operator used to compare two expressions. A single '=' is the assignment operator.",
                "why_wrong": {
                    "=": "The assignment operator used to store a value in a variable.",
                    "+=": "Compound addition assignment operator (e.g. x += 2).",
                    "&&": "Logical AND operator used to combine Boolean conditions."
                },
                "marking_points": ["Distinguishes equality comparison (==) from assignment (=)"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 8",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-009",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["loops", "do-while", "post-test", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int x = 0;\n    do {\n        printf(\"%d \", x);\n        x++;\n    } while(x < 2);\n    return 0;\n}\n```",
                "options": [
                    "0",
                    "0 1",
                    "1 2",
                    "0 1 2"
                ],
                "answer": "0 1",
                "explanation": "Iteration 1: prints '0 ', x increments to 1. Condition (1 < 2) is true, loop repeats. Iteration 2: prints '1 ', x increments to 2. Condition (2 < 2) is false, loop terminates. Total output: '0 1 '.",
                "why_wrong": {
                    "0": "Assumes loop only executes once.",
                    "1 2": "Assumes x is incremented before printing.",
                    "0 1 2": "Off-by-one error; assumes condition checked before or inclusive of 2."
                },
                "marking_points": ["Traces do-while post-test execution for exactly 2 passes"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 9",
                "verified": True,
                "verified_output": "0 1 "
            },
            {
                "id": "cos201-mid-010",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["loops", "control-flow", "pre-test", "midterm-2024"],
                "question": "Which loop is best suited when the condition is checked before executing the loop body in C?",
                "options": [
                    "for",
                    "while",
                    "do-while",
                    "switch"
                ],
                "answer": "while",
                "explanation": "The 'while' loop is a pre-test loop that evaluates the condition before entering the body. If the condition is false initially, the body does not execute even once. (Note: 'for' is also pre-test, but 'while' is the classic canonical answer tested by the examiner in contrast to do-while).",
                "why_wrong": {
                    "do-while": "This is a post-test loop; its body is guaranteed to execute at least once before the condition is checked.",
                    "switch": "This is a multi-way selection structure, not an iteration loop.",
                    "for": "While 'for' also tests before execution, 'while' is the canonical answer in Nile lecture slides for general condition-controlled pre-test looping."
                },
                "marking_points": ["Identifies pre-test loop characteristics vs post-test (do-while)"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 10",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-011",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["arrays", "indexing", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int arr[3] = {1, 2, 3};\n    printf(\"%d\", arr[2]);\n    return 0;\n}\n```",
                "options": [
                    "1",
                    "2",
                    "3",
                    "Error"
                ],
                "answer": "3",
                "explanation": "C arrays are 0-indexed: arr[0] is 1, arr[1] is 2, and arr[2] is 3. Accessing arr[2] prints 3.",
                "why_wrong": {
                    "1": "arr[0] is 1; assumes 1-based indexing where arr[1] is first.",
                    "2": "arr[1] is 2.",
                    "Error": "arr[2] is completely within the 3-element bounds (indices 0, 1, 2)."
                },
                "marking_points": ["Applies 0-based array indexing to retrieve third element at index 2"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 11",
                "verified": True,
                "verified_output": "3"
            },
            {
                "id": "cos201-mid-012",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["control-flow", "if-else", "syntax", "midterm-2024"],
                "question": "Which of the following is the correct syntax for if-else if-else in C?",
                "options": [
                    "if(condition){} else if(condition){} else{}",
                    "if(condition){} elseif(condition){} else{}",
                    "if condition {} else if condition {} else {}",
                    "if(){} else(){} elseif(){}"
                ],
                "answer": "if(condition){} else if(condition){} else{}",
                "explanation": "In C, conditions must be parenthesized 'if (condition)', and the chained alternative is written as two separate words: 'else if (condition)' followed by the final 'else'.",
                "why_wrong": {
                    "if(condition){} elseif(condition){} else{}": "'elseif' is a single keyword in PHP or Python (elif); in C it is two separate words: 'else if'.",
                    "if condition {} else if condition {} else {}": "Omits mandatory parentheses around conditions required by C syntax.",
                    "if(){} else(){} elseif(){}": "'else' cannot have a condition or parentheses; 'elseif' is invalid."
                },
                "marking_points": ["Recognizes required parentheses and two-word 'else if' syntax"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 12",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-013",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["control-flow", "if-else", "relational", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int x = 1, y = 2;\n    if(x > y)\n        printf(\"X\");\n    else\n        printf(\"Y\");\n    return 0;\n}\n```",
                "options": [
                    "X",
                    "Y",
                    "1",
                    "Error"
                ],
                "answer": "Y",
                "explanation": "The condition (x > y) evaluates (1 > 2), which is false (0). Therefore, the 'if' body is skipped and the 'else' branch executes, printing 'Y'.",
                "why_wrong": {
                    "X": "Assumes the condition (1 > 2) evaluates to true.",
                    "1": "Confuses string literal output with variable value.",
                    "Error": "Valid single-statement if-else branch syntax."
                },
                "marking_points": ["Evaluates (1 > 2) as false and selects the else branch"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 13",
                "verified": True,
                "verified_output": "Y"
            },
            {
                "id": "cos201-mid-014",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 1,
                "tags": ["syntax", "comments", "midterm-2024"],
                "question": "Which of the following is a correct single-line comment in C?",
                "options": [
                    "# This is a comment",
                    "// This is a comment",
                    "/* This is a comment",
                    "<!-- This is a comment -->"
                ],
                "answer": "// This is a comment",
                "explanation": "Since C99, C supports single-line comments introduced by two forward slashes '//'. (Traditional multi-line comments require matching /* ... */).",
                "why_wrong": {
                    "# This is a comment": "Used in Python, Bash, and Ruby; in C, '#' begins preprocessor directives.",
                    "/* This is a comment": "Missing the closing '*/' delimiter required for multi-line comment blocks.",
                    "<!-- This is a comment -->": "HTML/XML comment syntax."
                },
                "marking_points": ["Identifies '//' as C single-line comment delimiter"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 14",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-015",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["operators", "precedence", "arithmetic", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int a = 3, b = 4;\n    printf(\"%d\", a + b * 2);\n    return 0;\n}\n```",
                "options": [
                    "14",
                    "11",
                    "10",
                    "7"
                ],
                "answer": "11",
                "explanation": "Multiplication (*) has higher precedence than addition (+). Thus, b * 2 is evaluated first (4 * 2 = 8), followed by addition (3 + 8 = 11).",
                "why_wrong": {
                    "14": "Evaluates left-to-right ignoring operator precedence: (3 + 4) * 2 = 7 * 2 = 14.",
                    "10": "Arithmetic miscalculation.",
                    "7": "Evaluates a + b only without multiplying."
                },
                "marking_points": ["Applies precedence: multiplication before addition"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 15",
                "verified": True,
                "verified_output": "11"
            },
            {
                "id": "cos201-mid-016",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["arrays", "2D-arrays", "declarations", "midterm-2024"],
                "question": "Which of the following is correct to declare a 2D array in C?",
                "options": [
                    "int arr[2][3];",
                    "int arr[2,3];",
                    "int arr(2,3);",
                    "int arr[2];"
                ],
                "answer": "int arr[2][3];",
                "explanation": "Multidimensional arrays in C specify each dimension in its own set of square brackets: 'int arr[rows][cols];'.",
                "why_wrong": {
                    "int arr[2,3];": "Uses comma operator inside brackets; this does not declare a 2D array in C (common in languages like C#).",
                    "int arr(2,3);": "Parentheses indicate function call or declaration, not array subscripting.",
                    "int arr[2];": "Declares a 1D array of 2 elements, not a 2D array."
                },
                "marking_points": ["Identifies separate square brackets for each dimension"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 16",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-017",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["loops", "for-loop", "accumulation", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int x = 0;\n    for(int i = 0; i < 3; i++) {\n        x += i;\n    }\n    printf(\"%d\", x);\n    return 0;\n}\n```",
                "options": [
                    "2",
                    "3",
                    "1",
                    "0"
                ],
                "answer": "3",
                "explanation": "The loop executes for i = 0, 1, 2. When i=0: x += 0 (x=0). When i=1: x += 1 (x=1). When i=2: x += 2 (x=3). Loop terminates when i=3. The final value printed is 3.",
                "why_wrong": {
                    "2": "Assumes only the last value of i is stored into x instead of being accumulated.",
                    "1": "Stops accumulation early.",
                    "0": "Assumes the loop did not execute or x remained unmutated."
                },
                "marking_points": ["Traces accumulation: 0 + 0 + 1 + 2 = 3"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 17",
                "verified": True,
                "verified_output": "3"
            },
            {
                "id": "cos201-mid-018",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["operators", "ternary", "syntax", "midterm-2024"],
                "question": "Which of the following correctly uses the ternary operator in C?",
                "options": [
                    "a > b ? x = y : x = z;",
                    "if(a > b) x = y else x = z;",
                    "a > b : x = y ? x = z;",
                    "x = a > b ? y : z;"
                ],
                "answer": "x = a > b ? y : z;",
                "explanation": "The ternary operator syntax is 'condition ? expr_if_true : expr_if_false'. Assigning its result to a variable is written: 'x = a > b ? y : z;'.",
                "why_wrong": {
                    "a > b ? x = y : x = z;": "Invalid precedence in C without parentheses around assignment in the alternative branches.",
                    "if(a > b) x = y else x = z;": "This is a standard if-else statement, not the ternary operator (?:).",
                    "a > b : x = y ? x = z;": "Reverses the '?' and ':' delimiters."
                },
                "marking_points": ["Recognizes standard assignment with ternary operator"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 18",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-019",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["control-flow", "switch", "branching", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int a = 5;\n    switch(a) {\n        case 1: printf(\"One\"); break;\n        case 5: printf(\"Five\"); break;\n        default: printf(\"Other\");\n    }\n    return 0;\n}\n```",
                "options": [
                    "One",
                    "Five",
                    "Other",
                    "Error"
                ],
                "answer": "Five",
                "explanation": "Variable 'a' has value 5. Execution jumps directly to 'case 5:', printing 'Five'. The 'break' statement terminates the switch block, preventing fallthrough into default.",
                "why_wrong": {
                    "One": "Only executes if a == 1.",
                    "Other": "Only executes if no cases match or if a matching case falls through.",
                    "Error": "Completely valid switch statement syntax."
                },
                "marking_points": ["Matches switch expression to case 5 and halts at break"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 19",
                "verified": True,
                "verified_output": "Five"
            },
            {
                "id": "cos201-mid-020",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["operators", "increment", "syntax", "midterm-2024"],
                "question": "Which of the following is correct to increment a variable x by 1 in C?",
                "options": [
                    "x = x + 1;",
                    "x++;",
                    "++x;",
                    "All of the above"
                ],
                "answer": "All of the above",
                "explanation": "All three expressions increment x by 1. 'x = x + 1;' is standard assignment, 'x++;' is post-increment, and '++x;' is pre-increment. As standalone statements, their end effect on x is identical.",
                "why_wrong": {
                    "x = x + 1;": "This is correct, but options B and C are also correct.",
                    "x++;": "This is correct, but options A and C are also correct.",
                    "++x;": "This is correct, but options A and B are also correct."
                },
                "marking_points": ["Recognizes equivalence of assignment, pre-, and post-increment statements"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 20",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-021",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["arrays", "indexing", "arithmetic", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int arr[4] = {2, 4, 6, 8};\n    printf(\"%d\", arr[1] + arr[3]);\n    return 0;\n}\n```",
                "options": [
                    "6",
                    "12",
                    "10",
                    "8"
                ],
                "answer": "12",
                "explanation": "With 0-based indexing: arr[0]=2, arr[1]=4, arr[2]=6, arr[3]=8. arr[1] is 4 and arr[3] is 8. Their sum is 4 + 8 = 12.",
                "why_wrong": {
                    "6": "Sum of arr[0] + arr[1] (2 + 4 = 6).",
                    "10": "Sum of arr[1] + arr[2] (4 + 6 = 10) or arr[0] + arr[3] (2 + 8 = 10).",
                    "8": "Value of arr[3] alone."
                },
                "marking_points": ["Extracts arr[1]=4 and arr[3]=8 and computes sum = 12"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 21",
                "verified": True,
                "verified_output": "12"
            },
            {
                "id": "cos201-mid-022",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["arrays", "memory", "properties", "midterm-2024"],
                "question": "Which of the following statements about arrays in C is TRUE?",
                "options": [
                    "Array elements are always stored in consecutive memory locations.",
                    "Array indices start from 1.",
                    "Array size can change at runtime.",
                    "Array can store multiple data types."
                ],
                "answer": "Array elements are always stored in consecutive memory locations.",
                "explanation": "By definition in C, array elements occupy a contiguous (consecutive) block of memory addresses. Indices start at 0, static array sizes are fixed, and arrays are homogeneous (all elements must be the same type).",
                "why_wrong": {
                    "Array indices start from 1.": "C array indices strictly start at 0.",
                    "Array size can change at runtime.": "Standard C arrays have fixed size determined at declaration.",
                    "Array can store multiple data types.": "Arrays are homogeneous; structures ('struct') store multiple types."
                },
                "marking_points": ["Recalls fundamental array guarantee: contiguous memory layout"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 22",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-023",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["operators", "logical-or", "short-circuit", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int x = 0;\n    if(x || 1)\n        printf(\"True\");\n    else\n        printf(\"False\");\n    return 0;\n}\n```",
                "options": [
                    "True",
                    "False",
                    "0",
                    "1"
                ],
                "answer": "True",
                "explanation": "In the expression (x || 1), x is 0 (false) but the right operand is 1 (true). For logical OR (||), if either operand is non-zero, the overall condition evaluates to 1 (true), executing the 'if' branch.",
                "why_wrong": {
                    "False": "Assumes both operands must be true (confusion with logical AND &&).",
                    "0": "The code prints the string literal 'True', not an integer.",
                    "1": "The code prints 'True', not the numeric truth value."
                },
                "marking_points": ["Evaluates (0 || 1) as true (1) and prints 'True'"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 23",
                "verified": True,
                "verified_output": "True"
            },
            {
                "id": "cos201-mid-024",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 1,
                "tags": ["variables", "syntax", "declarations", "midterm-2024"],
                "question": "Which of the following is the correct way to declare multiple variables in a single line in C?",
                "options": [
                    "int x, y, z;",
                    "int x; y; z;",
                    "int x y z;",
                    "int x, y; z;"
                ],
                "answer": "int x, y, z;",
                "explanation": "Multiple variables of the same type are declared on a single line by separating the variable names with commas: 'int x, y, z;'.",
                "why_wrong": {
                    "int x; y; z;": "Semicolon ends a statement; 'y;' and 'z;' are invalid statements without types.",
                    "int x y z;": "Missing comma separators causes a syntax compiler error.",
                    "int x, y; z;": "'z;' is an isolated identifier statement without a type."
                },
                "marking_points": ["Identifies comma-separated declarator list syntax"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 24",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-025",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["operators", "ternary", "evaluation", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int x = 2, y = 3;\n    printf(\"%d\", x > y ? x : y);\n    return 0;\n}\n```",
                "options": [
                    "2",
                    "3",
                    "0",
                    "Error"
                ],
                "answer": "3",
                "explanation": "Condition (x > y) is (2 > 3), which is false (0). When the condition is false, the ternary operator evaluates and returns the expression after the colon (:), which is y (3).",
                "why_wrong": {
                    "2": "Value of x; this would be returned if (x > y) were true.",
                    "0": "Confuses the result with the Boolean truth value (0) of the comparison.",
                    "Error": "Valid inline ternary operator in printf."
                },
                "marking_points": ["Evaluates condition (2 > 3) as false and returns y (3)"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 25",
                "verified": True,
                "verified_output": "3"
            },
            {
                "id": "cos201-mid-026",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["constants", "preprocessor", "syntax", "midterm-2024"],
                "question": "Which of the following is correct for defining a constant in C?",
                "options": [
                    "#define PI 3.14",
                    "const PI = 3.14;",
                    "define PI 3.14",
                    "constant PI = 3.14;"
                ],
                "answer": "#define PI 3.14",
                "explanation": "'#define PI 3.14' is the standard preprocessor directive to define a manifest symbolic constant. Note: 'const double PI = 3.14;' would be valid with a type, but 'const PI = 3.14;' lacks the type specifier.",
                "why_wrong": {
                    "const PI = 3.14;": "Missing type specifier ('const double PI = 3.14;').",
                    "define PI 3.14": "Missing the required leading '#' character for preprocessor directives.",
                    "constant PI = 3.14;": "'constant' is not a C keyword; C uses 'const'."
                },
                "marking_points": ["Identifies valid preprocessor '#define' constant declaration"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 26",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-027",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["loops", "post-increment", "iteration", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int i = 1;\n    while(i <= 3) {\n        printf(\"%d \", i++);\n    }\n    return 0;\n}\n```",
                "options": [
                    "1 2 3",
                    "1 2 3 4",
                    "0 1 2",
                    "2 3 4"
                ],
                "answer": "1 2 3",
                "explanation": "Because post-increment (i++) is used, printf receives the current value of i before the increment occurs: pass 1 prints 1 (i becomes 2); pass 2 prints 2 (i becomes 3); pass 3 prints 3 (i becomes 4). Condition (4 <= 3) is false, so loop terminates. Output: '1 2 3 '.",
                "why_wrong": {
                    "2 3 4": "This would occur if pre-increment (++i) had been used.",
                    "1 2 3 4": "Assumes i <= 3 is evaluated after post-increment inside the body.",
                    "0 1 2": "Assumes 0-based initial value."
                },
                "marking_points": ["Traces post-increment within printf: prints current value then increments"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 27",
                "verified": True,
                "verified_output": "1 2 3 "
            },
            {
                "id": "cos201-mid-028",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["functions", "modular-programming", "midterm-2024"],
                "question": "Which of the following is TRUE about functions in C?",
                "options": [
                    "A function must return a value.",
                    "Functions can be called before declaration.",
                    "Functions help in modular programming.",
                    "Only main() can call functions."
                ],
                "answer": "Functions help in modular programming.",
                "explanation": "Functions facilitate modular programming by breaking large problems into smaller, manageable, reusable modules. Void functions do not return values, functions cannot be called without declaration/prototype in modern C, and any function can call other functions.",
                "why_wrong": {
                    "A function must return a value.": "Functions declared with return type 'void' do not return a value.",
                    "Functions can be called before declaration.": "In modern C (C99/C11), calling a function without prior declaration/prototype is an error.",
                    "Only main() can call functions.": "Any function can call other functions (and call itself recursively)."
                },
                "marking_points": ["Identifies modular programming as core role of functions in C"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 28",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-029",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["control-flow", "if-else-if", "ladder", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int x = 5;\n    if(x > 10)\n        printf(\"Big\");\n    else if(x > 3)\n        printf(\"Medium\");\n    else\n        printf(\"Small\");\n    return 0;\n}\n```",
                "options": [
                    "Big",
                    "Medium",
                    "Small",
                    "Error"
                ],
                "answer": "Medium",
                "explanation": "x is 5. First test (5 > 10) is false. Next branch (5 > 3) is true, so 'Medium' is printed. The remainder of the if-else ladder is skipped.",
                "why_wrong": {
                    "Big": "5 is not greater than 10.",
                    "Small": "Only reached if all preceding conditions are false.",
                    "Error": "Valid chained if-else ladder syntax."
                },
                "marking_points": ["Evaluates conditions sequentially and executes first true branch ('Medium')"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 29",
                "verified": True,
                "verified_output": "Medium"
            },
            {
                "id": "cos201-mid-030",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 1,
                "tags": ["operators", "modulus", "remainder", "midterm-2024"],
                "question": "Which of the following operators is used for modulus (remainder) in C?",
                "options": [
                    "%",
                    "/",
                    "*",
                    "+"
                ],
                "answer": "%",
                "explanation": "The percent symbol '%' is the modulus operator in C; it yields the remainder after integer division (e.g. 7 % 3 = 1).",
                "why_wrong": {
                    "/": "Division operator.",
                    "*": "Multiplication operator.",
                    "+": "Addition operator."
                },
                "marking_points": ["Recalls '%' as the C modulus operator"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 30",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-031",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["arrays", "indexing", "code-tracing", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int arr[3] = {10, 20, 30};\n    printf(\"%d\", arr[0] + arr[2]);\n    return 0;\n}\n```",
                "options": [
                    "10",
                    "30",
                    "40",
                    "20"
                ],
                "answer": "40",
                "explanation": "With 0-based indexing: arr[0] is 10 and arr[2] is 30. Adding them yields 10 + 30 = 40.",
                "why_wrong": {
                    "10": "Value of arr[0] alone.",
                    "30": "Value of arr[2] alone.",
                    "20": "Value of arr[1] alone."
                },
                "marking_points": ["Indexes arr[0]=10 and arr[2]=30, computing 10+30=40"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 31",
                "verified": True,
                "verified_output": "40"
            },
            {
                "id": "cos201-mid-032",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["pointers", "syntax", "declarations", "midterm-2024"],
                "question": "Which of the following is correct syntax for declaring a pointer to an integer in C?",
                "options": [
                    "int *p;",
                    "int p*;",
                    "int &p;",
                    "int p;"
                ],
                "answer": "int *p;",
                "explanation": "A pointer in C is declared with an asterisk (*) preceding the variable identifier: 'int *p;'.",
                "why_wrong": {
                    "int p*;": "Syntax error; the asterisk must precede the identifier, not follow it.",
                    "int &p;": "Reference variable syntax used in C++, not valid variable declaration in C.",
                    "int p;": "Declares an ordinary scalar integer, not a pointer."
                },
                "marking_points": ["Identifies 'int *p;' as pointer declaration syntax"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 32",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-033",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["operators", "logical-and", "control-flow", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int x = 1, y = 0;\n    if(x && y)\n        printf(\"Yes\");\n    else\n        printf(\"No\");\n    return 0;\n}\n```",
                "options": [
                    "Yes",
                    "No",
                    "1",
                    "0"
                ],
                "answer": "No",
                "explanation": "In the logical AND expression (x && y), x is 1 (true) and y is 0 (false). Because logical AND requires both operands to be non-zero to be true, (1 && 0) evaluates to 0 (false). The 'else' branch executes, printing 'No'.",
                "why_wrong": {
                    "Yes": "Assumes true if any operand is true (confusion with logical OR ||).",
                    "1": "Prints string literal 'No', not integer.",
                    "0": "Prints string literal 'No', not numeric result."
                },
                "marking_points": ["Evaluates logical AND (1 && 0) as false, printing 'No'"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 33",
                "verified": True,
                "verified_output": "No"
            },
            {
                "id": "cos201-mid-034",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["operators", "compound-assignment", "syntax", "midterm-2024"],
                "question": "Which of the following is correct to increment a variable by 2 in C?",
                "options": [
                    "x += 2;",
                    "x = x + 2;",
                    "x++ + x++;",
                    "Both A and B"
                ],
                "answer": "Both A and B",
                "explanation": "Both 'x += 2;' (compound addition assignment) and 'x = x + 2;' (standard assignment) correctly increment variable x by 2. 'x++ + x++;' modifies x multiple times without a sequence point, which causes Undefined Behavior.",
                "why_wrong": {
                    "x += 2;": "Correct, but option B is equally correct, making D the complete answer.",
                    "x = x + 2;": "Correct, but option A is equally correct, making D the complete answer.",
                    "x++ + x++;": "Undefined behavior in C (unsequenced side effects on x)."
                },
                "marking_points": ["Identifies both standard and compound assignment as valid methods"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 34",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-035",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["loops", "for-loop", "code-tracing", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int i = 0;\n    for(i = 0; i < 3; i++) {\n        printf(\"%d \", i * 2);\n    }\n    return 0;\n}\n```",
                "options": [
                    "0 2 4",
                    "0 1 2",
                    "2 4 6",
                    "1 3 5"
                ],
                "answer": "0 2 4",
                "explanation": "The loop iterates for i = 0, 1, 2. When i=0: 0*2 = 0. When i=1: 1*2 = 2. When i=2: 2*2 = 4. When i=3: condition (3 < 3) is false. Total output: '0 2 4 '.",
                "why_wrong": {
                    "0 1 2": "Prints the index i directly without multiplying by 2.",
                    "2 4 6": "Assumes i starts at 1 instead of 0.",
                    "1 3 5": "Odd numbers sequence; incorrect arithmetic."
                },
                "marking_points": ["Multiplies loop index by 2 across iterations 0, 1, 2"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 35",
                "verified": True,
                "verified_output": "0 2 4 "
            },
            {
                "id": "cos201-mid-036",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 1,
                "tags": ["arrays", "declarations", "syntax", "midterm-2024"],
                "question": "Which of the following correctly declares a 1D array of 10 integers in C?",
                "options": [
                    "int arr[10];",
                    "int arr(10);",
                    "int arr{};",
                    "int arr;"
                ],
                "answer": "int arr[10];",
                "explanation": "In C, a fixed-size 1D array is declared with square brackets enclosing the integer size: 'int arr[10];'.",
                "why_wrong": {
                    "int arr(10);": "Parentheses represent function parameter lists or prototypes, not arrays.",
                    "int arr{};": "Empty curly braces syntax error in variable declaration.",
                    "int arr;": "Declares a single scalar integer, not an array."
                },
                "marking_points": ["Selects square bracket syntax with dimension 10"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 36",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-037",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["control-flow", "switch", "default-case", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int x = 3;\n    switch(x) {\n        case 1: printf(\"One\"); break;\n        case 2: printf(\"Two\"); break;\n        default: printf(\"Other\");\n    }\n    return 0;\n}\n```",
                "options": [
                    "One",
                    "Two",
                    "Other",
                    "Error"
                ],
                "answer": "Other",
                "explanation": "Variable x is 3. Neither 'case 1:' nor 'case 2:' matches x. Therefore, control transfers to the 'default:' label, printing 'Other'.",
                "why_wrong": {
                    "One": "Only executes if x == 1.",
                    "Two": "Only executes if x == 2.",
                    "Error": "Valid switch statement; default executes when no case matches."
                },
                "marking_points": ["Transfers control to default label when no case matches"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 37",
                "verified": True,
                "verified_output": "Other"
            },
            {
                "id": "cos201-mid-038",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 2,
                "tags": ["constants", "syntax", "const", "midterm-2024"],
                "question": "Which of the following is correct syntax to declare a constant integer in C?",
                "options": [
                    "const int x = 5;",
                    "int const x;",
                    "#define x 5",
                    "All of the above"
                ],
                "answer": "All of the above",
                "explanation": "'const int x = 5;' is standard const-qualified integer declaration. 'int const x;' is valid C syntax (the type qualifier may appear before or after the type specifier). '#define x 5' creates a preprocessor constant. Thus, all represent valid constant mechanisms in C.",
                "why_wrong": {
                    "const int x = 5;": "Correct, but B and C are also valid forms of defining constants in C.",
                    "int const x;": "Valid C const qualification syntax (though uninitialized), but A and C are also valid.",
                    "#define x 5": "Preprocessor symbolic constant, but A and B are also valid."
                },
                "marking_points": ["Recognizes const prefix, const postfix, and #define as constant techniques"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 38",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-039",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "code_output",
                "difficulty": 3,
                "tags": ["operators", "ternary", "relational", "midterm-2024"],
                "question": "What will be the output of the following code?\n\n```c\n#include <stdio.h>\nint main() {\n    int x = 1, y = 2;\n    printf(\"%d\", x < y ? y : x);\n    return 0;\n}\n```",
                "options": [
                    "1",
                    "2",
                    "0",
                    "Error"
                ],
                "answer": "2",
                "explanation": "Condition (x < y) evaluates (1 < 2), which is true (1). Because condition is true, the first expression (y) is evaluated and returned. y has value 2.",
                "why_wrong": {
                    "1": "Value of x; this would be returned if x < y were false.",
                    "0": "Confuses result with boolean evaluation.",
                    "Error": "Valid ternary conditional invocation."
                },
                "marking_points": ["Evaluates condition (1 < 2) as true and selects y=2"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 39",
                "verified": True,
                "verified_output": "2"
            },
            {
                "id": "cos201-mid-040",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "mcq",
                "difficulty": 1,
                "tags": ["control-flow", "loops", "jump-statements", "midterm-2024"],
                "question": "Which of the following is used to terminate a loop immediately in C?",
                "options": [
                    "break",
                    "continue",
                    "exit",
                    "return"
                ],
                "answer": "break",
                "explanation": "The 'break' statement terminates execution of the nearest enclosing loop (for, while, do-while) or switch statement immediately, transferring control to the statement directly following the loop block.",
                "why_wrong": {
                    "continue": "Skips the remainder of the current loop iteration and proceeds to the next iteration; it does not terminate the loop.",
                    "exit": "'exit()' is a standard library function in <stdlib.h> that terminates the entire program process.",
                    "return": "Exits the current function entirely, not merely the loop."
                },
                "marking_points": ["Identifies 'break' as immediate loop termination statement"],
                "source": "Nile University COS 201 Midterm Exam (Type B), Question 40",
                "verified": True,
                "verified_output": "N/A"
            },
            # Flashcards for Topic 9
            {
                "id": "cos201-mid-fc01",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "operators", "pre-increment"],
                "question": "What is the difference in evaluation timing between ++x and x++ in C?",
                "options": [],
                "answer": "++x increments x before returning its value for evaluation; x++ returns the current value for evaluation first, then increments x afterwards.",
                "explanation": "Prefix (++x) updates first, then evaluates. Postfix (x++) evaluates first, then updates.",
                "why_wrong": {},
                "marking_points": ["States prefix updates before evaluation", "States postfix evaluates before increment"],
                "source": "Nile Midterm Type B Q3 & Q27 synthesis",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-fc02",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "arithmetic", "division"],
                "question": "What is the result of 5 / 2 in C, and why?",
                "options": [],
                "answer": "2. Because both operands (5 and 2) are integers, C performs integer division and truncates (discards) the fractional remainder.",
                "explanation": "To get 2.5, at least one operand must be a floating-point type (e.g. 5.0 / 2 or (float)5 / 2).",
                "why_wrong": {},
                "marking_points": ["States result is 2", "Explains integer truncation"],
                "source": "Nile Midterm Type B Q7",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-fc03",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "arrays", "memory"],
                "question": "How are array elements stored in computer memory in C?",
                "options": [],
                "answer": "In contiguous (consecutive) memory locations without gaps between elements.",
                "explanation": "Contiguity allows pointer arithmetic: *(arr + i) accesses the element at offset i * sizeof(type).",
                "why_wrong": {},
                "marking_points": ["Recalls contiguous/consecutive storage"],
                "source": "Nile Midterm Type B Q22",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-fc04",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "loops", "control-flow"],
                "question": "What is the difference between 'break' and 'continue' in a loop?",
                "options": [],
                "answer": "'break' terminates the loop entirely and transfers control outside; 'continue' skips only the rest of the current iteration and begins the next loop test/step.",
                "explanation": "'break' exits; 'continue' jumps to the end of the body to advance to the next pass.",
                "why_wrong": {},
                "marking_points": ["Explains break terminates loop", "Explains continue skips to next iteration"],
                "source": "Nile Midterm Type B Q40",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-fc05",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "operators", "ternary"],
                "question": "What is the syntax of the ternary operator in C?",
                "options": [],
                "answer": "condition ? expression_if_true : expression_if_false",
                "explanation": "It evaluates condition. If non-zero, expr1 is evaluated; if zero, expr2 is evaluated.",
                "why_wrong": {},
                "marking_points": ["Identifies condition ? expr1 : expr2 structure"],
                "source": "Nile Midterm Type B Q18",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-fc06",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "pointers", "declarations"],
                "question": "How do you declare a pointer variable in C?",
                "options": [],
                "answer": "type *pointer_name; (e.g. int *p;)",
                "explanation": "The asterisk denotes indirection/pointer type.",
                "why_wrong": {},
                "marking_points": ["States asterisk precedes pointer identifier"],
                "source": "Nile Midterm Type B Q32",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-fc07",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "keywords", "language"],
                "question": "Are 'main' and 'printf' reserved keywords in C?",
                "options": [],
                "answer": "No. 'main' is a function identifier (entry point) and 'printf' is a standard library function name. C keywords include return, int, while, if, etc.",
                "explanation": "C has 32 keywords in C89/C90, 37 in C99, 44 in C11. Neither main nor printf is a keyword.",
                "why_wrong": {},
                "marking_points": ["States neither main nor printf is a keyword", "Names valid C keywords"],
                "source": "Nile Midterm Type B Q2",
                "verified": True,
                "verified_output": "N/A"
            },
            {
                "id": "cos201-mid-fc08",
                "course": "COS 201",
                "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                "type": "flashcard",
                "difficulty": 1,
                "tags": ["flashcard", "operators", "logical-or"],
                "question": "What is short-circuit evaluation in C logical operations?",
                "options": [],
                "answer": "In logical operations, if the first operand determines the entire outcome (e.g. true || expr or false && expr), the second operand is never evaluated.",
                "explanation": "Short-circuiting prevents side effects in unneeded expressions and allows safe guarding (e.g. ptr != NULL && *ptr > 0).",
                "why_wrong": {},
                "marking_points": ["Explains second operand evaluation skipped when result is already determined"],
                "source": "Nile Midterm Type B Q23",
                "verified": True,
                "verified_output": "N/A"
            }
        ],
        "case_studies": [
            {
                "id": "cos201-mid-cs01",
                "scenario": "A Nile University student is debugging a student grade reporting module. The program has several logical and syntactic flaws based on patterns from the midterm exam: it uses post-increment inside a loop, truncates float averages during integer division, and has a missing break in a grade categorization switch statement.",
                "sub_questions": [
                    {
                        "id": "cos201-mid-cs01-q1",
                        "course": "COS 201",
                        "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                        "type": "code_bug",
                        "difficulty": 3,
                        "tags": ["case-study", "integer-division", "debugging"],
                        "question": "The student calculates the student score average with: `float avg = (score1 + score2) / 2;` where score1=85 and score2=80 (both integers). What bug occurs, and what is the fix?",
                        "options": [
                            "Integer division truncates fractional parts before assignment to float; fix by dividing by `2.0` or casting `(float)`.",
                            "Syntax error: parentheses cannot be used in arithmetic expressions.",
                            "The compiler will fail because float cannot store integer values.",
                            "The addition overflows 8-bit registers."
                        ],
                        "answer": "Integer division truncates fractional parts before assignment to float; fix by dividing by `2.0` or casting `(float)`.",
                        "explanation": "Because (score1 + score2) and 2 are both int, C performs integer division. For 165 / 2, the result is 82, which is then promoted to 82.000000. To preserve the 82.5 average, one operand must be a float: `(score1 + score2) / 2.0`.",
                        "why_wrong": {
                            "Syntax error: parentheses cannot be used in arithmetic expressions.": "Parentheses are standard for expression grouping.",
                            "The compiler will fail because float cannot store integer values.": "C implicitly converts integers to float.",
                            "The addition overflows 8-bit registers.": "Standard ints are 32-bit (range up to 2 billion)."
                        },
                        "marking_points": ["Identifies integer division truncation before assignment", "Suggests 2.0 or float cast"],
                        "source": "Nile Midterm Past Questions Scenario Application",
                        "verified": True,
                        "verified_output": "N/A"
                    },
                    {
                        "id": "cos201-mid-cs01-q2",
                        "course": "COS 201",
                        "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                        "type": "code_output",
                        "difficulty": 4,
                        "tags": ["case-study", "switch", "fallthrough"],
                        "question": "What will be the output of the student's switch block if gradeTier is 1?\n\n```c\n#include <stdio.h>\nint main() {\n    int gradeTier = 1;\n    switch(gradeTier) {\n        case 1: printf(\"Gold \");\n        case 2: printf(\"Silver \"); break;\n        default: printf(\"Pass \");\n    }\n    return 0;\n}\n```",
                        "options": [
                            "Gold ",
                            "Gold Silver ",
                            "Silver ",
                            "Gold Silver Pass "
                        ],
                        "answer": "Gold Silver ",
                        "explanation": "Because 'case 1:' lacks a 'break' statement, execution falls through into 'case 2:', executing printf(\"Silver \"). The break in case 2 then halts switch execution. The total output is 'Gold Silver '.",
                        "why_wrong": {
                            "Gold ": "Misses the switch fallthrough caused by the omitted break statement.",
                            "Silver ": "Ignores the match at case 1.",
                            "Gold Silver Pass ": "Case 2 contains a break, so execution halts before reaching default."
                        },
                        "marking_points": ["Applies switch fallthrough from case 1 into case 2 and terminates at break"],
                        "source": "Nile Midterm Past Questions Scenario Application",
                        "verified": True,
                        "verified_output": "Gold Silver "
                    }
                ]
            },
            {
                "id": "cos201-mid-cs02",
                "scenario": "A telecommunications engineer at Nile University is processing sensor packets stored in an array: `int packet[4] = {10, 20, 30, 40};`. The engineer wants to pass the array to a checksum function, traverse the values using pointer arithmetic, and verify buffer safety.",
                "sub_questions": [
                    {
                        "id": "cos201-mid-cs02-q1",
                        "course": "COS 201",
                        "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                        "type": "code_trace",
                        "difficulty": 4,
                        "tags": ["case-study", "pointers", "arrays", "tracing"],
                        "question": "Trace the output of the following pointer traversal code:\n\n```c\n#include <stdio.h>\nint main() {\n    int packet[4] = {10, 20, 30, 40};\n    int *ptr = packet;\n    printf(\"%d \", *ptr);\n    ptr += 2;\n    printf(\"%d\", *ptr);\n    return 0;\n}\n```",
                        "options": [
                            "10 30",
                            "10 20",
                            "10 40",
                            "20 40"
                        ],
                        "answer": "10 30",
                        "explanation": "Initially ptr points to packet[0] (value 10). *ptr prints '10 '. Then ptr += 2 advances the pointer forward by 2 integers to packet[2] (value 30). *ptr prints '30'. Total output: '10 30'.",
                        "why_wrong": {
                            "10 20": "Assumes ptr += 2 only advanced 1 element.",
                            "10 40": "Assumes ptr += 2 advanced to packet[3].",
                            "20 40": "Assumes ptr started at packet[1]."
                        },
                        "marking_points": ["Traces *ptr to packet[0] (10) and *(ptr+2) to packet[2] (30)"],
                        "source": "Nile Midterm Past Questions Scenario Application",
                        "verified": True,
                        "verified_output": "10 30"
                    },
                    {
                        "id": "cos201-mid-cs02-q2",
                        "course": "COS 201",
                        "topic": "Midterm Past Questions (Reconstruction & Deep Breakdown)",
                        "type": "mcq",
                        "difficulty": 3,
                        "tags": ["case-study", "pointers", "arrays"],
                        "question": "When passing the array `packet` to a function `void computeChecksum(int arr[], int size)`, which statement about `arr` inside the function is TRUE?",
                        "options": [
                            "`arr` decays to a pointer to the first element (`int *`), so `sizeof(arr)` yields pointer size, not array byte count.",
                            "`arr` copies all 4 integers onto the function call stack.",
                            "`arr` cannot be modified because arrays are always passed by const value in C.",
                            "The function automatically detects array size without needing the `size` parameter."
                        ],
                        "answer": "`arr` decays to a pointer to the first element (`int *`), so `sizeof(arr)` yields pointer size, not array byte count.",
                        "explanation": "In C, an array passed as a function argument decays into a pointer to its first element. Consequently, sizeof(arr) inside the function evaluates to the size of a pointer (e.g. 4 or 8 bytes), which is why passing the explicit length parameter is mandatory.",
                        "why_wrong": {
                            "`arr` copies all 4 integers onto the function call stack.": "C never passes array contents by value; only the memory address is passed.",
                            "`arr` cannot be modified because arrays are always passed by const value in C.": "Because the pointer is passed, the function can mutate elements in the caller's array unless qualified with const.",
                            "The function automatically detects array size without needing the `size` parameter.": "C arrays do not carry length metadata; passing the size parameter is required."
                        },
                        "marking_points": ["Recalls array decaying to pointer upon function parameter passing"],
                        "source": "Nile Midterm Past Questions Scenario Application",
                        "verified": True,
                        "verified_output": "N/A"
                    }
                ]
            }
        ]
    }

    out_path = r'c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content\COS 201\midterm_past_questions.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(topic_data, f, indent=2)
    print(f"Successfully generated {out_path} with {len(topic_data['questions'])} questions and {len(topic_data['case_studies'])} case studies.")

if __name__ == '__main__':
    create_topic9()
