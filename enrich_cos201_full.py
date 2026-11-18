import json
import os

EXAMINER_ENRICHMENTS = {
    # Control Flow
    "cos201-cf-013": "The 'break' keyword forces an immediate exit from the switch statement body, transferring execution control to the first statement following the enclosing switch block. Without 'break', execution falls through sequentially to subsequent cases.",
    "cos201-cf-fc01": "In C, 'if' is a single-selection statement (executing an action if condition is true), 'if-else' is a double-selection statement (choosing between two paths), and 'switch' is a multi-selection statement (selecting from multiple actions based on an integral value). (Deitel & Deitel, Ch 3.3).",
    "cos201-cf-fc02": "In C, any non-zero numeric value (positive or negative, e.g. -1, 42, 0.5) evaluates as logical TRUE, while strictly zero (0, 0.0, '\\0', NULL) evaluates as FALSE. (Deitel, Ch 3.4).",
    "cos201-cf-fc03": "The switch expression and all case labels MUST evaluate to integer types (int, char, enum, short, long). Floating-point types (float, double) and string literals are strictly illegal in C switch statements and cause compile-time syntax errors. (Deitel, Ch 4.7).",
    "cos201-cf-fc05": "The classic dangling-else ambiguity is resolved in C by binding an 'else' to the closest preceding unmatched 'if' within the same block, irrespective of source indentation. Always use curly braces to make nesting unambiguous. (Deitel, Ch 3.6).",
    "cos201-cf-fc06": "The 'default' case in a switch provides a deterministic fallback catch-all path when none of the explicit case constants match the tested expression. It is defensive programming to always include a default case. (Deitel, Ch 4.7).",
    "cos201-cf-fc07": "Case labels in C switch statements must be compile-time constant integer expressions (e.g., 'case 5:' or 'case 'A':'). Using variable identifiers or non-constant expressions causes a compilation error: 'case label does not reduce to an integer constant'. (Deitel, Ch 4.7).",
    "cos201-cf-fc08": "Placing a semicolon directly after the header of an if, while, or for statement (e.g. 'if (x > 0);') forms a null statement. The controlled body becomes empty, and the subsequent indented block executes unconditionally regardless of the test condition. (Deitel, Ch 3.5).",

    # Data Types & Variables
    "cos201-dt-fc03": "C identifiers must begin with an alphabetic letter (a-z, A-Z) or an underscore (_), followed by letters, digits (0-9), or underscores. An identifier cannot begin with a digit (e.g. '1count' is illegal; '_count1' is valid) and cannot be a C reserved keyword. (Deitel, Ch 2.4).",
    "cos201-dt-fc04": "The '#define' preprocessor directive performs literal text substitution before compilation begins; it does not take a semicolon at the end of the line (e.g. '#define PI 3.14159'). The 'const' qualifier creates a typed, read-only memory variable evaluated by the C compiler. (Deitel, Ch 6.4).",
    "cos201-dt-fc05": "In standard C (IEEE 754), 'float' is single-precision (typically 32 bits, ~7 decimal digits of precision), whereas 'double' is double-precision (typically 64 bits, ~15-17 decimal digits of precision with a much wider exponent range). (Deitel, Ch 3.9).",
    "cos201-dt-fc07": "The 'unsigned' type specifier instructs the compiler to treat the most significant bit as a magnitude bit rather than a two's-complement sign bit. This doubles the maximum positive range of the integer while preventing negative values (e.g., 0 to 65,535 for 16-bit unsigned vs -32,768 to +32,767 for signed). (Deitel, Ch 5.12).",

    # Functions
    "cos201-fn-fc01": "A function prototype declares the function's return type, name, and parameter types before its definition or call. It enables the compiler to enforce strict type checking on arguments and return values, preventing runtime stack corruption. (Deitel, Ch 5.3).",
    "cos201-fn-fc02": "By default, C passes all primitive arguments by value: a copy of each argument is pushed onto the call stack. Changes made to parameters inside the called function do not affect the original variables in the caller. To modify caller data, pass pointers (simulated call-by-reference). (Deitel, Ch 5.5).",
    "cos201-fn-fc03": "A local variable declared with the 'static' storage-class specifier is allocated in static data memory rather than on the call stack. It retains its value across multiple function calls throughout program lifetime, but its scope remains strictly private to the enclosing function. (Deitel, Ch 5.11).",
    "cos201-fn-fc04": "Every recursive function must have at least one base case that terminates recursion without making further recursive calls. Omitting the base case or failing to converge towards it leads to infinite recursion and eventual stack overflow (segmentation fault). (Deitel, Ch 5.14).",
    "cos201-fn-fc05": "A function with a 'void' return type does not return a value. It may terminate naturally at its closing brace, or exit early using a bare 'return;' statement without an expression. (Deitel, Ch 5.4).",
    "cos201-fn-fc06": "When an array name is passed as an argument to a function in C, it automatically decays to a pointer to its first element (type int[] decays to int*). Consequently, array arguments are passed by reference and function modifications affect caller memory. (Deitel, Ch 6.5).",
    "cos201-fn-fc07": "Returning 0 from 'main()' signals successful program completion to the host operating system. Returning a non-zero integer (such as EXIT_FAILURE or 1) indicates an error or abnormal termination condition. (Deitel, Ch 2.3).",
    "cos201-fn-fc08": "Stack overflow occurs when call stack memory is exhausted, commonly caused by runaway infinite recursion or allocating excessively large local arrays on the stack. The OS terminates the process with a segmentation fault. (Deitel, Ch 5.14).",

    # Loops
    "cos201-lp-fc01": "The 'while' loop is a pre-test (entry-controlled) loop: its continuation condition is evaluated BEFORE the loop body executes. If the condition is false initially, the body executes zero times. (Deitel, Ch 4.3).",
    "cos201-lp-fc02": "The 'do-while' loop is a post-test (exit-controlled) loop: its condition is evaluated AFTER the loop body executes. Therefore, the body is guaranteed to execute at least once regardless of whether the condition is true or false. (Deitel, Ch 4.6).",
    "cos201-lp-fc03": "The 'break' statement terminates loop execution immediately and jumps to the statement following the loop. The 'continue' statement skips the remaining statements in the current iteration and jumps directly to the next iteration's increment or condition test. (Deitel, Ch 4.8).",
    "cos201-lp-fc05": "A sentinel value (also called a dummy or flag value) is a distinct data value used to indicate the end of input data. It must be carefully chosen so that it cannot be confused with any legitimate input data value (e.g. -1 for positive test scores). (Deitel, Ch 3.8).",
    "cos201-lp-fc06": "The construct 'for(;;)' or 'while(1)' creates an intentional infinite loop. The loop relies on an internal selection statement containing a 'break' or 'return' to terminate when an exit condition is reached. (Deitel, Ch 4.4).",
    "cos201-lp-fc07": "An off-by-one error (OBOE) is a common boundary logic bug where a loop iterates one time too many or one time too few (e.g., using '<=' instead of '<' on a 0-indexed array of length N, which reads beyond the array bounds). (Deitel, Ch 4.5).",
    "cos201-lp-fc08": "In C, a 'do-while' loop must terminate with a closing semicolon after the condition: 'do { ... } while (condition);'. Omitting this semicolon results in a compilation syntax error. (Deitel, Ch 4.6).",

    # Midterm & Past Questions
    "cos201-mid-fc06": "In pointer declarations such as 'int *ptr;', the asterisk (*) denotes that the variable is an indirection pointer that holds the memory address of an integer. In expressions, '*ptr' dereferences the pointer to access or modify the value at that address. (Deitel, Ch 7.3).",

    # Operators & Expressions
    "cos201-op-fc01": "The modulus operator (%) yields the remainder of integer division (e.g., 17 % 5 = 2). It cannot be applied to floating-point types (float or double) in C; using it with floats causes a compile-time error. (Deitel, Ch 2.6).",
    "cos201-op-fc02": "Pre-increment (++x) increments the operand x by 1 first and evaluates to the new value. Post-increment (x++) evaluates to the current value of x first in the enclosing expression, and then increments x by 1. (Deitel, Ch 3.12).",
    "cos201-op-fc04": "The ternary conditional operator (? :) takes three operands: 'condition ? expr1 : expr2'. It evaluates expr1 if condition is true (non-zero), or expr2 if condition is false (zero). It is the only ternary operator in C. (Deitel, Ch 3.6).",
    "cos201-op-fc05": "In C, '=' is the assignment operator (stores a value), whereas '==' is the relational equality operator (tests for equality). Confusing 'if (x = 5)' for 'if (x == 5)' assigns 5 to x and evaluates to 5 (true), a classic logical bug. (Deitel, Ch 3.13).",
    "cos201-op-fc06": "In C operator precedence, arithmetic operators (*, /, %, +, -) have higher precedence than relational operators (<, <=, >, >=), which have higher precedence than equality operators (==, !=), which precede logical operators (&&, ||). Parentheses override default precedence. (Deitel, Ch 4.11).",
    "cos201-op-fc07": "Most operators in C (arithmetic, relational, logical) evaluate Left-to-Right. However, assignment operators (=, +=, etc.), the ternary conditional operator (? :), and unary operators (!, ++, --, sizeof, &, *) are right-associative (evaluate Right-to-Left). (Deitel, Ch 4.11).",
    "cos201-op-fc08": "Compound assignment operators (+=, -=, *=, /=, %=) combine an arithmetic operation with assignment. The expression 'x += y + 1' is strictly equivalent to 'x = x + (y + 1)', where the entire right-hand side is evaluated first. (Deitel, Ch 3.11).",

    # Strings
    "cos201-str-fc03": "The 'strlen()' function counts and returns the number of characters in a string up to, but NOT including, the terminating null character ('\\0'). In contrast, 'sizeof(str)' on an array yields the total allocated byte size including '\\0'. (Deitel, Ch 8.3)."
}

