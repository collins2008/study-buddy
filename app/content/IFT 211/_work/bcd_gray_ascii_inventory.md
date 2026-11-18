# IFT 211 — Topic 3: BCD, Gray Code & ASCII Encoding Inventory
*Source: Digital Logic Lecture Notes (A.F. Kana), Pages 11–14 & Nile Final Examination (Exercises III & IV)*

---

## 1. Binary Coded Decimal (BCD)
- **Concept:** Representation of decimal numbers where each decimal digit ($0..9$) is individually encoded by its 4-bit binary equivalent ($0000_2$ to $1001_2$).
- **Position Weights:** Standard BCD is $8421$.
- **Invalid / Illegal BCD States:** 6 out of 16 states are invalid for a single decimal digit: $1010_2$ (10), $1011_2$ (11), $1100_2$ (12), $1101_2$ (13), $1110_2$ (14), $1111_2$ (15).
- **BCD vs Pure Binary Conversion Distinction:**
  - Decimal $13 \implies$ Pure Binary $= 1101_2$.
  - Decimal $13 \implies$ BCD $= 0001\ 0011_{\text{BCD}}$.
- **BCD to Binary Conversion Algorithm (Nile Exam Exercise IV, Q2):**
  - Given BCD $1001\ 0001\ 0100_{\text{BCD}}$:
    - Decode nibbles: $1001 = 9$, $0001 = 1$, $0100 = 4 \implies 914_{10}$.
    - Convert decimal $914$ to binary by successive division: $914_{10} = 1110010010_2$.
- **Other Decimal Codes:**
  - $8, 4, -2, -1$ code.
  - $2, 4, 2, 1$ code.
  - **Excess-3 Code:** Non-weighted, self-complementing code formed by adding $3$ ($0011_2$) to each decimal digit's binary equivalent (e.g. $0 \to 0011$, $6 \to 1001$).
  - **Self-Complementing Property:** 9's complement of a decimal digit is directly obtained by inverting all bits of its code word.

---

## 2. Gray Code (Reflected Binary / Unit Distance Code)
- **Concept:** Unweighted, non-arithmetic cyclic code where consecutive numbers differ by **only ONE bit**.
- **Application:** Shaft position encoders, analog-to-digital converters, Karnaugh map adjacency, preventing race conditions.
- **Binary to Gray Conversion Algorithm (Nile Exam Exercise IV, Q1a):**
  - $G_{n-1} = B_{n-1}$ (MSB unchanged).
  - For $i = n-2$ down to $0$: $G_i = B_{i+1} \oplus B_i$.
  - Example: Decimal $21 \implies$ Binary $10101_2$:
    - $G_4 = 1$
    - $G_3 = 1 \oplus 0 = 1$
    - $G_2 = 0 \oplus 1 = 1$
    - $G_1 = 1 \oplus 0 = 1$
    - $G_0 = 0 \oplus 1 = 1$
    - Result $= 11111_{\text{Gray}}$.
- **Gray to Binary Conversion Algorithm (Nile Exam Exercise IV, Q1b):**
  - $B_{n-1} = G_{n-1}$ (MSB unchanged).
  - For $i = n-2$ down to $0$: $B_i = B_{i+1} \oplus G_i$.
  - Example: Gray $11101_{\text{Gray}}$:
    - $B_4 = 1$
    - $B_3 = 1 \oplus 1 = 0$
    - $B_2 = 0 \oplus 1 = 1$
    - $B_1 = 1 \oplus 0 = 1$
    - $B_0 = 1 \oplus 1 = 0$
    - Result $= 10110_2 = 22_{10}$.

---

## 3. Alphanumeric & Error-Detection Codes (ASCII & Parity)
- **ASCII (American Standard Code for Information Interchange):**
  - 7-bit standard code (often padded to 8 bits / 1 byte).
  - Key ASCII values:
    - Space $= 32_{10} = 00100000_2$.
    - Hyphen / Minus $= 45_{10} = 00101101_2$.
    - Digits '0'-'9' $= 48_{10}$ to $57_{10}$ ($00110000_2$ to $00111001_2$).
    - Uppercase 'A'-'Z' $= 65_{10}$ to $90_{10}$ ($01000001_2$ to $01011010_2$).
    - Lowercase 'a'-'z' $= 97_{10}$ to $122_{10}$ ($01100001_2$ to $01111010_2$).
- **Nile Final Exam Exercise III (20 marks):**
  - Decoding stream: `01000011 01101111 01100100 01100101 01100100 00100000 00101101 00100000 00110000 00110010 00110001 00110001`
  - Values: 67 ('C'), 111 ('o'), 100 ('d'), 101 ('e'), 100 ('d'), 32 (' '), 45 ('-'), 32 (' '), 48 ('0'), 50 ('2'), 49 ('1'), 49 ('1').
  - Decoded Text: `"Coded - 0211"`.
- **Parity Bit Error Detection:**
  - Even Parity: Parity bit set so total count of 1s (including parity bit) is **even**.
  - Odd Parity: Parity bit set so total count of 1s (including parity bit) is **odd**.
  - Critical Limitation: Parity can detect single-bit errors (or any odd number of errors), but **cannot detect even numbers of bit errors** (e.g. 2 flipped bits maintain the same parity).
