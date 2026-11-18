# SEN 201: Introduction to Software Engineering — 1-Page Exam Cheatsheet
*Nile University of Nigeria • Department of Software Engineering (200 Level, First Semester)*
*Instructor: Yusuf Mshelia | Examination Format: Type B (100 Marks, 80 MCQs, 2 Hours)*

---

## 1. Software Engineering Foundations & The Software Crisis
- **Definition (IEEE 610.12)**: The systematic, disciplined, quantifiable approach to development, operation, and maintenance of software.
- **The Software Crisis**: High project failure rates in the 1960s/70s due to schedule/budget blowouts, system crashes, and developer shortages. Solved by shifting from ad-hoc craftsmanship to formal engineering.
- **Boehm's Cost of Change**: Cost to fix defects grows exponentially across phases ($1\times$ in Requirements $\to 5\times$ in Design $\to 10\times$ in Code $\to 20\times$ in Unit Test $\to 100\times+$ in Post-Release Maintenance).
- **Lehman's Laws of Evolution**:
  - *I. Continuing Change*: Software must adapt to its environment or become obsolete.
  - *II. Increasing Complexity*: Evolving systems become structurally more complex unless refactored.
  - *VI. Continuing Growth*: Functionality must continually expand to maintain user satisfaction.

---

## 2. Process Models & Agile Methodologies
| Model | Core Characteristics | Best Suited For |
|---|---|---|
| **Waterfall** | Strict linear phase gates; requirements frozen early. High risk of late surprises. | Stable, well-understood requirements; regulated defense/hardware systems. |
| **Spiral (Boehm)** | Risk-driven iterative loops (Objective, Risk Analysis, Development, Review). | High-risk, large-scale, mission-critical systems. |
| **RUP (Kruchten)** | Architecture-centric, use-case driven; 4 phases: Inception, Elaboration, Construction, Transition. | Complex enterprise applications needing architectural stability upfront. |
| **Scrum** | Agile framework; 2–4 week sprints, Product Backlog, Sprint Backlog, Daily Standup, Retrospective. | Fast-changing user requirements, commercial web/mobile apps. |
| **XP (Beck)** | Engineering craftsmanship: Pair Programming, TDD, Continuous Integration, Refactoring. | Small to medium collocated teams with high change volatility. |
| **Kanban** | Continuous flow, WIP (Work In Progress) limits, cycle time optimization. | Maintenance, operations, servicing teams. |

---

## 3. Requirements Engineering
- **Functional Requirements (FR)**: What the system *must do* (services, calculations, data transformations).
- **Non-Functional Requirements (NFR)**: System quality constraints (performance, reliability, security, availability, regulatory compliance). Must be quantified (e.g., "99.99% uptime", "<500ms latency at 1,000 req/sec").
- **Requirement Types**:
  - *Business*: Organizational goals and revenue justification.
  - *User*: High-level operational tasks in natural language.
  - *System*: Detailed technical specifications for developers (SRS).
- **Flaws of Natural Language**: Ambiguity, over-flexibility, lack of modularity, contradictory assumptions.
- **Scope Creep**: Uncontrolled requirement expansion without adjustments to time, cost, or resources. Mitigated via formal Change Control Boards (CCB).

---

## 4. System Modeling & UML
- **Structural Models (Static)**:
  - *Class Diagram*: Classes, attributes, methods, associations, multiplicities.
  - *Generalization*: Inheritance (`is-a` relationship, hollow triangle arrow).
  - *Aggregation vs Composition*: Aggregation (shared/weak `has-a`, hollow diamond); Composition (exclusive/strong `has-a` lifecycle ownership, solid diamond).
  - *Context Model*: Defines system boundaries and external interfaces.
- **Behavioral Models (Dynamic)**:
  - *Use Case*: Actors, boundary, `<<include>>` (mandatory sub-step) vs `<<extend>>` (conditional optional variation).
  - *Sequence Diagram*: Chronological message exchange; Lifelines (vertical dashed), Activation bars (rectangles), Synchronous calls (solid arrow), Return (dashed open arrow).
  - *Activity Diagram*: Business workflows; Decision diamonds, Forks/Joins (parallel concurrency bars).
  - *State Machine*: State transitions triggered by events with optional boolean guard conditions `[guard]`.

---

## 5. Software Architecture & Design Patterns
- **Kruchten's 4+1 View Model**:
  - *Logical View*: Classes, domain abstractions, object packages.
  - *Process View*: Concurrency, runtime processes, threads, synchronization, latency.
  - *Development View*: Source code modularity, libraries, build dependencies.
  - *Physical View*: Hardware nodes, network topology, deployment environments.
  - *+1 Use Cases*: Unifying operational scenarios.
