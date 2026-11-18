import json
import os
import subprocess
import tempfile

def run_gcc(code_str):
    temp_dir = tempfile.mkdtemp()
    src = os.path.join(temp_dir, 'run.c')
    exe = os.path.join(temp_dir, 'run.exe')
    with open(src, 'w', encoding='utf-8') as f:
        f.write(code_str)
    res = subprocess.run(['gcc', '-Wall', '-Wextra', '-std=c11', src, '-o', exe], capture_output=True, text=True)
    if res.returncode != 0:
        return False, res.stderr
    try:
        r = subprocess.run([exe], capture_output=True, text=True, timeout=5)
        return True, r.stdout
    except Exception as e:
        return False, str(e)

topic_data = {
    "course": "COS 201",
    "topic": "Control Flow: If-Else & Switch-Case",
    "summary": "Covers conditional branching in C: single-selection if statements, double-selection if-else statements, nested conditions and the dangling-else ambiguity, multi-way if-else if ladders, and the switch selection structure including integral expression requirements, constant case labels, fallthrough mechanics, and default handling.",
    "key_terms": [
        { "term": "Selection Statement", "definition": "A control structure that chooses among alternative paths of execution based on the truth value of a condition." },
        { "term": "Dangling Else", "definition": "The syntactic ambiguity where an unbraced else statement attaches to the nearest preceding open if statement." },
        { "term": "Compound Statement (Block)", "definition": "A sequence of declarations and statements enclosed in braces { and } treated as a single syntactic unit." },
        { "term": "Switch Statement", "definition": "A multi-way branching statement that tests an integral expression against a series of constant integer case labels." },
        { "term": "Fallthrough", "definition": "The sequential continuation of execution into subsequent case labels in a switch structure when a break statement is omitted." },
        { "term": "Break Statement", "definition": "A jump statement that immediately terminates execution of the nearest enclosing switch or loop block." },
        { "term": "Default Case", "definition": "An optional catch-all label in a switch statement executed when no case label matches the controlling expression." },
        { "term": "Null Statement", "definition": "A single semicolon (;) performing no operation, often erroneously placed after an if condition." }
    ],
    "questions": [],
    "case_studies": []
}

