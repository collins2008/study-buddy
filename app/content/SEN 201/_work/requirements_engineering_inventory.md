# Exhaustive Topic Inventory: SEN 201 Topic 4
**Topic**: Requirements Engineering & Specification (`requirements_engineering.json`)
**Course**: SEN 201 — Introduction to Software Engineering (Nile University of Nigeria)
**Lecturer**: Yusuf Mshelia
**Sources**:
- `Software_Engineering_Concepts_and_Principles_Lecture_Notes (1).pdf`, Section 6
- Nile University 2024/2025 Final Examination Paper (Type B), Questions 5, 6, 16, 17, 18, 19, 20, 49
- IEEE 830 Recommended Practice for Software Requirements Specifications (SRS)

---

## 1. Requirements Classification
1. **Functional Requirements (FR)** (Nile Exam Q16):
   - Statements of services the system should provide, how the system should react to particular inputs, and how the system should behave in particular situations (e.g., "The system shall allow students to register for up to 24 credit units per semester").
2. **Non-Functional Requirements (NFR)** (Nile Exam Q5 & Q18):
   - Constraints on the services or functions offered by the system.
   - Categories:
     - Performance (response time $< 2$ seconds for 500 concurrent users).
     - Reliability (Mean Time Between Failures MTBF $> 1000$ hours).
     - Availability (99.9% uptime during exam registration week).
     - Security (AES-256 encryption at rest; multi-factor authentication for admins).
     - Usability, Portability, and Maintainability.
3. **Levels of Requirements**:
   - **Business Requirements** (Nile Exam Q19): High-level objectives and business goals of the sponsoring organization (why the system is being built).
   - **User Requirements** (Nile Exam Q20): Statements in natural language plus diagrams of the services the system provides and the operational tasks users can perform.
   - **System Requirements**: Detailed, technical specifications of the system's functions, services, and operational constraints for developers and testers (formal SRS).

---

## 2. Requirements Engineering Process
1. **Feasibility Study** (Nile Exam Q6):
   - Evaluates technical, economic, operational, schedule, and legal viability.
   - Determines: Is the system cost-effective and practical to build?
2. **Requirements Elicitation**:
   - Techniques: Interviews (structured/unstructured), Questionnaires/Surveys, Facilitated Workshops (Nile Exam Q44: collects input from many stakeholders simultaneously), Observation/Ethnography, Document Analysis, Prototyping.
3. **Requirements Analysis & Negotiation**:
   - Discovering boundaries, resolving conflicting stakeholder desires, identifying scope creep.
   - Prioritization: MoSCoW (Must have, Should have, Could have, Won't have this time).
4. **Requirements Specification**:
   - Documenting requirements in an SRS (Software Requirements Specification).
   - Format: Natural language sentences, structured tables, User Stories ("As a... I want... so that..."), and Use Cases.
5. **Requirements Validation**:
   - Reviews/Inspections, Walkthroughs, Prototyping, Test-case generation.
6. **Requirements Management**:
   - Controlling changes and establishing a Requirements Traceability Matrix (RTM) linking requirements to design, code, and test cases.

---

## 3. Characteristics of Good Requirements (Nile Exam Q17)
- **Unambiguous**: Only one interpretation is possible (Nile Exam Q17: "Ambiguous" is NOT a characteristic of good requirements).
- **Verifiable / Testable**: A quantified metric exists by which a tester can conclusively verify conformance (e.g. replacing "system must be fast" with "95% of queries complete in $< 2$ seconds under 500 concurrent user load").
- **Complete**: All necessary constraints and behaviors are specified.
- **Consistent**: No requirements contradict one another.
- **Traceable**: Assigned a unique identifier (FR-01, NFR-02) and traceable to business needs, architecture components, and test cases.

---

## 4. Scope Creep (Nile Exam Q49)
- Uncontrolled, continuous expansion of project scope beyond original agreed boundaries without adjustments to time, cost, and resources.
