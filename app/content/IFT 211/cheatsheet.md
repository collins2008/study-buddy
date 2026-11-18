# IFT 211: Digital Logic & Design — 1-Page Exam Cheatsheet
*Nile University of Nigeria — Department of Computer Science (200 Level, First Semester)*

---

## 1. Number Systems & Base Conversions
- **Radix Weights**: Base $r$ value $= \sum_{i} d_i \cdot r^i$. Decimal $\to$ Binary (repeated $\div 2$, record remainders bottom-up). Binary fraction $\to$ Decimal (repeated $\times 2$, record integer carries top-down).
- **Nibble Grouping**:
  - Binary $\leftrightarrow$ Hex: Group in 4s from binary point ($1101\ 1010_2 \to \text{DA}_{16}$).
  - Binary $\leftrightarrow$ Octal: Group in 3s from binary point ($101\ 110_2 \to 56_8$).
- **Exam Specific Conversions**:
  - $51_{10} = 32 + 16 + 2 + 1 = 00110011_2$.
  - $0.625_{10} = 0.5 + 0.125 = 0.101_2$.

---

## 2. Signed Arithmetic & Complements
- **Complements Definition**:
  - $r$'s complement of $N$: $r^n - N$. ($2$'s complement $= 1$'s complement $+ 1$).
  - Diminished radix $(r-1)$'s complement: $(r^n - 1) - N$. Invert all bits for 1's complement.
- **8-Bit Signed 2's Complement Range**: $[-2^7, +2^7 - 1] = [-128, +127]$.
  - $+44 = 00101100_2$.
  - $+14 = 00001110_2 \implies -14 = 11110001 + 1 = 11110010_2$.
  - $(+44) + (+14) = 00111010_2 = +58_{10}$.
  - $(+44) + (-14) = 00101100 + 11110010 = 1\ 00011110_2 \implies \mathbf{00011110_2 = +30_{10}}$ (discard end carry).
- **Multi-Method Subtraction ($M - N = 1001000_2 - 111001_2 = 72 - 57 = 15_{10} = 0001111_2$)**:
  - *Direct Borrowing*: Borrowing from position $k$ brings a weight of 2 to position $k-1$.
  - *1's Complement*: $1001000 + 1000110 = 1\ 0001110 \xrightarrow{+1 \text{ end carry}} \mathbf{0001111_2}$ (end-around carry).
  - *2's Complement*: $1001000 + 1000111 = 1\ 0001111 \implies \mathbf{0001111_2}$ (discard end carry).
- **Signed Overflow**: $V = C_{\text{in}}(\text{MSB}) \oplus C_{\text{out}}(\text{MSB}) = C_{n-1} \oplus C_n$.

---

## 3. Binary Encodings & ASCII
- **BCD (8421)**: Encodes digits 0–9. Codes $1010$–$1111$ are invalid don't-cares.
  - $1001\ 0001\ 0100_{\text{BCD}} \to \text{Digits } 9, 1, 4 \implies 914_{10} = \mathbf{1110010010_2}$.
- **Gray Code (Unit Distance)**:
  - *Binary $\to$ Gray*: $G_{n-1} = B_{n-1}$; $G_i = B_i \oplus B_{i+1}$.
    - $21_{10} = 10101_2 \implies G = 1, (1\oplus 0=1), (0\oplus 1=1), (1\oplus 0=1), (0\oplus 1=1) \implies \mathbf{11111_{\text{Gray}}}$.
  - *Gray $\to$ Binary*: $B_{n-1} = G_{n-1}$; $B_i = B_{i+1} \oplus G_i$.
    - $11101_{\text{Gray}} \implies B = 1, (1\oplus 1=0), (0\oplus 1=1), (1\oplus 0=1), (1\oplus 1=0) \implies \mathbf{10110_2 = 22_{10}}$.
- **ASCII Decoding**: Space $= 32_{10}$; Hyphen $= 45_{10}$; Digits `'0'-'9'` $= 48-57$; Upper `'A'-'Z'` $= 65-90$; Lower `'a'-'z'` $= 97-122$.
  - Exam Stream $[67, 111, 100, 101, 100, 32, 45, 32, 48, 50, 49, 49] \implies \mathbf{"Coded - 0211"}$.

---

