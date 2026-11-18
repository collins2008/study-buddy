# IFT 211 — Topic 4: Boolean Algebra & De Morgan's Laws Inventory
*Source: Digital Logic Lecture Notes (A.F. Kana), Pages 23–26*

---

## 1. Postulates of Boolean Algebra
- **Set & Operators:** Defined on $B = \{0, 1\}$ with binary operators $+$ (logical OR) and $\cdot$ (logical AND).
- **Postulate 1 (Closure):** For any $x, y \in B$, $x + y \in B$ and $x \cdot y \in B$.
- **Postulate 2 (Identity Elements):**
  - $0 + A = A$ ($0$ is the additive identity)
  - $1 \cdot A = A$ ($1$ is the multiplicative identity)
- **Postulate 3 (Commutative Law):**
  - $A + B = B + A$
  - $A \cdot B = B \cdot A$
- **Postulate 4 (Distributive Law):**
  - $A \cdot (B + C) = A \cdot B + A \cdot C$ ($\cdot$ distributes over $+$)
  - **$A + (B \cdot C) = (A + B) \cdot (A + C)$** ($+$ distributes over $\cdot$ — unique to Boolean algebra, false in ordinary algebra!)
- **Postulate 5 (Complement):**
  - $A + A' = 1$
  - $A \cdot A' = 0$

---

## 2. Theorems of Boolean Algebra
- **Theorem 1 (Idempotent / Identity Law):**
  - $A + A = A$
  - $A \cdot A = A$
- **Theorem 2 (Dominance / Boundedness Law):**
  - $A + 1 = 1$
  - $A \cdot 0 = 0$
- **Theorem 3 (Involution / Double Negation):**
  - $(A')' = A$
- **Theorem 4 (Associative Law):**
  - $(A + B) + C = A + (B + C)$
  - $(A \cdot B) \cdot C = A \cdot (B \cdot C)$
- **Theorem 5 (De Morgan's Laws):**
  - $(A + B)' = A' \cdot B'$ (The complement of an OR sum is the AND product of the complements)
  - $(A \cdot B)' = A' + B'$ (The complement of an AND product is the OR sum of the complements)
  - Generalized $n$-variable: $(A + B + C + \dots)' = A' \cdot B' \cdot C' \dots$ and $(A \cdot B \cdot C \dots)' = A' + B' + C' \dots$
- **Theorem 6 (Absorption Laws):**
  - $A + A \cdot B = A$
  - $A \cdot (A + B) = A$
- **Consensus Theorem:**
  - $A B + A' C + B C = A B + A' C$
  - Dual: $(A + B)(A' + C)(B + C) = (A + B)(A' + C)$

---

## 3. The Principle of Duality
- **Statement:** Any valid Boolean algebraic relation remains valid if:
  1. All $+$ (OR) operators are replaced with $\cdot$ (AND)
  2. All $\cdot$ (AND) operators are replaced with $+$ (OR)
  3. All $0$s are replaced with $1$s
  4. All $1$s are replaced with $0$s
- **Crucial Rule:** Literal variables and their complements are **NOT** inverted in the dual (e.g., dual of $A + B'$ is $A \cdot B'$).

---

## 4. Algebraic Simplification Examples
- $A B + A B' = A(B + B') = A(1) = A$
- $A + A' B = (A + A')(A + B) = 1 \cdot (A + B) = A + B$
- $(A + B)(A + B') = A + B B' = A + 0 = A$
