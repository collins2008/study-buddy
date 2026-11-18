# SEN 201 — Introduction to Software Engineering
## Exam Style Guide & Pedagogical Blueprint
*Derived directly from Nile University 2024/2025 First Semester Final Examination (Type B, 100 Marks, Lecturer: Yusuf Mshelia), Course Outline, & Lecture Notes*

---

## 1. Exam Structure & Examiner Profile
- **Course**: SEN 201 — Introduction to Software Engineering (2 Credit Units)
- **Time Allocated**: 2 Hours (120 Minutes)
- **Total Marks**: 100 Marks
- **Format**: 80 Comprehensive Multiple Choice Questions (Type B Exam Format) covering the full breadth and depth of Software Engineering principles.
- **Examiner**: Yusuf Mshelia (Department of Software Engineering, Faculty of Computing)
- **Exam Weighting by Domain**:
  1. **Software Engineering Concepts & The Software Crisis (~10%)**:
     - Historical definition of "Software Crisis" (schedule/budget blowouts, unreliable systems).
     - Engineering approach vs ad-hoc programming (disciplined, measurable, lifecycle-wide).
     - Economic costs: maintenance consumes 60–80% of total lifecycle cost.
  2. **Software Process & Life Cycle Models (~15%)**:
     - Waterfall model: linear sequential phases, heavy documentation, late verification risk.
     - V-Model: explicit correspondence between development and testing levels.
     - Prototyping: requirements validation, user interaction, throwaway vs evolutionary.
     - Spiral model: risk-driven lifecycle (Boehm), iterative radial quadrants.
     - Rational Unified Process (RUP): 4 phases (Inception, Elaboration, Construction, Transition) and architecture-centric iterative workflows.
  3. **Agile Methodologies & DevOps (~15%)**:
     - Agile Manifesto: working software over comprehensive documentation, responding to change over following a plan.
     - Extreme Programming (XP): pair programming (knowledge sharing & collective ownership), test-driven development (TDD), continuous integration, small releases.
     - Scrum: sprints (1–4 weeks), Product Backlog, Sprint Backlog, Daily Standup, Scrum Master, Product Owner.
     - DevOps & Open Source: CI/CD automation, open-source business models (selling support and services).
  4. **Requirements Engineering & Modeling (~15%)**:
     - Functional vs Non-Functional requirements (constraints: performance, reliability, security, availability).
     - User requirements (task-oriented) vs System requirements (detailed specification).
     - Characteristics of good requirements: unambiguous, verifiable, traceable, complete, consistent.
     - Scope creep: uncontrolled project boundary expansion.
     - Context models: defining system boundary and external interfaces.
  5. **System Modeling & UML (~10%)**:
     - Structural vs Behavioral diagrams.
     - Class diagrams: classes, attributes, operations, associations, multiplicity, generalization, aggregation vs composition.
     - Use Case diagrams: actors, system boundary, `<<include>>` (mandatory) vs `<<extend>>` (optional/conditional).
     - Sequence diagrams: lifeline, synchronous/asynchronous messages, execution occurrences.
  6. **Software Architecture & Design Principles (~15%)**:
     - Architectural styles: Layered, Client-Server, Pipe-and-Filter (sequential stream transformations), Repository / Blackboard, Model-View-Controller (MVC).
     - Kruchten's 4+1 View Model: Logical, Process (runtime interactions), Development, Physical/Deployment + Use Case View.
     - Modular principles: High Cohesion (functional cohesion is highest) and Low Coupling (loose coupling avoids cascading ripple effects).
     - SOLID principles: Single Responsibility (SRP), Open-Closed (OCP), Liskov Substitution (LSP), Interface Segregation (ISP), Dependency Inversion (DIP).
  7. **Software Testing & Quality Assurance (~10%)**:
     - Verification ("Are we building the product right?") vs Validation ("Are we building the right product?").
     - Testing levels: Unit, Integration (top-down, bottom-up, big-bang), System, Acceptance (Alpha in developer environment, Beta in user environment).
     - Static testing (code inspection, walkthroughs, review without code execution) vs Dynamic testing (running executable).
     - Regression testing: ensuring code changes/fixes do not break existing functionality.
     - Stress testing: evaluating failure behavior and recovery beyond normal operating loads.
  8. **Software Project Management, Metrics & Process Assessment (~10%)**:
     - Project planning & WBS (Work Breakdown Structure).
     - Estimation: COCOMO (Constructive Cost Model), Function Points, LOC.
     - SQA & SCM (Software Configuration Management, baseline, check-in/check-out, versioning).
     - CMMI (Capability Maturity Model Integration, 5 levels: Initial, Managed, Defined, Quantitatively Managed, Optimizing).
     - Maintenance phases: Evolution $\to$ Servicing (only operational patches, zero new features) $\to$ Phase-out.
     - Legacy system strategies: Scrap, Maintain, Re-engineer (source translation, refactoring), Replace.
     - Code Smells: Duplicate code, Long methods, Large classes, Speculative generality.

---

## 2. Command Words & Phrasing Patterns (Exact Yusuf Mshelia Phrasing)
- *"What does the term 'software crisis' refer to?"*
- *"What is a key feature of the Spiral Model?"*
- *"Which type of requirement specifies system reliability and response time?"*
- *"What is the primary purpose of version management systems?"*
- *"In object-oriented design, what represents the static structure of classes and their relationships?"*
- *"What is the main focus of regression testing?"*
- *"What does the 'process view' in the 4+1 architectural model represent?"*
- *"Which type of testing does NOT require code execution?"*
- *"During which stage of the software lifecycle are only operational patches made without adding new functionality?"*
- *"Which of the following is considered a 'bad smell' in source code?"*

---

## 3. Strict Distractor & Misconception Rules
Every distractor across all generated questions must target classic software engineering traps:
- Confusing **Functional** (behavior/services) with **Non-Functional** (qualities/constraints like speed, reliability).
- Confusing **Verification** (specification conformance) with **Validation** (customer needs fulfillment).
- Confusing **White-box** (internal logic/path coverage) with **Black-box** (interface specification/equivalence partitioning).
- Confusing **Refactoring** (improving internal structure without altering external behavior) with **Re-engineering** (larger-scale redesign/modernization).
- Confusing **Alpha testing** (internal testing with users at developer site) with **Beta testing** (external testing in actual client environment).
- Confusing **Servicing** (maintenance bug fixes only) with **Evolution** (adding new capabilities to meet evolving business needs).
- Confusing **Agile** with "no documentation" or "coding without design" (Agile prioritizes working software, not total absence of documentation).
