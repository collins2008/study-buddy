# Exhaustive Topic Inventory: SEN 201 Topic 3
**Topic**: Agile Software Development, Scrum, Kanban, XP & DevOps (`agile_scrum_kanban_xp.json`)
**Course**: SEN 201 — Introduction to Software Engineering (Nile University of Nigeria)
**Lecturer**: Yusuf Mshelia
**Sources**:
- `Software_Engineering_Concepts_and_Principles_Lecture_Notes (1).pdf`, Section 5.4 & 5.6
- Nile University 2024/2025 Final Examination Paper (Type B), Questions 9, 53, 54, 57, 58
- The Agile Manifesto & Extreme Programming (XP) Standards

---

## 1. The Agile Manifesto & Core Philosophy
1. **Four Fundamental Agile Value Pairs**:
   - Individuals and interactions *over* processes and tools.
   - Working software *over* comprehensive documentation.
   - Customer collaboration *over* contract negotiation.
   - Responding to change *over* following a plan.
2. **Key Agile Principles (Nile Exam Q9 & Q53)**:
   - Primary measure of progress: **Working software delivered frequently** (every few weeks).
   - Welcome changing requirements, even late in development.
   - Sustainable development pace; close daily collaboration between business and developers.

---

## 2. Scrum Framework
1. **Roles**:
   - **Product Owner (PO)**: Voice of the customer. Owns and prioritizes the Product Backlog, defines acceptance criteria, accepts or rejects work.
   - **Scrum Master (SM)**: Servant-leader and agile coach. Protects team, removes impediments/blockers, ensures Scrum rules are followed.
   - **Development Team**: 3–9 members. Cross-functional, self-organizing, collectively responsible for sprint deliverables.
2. **Artifacts**:
   - **Product Backlog**: Living, prioritized master list of all user stories and features.
   - **Sprint Backlog**: Subset of product backlog items selected for execution in the current sprint, broken into tasks.
   - **Increment**: Potentially shippable product functionality completed during the sprint meeting the "Definition of Done".
   - **Burndown Chart**: Graphical chart tracking remaining work/hours versus days in the sprint.
3. **Ceremonies / Events**:
   - **Sprint**: Fixed timebox of 1 to 4 weeks (typically 2 weeks).
   - **Sprint Planning**: Defines sprint goal and selects backlog items.
   - **Daily Scrum (Daily Standup)**: 15-minute timeboxed meeting addressing 3 questions: What did I accomplish yesterday? What will I do today? What blockers exist?
   - **Sprint Review**: Demonstration of working software to stakeholders for feedback.
   - **Sprint Retrospective**: Internal team inspection of team dynamics, tools, and processes for continuous improvement.

---

## 3. Extreme Programming (XP)
1. **Practices**:
   - **Pair Programming (Nile Exam Q54)**: Two developers at one workstation (Driver writes code; Navigator reviews, thinks strategically, spots bugs). Goal: **Spreads knowledge across the team and encourages collective code ownership**, reducing defect rates.
   - **Test-Driven Development (TDD)**: Write failing test first (Red) $\to$ write minimal code to pass (Green) $\to$ clean up structure (Refactor).
   - **Continuous Integration (CI)**: Code merged into mainline repository and automatically built/tested multiple times daily.
   - **Collective Code Ownership**: Any developer can modify any code file; no single developer bottleneck.
   - **Refactoring & Simple Design**: Continuous improvement of internal design without altering external behavior.
   - **On-Site Customer**: Full-time business representative embedded with the development team.

---

## 4. Kanban & Lean Development
1. **Kanban Core Principles**:
   - Visualizing workflow using a Kanban board (Backlog $\to$ Ready $\to$ Coding $\to$ Review $\to$ Done).
   - **Limiting Work In Progress (WIP Limits)**: Strict limit on active items in a column to prevent multitasking bottlenecks and expose flow blockages.
   - Continuous flow without fixed sprint iterations.

---

## 5. DevOps & Open-Source Software
1. **DevOps**:
   - Cultural and automated unification of software development (Dev) and IT operations (Ops).
   - CI/CD pipelines: Automated build, test, package, and deployment.
   - Infrastructure as Code (IaC): Terraform/Ansible; treating server configurations like version-controlled code.
   - Continuous monitoring, logging, and automated rollback.
2. **Open-Source Software Development (Nile Exam Q57 & Q58)**:
   - Core Feature: Collaborative public development with source code freely accessible under open licenses.
   - Business Models: Generating revenue by selling technical support, managed cloud hosting, consulting, and enterprise services (e.g. Red Hat model).
