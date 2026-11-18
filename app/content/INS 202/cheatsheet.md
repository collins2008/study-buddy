# INS 202: Human-Computer Interaction — 1-Page Exam Cheatsheet
*Nile University of Nigeria | Department of Information Technology / Computer Science | 200-Level Midterms*

---

### 1. HCI Foundational Taxonomy & Core Goals
- **Definition of HCI**: An interdisciplinary field (computer science, cognitive psychology, ergonomics, industrial design) studying the design, evaluation, and implementation of interactive computing systems for human use.
- **The 5 Core Goals of HCI (EXAM FAVORITE — Lecturer Note)**:
  1. **Safety**: Protecting users from physical harm (avionics, radiation therapy, industrial robotics) and preventing catastrophic, irreversible data loss.
  2. **Utility**: The functional capabilities, features, and programmatic services delivered by the system (what the system can do).
  3. **Effectiveness**: Whether users can successfully achieve their intended goals using the provided features (e.g., if a feature exists but is undiscoverable, effectiveness is zero).
  4. **Efficiency**: How quickly and effortlessly users accomplish tasks once proficient (measured in task time, keystrokes, and mental workload).
  5. **Usability**: The ease of learning (learnability), ease of remembering (memorability), error recovery, and subjective user satisfaction.
- **Interaction vs Interface (Mandatory Distinction)**:
  - *Interaction*: The abstract, conceptual behavioral model of dialogue, task flows, and information exchange between user and device.
  - *Interface*: The concrete physical/technical realization (hardware controls, GUI widgets, touch displays, haptic motors).
- **Historical Milestones**:
  - *IBM 1953 (IBM 701, ~33 kb memory)*: Batch computing / punched cards; human time was sacrificed to save scarce machine computing cycles.
  - *Vannevar Bush (1945, Memex)* $\to$ *Douglas Engelbart (1968, Mother of All Demos: Mouse, GUI, Hypertext)* $\to$ *Xerox PARC (Alto, GUI desktop metaphor)* $\to$ *Apple Macintosh (1984)*.

---

### 2. Cognitive Psychology & Ergonomics
- **Memory & Cognition**:
  - *George Miller (1956)*: Working memory limit is **$7 \pm 2$ chunks**. Chunking aggregates discrete units into meaningful wholes (e.g., phone numbers `080-331-4492`).
  - *Recognition over Recall*: The golden rule of UI design; selecting visible items from a menu requires far less cognitive effort than recalling command syntax from memory.
  - *Mental Models*: User mental models (how users believe the system works) must align with the Designer's Conceptual Model through the Interface System Image.
