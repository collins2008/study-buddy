import json
import os

topic_data = {
    "course": "IFT 203",
    "topic": "CSS Box Model, Flexbox & Responsive Layouts",
    "summary": "This topic governs visual layout geometry, dimensions, and responsive positioning in modern CSS. Every rendered HTML element forms a rectangular box comprised of four concentric layers: Content (text/media), Padding (internal transparent cushion), Border (perimeter boundary line), and Margin (external spacing separating neighboring elements). Students master the critical distinction between the legacy default `box-sizing: content-box` (where padding and border expand total rendered dimensions) and the modern standard `box-sizing: border-box` (where padding and border are absorbed inside the explicit width and height). The topic analyzes margin collapsing rules, CSS display modes (`block`, `inline`, `inline-block`, `none` vs `visibility: hidden`), and the five positioning schemes (`static`, `relative`, `absolute`, `fixed`, `sticky`) with `z-index` stacking contexts. Finally, it details CSS Flexbox for 1-dimensional row/column alignment (`justify-content` along the main axis, `align-items` along the cross axis) and fluid mobile responsive design via `@media` queries.",
    "key_terms": [
        {
            "term": "CSS Box Model",
            "definition": "The conceptual model defining how every HTML element is rendered as a rectangular box consisting of four layers from inside out: Content, Padding, Border, and Margin."
        },
        {
            "term": "box-sizing: border-box",
            "definition": "A CSS sizing property that forces the element's specified width and height to include its content, padding, and border, preventing layout disintegration when padding is added."
        },
        {
            "term": "box-sizing: content-box",
            "definition": "The default W3C CSS box sizing model where width and height apply exclusively to the content area, so adding padding and border increases the total rendered outer dimensions."
        },
        {
            "term": "Margin Collapsing",
            "definition": "The behavior in CSS where adjacent vertical margins between block-level elements in normal flow combine into a single margin equal to the maximum of the two margin values."
        },
        {
            "term": "position: relative",
            "definition": "A positioning scheme where an element is shifted relative to its normal position in document flow, retaining its original space and establishing a positioning context for absolute children."
        },
        {
            "term": "position: absolute",
            "definition": "A positioning scheme that removes the element completely from normal document flow and positions it relative to its nearest non-static positioned ancestor."
        },
        {
            "term": "Flexbox (Flexible Box Layout)",
            "definition": "A one-dimensional CSS layout model designed for distributing space and aligning items efficiently along a main axis (row or column) and a cross axis."
        },
        {
            "term": "Media Query (@media)",
            "definition": "A CSS technique used to apply different style rules based on device characteristics, such as screen viewport width, resolution, or device orientation."
        }
    ],
    "questions": [
        {
            "id": "ift203-bm-001",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "calculation",
            "difficulty": 3,
            "tags": ["box-model", "calculation", "content-box"],
            "question": "A `<div>` element has the following CSS rules applied:\n```css\ndiv {\n  box-sizing: content-box;\n  width: 250px;\n  padding: 20px;\n  border: 5px solid black;\n  margin: 15px;\n}\n```\nWhat is the TOTAL rendered horizontal space (in pixels) that this element occupies on the web page (including outer margins)?",
            "options": [
                "250px",
                "300px",
                "330px",
                "290px"
            ],
            "answer": 2,
            "explanation": "Under `box-sizing: content-box`:\n- Content width = 250px\n- Left + Right Padding = 20px + 20px = 40px\n- Left + Right Border = 5px + 5px = 10px\n- Total Element Width = 250 + 40 + 10 = 300px\n- Left + Right Margin = 15px + 15px = 30px\n- Total Horizontal Space Occupied = 300px + 30px = 330px.",
            "why_wrong": {
                "0": "250px is only the inner content width, ignoring all padding, borders, and margins.",
                "1": "300px is the element's border-box width, but omits the 30px horizontal margins.",
                "3": "290px incorrectly subtracts or miscalculates the padding and border values."
            },
            "source": "IFT 203 Week 6 Slides; MDN The Box Model"
        },
        {
            "id": "ift203-bm-002",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["border-box", "reset", "layout"],
            "question": "Why do modern web developers universally include the reset rule `*, *::before, *::after { box-sizing: border-box; }` at the beginning of their stylesheets?",
            "options": [
                "To force all text to be displayed in uppercase letters",
                "Because under `border-box`, specified `width` and `height` include content, padding, and border, making multi-column grid calculations predictable and preventing layouts from breaking when padding is adjusted",
                "To remove all colors and images from the web page",
                "Because `border-box` is required by the Windows operating system to open files"
            ],
            "answer": 1,
            "explanation": "By default (`content-box`), adding padding or borders expands the outer width of an element beyond its defined `width`, which easily breaks percentage-based column grids. `box-sizing: border-box` absorbs padding and borders inside the declared width, so a 50% box remains exactly 50% regardless of internal padding, simplifying responsive web design.",
            "why_wrong": {
                "0": "Uppercase text is controlled by `text-transform: uppercase;`, not `box-sizing`.",
                "2": "`box-sizing` affects box dimension calculations; it does not remove colors or images.",
                "3": "Operating systems do not require CSS box-sizing rules to open files."
            },
            "source": "IFT 203 Week 6 Slides; MDN box-sizing"
        },
        {
            "id": "ift203-bm-003",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "calculation",
            "difficulty": 3,
            "tags": ["margin-collapsing", "calculation", "layout"],
            "question": "Two paragraph elements are stacked vertically in normal document flow. Paragraph 1 has `margin-bottom: 35px;`. Paragraph 2 has `margin-top: 20px;`. Under standard CSS margin collapsing rules, what is the EXACT vertical pixel distance between the borders of the two paragraphs?",
            "options": [
                "55px (35px + 20px)",
                "35px",
                "15px (35px - 20px)",
                "20px"
            ],
            "answer": 1,
            "explanation": "In CSS, adjacent vertical margins between block-level elements in normal document flow undergo 'Margin Collapsing': they do not add together ($35 + 20 \\ne 55$). Instead, the margins collapse into a single space equal to the LARGER of the two margin values: $\\max(35, 20) = 35\\text{px}$.",
            "why_wrong": {
                "0": "55px is the most common student trap; vertical margins collapse rather than sum together.",
                "2": "15px incorrectly subtracts the two values.",
                "3": "20px is the smaller margin; the cascade selects the maximum value (35px)."
            },
            "source": "IFT 203 Week 6 Slides; MDN Mastering Margin Collapsing"
        },
        {
            "id": "ift203-bm-004",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "html_render",
            "difficulty": 3,
            "tags": ["display-none", "visibility-hidden", "html-render"],
            "question": "What is the key visual and layout difference between applying `display: none;` versus `visibility: hidden;` to an element?",
            "options": [
                "`display: none;` turns the element red, while `visibility: hidden;` turns it blue",
                "`display: none;` removes the element completely from document flow (surrounding elements collapse into its space), whereas `visibility: hidden;` hides the element visually but preserves its exact physical dimensions and blank space in the layout",
                "There is no difference; both delete the element from the HTML file permanently",
                "`visibility: hidden;` works only on images, while `display: none;` works only on text"
            ],
            "answer": 1,
            "explanation": "`display: none` un-renders the element completely from the visual layout tree: no space is allocated, and adjacent elements shift to fill the gap. In contrast, `visibility: hidden` makes the element invisible (like a transparent pane of glass), but the box retains its width, height, margins, and layout footprint on the page.",
            "why_wrong": {
                "0": "Neither property controls text color; both affect element visibility.",
                "2": "Neither CSS property alters or deletes the underlying HTML DOM tree.",
                "3": "Both properties apply universally to any HTML element."
            },
            "source": "IFT 203 Week 6 Slides; MDN display vs visibility"
        },
        {
            "id": "ift203-bm-005",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "matching",
            "difficulty": 3,
            "tags": ["positioning", "matching", "coordinates"],
            "question": "Match each CSS `position` value to its exact reference origin for coordinates (`top`, `left`, etc.):",
            "options": [
                {"left": "static", "right": "Normal document flow; top/left/z-index properties have zero effect"},
                {"left": "relative", "right": "Positioned offset from its own normal flow position, retaining its original footprint"},
                {"left": "absolute", "right": "Removed from flow; positioned relative to nearest non-static positioned ancestor"},
                {"left": "fixed", "right": "Removed from flow; positioned relative to browser viewport, staying stationary on scroll"},
                {"left": "sticky", "right": "Toggles between relative and fixed positioning based on the user's scroll position"}
            ],
            "answer": [
                {"left": "static", "right": "Normal document flow; top/left/z-index properties have zero effect"},
                {"left": "relative", "right": "Positioned offset from its own normal flow position, retaining its original footprint"},
                {"left": "absolute", "right": "Removed from flow; positioned relative to nearest non-static positioned ancestor"},
                {"left": "fixed", "right": "Removed from flow; positioned relative to browser viewport, staying stationary on scroll"},
                {"left": "sticky", "right": "Toggles between relative and fixed positioning based on the user's scroll position"}
            ],
            "explanation": "These five positioning schemes dictate how elements are placed and shifted relative to the normal flow, ancestors, or viewport.",
            "why_wrong": {},
            "source": "IFT 203 Week 6 Slides; MDN Position"
        },
        {
            "id": "ift203-bm-006",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "sequencing",
            "difficulty": 2,
            "tags": ["box-model-layers", "sequencing"],
            "question": "Arrange the four concentric layers of the CSS Box Model in sequential order from the INMOST layer to the OUTMOST layer:",
            "options": [
                "Content (the inner text, child elements, or image)",
                "Padding (the transparent interior cushion around the content)",
                "Border (the outline enclosing the padding and content)",
                "Margin (the transparent exterior clearance outside the border)"
            ],
            "answer": [
                "Content (the inner text, child elements, or image)",
                "Padding (the transparent interior cushion around the content)",
                "Border (the outline enclosing the padding and content)",
                "Margin (the transparent exterior clearance outside the border)"
            ],
            "explanation": "The CSS Box Model is structured strictly from inside to outside: Content -> Padding -> Border -> Margin.",
            "why_wrong": {},
            "source": "IFT 203 Week 6 Slides; W3C Box Model"
        },
        {
            "id": "ift203-bm-007",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "code_bug",
            "difficulty": 3,
            "tags": ["absolute-positioning", "syntax-bug", "layout"],
            "question": "A developer attempts to position a 'Close' badge in the top-right corner of a card container:\n```html\n<div class=\"card\">\n  <button class=\"close-btn\">X</button>\n  <h3>Card Title</h3>\n</div>\n```\nWith CSS:\n```css\n.card {\n  width: 300px;\n  height: 200px;\n}\n.close-btn {\n  position: absolute;\n  top: 10px;\n  right: 10px;\n}\n```\nInstead of appearing in the top-right corner of the card, the button jumps to the very top-right corner of the ENTIRE browser window. What is the bug, and how is it fixed?",
            "options": [
                "The button needs `display: none;`",
                "An element with `position: absolute` searches up the DOM tree for the nearest ancestor with `position != static`; because `.card` has default `position: static`, the button escaped to the `<body>` viewport. Fix: Add `position: relative;` to `.card`",
                "`position: absolute` is deprecated in CSS3 and must be replaced with `float: right`",
                "The `top` and `right` values should be negative numbers"
            ],
            "answer": 1,
            "explanation": "This is one of the most famous CSS bugs in web development. An absolutely positioned element is positioned relative to its nearest *positioned* ancestor (an ancestor whose position is anything other than `static`). Because `.card` has the default `position: static`, the button jumps all the way up to the initial containing block (`<html>` / viewport). Adding `position: relative;` to `.card` establishes the necessary positioning context.",
            "why_wrong": {
                "0": "`display: none` would completely hide the close button.",
                "2": "`position: absolute` is an active, indispensable modern standard.",
                "3": "Negative values would shift the button outside the viewport entirely."
            },
            "source": "IFT 203 Week 6 Slides; MDN Absolute Positioning Context"
        },
        {
            "id": "ift203-bm-008",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "multi_select",
            "difficulty": 3,
            "tags": ["flexbox", "alignment", "modern-css"],
            "question": "Which of the following statements regarding CSS Flexbox are ACCURATE? (Select ALL that apply)",
            "options": [
                "`justify-content` controls the distribution and alignment of flex items along the Main Axis (horizontal by default when `flex-direction: row`)",
                "`align-items` controls alignment of flex items along the Cross Axis (vertical by default when `flex-direction: row`)",
                "A child element can be perfectly centered both vertically and horizontally inside a container using: `display: flex; justify-content: center; align-items: center;`",
                "Flexbox was designed in 1965 for black-and-white televisions"
            ],
            "answer": [0, 1, 2],
            "explanation": "Options 0, 1, and 2 are core Flexbox principles: `justify-content` governs main-axis alignment, `align-items` governs cross-axis alignment, and combining both with `center` achieves perfect 2-axis centering. Option 3 is humorous nonsense.",
            "why_wrong": {
                "3": "CSS Flexbox was developed by the W3C in the 2010s for responsive web layouts, not 1965 televisions."
            },
            "source": "IFT 203 Week 6 Slides; W3C CSS Flexible Box Layout"
        },
        {
            "id": "ift203-bm-fc01",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "box-model"],
            "question": "Name the four concentric components of the CSS Box Model from inside out.",
            "answer": "1. Content, 2. Padding, 3. Border, 4. Margin.",
            "explanation": "Core definition from IFT 203 Week 6.",
            "why_wrong": {},
            "source": "IFT 203 Week 6 Slides"
        },
        {
            "id": "ift203-bm-fc02",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "border-box"],
            "question": "What is `box-sizing: border-box;` and why is it preferred over `content-box`?",
            "answer": "Under `border-box`, padding and borders are included INSIDE the element's specified width and height. This prevents boxes from expanding unexpectedly and breaking multi-column grid layouts.",
            "explanation": "Standard universal reset used in modern web engineering.",
            "why_wrong": {},
            "source": "IFT 203 Week 6 Slides"
        },
        {
            "id": "ift203-bm-fc03",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "margin-collapse"],
            "question": "What is Margin Collapsing?",
            "answer": "When two adjacent vertical margins meet in normal document flow, they collapse into a single margin equal to the larger of the two values, rather than adding together.",
            "explanation": "Applies strictly to vertical margins in block layout; horizontal margins never collapse.",
            "why_wrong": {},
            "source": "IFT 203 Week 6 Slides"
        },
        {
            "id": "ift203-bm-fc04",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "inline-block"],
            "question": "What is the key advantage of `display: inline-block`?",
            "answer": "It flows horizontally alongside other text/elements without forcing a line break (like inline), BUT allows setting explicit width, height, and top/bottom padding and margins (like block).",
            "explanation": "Combines the inline flow with block dimensional control.",
            "why_wrong": {},
            "source": "IFT 203 Week 6 Slides"
        },
        {
            "id": "ift203-bm-fc05",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "display-vs-visibility"],
            "question": "Contrast `display: none` with `visibility: hidden`.",
            "answer": "`display: none` removes the element completely from document layout (no space allocated).\n`visibility: hidden` hides the element visually, but preserves its exact width, height, and blank space in the layout.",
            "explanation": "Commonly examined CSS layout property distinction.",
            "why_wrong": {},
            "source": "IFT 203 Week 6 Slides"
        },
        {
            "id": "ift203-bm-fc06",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "position-absolute"],
            "question": "What determines the positioning origin of an element with `position: absolute`?",
            "answer": "It is positioned relative to its nearest ancestor that has a `position` other than `static` (e.g., `relative`, `absolute`, or `fixed`). If no such ancestor exists, it is positioned relative to the initial containing block (`<html>` / viewport).",
            "explanation": "Crucial concept for modal dialogs and dropdown menus.",
            "why_wrong": {},
            "source": "IFT 203 Week 6 Slides"
        },
        {
            "id": "ift203-bm-fc07",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "position-fixed"],
            "question": "What does `position: fixed` do, and what is a common use case?",
            "answer": "It removes the element from document flow and positions it relative to the browser viewport. The element remains in the exact same screen position even when the user scrolls the page. Common use case: persistent top navigation bars or floating action buttons.",
            "explanation": "Frequently used for sticky UI headers and sidebars.",
            "why_wrong": {},
            "source": "IFT 203 Week 6 Slides"
        },
        {
            "id": "ift203-bm-fc08",
            "course": "IFT 203",
            "topic": "CSS Box Model, Flexbox & Responsive Layouts",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "perfect-centering"],
            "question": "Write the three lines of CSS required to perfectly center content inside a container using Flexbox.",
            "answer": "```css\ndisplay: flex;\njustify-content: center;\nalign-items: center;\n```",
            "explanation": "The modern industry standard for two-axis centering.",
            "why_wrong": {},
            "source": "IFT 203 Week 6 Slides"
        }
    ],
    "case_studies": [
        {
            "id": "ift203-bm-cs01",
            "scenario": "A student builds a 3-column course summary grid for the Nile University computer science department:\n```html\n<div class=\"container\">\n  <div class=\"card\">COS 201</div>\n  <div class=\"card\">IFT 203</div>\n  <div class=\"card\">SEN 201</div>\n</div>\n```\nWith CSS:\n```css\n.container {\n  width: 900px;\n}\n.card {\n  display: inline-block;\n  width: 300px;\n  padding: 20px;\n  border: 2px solid #ccc;\n}\n```\nThe student expects all three cards to sit side-by-side in a single 900px row. Instead, each card drops onto a new line, stacking vertically.",
            "sub_questions": [
                {
                    "id": "ift203-bm-cs01-q1",
                    "course": "IFT 203",
                    "topic": "CSS Box Model, Flexbox & Responsive Layouts",
                    "type": "calculation",
                    "difficulty": 3,
                    "tags": ["case-study", "box-model-bug", "calculation"],
                    "question": "Calculate the actual rendered width of EACH card under default `content-box`, and explain why the 3 cards failed to fit side-by-side in the 900px container.",
                    "options": [
                        "Each card is 300px; they failed because CSS prohibits 3 cards in one row",
                        "Each card rendered width is 344px (300px width + 40px padding + 4px border); three cards require 1032px, which exceeds the 900px container by 132px, forcing line wrapping",
                        "Each card rendered width is 260px; they failed because the container was too wide",
                        "Each card rendered width is 900px"
                    ],
                    "answer": 1,
                    "explanation": "Under default `box-sizing: content-box`: $\\text{Card Width} = 300\\text{px} + 2(20\\text{px padding}) + 2(2\\text{px border}) = 344\\text{px}$. For three cards, the total width required is $344 \\times 3 = 1032\\text{px}$. Because $1032\\text{px} > 900\\text{px}$, the browser cannot fit them on one line and wraps them onto subsequent lines.",
                    "why_wrong": {
                        "0": "300px is the content width alone, ignoring padding and borders under `content-box`.",
                        "2": "Padding and borders expand the box; they do not shrink it.",
                        "3": "900px is the container width, not the individual card width."
                    },
                    "source": "IFT 203 Week 6 Slides; Box Model Geometry"
                },
                {
                    "id": "ift203-bm-cs01-q2",
                    "course": "IFT 203",
                    "topic": "CSS Box Model, Flexbox & Responsive Layouts",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case-study", "flexbox-refactoring", "responsive"],
                    "question": "Refactor this layout into modern, responsive CSS using Flexbox and `box-sizing: border-box`, and include a media query that stacks the cards into a single column on mobile devices (screens under 768px).",
                    "marking_points": [
                        "Applies universal box-sizing reset: `*, *::before, *::after { box-sizing: border-box; }`.",
                        "Converts container to Flexbox: `.container { display: flex; flex-wrap: wrap; gap: 20px; max-width: 900px; margin: 0 auto; }`.",
                        "Sizes cards flexibly: `.card { flex: 1 1 calc(33.333% - 20px); padding: 20px; border: 2px solid #ccc; }` or `flex: 1`.",
                        "Adds responsive mobile media query: `@media (max-width: 768px) { .card { flex: 1 1 100%; } }`.",
                        "Explains how `gap` and `border-box` prevent overflow bugs."
                    ],
                    "answer": "```css\n/* Universal border-box reset */\n*, *::before, *::after {\n  box-sizing: border-box;\n}\n\n.container {\n  display: flex;\n  flex-wrap: wrap;\n  gap: 20px;\n  max-width: 900px;\n  margin: 0 auto; /* Centers the container on desktop */\n}\n\n.card {\n  flex: 1 1 calc(33.333% - 14px); /* Equal 3-column distribution accounting for gap */\n  padding: 20px;\n  border: 2px solid #ccc;\n  background-color: #f9f9f9;\n  border-radius: 8px;\n}\n\n/* Mobile Responsive Breakpoint */\n@media screen and (max-width: 768px) {\n  .card {\n    flex: 1 1 100%; /* Stacks cards into a full-width single column on phones */\n  }\n}\n```\n\nExplanation of Fix:\n1. `box-sizing: border-box` ensures that the 20px padding and 2px border are absorbed inside the card's width rather than expanding it.\n2. `display: flex` with `gap: 20px` cleanly spaces cards without buggy inline-block whitespace margins.\n3. The `@media (max-width: 768px)` rule dynamically adjusts card basis to `100%`, providing a seamless responsive transition from a 3-column desktop layout to an accessible single-column mobile view.",
                    "explanation": "Modern Flexbox combined with border-box and media queries provides robust responsive layouts.",
                    "why_wrong": {},
                    "source": "IFT 203 Week 6 Slides; Modern Responsive CSS"
                }
            ]
        },
        {
            "id": "ift203-bm-cs02",
            "scenario": "On the Nile University Exam Portal, developers implement a sticky top navigation bar:\n```css\n.navbar {\n  position: fixed;\n  top: 0;\n  left: 0;\n  width: 100%;\n  height: 60px;\n  background: #003366;\n}\n```\nTwo severe usability bugs emerge: (1) The top 60px of page content (the main heading `<h1>Student Exam Schedule</h1>`) is hidden underneath the fixed navbar when the page loads; (2) When a student opens a dropdown menu from the navbar, the dropdown disappears BEHIND an embedded course video player on the page.",
            "sub_questions": [
                {
                    "id": "ift203-bm-cs02-q1",
                    "course": "IFT 203",
                    "topic": "CSS Box Model, Flexbox & Responsive Layouts",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case-study", "fixed-position-offset", "z-index"],
                    "question": "Why did the page heading disappear underneath the navbar, and what CSS rule fixes Bug 1?",
                    "options": [
                        "The heading was deleted by the browser; fix by rewriting the HTML",
                        "`position: fixed` removes the navbar from the normal document flow, so subsequent content moves up to occupy the top of the viewport. Fix: Add `padding-top: 60px;` (or margin) to `body` or `<main>` to push page content down below the fixed navbar height",
                        "The heading color matched the navbar; fix by changing heading text color to green",
                        "The heading was too long; fix by shortening the course title"
                    ],
                    "answer": 1,
                    "explanation": "When an element is assigned `position: fixed`, it is completely removed from document flow and no longer reserves space on the page canvas. The subsequent normal flow content (`<body>` / `<main>`) starts at the very top (`y = 0`), slipping under the 60px navbar. Adding `padding-top: 60px;` to `body` restores the necessary clearance.",
                    "why_wrong": {
                        "0": "The HTML heading exists in the DOM; it is merely visually obscured by the overlapping navbar.",
                        "2": "Changing text color does not fix physical overlap caused by zero flow clearance.",
                        "3": "Title length does not resolve the 60px flow collapse."
                    },
                    "source": "IFT 203 Week 6 Slides; MDN Fixed Positioning"
                },
                {
                    "id": "ift203-bm-cs02-q2",
                    "course": "IFT 203",
                    "topic": "CSS Box Model, Flexbox & Responsive Layouts",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case-study", "z-index", "stacking-context"],
                    "question": "Explain the mechanics of `z-index` and Stacking Contexts that caused Bug 2 (dropdown hiding behind the video), and provide the exact CSS fix to ensure the dropdown always renders in front of all page media.",
                    "marking_points": [
                        "Explains Stacking Context and `z-index`: `z-index` controls depth rendering along the z-axis, but only functions on elements that have an explicit `position` other than `static`.",
                        "Explains why video overlapped dropdown: Browser default rendering or native video hardware overlays often create new stacking contexts or have default higher stacking priority.",
                        "Provides the fix: Setting `z-index: 1000;` on `.navbar` (which already has `position: fixed;`) or positioning the dropdown with a high z-index.",
                        "Notes best practice: Creating a disciplined z-index scale (e.g., dropdown: 100, modal: 1000) rather than random numbers like `999999`."
                    ],
                    "answer": "1. Stacking Context & `z-index` Mechanics:\n- `z-index` determines the 3-dimensional stacking order of elements perpendicular to the screen (the Z-axis). Elements with higher z-index values are rendered in front of elements with lower values.\n- Critical Rule: `z-index` ONLY applies to positioned elements (elements where `position` is `relative`, `absolute`, `fixed`, or `sticky`). On default `position: static` elements, `z-index` is ignored by the browser.\n- In Bug 2, the video player element created a separate hardware-accelerated stacking context, rendering in front of the un-elevated navbar dropdown.\n\n2. The CSS Fix:\nAssign a high z-index to the `.navbar` container (which already has `position: fixed;`):\n```css\n.navbar {\n  position: fixed;\n  top: 0;\n  left: 0;\n  width: 100%;\n  height: 60px;\n  background: #003366;\n  z-index: 1000; /* Guarantees navbar and its child dropdowns sit on top of all page elements */\n}\n\n.dropdown-menu {\n  position: absolute;\n  top: 60px;\n  left: 0;\n  z-index: 1001;\n}\n```",
                    "explanation": "Elevating the positioned navbar's z-index resolves visual clipping and maintains consistent modal hierarchy.",
                    "why_wrong": {},
                    "source": "IFT 203 Week 6 Slides; MDN Understanding CSS z-index"
                }
            ]
        }
    ]
}

out_file = r"c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content\IFT 203\css_box_model_layout.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(topic_data, f, indent=2)

print(f"Successfully generated {out_file} with {len(topic_data['questions']) + sum(len(cs['sub_questions']) for cs in topic_data.get('case_studies', []))} total questions.")
