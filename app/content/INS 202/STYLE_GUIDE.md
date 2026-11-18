# Course Style Guide: INS 202 (Human-Computer Interaction)
*Nile University of Nigeria • Department of Information Systems / Computing (200 Level, First Semester)*
*Textbook & Syllabus: Gerard Jounghyun Kim, "Human-Computer Interaction: Fundamentals and Practice" & Prentice Hall UCD Curriculum*

---

## 1. Course Nature & Examination Pedagogy
- **Subject Type**: Design Theory, Cognitive Psychology, Information Architecture & Usability Engineering.
- **Reference Texts**:
  - Kim, Gerard Jounghyun. *Human–Computer Interaction: Fundamentals and Practice*. CRC Press.
  - McCracken, D. D., & Wolfe, R. J. *User-Centered Website Development: A Human-Computer Interaction Approach*. Prentice Hall.
- **Lecturer Focus & High-Priority Signals (Direct from Lecture Decks & Student Notebook)**:
  - **The 5 Core Goals of HCI (EXPLICITLY FLAGGED AS CRITICAL FOR EXAMS)**:
    1. *Safety*: Protecting human users from hazardous situations (e.g. air traffic control, nuclear plants, intensive care monitors) and protecting critical data from accidental destruction.
    2. *Utility*: The functional capabilities, features, and services provided by a system (what tasks the system allows users to execute).
    3. *Effectiveness*: Whether users can successfully achieve their intended goals or complete transactions without failure (distinct from utility: a system might offer a feature, but if users cannot find it, it lacks effectiveness).
    4. *Efficiency*: How rapidly users can accomplish their tasks or finish their work once learned (measured in task completion time, keystrokes, clicks).
    5. *Usability*: Ease of learning (learnability), ease of remembering (memorability), error prevention, and general user satisfaction.
  - **Interaction vs Interface**:
    - *Interaction*: An abstract, conceptual model through which a human user interacts with a computing device to perform a specific task.
    - *Interface*: The concrete physical or technological realization (hardware, input/output peripherals, graphical display, software controls) of that interaction model.
    - *HCI Definition*: The "I" in HCI encompasses both the abstract interaction model and the technological interface methodology.
  - **Historical Milestone**:
    - *IBM 1953 (IBM 701, ~33 kb memory)*: The commercial birth of scientific electronic computers; batch-oriented, physical punch card interface, where human programmer time was sacrificed to save scarce machine computing time.
  - **Cognitive Psychology & Human Factors**:
    - *George Miller's Magic Number (1956)*: Short-term working memory capacity is strictly limited to $7 \pm 2$ chunks of information.
    - *Chunking*: Organizing individual data units into meaningful cohesive groups (e.g. phone numbers or URLs like `www.bestbookbuys.com`).
    - *Recognition vs Recall*: Interfaces must favor recognition over recall (e.g. drop-down menus, bookmarks, and visual icons are far easier than requiring users to type command syntax from memory).
    - *Gestalt Principles*: Proximity (grouping by distance), Similarity (grouping by visual shape/color/size), Symmetry (expecting balanced groupings), Continuity/Alignment (visual alignment along virtual axes), and Closure (mentally filling in missing visual gaps).
    - *Affordances & Signifiers*: Perceived affordance indicates how an object can be used (e.g., a raised button affords pushing).
  - **Content Organization & Information Architecture**:
    - *Exact Schemes*: Categorize content into mutually exclusive groups: Alphabetical, Chronological, Geographical.
    - *Ambiguous Schemes*: Context-dependent groupings with overlapping boundaries: Topical (subject), Task-Oriented (what user wants to do), Audience-Specific (tailored for distinct groups: Students vs Staff), and Metaphor-Driven.
    - *Structures*: Hierarchical (Top-down tree; Breadth = links per level, Depth = number of levels), Hypertext (associative networked links), and Database (bottom-up search queries).
  - **Navigation Design**:
    - *Site-level Navigation*: Moves users through information architecture (Global navigation bar consistent on every page, Breadcrumb trails).
    - *Page-level Navigation*: Enhances understanding within an individual page (tables of contents, internal anchor links).
  - **Prototyping & Evaluation**:
    - *Fidelity*: Low-Fidelity (inexpensive paper wireframes, sketch pads, cards; flushes out early structural flaws) vs High-Fidelity (interactive clickable prototypes in tools like **Figma, Webflow, WordPress, Wix, Colorlib**).
    - *Scope*: Horizontal (broad range of features, shallow depth) vs Vertical (few features, deep functional implementation).
    - *Usability Evaluation*: Think Aloud protocol ("Gold Standard" of observation), Performance measures (objective time/errors) vs Preference measures (**Likert Scales**, satisfaction ratings), Nielsen's 10 Heuristics.

---

## 2. Examination Blueprint & Question Types
All generated questions must reflect strict academic examination standards:
- **MCQ (Single Answer)**: Diagnostic distractors with comprehensive `why_wrong` explanations.
- **Multi-Select**: Comprehensive identification of HCI goals, Gestalt principles, and prototyping tradeoffs.
- **True/False with Justification (`true_false_why`)**: Conceptual boundary checks (e.g. utility vs effectiveness, low vs high fidelity prototyping).
- **Type Answer**: Normalised technical terminology (e.g. "Likert", "chunking", "affordance", "Figma", "7").
- **Cloze**: Structural multi-blank formulas, definition chains, and cognitive thresholds.
- **Matching**: Matching Gestalt principles to visual examples, organizational schemes to site structures, prototyping models to development stages.
- **Sequencing**: Ordering User-Centered Development (UCD) lifecycle phases, task analysis hierarchies (Goal $\to$ Task $\to$ Action), prototyping workflows.
- **Explain (Free-text with Marking Points)**: Analytical comparisons (Interaction vs Interface, Recognition vs Recall, Horizontal vs Vertical prototypes).
- **Case Studies**: Real-world e-commerce, banking, hospital, and university portal redesign scenarios with 3–5 multi-part diagnostic and design questions.

---

## 3. Difficulty Level Distribution
- **Level 1 (Recall)**: Definitions, inventors, historical dates, memory limits (~25%).
- **Level 2 (Understand)**: Explaining psychological principles, scheme tradeoffs, prototyping fidelity (~30%).
- **Level 3 (Apply)**: Diagnosing usability defects on university websites, designing navigation bars, constructing Likert surveys (~30%).
- **Level 4 (Analyze/Evaluate)**: Redesigning complex medical/banking interfaces, resolving navigation breadth/depth conflicts (~15%).
- **Target**: At least 40% Level 3–4 across all topics.
