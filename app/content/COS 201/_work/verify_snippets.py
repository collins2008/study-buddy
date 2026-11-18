import subprocess
import os
import tempfile
import json

def verify_c_code(code_str):
    temp_dir = tempfile.mkdtemp()
    src_file = os.path.join(temp_dir, 'test.c')
    exe_file = os.path.join(temp_dir, 'test.exe')
    
    with open(src_file, 'w', encoding='utf-8') as f:
        f.write(code_str)
        
    comp = subprocess.run(['gcc', '-Wall', '-Wextra', '-std=c11', src_file, '-o', exe_file], capture_output=True, text=True)
    if comp.returncode != 0:
        return {'success': False, 'stage': 'compilation', 'error': comp.stderr, 'output': ''}
        
    try:
        run = subprocess.run([exe_file], capture_output=True, text=True, timeout=5)
        return {'success': True, 'stage': 'run', 'error': run.stderr, 'output': run.stdout}
    except subprocess.TimeoutExpired:
        return {'success': False, 'stage': 'timeout', 'error': 'Execution timed out (possible infinite loop)', 'output': ''}

if __name__ == '__main__':
    test_cases = [
        ("int x = 2; printf(\"%d\", ++x);", """#include <stdio.h>
int main() {
    int x = 2;
    printf("%d", ++x);
    return 0;
}"""),
        ("int a = 5, b = 2; printf(\"%d\", a/b);", """#include <stdio.h>
int main() {
    int a = 5, b = 2;
    printf("%d", a / b);
    return 0;
}"""),
        ("macro expansion without parens", """#include <stdio.h>
#define VAL 10 + 2
int main() {
    int res = VAL * 3;
    printf("%d", res);
    return 0;
}"""),
        ("char to int arithmetic", """#include <stdio.h>
int main() {
    char c = 'A';
    printf("%c %d", c + 1, c + 1);
    return 0;
}"""),
        ("implicit truncation float to int", """#include <stdio.h>
int main() {
    int x = 5.99;
    printf("%d", x);
    return 0;
}"""),
        ("format specifier mismatch float as int", """#include <stdio.h>
int main() {
    int a = 65;
    printf("%c-%d", a, a);
    return 0;
}""")
    ]

    for label, code in test_cases:
        res = verify_c_code(code)
        print(f"[{label}] -> Output: '{res['output']}' | Success: {res['success']}")
