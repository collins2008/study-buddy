# IFT 203: Introduction to Web Technology — 1-Page Exam Cheatsheet
*Nile University of Nigeria • Department of Information Technology (200 Level, First Semester)*
*Instructor: Zakariyya Abdullahi Adamu | Subject: HTML5, CSS3, JavaScript, HTTP & Web Architecture*

---

## 1. Web Architecture & Foundations
- **Internet vs WWW**: Internet = global physical network infrastructure (TCP/IP, 1969); WWW = information service of interlinked hypertext documents accessed via HTTP/URLs (Tim Berners-Lee, 1989).
- **Browser vs Search Engine**: Browser = local client rendering software (Chrome, Firefox); Search Engine = remote web crawler and indexing service (Google, Bing).
- **Static vs Dynamic**: Static = pre-written HTML/CSS files sent identically to all visitors; Dynamic = generated on-the-fly by server scripts (Node/PHP) querying databases.
- **URL Anatomy**: `https://portal.nileuniversity.edu.ng:443/students/results?sem=1#grades`
  - Protocol (`https://`) | Subdomain (`portal.`) | Domain (`nileuniversity.edu.ng`) | Port (`:443`) | Path (`/students/results`) | Query (`?sem=1`) | Fragment (`#grades`).
- **HTTP vs HTTPS**: HTTP = plain-text over port 80; HTTPS = TLS/SSL encrypted over port 443.

---

## 2. HTML5 Core & Semantic Landmarks
- **Standard Boilerplate**:
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nile Portal</title>
  </head>
  <body> ... </body>
  </html>
  ```
- **Void (Empty) Elements (No closing tag)**: `<img>`, `<br>`, `<hr>`, `<input>`, `<meta>`, `<link>`.
- **Block vs Inline**:
  - *Block* (starts new line, 100% width): `<div>`, `<p>`, `<h1>`-`<h6>`, `<section>`, `<article>`, `<header>`, `<footer>`, `<ul>`, `<table>`.
  - *Inline* (flows with text, width fits content): `<span>`, `<a>`, `<strong>`, `<em>`, `<b>`, `<i>`, `<label>`, `<input>`.
- **Semantic HTML5 Landmarks**: `<header>`, `<nav>`, `<main>` (only 1 per page), `<article>` (independent syndication), `<section>` (thematic group), `<aside>` (sidebar), `<footer>`.
- **Semantic vs Presentational**: `<strong>` (semantic importance for screen readers) vs `<b>` (visual bold only); `<em>` (semantic emphasis) vs `<i>` (visual italic).

---

## 3. Forms, Tables & Media
- **Forms**: `<form action="target.php" method="POST" enctype="multipart/form-data">`
  - `GET`: Appends inputs to URL query string (`?user=aliyu`); visible in URL/history, cached, ~2KB limit. Use ONLY for idempotent searches; NEVER for passwords!
  - `POST`: Sends data in HTTP request body; hidden from URL, uncached, no size limits. Mandatory for passwords, sensitive data, and file uploads.
  - `enctype="multipart/form-data"`: Mandatory for `<input type="file">`.
- **Form Controls & States**:
  - Radio Buttons: Mutually exclusive ONLY when they share the EXACT same `name` attribute!
  - `<label for="id">`: Binds label text to input with matching `id`.
  - `disabled`: Grayed out, un-editable, AND excluded from form submission.
  - `readonly`: Un-editable, but INCLUDED in form submission.
- **HTML Tables**:
  - `<table>`, `<caption>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<th scope="col|row">`, `<td>`.
  - `colspan="n"`: Merges a cell horizontally across $n$ columns.
  - `rowspan="n"`: Merges a cell vertically down across $n$ rows.
- **Links & Media**:
  - `<a href="url" target="_blank" rel="noopener noreferrer">`: Opens new tab safely.
  - `<img src="pic.jpg" alt="Description" loading="lazy">`: `alt` is mandatory for accessibility.

---

## 4. CSS Selectors, Specificity & Typography
- **Three Ways to Apply CSS**: Inline (`style="..."`) > Internal (`<style>`) > External (`<link rel="stylesheet">`). External is best practice (caching, separation of concerns).
- **CSS Specificity Tuple $(a, b, c, d)$**:
  - $a$: Inline styles (`style="..."` = 1,0,0,0).
  - $b$: ID selectors (`#nav` = 0,1,0,0).
  - $c$: Classes, attributes, pseudo-classes (`.btn`, `[type="text"]`, `:hover` = 0,0,1,0).
  - $d$: Elements, pseudo-elements (`p`, `div`, `::after` = 0,0,0,1).
  - Hierarchy: $a > b > c > d$. One ID beats 100 classes. Equal specificity $\implies$ later rule in source order wins.
