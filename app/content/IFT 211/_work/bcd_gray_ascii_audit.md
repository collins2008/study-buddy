# IFT 211 — Topic 3: BCD, Gray Code & ASCII Encoding Audit Report
*Reviewer: Strict University Examiner / Digital Logic Verifier*
*Date: 2026-11-18*

---

## 1. Compliance Audit & Verification Checklist

| Question ID | Concept | Verification Method | Distractor Exclusivity | Schema Conformance | Result |
|-------------|---------|---------------------|-------------------------|--------------------|--------|
| `ift211-cd-001` | Decimal 21 to Gray code | Python: `bin(21)=10101 -> gray=11111` | Matches Nile Final Exam Ex IV Q1a | Full | PASS |
| `ift211-cd-002` | Gray 11101 to binary | Python: `gray(11101) -> bin(10110)=22` | Matches Nile Final Exam Ex IV Q1b | Full | PASS |
| `ift211-cd-003` | BCD 1001 0001 0100 to binary | Python: `914 -> 1110010010_2` | Matches Nile Final Exam Ex IV Q2 | Full | PASS |
| `ift211-cd-004` | ASCII stream decoding | Python: byte-by-byte decode | Matches Nile Final Exam Ex III ("Coded - 0211") | Full | PASS |
| `ift211-cd-005` | Invalid 8421 BCD states | 1010 to 1111 definition | Unambiguous distinction | Full | PASS |
| `ift211-cd-006` | Binary coding vs conversion | Decimal 13 = 1101 vs 0001 0011 | Lecture note Page 12 rule | Full | PASS |
| `ift211-cd-007` | Excess-3 for digit 6 | Python: `6 + 3 = 9 = 1001_2` | Self-complementing check | Full | PASS |
| `ift211-cd-008` | Shaft encoder Gray code advantage | Unit distance eliminates race glitches | Rigorous electromechanical analysis | Full | PASS |
| `ift211-cd-009` | Even parity bit for 1 0 1 | Total 1s must be even -> P=0 | Parity logic | Full | PASS |
| `ift211-cd-010` | 2-bit error parity limitation | Odd vs even error detection proof | Mathematical certainty | Full | PASS |
| `ift211-cd-fc01..fc08` | Core definitions & formulas | Lecture note & exam synthesis | Flashcard format | Full | PASS |
| `ift211-cd-cs01` | Industrial shaft encoder 7->8 | Python: Gray 7=0100, 8=1100 | Verified single-bit flip | Full | PASS |
| `ift211-cd-cs02` | IoT telemetry ASCII + parity | Python: 'T25C' + P=1 check | Real-world serial protocol | Full | PASS |

---

## 2. Cognitive Level & Coverage Audit
- Total Questions: 22 (18 direct + 4 case-study sub-questions).
- Higher-Order Cognitive Level (Levels 3 & 4): 9 out of 22 questions (40.9%), meeting the >= 30% mandate.
- Exact Nile Exam Replication: 100% faithful to Nile University Final Examination Exercises III and IV.
