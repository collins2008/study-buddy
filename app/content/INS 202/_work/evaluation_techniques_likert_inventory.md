# INS 202 — Topic 5: UI Evaluation Techniques, Heuristics & Likert Scales
## Exhaustive Knowledge Inventory

---

### 1. Usability Specifications & Evaluation Taxonomy
- **Purpose**: Usability can and must be quantified and measured. Usability specifications must be established at the beginning of the project (requirements phase) before implementation begins, setting explicit measurable criteria for success.
- **Formative Evaluation**:
  - Conducted iteratively *during* design and development (using low-fidelity or high-fidelity prototypes).
  - Goal: Diagnose interface flaws, understand *why* problems occur, and guide immediate iterative redesign.
  - Dominantly qualitative (think-aloud protocols, observation notes, design critique).
- **Summative Evaluation**:
  - Conducted at the *end* of a development cycle or upon product release.
  - Goal: Assess overall product quality, verify whether usability specifications were met, or benchmark against competitors.
  - Dominantly quantitative (statistical metrics, task completion rates, benchmark scoring).

---

### 2. Usability Specifications: Performance vs Preference Measures
- **Performance Measures (Objective Behavioral Data)**:
  - *Definition*: Directly observable, quantifiable actions taken by the user during task execution.
  - *Key Metrics*:
    1. **Task Completion Time**: Time required to locate an item or complete a workflow (e.g., time to find a book at Barnes & Noble, time to fill order details).
    2. **Task Completion Rate (Success Rate)**: Percentage of users who successfully complete a defined task scenario without moderator intervention.
    3. **Error Rate & Frequency**: Number of erroneous clicks, invalid form submissions, or slips made per task.
    4. **Back Button Frequency**: High usage of the browser "Back" button serves as a direct behavioral proxy for disorientation ("lostness") and failure of information architecture.
    5. **Click / Navigation Depth**: Number of clicks required to reach target information (e.g., clicks to locate TV program schedule).
    6. **Support & Regressive Behaviors**: Frequency of support calls, explicit user complaints, negative facial expressions, or regressive behaviors (e.g., slamming the mouse, shouting at the screen).
- **Preference Measures (Subjective Attitudinal Data)**:
  - *Definition*: Self-reported perceptions, feelings, opinions, and satisfaction levels expressed by users.
  - *Measurement*: Captured via post-task or post-test standardized questionnaires, primarily utilizing **Likert Scales**.
  - *Performance vs Preference Divergence*: A user may perform efficiently (fast task time) but express low preference (frustrated by aesthetic or perceived stress), or vice versa (slow task time due to exploration, but high satisfaction). Both dimensions must be measured.

---

### 3. Likert Scales: Theory, Design & Analysis
- **Definition**: Psychometric response scale developed by Rensis Likert (1932) where respondents specify their level of agreement or disagreement with a series of declarative statements.
- **Scale Structure**:
  - Typically 5-point (Strongly Disagree, Disagree, Neutral / Neither Agree nor Disagree, Agree, Strongly Agree) or 7-point (adds Moderately Agree/Disagree for higher granular discrimination).
  - Bipolar anchors: Symmetrical balance of positive and negative polarities centered around a neutral midpoint.
- **Methodological Rules**:
  - *Odd vs Even Number of Options*: 5-point and 7-point scales include a neutral midpoint to avoid forcing an artificial opinion; 4-point or 6-point "forced-choice" scales eliminate the neutral option when undecided responses must be prevented.
  - *Acquiescence Bias*: Tendency of participants to agree with statements regardless of content. Countered by including reverse-coded (negatively phrased) items.
  - *Measurement Scale Level*: Individual Likert items produce **ordinal data** (rank-ordered; distance between points is not mathematically guaranteed to be equal). Thus, medians and modes or non-parametric tests (Mann-Whitney U) are formally rigorous. However, multi-item composite Likert scales (e.g., SUS) are routinely treated as interval data for calculating means and standard deviations in UX research.
