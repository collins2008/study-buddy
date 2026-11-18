# Hostile Pedagogical & Technical Audit: IFT 211 Topic 7
**Topic**: Karnaugh Maps (2, 3, 4 Variables) (`karnaugh_maps.json`)
**Auditor**: Senior University Examiner & Digital Logic Lead

---

## 1. Inventory & Syllabus Coverage
- [x] Graphical 2D map structure and minterm mapping
- [x] Gray code coordinates (`00, 01, 11, 10`) ensuring Hamming distance of 1
- [x] Wrap-around adjacency and toroidal continuity
- [x] Four-corners grouping ($m_0, m_2, m_8, m_{10} \implies B'D'$)
- [x] Literal reduction rules ($2^k$ cells eliminate $k$ literals)
- [x] Prime Implicants (PI) vs. Essential Prime Implicants (EPI)
- [x] Product of Sums (POS) minimization via grouping 0s and De Morgan's inversion
- [x] Strategic exploitation of Don't-Care conditions ($X$) in BCD arithmetic
- [x] Algorithmic tabular minimization overview (Quine-McCluskey method for $\ge 5$ variables)
- [x] 2 Case Studies: 4-Variable Prime Implicant Analysis ($F = \Sigma m(0,2,5,7,8,10,14,15) \implies B'D' + A'BD + ABC$), and BCD Prime Number Detector with don't-cares ($F = B'C + BD$, demonstrating 2-literal gate input savings)

---

## 2. Statistical Breakdown
- Total Main Questions: 17
- Total Case Studies: 2 (4 sub-questions)
- Total Questions: 21
- Difficulty 1: 8 (38.1%)
- Difficulty 2: 4 (19.0%)
- Difficulty 3: 8 (38.1%)
- Difficulty 4: 1 (4.8%)
- **Higher-Order (L3-L4) Ratio**: **42.9%** (Target: $\ge 30\%$) -> **PASSED**
- Distractor Quality: 100% of distractors contain explicit `why_wrong` explanations detailing the geometric grouping mistake or algebraic misconception.

---

## 3. Mathematical & Geometric Verification
- Gray code coordinates: difference between $01$ and $11$ is 1 bit; difference between $11$ and $10$ is 1 bit; difference between $10$ and $00$ is 1 bit. Verified.
- Four corners grouping:
  - $(A'B'C'D' + A'B'CD' + AB'C'D' + AB'CD') = B'D'(A'C' + A'C + AC' + AC) = B'D'$. Verified.
- Majority function 3-variable:
  - $\Sigma m(3, 5, 6, 7) \implies ab + bc + ac$. Verified.
- BCD Prime Detector with don't-cares:
  - Primes: $2 (0010), 3 (0011), 5 (0101), 7 (0111)$.
  - Don't cares: $10 (1010), 11 (1011), 12 (1100), 13 (1101), 14 (1110), 15 (1111)$.
  - Group 1: $m_2, m_3, d_{10}, d_{11} \implies B'C$.
  - Group 2: $m_5, m_7, d_{13}, d_{15} \implies BD$.
  - Minimal SOP: $B'C + BD$. Verified.

---

## 4. Final Verdict
**APPROVED - ZERO DEFECTS**. Ready for index registration and app consumption.
