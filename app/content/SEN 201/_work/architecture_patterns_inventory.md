# Topic Inventory: SEN 201 Topic 6 — Software Architecture & Design Patterns
**Topic Slug**: `architecture_patterns`
**Source Materials**:
- Nile University Final Exam Paper Type B (Questions 60, 61, 62)
- Software Engineering Concepts and Principles Lecture Notes (Architectural Design, Patterns, Cohesion/Coupling)
- Somerville SE Chapter on Architectural Design & 4+1 Views

---

## 1. Exam Past Questions Extracted
- **Exam Q60**: Architectural patterns — Reusable descriptions of well-tried design practices across different systems and environments.
- **Exam Q61**: 4+1 Architectural View Model — Specifically the "Process View", which addresses runtime concurrency, communication between executing processes, thread management, and performance/scalability.
- **Exam Q62**: Pipe-and-Filter Architectural Style — Characterized by independent filters executing transformations on incoming data streams, communicating sequentially through pipes without knowing the identity of upstream or downstream filters.

---

## 2. Exhaustive Concept Inventory

### A. Architectural Fundamentals & Value
- **Definition of Software Architecture**: High-level structure consisting of software elements, relations between them, and properties of both.
- **Architecture in the Small vs Large**: "Small" focuses on individual programs and classes; "Large" focuses on complex enterprise, distributed, or multi-system compositions.
- **Value of Explicit Architecture**:
  1. *Stakeholder Communication*: High-level abstraction understandable by non-technical clients, managers, and developers.
  2. *System Analysis*: Evaluates whether non-functional requirements (performance, reliability, security, maintainability) can be satisfied early.
  3. *Large-Scale Reuse*: Architecture styles and components can be reused across product lines.

### B. Architectural Views (The 4+1 View Model of Kruchten)
1. **Logical View**: Shows system abstractions, class diagrams, object hierarchies, and package structures.
2. **Process View**: Shows runtime processes, concurrency, threads, message synchronization, and performance characteristics (Exam Q61).
3. **Development View**: Shows software organization from a programmer's perspective (code modules, libraries, directories, build configurations).
4. **Physical / Deployment View**: Shows physical hardware topology, computing nodes, server distribution, and communication links.
5. **+1 Use Case / Scenario View**: Concrete operational scenarios that validate and unify the four views.

### C. Classic Architectural Patterns / Styles
1. **Layered Architecture (n-tier)**:
   - Structure: Presentation Layer -> Application/Logic Layer -> Data Access Layer -> Database Layer.
   - Rules: Each layer depends only on adjacent lower layers.
   - Advantages: High maintainability, modularity, replaceable layers.
   - Disadvantages: Performance overhead ("sinkhole" anti-pattern), difficulty in cleanly separating concerns in complex workflows.
2. **Repository / Blackboard Architecture**:
   - Structure: Central data store accessed by multiple independent components.
   - Advantages: Efficient sharing of large datasets, components are decoupled from each other.
   - Disadvantages: Central point of failure, data schema changes affect all components, difficult distributed scaling.
3. **Client-Server Architecture**:
   - Structure: Centralized servers offer services (database, compute), clients request services over a network.
   - Variants: Thin client (browser does UI, server does logic and data) vs Fat/Rich client (client runs application logic, server handles storage).
4. **Pipe and Filter Architecture (Exam Q62)**:
   - Structure: Data streams pass through successive transformation steps (filters) connected by channels (pipes).
   - Key attributes: Filters are decoupled, stateless, and do not know who feeds them or who consumes their output.
   - Use cases: Data processing pipelines, compilers, Unix CLI pipelines, audio/video encoding.
5. **Model-View-Controller (MVC)**:
   - Model: Encapsulates state and business logic.
   - View: Renders UI and displays state to user.
   - Controller: Handles user input and triggers model updates and view refreshes.
   - Decouples presentation from application logic.

### D. Architectural Quality Metrics & SOLID Principles
1. **Cohesion**: The degree to which elements within a single module belong together (Goal: High/Strong functional cohesion).
2. **Coupling**: The degree of direct interdependence between software modules (Goal: Loose/Low coupling).
3. **SOLID Principles**:
   - **S**RP: Single Responsibility Principle (A class should have only one reason to change).
   - **O**CP: Open/Closed Principle (Open for extension, closed for modification).
   - **L**SP: Liskov Substitution Principle (Subtypes must be substitutable for their base types without altering program correctness).
   - **I**SP: Interface Segregation Principle (Clients should not be forced to depend on interfaces they do not use).
   - **D**IP: Dependency Inversion Principle (High-level modules should not depend on low-level modules; both should depend on abstractions).

### E. Foundational Gang of Four (GoF) Design Patterns
1. **Creational**:
   - *Singleton*: Ensures a class has only one instance and provides a global access point.
   - *Factory Method*: Defines an interface for creating objects, delegating instantiation to subclasses.
2. **Structural**:
   - *Adapter*: Converts the interface of a class into another interface clients expect.
   - *Facade*: Provides a unified, simplified interface to a complex subsystem.
3. **Behavioral**:
   - *Observer (Publish-Subscribe)*: One-to-many dependency where state change notifies all dependent observers.
   - *Strategy*: Defines a family of interchangeable algorithms encapsulated behind a common interface.
