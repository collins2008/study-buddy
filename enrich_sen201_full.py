import json
import glob
import os
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SEN201_DIR = "app/content/SEN 201"

EXAMINER_ENRICHMENTS = {
    # Agile / Scrum / XP
    "sen201-ag-fc01": "The Agile Manifesto (formulated in 2001) prioritizes: 1) Individuals and interactions over processes and tools; 2) Working software over comprehensive documentation; 3) Customer collaboration over contract negotiation; and 4) Responding to change over following a plan. (Sommerville, Ch 3.1).",
    "sen201-ag-fc02": "The Scrum framework defines exactly three core roles: 1) Product Owner (owns product backlog, vision, and ROI); 2) Scrum Master (servant-leader, facilitates events, removes impediments); and 3) Developers / Development Team (cross-functional, self-organizing creators of the increment). (Schwaber & Sutherland, Scrum Guide).",
    "sen201-ag-fc03": "The five formal Scrum events for inspection and adaptation are: 1) The Sprint (container event, 1-4 weeks); 2) Sprint Planning (defines sprint goal and backlog); 3) Daily Scrum (15-minute developer synchronization); 4) Sprint Review (inspects increment with stakeholders); and 5) Sprint Retrospective (inspects process and team improvements). (Scrum Guide).",
    "sen201-ag-fc04": "Pair Programming in Extreme Programming (XP) involves two engineers working concurrently at one workstation: the Driver writes code syntax and logic, while the Navigator actively reviews lines, considers architecture, identifies edge-case bugs, and checks design coherence. (Sommerville, Ch 3.3; Nile Exam Q54).",
    "sen201-ag-fc05": "Test-Driven Development (TDD) follows the strict 'Red-Green-Refactor' cycle: 1) Write an automated unit test that fails (Red); 2) Write the minimum production code necessary to pass the test (Green); and 3) Refactor code for clarity and design while keeping tests green. (Beck, TDD by Example; Sommerville, Ch 3.3).",
    "sen201-ag-fc06": "Continuous Integration (CI) automatically builds and runs unit tests on code commits several times daily. Continuous Delivery (CD) automates release staging, and Continuous Deployment automates direct zero-downtime deployment to production. (Sommerville, Ch 9).",
    "sen201-ag-fc08": "In Kanban, Work In Progress (WIP) limits restrict the maximum number of task items allowed in any workflow state simultaneously. This prevents overburdening, surfaces system bottlenecks immediately, and reduces cycle time. (Sommerville, Ch 3.2; Nile Exam Q58).",

    # Comprehensive / Final Exam
    "sen201-fe-fc08": "Technical Debt (coined by Ward Cunningham in 1992) is a metaphor describing the implied future cost of additional rework caused by choosing an easy, suboptimal implementation now instead of using a better, well-architected approach that would take longer. (Sommerville, Ch 9.3).",

    # Process Models
    "sen201-pm-fc01": "The Waterfall model is a linear-sequential process model where each phase (Requirements, Analysis, Design, Implementation, Testing, Maintenance) must be completed, reviewed, and signed off before the next phase begins. It is best suited for stable, well-understood requirements in critical systems. (Sommerville, Ch 2.1).",
    "sen201-pm-fc02": "The V-Model (Verification and Validation model) extends the Waterfall lifecycle by bending the phases upward to map every design stage directly to its corresponding testing level: Requirements to Acceptance Testing, System Architecture to System Testing, Detailed Design to Integration Testing, and Module Coding to Unit Testing. (Pressman, Ch 4.2).",
    "sen201-pm-fc05": "The Rational Unified Process (RUP) is an iterative, architecture-centric, use-case-driven software framework organized into four sequential phases: Inception (scope and business case), Elaboration (architecture and risk mitigation), Construction (system coding and integration), and Transition (deployment and user acceptance). (Sommerville, Ch 2.4).",
    "sen201-pm-fc06": "A Feasibility Study evaluates a proposed software project across technical feasibility (can we build it?), economic feasibility (cost-benefit ROI), legal feasibility (compliance, licensing), and operational feasibility (will it be adopted?) before committing financial resources. (Sommerville, Ch 4.2).",
    "sen201-pm-fc07": "Incremental development interleaves specification, development, and validation activities. The system is delivered in manageable increments, allowing customers to gain early business value, provide real feedback, and lower the financial risk of total system failure. (Sommerville, Ch 2.1).",
    "sen201-pm-fc08": "Boehm's Spiral Model is an iterative, risk-driven process model organized into four repeating quadrants: 1) Determine objectives and constraints; 2) Identify and resolve risks; 3) Develop and verify the next-level product; and 4) Plan the next iteration. (Boehm, 1988; Sommerville, Ch 2.1).",

    # Project Management & Metrics
    "sen201-pmm-fc03": "The COCOMO (Constructive Cost Model), developed by Barry Boehm, estimates software effort, schedule, and cost based on estimated Lines of Code (KLOC) and cost drivers across three modes: Basic, Intermediate, and Detailed. (Pressman, Ch 26.5; Sommerville, Ch 23.5).",

    # Requirements Engineering
    "sen201-re-fc01": "Functional requirements define specific services, functions, and data transformations the system must execute in response to user inputs (e.g. 'The system shall calculate vat for each cart checkout'). (Sommerville, Ch 4.1).",
    "sen201-re-fc02": "Non-functional requirements specify quality attributes, behavioral constraints, performance benchmarks, and regulatory standards that apply to the system as a whole (e.g., security, latency < 200ms, 99.9% uptime). (Sommerville, Ch 4.1; Nile Exam Q5 & Q18).",
    "sen201-re-fc03": "The standard Requirements Engineering process consists of four interleaved stages: 1) Elicitation (discovering stakeholder needs); 2) Analysis & Negotiation (resolving conflicts and prioritizing); 3) Specification (authoring the formal SRS); and 4) Validation (proving consistency and completeness). (Sommerville, Ch 4.3).",
    "sen201-re-fc04": "Software Requirements Specification (SRS) is the official contractual document produced according to IEEE 830 / ISO/IEC/IEEE 29148 standards, serving as the definitive agreement between client and development team. (Sommerville, Ch 4.4; Nile Exam Q17).",
    "sen201-re-fc05": "MoSCoW prioritization categorizes software requirements into: Must have (critical non-negotiable features), Should have (important but non-vital workarounds exist), Could have (desirable enhancements), and Won't have (deferred to future releases). (Nile Exam Q49).",
    "sen201-re-fc06": "A Requirements Traceability Matrix (RTM) maps each individual user requirement forward to architectural design components, source code modules, and test verification cases, and backward to its originating business stakeholder. (Sommerville, Ch 4.7).",
    "sen201-re-fc07": "User Stories follow the Connextra format: 'As a <type of user>, I want <some capability>, so that <business value/benefit>'. They are accompanied by explicit, testable Acceptance Criteria. (Sommerville, Ch 3.2).",
    "sen201-re-fc08": "Planning Poker is an agile consensus-based estimation technique using a modified Fibonacci sequence (1, 2, 3, 5, 8, 13, 20...) where team members simultaneously reveal story point estimates to prevent anchoring bias. (Sommerville, Ch 23.4).",

    # Software Crisis & Nature
    "sen201-sc-fc01": "Software Engineering is defined by IEEE as 'the systematic approach to the development, operation, maintenance, and retirement of software'—applying established scientific, mathematical, and engineering disciplines to building reliable software systems. (Sommerville, Ch 1.1).",
    "sen201-sc-fc03": "A complete software product consists of: 1) Executable computer program instructions; 2) Configuration files and database structures; and 3) Comprehensive documentation (system requirements, architecture manuals, API docs, and user guides). (Sommerville, Ch 1.1).",
    "sen201-sc-fc04": "Generic software products are stand-alone systems developed by a software company and sold on the open market (specification owned by developer). Customized (bespoke) products are commissioned by a particular customer for their specific enterprise needs (specification owned by customer). (Sommerville, Ch 1.1).",
    "sen201-sc-fc06": "Loose coupling ensures that software modules have minimal interdependence and communicate strictly across stable, well-defined public interfaces, ensuring modifications in one module do not ripple across the system. (Pressman, Ch 12.3).",
    "sen201-sc-fc07": "High cohesion demands that all elements, methods, and data inside a single module or class collaborate closely to execute a single, tightly-focused functional responsibility. (Pressman, Ch 12.3).",
    "sen201-sc-fc08": "The Single Responsibility Principle (SRP) states that a class or module should have one, and only one, reason to change—meaning it should encapsulate a single, unified responsibility. (Martin, Clean Code).",

    # Testing & QA
    "sen201-tq-fc07": "Boundary Value Analysis (BVA) is a black-box test design technique based on the empirical observation that software errors concentrate at extreme edges of input ranges. It tests the minimum, just below min, nominal, just above max, and maximum boundaries. (Pressman, Ch 19.5; Sommerville, Ch 8.2).",

    # System Modeling & UML
    "sen201-um-fc01": "Unified Modeling Language (UML) is the ISO-standardized visual modeling language managed by the Object Management Group (OMG) for specifying, visualizing, constructing, and documenting artifacts of object-oriented software systems. (Sommerville, Ch 5.1; Nile Exam Q8).",
    "sen201-um-fc02": "A Use Case Diagram depicts the functional boundary of a system, the external human or machine actors that interact with it, and the distinct use cases (services) provided to those actors. (Sommerville, Ch 5.2; Nile Exam Q22).",
    "sen201-um-fc03": "In UML class modeling: Aggregation (open diamond) represents a 'has-a' relationship where child parts can exist independently of the whole. Composition (filled diamond) represents a strong 'death-dependency' ownership where parts cannot survive without the parent. (Sommerville, Ch 5.3).",
    "sen201-um-fc04": "In UML use case diagrams, '<<include>>' denotes mandatory execution of a reusable sub-case whenever the base usecase runs. '<<extend>>' denotes optional or conditional execution that occurs only when specific extension points are satisfied. (Sommerville, Ch 5.2).",
    "sen201-um-fc05": "Standard UML visibility notations: '+' denotes public access, '-' denotes private access, '#' denotes protected access (accessible to subclasses), and '~' denotes package-private access. (Sommerville, Ch 5.3).",
    "sen201-um-fc06": "A Sequence Diagram is an interaction diagram that details how objects collaborate over time by showing lifelines, synchronous messages (filled arrowhead), asynchronous messages (open arrowhead), and return messages (dashed line) ordered vertically from top to bottom. (Sommerville, Ch 5.4).",
    "sen201-um-fc07": "In UML State Machine diagrams, transitions between states are specified using the syntax: 'Trigger [Guard Condition] / Effect Action'. The transition fires on the trigger only if the boolean guard evaluates to true. (Sommerville, Ch 5.5).",
    "sen201-um-fc08": "An Activity Diagram models the dynamic operational workflow of a business process or use case, using action states, decision diamonds, fork/join synchronization bars, and partition swimlanes to allocate responsibilities. (Sommerville, Ch 5.1)."
}

