# Exhaustive Topic Inventory: SEN 201 Topic 1
**Topic**: Software Engineering Principles & The Software Crisis (`principles_software_crisis.json`)
**Course**: SEN 201 — Introduction to Software Engineering (Nile University of Nigeria)
**Lecturer**: Yusuf Mshelia
**Sources**:
- `Software_Engineering_Concepts_and_Principles_Lecture_Notes (1).pdf`, Sections 1–3
- Nile University 2024/2025 Final Examination (Type B), Questions 1 & 2
- Department of Software Engineering Course Outline & Learning Outcomes

---

## 1. Core Definitions & Concepts
1. **Software Engineering**:
   - A systematic, disciplined, and measurable approach to the development, operation, maintenance, and evolution of software systems.
   - Applies engineering principles to produce software that satisfies user requirements, meets quality standards, remains maintainable, and is delivered within time and budget constraints.
2. **Definition of Software**:
   - Software is NOT just executable code. It is a collection of:
     1. Computer programs (executable code and binaries).
     2. Procedures and configuration data.
     3. Associated documentation (requirements specs, architecture designs, user manuals, test plans).
3. **The Software Crisis**:
   - Coined at the 1968 NATO Science Committee conference in Garmisch, Germany.
   - Manifestations / Symptoms:
     - Projects consistently exceeding scheduled time and financial budgets.
     - Low quality, frequent software crashes, and high defect densities.
     - Systems failing to satisfy user requirements or business objectives.
     - Software being unmaintainable and difficult to modify.
     - Low developer productivity relative to skyrocketing hardware complexity.
4. **Birth of Software Engineering**:
   - Prompted by the failure of large, complex software systems built using unstructured, artisanal, individual programming techniques.
   - Shifted focus from craft-based programming to formalized engineering lifecycles.
5. **Software Engineering vs. Programming**:
   - Scope: SE spans the entire Software Development Life Cycle (SDLC); Programming focuses on coding and debugging.
   - Team Dynamics: SE involves multidisciplinary teams (analysts, designers, developers, QA, DevOps, managers); Programming is often individual or pair-based.
   - Core Concerns: SE emphasizes quality, architecture, risk, cost, and lifecycle maintenance; Programming emphasizes algorithms, syntax, and execution logic.

---

## 2. Classification of Software Products
1. **Generic Products**:
   - Stand-alone systems produced by a development organization and sold on the open market to any customer who wishes to buy them.
   - Specification: Owned and controlled by the software developer (e.g. Microsoft Windows, Adobe Photoshop, Microsoft Office).
2. **Customized (Bespoke) Products**:
   - Systems commissioned by a specific customer to satisfy their unique operational needs.
   - Specification: Owned and controlled by the customer/client (e.g. Nile University Student Registration Portal, Air Traffic Control System, Military Radar).

---

## 3. Core Software Engineering Principles
1. **Abstraction**: Capturing essential characteristics while hiding non-essential implementation details.
2. **Modularity**: Decomposing a large system into smaller, self-contained, manageable modules.
3. **Encapsulation & Information Hiding**: Bundling state and operations within a boundary and restricting external direct access to private internal representations.
4. **Separation of Concerns (SoC)**: Dissecting software into distinct sections such that each section addresses a separate concern (e.g., presentation vs. business logic vs. data access).
5. **High Cohesion**: Measuring the degree to which all elements inside a single module belong together and serve a single well-defined purpose. Functional cohesion is the strongest and most desirable form.
6. **Low Coupling**: Minimizing interdependencies and direct knowledge between distinct modules, ensuring changes in one module do not cause cascading ripple bugs in others.
7. **Reusability & Simplicity**: Designing components for repeated use across multiple projects; adhering to Occam's razor / KISS.
8. **DRY (Don't Repeat Yourself)**: Every piece of knowledge or business rule must have a single, unambiguous, authoritative representation within a system.
9. **SOLID Principles**:
   - **SRP (Single Responsibility Principle)**: A class/module should have one, and only one, reason to change.
   - **OCP (Open-Closed Principle)**: Software entities should be open for extension, but closed for modification.
   - **DIP (Dependency Inversion Principle)**: High-level modules should not depend on low-level modules; both should depend on abstractions.
10. **Principle of Least Privilege**: A security rule granting a component or user only the minimal access rights necessary to complete its specific operational function.
11. **Defensive Programming**: Proactively anticipating potential errors, unexpected inputs, and system failures through comprehensive validation and exception handling.
