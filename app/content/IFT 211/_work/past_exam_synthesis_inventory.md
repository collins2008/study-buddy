# Exhaustive Topic Inventory: IFT 211 Topic 8
**Topic**: Past Exam Synthesis & Multi-Topic Problem Solving (`past_exam_synthesis.json`)
**Course**: IFT 211 — Digital Logic and Design (Nile University of Nigeria)
**Sources**:
- Nile University 2024/2025 Final Examination Paper (Department of Computer Science), Exercises I through VI
- Lecturer Review Hints & Exam Style Guide (`STYLE_GUIDE.md`)

---

## 1. Exam Problem Set & Marking Structure (60 Marks Total)
1. **Exercise I: Signed Binary Arithmetic & Subtraction Methods (20 Marks)**
   - Problem 1(a): Perform $(+44) + (+14)$ in 8-bit 2's complement representation.
     - $(+44)_{10} = 00101100_2$
     - $(+14)_{10} = 00001110_2$
     - Sum = $00111010_2 = (+58)_{10}$. No overflow.
   - Problem 1(b): Perform $(+44) + (-14)$ in 8-bit 2's complement representation.
     - $(+44)_{10} = 00101100_2$
     - $(-14)_{10}$: $+14 = 00001110_2 \to \text{1's comp } 11110001 \to \text{2's comp } 11110010_2$.
     - Addition: $00101100 + 11110010 = 1\ 00011110_2$. End carry is discarded in 2's complement. Result = $00011110_2 = (+30)_{10}$.
   - Problem 1(c): Subtraction $1001000_2 - 111001_2$ ($72_{10} - 57_{10} = 15_{10} = 001111_2$):
     - Method 1: Direct binary subtraction with borrowing.
     - Method 2: 1's complement subtraction with end-around carry ($1001000 + 000110 = 1001110 \to 001110 + 1 = 001111_2$).
     - Method 3: 2's complement subtraction with discarded end carry ($1001000 + 000111 = 1\ 0001111 \to 001111_2$).

2. **Exercise II: Radix Conversions (10 Marks)**
   - Problem 2(a): Decimal $51_{10}$ to binary.
     - $51 / 2 = 25$ rem $1$; $25/2 = 12$ rem $1$; $12/2 = 6$ rem $0$; $6/2 = 3$ rem $0$; $3/2 = 1$ rem $1$; $1/2 = 0$ rem $1$.
     - Result = $110011_2$ (or 8-bit $00110011_2$).
   - Problem 2(b): Binary $11011010_2$ to Hexadecimal.
     - Group into 4-bit nibbles: `1101` and `1010`.
     - `1101` = $13_{10} = \text{D}_{16}$.
     - `1010` = $10_{10} = \text{A}_{16}$.
     - Result = $\text{DA}_{16}$.

3. **Exercise III: ASCII Stream Decoding (10 Marks)**
   - 12-byte stream decoding:
     - `01000011` (67) = `'C'`
     - `01101111` (111) = `'o'`
     - `01100100` (100) = `'d'`
     - `01100101` (101) = `'e'`
     - `01100100` (100) = `'d'`
     - `00100000` (32) = `' '`
     - `00101101` (45) = `'-'`
     - `00100000` (32) = `' '`
     - `00110000` (48) = `'0'`
     - `00110010` (50) = `'2'`
     - `00110001` (49) = `'1'`
     - `00110001` (49) = `'1'`
     - Hidden Text: `"Coded - 0211"`.

4. **Exercise IV: Non-Weighted Binary Encodings (10 Marks)**
   - Problem 4(a): Decimal $21_{10}$ to Gray Code.
     - $21_{10} = 10101_2$.
     - Gray conversion: $G_4=B_4=1$; $G_3 = B_4 \oplus B_3 = 1\oplus 0 = 1$; $G_2 = B_3 \oplus B_2 = 0\oplus 1 = 1$; $G_1 = B_2 \oplus B_1 = 1\oplus 0 = 1$; $G_0 = B_1 \oplus B_0 = 0\oplus 1 = 1$.
     - Result = $11111_{\text{Gray}}$.
   - Problem 4(b): Gray Code $11101_{\text{Gray}}$ to Binary.
     - $B_4 = G_4 = 1$.
     - $B_3 = B_4 \oplus G_3 = 1 \oplus 1 = 0$.
     - $B_2 = B_3 \oplus G_2 = 0 \oplus 1 = 1$.
     - $B_1 = B_2 \oplus G_1 = 1 \oplus 0 = 1$.
     - $B_0 = B_1 \oplus G_0 = 1 \oplus 1 = 0$.
     - Binary Result = $10110_2$ (Decimal $22_{10}$).
   - Problem 4(c): BCD $1001\ 0001\ 0100_{\text{BCD}}$ to Equivalent Binary.
     - Nibble 1: $1001_2 = 9_{10}$.
     - Nibble 2: $0001_2 = 1_{10}$.
     - Nibble 3: $0100_2 = 4_{10}$.
     - Decimal value = $914_{10}$.
     - Convert $914_{10}$ to pure binary: $914 = 512 + 256 + 128 + 16 + 2 = 1110010010_2$.

5. **Exercise V & VI: Logic Circuits & Universality (10 Marks)**
   - Problem 5(a): Primary Gates vs Universal Gates classification.
     - Primary: OR, AND, NOT.
     - Universal: NAND, NOR.
   - Problem 5(b): Circuit Node Tracing & Truth Table for $X = (A \oplus B) + B \cdot C'$.
     - Intermediate nodes $R = A \oplus B$, $Q = C'$, $S = B \cdot C'$.
     - Evaluated across all 8 input combinations; active minterms $\Sigma m(2,3,4,5,6)$.
