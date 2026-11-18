# Exhaustive Topic Inventory: IFT 211 Topic 7
**Topic**: Karnaugh Maps (2, 3, 4 Variables) (`karnaugh_maps.json`)
**Course**: IFT 211 — Digital Logic and Design (Nile University of Nigeria)
**Sources**:
- `Digital Logic Lecture Note (1).pdf`, Pages 36–45
- Nile University 2024/2025 Final Examination Syllabus
- Department of Computer Science Lecturer Notebook & Course Outline

---

## 1. Core Principles of Karnaugh Maps
1. **Definition & Purpose**:
   - Karnaugh Map (Veitch diagram or K-map): A graphical, two-dimensional geometric representation of a Boolean truth table where each cell represents a distinct minterm.
   - Purpose: Minimizes Boolean algebraic expressions into minimal Sum-of-Products (SOP) or minimal Product-of-Sums (POS) without complex algebraic factoring.
2. **Gray Code Coordinate Ordering**:
   - Rows and columns are sequenced in Gray code order: `00, 01, 11, 10` (NOT standard binary `00, 01, 10, 11`).
   - Fundamental Rule: Two adjacent cells differ by exactly one binary variable (Hamming distance = 1).
3. **Wrap-Around Adjacency (Toroidal Surface)**:
   - The top edge is contiguous with the bottom edge; the left edge is contiguous with the right edge.
   - Four Corners: In a 4-variable map, cells $m_0 (0000), m_2 (0010), m_8 (1000), m_{10} (1010)$ are adjacent and combine into a single quad: $B'D'$.
4. **Grouping Rules**:
   - Group sizes must be powers of 2: $1, 2, 4, 8, 16$.
   - Groups must be rectangular or square (never diagonal, L-shaped, or irregular).
   - In a 4-variable K-map:
     - Group of 1 cell covers a 4-literal product term.
     - Group of 2 cells covers a 3-literal product term (1 variable eliminated).
     - Group of 4 cells covers a 2-literal product term (2 variables eliminated).
     - Group of 8 cells covers a 1-literal product term (3 variables eliminated).
     - Group of 16 cells equals logic 1 (all variables eliminated).
   - Groups should be as large as possible, with the fewest total groups covering all 1s.

---

## 2. Implicant Terminology
1. **Implicant**: Any single minterm or valid rectangular group of minterms that implies $F$ ($P \le F$).
2. **Prime Implicant (PI)**: A group of minterms that cannot be combined with any adjacent group to form a larger group of power-of-2 size (i.e., minimal literals).
3. **Essential Prime Implicant (EPI)**: A prime implicant that covers at least one '1' that is not covered by any other prime implicant. Every EPI MUST be included in the minimal sum of products.
4. **Redundant / Non-Essential Implicant**: A prime implicant whose covered 1s are already completely covered by other essential prime implicants. Must be discarded to prevent gate waste.

---

## 3. Product of Sums (POS) & Don't Care Minimization
1. **POS Simplification via K-Maps**:
   - Group adjacent 0s on the map to find the minimal SOP for $F'$.
   - Apply De Morgan's Law: $F = (F')'$ to transform product terms into sum terms, yielding minimal POS.
2. **Don't-Care Conditions (X or d)**:
   - Cells corresponding to invalid, unreachable input states (e.g., BCD codes $1010$ to $1111$).
   - Strategic Rule: Include an $X$ in a group only if it enlarges the group (reducing literal count); treat $X$ as 0 if it does not help enlarge an existing group. Never create a group consisting solely of $X$s.
3. **Quine-McCluskey (Tabulation Method)**:
   - Algorithmic, deterministic tabular method for $\ge 5$ variables, finding prime implicants systematically and utilizing a prime implicant coverage chart.

---

## 4. Worked Examples from Lecturer Note
1. **Majority Function (3 variables)**:
   - $M(a, b, c) = \Sigma m(3, 5, 6, 7) \implies M = ab + bc + ac$.
2. **Four Corners Quad**:
   - $\Sigma m(0, 2, 8, 10) \implies B'D'$.
3. **BCD Prime Number Detector with Don't Cares**:
   - Inputs $0$ to $9$; primes are $2, 3, 5, 7 \implies m_2, m_3, m_5, m_7$.
   - Don't cares: $d(10, 11, 12, 13, 14, 15)$.
   - Grouping $m_2, m_3$ with $d_{10}, d_{11} \implies B'C$.
   - Grouping $m_5, m_7$ with $d_{13}, d_{15} \implies BD$.
   - Minimal expression: $F = B'C + BD$.