EXACT_WHY_WRONG_FIXES = {
    "cos201-dt-010": {
        "1": "A char is defined by ISO C to be exactly 1 byte (sizeof(char) == 1 by definition). It is never 2 bytes.",
        "2": "4 bytes is typical for an int or float on modern 32/64-bit systems, not char.",
        "3": "While int and pointer sizes are architecture-dependent, sizeof(char) is strictly guaranteed by ISO C to be 1 on all architectures."
    },
    "cos201-lp-004": {
        "1": "Only adds the final iteration value i=2 without accumulating previous iterations (0+1).",
        "2": "6 would be the result if i <= 3 was used (0 + 1 + 2 + 3 = 6).",
        "3": "x is updated in iterations 1 and 2, so it does not remain 0."
    },
    "cos201-mid-003": {
        "0": "2 would be the result if post-increment (x++) was used instead of pre-increment (++x).",
        "2": "Pre-increment adds 1 to x (2+1=3), it does not subtract.",
        "3": "Pre-increment within a printf call is standard, valid C syntax."
    },
    "cos201-mid-007": {
        "1": "2.5 is the mathematical result, but integer division in C truncates the fractional part, yielding 2.",
        "2": "C integer division truncates towards zero; it does not round up to 3.",
        "3": "Dividing two integers using '/' is completely valid standard C syntax."
    },
    "cos201-mid-011": {
        "0": "arr[0] is 1; in C, array indexing is 0-based.",
        "1": "arr[1] is 2, not arr[2].",
        "3": "arr[2] is completely within the bounds of a 3-element array (valid indices are 0, 1, and 2)."
    },
    "cos201-mid-017": {
        "0": "x accumulates i across iterations: x = 0 + 0 + 1 + 2 = 3. 2 stops the summation early.",
        "2": "Only accounts for the first non-zero iteration (i=1), omitting i=2.",
        "3": "Assumes the loop body was not executed or x remained unmutated."
    },
    "cos201-mid-023": {
        "1": "The logical OR (||) expression (0 || 1) evaluates to 1 (true), so the if-branch executes.",
        "2": "The code prints the string literal 'True', not numeric 0.",
        "3": "The code prints the string literal 'True', not numeric 1."
    },
    "cos201-mid-025": {
        "0": "2 is the value of x; this would only be evaluated if (x > y) were true (2 > 3 is false).",
        "2": "The ternary operator returns the evaluated expression (y = 3), not the boolean condition result.",
        "3": "Using a ternary expression inside a printf call is standard, valid C syntax."
    },
    "cos201-mid-033": {
        "0": "The logical AND (&&) expression (1 && 0) evaluates to 0 (false), so the else-branch executes.",
        "2": "The code prints the string literal 'No', not numeric 1.",
        "3": "The code prints the string literal 'No', not numeric 0."
    },
    "cos201-mid-039": {
        "0": "1 is the value of x; this would only be returned if the condition (x < y) were false.",
        "2": "The ternary operator returns the chosen operand (y = 2), not boolean 0.",
        "3": "The ternary conditional expression inside printf is valid standard C syntax."
    },
    "cos201-op-001": {
        "0": "2 is returned by post-increment (x++), but pre-increment (++x) increments before yielding the value.",
        "2": "Pre-increment adds 1 to x, it does not decrement.",
        "3": "Pre-increment inside printf is completely valid C syntax."
    },
    "cos201-op-003": {
        "1": "2.5 is the mathematical result, but integer division in C truncates all decimals.",
        "2": "C integer division truncates towards zero; it never rounds up.",
        "3": "Dividing two integers is valid standard C syntax."
    },
    "cos201-op-008": {
        "1": "(0 || 1) evaluates to 1 (true), so the if branch executes and prints 'True'.",
        "2": "The code prints the string literal 'True', not numeric 0.",
        "3": "The code prints the string literal 'True', not numeric 1."
    },
    "cos201-op-009": {
        "0": "2 is 'x', which is only selected if x > y is true (2 > 3 is false).",
        "2": "The ternary evaluates to the chosen operand's value (3), not boolean 0.",
        "3": "Using ternary expressions inside printf arguments is fully standard C."
    },
    "cos201-op-011": {
        "0": "(1 && 0) evaluates to 0 (false), so the else branch executes and prints 'No'.",
        "2": "The code outputs the string 'No', not 1.",
        "3": "The code outputs the string 'No', not 0."
    },
    "cos201-op-013": {
        "0": "1 is 'x', which would be selected only if x < y were false (1 < 2 is true).",
        "2": "The ternary yields the evaluated expression (y = 2), not 0.",
        "3": "The syntax is valid standard C."
    }
}

def apply_fixes():
    import glob
    cos_dir = "app/content/COS 201"
    files = sorted(glob.glob(os.path.join(cos_dir, "*.json")))
    
    updated_expl = 0
    updated_ww = 0
    
    for f in files:
        if "mock_exams" in f:
            continue
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            
        modified = False
        for q in data.get("questions", []):
            qid = q.get("id")
            if qid in EXAMINER_ENRICHMENTS:
                q["explanation"] = EXAMINER_ENRICHMENTS[qid]
                updated_expl += 1
                modified = True
                
            if qid in EXACT_WHY_WRONG_FIXES:
                if "why_wrong" not in q:
                    q["why_wrong"] = {}
                for k, v in EXACT_WHY_WRONG_FIXES[qid].items():
                    q["why_wrong"][k] = v
                updated_ww += 1
                modified = True
                
        if modified:
            with open(f, "w", encoding="utf-8") as fp:
                json.dump(data, fp, indent=2, ensure_ascii=False)
                
    print(f"Applied {updated_expl} explanation enrichments and {updated_ww} why_wrong dictionary updates.")

if __name__ == "__main__":
    apply_fixes()
