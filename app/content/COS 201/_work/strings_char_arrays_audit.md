# Audit Report: COS 201 Topic 8 — Strings & Character Arrays

## 1. Topic Overview
- **Course:** COS 201 (Computer Programming I / C)
- **Topic:** Strings & Character Arrays (`strings_char_arrays`)
- **JSON File:** `app/content/COS 201/strings_char_arrays.json`
- **Total Questions:** 23 standard questions + 2 scenario case studies (4 sub-questions) = 27 items
- **Flashcards:** 8 key terms covered
- **Difficulty 3-4 (Apply/Analyze):** 13 / 27 (48.1%) -> Exceeds minimum 30% requirement

## 2. Past Exam Alignment (Nile Midterm Type B)
- **Direct Past Exam Coverage:**
  - Past Exam Q4 (`char arr[5] = "hello";` lack of space for `\0`) -> Fully covered in `cos201-str-001`.
  - The null terminator `'\0'` ASCII code 0 vs `'0'` (48) -> Covered in `cos201-str-002` and `cos201-str-fc02`.
  - `strlen` (visible chars) vs `sizeof` (total bytes including `'\0'`) -> Covered in `cos201-str-003` and `cos201-str-fc04`.
  - `strcat` string concatenation semantics -> Covered in `cos201-str-004`.
  - `strcmp` return value conventions (0 = equal, negative = less than, positive = greater than) -> Covered in `cos201-str-005` and `cos201-str-006`.
  - String literals as read-only memory segmentation fault hazard -> Covered in `cos201-str-007`.
  - Character classification via `<ctype.h>` (`isalpha`, `isdigit`) -> Covered in `cos201-str-008`.
  - Security hazards of `strcpy` vs bounded copies / `fgets` -> Covered in `cos201-str-009`, `cos201-str-012`, and `cos201-str-cs01`.
  - In-place string reversal and palindrome verification algorithm -> Covered in `cos201-str-010` and `cos201-str-cs02`.

## 3. GCC Verification Status
- **Compiler:** `gcc.exe (Rev13, MSYS2) 15.2.0` with `-Wall -Wextra -std=c11`
- **Verification Rate:** 100% of executable code questions compiled and executed in Windows MSYS2 GCC environment.
- **Verified Outputs:**
  - `cos201-str-003` (strlen vs sizeof): Output `len=4 size=5` verified.
  - `cos201-str-004` (strcat concatenation): Output `StudyBuddy` verified.
  - `cos201-str-005` (strcmp negative branch): Output `s1 before s2` verified.
  - `cos201-str-008` (ctype classification): Output `letters=4 digits=4` verified.
  - `cos201-str-010` (In-place reversal): Output `radar` verified.
  - `cos201-str-cs01-q1` (Safe bounded copy): Output `Compu` verified.
  - `cos201-str-cs02-q1` (Two-pointer palindrome verification): Output `1 0` verified.

## 4. Misconception and Option Quality Audit
- All MCQs feature fully justified distractor rationale in `why_wrong`.
- Deep student traps targeted:
  - Forgetting the null terminator byte when sizing arrays for strings (`"hello"` requires 6 bytes).
  - Confusing `strlen()` with `sizeof()`.
  - Inverting `strcmp` result (`if (strcmp(s1, s2))` is true when strings are UNEQUAL).
  - Attempting to mutate string literal pointers (`char *s = "text"; s[0]='T';`).
  - Relying on `strncpy` without realizing it omits the null terminator if source is too long.

## 5. Audit Verdict: PASSED
Ready for student practice and master index integration.
