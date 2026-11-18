# Exhaustive Inventory: Topic 3 — Human Factors, Cognitive Psychology & Ergonomics
*Course: INS 202 (Human-Computer Interaction) — Nile University of Nigeria*
*Source Materials: Module_02 1.pptx (57 slides), Gerard Jounghyun Kim Textbook, Student Notebook*

---

## 1. Cognitive Psychology & Human Perception
- **Cognitive Psychology**: The scientific study of mental processes: how people perceive, attend, learn, remember, think, and make decisions.
- **Senses in Computing**: Sight is the primary sensory channel in computing interfaces ("We are visual beings"); hearing (auditory feedback) and touch (haptic feedback) serve secondary confirmation roles.
- **Constructivism**:
  - Theory asserting that the human mind does not record or store literal "pixel-by-pixel" raw sensory snapshots of reality.
  - Instead, the brain actively constructs an intervening abstract cognitive model that summarizes and interprets sensory inputs.
  - Proof: People can recognize the Amazon homepage or Google logo instantly, yet cannot state the exact number of top links, the exact sequence of Google letter colors, or the exact count of stripes in the IBM logo.
- **Context & Mindset**:
  - What a person perceives is heavily governed by the context and their existing mindset (prior expectations).
  - Ambiguous stimuli (e.g. a symbol that can read as the number '13' or letter 'B') are interpreted strictly according to adjacent context (`A 13 C` vs `12 13 14`).
  - Expectation failure: users fail to see a prominent object right in front of them if its shape or location contradicts their mental expectation.
- **Figure and Ground**:
  - Visual perception automatically partitions visual scenes into a *Figure* (foreground object of focal attention) and *Ground* (background context).
  - Rubin's Vase: demonstrates visual bistability where foreground and background flip depending on perceptual focus. Interfaces must clearly differentiate active dialogs/modals (figure) from the underlying page (dimmed ground).

---

## 2. Gestalt Psychology: Five Visual Principles
*German for "unified shape/whole"; principle that the mind perceives holistic structures rather than isolated collections of parts.*
1. **Proximity**:
   - Objects positioned physically close to each other are perceived as belonging to a common group.
   - UI Application: Form field labels must be placed significantly closer to their corresponding input boxes than to the preceding or succeeding inputs; spacing between unrelated card widgets must exceed internal card padding.
2. **Similarity**:
   - Objects that share visual characteristics (shape, color, font, size, orientation) are perceived as related or sharing identical functionality.
   - UI Application: All primary action buttons must share identical colors and geometry; secondary buttons share another consistent style; uniform typography across lists.
3. **Symmetry**:
   - The visual system seeks balance and simplicity, perceiving symmetrical visual elements as unified figures.
   - UI Application: Balanced multi-column layouts, paired navigation elements, centered dialog structures.
4. **Continuity & Alignment**:
   - The eye naturally follows smooth, continuous lines, curves, and visual paths rather than abrupt directional changes.
   - UI Application: Vertical left-alignment of text labels and input fields creates a clean virtual vertical axis, allowing rapid top-to-bottom visual scanning; avoiding ragged centered text for multi-line paragraphs.
5. **Closure**:
   - The human mind automatically fills in missing gaps, contours, or details to perceive a complete, enclosed visual object.
   - UI Application: Icons with broken outlines (like the IBM striped logo or loading spinners) are perceived as complete shapes; cards with partial borders are still understood as bounded containers.

---

## 3. Memory Architecture & Cognitive Limits
- **Sensory Buffer**: Microsecond storage holding raw physical sensory impressions.
- **Short-Term Memory (STM) / Working Memory**:
  - Highly limited capacity; temporary workspace for immediate cognitive tasks.
  - **George Miller's Rule (1956)**: *"The Magical Number Seven, Plus or Minus Two"* ($7 \pm 2$ items). Modern cognitive science refines this to 4–5 items for complex concepts.
  - Information in STM decays within 15–30 seconds unless actively refreshed through rehearsal.
- **Chunking**:
  - The cognitive process of grouping multiple discrete data elements into a smaller number of meaningful, coherent composite "chunks".
  - Examples: Memorizing a 10-digit phone number as three chunks (`080-331-4492`) instead of 10 isolated digits (`0803314492`); reading URLs like `www.bestbookbuys.com` as 4 semantic chunks (`www`, `best`, `book`, `buys`, `.com`).
- **Recognition vs Recall (Golden Rule of Usability)**:
  - *Recall*: Retrieving facts entirely from long-term memory without external prompts (high cognitive load; e.g. typing a terminal command syntax or answering an essay question).
  - *Recognition*: Identifying a correct option from a presented visual list (low cognitive load; e.g. multiple-choice questions, drop-down menus, browser history, bookmarks).
  - *UI Rule*: Always favor recognition over recall! Provide visible menus, search auto-complete, recent file lists, and pickers instead of requiring users to remember and type exact text.
- **Handling Interruptions & Response Times (Robert Miller, 1968)**:
  - *0.1 second*: Perceived as instantaneous; essential for direct manipulation (cursor dragging, button depress states).
  - *1.0 second*: User perceives delay, but their natural stream of thought remains uninterrupted.
  - *10 seconds*: The maximum threshold for maintaining a user's focused attention on a single task. Beyond 10 seconds, attention breaks and users switch to other activities; progress bars and background asynchronous processing are mandatory.

---

## 4. Fitts's Law & Motor Ergonomics
- **Fitts's Law (Paul Fitts, 1954)**:
  - Predicts the time ($T$) required to rapidly move to a target area as a function of the ratio between the target distance ($D$) and target width ($W$):
    $$T = a + b \log_2\left(1 + \frac{D}{W}\right)$$
  - *Index of Difficulty (ID)*: $\log_2(1 + D/W)$ measured in bits.
  - *Key Design Rules*:
    1. Make interactive clickable targets (buttons, links) sufficiently large ($W$), especially on touchscreens (minimum $48 \times 48$ pixels).
    2. Place frequently used controls close to the user's cursor or thumb resting zone ($D$).
    3. The edges and four corners of a computer screen have "infinite width" ($W = \infty$) in desktop GUIs because the mouse cursor stops against the edge of the screen and cannot overshoot (e.g. Windows Start button in bottom-left corner; macOS menu bar along top edge).
- **Physical Ergonomics & Accessibility**:
  - Preventing Repetitive Strain Injury (RSI), carpal tunnel syndrome, and neck strain.
  - Visual ergonomics: high contrast ratios ($\ge 4.5:1$ for normal text under WCAG AA), avoiding pure red-green combinations for color-blind users (deuteranopia/protanopia affects ~8% of males).