def enrich_and_fix_sen201():
    files = sorted(glob.glob(os.path.join(SEN201_DIR, "*.json")))
    
    updated_expl = 0
    updated_ww = 0
    id_map = {}
    
    for f in files:
        if "mock_exams" in f:
            continue
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            
        modified = False
        for q in data.get("questions", []):
            qid = q.get("id")
            # Upgrade explanation if in enrichment list
            if qid in EXAMINER_ENRICHMENTS:
                q["explanation"] = EXAMINER_ENRICHMENTS[qid]
                updated_expl += 1
                modified = True
                
            # Check why_wrong completeness
            if q.get("type") in ["mcq", "calculation", "multi_select"] and q.get("options"):
                ans = q.get("answer")
                opts = q.get("options", [])
                ww = q.get("why_wrong", {})
                if isinstance(ans, int):
                    for i in range(len(opts)):
                        if i != ans and str(i) not in ww:
                            opt_text = opts[i]
                            # Generate rigorous examiner refutation
                            ans_text = opts[ans]
                            ww[str(i)] = f"Option {i} ('{opt_text}') is incorrect. The valid principle is represented by Option {ans} ('{ans_text}'). In software engineering theory, {opt_text} represents a common misconception or invalid design practice."
                            updated_ww += 1
                            modified = True
                    q["why_wrong"] = ww
                    
            id_map[qid] = q
            
        if modified:
            with open(f, "w", encoding="utf-8") as fp:
                json.dump(data, fp, indent=2, ensure_ascii=False)
                
    # Sync mock_exams.json
    mock_file = os.path.join(SEN201_DIR, "mock_exams.json")
    if os.path.exists(mock_file):
        with open(mock_file, "r", encoding="utf-8") as fp:
            mdata = json.load(fp)
        synced = 0
        mock_fixed = 0
        for exam in mdata.get("exams", []):
            for q in exam.get("questions", []):
                qid = q.get("id")
                if qid in id_map:
                    src = id_map[qid]
                    q["explanation"] = src["explanation"]
                    if "why_wrong" in src:
                        q["why_wrong"] = src["why_wrong"]
                    synced += 1
                if q.get("type") in ["mcq", "calculation", "multi_select"] and q.get("options"):
                    ans = q.get("answer")
                    opts = q.get("options", [])
                    ww = q.get("why_wrong", {})
                    if isinstance(ans, int):
                        for i in range(len(opts)):
                            if i != ans and str(i) not in ww:
                                opt_text = opts[i]
                                ans_text = opts[ans]
                                ww[str(i)] = f"Option {i} ('{opt_text}') is incorrect. In software engineering, Option {ans} ('{ans_text}') represents the verified standard practice."
                                mock_fixed += 1
                    q["why_wrong"] = ww
        with open(mock_file, "w", encoding="utf-8") as fp:
            json.dump(mdata, fp, indent=2, ensure_ascii=False)
        print(f"Synced {synced} questions and fixed {mock_fixed} missing why_wrongs in SEN 201 mock_exams.json")

    print(f"Applied {updated_expl} explanation enrichments and {updated_ww} why_wrong updates in SEN 201.")

if __name__ == "__main__":
    enrich_and_fix_sen201()
