# IFT 211 — Topic 2: Arithmetic & Complements Inventory
*Source: Digital Logic Lecture Notes (A.F. Kana), Pages 6–10 & Nile Final Examination (Exercise I)*

---

## 1. Core Representations of Signed Numbers

| Property | Sign-Magnitude | 1's Complement (Diminished Radix) | 2's Complement (Radix Complement) | Excess-$K$ |
| :--- | :--- | :--- | :--- | :--- |
| **Sign Bit** | MSB: $0=+$, $1=-$ | MSB: $0=+$, $1=-$ | MSB: $0=+$, $1=-$ | MSB biased (inverted) |
| **Negation Rule** | Invert MSB only | Invert all bits ($0 \leftrightarrow 1$) | Invert all bits, then add $1$ | Subtract bias $K$ |
| **Zero Representations** | Two: $+0$ (`00000000`), $-0$ (`10000000`) | Two: $+0$ (`00000000`), $-0$ (`11111111`) | **One unique zero**: `00000000` | One unique zero: $K$ |
| **Range for $n$ bits** | $[-(2^{n-1}-1), +(2^{n-1}-1)]$ | $[-(2^{n-1}-1), +(2^{n-1}-1)]$ | $[-2^{n-1}, +(2^{n-1}-1)]$ | Arbitrary based on $K$ |
| **8-bit Range** | $[-127, +127]$ | $[-127, +127]$ | **$[-128, +127]$** | e.g. $[-128, +127]$ |
| **Hardware Hardware Addition** | Requires separate subtractor | Requires end-around carry logic | **Standard binary adder works directly** | Bias adjustment needed |

---

## 2. Complement Form Calculations & Formulas
- **Diminished Radix Complement ($r-1$'s complement):** $(r^n - 1) - N$.
  - Decimal (9's complement): Subtract each digit from $9$.
  - Binary (1's complement): Invert each bit ($0 \to 1$, $1 \to 0$).
- **Radix Complement ($r$'s complement):** $r^n - N = \text{Diminished Radix Complement} + 1$.
  - Decimal (10's complement): 9's complement $+ 1$.
  - Binary (2's complement): 1's complement $+ 1$.
  - Shortcut for 2's complement: Starting from LSB, leave all zeros and the first 1 unchanged; invert all subsequent bits to the left.

---

## 3. Subtraction Algorithms (The Three Nile Methods)
For subtracting $Y$ from $X$ ($X - Y$):
1. **Method 1: Direct Binary Subtraction (with Borrowing):**
   - $0 - 0 = 0$
   - $1 - 0 = 1$
   - $1 - 1 = 0$
   - $0 - 1 = 1$ with a borrow of $2$ from the next higher column.
2. **Method 2: 1's Complement Subtraction:**
   - Pad $Y$ to same bit-length as $X$.
   - Form 1's complement of $Y$ (invert all bits).
   - Add $X + Y_{\text{1's comp}}$.
   - If an end carry is produced: add $1$ to the LSB (**End-Around Carry**). The result is positive.
   - If NO end carry: the result is negative; take 1's complement of the sum and prepend a minus sign.
3. **Method 3: 2's Complement Subtraction:**
   - Form 2's complement of $Y$ (invert bits and add 1).
   - Add $X + Y_{\text{2's comp}}$.
   - If an end carry is produced: **discard the carry**. The result is positive.
   - If NO end carry: the result is negative; take 2's complement of the sum and prepend a minus sign.

---

## 4. Past Exam Focus (Nile University Final Exam, Exercise I)
1. **Exercise I, Question 1 (10 marks):**
   - Perform $(+44) + (+14)$ in 8-bit binary using 2's complement form:
     - $+44 = 00101100_2$
     - $+14 = 00001110_2$
     - Sum $= 00101100 + 00001110 = 00111010_2 = +58_{10}$.
   - Perform $(+44) + (-14)$ in 8-bit binary using 2's complement form:
     - $+44 = 00101100_2$
     - $+14 = 00001110_2 \implies -14 = 11110001 + 1 = 11110010_2$.
     - Sum $= 00101100 + 11110010 = 100011110_2$.
     - Discard 9th bit end-carry $\implies 00011110_2 = +30_{10}$ ($44 - 14 = 30$).
2. **Exercise I, Question 2 (10 marks):**
   - Perform $1001000_2 - 111001_2$ ($72_{10} - 57_{10} = 15_{10} = 0001111_2$):
     - Direct borrow method worked step-by-step.
     - 1's complement method with end-around carry: $1001000 + 1000110 = 10001110 \xrightarrow{+1} 0001111_2$.
     - 2's complement method: $1001000 + 1000111 = 10001111 \xrightarrow{\text{discard}} 0001111_2$.

---

## 5. Overflow Rules in 2's Complement
- Overflow occurs **if and only if**:
  1. Adding two positive numbers yields a negative result (MSB = 1).
  2. Adding two negative numbers yields a positive result (MSB = 0).
- Adding numbers of opposite signs **can never produce an overflow**.
- Hardware gate logic: $\text{Overflow} = C_{\text{in}} \oplus C_{\text{out}}$ of the MSB full adder.
