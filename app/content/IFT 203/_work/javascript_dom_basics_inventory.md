# Topic Inventory: IFT 203 Topic 6 — JavaScript Fundamentals, Control Flow & DOM
**Topic Slug**: `javascript_dom_basics`
**Source Materials**:
- IFT 203 Syllabus & Web Technology Lecture Notes (JavaScript, DOM Manipulation, Event Handling)
- W3C DOM Level 4 Specification & ECMAScript Standards (ES6+)
- MDN Web Docs: JavaScript Basics, DOM APIs & Event Model

---

## 1. Exhaustive Concept Inventory

### A. JavaScript Language Fundamentals
- **Role in Web Architecture**: Provides client-side dynamic behavior, user interactivity, API data fetching, and DOM manipulation.
- **Script Attachment**:
  - `<script src="app.js"></script>` at end of `<body>` or in `<head>` with `defer` (executes in order after HTML parsing).
  - Internal `<script> ... </script>` vs External `.js` files.
- **Variables & Scope**:
  - `var`: Function-scoped, hoisted to top with `undefined`, allows re-declaration (legacy).
  - `let`: Block-scoped `{ }`, reassignable, temporal dead zone (modern ES6).
  - `const`: Block-scoped `{ }`, cannot be reassigned, mandatory initializer.
- **Type System & Operators**:
  - Primitives: String, Number, Boolean, Null, Undefined, BigInt, Symbol.
  - Loose equality `==` (coerces types, `'5' == 5` is `true`) vs Strict equality `===` (evaluates type AND value, `'5' === 5` is `false`).
  - Control Flow: `if / else`, `switch (val) { case x: break; }`, `for`, `while`, `for (const item of items)`.
  - Functions: Declarations `function greet() {}`, Expressions `const greet = function() {}`, Arrow functions `const greet = () => {}`.

### B. Document Object Model (DOM) Architecture
- **Definition**: The hierarchical tree representation of an HTML document created in memory by the browser engine upon parsing.
- **DOM Node Hierarchy**: `document` $\to$ `<html>` (root element) $\to$ `<head>` and `<body>` $\to$ child element nodes, attribute nodes, and text nodes.
- **Selection Methods**:
  1. `document.getElementById('id')`: Returns single matching Element node or `null`.
  2. `document.getElementsByClassName('class')`: Returns live `HTMLCollection`.
  3. `document.querySelector('cssSelector')`: Returns first element matching any valid CSS selector (`.card > p`, `#submit-btn`).
  4. `document.querySelectorAll('cssSelector')`: Returns static `NodeList` of all matching elements (supports `.forEach()`).

### C. DOM Manipulation & Modification
- **Content Modification**:
  - `element.textContent`: Reads/writes plain unformatted text (safe from XSS).
  - `element.innerHTML`: Reads/writes raw HTML markup (parses tags; danger of Cross-Site Scripting - XSS if used with untrusted user input).
- **Attribute & Class Manipulation**:
  - `element.setAttribute('src', 'logo.png')`, `element.getAttribute('href')`.
  - `element.classList.add('active')`, `element.classList.remove('active')`, `element.classList.toggle('active')`, `element.classList.contains('active')`.
- **Dynamic Node Creation**:
  - `const el = document.createElement('div')`
  - `el.textContent = 'New Course'`
  - `parent.appendChild(el)` or `parent.append(el)`
  - `el.remove()`

### D. Event Handling & Propagation
- **Standard Syntax**: `element.addEventListener('click', (event) => { ... });`.
- **Event Object & Methods**:
  - `event.target`: The exact element that triggered the event.
  - `event.preventDefault()`: Prevents default browser action (e.g., stops `<form>` submission page reload or `<a>` link navigation).
  - `event.stopPropagation()`: Halts event bubbling up the DOM tree hierarchy.
- **Event Bubbling & Event Delegation**:
  - Bubbling: Event triggers on innermost child and propagates up through parents to `document`.
  - Event Delegation: Attaching a single event listener to a parent container to manage events triggered by existing or dynamically added child elements.
