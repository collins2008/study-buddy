import subprocess
import tempfile
import os

code_snippets = {
    'q3': '''#include <stdio.h>
int main(void) {
    int x = 2;
    printf("%d", ++x);
    return 0;
}''',
    'q5': '''#include <stdio.h>
int main(void) {
    int a = 1;
    while(a < 4) {
        printf("%d ", a);
        a++;
    }
    return 0;
}''',
    'q7': '''#include <stdio.h>
int main(void) {
    int a = 5, b = 2;
    printf("%d", a / b);
    return 0;
}''',
    'q9': '''#include <stdio.h>
int main(void) {
    int x = 0;
    do {
        printf("%d ", x);
        x++;
    } while(x < 2);
    return 0;
}''',
    'q11': '''#include <stdio.h>
int main(void) {
    int arr[3] = {1, 2, 3};
    printf("%d", arr[2]);
    return 0;
}''',
    'q13': '''#include <stdio.h>
int main(void) {
    int x = 1, y = 2;
    if(x > y)
        printf("X");
    else
        printf("Y");
    return 0;
}''',
    'q15': '''#include <stdio.h>
int main(void) {
    int a = 3, b = 4;
    printf("%d", a + b * 2);
    return 0;
}''',
    'q17': '''#include <stdio.h>
int main(void) {
    int x = 0;
    for(int i = 0; i < 3; i++) {
        x += i;
    }
    printf("%d", x);
    return 0;
}''',
    'q19': '''#include <stdio.h>
int main(void) {
    int a = 5;
    switch(a) {
        case 1: printf("One"); break;
        case 5: printf("Five"); break;
        default: printf("Other");
    }
    return 0;
}''',
    'q21': '''#include <stdio.h>
int main(void) {
    int arr[4] = {2, 4, 6, 8};
    printf("%d", arr[1] + arr[3]);
    return 0;
}''',
    'q23': '''#include <stdio.h>
int main(void) {
    int x = 0;
    if(x || 1)
        printf("True");
    else
        printf("False");
    return 0;
}''',
    'q25': '''#include <stdio.h>
int main(void) {
    int x = 2, y = 3;
    printf("%d", x > y ? x : y);
    return 0;
}''',
    'q27': '''#include <stdio.h>
int main(void) {
    int i = 1;
    while(i <= 3) {
        printf("%d ", i++);
    }
    return 0;
}''',
    'q29': '''#include <stdio.h>
int main(void) {
    int x = 5;
    if(x > 10)
        printf("Big");
    else if(x > 3)
        printf("Medium");
    else
        printf("Small");
    return 0;
}''',
    'q31': '''#include <stdio.h>
int main(void) {
    int arr[3] = {10, 20, 30};
    printf("%d", arr[0] + arr[2]);
    return 0;
}''',
    'q33': '''#include <stdio.h>
int main(void) {
    int x = 1, y = 0;
    if(x && y)
        printf("Yes");
    else
        printf("No");
    return 0;
}''',
    'q35': '''#include <stdio.h>
int main(void) {
    int i = 0;
    for(i = 0; i < 3; i++) {
        printf("%d ", i * 2);
    }
    return 0;
}''',
    'q37': '''#include <stdio.h>
int main(void) {
    int x = 3;
    switch(x) {
        case 1: printf("One"); break;
        case 2: printf("Two"); break;
        default: printf("Other");
    }
    return 0;
}''',
    'q39': '''#include <stdio.h>
int main(void) {
    int x = 1, y = 2;
    printf("%d", x < y ? y : x);
    return 0;
}'''
}

results = {}
for qid, code in code_snippets.items():
    with tempfile.NamedTemporaryFile(suffix='.c', delete=False, mode='w', encoding='utf-8') as f:
        f.write(code)
        c_path = f.name
    exe_path = c_path.replace('.c', '.exe')
    try:
        c_res = subprocess.run(['gcc', '-Wall', '-Wextra', '-std=c11', c_path, '-o', exe_path], capture_output=True, text=True)
        if c_res.returncode != 0:
            print(f'{qid}: COMPILE ERROR: {c_res.stderr}')
            results[qid] = {'error': c_res.stderr}
            continue
        r_res = subprocess.run([exe_path], capture_output=True, text=True, timeout=5)
        out = r_res.stdout
        print(f'{qid}: stdout = "{out}"')
        results[qid] = {'stdout': out}
    finally:
        if os.path.exists(c_path): os.remove(c_path)
        if os.path.exists(exe_path): os.remove(exe_path)