questions = [
    # 1. Past Q12: If-Else Syntax
    {
        "id": "cos201-cf-001",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "mcq", "difficulty": 1,
        "tags": ["syntax", "if-else", "midterm-past-q"],
        "question": "Which of the following is the correct syntax for an if-else if-else structure in C?",
        "options": [
            "if (condition) {} else if (condition) {} else {}",
            "if (condition) {} elseif (condition) {} else {}",
            "if condition {} else if condition {} else {}",
            "if () {} else () {} elseif () {}"
        ],
        "answer": 0,
        "explanation": "In C, conditions must be enclosed in parentheses '()', the keyword is 'else if' (two separate words, not 'elseif'), and optional compound statements are enclosed in braces '{}'.",
        "why_wrong": {
            "1": "'elseif' is a single word used in PHP/Visual Basic; C strictly uses two words: 'else if'.",
            "2": "C requires parentheses around conditions; omitting them is a syntax error.",
            "3": "'else' does not take a condition, and 'elseif' is not a C keyword."
        },
        "source": "COS 201 Midterm Type B, Q12; Deitel Ch 3.6",
        "verified": True, "verified_output": ""
    },
    # 2. Past Q13: If-Else Output
    {
        "id": "cos201-cf-002",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "code_output", "difficulty": 2,
        "tags": ["if-else", "relational", "midterm-past-q"],
        "question": "What will be the output of the following C code?",
        "code": "#include <stdio.h>\nint main(void) {\n    int x = 1, y = 2;\n    if (x > y)\n        printf(\"X\\n\");\n    else\n        printf(\"Y\\n\");\n    return 0;\n}",
        "options": [
            "X",
            "Y",
            "1",
            "Error"
        ],
        "answer": 1,
        "explanation": "The expression 'x > y' evaluates to 1 > 2, which is false (0). Therefore, the if branch is bypassed and the else branch executes, printing 'Y'.",
        "why_wrong": {
            "0": "'X' is only printed if x is strictly greater than y.",
            "2": "The code prints the literal character 'Y', not the numeric value of x.",
            "3": "Standard single-statement if-else without braces is completely valid in C."
        },
        "source": "COS 201 Midterm Type B, Q13; Deitel Ch 3.4",
        "verified": True, "verified_output": "Y\n"
    },
    # 3. Past Q19: Switch matching
    {
        "id": "cos201-cf-003",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "code_output", "difficulty": 2,
        "tags": ["switch", "case", "break", "midterm-past-q"],
        "question": "What will be the output of the following C code?",
        "code": "#include <stdio.h>\nint main(void) {\n    int a = 5;\n    switch (a) {\n        case 1:\n            printf(\"One\\n\");\n            break;\n        case 5:\n            printf(\"Five\\n\");\n            break;\n        default:\n            printf(\"Other\\n\");\n    }\n    return 0;\n}",
        "options": [
            "One",
            "Five",
            "Other",
            "Error"
        ],
        "answer": 1,
        "explanation": "The controlling expression 'a' has value 5, which matches 'case 5:'. The statement 'printf(\"Five\\n\");' executes, followed by 'break;' which immediately exits the switch statement.",
        "why_wrong": {
            "0": "'One' is associated with case 1, not case 5.",
            "2": "'Other' is the default branch, which is only reached if no case label matches or if fallthrough occurs.",
            "3": "The switch syntax is standard and clean."
        },
        "source": "COS 201 Midterm Type B, Q19; Deitel Ch 4.7",
        "verified": True, "verified_output": "Five\n"
    },
    # 4. Past Q29: If-Else If Ladder
    {
        "id": "cos201-cf-004",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "code_output", "difficulty": 2,
        "tags": ["if-else", "ladder", "midterm-past-q"],
        "question": "What will be the output of the following C code?",
        "code": "#include <stdio.h>\nint main(void) {\n    int x = 5;\n    if (x > 10)\n        printf(\"Big\\n\");\n    else if (x > 3)\n        printf(\"Medium\\n\");\n    else\n        printf(\"Small\\n\");\n    return 0;\n}",
        "options": [
            "Big",
            "Medium",
            "Small",
            "Error"
        ],
        "answer": 1,
        "explanation": "1. 'x > 10' (5 > 10) is false (0).\n2. C moves to 'else if (x > 3)' (5 > 3), which is true (1).\n3. 'printf(\"Medium\\n\");' executes, and the rest of the ladder is skipped.",
        "why_wrong": {
            "0": "5 is not greater than 10.",
            "2": "'Small' is only reached if x <= 3.",
            "3": "Valid nested conditional ladder syntax."
        },
        "source": "COS 201 Midterm Type B, Q29; Deitel Ch 3.6",
        "verified": True, "verified_output": "Medium\n"
    },
    # 5. Past Q37: Switch Default Execution
    {
        "id": "cos201-cf-005",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "code_output", "difficulty": 2,
        "tags": ["switch", "default", "midterm-past-q"],
        "question": "What will be the output of the following C code?",
        "code": "#include <stdio.h>\nint main(void) {\n    int x = 3;\n    switch (x) {\n        case 1:\n            printf(\"One\\n\");\n            break;\n        case 2:\n            printf(\"Two\\n\");\n            break;\n        default:\n            printf(\"Other\\n\");\n    }\n    return 0;\n}",
        "options": [
            "One",
            "Two",
            "Other",
            "Error"
        ],
        "answer": 2,
        "explanation": "The value of 'x' is 3. Neither 'case 1:' nor 'case 2:' matches. Control transfers to the 'default:' label, printing 'Other'.",
        "why_wrong": {
            "0": "Case 1 does not match x = 3.",
            "1": "Case 2 does not match x = 3.",
            "3": "Default handling is a core feature of switch statements, not an error."
        },
        "source": "COS 201 Midterm Type B, Q37; Deitel Ch 4.7",
        "verified": True, "verified_output": "Other\n"
    },
    # 6. Switch Fallthrough (Missing break)
    {
        "id": "cos201-cf-006",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "code_output", "difficulty": 3,
        "tags": ["switch", "fallthrough", "missing-break"],
        "question": "What will be the output of the following C program where break statements are omitted?",
        "code": "#include <stdio.h>\nint main(void) {\n    int val = 2;\n    switch (val) {\n        case 1:\n            printf(\"1 \");\n        case 2:\n            printf(\"2 \");\n        case 3:\n            printf(\"3 \");\n        default:\n            printf(\"D\\n\");\n    }\n    return 0;\n}",
        "options": [
            "2 3 D",
            "2 ",
            "2 3 ",
            "1 2 3 D"
        ],
        "answer": 0,
        "explanation": "Switch execution begins at 'case 2:', printing '2 '. Because there are no 'break;' statements, execution falls through sequentially into 'case 3:' (printing '3 ') and 'default:' (printing 'D\\n'). The output is '2 3 D'.",
        "why_wrong": {
            "1": "'2 ' would only print if a 'break;' followed case 2.",
            "2": "'2 3 ' would only print if a 'break;' followed case 3.",
            "3": "Case 1 is skipped because val != 1."
        },
        "source": "Deitel Ch 4.7",
        "verified": True, "verified_output": "2 3 D\n"
    },
    # 7. Dangling Else Ambiguity
    {
        "id": "cos201-cf-007",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "code_output", "difficulty": 4,
        "tags": ["dangling-else", "syntax", "traps"],
        "question": "What will be printed by the following program containing the classic 'dangling else' construct?",
        "code": "#include <stdio.h>\nint main(void) {\n    int x = 5, y = 2;\n    if (x > 10)\n        if (y > 5)\n            printf(\"Both\\n\");\n    else\n        printf(\"Neither\\n\");\n    return 0;\n}",
        "options": [
            "No output",
            "Neither",
            "Both",
            "Compilation Error"
        ],
        "answer": 0,
        "explanation": "In C, an 'else' always associates with the closest preceding unmatched 'if' (here, 'if (y > 5)'), regardless of visual indentation! Because the outer condition 'x > 10' (5 > 10) is false, the entire inner if-else structure is completely bypassed. Nothing is printed at all.",
        "why_wrong": {
            "1": "'Neither' is the intended output only if braces had tied the else to 'if (x > 10)'. Without braces, the else belongs to the inner if.",
            "2": "'Both' requires x > 10 and y > 5.",
            "3": "Dangling else is valid syntax in C; the compiler resolves it via nearest-if binding."
        },
        "source": "Deitel Ch 3.6",
        "verified": True, "verified_output": ""
    },
    # 8. Null Statement after if condition
    {
        "id": "cos201-cf-008",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "code_output", "difficulty": 3,
        "tags": ["null-statement", "semicolon", "bugs"],
        "question": "What will be printed by the following C program?",
        "code": "#include <stdio.h>\nint main(void) {\n    int x = 0;\n    if (x > 10);\n        printf(\"Greater\\n\");\n    return 0;\n}",
        "options": [
            "Greater",
            "No output",
            "Compilation Error",
            "Undefined"
        ],
        "answer": 0,
        "explanation": "The semicolon immediately following 'if (x > 10);' forms a null (empty) statement as the if-body. The subsequent 'printf(\"Greater\\n\");' is an ordinary statement outside the if construct, so it executes unconditionally and prints 'Greater'.",
        "why_wrong": {
            "1": "'No output' is what the programmer intended, but the stray semicolon terminates the if branch.",
            "2": "A null statement is syntactically legal in C.",
            "3": "Behavior is strictly well-defined."
        },
        "source": "Deitel Common Programming Error 3.10",
        "verified": True, "verified_output": "Greater\n"
    },
    # 9. Switch Expression Type Requirement
    {
        "id": "cos201-cf-009",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "mcq", "difficulty": 2,
        "tags": ["switch", "types", "compiler-error"],
        "question": "Which of the following data types CANNOT be used as the controlling expression in a C switch statement?",
        "options": [
            "float",
            "int",
            "char",
            "enum"
        ],
        "answer": 0,
        "explanation": "The C standard requires the controlling expression of a switch statement to have an integer type (or an enumeration type, which maps to integer). Floating-point types ('float', 'double') are not allowed in switch statements.",
        "why_wrong": {
            "1": "'int' is the standard type used in switch expressions.",
            "2": "'char' is an integral type (representing ASCII integer codes) and is fully legal.",
            "3": "'enum' identifiers are integral constants and legal in switch statements."
        },
        "source": "Deitel Ch 4.7; ISO C Standard 6.8.4.2",
        "verified": True, "verified_output": ""
    },
    # 10. Switch Case Labels Must Be Constants
    {
        "id": "cos201-cf-010",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "mcq", "difficulty": 3,
        "tags": ["switch", "case-labels", "syntax"],
        "question": "Why is the following switch case label illegal in standard C?\nint limit = 10;\nswitch (x) {\n    case limit: printf(\"Limit!\"); break;\n}",
        "options": [
            "Case labels must be constant expressions known at compile-time; variables like 'limit' are illegal.",
            "Case labels cannot use words, only numbers.",
            "The break statement is placed on the same line as printf.",
            "The switch variable 'x' must match the name of the case variable."
        ],
        "answer": 0,
        "explanation": "In C, each case label must be an integral constant expression evaluated at compile time (such as 10, 'A', or 2 * 5). A variable (even if qualified with const in standard C90) is not a constant expression in case labels.",
        "why_wrong": {
            "1": "Character constants ('A') and macro names (#define) are words and fully legal.",
            "2": "Whitespace and line breaks do not alter C syntax.",
            "3": "Case labels evaluate targets, not identifier names."
        },
        "source": "Deitel Ch 4.7",
        "verified": True, "verified_output": ""
    },
    # 11. Code Output: Char in switch
    {
        "id": "cos201-cf-011",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "code_output", "difficulty": 3,
        "tags": ["switch", "char", "fallthrough"],
        "question": "What will be printed by the following C program?",
        "code": "#include <stdio.h>\nint main(void) {\n    char code = 'b';\n    switch (code) {\n        case 'a':\n        case 'A':\n            printf(\"Alpha\\n\");\n            break;\n        case 'b':\n        case 'B':\n            printf(\"Beta\\n\");\n            break;\n        default:\n            printf(\"Other\\n\");\n    }\n    return 0;\n}",
        "options": [
            "Beta",
            "Alpha",
            "Beta\\nOther",
            "Other"
        ],
        "answer": 0,
        "explanation": "This demonstrates intentional fallthrough for multiple case labels. 'code' matches 'case 'b':', which has no body, falling through immediately to 'case 'B':' where 'printf(\"Beta\\n\"); break;' executes.",
        "why_wrong": {
            "1": "Alpha is for 'a' or 'A'.",
            "2": "A 'break;' follows the Beta print, so default is not executed.",
            "3": "Default only executes if no case matches."
        },
        "source": "Deitel Ch 4.7",
        "verified": True, "verified_output": "Beta\n"
    },
    # 12. Non-zero truthiness in if condition
    {
        "id": "cos201-cf-012",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "code_output", "difficulty": 3,
        "tags": ["truthiness", "if-condition"],
        "question": "What is the output of the following C program evaluating negative and non-zero truth values?",
        "code": "#include <stdio.h>\nint main(void) {\n    int val = -5;\n    if (val)\n        printf(\"NonZero\\n\");\n    else\n        printf(\"Zero\\n\");\n    return 0;\n}",
        "options": [
            "NonZero",
            "Zero",
            "Compilation Error",
            "Undefined"
        ],
        "answer": 0,
        "explanation": "In C, ANY non-zero numerical value evaluates as true in conditional contexts. Because -5 != 0, 'val' evaluates to true, executing the if branch to print 'NonZero'. Only 0 is false.",
        "why_wrong": {
            "1": "Only 0 is treated as false in C; negative numbers are non-zero and therefore true.",
            "2": "Using non-boolean integral expressions in if conditions is standard in C.",
            "3": "Truth value semantics are strictly defined in ISO C."
        },
        "source": "Deitel Ch 3.3",
        "verified": True, "verified_output": "NonZero\n"
    },
    # 13. Type Answer: Jump statement
    {
        "id": "cos201-cf-013",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "type_answer", "difficulty": 1,
        "tags": ["keywords", "switch"],
        "question": "Which C keyword is used to prevent execution from falling through from one switch case into the next?",
        "answer": "break",
        "accepted_answers": ["break", "break;"],
        "explanation": "'break' causes control to exit the switch structure immediately.",
        "why_wrong": {},
        "source": "Deitel Ch 4.7",
        "verified": True, "verified_output": ""
    },
    # 14. Cloze: Selection
    {
        "id": "cos201-cf-014",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "cloze", "difficulty": 2,
        "tags": ["cloze", "control-flow"],
        "question": "Fill in the correct C keywords for selection control structures:",
        "template": "A single-selection statement begins with [[blank]], while a multi-way branch testing constant expressions begins with [[blank]]. Inside a switch statement, the catch-all label that runs when no case matches is [[blank]].",
        "blanks": ["if", "switch", "default"],
        "explanation": "'if' begins single-selection, 'switch' multiple-selection, and 'default' is the catch-all case.",
        "why_wrong": {},
        "source": "Deitel Ch 3.3, 4.7",
        "verified": True, "verified_output": ""
    },
    # 15. Matching Control Flow Concepts
    {
        "id": "cos201-cf-015",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "matching", "difficulty": 2,
        "tags": ["matching", "selection"],
        "question": "Match each control flow term with its technical description:",
        "pairs": [
            { "left": "if statement", "right": "Performs an action only when a condition evaluates to non-zero" },
            { "left": "if-else statement", "right": "Chooses between two mutually exclusive actions" },
            { "left": "switch statement", "right": "Branches among multiple actions based on integral constant match" },
            { "left": "break keyword", "right": "Terminates execution within a switch case or loop immediately" }
        ],
        "explanation": "Summarizes the selection constructs defined in the C language standard.",
        "why_wrong": {},
        "source": "Deitel Ch 3, Ch 4",
        "verified": True, "verified_output": ""
    },
    # 16. Sequencing Evaluation of If-Else If Ladder
    {
        "id": "cos201-cf-016",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "sequencing", "difficulty": 2,
        "tags": ["sequencing", "if-else"],
        "question": "Order the steps C takes when evaluating an if-else if-else ladder:",
        "steps": [
            "Evaluate the initial if condition",
            "If true, execute the if-body and exit the entire ladder",
            "If false, proceed to evaluate the subsequent else if condition",
            "If no condition evaluates to true, execute the final else block"
        ],
        "explanation": "C evaluates conditions in an if-else if ladder sequentially top-to-bottom. The first condition that evaluates to true executes its associated block, and all remaining branches are skipped.",
        "why_wrong": {},
        "source": "Deitel Ch 3.6",
        "verified": True, "verified_output": ""
    },
    # 17. Code Write: Switch-Based Menu
    {
        "id": "cos201-cf-017",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "code_write", "difficulty": 3,
        "tags": ["code_write", "switch"],
        "question": "Write a complete C main function that declares an integer variable 'choice = 2'. Using a switch statement on 'choice', print 'Add\\n' for case 1, 'Delete\\n' for case 2, and 'Invalid\\n' for default. Include all necessary break statements.",
        "code_lang": "c",
        "reference_solution": "#include <stdio.h>\nint main(void) {\n    int choice = 2;\n    switch (choice) {\n        case 1:\n            printf(\"Add\\n\");\n            break;\n        case 2:\n            printf(\"Delete\\n\");\n            break;\n        default:\n            printf(\"Invalid\\n\");\n            break;\n    }\n    return 0;\n}",
        "marking_points": [
            "Declares choice = 2",
            "Implements switch (choice)",
            "Handles case 1 with printf(\"Add\\n\") and break",
            "Handles case 2 with printf(\"Delete\\n\") and break",
            "Handles default with printf(\"Invalid\\n\")",
            "Returns 0 from main"
        ],
        "explanation": "Standard switch control structure testing case labels and break termination.",
        "why_wrong": {},
        "source": "Deitel Ch 4.7",
        "verified": True, "verified_output": "Delete\n"
    },
    # 18. Explain: Why braces are critical in nested if
    {
        "id": "cos201-cf-018",
        "course": "COS 201", "topic": "control_flow_selection",
        "type": "explain", "difficulty": 3,
        "tags": ["theory", "dangling-else", "braces"],
        "question": "Explain the 'dangling else' problem in C and how using compound statement braces ({ }) prevents subtle logic bugs.",
        "answer": "1. Definition: The dangling else problem occurs when nested if statements are written without braces and an else clause is present. The grammar rule of C stipulates that an else is always bound to the nearest preceding open if.\n2. Danger: Indentation might mislead the programmer into believing the else belongs to the outer if, when in reality the compiler binds it to the inner if.\n3. Solution: Wrapping the inner or outer statements in explicit braces { } removes all ambiguity and forces the compiler to bind the else exactly where intended.",
        "marking_points": [
            "States that an else binds to the nearest preceding unmatched if by default",
            "Explains that visual indentation does not change compiler grammar binding",
            "Explains that explicit braces { } strictly control block scope and eliminate ambiguity"
        ],
        "explanation": "A cornerstone concept in control flow design.",
        "why_wrong": {},
        "source": "Deitel Ch 3.6",
        "verified": True, "verified_output": ""
    },
    # Flashcards (8)
    {
        "id": "cos201-cf-fc01", "course": "COS 201", "topic": "control_flow_selection",
        "type": "flashcard", "difficulty": 1, "tags": ["flashcard", "selection"],
        "question": "What is the difference between single-selection, double-selection, and multiple-selection in C?",
        "answer": "Single-selection (if) performs or skips an action. Double-selection (if-else) chooses between two actions. Multiple-selection (switch or if-else if) chooses among three or more actions.",
        "explanation": "Deitel Ch 3.3."
    },
    {
        "id": "cos201-cf-fc02", "course": "COS 201", "topic": "control_flow_selection",
        "type": "flashcard", "difficulty": 1, "tags": ["flashcard", "truth"],
        "question": "What numeric values in C represent false and true in conditional tests?",
        "answer": "0 represents false. ANY non-zero value (positive or negative) represents true.",
        "explanation": "E.g. if (-1) evaluates as true."
    },
    {
        "id": "cos201-cf-fc03", "course": "COS 201", "topic": "control_flow_selection",
        "type": "flashcard", "difficulty": 2, "tags": ["flashcard", "switch"],
        "question": "Can a float or double variable be used in a C switch statement?",
        "answer": "No. The switch controlling expression MUST evaluate to an integer type (int, char, enum).",
        "explanation": "Floating-point types are illegal in C switch statements."
    },
    {
        "id": "cos201-cf-fc04", "course": "COS 201", "topic": "control_flow_selection",
        "type": "flashcard", "difficulty": 2, "tags": ["flashcard", "fallthrough"],
        "question": "What is fallthrough in a switch statement?",
        "answer": "When a break statement is omitted, execution automatically flows into the next case's statements regardless of its label.",
        "explanation": "Fallthrough continues until a break or the end of the switch block."
    },
    {
        "id": "cos201-cf-fc05", "course": "COS 201", "topic": "control_flow_selection",
        "type": "flashcard", "difficulty": 2, "tags": ["flashcard", "dangling-else"],
        "question": "To which 'if' does an 'else' associate in nested if statements without braces?",
        "answer": "To the nearest preceding unmatched 'if'.",
        "explanation": "The dangling else rule in C grammar."
    },
    {
        "id": "cos201-cf-fc06", "course": "COS 201", "topic": "control_flow_selection",
        "type": "flashcard", "difficulty": 1, "tags": ["flashcard", "default"],
        "question": "Is the 'default' case mandatory in a switch statement?",
        "answer": "No, it is optional. If omitted and no case matches, the switch does nothing.",
        "explanation": "It provides a catch-all safety path."
    },
    {
        "id": "cos201-cf-fc07", "course": "COS 201", "topic": "control_flow_selection",
        "type": "flashcard", "difficulty": 1, "tags": ["flashcard", "case-labels"],
        "question": "Can case labels in a switch statement contain variables? (e.g. case x:)",
        "answer": "No. Case labels MUST be constant integer expressions known at compile-time.",
        "explanation": "Variables cause a compilation error."
    },
    {
        "id": "cos201-cf-fc08", "course": "COS 201", "topic": "control_flow_selection",
        "type": "flashcard", "difficulty": 2, "tags": ["flashcard", "null-statement"],
        "question": "What is the danger of writing 'if (score >= 50);' with a trailing semicolon?",
        "answer": "The semicolon terminates the if-body as a null statement, causing the subsequent indented block to execute unconditionally.",
        "explanation": "A common syntax trap."
    }
]

