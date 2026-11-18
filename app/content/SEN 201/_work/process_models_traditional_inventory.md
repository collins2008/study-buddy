# Exhaustive Topic Inventory: SEN 201 Topic 2
**Topic**: Software Process Models (Waterfall, V-Model, Prototyping, Incremental, Spiral, RUP) (`process_models_traditional.json`)
**Course**: SEN 201 — Introduction to Software Engineering (Nile University of Nigeria)
**Lecturer**: Yusuf Mshelia
**Sources**:
- `Software_Engineering_Concepts_and_Principles_Lecture_Notes (1).pdf`, Section 4 & 5
- Nile University 2024/2025 Final Examination Paper (Type B), Questions 3, 4, 10, 15, 43
- `Contents.pdf` Learning Outcomes 1, 2, 3

---

## 1. Software Life Cycle Phases (SDLC)
1. **Planning & Feasibility Study**:
   - Technical feasibility: Are required hardware/software tools and engineer skills available?
   - Economic feasibility: Cost-benefit analysis; ROI.
   - Operational feasibility: Will users accept and support the system?
   - Schedule feasibility: Can project be finished before deadline?
   - Legal/Regulatory feasibility: Data privacy laws (NDPR/GDPR), IP, licensing.
2. **Requirements Analysis**:
   - Eliciting, negotiating, analyzing, documenting, and validating stakeholder needs.
3. **System Design**:
   - High-level architectural design (components, interfaces, subsystem relationships).
   - Detailed design (data structures, algorithms, database schemas, UI design).
4. **Implementation & Unit Testing**:
   - Writing program code, compiling, debugging, and testing individual components.
5. **Integration & System Testing**:
   - Assembling components into subsystems and testing end-to-end functionality, security, performance.
6. **Deployment & Release**:
   - Installing software in production environment, data migration, user training.
7. **Maintenance & Evolution**:
   - Modifying software after delivery to fix defects (corrective), adapt to environment changes (adaptive), enhance performance (perfective), or prevent future failures (preventive).

---

## 2. Process Models Detailed Breakdown
1. **The Waterfall Model (Linear Sequential / Classic Life Cycle)**:
   - Phases: Feasibility $\to$ Requirements $\to$ Design $\to$ Coding $\to$ Testing $\to$ Maintenance.
   - Key Characteristic: Strictly phased; one phase must complete with approved sign-off documentation before the next begins (phase gates).
   - Strengths: Structured, easy to manage, clear documentation trail, suitable for stable, well-understood requirements.
   - Weaknesses: Inflexible, high cost of late change, working software appears only late in the cycle ("big bang" integration risk), blocks customer feedback until the end.
2. **The V-Model (Verification and Validation Model)**:
   - Visualized as a 'V': Downward arm represents development (Requirements $\to$ Architecture $\to$ Detailed Design $\to$ Coding); upward arm represents testing levels corresponding directly to development phases:
     - Acceptance Testing verifies Requirements.
     - System Testing verifies Architectural System Design.
     - Integration Testing verifies Detailed Subsystem Design.
     - Unit Testing verifies Program Code Modules.
   - Strength: Early test planning during development phases.
3. **Prototyping Model**:
   - Purpose: Eliciting, clarifying, and validating uncertain user requirements and UI workflows.
   - Main Value (Nile Exam Q43): Reveals hidden assumptions through interactive visual prototypes.
   - Types: Throwaway prototyping (discarded after requirement validation) vs Evolutionary prototyping (progressively refactored into production code).
   - Major Risk: Customers/management mistake an unsecure prototype for finished production software and push it prematurely into deployment.
4. **Incremental & Iterative Development**:
   - System is partitioned into functional increments delivered over successive releases.
   - Increments deliver priority value early to users.
5. **The Spiral Model (Barry Boehm)**:
   - Key Feature (Nile Exam Q3): **Explicit Risk Assessment and Management**.
   - Radial quadrants in each 360° cycle:
     1. Objective Setting & Constraints.
     2. Risk Analysis, Assessment & Mitigation (e.g. prototyping, simulations).
     3. Development & Verification (engineering product for that cycle).
     4. Review & Planning next phase.
   - Best for: Large, mission-critical, high-risk systems.
6. **Rational Unified Process (RUP)**:
   - Key Focus (Nile Exam Q15): Iterative development and architecture-centric management of requirements.
   - Four Sequential Phases: Inception, Elaboration (baseline architecture created), Construction, Transition (deployment to user environment).
