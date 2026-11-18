# COS 201 — Midterm Past Questions (Type B) Inventory
*Source: Nile University of Nigeria — Faculty of Computing, Department of Software Engineering*
*Course: Computer Programming 1 (COS 201) — Midterm Examination (Type B, 60 minutes)*

---

## Question-by-Question Analysis & Concept Mapping

| # | Question Summary | Core C Concept | Question Type | Cognitive Level | GCC Verified Output |
|---|------------------|----------------|---------------|-----------------|---------------------|
| 1 | Correct way to declare a float variable | Variable declaration syntax | mcq | Level 1 (Recall) | N/A |
| 2 | Valid C keyword (`return` vs `main`, `printf`, `integer`) | Language keywords vs identifiers | mcq | Level 1 (Recall) | N/A |
| 3 | Code output: `int x=2; printf("%d", ++x);` | Pre-increment operator semantics | code_output | Level 3 (Apply) | `3` |
| 4 | Correct way to declare a character array (`char arr[5];`) | Array syntax & square brackets | mcq | Level 1 (Recall) | N/A |
| 5 | Code output: `while(a<4){ printf("%d ", a); a++; }` | While loop entry test & iteration | code_output | Level 3 (Apply) | `1 2 3 ` |
| 6 | Valid way to define a function returning void | Function header syntax | mcq | Level 2 (Understand) | N/A |
| 7 | Code output: `int a=5, b=2; printf("%d", a/b);` | Integer division truncation | code_output | Level 3 (Apply) | `2` |
| 8 | Operator used to compare two values (`==`) | Relational vs assignment operators | mcq | Level 1 (Recall) | N/A |
| 9 | Code output: `do{ printf("%d ", x); x++; } while(x<2);` | Do-while exit test execution | code_output | Level 3 (Apply) | `0 1 ` |
| 10 | Loop best suited when condition checked before execution | Pre-test loops (`while` / `for`) | mcq | Level 2 (Understand) | N/A |
| 11 | Code output: `int arr[3]={1,2,3}; printf("%d", arr[2]);` | Array 0-based indexing | code_output | Level 3 (Apply) | `3` |
| 12 | Syntax for `if - else if - else` | Control structure block syntax | mcq | Level 2 (Understand) | N/A |
| 13 | Code output: `int x=1,y=2; if(x>y) printf("X"); else printf("Y");` | Relational selection branch | code_output | Level 3 (Apply) | `Y` |
| 14 | Correct single-line comment in C (`//`) | C99/C11 comment syntax | mcq | Level 1 (Recall) | N/A |
| 15 | Code output: `int a=3,b=4; printf("%d", a+b*2);` | Arithmetic operator precedence | code_output | Level 3 (Apply) | `11` |
| 16 | Correct declaration of a 2D array (`int arr[2][3];`) | Multidimensional array syntax | mcq | Level 2 (Understand) | N/A |
| 17 | Code output: `for(int i=0;i<3;i++) x+=i;` | For loop variable accumulation | code_output | Level 3 (Apply) | `3` |
| 18 | Correct ternary operator usage (`x = a>b ? y : z;`) | Conditional operator syntax | mcq | Level 2 (Understand) | N/A |
| 19 | Code output: `switch(a){ case 1: ... case 5: printf("Five"); break; }` | Switch case matching with break | code_output | Level 3 (Apply) | `Five` |
| 20 | Correct way to increment variable by 1 (`x=x+1`, `x++`, `++x`) | Increment expressions equivalence | mcq | Level 2 (Understand) | N/A |
| 21 | Code output: `int arr[4]={2,4,6,8}; printf("%d", arr[1]+arr[3]);` | Array element retrieval & sum | code_output | Level 3 (Apply) | `12` |
| 22 | True statement about arrays (consecutive memory locations) | Array memory contiguity | mcq | Level 2 (Understand) | N/A |
| 23 | Code output: `int x=0; if(x||1) printf("True"); else printf("False");` | Logical OR truth table & short-circuit | code_output | Level 3 (Apply) | `True` |
| 24 | Declare multiple variables in single line (`int x,y,z;`) | Comma-separated declarator list | mcq | Level 1 (Recall) | N/A |
| 25 | Code output: `int x=2,y=3; printf("%d", x>y?x:y);` | Ternary operator evaluation | code_output | Level 3 (Apply) | `3` |
| 26 | Defining a constant in C (`#define PI 3.14`) | Preprocessor macro constants | mcq | Level 2 (Understand) | N/A |
| 27 | Code output: `while(i<=3){ printf("%d ", i++); }` | Post-increment in print statement | code_output | Level 3 (Apply) | `1 2 3 ` |
| 28 | True statement about functions (help modular programming) | Modular software design in C | mcq | Level 2 (Understand) | N/A |
| 29 | Code output: `if(x>10)... else if(x>3) printf("Medium");...` | Multi-way ladder evaluation | code_output | Level 3 (Apply) | `Medium` |
| 30 | Operator used for modulus (`%`) | Remainder operator | mcq | Level 1 (Recall) | N/A |
| 31 | Code output: `int arr[3]={10,20,30}; printf("%d", arr[0]+arr[2]);` | 0-based boundary summing | code_output | Level 3 (Apply) | `40` |
| 32 | Correct syntax for declaring a pointer (`int *p;`) | Pointer type declarator syntax | mcq | Level 2 (Understand) | N/A |
| 33 | Code output: `int x=1,y=0; if(x&&y) printf("Yes"); else printf("No");` | Logical AND evaluation with zero | code_output | Level 3 (Apply) | `No` |
| 34 | Increment variable by 2 (`x+=2;` and `x=x+2;`) | Compound assignment equivalence | mcq | Level 2 (Understand) | N/A |
| 35 | Code output: `for(i=0;i<3;i++) printf("%d ", i*2);` | Scaled index printing in loop | code_output | Level 3 (Apply) | `0 2 4 ` |
| 36 | Declare 1D array of 10 integers (`int arr[10];`) | Sized array declaration | mcq | Level 1 (Recall) | N/A |
| 37 | Code output: `switch(x){ case 1: ... case 2: ... default: printf("Other");}` | Switch default branch execution | code_output | Level 3 (Apply) | `Other` |
| 38 | Correct syntax to declare a constant integer | `const int x=5;` vs `#define` | mcq | Level 2 (Understand) | N/A |
| 39 | Code output: `int x=1,y=2; printf("%d", x<y?y:x);` | Ternary conditional selection | code_output | Level 3 (Apply) | `2` |
| 40 | Terminate a loop immediately (`break`) | Jump statements (`break` vs `continue`) | mcq | Level 1 (Recall) | N/A |
