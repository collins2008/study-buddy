# Exhaustive Topic Inventory: SEN 201 Topic 5
**Topic**: System Modeling & UML Diagrams (`system_modeling_uml.json`)
**Course**: SEN 201 — Introduction to Software Engineering (Nile University of Nigeria)
**Lecturer**: Yusuf Mshelia
**Sources**:
- `Software_Engineering_Concepts_and_Principles_Lecture_Notes (1).pdf`, Section 6.3 & 7.6
- Nile University 2024/2025 Final Examination Paper (Type B), Questions 8 & 22
- OMG Unified Modeling Language (UML) Specification 2.5

---

## 1. System Modeling Perspectives & Context Models
1. **Context Models (Nile Exam Q22)**:
   - Illustrates the operational boundary of a software system, identifying what is inside the system and what external entities/systems interface with it.
   - Purpose: Defines project boundaries, integration touchpoints, and external actors.
2. **Structural vs. Behavioral Models**:
   - **Structural (Static)**: Depicts the organization and architecture of components, classes, and physical artifacts.
   - **Behavioral (Dynamic)**: Depicts how the system executes, responds to events, sequences messages, and transitions between internal states over time.

---

## 2. Structural UML Diagrams
1. **Class Diagrams (Nile Exam Q8)**:
   - Represents the static structure of an object-oriented system: classes, attributes, operations, and relationships.
   - Compartments:
     1. Class Name (in bold/centered, italics for abstract).
     2. Attributes: `visibility name : type [multiplicity] = default`.
     3. Operations: `visibility name(param : type) : returnType`.
   - Visibility Notations:
     - `+` Public
     - `-` Private
     - `#` Protected
     - `~` Package
   - Relationships:
     - **Association**: Solid line with multiplicity (e.g. `1` to `0..*`).
     - **Aggregation** (Shared ownership / "has-a"): Hollow diamond at owner end. If container is destroyed, parts survive (e.g., Department has Lecturers).
     - **Composition** (Strict composite ownership / "death dependency"): Filled black diamond at container end. If container is destroyed, child parts are destroyed (e.g., University Examination has Exam Questions).
     - **Generalization / Inheritance** ("is-a"): Solid line with large hollow triangle pointing to superclass.
     - **Realization / Implementation**: Dashed line with hollow triangle pointing to interface.
     - **Dependency**: Dashed directed arrow (`-->`).
2. **Component Diagrams**:
   - Illustrates software components, provided interfaces (lollipops `—O`), and required interfaces (sockets `—)`), showing physical packaging and deployment dependencies.

---

## 3. Behavioral UML Diagrams
1. **Use Case Diagrams**:
   - Components: Actors (stick figures representing roles, external systems, or time), System Boundary box, Use Cases (horizontal ovals).
   - Relationship stereotypes:
     - `<<include>>`: Mandatory sub-flow. Use Case A cannot complete without executing Use Case B (dashed arrow pointing from base to included use case, e.g., `Register Courses` `<<include>>` `Authenticate User`).
     - `<<extend>>`: Optional / conditional sub-flow. Use Case B conditionally adds behavior to Use Case A at specified extension points (dashed arrow pointing from extending use case to base use case, e.g., `Flag Late Penalty Fee` `<<extend>>` `Pay Tuition`).
2. **Sequence Diagrams**:
   - Represents object interactions organized in time sequence.
   - Elements:
     - Lifelines: Vertical dashed lines representing an object instance over time.
     - Activation Boxes: Thin vertical rectangles on the lifeline denoting execution of an operation.
     - Messages:
       - Synchronous Call: Solid line with filled triangular arrowhead (`—>`). Caller blocks waiting for return.
       - Asynchronous Call: Solid line with open arrowhead (`—>`). Caller continues without waiting.
       - Return Message: Dashed line with open arrowhead (`<---`).
     - Combined Fragments: `alt` (if-else conditional alternatives), `opt` (optional single-branch execution), `loop` (iteration).
3. **State Machine (Statechart) Diagrams**:
   - Models the dynamic lifecycle of a single reactive object transitioning through states in response to external events.
   - Elements: Initial state (solid black circle), States (rounded rectangles), Transitions (directed arrows with `event [guard] / action`), Final state (bullseye circle).
4. **Activity Diagrams**:
   - Models procedural workflow, business processes, and concurrency.
   - Elements: Initial node, Activity states, Decision/Merge diamonds, Fork/Join synchronization bars (concurrency).
