# IFT 211 — Digital Logic and Design
## Exam Style Guide & Pedagogical Blueprint
*Derived directly from Nile University 2024/2025 Final Examination Paper, Department of Computer Sciences, & Lecturer Notes*

---

## 1. Exam Structure & Profile
- **Course**: IFT 211 — Digital Logic and Design (2 Credit Units)
- **Time Allocated**: 1 hour 30 minutes
- **Total Marks**: 60 Marks
- **Format**: Structured Multi-Part Problem Solving + Multi-Choice Calculation & Logic Questions.
- **Examiner's Core Pillars**:
  1. **Binary & Number System Arithmetic (~35%)**:
     - Base conversions (Decimal $\leftrightarrow$ Binary $\leftrightarrow$ Octal $\leftrightarrow$ Hexadecimal).
     - Signed binary arithmetic using 2's complement representation.
     - Multi-method subtraction: (a) Direct binary borrowing, (b) 1's complement method, (c) 2's complement method with end-carry/overflow analysis.
  2. **Binary Encodings & Character Sets (~25%)**:
     - Binary Coded Decimal (BCD): converting 4-bit nibbles to decimal and thence to pure binary.
     - Gray Code: Binary-to-Gray ($G_i = B_i \oplus B_{i+1}$) and Gray-to-Binary ($B_{n-1} = G_{n-1}$, $B_i = B_{i+1} \oplus G_i$).
     - 8-bit ASCII Decoding: string decoding from byte streams (spaces `032`, hyphens `045`, digits `48-57`, uppercase `65-90`, lowercase `97-122`).
  3. **Boolean Algebra & Gate Synthesis (~25%)**:
     - Truth tables for multi-input combinational logic.
     - Logic circuit node tracing (determining intermediate expressions $R, Q, S, T, C$).
     - Gate classification (Lecturer Emphasis: **OR, AND, NOT** are *primary gates*; **NAND, NOR** are *universal gates*).
     - Sum-of-Products (SOP), Product-of-Sums (POS), and XOR/XNOR simplification.
  4. **Karnaugh Maps & Minimization (~15%)**:
     - 2-, 3-, and 4-variable K-maps, Gray code adjacency, prime implicants, and don't-care conditions.

---

## 2. Command Words & Phrasing Patterns (Exact Nile University Phrasing)
All generated questions must imitate the examiner's precise terminology:
- *"Perform the arithmetic operations (+A) + (+B) and (+A) + (-B) in binary using their 2's complement form."*
- *"Using any two of the three methods of subtractions done in class, perform: ... (show your works)."*
- *"What is the binary representation of the decimal number ...?"*
- *"What is the hexadecimal equivalent of the binary number ...?"*
- *"Convert the Binary stream into ASCII-code to reveal the hidden text."*
- *"Find (a) the Gray code equivalent of decimal ... and (b) the binary equivalent of Gray code number ..."*
- *"A given this BCD number ... convert into an equivalent binary number."*
- *"Provide the Boolean expression and the truth table for the logic circuit below."*
- *"Draw / specify the logic circuit that leads to this Boolean expression: X = A ⊕ B + B · C'."*
- *"State which gates are considered primary and justify why NAND and NOR are universal gates."*

---

## 3. Recurring Examiner Traps & Misconceptions
The Nile University examiner systematically tests specific digital logic edge cases:
1. **Bit-Length Overflow in 2's Complement:**
   - In 8-bit signed arithmetic, range is $[-128, +127]$. Adding two positive numbers that yield $\ge 128$ results in negative sign bit (overflow flag set).
2. **End-Around Carry in 1's Complement vs 2's Complement:**
   - In 1's complement subtraction, an end carry must be added back to the LSB (end-around carry). In 2's complement, an end carry is simply discarded!
3. **BCD vs Binary Distinction:**
   - BCD `1001 0001 0100` represents digits `9`, `1`, `4` (decimal $914$), NOT binary $2324$. To convert BCD to binary, first extract the decimal digits, then convert the decimal number to binary.
4. **Gray Code Conversion Rules:**
   - Decimal $21 \to$ Binary $10101_2 \to$ Gray: MSB unchanged ($1$), next bits are $B_i \oplus B_{i-1} \implies 1, (1\oplus 0=1), (0\oplus 1=1), (1\oplus 0=1), (0\oplus 1=1) \implies 11111_{\text{Gray}}$.
   - Gray-to-Binary: $11101_{\text{Gray}} \implies B_4=1; B_3=1\oplus 1=0; B_2=0\oplus 1=1; B_1=1\oplus 0=1; B_0=1\oplus 1=0 \implies 10110_2$ (decimal $22$).
5. **Universal Gate Property:**
   - NAND can implement NOT ($A \text{ NAND } A$), AND ($(A \text{ NAND } B) \text{ NAND } (A \text{ NAND } B)$), and OR ($(A \text{ NAND } A) \text{ NAND } (B \text{ NAND } B)$).
   - Primary gates cannot implement each other without combining.

---

## 4. Verification Standards for IFT 211
Every numeric calculation, base conversion, 2's complement addition/subtraction, truth table row, and Boolean simplification must:
1. Be cross-verified by dual independent Python verification scripts.
2. Provide step-by-step mathematical working in `explanation`.
3. Include explicit `why_wrong` explanations detailing the exact arithmetic misstep for all distractors.
