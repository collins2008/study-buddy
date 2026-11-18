# Topic Inventory: IFT 203 Topic 3 — HTML Forms, Inputs, Tables & Media Elements
**Topic Slug**: `html_forms_tables_media`
**Source Materials**:
- IFT 203 Week 5 Slides: "HTML: Structure and Content" (Forms, Tables, Lists, Media)
- IFT 203 Practice Codes Docx: "Student Registration Webpage" (Complete Lecture Code)
- IFT 203 Take-Home Practical 1 (Nile University Dept of IT)
- W3C HTML5 Form & Table Standards

---

## 1. Exhaustive Concept Inventory

### A. HTML Form Architecture & Submission Mechanics
- `<form action="target_url" method="GET|POST" enctype="...">`:
  - `action`: Server endpoint URL receiving data.
  - `method="GET"`: Appends data to URL as query string (`?key=val`). Visible in URL bar, cached, bookmarked, maximum URL length ~2048 chars, idempotent. Insecure for passwords.
  - `method="POST"`: Transmits data in HTTP request payload/body. Hidden from URL bar, not cached, no length limits, mandatory for passwords, sensitive data, and file uploads.
  - `enctype="multipart/form-data"`: Mandatory attribute when form includes `<input type="file">`; without this, only file name string is transmitted rather than binary file contents.

### B. Form Controls & Input Elements
- `<label for="element_id">`: Links text label to specific form control. Improves accessibility and expands clickable hit target.
- `<input type="...">`:
  - `text`, `password` (masked characters), `email` (regex syntax validation), `number` (`min`, `max`, `step`), `date`, `color`, `file`.
  - `radio`: Mutually exclusive options within a group. ALL radios in a set MUST share identical `name="gender"` attribute!
  - `checkbox`: Independent multi-select toggles; share name or unique name.
  - `submit`: Sends form data to action URL.
  - `reset`: Restores all fields to initial default values.
- `<textarea name="..." rows="5" cols="40">`: Multi-line text input; container element requiring `</textarea>` closing tag.
- `<select name="...">` & `<option value="...">`: Dropdown menu (`selected` default option, `multiple` for multi-selection).
- `<fieldset>` & `<legend>`: Semantic and visual grouping of related form controls (e.g., "Personal Details", "Next of Kin").
- Control State Attributes:
  - `required`: Prevents submission if empty (native HTML5 client-side validation).
  - `placeholder`: Temporary hint text that disappears upon typing.
  - `value`: Default or entered string submitted to server.
  - `disabled`: Grayed out, un-editable, AND excluded from form submission.
  - `readonly`: Un-editable, but INCLUDED in form submission.

### C. HTML Tables & Cell Merging
- Semantic Table Elements:
  - `<table>`: Table root.
  - `<caption>`: Accessible title of table (placed immediately after `<table>`).
  - `<thead>`: Header row container.
  - `<tbody>`: Main data row container.
  - `<tfoot>`: Summary / total row container.
- Table Row & Cells:
  - `<tr>`: Table row.
  - `<th>`: Header cell (bold and horizontally centered by default, `scope="col|row"`).
  - `<td>`: Data cell (regular font, left-aligned by default).
- Cell Span / Merging Attributes:
  - `colspan="n"`: Merges a cell horizontally across $n$ columns.
  - `rowspan="n"`: Merges a cell vertically down across $n$ rows.
- Formatting Attributes: `border`, `cellpadding` (padding inside cell), `cellspacing` (space between cells).

### D. Hyperlinks & Media Elements
- Hyperlinks: `<a href="..." target="..." rel="...">`:
  - `target="_blank"`: Opens in new tab/window; requires `rel="noopener noreferrer"` for security.
  - Fragment links: `<a href="#syllabus">` scrolls directly to `<h2 id="syllabus">`.
  - Email protocol: `<a href="mailto:registrar@nileuniversity.edu.ng">`.
- Images: `<img src="path" alt="text" width="x" height="y">`:
  - `alt`: Mandatory fallback text for screen readers and broken image paths.
- Audio & Video:
  - `<audio controls><source src="audio.mp3" type="audio/mpeg"></audio>`
  - `<video controls width="640"><source src="video.mp4" type="video/mp4"></video>`
