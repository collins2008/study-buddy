# Topic Inventory: IFT 203 Topic 4 — CSS Selectors, Specificity & Typography
**Topic Slug**: `css_selectors_typography`
**Source Materials**:
- IFT 203 Week 6 Slides: "CSS From the Beginning: Creating, Connecting and Styling Webpages" (Lecturer: Zakariyya Abdullahi Adamu)
- W3C CSS Cascading and Specificity Level 4 Specification
- MDN Web Docs: CSS Selectors, Specificity & Text Styling

---

## 1. Exhaustive Concept Inventory

### A. CSS Syntax & Linking Methods
- **CSS Rule Structure**: `selector { property: value; }`.
- **Three Ways to Apply CSS**:
  1. *Inline*: `<p style="color: blue;">`. Highest specificity (1,0,0,0). Anti-pattern for large apps; poor maintainability.
  2. *Internal / Embedded*: `<style> p { color: blue; } </style>` inside `<head>`. Useful for single-page standalone documents.
  3. *External*: `<link rel="stylesheet" href="styles.css">` inside `<head>`. Industry standard; separates concerns, enables browser caching across pages.
- **The Cascade & Source Order**: When two selectors have equal specificity, the rule appearing later in the CSS document order wins.

### B. CSS Selectors & Combinators
- `*`: Universal selector (matches all elements; specificity 0).
- `element`: Type/element selector (e.g., `h1`, `p`, `div`; specificity 1).
- `.class`: Class selector (e.g., `.btn`, `.card`; specificity 10). Reusable.
- `#id`: ID selector (e.g., `#navbar`, `#submit-btn`; specificity 100). Unique per document.
- `A, B`: Grouping selector (applies declarations to both A and B).
- Combinators:
  - `A B`: Descendant selector (matches any B nested inside A at any depth).
  - `A > B`: Child selector (matches only direct immediate children B of A).
  - `A + B`: Adjacent sibling (matches B immediately preceded by A).
  - `A ~ B`: General sibling (matches any B following A with the same parent).
- Pseudo-classes: `:hover`, `:active`, `:focus`, `:visited`, `:first-child`, `:nth-child(n)`.
- Pseudo-elements: `::before`, `::after`, `::first-letter`, `::first-line`.

### C. Specificity Calculation (The 4-Tier Weight System)
- Tuple $(a, b, c, d)$:
  - $a$: Inline styles (`style="..."` = 1,0,0,0).
  - $b$: ID selectors (`#id` = 0,1,0,0).
  - $c$: Classes, attributes, and pseudo-classes (`.class`, `[type="text"]`, `:hover` = 0,0,1,0).
  - $d$: Element/type selectors and pseudo-elements (`div`, `p`, `::after` = 0,0,0,1).
- Key Rule: Specificity is strictly hierarchical from left to right. One ID (0,1,0,0) overrides 100 classes (0,0,100,0)!
- The `!important` Exception: Forces declaration to override all standard specificity, breaking natural cascade.

### D. Colors & Color Formats
- Named colors: `red`, `blue`, `crimson`.
- Hexadecimal: `#RRGGBB` (e.g., `#ff0000` for red, `#ffffff` for white, shorthand `#f00`).
- RGB: `rgb(red, green, blue)` with values 0 to 255.
- RGBA: `rgba(red, green, blue, alpha)` where alpha is opacity from 0.0 (transparent) to 1.0 (opaque).
- HSL / HSLA: `hsl(hue, saturation%, lightness%)`.

### E. Typography & Measurement Units
- `font-family`: Font stack with generic family fallback (e.g., `Arial, Helvetica, sans-serif;` or `'Times New Roman', Times, serif;`).
- Units of Measurement:
  - *Absolute Units*: `px` (pixels; fixed, does not scale when user changes browser default font size).
  - *Relative Units*:
    - `em`: Relative to the font size of the immediate parent element (compounds multiplicatively in nested structures).
    - `rem` (Root EM): Relative to the font size of the root `<html>` element (default 16px). 1rem = 16px, 1.5rem = 24px. Standard for responsive accessibility.
    - `%`, `vw` (1% of viewport width), `vh` (1% of viewport height).
- Text Properties: `font-size`, `font-weight` (`normal`, `bold`, `400`, `700`), `font-style` (`italic`), `text-align` (`left`, `center`, `right`, `justify`), `text-decoration` (`none` to remove link underlines, `underline`), `text-transform` (`uppercase`, `lowercase`, `capitalize`), `line-height` (vertical line spacing).
