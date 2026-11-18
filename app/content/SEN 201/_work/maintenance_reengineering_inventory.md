# Topic Inventory: SEN 201 Topic 8 — Software Evolution, Maintenance & Legacy Systems
**Topic Slug**: `maintenance_reengineering`
**Source Materials**:
- Nile University Final Exam Paper Type B (Questions 14, 72, 73, 74, 75, 76, 77, 78, 79, 80)
- Software Engineering Concepts and Principles Lecture Notes (Software Evolution, Maintenance Types, Legacy Systems)
- Somerville SE Chapter on Software Evolution & Lehman's Laws

---

## 1. Exam Past Questions Extracted
- **Exam Q14**: Software Evolution — The continuous lifecycle process of adapting software after initial release to preserve organizational utility.
- **Exam Q72**: Servicing Stage — The evolutionary phase where only critical bug fixes and environment patches are applied; no new business functionality is added.
- **Exam Q73**: Legacy System Components — Encompasses hardware, system infrastructure software, application code, enterprise data, business policies, and human processes.
- **Exam Q74**: Legacy Strategy (Low Quality, High Business Value) — Re-engineer or replace the system to safeguard core business operations while reducing risk.
- **Exam Q75**: Environmental Adaptation Maintenance — Maintenance required due to external changes (OS upgrades, DBMS transitions, cloud migration).
- **Exam Q76**: Maintenance Prediction — Forecasting future change frequency, costs, and component degradation.
- **Exam Q77**: Software Re-engineering Activities — Reverse engineering, code translation, program restructuring, data re-engineering, and refactoring.
- **Exam Q78**: Bad Smells in Code — Duplicate code, long methods/God classes, speculative generality, feature envy (All of the above).
- **Exam Q79**: Complexity Metrics for Maintainability — Number of system interfaces, data structure complexity, cyclomatic control complexity (All of the above).
- **Exam Q80**: Advantage of Re-engineering over Greenfield Development — Reduced business risk and substantially lower cost.

---

## 2. Exhaustive Concept Inventory

### A. Software Evolution Lifecycle & Stages
1. **Initial Development**: The initial creation of the first software release.
2. **Evolution (Evolutionary Stage)**: Major feature enhancements, architectural adaptations, and business expansion.
3. **Servicing (Exam Q72)**: Only essential operational bug fixes and OS patches; no new functional features added.
4. **Phase-out / Retirement**: System is decommissioned or replaced.

### B. Lehman's Laws of Software Evolution
- **Law of Continuing Change**: Systems must continually adapt to changing operating environments, or become progressively less satisfactory.
- **Law of Increasing Complexity**: As an evolving system is modified, its structure degrades and complexity increases unless deliberate preventive work (refactoring) is undertaken.
- **Law of Continuing Growth**: Functional capability must continually expand over the system's lifetime to maintain customer satisfaction.

### C. Types of Software Maintenance (ISO/IEC 14764)
1. **Corrective**: Reactive repairs to correct residual runtime faults and bugs.
2. **Adaptive (Exam Q75)**: Modifying software to operate in a changed hardware, OS, network, or third-party environment.
3. **Perfective**: Implementing new user requirements, enhancing system performance, or improving UI.
4. **Preventive (Refactoring)**: Proactively modifying software to detect and correct latent faults and eliminate code smells before they degrade maintainability.

### D. Legacy System Management & Quadrant Analysis
- **Definition**: Socio-technical systems that rely on obsolete hardware, languages, or architectures, yet remain critical to enterprise operations (Exam Q73).
- **Portfolio Assessment**:
  - *High Business Value, High Quality*: Maintain normally.
  - *High Business Value, Low Quality (Exam Q74)*: Re-engineer or incrementally replace.
  - *Low Business Value, High Quality*: Decommission, archive, or replace with off-the-shelf COTS.
  - *Low Business Value, Low Quality*: Scrap immediately.

### E. Code Smells & Refactoring
- **Code Smells (Exam Q78)**: Structural symptoms indicating deeper design decay:
  - *Duplicated Code*: Identical or highly similar code across multiple locations.
  - *Long Method*: Functions exceeding cognitive limits or handling multiple concerns.
  - *Large Class / God Object*: Classes with excessive attributes and responsibilities.
  - *Feature Envy*: A method that makes more calls to another class's data than its own.
- **Refactoring**: Behavior-preserving transformations (Extract Method, Introduce Parameter Object, Replace Conditional with Polymorphism).

### F. Re-engineering vs Greenfield Redevelopment (Exam Q77, Q80)
- **Re-engineering Steps**: Source code translation, reverse engineering, modular restructuring, data re-engineering.
- **Economic & Risk Advantage**: Greenfield redevelopment has high failure rates due to lost domain knowledge in original specs; re-engineering preserves proven business logic at lower cost.