- **Visual Perception (Gestalt Principles)**:
  - *Proximity*: Items placed close together are perceived as a unified cognitive group (e.g., Dan's clothing: group Men/Women clothes, not alphabetical disorder).
  - *Similarity*: Elements sharing color, shape, or orientation are seen as belonging together.
  - *Continuity / Alignment*: Visual grid anchor lines reduce scanning fatigue.
  - *Closure*: The brain fills in incomplete visual contours.
- **Motor Control & Response Time**:
  - *Fitts's Law*: $T = a + b \log_2(1 + D/W)$. Movement time $T$ depends on target distance $D$ and width $W$. Screen corners and edges have *infinite virtual width* ($W = \infty$) because the cursor cannot overshoot the physical display boundary.
  - *Hick-Hyman Law*: $T = b \log_2(n + 1)$. Decision time increases logarithmically with the number of choices $n$.
  - *Robert Miller's Response Time Thresholds (1968)*:
    - **0.1 s**: Perceived as instantaneous direct manipulation.
    - **1.0 s**: User's mental flow of thought remains uninterrupted; slight delay noticeable.
    - **10.0 s**: Maximum threshold for focused human attention; operations $>10\text{s}$ require explicit progress bars and backgrounding.

---

### 3. User-Centered Development (UCD) & Prototyping
- **Core Tenet**: "Know Thy User." Designers are NOT users; managers are NOT users. Always observe frontline end users in their authentic operational context.
- **The Implementation Paradox**: Testing cannot happen until code is written, yet written code is too expensive to discard when flaws appear. Resolved by **rapid iterative prototyping**.
- **Prototyping Taxonomy**:
  - *Low-Fidelity (Paper / Balsamiq)*: Inexpensive, rapid to iterate, pencil/eraser, focuses on layout and information flow, prevents premature aesthetic attachment.
  - *High-Fidelity (Figma / Webflow)*: Clickable vector prototypes, realistic interactions, design system tokens; tests detailed micro-interactions but expensive to overhaul.
  - *Horizontal*: Broad feature scope, top-level pages only, zero backend depth.
  - *Vertical*: Narrow feature scope, deep fully-functional database/logic pipeline.
  - *Evolutionary* (prototype matures into the final code) vs *Throwaway* (discarded after validating specifications).
- **Usability Testing Protocol**:
  - *Think-Aloud Protocol*: Users speak their thoughts aloud during task execution; evaluators maintain strict neutrality (never hint, defend, or guide).

---

### 4. Usability Specifications & Evaluation Techniques
- **Usability Specifications (Module 03)**:
  - *Performance Measures*: Objective behavioral data (task completion time, task success rate, error counts, back button clicks indicating navigational disorientation, support calls, regressive behaviors like shouting).
  - *Preference Measures*: Subjective attitudinal data captured via **Likert Scales** (5-point or 7-point bipolar agreement ratings; mitigate acquiescence bias with reverse coding).
  - *Performance vs Preference Divergence*: Users can rate a system favorably on Likert scales despite taking excessive time and committing multiple errors.
- **Expert Inspection (Without Users)**:
  - *Jakob Nielsen's Heuristic Evaluation*:
    - 1 evaluator catches only ~35% of flaws.
    - **3 to 5 evaluators identify 75% to 85% of usability issues** (optimal cost-benefit balance; $>5$ produces diminishing returns).
    - Top heuristics: Visibility of system status, Match with real world, User control & freedom (undo/emergency exit), Error prevention, Recognition over recall, Aesthetic minimalism.
  - *Cognitive Walkthrough*: Task-based inspection focusing on novice **learnability** across 4 psychological questions.

---

### 5. Information Architecture, Navigation & Accessibility
- **Organizational Schemes (Module 04)**:
  - *Exact*: Alphabetical, Chronological, Geographical (mutually exclusive, objective).
  - *Ambiguous*: Topical, Task-oriented, Audience-specific, Metaphor-driven (conceptual, flexible for browsing).
  - *Card Sorting*: **Open** (users create categories and labels; generative mental model discovery) vs **Closed** (users sort into pre-set categories; evaluative validation).
  - *Hierarchies*: Broad-and-shallow outperforms narrow-and-deep (reduces speculative clicks and lostness).
- **Principles of Visual Organization (Module 05)**:
  - Proximity, Alignment, Consistency, Contrast.
- **Web Accessibility Standards (WCAG 2.1 POUR)**:
  - **P**erceivable: Text alternatives (`alt=""` for decorative), color contrast $\ge 4.5:1$ (normal text) and $\ge 3:1$ (large text), never rely solely on color.
  - **O**perable: Complete keyboard navigation (`Tab`/`Shift+Tab`), no keyboard traps, skip navigation links, no flashes $>3\text{Hz}$.
  - **U**nderstandable: Plain language, predictable inputs, clear form error correction.
  - **R**obust: Semantic HTML5 elements (`<button>`, `<nav>`, `<dialog>`); "No ARIA is better than bad ARIA".
- **Emerging Paradigms**:
  - *VUI*: Hands-free, but transient and serial; heavy short-term memory load; lack of visual affordances.
  - *Gestural / Touch*: Physical fatigue ("Gorilla arm" syndrome from unsupported vertical reaching).
  - *VR / AR*: 6 Degrees of Freedom (translation X,Y,Z + rotation pitch,yaw,roll); simulator sickness from vestibular-ocular sensory conflict.
