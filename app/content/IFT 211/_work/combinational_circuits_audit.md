# Hostile Pedagogical & Technical Audit: IFT 211 Topic 6
**Topic**: Combinational Circuits & Truth Tables (`combinational_circuits.json`)
**Auditor**: Senior University Examiner & Digital Logic Lead

---

## 1. Inventory & Syllabus Coverage
- [x] Memoryless combinational circuit definition and contrast with sequential circuits
- [x] Half Adder: $S = A \oplus B$, $C = AB$
- [x] Full Adder: derivation from 2 Half Adders and 1 OR gate; majority function for $C_{\text{out}}$
- [x] Ripple Carry Adder: cascading delay calculations ($31 \times 2 + 1 = 63$ gate delays for 32 bits)
- [x] Half Subtractor & Full Subtractor equations ($D = X \oplus Y$, $B = X'Y$)
- [x] Unified Adder-Subtractor using XOR mode control $M$ and 2's complement
- [x] MSI Components: Decoders ($n$-to-$2^n$), Encoders, Priority Encoders, Multiplexers ($2^n$-to-1), Demultiplexers
- [x] Boolean synthesis using MUX and Decoders
- [x] Past Exam Question (Nile Final Exam Exercise VI): Circuit node tracing for $X = (A \oplus B) + B \cdot C'$ across all 8 minterms
- [x] 2 Case Studies: 8-bit ALU Critical Path Delay with Signed Overflow Detection ($V = C_7 \oplus C_8$), and Nile Exam Exercise VI full minterm canonical expansion ($\Sigma m(2,3,4,5,6)$)

---

## 2. Statistical Breakdown
- Total Main Questions: 20
- Total Case Studies: 2 (4 sub-questions)
- Total Questions: 24
- Difficulty 1: 9 (37.5%)
- Difficulty 2: 5 (20.8%)
- Difficulty 3: 8 (33.3%)
- Difficulty 4: 2 (8.3%)
- **Higher-Order (L3-L4) Ratio**: **41.7%** (Target: $\ge 30\%$) -> **PASSED**
- Distractor Quality: 100% of distractors contain explicit `why_wrong` explanations detailing the arithmetic misstep or logical misconception.

---

## 3. Mathematical & Logical Verification
- Adder propagation delay:
  - 32-bit RCA delay: $2(31) + 1 = 63$ gate delays. Verified.
  - 8-bit ALU delay: $1.5\,\text{ns} (\text{XOR}) + 7 \times 2\,\text{ns} + 3\,\text{ns} = 18.5\,\text{ns}$. Verified.
- MUX synthesis: XOR truth table for $A, B \implies [0, 1, 1, 0]$ on $D_0, D_1, D_2, D_3$. Verified.
- Nile Exam Exercise VI:
  - Input $(1, 1, 0) \implies (1 \oplus 1) + (1 \cdot 0') = 0 + 1 = 1$. Verified.
  - Active minterms: $m_2 (010), m_3 (011), m_4 (100), m_5 (101), m_6 (110) \implies \Sigma m(2,3,4,5,6)$. Exactly 5 minterms. Verified.

---

## 4. Final Verdict
**APPROVED - ZERO DEFECTS**. Ready for index registration and app consumption.
