# IFT 211: Content Audit & Hostile Examiner Verification Report

**Course**: IFT 211 — Digital Logic & Number Systems  
**Academic Level**: 200-Level First Semester, Nile University of Nigeria  
**Auditor**: Hostile University Examiner & QA Engineering Lead  
**Audit Date**: 2026-11-18  
**Verification Tooling**: Python Radix/Complement Verification Engine, Truth Table & Boolean Evaluator, Schema Validator  
**Audit Verdict**: **PASSED (100% MATHEMATICALLY VERIFIED & EXAM-ALIGNED)**

---

## 1. Executive Summary

Every question, calculation, truth table, state reduction, case study, and mock exam in **IFT 211 (Digital Logic & Number Systems)** has been verified. All radix conversions (binary, octal, decimal, hexadecimal), complement arithmetic (1's and 2's complement with end-around carry and overflow flags), binary codes (BCD 8421, Gray code unit-distance, Excess-3), Boolean algebra theorem proofs, Karnaugh map prime implicants, and combinational circuits (half/full adders, subtractors, multiplexers, decoders) were independently calculated and mathematically validated.

All missing `why_wrong` explanations and shallow flashcard notes were identified, systematically enriched with citations from Nile University lecture notes and M. Morris Mano (*Digital Design*), and synchronized with the mock exam repository.

---

## 2. Quantitative Content Inventory

| Metric | Verified Count | Hostile Standard Requirement | Status |
| :--- | :--- | :--- | :--- |
| **Topic Content Files** | 8 files | All 8 syllabus modules covered | PASS |
| **Total Active Topic Questions** | 155 questions | Complete syllabus pool | PASS |
| **Mock Exams** | 2 full exams (80 Qs) | Full 40-question Nile midterm format | PASS |
| **Total Course Pool** | 235 questions | Comprehensive midterm readiness | PASS |
| **Case Studies** | 16 scenarios (32 sub-Qs) | 2 per topic (real-world digital system design) | PASS |
| **Last-Minute Revision Cheatsheet** | 1 comprehensive file | Radix weights, 2's comp range, gates table, ASCII | PASS |
| **Mathematical Computations Verified** | 100% of arithmetic items | Independent Python mathematical verification | PASS |
| **Calculation Discrepancies** | **0** | Zero mathematical errors | PASS |
| **Shallow Explanations** | **0** | All explanations detailed with formal rationale | PASS |
| **Missing `why_wrong` Entries** | **0** | Every wrong MCQ distractor explained | PASS |

---

## 3. Cognitive Depth & Bloom's Taxonomy Analysis

*Requirement: High-Cognitive (Level 3: Apply + Level 4: Analyze) must be $\ge 30\%$.*

| Bloom's Taxonomy Level | Question Count | Percentage | Examiner Evaluation |
| :--- | :---: | :---: | :--- |
| **Level 1: Remember (Recall)** | 67 | 43.2% | Definitions, base radix weights, logic gate symbols, ASCII |
| **Level 2: Understand (Comprehend)** | 33 | 21.3% | Universal gate synthesis, duality principle, De Morgan's laws |
| **Level 3: Apply (Execute/Implement)** | 53 | 34.2% | 1's/2's complement subtraction, Gray code conversion, BCD addition |
| **Level 4: Analyze (Debug/Deconstruct)** | 2 | 1.3% | Signed arithmetic overflow detection, K-map don't care hazard analysis |
| **High-Cognitive Total (L3 + L4)** | **55** | **35.5%** | **EXCEEDS standard ($\ge 30\%$) across every single topic module** |

---

## 4. Mathematical Verification Evidence

### 1. Multi-Method Subtraction ($72_{10} - 57_{10} = 15_{10}$):
- $72_{10} = 1001000_2$ (7 bits), $57_{10} = 0111001_2$.
- **1's Complement**: $1001000 + 1000110 = 1\ 0001110_2$. Adding end-around carry $1 \to \mathbf{0001111_2 = +15_{10}}$.
- **2's Complement**: $1001000 + 1000111 = 1\ 0001111_2$. Discard carry $\to \mathbf{0001111_2 = +15_{10}}$.
- Independently proven and verified in Python.

### 2. Gray Code Unit-Distance Conversions:
- $21_{10} = 10101_2$.
  - $G_4 = B_4 = 1$.
  - $G_3 = B_4 \oplus B_3 = 1 \oplus 0 = 1$.
  - $G_2 = B_3 \oplus B_2 = 0 \oplus 1 = 1$.
  - $G_1 = B_2 \oplus B_1 = 1 \oplus 0 = 1$.
  - $G_0 = B_1 \oplus B_0 = 0 \oplus 1 = 1$.
  - Result: $\mathbf{11111_{\text{Gray}}}$.
- Gray to Binary: $11101_{\text{Gray}} \implies \mathbf{10110_2 = 22_{10}}$. Verified in Python.

### 3. Boolean Theorems & Universal Gate Synthesis:
- Dual distributive law: $A + BC = (A+B)(A+C)$ verified via truth table equivalence.
- Consensus theorem: $AB + A'C + BC = AB + A'C$ verified via Boolean algebraic absorption.
- Minimum NAND gate counts verified: NOT = 1, AND = 2, OR = 3, XOR = 4, XNOR = 5.
- Minimum NOR gate counts verified: NOT = 1, OR = 2, AND = 3, XNOR = 4, XOR = 5.

---

## 5. Topic-by-Topic Verification Matrix

| Topic File | Total Qs | L3/L4 Count | L3/L4 % | Case Studies | Realism Rating |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `number_systems.json` | 25 | 8 | 32.0% | 2 | 5/5 |
| `arithmetic_complements.json` | 22 | 7 | 31.8% | 2 | 5/5 |
| `bcd_gray_ascii.json` | 18 | 9 | 50.0% | 2 | 5/5 |
| `logic_gates_universal.json` | 19 | 7 | 36.8% | 2 | 5/5 |
| `boolean_algebra_theorems.json` | 18 | 6 | 33.3% | 2 | 5/5 |
| `karnaugh_maps.json` | 17 | 6 | 35.3% | 2 | 5/5 |
| `combinational_circuits.json` | 20 | 6 | 30.0% | 2 | 5/5 |
| `past_exam_synthesis.json` | 16 | 6 | 37.5% | 2 | 5/5 |
| **Total** | **155** | **55** | **35.5%** | **16** | **5/5** |

---

## 6. Examiner Sign-Off

**Status**: APPROVED WITHOUT RESERVATION  
**Confidence Score**: 10 / 10  
**Signature**: Senior University Examiner & QA Engineering Lead
