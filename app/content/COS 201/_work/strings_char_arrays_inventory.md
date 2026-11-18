# Topic Inventory: COS 201 — Topic 8: Strings & Character Arrays

## 1. Core Concepts & Definitions
- **String in C:** A sequence of characters stored in a contiguous 1-dimensional array of `char`, terminated by the null character `'\0'`. C has no native `string` data type.
- **Null Character (`'\0'`):** ASCII code 0 (all 8 bits zero). Acts as the sentinel delimiter signaling the end of the string to all string-handling functions.
- **String Length vs Array Size:**
  - `strlen(s)` returns the number of visible characters before `'\0'`.
  - The array holding string `s` must be sized at least `strlen(s) + 1` to accommodate `'\0'`.
  - Example: `"cat"` has length 3, but requires 4 bytes of memory (`'c'`, `'a'`, `'t'`, `'\0'`).

## 2. Declarations & Initialization
- **Character Array Initializations:**
  - `char s[] = "hello";` -> Sized automatically to 6 bytes (including `'\0'`). Mutable array in local stack memory.
  - `char s[5] = "hello";` -> Past Exam Q4: Compile warning or error; if accepted, no null terminator is appended, so `s` is a raw character array, NOT a valid C string!
  - `char s[10] = "hello";` -> Remaining 4 bytes are padded with `'\0'`.
  - `char s[] = {'h', 'e', 'l', 'l', 'o', '\0'};` -> Equivalent to string literal syntax.
- **String Literal Pointer:**
  - `char *p = "hello";` -> `p` points to a string literal in read-only / constant text memory.
  - Attempting to modify `*p = 'H';` causes undefined behavior (segmentation fault on modern OS).
  - To allow modification, declare as an array: `char s[] = "hello"; s[0] = 'H';` (valid).

## 3. String Input & Output Functions
- `printf("%s", str)`: Prints characters until `'\0'` is encountered.
- `puts(str)`: Prints string followed automatically by a newline `\n`.
- `scanf("%s", str)`:
  - Reads input up to the first whitespace (space, tab, newline).
  - Skips leading whitespace.
  - Does NOT check buffer capacity -> severe security vulnerability (buffer overflow).
  - Safe form: `scanf("%19s", str)` for a 20-byte buffer.
- `fgets(str, size, stdin)`:
  - Safe replacement: reads at most `size - 1` characters and always appends `'\0'`.
  - Retains trailing newline `\n` if room permits.

## 4. `<string.h>` Library Functions
- **`strlen(const char *s)`:** Returns `size_t` count of characters preceding `'\0'`.
- **`strcpy(char *dest, const char *src)`:** Copies characters from `src` to `dest` including `'\0'`. `dest` must have sufficient allocated space.
- **`strncpy(char *dest, const char *src, size_t n)`:** Copies up to `n` characters. If `strlen(src) >= n`, `dest` will NOT be null-terminated!
- **`strcat(char *dest, const char *src)`:** Appends `src` to `dest`, overwriting the original `'\0'` in `dest` and appending a new `'\0'`.
- **`strncat(char *dest, const char *src, size_t n)`:** Appends at most `n` characters and always adds a terminating null character.
- **`strcmp(const char *s1, const char *s2)`:**
  - Lexicographically compares ASCII values.
  - Returns `< 0` if `s1` comes before `s2`.
  - Returns `0` if `s1` and `s2` are identical.
  - Returns `> 0` if `s1` comes after `s2`.
  - Common trap: `if (strcmp(s1, s2))` evaluates to `false` when strings are equal! Correct test: `if (strcmp(s1, s2) == 0)`.

## 5. `<ctype.h>` Character Classification & Conversion
- `isalpha(c)`: Checks if character is alphabetic (A-Z, a-z).
- `isdigit(c)`: Checks if character is a digit (0-9).
- `isalnum(c)`: Checks if character is alphanumeric.
- `isspace(c)`: Checks for whitespace (space, `\t`, `\n`, `\r`, `\f`, `\v`).
- `toupper(c)`: Converts lowercase to uppercase.
- `tolower(c)`: Converts uppercase to lowercase.

## 6. Algorithmic Patterns
- Manual string length calculation with pointer.
- Manual string copy loop.
- In-place string reversal.
- Palindrome checking.
- Counting vowels/consonants/digits.
