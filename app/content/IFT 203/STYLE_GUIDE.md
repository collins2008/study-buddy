# Course Style Guide: IFT 203 (Introduction to Web Technology)
*Nile University of Nigeria • Department of Information Technology (200 Level, First Semester)*
*Lecturer: Zakariyya Abdullahi Adamu*

---

## 1. Course Nature & Examination Pedagogy
- **Subject Type**: Hybrid — Technical Foundations + Hands-on Web Markup & Scripting (HTML5, CSS3, Vanilla JavaScript, HTTP Architecture).
- **Lecturer Focus**:
  - Foundational terminology: Internet vs World Wide Web, Webpage vs Website vs Web Application, Web Browser vs Search Engine, Client-side vs Server-side.
  - Correct, valid HTML5 document structures, strict nesting rules, container vs void/empty elements.
  - Semantic HTML5 (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`) and accessibility (`alt`, `<label for="...">`).
  - Form mechanics: `<form action="..." method="GET|POST">`, difference between GET (URL query parameters, idempotent, visible, length limit) and POST (HTTP request body, sensitive data, file uploads).
  - CSS styling methods (Inline vs Internal vs External) and the exact cascade/specificity calculation rules (Inline: 1000, ID: 100, Class: 10, Element: 1, `!important`).
  - The CSS Box Model: Content, Padding, Border, Margin, and `box-sizing: border-box` vs `content-box`.
  - Take-home practical code patterns: Student registration forms, academic timetable tables (`rowspan`, `colspan`), navigation bars.

---

## 2. Examination Blueprint & Question Types
All generated questions must reflect Nile University examination rigor:
1. **Multiple Choice Questions (MCQ) & Multi-Select**:
   - Misconception-driven distractors targeting common syntax and semantic errors (e.g., placing `id` twice on a page, confusing `padding` with `margin`, using `GET` for password submission, omitting `alt` or `doctype`).
   - Every single wrong option must include an in-depth `why_wrong` explanation dissecting the precise web standard violation.
2. **Code Output / Render Verification (`html_render`, `code_output`, `code_bug`, `code_fill`)**:
   - Provide exact HTML/CSS snippets.
   - Use `html_render` renderer so students can see sandboxed previews or identify rendering quirks (e.g., inline-block whitespace, margin collapse, table cell merging).
3. **Sequencing & Matching**:
   - Step-by-step sequencing of browser request-response cycles, CSS specificity cascades, DOM event bubbling, or HTML document hierarchy.
   - Matching HTML elements to semantic roles, CSS properties to box model layers, or HTTP status codes (200, 301, 400, 403, 404, 500) to operational meanings.
4. **Scenario Case Studies**:
   - Multi-part practical problems analyzing broken responsive layouts, inaccessible forms, student registration portals, or client-server debugging.

---

## 3. Cognitive Level Distribution Target
- Difficulty 1 (Recall / Syntax): ~30%
- Difficulty 2 (Understanding / Concepts): ~25%
- Difficulty 3 (Application / Code Troubleshooting): ~35%
- Difficulty 4 (Analysis / Architecture / Design): ~10%
- **Higher-Order (L3-L4) Target**: $\ge 30\%$ across every topic.

---

## 4. Verification Standards
- Every HTML snippet must adhere to standard W3C HTML5 markup rules.
- CSS properties and selectors must conform to standard W3C CSS specifications.
- Verified flag must be set to `true` for all code questions.
