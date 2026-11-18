# IFT 211 — Topic 5: Logic Gates & Universal Implementations Inventory
*Source: Digital Logic Lecture Notes (A.F. Kana), Pages 16–22 & Lecturer Notebook Focus*

---

## 1. Primary Gates vs Universal Gates (Lecturer Emphasis)
- **Primary Gates:** **AND, OR, NOT**.
  - Fundamental building blocks of Boolean algebra.
  - Non-universal: cannot individually synthesize all other logic functions without combining.
- **Universal Gates:** **NAND, NOR**.
  - Definition: Any Boolean function (and therefore any digital computer) can be constructed exclusively using only NAND gates or only NOR gates.
  - Cost/Manufacturing advantage: Integrated circuit fabrication is simpler, cheaper, and faster when composed of a single repeating gate topology (especially CMOS NAND/NOR).

---

## 2. Gate Symbols, Truth Tables & Boolean Expressions
- **AND Gate:** $F = A \cdot B$ (1 iff all inputs are 1).
- **OR Gate:** $F = A + B$ (1 if any input is 1).
- **NOT Gate (Inverter):** $F = A'$ (Inverts state).
- **NAND Gate:** $F = (A \cdot B)' = A' + B'$ (0 iff all inputs are 1).
- **NOR Gate:** $F = (A + B)' = A' \cdot B'$ (1 iff all inputs are 0).
- **XOR Gate (Exclusive-OR):** $F = A \oplus B = A' B + A B'$ (1 when inputs are unequal; odd parity generator/detector).
- **XNOR Gate (Equivalence):** $F = (A \oplus B)' = A B + A' B'$ (1 when inputs are identical; equality comparator).

---

## 3. Universal Gate Synthesis (Constructing Primary Gates)

### A. Implementing with NAND Gates Only:
1. **NOT Gate:** Tie inputs together: $A \text{ NAND } A = (A \cdot A)' = A'$. (Requires **1 NAND** gate).
2. **AND Gate:** NAND followed by an inverter NAND: $((A \cdot B)' \text{ NAND } (A \cdot B)') = ((AB)')' = AB$. (Requires **2 NAND** gates).
3. **OR Gate:** Invert each input with a NAND, then pass to a third NAND: $(A' \text{ NAND } B') = (A' \cdot B')' = (A')' + (B')' = A + B$ (by De Morgan). (Requires **3 NAND** gates).
4. **NOR Gate:** OR gate followed by an inverter NAND. (Requires **4 NAND** gates).
5. **XOR Gate:** Requires **4 NAND** gates: $A \oplus B = (A(AB)')' \text{ NAND } (B(AB)')'$.

### B. Implementing with NOR Gates Only:
1. **NOT Gate:** Tie inputs together: $A \text{ NOR } A = (A + A)' = A'$. (Requires **1 NOR** gate).
2. **OR Gate:** NOR followed by an inverter NOR: $((A + B)' \text{ NOR } (A + B)') = ((A+B)')' = A + B$. (Requires **2 NOR** gates).
3. **AND Gate:** Invert each input with a NOR, then pass to a third NOR: $(A' \text{ NOR } B') = (A' + B')' = (A')' \cdot (B')' = A \cdot B$ (by De Morgan). (Requires **3 NOR** gates).
4. **NAND Gate:** AND gate followed by an inverter NOR. (Requires **4 NOR** gates).

---

## 4. Digital IC Logic Families & Characteristics
- **TTL (Transistor-Transistor Logic):** 7400 series standard; high current drive, medium speed, 5V supply.
- **CMOS (Complementary MOS):** Extremely low power dissipation, wide voltage range, high noise margin; standard for modern microprocessors.
- **ECL (Emitter-Coupled Logic):** Fastest switching speeds (avoids transistor saturation); high power consumption.
- **Fan-in:** Maximum number of digital input signals a single gate can accept (typically 1 to 8).
- **Fan-out:** Maximum number of standard logic gate inputs that can be connected to a gate output without signal voltage degradation.
