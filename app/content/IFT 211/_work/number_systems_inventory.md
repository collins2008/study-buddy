# IFT 211 — Topic 1: Number Systems Inventory
*Source: Digital Logic Lecture Notes (A.F. Kana), Pages 1–6 & Nile University Exam Papers*

---

## 1. Core Concepts & Definitions
- **Radix (Base $b$):** The total number of unique digits available in a positional numbering system.
  - Base 2 (Binary): $\{0, 1\}$
  - Base 8 (Octal): $\{0, 1, 2, 3, 4, 5, 6, 7\}$
  - Base 10 (Decimal): $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$
  - Base 16 (Hexadecimal): $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \text{A}, \text{B}, \text{C}, \text{D}, \text{E}, \text{F}\}$ where $\text{A}=10, \text{B}=11, \text{C}=12, \text{D}=13, \text{E}=14, \text{F}=15$.
- **Positional Weighting:** Value of digit $d_i$ at position $i$ is $d_i \times b^i$.
  - Radix point separates positive powers $b^0, b^1, b^2 \dots$ from negative fractional powers $b^{-1}, b^{-2}, b^{-3} \dots$

---

## 2. Algorithms & Conversion Procedures

### A. Decimal to Any Base $b$
1. **Integer Part:** Successive division by $b$.
   - Divide integer by $b$; record quotient and integer remainder.
   - Repeat with quotient until quotient $= 0$.
   - Read remainders in reverse order (last remainder is Most Significant Digit, MSD).
2. **Fractional Part:** Successive multiplication by $b$.
   - Multiply fractional part by $b$.
   - Extract the integer part as the next digit after the radix point.
   - Repeat with the remaining fraction until fraction $= 0$ or required precision is reached.
   - Read integer digits from top to bottom.

### B. Any Base $b$ to Decimal
- Polynomial expansion: $N_{10} = \sum_{i=-m}^{n-1} d_i \cdot b^i$.
- Example: $4\text{B}3_{16} = 4 \times 16^2 + 11 \times 16^1 + 3 \times 16^0 = 1024 + 176 + 3 = 1203_{10}$.
- Example with fraction: $156.1875_{10}$ or $0.3_{16} = 3 \times 16^{-1} = 0.1875_{10}$.

### C. Direct Power-of-Two Conversions ($2 \leftrightarrow 8 \leftrightarrow 16$)
- **Binary to Octal ($2 \to 8$):** Group binary bits into sets of 3, starting from radix point (left for integer, right for fraction). Pad outermost groups with zeros. Replace each triplet with its octal digit ($000_2 \to 0$ up to $111_2 \to 7$).
- **Binary to Hexadecimal ($2 \to 16$):** Group binary bits into sets of 4, starting from radix point. Pad outermost with zeros. Replace each nibble with hex digit ($0000_2 \to 0$ to $1111_2 \to \text{F}$).
- **Octal to Hexadecimal ($8 \to 16$):** Expand each octal digit into 3 binary bits, then regroup into sets of 4 bits.

---

## 3. Past Exam Questions Involving Number Systems
- Nile Final Exam Exercise II, Q1: Decimal 51 to Binary $\implies 51_{10} = 32 + 16 + 2 + 1 = 00110011_2$.
- Nile Final Exam Exercise II, Q2: Binary $11011010_2$ to Hex $\implies 1101_2 = \text{D}, 1010_2 = \text{A} \implies \text{DA}_{16}$.
- Worked textbook examples: $1341_{10} \implies 10100111101_2 = 2475_8 = 53\text{D}_{16}$.
- Fractional conversions: $0.6875_{10} \implies 0.1011_2$.

---

## 4. Common Misconceptions & Traps
1. **Padded Zeros Placement:** Padding zeros on the wrong side of fractional groups (e.g. padding $0.1_2$ on the left instead of the right $0.100_2$).
2. **Hex Digits $\ge 10$:** Confusing $\text{B}$ ($11$) with $\text{D}$ ($13$) or $\text{E}$ ($14$).
3. **Remainder Reading Order:** Reading remainders top-to-bottom instead of bottom-to-top (MSD).
4. **Fractional Termination:** Assuming fractional multiplication always terminates (many decimal fractions like $0.1_{10}$ are recurring infinite binary fractions).
