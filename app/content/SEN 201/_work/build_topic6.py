import json
import os

topic_data = {
    "course": "SEN 201",
    "topic": "Software Architecture & Design Patterns",
    "summary": "Software architecture provides a high-level blueprint representing system structures, computational elements, and their interrelations. It bridges requirements analysis and detailed software implementation, directly determining critical non-functional properties including scalability, security, performance, and maintainability. Kruchten's 4+1 View Model organizes architectural perspectives into Logical, Process, Development, and Physical views, unified by use-case scenarios. Major architectural styles include Layered (n-tier separation of concerns), Repository/Blackboard (shared data storage), Client-Server (distributed service distribution), Pipe-and-Filter (sequential stream transformation by decoupled filters), and Model-View-Controller (MVC). Robust system design adheres to high cohesion, low coupling, and the SOLID principles to minimize technical debt and facilitate enterprise evolution.",
    "key_terms": [
        {
            "term": "Software Architecture",
            "definition": "The fundamental structure of a software system, comprising software components, externally visible properties of those components, and the relationships among them."
        },
        {
            "term": "Architectural Pattern",
            "definition": "A stylized, reusable solution to a commonly occurring design problem in software architecture, providing structural templates and operating rules."
        },
        {
            "term": "4+1 View Model",
            "definition": "An architectural view model defined by Philippe Kruchten that illustrates systems through four distinct viewpoints: Logical, Process, Development, and Physical, tied together by Scenarios (+1)."
        },
        {
            "term": "Pipe-and-Filter Architecture",
            "definition": "An architectural style where processing units (filters) transform sequential input data streams and transmit outputs to downstream units through communication channels (pipes) without knowing unit identities."
        },
        {
            "term": "Model-View-Controller (MVC)",
            "definition": "An architectural pattern that decouples an application into three interconnected parts: Model (data and business logic), View (UI presentation), and Controller (handles user input and mutates the model)."
        },
        {
            "term": "High Cohesion",
            "definition": "An engineering principle where all responsibilities, data, and methods within a module or class are closely related to a single well-defined purpose."
        },
        {
            "term": "Loose Coupling",
            "definition": "An engineering design principle where modules have minimal dependencies on the internal implementation details of other modules, enabling independent testing and modification."
        },
        {
            "term": "Dependency Inversion Principle (DIP)",
            "definition": "The SOLID principle stating that high-level modules should not depend on low-level modules; both should depend on abstractions (interfaces), and abstractions should not depend on details."
        }
    ],
    "questions": [
        {
            "id": "sen201-ap-001",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "mcq",
            "difficulty": 1,
            "tags": ["architecture", "patterns", "design", "nile-exam"],
            "question": "What is an architectural pattern in software engineering?",
            "options": [
                "A detailed database table schema specifying primary and foreign key constraints",
                "A reusable description of a well-tried design practice across different software systems and environments",
                "A specific programming language compiler syntax rule",
                "A project management Gantt chart detailing developer assignments"
            ],
            "answer": 1,
            "explanation": "As defined in software engineering literature and Nile Final Exam Question 60, an architectural pattern is a reusable, stylized description of good design practice that has been tried and tested across different operational environments and system types.",
            "why_wrong": {
                "0": "A database schema is a low-level physical data design artifact, not an architectural pattern.",
                "2": "A compiler syntax rule governs language parsing, which is language specification rather than system architecture.",
                "3": "A Gantt chart is a project management scheduling artifact, not a software architectural pattern."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q60; Sommerville Ch. 6"
        },
        {
            "id": "sen201-ap-002",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["4+1-view", "process-view", "concurrency", "nile-exam"],
            "question": "In Kruchten's 4+1 View Model of software architecture, what is the primary focus of the 'Process View'?",
            "options": [
                "The decomposition of the software into packages, classes, and inheritance hierarchies",
                "The interactions between runtime processes, concurrency, threads, and performance scalability",
                "The physical mapping of software binaries onto server nodes and network links",
                "The software development environment, repository branching, and build tool configuration"
            ],
            "answer": 1,
            "explanation": "According to Nile Final Exam Question 61 and Kruchten's 4+1 View Model, the Process View specifically addresses the dynamic aspects of the system at runtime: communicating processes, threads, synchronization, concurrency, and performance constraints.",
            "why_wrong": {
                "0": "Decomposition into packages, classes, and object hierarchies is the domain of the Logical View.",
                "2": "The physical mapping onto servers and hardware topology is the domain of the Physical/Deployment View.",
                "3": "The developer organization, build tools, and directory structure are the domain of the Development View."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q61; Kruchten 4+1"
        },
        {
            "id": "sen201-ap-003",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["pipe-and-filter", "architectural-styles", "nile-exam"],
            "question": "Which of the following best describes the Pipe-and-Filter architectural style?",
            "options": [
                "A central database where multiple clients concurrently modify a shared blackboard",
                "Sequential transformations of data streams where independent filters process inputs and output results to pipes without knowing upstream or downstream identities",
                "A client requesting a transaction from a remote server through an RPC call",
                "A hierarchical structure where user interfaces directly mutate low-level database records without intermediary layers"
            ],
            "answer": 1,
            "explanation": "Nile Final Exam Question 62 and standard SE texts define the Pipe-and-Filter architecture as a pipeline of independent transformation components (filters) connected by communication buffers (pipes). Each filter processes streaming data and transmits output without needing to know the identity or implementation of adjacent filters.",
            "why_wrong": {
                "0": "A central database modified concurrently by multiple clients describes the Repository or Blackboard architecture.",
                "2": "Remote procedure calls between clients and servers describe the Client-Server or Distributed Object style.",
                "3": "Direct modification of database records from UI violates layered architectural principles and describes anti-pattern spaghetti architecture."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q62; Sommerville Ch. 6"
        },
        {
            "id": "sen201-ap-004",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["cohesion", "coupling", "software-design"],
            "question": "A senior software architect reviews a proposed module and notices that it handles user authentication, generates monthly PDF invoices, sends email alerts, and directly executes raw SQL queries against three different database tables. What design assessment must the architect issue?",
            "options": [
                "The module exhibits ideal high cohesion and tight coupling, maximizing execution speed",
                "The module suffers from low cohesion and tight coupling, violating the Single Responsibility Principle and creating maintenance fragility",
                "The module demonstrates loose coupling because all operations are grouped inside a single source file",
                "The module demonstrates high cohesion because all four tasks are executed by an online web application"
            ],
            "answer": 1,
            "explanation": "The module possesses low cohesion because it combines unrelated responsibilities (security, document generation, network communications, and database access). It also possesses high/tight coupling because it binds directly to multiple database tables and external communication systems. In good design, modules should strive for high cohesion (single, focused purpose) and loose coupling.",
            "why_wrong": {
                "0": "Tight coupling is a design defect, not an advantage, and low cohesion impairs maintainability.",
                "2": "Grouping disparate tasks into a single source file creates a 'God class' monolith, which increases coupling rather than loosening it.",
                "3": "Belonging to the same overall web application does not make functions cohesive; cohesion requires strong functional relatedness within the specific class or module."
            },
            "source": "Software Engineering Concepts and Principles Lecture Notes; Sommerville Ch. 6"
        },
        {
            "id": "sen201-ap-005",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "matching",
            "difficulty": 3,
            "tags": ["4+1-view", "matching", "architecture"],
            "question": "Match each 4+1 Architectural View to its primary focus and representation:",
            "options": [
                {"left": "Logical View", "right": "Class diagrams, object models, and domain abstractions"},
                {"left": "Process View", "right": "Concurrency, threads, inter-process communication, and latency"},
                {"left": "Development View", "right": "Code packages, libraries, modular subsystems, and build dependencies"},
                {"left": "Physical View", "right": "Hardware processors, server nodes, network topologies, and deployment units"}
            ],
            "answer": [
                {"left": "Logical View", "right": "Class diagrams, object models, and domain abstractions"},
                {"left": "Process View", "right": "Concurrency, threads, inter-process communication, and latency"},
                {"left": "Development View", "right": "Code packages, libraries, modular subsystems, and build dependencies"},
                {"left": "Physical View", "right": "Hardware processors, server nodes, network topologies, and deployment units"}
            ],
            "explanation": "Philippe Kruchten's 4+1 View Model structures architectural descriptions according to stakeholder viewpoints: Logical (functional domain abstractions), Process (runtime concurrency/performance), Development (source code modularity/builds), and Physical (hardware deployment topology).",
            "why_wrong": {},
            "source": "Kruchten 4+1 View Model; Nile Final Exam Q61"
        },
        {
            "id": "sen201-ap-006",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "sequencing",
            "difficulty": 2,
            "tags": ["layered-architecture", "n-tier", "sequencing"],
            "question": "Arrange the layers of a classic 4-tier enterprise software architecture in order from highest level (closest to the end-user) to lowest level (closest to persistent storage):",
            "options": [
                "Presentation Layer (User Interface & Controllers)",
                "Business Logic / Domain Application Layer",
                "Data Access / Persistence Layer (ORMs, DAOs)",
                "Database / Storage Layer (Relational DBMS, Cloud Storage)"
            ],
            "answer": [
                "Presentation Layer (User Interface & Controllers)",
                "Business Logic / Domain Application Layer",
                "Data Access / Persistence Layer (ORMs, DAOs)",
                "Database / Storage Layer (Relational DBMS, Cloud Storage)"
            ],
            "explanation": "In standard n-tier architecture, requests flow downward: Presentation Layer captures user actions -> Business Logic executes business validation and computations -> Data Access Layer constructs queries and maps models -> Database Layer stores and manages persistent records.",
            "why_wrong": {},
            "source": "Sommerville Ch. 6; Software Engineering Concepts and Principles Lecture Notes"
        },
        {
            "id": "sen201-ap-007",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["mvc", "design-patterns", "architecture"],
            "question": "In the Model-View-Controller (MVC) architectural pattern, how is separation of concerns achieved when a user submits a form on a web page?",
            "options": [
                "The View updates the database directly and then refreshes the Controller",
                "The Controller receives user input, validates or delegates it to update the Model, and instructs the View to update its presentation",
                "The Model intercepts the HTTP request, renders HTML directly, and bypasses the Controller",
                "The Controller stores database rows and executes SQL statements without involving the Model"
            ],
            "answer": 1,
            "explanation": "In MVC, the Controller acts as the orchestrator: it listens to user actions, interprets inputs, commands the Model to update its state, and selects the appropriate View to render the updated state back to the user.",
            "why_wrong": {
                "0": "The View should have no direct interaction with or knowledge of the persistent database.",
                "2": "The Model encapsulates data and business logic; it does not parse raw HTTP requests or generate UI HTML markup directly.",
                "3": "Database persistence and business logic belong in the Model, not the Controller."
            },
            "source": "Sommerville Ch. 6; Software Engineering Concepts and Principles Lecture Notes"
        },
        {
            "id": "sen201-ap-008",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "multi_select",
            "difficulty": 3,
            "tags": ["solid", "design-principles", "object-oriented"],
            "question": "Which of the following scenarios represent DIRECT VIOLATIONS of SOLID design principles? (Select ALL that apply)",
            "options": [
                "A `Square` class inherits from `Rectangle`, but overriding `setWidth()` automatically alters height, breaking client code that calculates rectangle area (Violates Liskov Substitution Principle)",
                "A report generation class requires modification to its core source code whenever a new export format (e.g., CSV, JSON, XML) is introduced, rather than plugging in a new formatter interface (Violates Open/Closed Principle)",
                "A high-level `OrderProcessingService` instantiates a concrete `MySqlDatabaseConnection` directly in its constructor instead of receiving a `DatabaseInterface` via dependency injection (Violates Dependency Inversion Principle)",
                "A class defines private variables and exposes getters and setters to encapsulate its internal state"
            ],
            "answer": [0, 1, 2],
            "explanation": "Options 0, 1, and 2 are classic violations of LSP (derived class breaks base contract), OCP (core class is not closed for modification), and DIP (high-level policy depends on concrete low-level implementation). Option 3 describes standard encapsulation, which is a foundational OO principle and not a violation.",
            "why_wrong": {
                "3": "Encapsulating internal fields via accessors is standard object-oriented information hiding, not a violation of SOLID."
            },
            "source": "Software Engineering Concepts and Principles Lecture Notes; Martin (2002) Agile Software Development"
        },
        {
            "id": "sen201-ap-fc01",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "architecture"],
            "question": "What is the primary definition and role of Software Architecture?",
            "answer": "The high-level structure of a system, comprising software components, externally visible properties of those components, and the relationships among them. It establishes the technical foundation for non-functional properties (scalability, security, performance).",
            "explanation": "Architecture establishes early constraints and trade-offs before detailed coding begins.",
            "why_wrong": {},
            "source": "Sommerville Ch. 6"
        },
        {
            "id": "sen201-ap-fc02",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "patterns"],
            "question": "What is an Architectural Pattern?",
            "answer": "A stylized, reusable solution to a commonly occurring design problem in software architecture, providing structural templates and operating rules across different applications.",
            "explanation": "Examined in Nile University SEN 201 Final Exam Paper Type B Question 60.",
            "why_wrong": {},
            "source": "Nile Final Exam Paper Type B Q60"
        },
        {
            "id": "sen201-ap-fc03",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "cohesion"],
            "question": "What does High Cohesion mean in software design?",
            "answer": "It means all responsibilities, attributes, and methods within a module or class are closely related to a single well-defined purpose, making the component easier to understand, test, and maintain.",
            "explanation": "High cohesion reduces cognitive overhead and bug propagation.",
            "why_wrong": {},
            "source": "Software Engineering Concepts and Principles Lecture Notes"
        },
        {
            "id": "sen201-ap-fc04",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "coupling"],
            "question": "What does Loose Coupling mean, and why is it desirable?",
            "answer": "Modules have minimal, well-defined dependencies on each other's internal implementation details. It allows modifying or replacing one module with minimal risk of breaking others.",
            "explanation": "Loose coupling enables concurrent team development and modular testing.",
            "why_wrong": {},
            "source": "Software Engineering Concepts and Principles Lecture Notes"
        },
        {
            "id": "sen201-ap-fc05",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "pipe-and-filter"],
            "question": "What are the core characteristics of a Pipe-and-Filter architecture?",
            "answer": "Independent processing units (filters) transform sequential input streams and emit outputs into channels (pipes). Filters are stateless, decoupled, and unaware of upstream/downstream identities.",
            "explanation": "Examined in Nile University SEN 201 Final Exam Paper Type B Question 62.",
            "why_wrong": {},
            "source": "Nile Final Exam Paper Type B Q62"
        },
        {
            "id": "sen201-ap-fc06",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "repository"],
            "question": "What is the Repository (or Blackboard) architectural style, and what is its main drawback?",
            "answer": "A style where multiple independent subsystems share and exchange data via a central repository. Its main drawback is that the central repository is a single point of failure and bottleneck, and schema changes impact all subsystems.",
            "explanation": "Widely used in IDEs, CAD systems, and centralized databases.",
            "why_wrong": {},
            "source": "Sommerville Ch. 6"
        },
        {
            "id": "sen201-ap-fc07",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "solid", "dip"],
            "question": "State the Dependency Inversion Principle (the 'D' in SOLID).",
            "answer": "High-level policy modules should not depend on low-level implementation modules; both must depend on abstractions (interfaces). Abstractions should not depend on details; details should depend on abstractions.",
            "explanation": "DIP enables true modular decoupling and unit test mock injection.",
            "why_wrong": {},
            "source": "Software Engineering Concepts and Principles Lecture Notes"
        },
        {
            "id": "sen201-ap-fc08",
            "course": "SEN 201",
            "topic": "Software Architecture & Design Patterns",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "design-patterns", "observer"],
            "question": "What is the Observer design pattern, and when is it applied?",
            "answer": "A behavioral pattern defining a one-to-many relationship where a subject notifies all registered observers automatically whenever its internal state changes, without knowing their concrete classes.",
            "explanation": "Forms the foundation of event handling, reactive streams, and UI data-binding.",
            "why_wrong": {},
            "source": "GoF Design Patterns; Sommerville Ch. 6"
        }
    ],
    "case_studies": [
        {
            "id": "sen201-ap-cs01",
            "scenario": "Nile University's student registration portal was originally developed as a single PHP/MySQL script where UI HTML rendering, session authentication, grade computation, payment gateway API calls, and raw database queries were intermixed in 8,000 lines of code. During peak midterm enrollment, a crash in the payment gateway API handler caused total portal downtime, locking students out of submitting course registrations. Furthermore, calculating cumulative GPAs takes 45 seconds per query because calculations run synchronously inside the presentation loop. The university CTO has chartered an architectural overhaul.",
            "sub_questions": [
                {
                    "id": "sen201-ap-cs01-q1",
                    "course": "SEN 201",
                    "topic": "Software Architecture & Design Patterns",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case-study", "architectural-refactoring", "layered"],
                    "question": "Which architectural refactoring strategy will best isolate external third-party payment failures and prevent them from cascading into total portal downtime?",
                    "options": [
                        "Merging all database tables into a single large flat file to reduce query hops",
                        "Decomposing the monolith into a layered architecture with an asynchronous event-driven or adapter-isolated service layer for third-party integrations",
                        "Moving all PHP code directly into MySQL stored procedures",
                        "Converting the client browser into a fat client that writes directly to the production database via TCP sockets"
                    ],
                    "answer": 1,
                    "explanation": "Adopting a layered architecture and isolating the payment gateway behind a resilient service layer (using Adapter and asynchronous messaging / circuit breaker) prevents external gateway timeouts from blocking HTTP request threads and crashing the entire registration workflow.",
                    "why_wrong": {
                        "0": "A single flat file introduces extreme data corruption risks and eliminates ACID transactional safety.",
                        "2": "Moving business logic into stored procedures tightly couples logic to a specific database vendor and does not solve third-party API timeout crashes.",
                        "3": "Permitting client browsers to execute direct TCP socket writes to a production database is an catastrophic security vulnerability."
                    },
                    "source": "Sommerville Ch. 6; Case Study Synthesis"
                },
                {
                    "id": "sen201-ap-cs01-q2",
                    "course": "SEN 201",
                    "topic": "Software Architecture & Design Patterns",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case-study", "architectural-analysis", "caching"],
                    "question": "Explain how introducing a Repository pattern combined with an in-memory caching layer (e.g., Redis) resolves the 45-second GPA computation bottleneck, and state what cache invalidation policy must be applied.",
                    "marking_points": [
                        "Identifies that the Repository pattern abstracts data access away from business logic, centralizing query optimization and caching.",
                        "Explains that pre-computing or memoizing calculated GPAs into an in-memory cache eliminates repeated sequential full-table scans during peak concurrent traffic.",
                        "Specifies an exact cache invalidation trigger (e.g., invalidate or update cache entry when a lecturer uploads or amends an approved grade).",
                        "Notes the non-functional benefit: drastic reduction in database CPU contention and sub-second response times for student queries."
                    ],
                    "answer": "1. Architectural Abstraction: The Repository pattern encapsulates data retrieval logic, cleanly isolating GPA calculation rules from persistent storage.\n2. Caching Strategy: Because grade records are read far more frequently than they are updated, GPA results can be memoized in an in-memory cache (e.g., Redis), transforming expensive 45-second multi-table aggregation queries into sub-millisecond key-value lookups.\n3. Cache Invalidation Policy: The cache must use write-through or event-driven invalidation—whenever a lecturer submits or modifies a grade in the Academic Records subsystem, the cached GPA entry for affected students is invalidated and recalculated.\n4. Non-Functional Impact: Relieves database lock contention and guarantees consistent sub-second page loads during peak registration.",
                    "explanation": "Separating calculation logic from direct disk storage via repository caching ensures high availability and eliminates recalculation storms.",
                    "why_wrong": {},
                    "source": "Sommerville Ch. 6; Architecture Case Studies"
                }
            ]
        },
        {
            "id": "sen201-ap-cs02",
            "scenario": "A Nigerian FinTech unicorn processes 4,000 card transactions per second. Each incoming transaction payload must undergo five distinct checks before authorization: (1) schema format validation, (2) blacklist fraud phone check, (3) AI behavioral anomaly scoring, (4) ledger balance check, and (5) cryptographic token generation. The transaction screening engine must achieve an end-to-end response time of under 120ms. The engineering team is debating between a centralized Repository (Blackboard) architecture and a Pipe-and-Filter streaming architecture.",
            "sub_questions": [
                {
                    "id": "sen201-ap-cs02-q1",
                    "course": "SEN 201",
                    "topic": "Software Architecture & Design Patterns",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case-study", "pipe-and-filter", "performance"],
                    "question": "Why is the Pipe-and-Filter architectural style vastly superior to a centralized Repository style for this high-throughput transaction screening pipeline?",
                    "options": [
                        "Because Pipe-and-Filter eliminates all database storage permanently",
                        "Because each screening filter operates independently as a decoupled stage in a streaming pipeline, allowing concurrent parallel execution across CPU cores without database locking bottlenecks",
                        "Because Pipe-and-Filter requires no communication channels between software components",
                        "Because Pipe-and-Filter forces all 5 steps to execute in a single blocking thread on one machine"
                    ],
                    "answer": 1,
                    "explanation": "Pipe-and-Filter allows each screening step (validation, blacklist, AI scoring, balance check, tokenization) to run as an autonomous filter. Streams of transactions pass through buffer pipes, allowing pipeline parallelism without contending for locks on a single centralized repository database.",
                    "why_wrong": {
                        "0": "Pipe-and-Filter does not eliminate databases; downstream filters still commit final ledger updates to persistent storage.",
                        "2": "Pipe-and-Filter explicitly relies on communication channels (pipes) between filters.",
                        "3": "Pipe-and-Filter enables concurrency and multi-threaded pipelining, the exact opposite of single-threaded blocking."
                    },
                    "source": "Nile Final Exam Paper Type B Q62; Sommerville Ch. 6"
                },
                {
                    "id": "sen201-ap-cs02-q2",
                    "course": "SEN 201",
                    "topic": "Software Architecture & Design Patterns",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case-study", "design-patterns", "strategy-pattern"],
                    "question": "The fraud detection team regularly deploys new AI fraud scoring algorithms (e.g., Random Forest, Gradient Boosted Trees, Neural Net) depending on shifting fraudulent patterns. Explain how applying the Strategy Design Pattern within the AI scoring filter satisfies the Open/Closed Principle (OCP).",
                    "marking_points": [
                        "Defines the Strategy Pattern: Encapsulates a family of algorithms behind a common interface, making them interchangeable at runtime.",
                        "States the OCP requirement: Software entities should be open for extension (adding new fraud detection models) but closed for modification (not editing existing transaction pipeline code).",
                        "Explains concrete implementation: An `IFraudScorer` interface with a `score(Transaction t)` method; concrete classes (`RandomForestScorer`, `NeuralNetScorer`) implement it.",
                        "Demonstrates that new fraud models can be added dynamically without altering the transaction pipeline or restarting running services."
                    ],
                    "answer": "1. Strategy Pattern Definition: Encapsulates the algorithmic scoring logic behind an abstract interface (e.g., `IFraudScoringStrategy`), allowing concrete scoring algorithms to be swapped seamlessly without altering the client filter.\n2. Conformance to Open/Closed Principle: The transaction pipeline filter is 'closed for modification' because its orchestration code never needs to be edited or recompiled when new fraud heuristics emerge. It is 'open for extension' because data scientists can implement a new class (e.g., `DeepNeuralScorer`) implementing the interface.\n3. Runtime Dynamic Selection: The pipeline can dynamically switch or A/B test fraud scoring models based on merchant category or transaction risk profile without system downtime or code regression.",
                    "explanation": "The Strategy pattern decouples algorithmic variations from execution infrastructure, ensuring clean OCP compliance.",
                    "why_wrong": {},
                    "source": "GoF Design Patterns; Sommerville Ch. 6"
                }
            ]
        }
    ]
}

out_file = r"c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content\SEN 201\architecture_patterns.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(topic_data, f, indent=2)

print(f"Successfully generated {out_file} with {len(topic_data['questions']) + sum(len(cs['sub_questions']) for cs in topic_data.get('case_studies', []))} total questions.")
