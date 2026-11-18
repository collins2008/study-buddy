import json
import os

topic_data = {
    "course": "SEN 201",
    "topic": "Software Project Management, Metrics & Process Assessment",
    "summary": "Software project management encompasses the organizational planning, monitoring, and governance required to deliver complex software systems within scope, time, and budget constraints. Project scheduling utilizes the Work Breakdown Structure (WBS) and the Critical Path Method (CPM) to identify project bottlenecks and slack times. Algorithmic cost estimation is anchored by Barry Boehm's COCOMO model, which categorizes projects into Organic, Semi-detached, and Embedded modes based on team familiarity and regulatory constraints. Software Configuration Management (SCM) establishes formal baselines, version control, and Change Control Board (CCB) reviews to prevent scope creep and manage artifact evolution. Organizational capability is evaluated through standardized process maturity frameworks, notably CMMI's five progressive levels (Initial, Managed, Defined, Quantitatively Managed, and Optimizing) and ISO/IEC 15504 (SPICE).",
    "key_terms": [
        {
            "term": "Software Configuration Management (SCM)",
            "definition": "A disciplined engineering process that manages, controls, and audits changes to all software work products (source code, documentation, test suites, schemas) across the system lifecycle."
        },
        {
            "term": "Scope Creep",
            "definition": "The uncontrolled, incremental expansion of project requirements or features without corresponding adjustments to time, budget, or engineering resources."
        },
        {
            "term": "COCOMO (Constructive Cost Model)",
            "definition": "An algorithmic software cost estimation model developed by Barry Boehm that calculates effort (in person-months) and schedule duration from size (KLOC) and cost drivers."
        },
        {
            "term": "Critical Path Method (CPM)",
            "definition": "A project modeling technique that identifies the longest sequence of dependent activities and the minimum time required to complete the total project, where activities have zero float (slack)."
        },
        {
            "term": "Baseline",
            "definition": "A formally reviewed and agreed-upon version of a configuration item that serves as the official foundation for subsequent development and can only be altered through formal change control."
        },
        {
            "term": "Change Control Board (CCB)",
            "definition": "A designated group of stakeholders responsible for reviewing, evaluating, approving, or rejecting proposed modifications to baselined software artifacts."
        },
        {
            "term": "CMMI Maturity Levels",
            "definition": "A five-level process improvement framework (1: Initial, 2: Managed, 3: Defined, 4: Quantitatively Managed, 5: Optimizing) assessing an organization's software engineering capability."
        },
        {
            "term": "Risk Exposure",
            "definition": "A quantitative measure of risk severity computed as the product of the probability of occurrence and the total financial or operational impact if the risk materializes: Risk Exposure = Probability x Impact."
        }
    ],
    "questions": [
        {
            "id": "sen201-pm-001",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["scm", "version-control", "project-management", "nile-exam"],
            "question": "What is the primary role of Software Configuration Management (SCM) and version control in a multi-developer software project?",
            "options": [
                "To automatically generate business profit and loss statements",
                "To track, coordinate, control, and audit changes across all digital software artifacts, preventing code overwrites and establishing stable release baselines",
                "To eliminate the need for writing unit and regression tests",
                "To replace human software architects with automated database scripts"
            ],
            "answer": 1,
            "explanation": "As tested in Nile Final Exam Question 11 and lecturer notes, SCM and version management provide systematic tracking, branch management, auditing, and change control for software artifacts throughout development, preventing concurrent overwrites and maintaining reproducible baselines.",
            "why_wrong": {
                "0": "Profit and loss statements belong to financial accounting, not software configuration management.",
                "2": "SCM manages change history; it does not replace testing or verification.",
                "3": "SCM tools support developers; they do not replace system architects."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q11; Sommerville Ch. 25"
        },
        {
            "id": "sen201-pm-002",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["scope-creep", "change-control", "nile-exam"],
            "question": "During a 6-month software development project, the client continuously requests 'minor' additional features during informal weekly phone calls without adjusting the project budget or delivery date. By month 5, the team is 10 weeks behind schedule. What project management failure occurred, and what mechanism directly prevents it?",
            "options": [
                "Over-engineering; prevented by deleting all project documentation",
                "Scope creep; prevented by establishing a formal Change Control Board (CCB) and change impact analysis procedures",
                "Excessive testing; prevented by releasing code directly to production without testing",
                "Improper compiler optimization; prevented by upgrading to a faster CPU"
            ],
            "answer": 1,
            "explanation": "Nile Final Exam Question 49 defines scope creep as the uncontrolled, gradual addition of features without adjusting time, budget, or resources. It is mitigated by enforcing formal change management: all requests must undergo impact analysis and obtain Change Control Board (CCB) approval.",
            "why_wrong": {
                "0": "Deleting documentation increases confusion and does not control requirement changes.",
                "2": "Skipping testing causes catastrophic quality failures and does not prevent scope growth.",
                "3": "Hardware upgrades cannot resolve unmanaged human requirement additions."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q49; Sommerville Ch. 22"
        },
        {
            "id": "sen201-pm-003",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["cocomo", "cost-estimation", "project-planning"],
            "question": "In Barry Boehm's COCOMO (Constructive Cost Model), what distinguishes an 'Embedded Mode' project from an 'Organic Mode' project?",
            "options": [
                "Embedded projects are small web apps built by 2 students with zero hardware constraints",
                "Embedded projects operate within tight, inflexible hardware and regulatory constraints with complex operational interfaces, requiring significantly higher effort per line of code than Organic projects",
                "Embedded projects are written exclusively in HTML/CSS",
                "Embedded projects do not require software testing or project management"
            ],
            "answer": 1,
            "explanation": "In COCOMO, projects are classified into Organic (small, experienced teams with flexible constraints), Semi-detached (intermediate complexity), and Embedded (rigid hardware/software constraints, strict regulatory standards, e.g., avionics or medical devices). Embedded projects exhibit much higher exponent factors (b=1.20 vs b=1.05) representing steep diseconomies of scale.",
            "why_wrong": {
                "0": "Small web apps built with flexible requirements represent the Organic mode.",
                "2": "Embedded projects often use Ada, C, or C++ and involve complex embedded systems, not pure HTML/CSS.",
                "3": "Embedded systems require the most stringent, rigorous verification and project management."
            },
            "source": "Boehm (1981) Software Engineering Economics; Sommerville Ch. 23"
        },
        {
            "id": "sen201-pm-004",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["cocomo", "calculation", "estimation"],
            "question": "Using Basic COCOMO for an Organic software project where Effort = 2.4 * (KLOC)^1.05 Person-Months, estimate the development effort required for a project estimated at 10 KLOC (given 10^1.05 ≈ 11.22):",
            "options": [
                "10.0 Person-Months",
                "26.9 Person-Months",
                "112.2 Person-Months",
                "240.0 Person-Months"
            ],
            "answer": 1,
            "explanation": "Applying the Basic COCOMO Organic formula: Effort = 2.4 * (10)^1.05 = 2.4 * 11.22 = 26.928 Person-Months (approximately 26.9 PM).",
            "why_wrong": {
                "0": "10.0 PM assumes a 1:1 linear mapping of 1 PM per KLOC, completely ignoring the formula constants.",
                "2": "112.2 PM neglects multiplying by the constant a = 2.4.",
                "3": "240.0 PM incorrectly multiplies 2.4 * 10 * 10 without proper power evaluation."
            },
            "source": "Software Engineering Concepts and Principles Lecture Notes; Sommerville Ch. 23"
        },
        {
            "id": "sen201-pm-005",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "matching",
            "difficulty": 3,
            "tags": ["cmmi", "process-models", "matching"],
            "question": "Match each of the 5 CMMI Maturity Levels to its defining organizational characteristic:",
            "options": [
                {"left": "Level 1: Initial", "right": "Processes are unpredictable, ad-hoc, and chaotic; success depends on individual heroics"},
                {"left": "Level 2: Managed", "right": "Basic project management is established; processes are planned and monitored at the project level"},
                {"left": "Level 3: Defined", "right": "Standard processes are characterized, documented, and integrated across the entire organization"},
                {"left": "Level 4: Quantitatively Managed", "right": "Process performance is controlled using statistical and quantitative measurement techniques"},
                {"left": "Level 5: Optimizing", "right": "Continuous process improvement is institutionalized through quantitative feedback and innovative piloting"}
            ],
            "answer": [
                {"left": "Level 1: Initial", "right": "Processes are unpredictable, ad-hoc, and chaotic; success depends on individual heroics"},
                {"left": "Level 2: Managed", "right": "Basic project management is established; processes are planned and monitored at the project level"},
                {"left": "Level 3: Defined", "right": "Standard processes are characterized, documented, and integrated across the entire organization"},
                {"left": "Level 4: Quantitatively Managed", "right": "Process performance is controlled using statistical and quantitative measurement techniques"},
                {"left": "Level 5: Optimizing", "right": "Continuous process improvement is institutionalized through quantitative feedback and innovative piloting"}
            ],
            "explanation": "The staged CMMI model defines five progressive maturity levels evaluating organizational engineering rigor from ad-hoc chaos (Level 1) to continuous quantitative optimization (Level 5).",
            "why_wrong": {},
            "source": "Software Process Assessment Models PDF; SEI CMMI Framework"
        },
        {
            "id": "sen201-pm-006",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "sequencing",
            "difficulty": 2,
            "tags": ["risk-management", "lifecycle", "sequencing"],
            "question": "Order the four stages of the Software Risk Management process in chronological sequence from first to last:",
            "options": [
                "Risk Identification (discovering potential project, product, and business risks)",
                "Risk Analysis & Evaluation (assessing probability of occurrence and severity of impact)",
                "Risk Planning (formulating avoidance, mitigation, and contingency strategies)",
                "Risk Monitoring (continuously tracking risk indicators and trigger conditions)"
            ],
            "answer": [
                "Risk Identification (discovering potential project, product, and business risks)",
                "Risk Analysis & Evaluation (assessing probability of occurrence and severity of impact)",
                "Risk Planning (formulating avoidance, mitigation, and contingency strategies)",
                "Risk Monitoring (continuously tracking risk indicators and trigger conditions)"
            ],
            "explanation": "Standard risk management follows a sequential lifecycle: first identify potential risks, analyze their probability and impact, plan responses/mitigations, and monitor risk triggers throughout project execution.",
            "why_wrong": {},
            "source": "Sommerville Ch. 22; Software Engineering Concepts and Principles Lecture Notes"
        },
        {
            "id": "sen201-pm-007",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["cpm", "scheduling", "critical-path"],
            "question": "In a Critical Path Method (CPM) project activity network, what is the defining characteristic of an activity that lies on the 'critical path'?",
            "options": [
                "It has the largest float (slack time) in the entire project schedule",
                "It has exactly zero float (slack time), meaning any delay in this activity will directly delay the overall project completion date",
                "It is always assigned to the most junior programmer",
                "It can be delayed by 6 months without affecting project delivery"
            ],
            "answer": 1,
            "explanation": "The critical path represents the longest sequence of dependent activities required to complete the project. Every activity on the critical path has zero slack (float); any delay on the critical path immediately causes a day-for-day delay in the total project completion deadline.",
            "why_wrong": {
                "0": "Critical path activities have zero float, not the largest float.",
                "2": "Critical path tasks are typically assigned to senior engineers because delays jeopardize project delivery.",
                "3": "Any delay on the critical path delays the final delivery date."
            },
            "source": "Software Engineering Concepts and Principles Lecture Notes; Sommerville Ch. 22"
        },
        {
            "id": "sen201-pm-008",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "multi_select",
            "difficulty": 3,
            "tags": ["ccb", "change-control", "scm"],
            "question": "Which of the following are primary duties and governance responsibilities of a Software Change Control Board (CCB)? (Select ALL that apply)",
            "options": [
                "Evaluating the technical feasibility, cost, schedule impact, and architectural risk of requested changes to baselined artifacts",
                "Formally approving, deferring, or rejecting submitted change requests",
                "Writing the machine-level assembly instructions for low-level memory allocation",
                "Ensuring that approved changes are systematically tracked, audited, and scheduled into specific release versions"
            ],
            "answer": [0, 1, 3],
            "explanation": "The Change Control Board (CCB) is a governance committee composed of managers, engineers, and clients responsible for assessing change impacts, approving/rejecting change requests, and scheduling approved changes into formal releases. Writing assembly instructions is developer implementation work, not CCB governance.",
            "why_wrong": {
                "2": "Writing assembly code is a low-level implementation programming task performed by developers, not a CCB management function."
            },
            "source": "Sommerville Ch. 25; Software Engineering Concepts and Principles Lecture Notes"
        },
        {
            "id": "sen201-pm-fc01",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "project-management"],
            "question": "What is the Software Project Management 'Triple Constraint' (Iron Triangle)?",
            "answer": "Scope, Time (Schedule), and Cost (Budget), with Quality at the center. Modifying any one constraint unavoidably impacts the other two.",
            "explanation": "Core project management framework across all engineering disciplines.",
            "why_wrong": {},
            "source": "Software Engineering Concepts and Principles Lecture Notes"
        },
        {
            "id": "sen201-pm-fc02",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "wbs"],
            "question": "What is a Work Breakdown Structure (WBS)?",
            "answer": "A hierarchical decomposition of the total scope of work to be carried out by the project team to accomplish project objectives and create required deliverables.",
            "explanation": "Forms the foundation for work packages, cost estimation, and schedule allocation.",
            "why_wrong": {},
            "source": "Sommerville Ch. 22"
        },
        {
            "id": "sen201-pm-fc03",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "cocomo"],
            "question": "What are the three project modes in the Basic COCOMO estimation model?",
            "answer": "1. Organic (small, experienced teams with flexible constraints),\n2. Semi-detached (medium teams with mixed experience and moderate constraints),\n3. Embedded (rigid hardware/software constraints and strict operational requirements).",
            "explanation": "Formulated by Barry Boehm in 1981.",
            "why_wrong": {},
            "source": "Boehm (1981); Sommerville Ch. 23"
        },
        {
            "id": "sen201-pm-fc04",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "cpm"],
            "question": "What is the Critical Path in project scheduling?",
            "answer": "The sequence of dependent tasks that forms the longest path through the activity network, determining the minimum total project duration. Tasks on this path have zero float (slack).",
            "explanation": "A delay in any critical path task immediately delays final delivery.",
            "why_wrong": {},
            "source": "Sommerville Ch. 22"
        },
        {
            "id": "sen201-pm-fc05",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "scm"],
            "question": "What is Software Configuration Management (SCM)?",
            "answer": "A disciplined engineering process that controls, tracks, and audits changes to all software artifacts (code, documentation, models, schemas) throughout the software lifecycle.",
            "explanation": "Examined in Nile University SEN 201 Final Exam Paper Type B Question 11.",
            "why_wrong": {},
            "source": "Nile Final Exam Paper Type B Q11"
        },
        {
            "id": "sen201-pm-fc06",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "baseline"],
            "question": "What is a 'Baseline' in Software Configuration Management?",
            "answer": "A formally reviewed and agreed-upon version of a configuration item that serves as the official foundation for subsequent development, modifiable only through formal change control.",
            "explanation": "Examples include the approved SRS, architectural baseline, and release builds.",
            "why_wrong": {},
            "source": "Software Engineering Concepts and Principles Lecture Notes"
        },
        {
            "id": "sen201-pm-fc07",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "cmmi"],
            "question": "Contrast CMMI Maturity Level 1 (Initial) with Level 5 (Optimizing).",
            "answer": "Level 1 (Initial): Processes are ad-hoc, chaotic, and unpredictable; success depends on individual heroic effort.\nLevel 5 (Optimizing): The organization focuses on continuous process improvement using quantitative statistical feedback and innovative piloting.",
            "explanation": "Represents the opposite ends of the CMMI process maturity spectrum.",
            "why_wrong": {},
            "source": "Software Process Assessment Models PDF"
        },
        {
            "id": "sen201-pm-fc08",
            "course": "SEN 201",
            "topic": "Software Project Management, Metrics & Process Assessment",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "risk-exposure"],
            "question": "How is Risk Exposure calculated, and how is it used?",
            "answer": "Risk Exposure = Probability of Occurrence x Financial/Schedule Impact. It allows project managers to rank risks objectively and allocate mitigation resources to the highest-severity items first.",
            "explanation": "Essential metric for risk prioritization and quantitative risk assessment.",
            "why_wrong": {},
            "source": "Sommerville Ch. 22"
        }
    ],
    "case_studies": [
        {
            "id": "sen201-pm-cs01",
            "scenario": "A Nigerian fintech startup is building a multi-currency mobile payment wallet. The project network consists of three concurrent activity paths: Path 1: UI/UX Wireframing -> Mobile Client Dev (10 weeks); Path 2: Microservice Backend Architecture -> Payment API Integration -> Security Penetration Testing (16 weeks); Path 3: Regulatory Compliance Filing -> Bank Partner KYC Integration (12 weeks). The total project launch is scheduled for 16 weeks. During week 8, the lead backend engineer contracts malaria, causing the Payment API Integration activity to be delayed by 3 weeks.",
            "sub_questions": [
                {
                    "id": "sen201-pm-cs01-q1",
                    "course": "SEN 201",
                    "topic": "Software Project Management, Metrics & Process Assessment",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case-study", "cpm", "critical-path"],
                    "question": "What is the critical path of the project, and what is the direct impact of the 3-week delay in Payment API Integration?",
                    "options": [
                        "Path 1 is the critical path; the delay has zero impact on the overall launch date",
                        "Path 2 is the critical path (16 weeks); because it has zero slack, the 3-week delay directly pushes the overall project launch date from week 16 to week 19",
                        "Path 3 is the critical path; the delay reduces project cost by 50%",
                        "Path 2 has 6 weeks of slack time; the project will finish 3 weeks early"
                    ],
                    "answer": 1,
                    "explanation": "Path 2 is the longest sequence (16 weeks) and represents the critical path with zero float (slack). Any delay on the critical path propagates directly to the final completion deadline, delaying delivery from 16 to 19 weeks unless schedule compression is applied.",
                    "why_wrong": {
                        "0": "Path 1 is only 10 weeks, meaning it has 6 weeks of float; Path 2 is the critical path.",
                        "2": "Path 3 is 12 weeks, which is shorter than Path 2 (16 weeks).",
                        "3": "Critical path activities have zero slack, never 6 weeks."
                    },
                    "source": "Sommerville Ch. 22; CPM Project Case Studies"
                },
                {
                    "id": "sen201-pm-cs01-q2",
                    "course": "SEN 201",
                    "topic": "Software Project Management, Metrics & Process Assessment",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case-study", "schedule-compression", "crashing-fast-tracking"],
                    "question": "To recover the 3-week delay and meet the contractual 16-week launch deadline, contrast the two schedule compression techniques—'Crashing' and 'Fast-Tracking'—and evaluate their specific risks for this fintech project.",
                    "marking_points": [
                        "Defines Crashing: Adding extra resources (overtime, bringing in senior contract developers) to critical path activities to shorten duration.",
                        "Identifies Crashing Risks: Increased project costs and Brook's Law risk ('adding manpower to a late software project makes it later' due to communication overhead).",
                        "Defines Fast-Tracking: Performing critical path activities in parallel that were originally planned in sequence (e.g., beginning security penetration testing concurrently with payment API integration).",
                        "Identifies Fast-Tracking Risks: Substantial rework risk and defect leakage if security flaws are uncovered in incomplete APIs."
                    ],
                    "answer": "1. Schedule Crashing: Involves injecting additional resources into critical path tasks (e.g., paying overtime or onboarding a senior contractor for API integration).\n- Risk: Substantially increases project costs. Furthermore, Brooks' Law states that adding developers to a late project can initially delay it further due to training and ramp-up communication overhead.\n2. Fast-Tracking: Involves executing sequential critical path activities concurrently (e.g., running security penetration testing in parallel while Payment API endpoints are still being completed).\n- Risk: Dramatically escalates defect and rework risks. If pen-testers find fundamental flaws in an evolving API, both the implementation and test harnesses must be completely rewritten, potentially corrupting payment security.\n3. Strategic Recommendation: Apply targeted crashing on well-defined isolated tasks rather than aggressive fast-tracking across safety-critical payment integration.",
                    "explanation": "Schedule compression requires balancing budget increases (crashing) against rework and defect risks (fast-tracking).",
                    "why_wrong": {},
                    "source": "Sommerville Ch. 22; PMBOK Schedule Management"
                }
            ]
        },
        {
            "id": "sen201-pm-cs02",
            "scenario": "A 100-developer enterprise software vendor fails an ISO 9001 and CMMI appraisal audit. The auditors discover that: (1) developers push unreviewed code directly into the production Git `main` branch; (2) requirements changes are communicated via Slack messages without formal logging; (3) different customers receive different, untracked binary builds containing unverified patches; and (4) when a critical regression occurs, the team cannot identify which code commit caused the failure or which customer received the affected version.",
            "sub_questions": [
                {
                    "id": "sen201-pm-cs02-q1",
                    "course": "SEN 201",
                    "topic": "Software Project Management, Metrics & Process Assessment",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case-study", "cmmi", "audit"],
                    "question": "Based on the auditor's findings, at which CMMI Maturity Level is this enterprise currently operating, and what is their immediate target level?",
                    "options": [
                        "Operating at Level 5 (Optimizing); target is Level 1",
                        "Operating at Level 1 (Initial); processes are chaotic and ad-hoc. The immediate target is Level 2 (Managed) to establish basic configuration management and project governance",
                        "Operating at Level 4 (Quantitatively Managed); target is Level 3",
                        "Operating at Level 3 (Defined); target is complete deregulation"
                    ],
                    "answer": 1,
                    "explanation": "Chaotic processes, direct unverified pushes to production, untracked releases, and reliance on individual ad-hoc communication characterize CMMI Maturity Level 1 (Initial). The organization must advance to Level 2 (Managed) by establishing disciplined project-level SCM, baseline control, and formal change tracking.",
                    "why_wrong": {
                        "0": "Level 5 represents statistically optimized engineering, the exact opposite of chaotic untracked builds.",
                        "2": "Level 4 requires quantitative statistical process control, which cannot exist without basic version control.",
                        "3": "Level 3 requires standardized organization-wide processes, which are completely absent here."
                    },
                    "source": "Software Process Assessment Models PDF; SEI CMMI Framework"
                },
                {
                    "id": "sen201-pm-cs02-q2",
                    "course": "SEN 201",
                    "topic": "Software Project Management, Metrics & Process Assessment",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case-study", "scm-workflow", "change-control"],
                    "question": "Design a formal Software Configuration Management (SCM) change control workflow to eliminate untracked production commits and establish release traceability.",
                    "marking_points": [
                        "Branch protection & pull request gates: Locking the `main` branch, requiring peer reviews and automated CI regression test passes before merging.",
                        "Formal Change Request (CR) ticketing: Every code change must map to an approved ticket specifying requirements and business justification.",
                        "Change Control Board (CCB) approval gate: Formal impact analysis and sign-off for release-candidate changes.",
                        "Semantic versioning & release auditing: Tagging immutable baselines (e.g., v2.1.0) and generating automated Bill of Materials (SBOM) for customer deployments."
                    ],
                    "answer": "1. Branch Protection & Git Governance: Direct commits to `main` and release branches are permanently locked. All changes must originate from dedicated feature/hotfix branches and require two senior peer code reviews plus passing CI regression builds before merge.\n2. Formal Change Request (CR) Integration: Every pull request must be linked to a tracked ticket (e.g., Jira) documenting the problem description, affected modules, and automated test proofs.\n3. CCB Review Gate: Emergency production hotfixes and scope additions must be evaluated by the Change Control Board (CCB) for architectural risk, timeline impact, and regression potential.\n4. Immutable Baselines & Release Traceability: Releases are tagged with cryptographic commit hashes and Semantic Versioning (SemVer: Major.Minor.Patch). An automated Software Bill of Materials (SBOM) is recorded, documenting exactly which build version was deployed to which customer, restoring complete audit traceability.",
                    "explanation": "Disciplined SCM transforms chaotic ad-hoc coding into audited, reproducible engineering releases.",
                    "why_wrong": {},
                    "source": "Sommerville Ch. 25; SCM Standards (IEEE 828)"
                }
            ]
        }
    ]
}

out_file = r"c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content\SEN 201\project_management_metrics.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(topic_data, f, indent=2)

print(f"Successfully generated {out_file} with {len(topic_data['questions']) + sum(len(cs['sub_questions']) for cs in topic_data.get('case_studies', []))} total questions.")
