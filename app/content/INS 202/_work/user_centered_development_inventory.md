# Exhaustive Inventory: Topic 4 — User-Centered Development (UCD) & Prototyping
*Course: INS 202 (Human-Computer Interaction) — Nile University of Nigeria*
*Source Materials: Module_03 (Slides 1–41), Module_07 (Slides 1–34), Gerard Jounghyun Kim Textbook, Student Notebook*

---

## 1. User-Centered Development (UCD) Methodology
- **UCD Philosophy**: Systems must be engineered around the needs, capabilities, workflows, and limitations of human users, rather than forcing users to adapt to system/data constraints.
- **Key Characteristics**:
  1. *User-Centric, Not Data-Centric*: Driven by user task flows rather than database schema tables.
  2. *Active User Involvement*: Real users participate throughout requirements, design, and iterative evaluation.
  3. *Empirical Usability Measurement*: Usability is quantified through objective metrics (task time, completion rates, error counts) and subjective metrics (Likert scale satisfaction).
  4. *Iterative Refinement*: Design $\to$ Prototype $\to$ Test $\to$ Refine cycle repeated continuously.
- **Four Core Stages of UCD**:
  1. *Needs Analysis*: Summarizes the high-level purpose of the system, who it will serve, and business benefits.
  2. *User & Task Analysis*: Exhaustive modeling of user personas, cognitive characteristics, and granular task hierarchies.
  3. *Functional Analysis*: Specifying the system functions required to support identified tasks.
  4. *Requirements & Prototyping*: Developing low-fidelity to high-fidelity prototypes and evaluating with users.

---

## 2. User Analysis & User Characteristics
- **Why User Analysis**: Reduces development and maintenance costs, prevents building unneeded features, increases retention. (IBM website redesign case study: sales increased 400% in first month; 84% reduction in Help button clicks).
- **Core User Dimensions**:
  - *Learning Style*: "Do-then-read" (active exploratory users who test before reading) vs "Read-then-do" (methodical users who study documentation first).
  - *Tool Preferences*: Mouse/touch pointing vs Keyboard power-user shortcuts.
  - *Physical & Demographic Differences*: Age (requiring larger typography and click targets), visual acuity, contrast sensitivity, motor dexterity.
  - *Application Familiarity*: Novice (timid, intimidated, requires high handholding/wizards) vs Intermediate (frequent, needs efficient navigation) vs Expert (power users, requires command shortcuts and dense macro automation).
  - *Primary vs Secondary Users*: Primary user directly operates the interface (e.g. airline check-in clerk); Secondary user receives reports or uses the system intermittently (e.g. regional supervisor).
- **Golden Rule of User Research**:
  - *"Managers are NOT users."* Managers hold assumptions about workflows that often contradict actual frontline practice. The Gold Standard is observing actual users in their authentic operational workplace.

---

## 3. Task Analysis: Goals, Tasks & Actions
- **Granular Hierarchy**:
  1. **Goal**: The high-level state or objective the user wants to achieve (e.g. "Buy a birthday present for a niece").
  2. **Task**: A structured composite activity required to advance toward the goal (e.g. "Select a toy category", "Provide shipping address").
  3. **Action**: An atomic, indivisible physical movement or sensory operation that cannot be decomposed further at this analysis granularity (e.g. "Click the purple dinosaur checkbox", "Type credit card expiry date").
- **User Observation & Research Techniques**:
  - *Think Aloud Protocol*: **"The Gold Standard"** of usability observation. Users verbalize their thoughts, intentions, confusion, and expectations out loud while performing real tasks. Evaluator rule: strictly neutral facilitating prompts ("Tell me what you are looking at right now"); ZERO hints, corrections, or positive/negative feedback!
  - *Talk Right After (Retrospective Interview)*: Reviewing task performance immediately after execution (best when thinking aloud interferes with high-concentration tasks).
  - *Role Playing*: Simulated acting for rare, hazardous, or emergency situations that cannot be observed in real time.
  - *Video-Cued Recall*: Reviewing recorded operational footage with the user to analyze decision points.
  - *Surveys & Focus Groups*: Fast to administer, but prone to leading questions and dominant personalities.
- **Environment Analysis**: Physical context of use (e.g. an outdoor ATM in winter requiring giant buttons for gloved hands; a sunlit mobile delivery app requiring high-contrast mode; a noisy factory floor ruling out subtle auditory alerts).

---

## 4. Prototyping Theory & Taxonomy
- **The Implementation Paradox**:
  - Traditional Waterfall software engineering asserts that you cannot test an interface until you write the code; but writing complete production code is so expensive and time-consuming that teams cannot afford to discard and rewrite it when major usability defects are discovered!
  - Prototyping breaks the paradox: building lightweight, inexpensive mockups allows rapid, low-risk user testing *before* committing engineering code.
- **Taxonomy of Prototypes**:
  - **By Fidelity**:
    - *Low-Fidelity (Lo-Fi)*: Paper sketches, wireframes, cardboard mockups, index cards. Inexpensive in time and cost, fast to modify (pencil and eraser), maximizes iteration cycles, no risk of management mistaking it for finished software. Disadvantages: cannot simulate actual response times; requires facilitator to manually switch paper screens.
    - *High-Fidelity (Hi-Fi)*: Realistic, interactive computer mockups using modern prototyping tools (**Figma, Webflow, WordPress, Wix**). Accurate response times, realistic typography and branding, clickable micro-interactions. Disadvantages: more time-consuming to create, users focus on superficial graphic details rather than core information architecture, management may assume backend is finished.
  - **By Dimensional Scope**:
    - *Horizontal Prototype*: Broad breadth of features across the system, but shallow depth (screens click to top-level pages, but underlying database logic or complex workflows are non-functional).
    - *Vertical Prototype*: Narrow breadth (only one or two specific features), but deep, fully functional operational logic (e.g. a fully working search engine algorithm on a single unstyled page).
  - **By System Coverage**:
    - *Global Prototype*: Comprehensive prototype covering breadth and depth across the entire application.
    - *Local Prototype*: Isolated mockups built specifically to test design alternatives for a contentious design impasse.
    - *Isolated Prototype*: Standalone screen or widget not linked to other pages.
  - **By Lifecycle**:
    - *Throwaway Prototype*: Built strictly to elicit requirements and user feedback, then completely discarded before writing production code.
    - *Evolutionary Prototype*: Incrementally refined and recoded until the prototype gradually becomes the finished production system.
- **Wireframing**:
  - A schematic illustration of a page interface focusing strictly on space allocation, content prioritization, and behavioral layout, intentionally omitting colors, fonts, branding, and final graphics.