- **Standardized UX Questionnaires**:
  - **SUS (System Usability Scale)**: 10-item Likert scale (alternating positive and negative statements) yielding a single composite score from 0 to 100. Average benchmark is 68.
  - **SEQ (Single Ease Question)**: 1-item 7-point Likert scale administered immediately after every task: "Overall, how easy or difficult was this task to complete?" (1 = Very Difficult, 7 = Very Easy).

---

### 4. Expert Usability Inspection Methods (Without Users)
- **Heuristic Evaluation (Jakob Nielsen & Rolf Molich)**:
  - *Definition*: An inspection method where a small group of usability experts evaluates an interface against established usability heuristics (rules of thumb).
  - *Evaluator Number & Return Curve*:
    - A single evaluator catches only ~35% of usability issues.
    - 3 to 5 evaluators identify ~75% to 85% of total usability problems.
    - Beyond 5 evaluators, diminishing returns set in: costs rise substantially while few new severe problems are found.
  - *Nielsen's 10 Usability Heuristics*:
    1. **Visibility of System Status**: System keeps users informed through appropriate feedback within reasonable time (e.g., progress bars, loading spinners).
    2. **Match Between System and Real World**: System speaks the user's language (familiar words, phrases, real-world metaphors like desktop trash can) rather than system-oriented jargon.
    3. **User Control and Freedom**: Clear emergency exits to leave unwanted states without an extended dialogue (Undo, Redo, Cancel).
    4. **Consistency and Standards**: Users should not wonder whether different words or actions mean the same thing. Follow platform conventions.
    5. **Error Prevention**: Preventing a problem from occurring in the first place is far superior to good error messages (e.g., confirmation dialogs for destructive actions, input masks, disabling invalid buttons).
    6. **Recognition Rather Than Recall**: Minimize user memory load by making objects, actions, and options visible.
    7. **Flexibility and Efficiency of Use**: Accelerators (keyboard shortcuts, touch gestures, macros) that speed up interaction for experts while keeping it accessible to novices.
    8. **Aesthetic and Minimalist Design**: Dialogues should not contain irrelevant or rarely needed information; every extra unit of information competes with relevant units.
    9. **Help Users Recognize, Diagnose, and Recover from Errors**: Error messages expressed in plain language (no cryptic hex codes), precisely indicating the problem and constructively suggesting a solution.
    10. **Help and Documentation**: Even though a system is usable without documentation, concise, searchable, task-oriented help should be easily accessible.
- **Cognitive Walkthrough (Wharton et al.)**:
  - *Focus*: Evaluating **learnability** and first-time usability for novice or walk-up-and-use interfaces (e.g., kiosks, ticket vending machines).
  - *Method*: Evaluator steps through specific action sequences required to achieve a goal, answering 4 questions at each step:
    1. Will the user try to achieve the right effect?
    2. Will the user notice that the correct action is available?
    3. Will the user associate the correct action with the desired effect?
    4. If the correct action is performed, will the user see that progress is being made towards the goal?

---

### 5. Empirical Usability Testing (With Real Users)
- **Recruiting Participants**:
  - Must recruit representative target users (employees, real customers, temp agencies, students).
  - **Never use family, friends, or development team members**: they are emotionally invested, lack neutrality, and will not be candidly critical.
  - Provide fair incentives (gift cards, coffee mugs, T-shirts, cash compensation).
- **Environment Analysis**:
  - Interfaces must be evaluated in their authentic physical operational context:
    - Outdoor ATM: Users wearing winter gloves require enlarged button touch targets.
    - Mobile browser: Direct glaring sunlight requires extreme contrast and non-reflective design.
    - Noisy manufacturing plant: Auditory alarms and notifications will fail; visual signals are mandatory.
- **Usability Testing Roles & Setup**:
  - *Facilitator / Moderator*: Welcomes participant, gives task scenarios, maintains neutral demeanor, never hints or defends the system.
  - *Participant*: Real user performing authentic tasks while thinking aloud.
  - *Observers / Note Takers*: Record performance timings, back button counts, slips, mistakes, and facial/verbal expressions.
  - *Ethical Pre-Test Briefing*: Explicit statement that "we are evaluating the interface, not testing your intelligence."
