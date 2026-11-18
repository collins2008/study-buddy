import os
import sys
import json

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CONTENT_DIR = os.path.abspath("app/content/COS 201")

UPDATES = {
    "cos201-cf-015": (
        "control_flow_selection.json",
        "In C, selection structures evaluate boolean expressions to determine control transfer: "
        "'if' provides single-selection executing code only when true; 'if-else' provides double-selection choosing between two mutually exclusive execution paths; "
        "'switch' provides multi-selection dispatching execution to integral constant case labels; and the ternary operator (?:) provides inline conditional evaluation returning an expression value."
    ),
    "cos201-cf-018": (
        "control_flow_selection.json",
        "The 'dangling else' ambiguity arises in nested 'if' statements when an 'else' clause is written without explicit compound statement braces. "
        "In C grammar (ANSI/ISO C99 Section 6.8.4.1), an 'else' unconditionally associates with the closest preceding unmatched 'if' within the same block scope, "
        "regardless of the programmer's visual indentation. If the outer condition fails, the inner block is bypassed completely. "
        "Enclosing inner selection statements inside curly braces '{ ... }' explicitly delineates block scope, forcing the compiler to bind the 'else' to the intended outer 'if' and preventing silent logic defects."
    ),
    "cos201-fn-008": (
        "functions_modular.json",
        "The 'void' keyword, when used as a function return type specifier in C, informs the compiler that the function performs an action (side effect) but produces no return value for the caller. "
        "Attempting to assign the result of a void function call to any variable results in a compile-time type mismatch error. "
        "Inside a void function, a bare 'return;' statement terminates execution early without an expression."
    ),
    "cos201-fn-010": (
        "functions_modular.json",
        "In C, storage class and declaration placement dictate memory duration and accessibility: "
        "Local auto variables possess block scope and automatic storage duration (created on the call stack at function entry and destroyed upon exit); "
        "Local static variables have block scope but static storage duration (retaining their values across multiple calls in the data segment); "
        "Global variables defined outside any function have file scope and static storage duration across the entire translation unit; "
        "and Register variables suggest placement in high-speed CPU registers without addressable memory locations (& operator prohibited)."
    ),
    "cos201-fn-011": (
        "functions_modular.json",
        "During a C function call: (1) The caller pushes arguments onto the call stack or loads them into ABI calling convention registers; "
        "(2) The 'call' instruction pushes the return address (the next instruction in the caller) onto the stack; "
        "(3) The function prologue allocates a new stack frame (activation record) by adjusting the base pointer (EBP/RBP) and stack pointer (ESP/RSP); "
        "(4) The callee's body executes local operations; "
        "(5) The function epilogue tears down local frame allocations, stores the return value in the designated accumulator register (EAX/RAX), and the 'ret' instruction pops the return address, restoring caller execution."
    ),
    "cos201-fn-012": (
        "functions_modular.json",
        "The iterative power function initializes a result accumulator to 1, then loops 'exp' times multiplying 'result *= base'. "
        "This algorithm runs in O(exp) linear time complexity and O(1) auxiliary space, correctly handling exp = 0 by returning 1 (since any non-zero number to power 0 equals 1). "
        "Both parameters are passed by value, leaving caller arguments unmodified."
    ),
    "cos201-fn-013": (
        "functions_modular.json",
        "C is strictly 'pass-by-value': when any argument is passed to a function, the runtime makes an independent copy of the value and places it into the callee's parameter stack frame. "
        "Modifications to parameters inside the function alter only the local copy, not the caller's variable. "
        "To simulate 'pass-by-reference' (allowing a function to mutate caller variables), programmers pass the address of the variable using the address-of operator (&var). "
        "The receiving function declares a pointer parameter (type *ptr) and dereferences it (*ptr = value) to directly access and overwrite the caller's memory location in place."
    ),
    "cos201-lp-014": (
        "loops_iteration.json",
        "The 'continue' statement immediately terminates only the current iteration of the innermost enclosing loop ('for', 'while', or 'do-while'). "
        "In a 'while' or 'do-while' loop, control transfers directly to the loop condition evaluation. "
        "In a 'for' loop, control transfers directly to the iteration/increment expression (e.g. 'i++') before the loop test condition is evaluated."
    ),
    "cos201-lp-016": (
        "loops_iteration.json",
        "C provides three distinct loop constructs: "
        "'for' is ideal for counter-controlled definite iteration where initialization, condition, and increment are centralized in the header; "
        "'while' is an entry-controlled (pre-test) loop executing 0 or more times, checking the condition prior to entering the body; "
        "and 'do-while' is an exit-controlled (post-test) loop guaranteed to execute at least once (1 or more times) because the evaluation condition is tested after the body executes."
    ),
    "cos201-lp-018": (
        "loops_iteration.json",
        "Factorial computation requires multiplying sequential integers from 1 up to N (5! = 1 * 2 * 3 * 4 * 5 = 120). "
        "The accumulator variable 'fact' must be initialized to 1 (not 0, which would zero-out the product). "
        "The for loop header 'for (int i = 1; i <= 5; i++) fact *= i;' executes 5 iterations, producing the final product 120."
    ),
    "cos201-lp-019": (
        "loops_iteration.json",
        "A programmer should choose 'do-while' instead of 'while' whenever the body of the loop MUST execute at least once before testing the loop exit condition. "
        "Classic real-world exam examples include: (1) Interactive menu-driven console applications where the menu options must be displayed to the user before reading their choice; "
        "(2) User input validation prompts (e.g. asking for a positive number or password) where the prompt and read must happen first, repeating only if the input fails validation; "
        "and (3) Network retry handshakes where an initial connection attempt is mandatory before testing connection success."
    ),
    "cos201-str-013": (
        "strings_char_arrays.json",
        "The standard `<string.h>` library provides fundamental operations on null-terminated character sequences: "
        "'strlen(s)' traverses memory until encountering the null terminator '\\0' and returns the character count (excluding '\\0'); "
        "'strcpy(dest, src)' copies characters including the null terminator into a pre-allocated destination buffer; "
        "'strcat(dest, src)' appends 'src' to the end of 'dest', overwriting the original null terminator of 'dest' and appending a new one; "
        "and 'strcmp(s1, s2)' performs lexicographical comparison returning 0 if equal, negative if s1 < s2, and positive if s1 > s2."
    )
}

def enrich():
    print("--- Enriching COS 201 Explanations with Rigorous Examiner Rationale ---")
    files_to_save = {}
    
    for qid, (fname, new_expl) in UPDATES.items():
        if fname not in files_to_save:
            fpath = os.path.join(CONTENT_DIR, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                files_to_save[fname] = json.load(f)
                
        d = files_to_save[fname]
        updated = False
        for q in d.get("questions", []):
            if q.get("id") == qid:
                q["explanation"] = new_expl
                updated = True
                print(f"  ✓ Upgraded explanation for {qid} in {fname}")
                break
        assert updated, f"Could not find {qid} in {fname}"
        
    for fname, data in files_to_save.items():
        fpath = os.path.join(CONTENT_DIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
    print("Enrichment complete!\n")

if __name__ == "__main__":
    enrich()
