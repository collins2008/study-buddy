# Hostile Pedagogical & Technical Audit: IFT 203 Topic 4
**Topic**: CSS Selectors, Specificity & Typography (`css_selectors_typography.json`)
**Auditor**: Senior University Examiner & Web Architecture Lead

---

## 1. Inventory & Exam Blueprint Coverage
- [x] Three CSS linking methods (Inline, Internal, External `<link>`): Separation of concerns, multi-page maintainability, and HTTP browser caching advantages.
- [x] CSS Specificity 4-tier tuple $(a, b, c, d)$: Inline (1000) > ID (100) > Class/Pseudo-class (10) > Element (1).
- [x] The Cascade & Source Order: Resolving equal-specificity conflicts deterministically via CSS document order.
- [x] Combinators: Descendant (`A B`) vs direct child (`A > B`), adjacent sibling (`+`), general sibling (`~`).
- [x] Selector categories & symbols: `#` (ID), `.` (Class), `,` (Grouping), `>` (Child), `:` (Pseudo-class).
- [x] Specificity hierarchy sequencing from universal `*` (0) to inline styles (1000).
- [x] Relative typography units: Dissecting `rem` (root font-size scaling, accessibility) vs `em` (parent compounding bug).
- [x] Typography best practices: Generic font-family fallbacks (`sans-serif`, `serif`), multi-word quoting, `text-decoration: none`.
- [x] Color models: Hexadecimal, RGB, RGBA with alpha opacity.
- [x] 2 Multi-part Case Studies:
  1. The Specificity War on the Nile Portal: Diagnosing class vs ID conflicts, dissecting why `!important` is a dangerous technical debt anti-pattern, and implementing class-based modular refactoring.
  2. Responsive Accessible Typography: Calculating mathematical font compounding ($16 \times 1.25^3 = 31.25\text{px}$) in nested `em` containers, refactoring to clean `rem` units, and configuring a cross-platform system font stack.

---

## 2. Statistical Breakdown
- Total Main Questions: 16
- Total Case Studies: 2 (4 sub-questions)
- Total Questions: 20
- Difficulty 1: 8 (40.0%)
- Difficulty 2: 2 (10.0%)
- Difficulty 3: 8 (40.0%)
- Difficulty 4: 2 (10.0%)
- **Higher-Order (L3-L4) Ratio**: **50.0%** (Target: $\ge 30\%$) -> **PASSED**
- Distractor Quality: 100% of distractors contain explicit, pedagogical `why_wrong` explanations dissecting cascading and selector misconceptions.

---

## 3. Final Verdict
**APPROVED - ZERO DEFECTS**. Ready for index registration and app consumption.