## 4. Boolean Algebra & De Morgan's Laws
- **Postulates**: Identity ($A+0=A$, $A\cdot 1=A$), Null ($A+1=1$, $A\cdot 0=0$), Idempotence ($A+A=A$, $A\cdot A=A$), Complement ($A+A'=1$, $A\cdot A'=0$), Involution ($A''=A$).
- **Distributive**: $A + BC = (A+B)(A+C)$ *(Key examiner trick)*; $A(B+C) = AB + AC$.
- **De Morgan**: $(A + B)' = A' \cdot B'$; $(A \cdot B)' = A' + B'$. General: $(x_1 + x_2 + \dots + x_n)' = x_1'x_2'\dots x_n'$.
- **Absorption**: $A + AB = A$; $A(A + B) = A$; $A + A'B = A + B$.
- **Consensus**: $AB + A'C + BC = AB + A'C$.

---

## 5. Gate Classifications & Universal Synthesis
- **Lecturer Gate Classification**:
  - **Primary Gates**: $\mathbf{OR, AND, NOT}$.
  - **Universal Gates**: $\mathbf{NAND, NOR}$ (each functionally complete).
  - **Derived Arithmetic**: $\mathbf{XOR}$ ($A'B + AB'$), $\mathbf{XNOR}$ ($AB + A'B'$).
- **Minimum Gate Counts for Synthesis**:
  | Function | NAND Gates | NOR Gates |
  |----------|:----------:|:---------:|
  | NOT | 1 | 1 |
  | AND | 2 | 3 |
  | OR | 3 | 2 |
  | XOR | 4 | 5 (or 4 with dual rail) |
  | XNOR | 5 | 4 |
- **Electrical Parameters**:
  - Fan-in: Max inputs a gate accepts.
  - Fan-out: Max standard loads output can drive without sagging ($\min(I_{OH}/I_{IH}, I_{OL}/I_{IL})$).
  - Power-Delay Product (PDP): $P \times t_{pd}$ (Joules).

---

## 6. Combinational Arithmetic & MSI Blocks
- **Half Adder**: $\text{Sum} = A \oplus B$, $\text{Carry} = AB$.
- **Full Adder**: $\text{Sum} = A \oplus B \oplus C_{\text{in}}$, $C_{\text{out}} = AB + C_{\text{in}}(A \oplus B) = AB + BC_{\text{in}} + AC_{\text{in}}$.
  - Built from: 2 Half Adders + 1 OR gate.
  - Ripple Delay: $2N - 1$ gate delays (32 bits $\implies 63$ delays).
- **Half Subtractor**: $\text{Diff} = X \oplus Y$, $\text{Borrow} = X'Y$.
- **Full Subtractor**: $\text{Diff} = A \oplus B \oplus B_{\text{in}}$, $B_{\text{out}} = A'B + B_{\text{in}}(A \oplus B)'$.
- **Adder-Subtractor**: Mode $M=0$ adds ($B \oplus 0 = B$, $C_0=0$); $M=1$ subtracts ($B \oplus 1 = B'$, $C_0=1 \implies A + B' + 1$).
- **MSI Blocks**:
  - *Decoder*: $n$ inputs $\to 2^n$ active-high minterms. Minterms combined via OR gate.
  - *Priority Encoder*: Resolves simultaneous inputs by precedence hierarchy.
  - *Multiplexer (MUX)*: $2^n$ inputs, $n$ select lines, 1 output. $Y = \sum m_k \cdot D_k$.
- **Exam Exercise VI Circuit**:
  - Inputs $A, B, C \implies R = A \oplus B$, $S = B \cdot C'$, $\mathbf{X = (A \oplus B) + B \cdot C' = \Sigma m(2, 3, 4, 5, 6)}$.

---

## 7. Karnaugh Maps (K-Maps) & Minimization
- **Coordinates**: Gray code `00, 01, 11, 10` (Hamming distance = 1).
- **Toroidal Wrap-Around**: Four corners $m_0(0000), m_2(0010), m_8(1000), m_{10}(1010) \implies \mathbf{B'D'}$.
- **Implicant Hierarchy**:
  - *Prime Implicant (PI)*: Maximal power-of-2 group ($1, 2, 4, 8, 16$).
  - *Essential Prime Implicant (EPI)*: Covers a '1' covered by no other PI. Must be retained.
- **Product of Sums (POS)**: Group 0s to get $F'$, apply De Morgan $\implies F = (F')'$.
- **Don't Cares ($X$)**: Include $X$ only if it enlarges an existing group of 1s (saving literals); never circle $X$s alone.
  - BCD Prime Detector ($2, 3, 5, 7$ with $X$ at $10-15$) $\implies \mathbf{F = B'C + BD}$ (saves 2 literals).
