# Hostile Pedagogical & Technical Audit: IFT 203 Topic 2
**Topic**: HTML5 Core: Elements, Semantic Tags & Attributes (`html_structure_semantics.json`)
**Auditor**: Senior University Examiner & Web Architecture Lead

---

## 1. Inventory & Exam Blueprint Coverage
- [x] Document Type Declaration (`<!DOCTYPE html>`): Standard HTML5 rendering mode vs quirks mode.
- [x] Void / Empty elements (`<img>`, `<br>`, `<hr>`, `<input>`, `<meta>`, `<link>`) vs container elements.
- [x] Semantic vs presentational text formatting: `<strong>` (importance/a11y) vs `<b>` (visual bold), `<em>` vs `<i>`.
- [x] Block-level vs Inline rendering behavior: `html_render` predicting line breaks, width expansion, and vertical stacking.
- [x] HTML5 Semantic Landmarks: `<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`.
- [x] Standard document hierarchy sequencing: DOCTYPE -> `<html>` -> `<head>` -> `<body>` -> `</html>`.
- [x] Syntax & Validation debugging: Prohibiting duplicate `id` attributes and preserving CSS specificity and JS query stability.
- [x] Global attributes: `id` (unique fingerprint) vs `class` (reusable categories).
- [x] Mobile Viewport configuration: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.
- [x] 2 Multi-part Case Studies:
  1. Accessibility Audit & Refactoring: Converting an unnavigable "div-soup" scholarship announcement into compliant Semantic HTML5 with screen-reader landmark navigation and SEO heading hierarchies.
  2. Mobile Viewport & Whitespace Bug: Diagnosing microscopic mobile canvas rendering and contrasting HTML whitespace collapsing with preformatted `<pre>` and CSS vertical margins.

---

## 2. Statistical Breakdown
- Total Main Questions: 16
- Total Case Studies: 2 (4 sub-questions)
- Total Questions: 20
- Difficulty 1: 9 (45.0%)
- Difficulty 2: 3 (15.0%)
- Difficulty 3: 6 (30.0%)
- Difficulty 4: 2 (10.0%)
- **Higher-Order (L3-L4) Ratio**: **40.0%** (Target: $\ge 30\%$) -> **PASSED**
- Distractor Quality: 100% of distractors contain explicit, pedagogical `why_wrong` explanations dissecting markup mistakes.

---

## 3. Final Verdict
**APPROVED - ZERO DEFECTS**. Ready for index registration and app consumption.
