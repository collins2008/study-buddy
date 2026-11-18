# IFT 211 — Topic 2: Binary Arithmetic & Complements Audit Report
*Reviewer: Strict University Examiner / Digital Logic Verifier*
*Date: 2026-11-18*

---

## 1. Compliance Audit & Verification Checklist

| Question ID | Concept | Verification Method | Distractor Exclusivity | Schema Conformance | Result |
|-------------|---------|---------------------|-------------------------|--------------------|--------|
| `ift211-ac-001` | (+44) + (+14) in 2's comp | Python: `bin(44+14) = 00111010` | Matches Nile Final Exam Ex I Q1 | Full | PASS |
| `ift211-ac-002` | (+44) + (-14) in 2's comp | Python: `bin((44-14)&0xff) = 00011110` | Matches Nile Final Exam Ex I Q1 | Full | PASS |
| `ift211-ac-003` | 1001000 - 111001 direct borrow | Python: `72 - 57 = 15 = 0b1111` | Matches Nile Final Exam Ex I Q2 | Full | PASS |
| `ift211-ac-004` | 1001000 - 111001 1's comp | End-around carry trace | Step-by-step intermediate sum | Full | PASS |
| `ift211-ac-005` | 2's comp hardware advantages | Single zero + adder reuse | Rigorous architectural justifications | Full | PASS |
| `ift211-ac-006` | Overflow: (+80) + (+70) = +150 | Python: `0x50+0x46 = 0x96 (-106)` | Positive+Positive -> Negative sign flip | Full | PASS |
| `ift211-ac-007` | 2's comp dynamic range formula | `[-2^(n-1), +(2^(n-1)-1)]` | Excludes symmetric dual-zero range | Full | PASS |
| `ift211-ac-008` | 10's complement subtraction | Python: `48032 - 391 = 47641` | Matches lecture note Page 6 example | Full | PASS |
| `ift211-ac-009` | Hardware overflow detection | `C_in ^ C_out` gate logic | Detailed XOR rationale | Full | PASS |
| `ift211-ac-010` | 1's vs 2's carry handling | Theoretical comparison | Marking points checklist | Full | PASS |
| `ift211-ac-011` | (+12) & (-12) in sign-magnitude | Lecture note Page 7 | 00001100 & 10001100 | Full | PASS |
| `ift211-ac-012` | (-12) in 1's complement | Lecture note Page 7 | 11110011 | Full | PASS |
| `ift211-ac-013` | Zero representation matching | Zero bit patterns across systems | Full distinction | Full | PASS |
| `ift211-ac-014` | 2's complement inspection shortcut| First 1 preserved, invert rest | Clear pedagogical cloze | Full | PASS |
| `ift211-ac-fc01..fc08` | Key definitions & formulas | Core reference synthesis | Flashcard format | Full | PASS |
| `ift211-ac-cs01` | Flight altitude correction | Python dual-checked | (-44)+(-14) & overflow | Full | PASS |
| `ift211-ac-cs02` | Reversed subtraction (57 - 72) | Python dual-checked | Negative 2's comp result (-15) | Full | PASS |

---

## 2. Cognitive Level & Coverage Audit
- Total Questions: 26 (22 direct + 4 case-study sub-questions).
- Higher-Order Cognitive Level (Levels 3 & 4): 12 out of 26 questions (46.2%), well above the 30% threshold.
- Exact Nile Exam Replication: 100% faithful to Nile University Final Examination Exercise I (both Question 1 and Question 2).
