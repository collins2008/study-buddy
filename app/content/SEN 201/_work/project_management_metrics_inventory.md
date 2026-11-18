# Topic Inventory: SEN 201 Topic 9 — Software Project Management, Metrics & Process Assessment
**Topic Slug**: `project_management_metrics`
**Source Materials**:
- Lecturer Notebook Hints ("SW project management, team mgmt, scheduling, measurement, risk, QA, config mgmt")
- Nile University Final Exam Paper Type B (Questions 11, 49)
- Software Process Assessment Models PDF (CMMI 5 Maturity Levels, ISO/IEC 15504 SPICE)
- Software Engineering Concepts and Principles Lecture Notes (Project Planning, Estimation, COCOMO, SCM)

---

## 1. Exam & Lecturer Hints Extracted
- **Lecturer Notebook**: Software project management, team management, scheduling, measurement, risk management, QA, configuration management.
- **Exam Q11**: Version control and Software Configuration Management (SCM) — Tracking, managing, and controlling changes to digital artifacts.
- **Exam Q49**: Scope creep — Uncontrolled expansion of project scope without adjustments to time, cost, and resources.

---

## 2. Exhaustive Concept Inventory

### A. Software Project Management Core Pillars
- **Project Dimensions (Triple Constraint / Iron Triangle)**: Scope, Time, Cost, with Quality at the center.
- **Work Breakdown Structure (WBS)**: Hierarchical decomposition of the total scope of work to be carried out by the project team.
- **Scheduling**: Gantt charts, activity networks, Critical Path Method (CPM), float/slack time calculation.

### B. Software Cost & Effort Estimation
1. **Algorithmic Cost Modeling (COCOMO - Constructive Cost Model by Barry Boehm)**:
   - Basic Formula: $\text{Effort} = a \times (\text{KLOC})^b$ [Person-Months].
   - Three Project Modes:
     * *Organic*: Small teams, experienced developers, familiar environments ($a=2.4, b=1.05$).
     * *Semi-detached*: Medium teams, mixed experience, medium constraints ($a=3.0, b=1.12$).
     * *Embedded*: Tight hardware/software constraints, strict regulations, complex interfaces ($a=3.6, b=1.20$).
   - Intermediate COCOMO: Multiplies base effort by 15 Cost Drivers (EAF - Effort Adjustment Factor).
2. **Function Point Analysis (Allan Albrecht)**:
   - Measures functional size delivered to user independent of programming language.
   - 5 Function Types: External Inputs (EI), External Outputs (EO), External Inquiries (EQ), Internal Logical Files (ILF), External Interface Files (EIF).

### C. Software Risk Management
- **Risk Definition**: A potential future event or condition that, if it occurs, has an adverse effect on project objectives.
- **Risk Management Lifecycle**:
  1. *Risk Identification*: Checklists, brainstorming, technology/people risks.
  2. *Risk Analysis / Assessment*: Likelihood (Probability) and Seriousness (Impact). Risk Exposure = Probability $\times$ Impact.
  3. *Risk Planning*:
     - Avoidance: Redesign to eliminate risk.
     - Mitigation: Take actions to reduce impact if it occurs.
     - Transfer: Pass risk to third party (insurance, outsourcing).
     - Acceptance: Acknowledge risk and establish contingency reserves.
  4. *Risk Monitoring*: Regular review meetings to track risk triggers.

### D. Software Configuration Management (SCM)
- **Baseline**: A formally reviewed and agreed-upon version of a configuration item, serving as the basis for further development.
- **SCM Activities**:
  1. Configuration Identification: Naming and cataloging artifacts.
  2. Version Control: Tracking revisions (Git, commits, branches, merges).
  3. Change Control: Change requests, impact analysis, Change Control Board (CCB) approval.
  4. Configuration Auditing: Verifying that released software contains exactly the approved versions.

### E. Software Process Assessment & CMMI (Capability Maturity Model Integration)
- **5 CMMI Maturity Levels (Staged Representation)**:
  1. *Level 1: Initial*: Ad-hoc, chaotic processes. Success depends on heroic individual efforts. High risk of schedule/budget blowouts.
  2. *Level 2: Managed*: Projects are planned, monitored, and controlled at the project level. Basic project management established.
  3. *Level 3: Defined*: Processes are well-characterized, standardized, and integrated into organization-wide standard processes.
  4. *Level 4: Quantitatively Managed*: Processes and product quality are measured statistically and quantitatively controlled.
  5. *Level 5: Optimizing*: Continuous process improvement driven by quantitative feedback and piloting innovative ideas.
- **ISO/IEC 15504 (SPICE)**: International standard framework for process assessment.