- **Architectural Styles**:
  - *Layered (n-tier)*: Presentation $\to$ Business Logic $\to$ Data Access $\to$ Database (downward dependency only).
  - *Pipe and Filter*: Decoupled, stateless filters transforming data streams sequentially via pipes.
  - *Repository / Blackboard*: Subsystems exchange data through a central data store (drawback: single point of failure).
  - *Model-View-Controller (MVC)*: Model (data/logic), View (UI), Controller (handles input and updates model).
- **Modular Quality**: High Cohesion (single focused purpose) + Low/Loose Coupling (minimal interdependencies).
- **SOLID Principles**:
  - **S**RP: Single Responsibility (one reason to change).
  - **O**CP: Open for extension, closed for modification.
  - **L**SP: Subtypes must substitute for base types without breaking correctness.
  - **I**SP: Many client-specific interfaces rather than one general interface.
  - **D**IP: High-level modules must depend on abstractions (interfaces), not concrete classes.

---

## 6. Software Testing & Quality Assurance
- **Verification vs Validation (Boehm)**:
  - *Verification*: "Are we building the product right?" (Conformance to specifications).
  - *Validation*: "Are we building the right product?" (Satisfies real customer needs).
- **Testing Stages**: Unit Testing $\to$ Integration Testing $\to$ System Testing $\to$ Release Testing $\to$ Acceptance Testing (Alpha/Beta).
- **Static vs Dynamic**: Static (code inspections, linters, reviews; zero execution); Dynamic (executing software with inputs).
- **Specialized Testing**:
  - *Regression Testing*: Re-executing existing tests to ensure changes did not break working code.
  - *Stress Testing*: Overloading past maximum capacity to verify graceful failure and recovery.
  - *Performance/Load*: Measuring response latency and throughput under peak expected load.
- **Black-Box Design**:
  - *Equivalence Partitioning*: Splitting input space into valid/invalid partitions.
  - *Boundary Value Analysis (BVA)*: Testing at edge transitions: $\text{min}-1$, $\text{min}$, $\text{min}+1$, $\text{max}-1$, $\text{max}$, $\text{max}+1$.
- **White-Box Design**:
  - *McCabe Cyclomatic Complexity*: $V(G) = P + 1 = E - N + 2P$ (Dictates minimum test paths for complete branch coverage).
- **Dijkstra's Axiom**: Testing can show the presence of bugs, but never their absence.

---

## 7. Software Evolution, Maintenance & Legacy Systems
- **Evolution Stages**: Initial Development $\to$ Evolution $\to$ Servicing (critical bug fixes only, no new features) $\to$ Phase-out/Retirement.
- **ISO/IEC 14764 Maintenance Types**:
  - *Corrective*: Reactive fixing of defects and crashes.
  - *Adaptive*: Updating software to run in changed environments (OS, database, hardware).
  - *Perfective*: Enhancing performance or implementing requested user features.
  - *Preventive (Refactoring)*: Proactive code restructuring to eliminate code smells before decay occurs.
- **Legacy System Assessment**: High Business Value + Low Technical Quality $\implies$ Re-engineer or incrementally replace (Strangler Fig pattern).
- **Code Smells**: Duplicated code, Long methods, God classes, Speculative generality, Feature envy.
- **Re-engineering Advantage**: Lower risk and lower cost than greenfield redevelopment by preserving tacit business rules.

---

## 8. Software Project Management, Metrics & CMMI
- **Triple Constraint**: Scope, Time (Schedule), Cost (Budget) $\implies$ Quality at the core.
- **COCOMO (Constructive Cost Model)**:
  - Basic Formula: $\text{Effort} = a \times (\text{KLOC})^b$ [Person-Months].
  - *Organic*: Small, experienced, flexible ($a=2.4, b=1.05$).
  - *Semi-detached*: Medium team, moderate constraints ($a=3.0, b=1.12$).
  - *Embedded*: Strict constraints, safety-critical ($a=3.6, b=1.20$).
- **Critical Path Method (CPM)**: The longest sequence of dependent tasks determining minimum project duration. Tasks have zero float (slack); delays on this path directly delay delivery.
- **Software Configuration Management (SCM)**:
  - *Baseline*: Formally frozen version modifiable only via Change Control Board (CCB).
  - *Traceability*: Mapping requirements $\to$ design $\to$ code $\to$ test cases.
- **CMMI 5 Maturity Levels**:
  - *1. Initial*: Chaotic, ad-hoc, unpredictable, hero-driven.
  - *2. Managed*: Planned, monitored, controlled at project level.
  - *3. Defined*: Organization-wide standard processes documented.
  - *4. Quantitatively Managed*: Statistical process control and metrics.
  - *5. Optimizing*: Continuous quantitative process improvement.
