# Hostile Pedagogical & Technical Audit: IFT 211 Topic 8
**Topic**: Past Exam Synthesis & Multi-Topic Problem Solving (`past_exam_synthesis.json`)
**Auditor**: Senior University Examiner & Digital Logic Lead

---

## 1. Inventory & Exam Replication Coverage
- [x] Exercise I(a): 8-bit signed 2's complement addition: $(+44) + (+14) = 00111010_2 = (+58)_{10}$
- [x] Exercise I(a): 8-bit signed 2's complement subtraction: $(+44) + (-14) = 00011110_2 = (+30)_{10}$ (with end carry discarded)
- [x] Exercise I(b): Multi-method binary subtraction $1001000_2 - 111001_2 = 15_{10} = 0001111_2$:
  - 1's complement with end-around carry
  - 2's complement with discarded end carry
- [x] Exercise II: Radix conversion:
  - Decimal $51 \to 00110011_2$
  - Binary $11011010_2 \to \text{DA}_{16}$
- [x] Exercise III: Full 12-byte ASCII stream decoding: `"Coded - 0211"`
- [x] Exercise IV: Non-weighted encodings:
  - Decimal $21 \to 11111_{\text{Gray}}$
  - Gray $11101 \to 10110_2$ ($22_{10}$)
  - BCD $1001\ 0001\ 0100_{\text{BCD}} \to 914_{10} \to 1110010010_2$
- [x] Exercise V & VI: Logic circuit node tracing and gate classifications:
  - Primary gates (OR, AND, NOT) vs. Universal gates (NAND, NOR)
  - Intermediate nodes $R = A \oplus B$, $Q = C'$, $S = B \cdot C'$, $X = R + S$
  - Minimal SOP expansion: $X = A'B + AB' + BC'$
- [x] 2 Case Studies: Exercise I Full Examination Protocol (comparing end-around carry vs discarded carry), and Exercise VI Circuit Node Tracing & K-map verification

---

## 2. Statistical Breakdown
- Total Main Questions: 16
- Total Case Studies: 2 (4 sub-questions)
- Total Questions: 20
- Difficulty 1: 8 (40.0%)
- Difficulty 2: 2 (10.0%)
- Difficulty 3: 9 (45.0%)
- Difficulty 4: 1 (5.0%)
- **Higher-Order (L3-L4) Ratio**: **50.0%** (Target: $\ge 30\%$) -> **PASSED**
- Distractor Quality: 100% of distractors contain explicit `why_wrong` explanations detailing the exact arithmetic trap or conceptual misunderstanding.

---

## 3. Mathematical & Logical Verification
- $(+44) + (+14) = 00101100_2 + 00001110_2 = 00111010_2 = 58_{10}$. Verified.
- $(+44) + (-14) = 00101100_2 + 11110010_2 = 1\ 00011110_2 \to 00011110_2 = 30_{10}$. Verified.
- $1001000_2 - 111001_2 = 72 - 57 = 15 = 1111_2$.
  - 1's complement: $1001000 + 1000110 = 1\ 0001110 \xrightarrow{+1} 0001111_2$. Verified.
  - 2's complement: $1001000 + 1000111 = 1\ 0001111 \to 0001111_2$. Verified.
- $51_{10} = 32 + 16 + 2 + 1 = 00110011_2$. Verified.
- $11011010_2 \to 1101_2 (\text{D}) \cdot 1010_2 (\text{A}) = \text{DA}_{16}$. Verified.
- ASCII bytes $[67, 111, 100, 101, 100, 32, 45, 32, 48, 50, 49, 49] \implies \text{"Coded - 0211"}$. Verified.
- Gray of $21_{10} (10101_2) = 11111_{\text{Gray}}$. Verified.
- Gray $11101_{\text{Gray}} \to 10110_2 = 22_{10}$. Verified.
- BCD $1001\ 0001\ 0100 = 914_{10} = 1110010010_2$. Verified.
- Intermediate nodes for $(0, 1, 1)$: $R = 0 \oplus 1 = 1$; $S = 1 \cdot 1' = 0$; $X = 1 + 0 = 1$. Verified.

---

## 4. Final Verdict
**APPROVED - ZERO DEFECTS**. Ready for index registration and app consumption.
