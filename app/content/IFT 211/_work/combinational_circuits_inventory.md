# Exhaustive Topic Inventory: IFT 211 Topic 6
**Topic**: Combinational Circuits & Truth Tables (`combinational_circuits.json`)
**Course**: IFT 211 — Digital Logic and Design (Nile University of Nigeria)
**Sources**:
- `Digital Logic Lecture Note (1).pdf`, Pages 26–30, 55–65
- Nile University 2024/2025 Final Examination Paper, Exercise VI (Circuit Node Tracing & Truth Table)
- Department of Computer Science Lecturer Notebook & Course Outline

---

## 1. Core Concepts & Definitions
1. **Combinational Circuit**:
   - Consists of interconnected logic gates whose outputs at any time are determined exclusively and directly by the present combination of input values, without feedback loops, memory elements, or dependence on past states.
   - Contrast with sequential circuits (which contain flip-flops and feedback loops).
2. **Analysis vs. Synthesis**:
   - Analysis: Given a schematic or logic diagram $\to$ trace intermediate nodes $\to$ derive Boolean expressions $\to$ construct complete truth table.
   - Synthesis: Given a word specification or system requirements $\to$ construct truth table $\to$ optimize Boolean expressions (SOP/POS/K-map) $\to$ implement using available gate families.
3. **Don't-Care Conditions (X or -)**:
   - Output states that can never occur in physical operation (e.g. invalid BCD codes 1010–1111, or division by zero where denominator is zero).
   - In circuit design, don't cares are assigned 0 or 1 strategically to minimize gate count and circuit area.
4. **Integration Scales**:
   - SSI (Small Scale Integration): $< 10$ gates per IC chip.
   - MSI (Medium Scale Integration): $10$ to $100$ gates per IC chip.
   - LSI (Large Scale Integration): $100$ to several thousand gates per IC.
   - VLSI (Very Large Scale Integration): $> 1,000$ to millions of gates per IC.

---

## 2. Arithmetic Combinational Circuits
1. **Half Adder**:
   - Adds two 1-bit binary numbers: inputs $A, B$.
   - Outputs: Sum $S = A \oplus B = A'B + AB'$, Carry $C = AB$.
   - Limitation: Cannot accept an incoming carry bit from a previous stage.
2. **Full Adder**:
   - Adds three 1-bit binary inputs: $A, B, C_{\text{in}}$ (or $C_i$).
   - Outputs:
     - Sum: $S = A \oplus B \oplus C_{\text{in}}$
     - Carry-out: $C_{\text{out}} = AB + BC_{\text{in}} + AC_{\text{in}} = AB + C_{\text{in}}(A \oplus B)$
   - Implementation via 2 Half Adders + 1 OR gate:
     - HA1: $S_1 = A \oplus B$, $C_1 = AB$.
     - HA2: $S = S_1 \oplus C_{\text{in}} = A \oplus B \oplus C_{\text{in}}$, $C_2 = S_1 \cdot C_{\text{in}} = (A \oplus B)C_{\text{in}}$.
     - Carry output: $C_{\text{out}} = C_1 + C_2 = AB + (A \oplus B)C_{\text{in}}$. (Can replace final OR with XOR since $C_1$ and $C_2$ can never be simultaneously 1).
3. **Ripple Carry Adder (RCA)**:
   - $N$ full adders cascaded such that $C_{\text{out}}$ of stage $k$ becomes $C_{\text{in}}$ of stage $k+1$.
   - Propagation delay calculation:
     - Each stage introduces 2 gate delays for carry propagation.
     - Total delay for $N$-bit adder = $2(N-1) + 1 = 2N - 1$ gate delays (or $2N$ depending on sum output stage). For 32-bit: $31 \times 2 + 1 = 63$ gate delays.
4. **Half Subtractor**:
   - Subtracts 1-bit subtrahend $Y$ from minuend $X$:
   - Difference $D = X \oplus Y = X'Y + XY'$, Borrow $B = X'Y$.
5. **Full Subtractor**:
   - Minuend $A$, subtrahend $B$, borrow-in $B_{\text{in}}$.
   - Difference $D = A \oplus B \oplus B_{\text{in}}$.
   - Borrow-out $B_{\text{out}} = A'B + B_{\text{in}}(A \oplus B)' = A'B + A'B_{\text{in}} + BB_{\text{in}}$.
6. **Binary Adder-Subtractor Unit**:
   - A ripple carry adder augmented with 2-input XOR gates on each $B_i$ line and controlled by mode signal $M$:
   - If $M=0$: $B_i \oplus 0 = B_i$, $C_{\text{in}}=0 \implies$ Operation is $A + B$.
   - If $M=1$: $B_i \oplus 1 = B_i'$, $C_{\text{in}}=1 \implies$ Operation is $A + B' + 1 = A - B$ (2's complement subtraction).

---

## 3. Medium Scale Integration (MSI) Circuits
1. **Decoders**:
   - $n$-to-$2^n$ line decoder: converts an $n$-bit binary input into $2^n$ unique output lines (exactly one active).
   - Active-high vs active-low outputs (NAND-based decoders usually active-low with inverted outputs).
   - Synthesis: Any arbitrary Boolean function can be implemented using an $n$-to-$2^n$ decoder and an external OR gate (sum of minterms).
2. **Encoders**:
   - $2^n$-to-$n$ line encoder: performs the inverse of a decoder, translating an active line into an $n$-bit binary code.
   - Limitation: Undefined output if zero or multiple inputs are simultaneously active.
3. **Priority Encoders**:
   - Assigns priority rank to input lines (e.g. $I_3 > I_2 > I_1 > I_0$).
   - If multiple lines are high, the output reflects the highest-order active input, utilizing don't cares ($X$) for lower lines.
   - Valid output bit $V$: 1 when at least one input is active; 0 when all inputs are 0.
4. **Multiplexers (MUX / Data Selectors)**:
   - $2^n$ data inputs, $n$ select (address) lines, 1 single output.
   - Equation for 4-to-1 MUX: $Y = S_1'S_0'I_0 + S_1'S_0I_1 + S_1S_0'I_2 + S_1S_0I_3$.
   - Functional completeness: Any $n$-variable Boolean function can be realized using a $2^{n-1}$-to-1 MUX by connecting $n-1$ variables to select lines and feeding $0, 1, V, V'$ to data inputs.
5. **Demultiplexers (DEMUX / Data Distributors)**:
   - 1 data input, $n$ select lines, $2^n$ outputs. Transmits input data to the selected output line while others remain inactive.
   - Identical in structure to an $n$-to-$2^n$ decoder where the enable line functions as the data input.

---

## 4. Past Exam Focus (Nile Final Exam Exercise VI)
- Circuit node tracing for multi-gate circuit:
  - Input variables $A, B, C$.
  - Sub-circuits: $R = A \oplus B$, $S = B \cdot C'$, $X = R + S = (A \oplus B) + (B \cdot C')$.
  - Truth table construction across all 8 input combinations $(000 \dots 111)$.
  - Gate delays and hazard analysis.