- **Combinators**: `div p` (any descendant) vs `div > p` (direct immediate child only) vs `h1 + p` (adjacent sibling).
- **Units**: `px` (absolute, fixed); `rem` (relative to root `<html>` font size, default 16px; standard for responsive a11y); `em` (relative to parent; compounds multiplicatively in nested tags).

---

## 5. CSS Box Model, Flexbox & Layout
- **Box Model Layers**: Content $\to$ Padding (inside border) $\to$ Border $\to$ Margin (outside border).
- **Box Sizing**:
  - `content-box` (default): $\text{Total Width} = \text{width} + \text{padding} + \text{border}$.
  - `border-box` (standard reset): $\text{width}$ includes content, padding, and border!
  - Reset: `*, *::before, *::after { box-sizing: border-box; }`.
- **Margin Collapsing**: Adjacent vertical margins collapse into $\max(\text{margin}_1, \text{margin}_2)$. Horizontal margins never collapse.
- **Display**: `block`, `inline`, `inline-block` (flows inline but respects width/height/padding), `none` (zero space allocated), `visibility: hidden` (blank space preserved).
- **Positioning**:
  - `static`: Normal flow.
  - `relative`: Offset relative to normal position; establishes positioning context for absolute children.
  - `absolute`: Removed from flow; positioned relative to nearest non-static positioned ancestor.
  - `fixed`: Removed from flow; positioned relative to viewport (stays fixed on scroll).
  - `sticky`: Hybrid; toggles relative to fixed on scroll.
- **Flexbox**:
  - Container: `display: flex; flex-direction: row|column; flex-wrap: wrap; gap: 1rem;`
  - Main Axis Alignment: `justify-content: flex-start | center | space-between;`
  - Cross Axis Alignment: `align-items: stretch | center | flex-start;`
  - Perfect Centering: `display: flex; justify-content: center; align-items: center;`

---

## 6. JavaScript & DOM Manipulation
- **Variables**: `const` (block-scoped, cannot be reassigned) > `let` (block-scoped, reassignable) > `var` (legacy function-scoped, hoisted).
- **Equality**: `==` (loose, coerces types: `'5' == 5` is `true`); `===` (strict, checks type AND value: `'5' === 5` is `false`).
- **DOM Selection**:
  - `document.getElementById('id')`: Single element.
  - `document.querySelector('selector')`: First matching element.
  - `document.querySelectorAll('selector')`: Static `NodeList` (iterable via `.forEach()`).
- **DOM Modification**:
  - `element.textContent = 'text'` (safe plain text) vs `element.innerHTML` (danger of XSS).
  - `element.classList.add()`, `.remove()`, `.toggle()`, `.contains()`.
  - `document.createElement('div')` + `parent.appendChild(el)`.
- **Event Handling**:
  - `form.addEventListener('submit', (e) => { e.preventDefault(); ... });` (stops page reload).
  - Event Flow: Capturing $\to$ Target $\to$ Bubbling.
  - Event Delegation: Single listener on parent container checking `event.target`.

---

## 7. Web Servers, HTTP Status Codes & Security
- **HTTP Status Codes Quick Reference**:
  - `200 OK`: Request succeeded.
  - `201 Created`: Resource successfully created (POST).
  - `301 Moved Permanently`: Permanent redirect (transfers SEO equity).
  - `302 Found`: Temporary redirect.
  - `304 Not Modified`: Cached browser asset is fresh.
  - `400 Bad Request`: Malformed client syntax/parameters.
  - `401 Unauthorized`: Unauthenticated; login required.
  - `403 Forbidden`: Authenticated, but lacking permission/rights.
  - `404 Not Found`: Target URL does not exist.
  - `500 Internal Server Error`: Backend application script crash.
  - `502 Bad Gateway`: Reverse proxy received an invalid upstream response.
  - `503 Service Unavailable`: Server overloaded or down for maintenance.
  - `504 Gateway Timeout`: Upstream server timed out before responding to reverse proxy.
- **Security & Best Practices**:
  - *Same-Origin Policy (SOP)*: Origin = Protocol + Host + Port.
  - *CORS*: Server sends `Access-Control-Allow-Origin: *` to permit cross-origin requests.
  - *Secure Cookie Flags*: `HttpOnly` (blocks JavaScript XSS theft), `Secure` (HTTPS only), `SameSite=Strict` (prevents CSRF).
  - *Performance*: Minification, Gzip/Brotli text compression, CDN edge caching.