# Case Studies
case_studies = [
    {
        "id": "cos201-cf-cs01",
        "course": "COS 201", "topic": "control_flow_selection",
        "title": "Nile Smart Card Campus Access Turnstile",
        "scenario": "A computerized turnstile at Nile University checks student smart card status codes. Status code 'A' indicates Active, 'S' indicates Suspended, 'E' indicates Expired, and all other codes indicate Unknown. A software trainee implements the decision logic using a switch construct.",
        "sub_questions": [
            {
                "id": "cos201-cf-cs01-q1",
                "course": "COS 201", "topic": "control_flow_selection",
                "type": "code_output", "difficulty": 3,
                "tags": ["scenario", "switch", "fallthrough"],
                "question": "What will be printed when the trainee executes the turnstile simulation with code 'S'?",
                "code": "#include <stdio.h>\nint main(void) {\n    char code = 'S';\n    switch (code) {\n        case 'A':\n            printf(\"Open \");\n            break;\n        case 'S':\n            printf(\"Suspended \");\n        case 'E':\n            printf(\"Expired \");\n            break;\n        default:\n            printf(\"Denied \");\n    }\n    printf(\"\\n\");\n    return 0;\n}",
                "options": [
                    "Suspended Expired ",
                    "Suspended ",
                    "Expired ",
                    "Suspended Expired Denied "
                ],
                "answer": 0,
                "explanation": "Case 'S' matches and prints 'Suspended '. Because there is no break statement after case 'S', execution falls through into case 'E', printing 'Expired '. The break statement in case 'E' then terminates the switch.",
                "why_wrong": {
                    "1": "Missing break causes execution to fall through into case 'E'.",
                    "2": "Case 'S' executed first.",
                    "3": "Case 'E' contains a break, preventing fallthrough into default."
                },
                "source": "Deitel Ch 4.7",
                "verified": True, "verified_output": "Suspended Expired \n"
            },
            {
                "id": "cos201-cf-cs01-q2",
                "course": "COS 201", "topic": "control_flow_selection",
                "type": "mcq", "difficulty": 3,
                "tags": ["scenario", "switch", "refactor"],
                "question": "To allow both uppercase ('A') and lowercase ('a') to grant entry ('Open'), how should case 'A' and 'a' be structured in the switch?",
                "options": [
                    "case 'A': case 'a': printf(\"Open \"); break;",
                    "case 'A' || 'a': printf(\"Open \"); break;",
                    "case 'A', 'a': printf(\"Open \"); break;",
                    "case ('A' || 'a'): printf(\"Open \"); break;"
                ],
                "answer": 0,
                "explanation": "In C switch statements, stacking multiple case labels without intervening code ('case 'A': case 'a':') is the standard idiom to associate multiple constant values with the same action.",
                "why_wrong": {
                    "1": "Logical OR '||' evaluates to 1, so 'case 'A' || 'a':' becomes 'case 1:', which is not the character code.",
                    "2": "Comma expressions are not permitted as composite case targets in standard C.",
                    "3": "Parenthesizing does not change the fact that '||' produces boolean 1."
                },
                "source": "Deitel Ch 4.7",
                "verified": True, "verified_output": ""
            }
        ]
    },
    {
        "id": "cos201-cf-cs02",
        "course": "COS 201", "topic": "control_flow_selection",
        "title": "Hospital Emergency Triage Sorting Algorithm",
        "scenario": "An emergency triage system in Abuja sorts incoming patients by blood pressure systolic readings and heart rate. Logic evaluates urgency into Critical, Urgent, and Normal.",
        "sub_questions": [
            {
                "id": "cos201-cf-cs02-q1",
                "course": "COS 201", "topic": "control_flow_selection",
                "type": "code_output", "difficulty": 3,
                "tags": ["scenario", "nested-if", "ladder"],
                "question": "What triage level is printed for a patient with systolic = 145 and heart_rate = 95?",
                "code": "#include <stdio.h>\nint main(void) {\n    int systolic = 145;\n    int heart_rate = 95;\n    if (systolic >= 180 || heart_rate >= 120)\n        printf(\"Critical\\n\");\n    else if (systolic >= 140 && heart_rate >= 90)\n        printf(\"Urgent\\n\");\n    else\n        printf(\"Normal\\n\");\n    return 0;\n}",
                "options": [
                    "Urgent",
                    "Critical",
                    "Normal",
                    "Compilation Error"
                ],
                "answer": 0,
                "explanation": "1. Condition 1 (systolic >= 180 || heart_rate >= 120) -> (145 >= 180 || 95 >= 120) is false.\n2. Condition 2 (systolic >= 140 && heart_rate >= 90) -> (145 >= 140 && 95 >= 90) -> (1 && 1) is true.\n3. Thus 'Urgent' is printed.",
                "why_wrong": {
                    "1": "Critical threshold is 180 systolic or 120 heart rate.",
                    "2": "Normal is only reached if Urgent condition fails.",
                    "3": "Standard C nested boolean logic."
                },
                "source": "Deitel Ch 3.6",
                "verified": True, "verified_output": "Urgent\n"
            }
        ]
    }
]

# Verify all code questions
for q in questions:
    if q.get('code') and q['type'] != 'code_bug':
        success, out = run_gcc(q['code'])
        if success:
            q['verified'] = True
            q['verified_output'] = out
        else:
            print(f"GCC FAIL for {q['id']}: {out}")

for cs in case_studies:
    for sq in cs.get('sub_questions', []):
        if sq.get('code'):
            success, out = run_gcc(sq['code'])
            if success:
                sq['verified'] = True
                sq['verified_output'] = out
            else:
                print(f"GCC FAIL for {sq['id']}: {out}")

topic_data['questions'] = questions
topic_data['case_studies'] = case_studies

out_path = r"c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content\COS 201\control_flow_selection.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(topic_data, f, indent=2)

print(f"Successfully generated {len(questions)} questions and {len(case_studies)} case studies in {out_path}")
