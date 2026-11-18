# Topic Inventory: IFT 203 Topic 2 — HTML5 Core: Elements, Semantic Tags & Attributes
**Topic Slug**: `html_structure_semantics`
**Source Materials**:
- IFT 203 Slide 3: "Introduction to HTML and Web Page Structure" (Lecturer: Zakariyya Abdullahi Adamu)
- HTML Basics Week 4 Slides & Take-Home Practical 1 (Nile University Dept of IT)
- W3C HTML5 Specification & MDN Web Docs

---

## 1. Exhaustive Concept Inventory

### A. Document Skeleton & Boilerplate
- `<!DOCTYPE html>`: Document type declaration informing browser to render in standards mode (not quirks mode).
- `<html lang="en">`: Root container element for entire document.
- `<head>`: Non-rendered metadata container:
  - `<meta charset="UTF-8">`: Specifies UTF-8 character encoding.
  - `<meta name="viewport" content="width=device-width, initial-scale=1.0">`: Critical mobile responsive configuration.
  - `<title>`: Browser tab text, bookmarks, and search engine title.
  - `<link rel="stylesheet" href="...">`: Connects external CSS.
- `<body>`: Contains all visible, rendered page content.

### B. Tags, Elements & Attributes
- **Tag**: `<p>` (opening tag), `</p>` (closing tag).
- **Element**: Start tag + content + end tag (e.g. `<p>Nile University</p>`).
- **Void (Empty) Elements**: Elements that cannot contain child content and have no closing tag: `<br>`, `<hr>`, `<img>`, `<input>`, `<meta>`, `<link>`.
- **Attributes**: Key-value pairs inside opening tags providing configuration:
  - Global attributes: `id` (unique document-wide identifier), `class` (reusable styling/scripting hook), `title` (browser hover tooltip), `style` (inline CSS), `hidden`, `tabindex`.

### C. Headings, Text Formatting & Document Typography
- Headings: `<h1>` to `<h6>` (hierarchical importance, block display).
- Paragraphs: `<p>`, line break `<br>`, thematic horizontal rule `<hr>`.
- Semantic vs Presentational Text Tags:
  - `<strong>` (semantic importance) vs `<b>` (visual bold only).
  - `<em>` (semantic emphasis) vs `<i>` (visual italic only).
  - `<mark>` (highlighted text), `<small>` (fine print), `<del>` (deleted text), `<ins>` (inserted text).
  - `<sub>` (subscript, e.g. $H_2O$) vs `<sup>` (superscript, e.g. $x^2$).
  - `<pre>` (preformatted monospace text preserving whitespace and newlines) vs `<code>` (code snippet).
- HTML Comments: `<!-- comment -->` (unrendered).

### D. Block-Level vs Inline Display Behaviors
- **Block-Level Elements**:
  - Behavior: Always start on a new line; take up the full available parent width (100%); respect top/bottom margins and padding.
  - Examples: `<div>`, `<h1>`-`<h6>`, `<p>`, `<ul>`, `<ol>`, `<li>`, `<header>`, `<main>`, `<section>`, `<article>`, `<footer>`.
- **Inline Elements**:
  - Behavior: Do not start on a new line; take up only necessary content width; vertical margins/padding do not push surrounding elements away.
  - Examples: `<span>`, `<a>`, `<img>`, `<strong>`, `<em>`, `<b>`, `<i>`, `<br>`, `<label>`, `<input>`.
- **Nesting Rules**: Block elements can contain block or inline elements; inline elements must never wrap block-level containers in standard HTML5.

### E. Semantic HTML5 Elements & Accessibility
- **Non-Semantic Elements**: `<div>` (generic block division) and `<span>` (generic inline span).
- **Semantic HTML5 Elements**:
  - `<header>`: Introductory content, university logo, site banner.
  - `<nav>`: Primary navigation links.
  - `<main>`: Central, unique body content of the document (only one per page).
  - `<section>`: Thematic grouping of content, typically with a heading.
  - `<article>`: Self-contained, independently distributable composition (news article, blog post, forum comment).
  - `<aside>`: Tangentially related sidebar content (author bio, related links).
  - `<footer>`: Closing content, copyright, privacy policy, contact details.
  - `<figure>` & `<figcaption>`: Self-contained media with accompanying caption.
- **Why Semantics Matter**:
  1. *Accessibility (a11y)*: Screen readers allow blind users to navigate landmark regions (`<main>`, `<nav>`).
  2. *Search Engine Optimization (SEO)*: Search engines accurately rank and index structured articles.
  3. *Developer Maintainability*: Self-documenting code structure eliminating nested "div-soup".
