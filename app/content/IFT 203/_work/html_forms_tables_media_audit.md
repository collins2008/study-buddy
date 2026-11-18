# Hostile Pedagogical & Technical Audit: IFT 203 Topic 3
**Topic**: HTML Forms, Inputs, Tables & Media Elements (`html_forms_tables_media.json`)
**Auditor**: Senior University Examiner & Web Architecture Lead

---

## 1. Inventory & Exam Blueprint Coverage
- [x] Form submission methods: Security and payload differences between `method="GET"` (query string, cacheable, URL leak) and `method="POST"` (request body, secure, uncached).
- [x] Binary file upload configuration: Mandatory `enctype="multipart/form-data"` with `method="POST"`.
- [x] Form controls & accessibility: Accessible `<label for="...">` binding, grouping radio buttons via identical `name` attribute to enforce mutual exclusivity.
- [x] Field state attributes: Dissecting the critical exam trap between `readonly` (un-editable but submitted) and `disabled` (grayed out and omitted from submission).
- [x] HTML Tables: Semantic hierarchy (`<table>`, `<caption>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<th>`, `<td>`).
- [x] Table cell merging geometry: Practical application and calculation of `colspan` (horizontal columns) and `rowspan` (vertical rows).
- [x] Hyperlinks and multimedia: Secure external linking (`target="_blank"` with `rel="noopener noreferrer"`), mandatory `alt` attribute on `<img>`, audio/video controls.
- [x] 2 Multi-part Case Studies:
  1. Nile University Student Registration Form Practical: Debugging multi-radio selection flaws, insecure GET password transmission, missing binary photo enctype, and writing refactored accessible HTML5 markup.
  2. Academic Timetable Grid: Computing exact `rowspan` and `colspan` cell geometry for a 2-hour lab lecture and daily assembly break, constructing clean semantic table code with proper cell omission rules.

---

## 2. Statistical Breakdown
- Total Main Questions: 16
- Total Case Studies: 2 (4 sub-questions)
- Total Questions: 20
- Difficulty 1: 8 (40.0%)
- Difficulty 2: 3 (15.0%)
- Difficulty 3: 7 (35.0%)
- Difficulty 4: 2 (10.0%)
- **Higher-Order (L3-L4) Ratio**: **45.0%** (Target: $\ge 30\%$) -> **PASSED**
- Distractor Quality: 100% of distractors contain explicit, pedagogical `why_wrong` explanations dissecting form and table mistakes.

---

## 3. Final Verdict
**APPROVED - ZERO DEFECTS**. Ready for index registration and app consumption.
