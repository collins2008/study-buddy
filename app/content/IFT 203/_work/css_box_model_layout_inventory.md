# Topic Inventory: IFT 203 Topic 5 — CSS Box Model, Flexbox & Responsive Layouts
**Topic Slug**: `css_box_model_layout`
**Source Materials**:
- IFT 203 Week 6 Slides: CSS Properties, Box Model & Layout
- W3C CSS Box Model Module Level 3 & CSS Flexible Box Layout Module Level 1
- MDN Web Docs: Box Model, Flexbox, Positioning & Media Queries

---

## 1. Exhaustive Concept Inventory

### A. The CSS Box Model Layers
- Every HTML element is rendered as a rectangular box consisting of four concentric layers from inside to outside:
  1. **Content**: Text, child elements, or media (`width`, `height`).
  2. **Padding**: Transparent spacing around content inside the border (`padding`).
  3. **Border**: The frame bounding padding and content (`border: width style color`).
  4. **Margin**: Transparent spacing outside the border separating neighboring elements (`margin`).
- Shorthand 4-Value Clockwise Notation:
  - `padding: 10px;` (all 4 sides)
  - `padding: 10px 20px;` (top/bottom, left/right)
  - `padding: 10px 20px 30px;` (top, left/right, bottom)
  - `padding: 10px 20px 30px 40px;` (top, right, bottom, left — Clockwise from 12 o'clock!)

### B. Box Sizing: `content-box` vs `border-box`
- **Default `box-sizing: content-box`**:
  - `width` applies ONLY to content area.
  - $\text{Total Width} = \text{width} + \text{padding-left} + \text{padding-right} + \text{border-left} + \text{border-right}$.
  - Trap: An element with `width: 50%`, `padding: 20px`, and `border: 2px solid` will exceed 50% total width, causing side-by-side elements to break onto new lines.
- **Modern Standard `box-sizing: border-box`**:
  - `width` includes content + padding + border!
  - Content area automatically compresses so outer dimensions match specified `width`.
  - Universal Reset: `*, *::before, *::after { box-sizing: border-box; }`.

### C. Margin Collapsing & Display Types
- **Margin Collapsing**: When two vertical margins meet between adjacent block elements in normal flow, they collapse into a single margin equal to the larger of the two values:
  - Example: Element 1 has `margin-bottom: 40px`; Element 2 has `margin-top: 25px`. Rendered vertical distance is $\max(40, 25) = 40\text{px}$ (NOT $65\text{px}$!).
  - Horizontal margins NEVER collapse.
- **Display Modes**:
  - `block`: Full-width, new line, respects width/height/margins/padding.
  - `inline`: No line break, width/height ignored, vertical padding/margin does not affect layout flow.
  - `inline-block`: Flows inline without line breaks, BUT respects explicit width, height, and all padding/margins.
  - `none`: Completely removed from rendering tree and visual space.
  - `visibility: hidden`: Hides element visually, BUT leaves an empty blank box preserving its exact dimensions.

### D. CSS Positioning Schemes (`position`)
1. `static`: Default normal document flow.
2. `relative`: Positioned relative to normal flow using `top`, `bottom`, `left`, `right`; retains original space in flow; creates positioning context for absolute children.
3. `absolute`: Removed from normal flow; positioned relative to nearest ancestor with `position != static`.
4. `fixed`: Removed from normal flow; positioned relative to browser viewport; remains pinned during scrolling.
5. `sticky`: Acts as `relative` until a scroll threshold is met, then acts as `fixed`.
- `z-index`: Stacking order along depth axis; only applies to positioned elements (`position != static`).

### E. CSS Flexbox (Flexible Box Layout)
- Container Properties:
  - `display: flex;`
  - `flex-direction: row | column | row-reverse | column-reverse;`
  - `justify-content: flex-start | flex-end | center | space-between | space-around | space-evenly;` (aligns along Main Axis)
  - `align-items: stretch | flex-start | flex-end | center | baseline;` (aligns along Cross Axis)
  - `flex-wrap: nowrap | wrap;`
- Item Properties: `flex-grow`, `flex-shrink`, `flex-basis`, shorthand `flex: 1;`.
- Perfect Centering Trick: `display: flex; justify-content: center; align-items: center;`.

### F. Responsive Design & Media Queries
- `@media screen and (max-width: 768px) { ... }`
- Fluid layouts, flexible media: `img { max-width: 100%; height: auto; }`.
