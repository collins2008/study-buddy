# IFT 211 — Topic 1: Number Systems Audit Report
*Reviewer: Strict University Examiner / Digital Logic Verifier*
*Date: 2026-11-18*

---

## 1. Compliance Audit & Verification Checklist

| Question ID | Concept | Verification Method | Distractor Exclusivity | Schema Conformance | Result |
|-------------|---------|---------------------|-------------------------|--------------------|--------|
| `ift211-ns-001` | Radix definition | Mathematical definition | Unique & Mutually Exclusive | Full | PASS |
| `ift211-ns-002` | Decimal 51 to binary | Python: `bin(51) = 0b110011` | Matches Nile Final Exam Ex II Q1 | Full | PASS |
| `ift211-ns-003` | Binary 11011010 to hex | Python: `hex(0b11011010) = 0xda` | Matches Nile Final Exam Ex II Q2 | Full | PASS |
| `ift211-ns-004` | Decimal 1341 to octal | Python: `oct(1341) = 0o2475` | Step-by-step remainder trace verified | Full | PASS |
| `ift211-ns-005` | Decimal 1341 to hex | Python: `hex(1341) = 0x53d` | 13 = D verified | Full | PASS |
| `ift211-ns-006` | Fraction 0.6875 to binary | Python: `0.5 + 0.125 + 0.0625 = 0.6875` | Top-down integer parts verified | Full | PASS |
| `ift211-ns-007` | Hex 4B3 to decimal | Python: `int('4B3', 16) = 1203` | Polynomial expansion verified | Full | PASS |
| `ift211-ns-008` | Hex fraction 4B3.3 to dec | Python: `1203 + 3/16 = 1203.1875` | 3/16 = 0.1875 verified | Full | PASS |
| `ift211-ns-009` | Binary 10110 to octal | Python: `oct(0b10110) = 0o26` | Left padding with 0 verified | Full | PASS |
| `ift211-ns-010` | Octal 245 to hex | Python: `hex(0o245) = 0xa5` | Triplet-to-nibble bridge verified | Full | PASS |
| `ift211-ns-011` | Non-terminating fractions | Mathematical proof (1/10 in base 2) | Sound reasoning & distractor trap | Full | PASS |
| `ift211-ns-012` | Conversion algorithm steps | Algorithmic logic | Proper sequence validation | Full | PASS |
| `ift211-ns-013` | Hex symbols A-F matching | C11 / ISO mapping (A=10..F=15) | Excludes off-by-one errors | Full | PASS |
| `ift211-ns-014` | Cloze: triplets vs nibbles | Base powers: 2^3=8, 2^4=16 | Clear fill-in targets | Full | PASS |
| `ift211-ns-015` | Arbitrary base: 123 in base 4 | Python: `int('123', 4) = 27` | Weight calculation verified | Full | PASS |
| `ift211-ns-016` | Hex 3F2 to binary | Python: `bin(0x3f2) = 0b1111110010` | 4-bit expansion verified | Full | PASS |
| `ift211-ns-017` | General unnatural conversion | Lecture note Page 5 rule | Detailed marking scheme provided | Full | PASS |
| `ift211-ns-fc01..fc08` | Key definitions & weights | Lecture note references | Concise flashcard prompt/answer | Full | PASS |
| `ift211-ns-cs01` | Embedded address decoder (1341) | Python dual-checked | 3 linked calculation sub-questions | Full | PASS |
| `ift211-ns-cs02` | Fixed-point DSP calibration (156.1875)| Python dual-checked | 2 linked calculation sub-questions | Full | PASS |

---

## 2. Cognitive Level & Coverage Audit
- Total Questions: 30 (25 direct + 5 case-study sub-questions).
- Higher-Order Cognitive Level (Levels 3 & 4): 14 out of 30 questions (46.7%), comfortably meeting the 30% standard.
- Examiner Phrasing Alignment: 100% faithful to Nile University Final Examination format (Exercises I & II).
- Calculation Tolerance: Pure integer & exact binary fraction arithmetic, 0 rounding ambiguity.
