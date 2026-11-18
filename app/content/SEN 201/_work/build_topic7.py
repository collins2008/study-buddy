import json
import os

topic_data = {
    "course": "SEN 201",
    "topic": "Software Testing & Quality Assurance",
    "summary": "Software testing and Quality Assurance (QA) encompass systematic verification and validation (V&V) activities throughout the software lifecycle. Verification ensures that intermediate artifacts conform to specified designs ('building the product right'), whereas validation ensures the final system satisfies user requirements and operational needs ('building the right product'). Static techniques (code inspections, peer reviews, static analysis) inspect artifacts without execution, while dynamic testing evaluates runtime behavior across unit, integration, system, and acceptance levels. Functional black-box testing leverages equivalence partitioning and boundary value analysis (BVA), while structural white-box testing targets statement, branch, and path coverage guided by McCabe's cyclomatic complexity. Modern agile engineering integrates Test-Driven Development (TDD) and continuous automated regression testing to prevent defect escapement, while performance and stress testing evaluate graceful degradation under extreme workloads.",
    "key_terms": [
        {
            "term": "Validation Testing",
            "definition": "The process of evaluating software during or at the end of development to determine whether it satisfies specified user and operational requirements ('building the right product')."
        },
        {
            "term": "Static Testing",
            "definition": "Testing and verification activities performed without executing program code, such as code inspections, architectural reviews, and automated static code analysis."
        },
        {
            "term": "Regression Testing",
            "definition": "Re-executing an existing suite of test cases to verify that recent source code modifications, bug fixes, or enhancements have not introduced new defects into previously functioning software."
        },
        {
            "term": "Stress Testing",
            "definition": "Subjecting a software system to workloads beyond its specified maximum operational capacity to assess its failure boundaries, stability, and graceful recovery mechanisms."
        },
        {
            "term": "Test-Driven Development (TDD)",
            "definition": "A software development methodology where automated unit tests are written before functional code, adhering to the iterative Red-Green-Refactor cycle."
        },
        {
            "term": "Boundary Value Analysis (BVA)",
            "definition": "A black-box test design technique that targets boundary conditions at the edges of equivalence classes (minimum, just above minimum, nominal, just below maximum, maximum), where errors cluster most frequently."
        },
        {
            "term": "Equivalence Partitioning",
            "definition": "A black-box testing technique that divides the input domain into classes of data from which test cases can be derived on the assumption that all members of a partition will be processed identically."
        },
        {
            "term": "Cyclomatic Complexity",
            "definition": "A quantitative software metric developed by Thomas McCabe that measures the number of linearly independent paths through a program's source code, computed as V(G) = E - N + 2P."
        }
    ],
    "questions": [
        {
            "id": "sen201-tq-001",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["validation", "verification", "v-and-v", "nile-exam"],
            "question": "What is the primary objective of validation testing in software engineering?",
            "options": [
                "To prove mathematically that a program contains zero execution bugs",
                "To demonstrate that the software system satisfies its customer requirements and operational intentions ('building the right product')",
                "To check that compiler syntax conforms strictly to ISO C99 standards",
                "To estimate developer salaries and hardware procurement budgets"
            ],
            "answer": 1,
            "explanation": "According to Nile Final Exam Question 63 and Barry Boehm's classic V&V definition, validation testing demonstrates that the software delivers the exact capabilities expected by the client ('building the right product'), whereas verification ensures conformance to specification ('building the product right').",
            "why_wrong": {
                "0": "Testing can only prove the presence of defects, never their total absence (Dijkstra's dictum).",
                "2": "Syntax checking is performed by compilers and linters as static verification, not validation testing.",
                "3": "Cost and salary estimations belong to project management, not validation testing."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q63; Sommerville Ch. 8"
        },
        {
            "id": "sen201-tq-002",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["static-testing", "reviews", "inspections", "nile-exam"],
            "question": "Which of the following is an example of 'static testing'?",
            "options": [
                "Running a Selenium web browser suite to click through an online shopping cart",
                "Conducting a formal Fagan code inspection and running an automated static analysis linter without executing the software binary",
                "Executing automated unit tests using JUnit to assert returned values",
                "Deploying a build to staging to measure CPU utilization under 1,000 concurrent HTTP requests"
            ],
            "answer": 1,
            "explanation": "As defined in Nile Final Exam Question 64, static testing encompasses all quality assessment techniques that do not require program execution, including peer reviews, walkthroughs, inspections, and static taint/security analysis.",
            "why_wrong": {
                "0": "Selenium automated browser testing executes the compiled running web application, which is dynamic testing.",
                "2": "JUnit unit tests execute code at runtime to verify assertions, which is dynamic testing.",
                "3": "Load and performance measurement requires a running runtime instance, which is dynamic testing."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q64; Sommerville Ch. 8"
        },
        {
            "id": "sen201-tq-003",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["release-testing", "acceptance", "nile-exam"],
            "question": "What distinguishes 'release testing' from internal developer testing?",
            "options": [
                "Release testing is conducted strictly by the developer who wrote the code using print statements",
                "Release testing is the formal process of testing a complete system release candidate intended for external customer use, typically by an independent QA team",
                "Release testing is executed before unit testing begins",
                "Release testing ignores functional requirements and checks only source code formatting"
            ],
            "answer": 1,
            "explanation": "Nile Final Exam Question 65 highlights that release testing evaluates a complete, integrated software version to ensure it meets requirements before external deployment. It is typically performed by an independent team to eliminate developer confirmation bias.",
            "why_wrong": {
                "0": "Release testing is performed by independent testers or QA teams, not individual authors relying on print statements.",
                "2": "Release testing occurs at the very end of the testing cycle, long after unit and integration testing have concluded.",
                "3": "Release testing focuses primarily on verifying that all customer-facing functional and non-functional requirements are satisfied."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q65; Sommerville Ch. 8"
        },
        {
            "id": "sen201-tq-004",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["regression-testing", "ci-cd", "maintenance", "nile-exam"],
            "question": "A team merges a security patch to fix an authentication bug in an API endpoint. Immediately after deployment, the billing checkout workflow crashes for international users. What testing practice was neglected?",
            "options": [
                "Static compiler syntax check",
                "Automated regression testing across the entire system test suite before merging",
                "Deleting all existing test cases after writing the bug patch",
                "Running performance stress tests to crash the database"
            ],
            "answer": 1,
            "explanation": "Nile Final Exam Question 66 emphasizes regression testing, which ensures that changes or bug fixes in one component do not inadvertently break existing functionality elsewhere in the system. Running an automated regression suite in CI/CD would have flagged the checkout failure immediately.",
            "why_wrong": {
                "0": "A syntax check only verifies language grammar; it cannot detect unintended runtime side-effects in billing logic.",
                "2": "Deleting test cases increases defect risk exponentially and destroys regression coverage.",
                "3": "Stress testing tests capacity limits; it does not replace functional regression verification."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q66; Sommerville Ch. 8"
        },
        {
            "id": "sen201-tq-005",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["stress-testing", "performance", "nile-exam"],
            "question": "What is the primary rationale for conducting 'stress testing' on an enterprise transaction server?",
            "options": [
                "To ensure that all source code files have proper indentation and docstrings",
                "To evaluate how the system behaves when pushed beyond its maximum design capacity and verify that it degrades gracefully rather than failing catastrophically or corrupting data",
                "To replace all unit tests with user surveys",
                "To guarantee that the software never requires maintenance"
            ],
            "answer": 1,
            "explanation": "As defined in Nile Final Exam Question 67, stress testing intentionally subjects a system to abnormal, overwhelming transaction volumes to uncover its breaking points, ensure transactional integrity, prevent memory crashes, and confirm graceful recovery.",
            "why_wrong": {
                "0": "Code formatting is checked by automated code linters during static analysis.",
                "2": "User surveys evaluate user sentiment/satisfaction, not concurrent server stress limits.",
                "3": "No form of testing eliminates software evolution or maintenance requirements."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q67; Sommerville Ch. 8"
        },
        {
            "id": "sen201-tq-006",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["tdd", "agile", "xp", "nile-exam"],
            "question": "What is a major engineering advantage of Test-Driven Development (TDD) as highlighted in software engineering examinations?",
            "options": [
                "It eliminates the need for any software requirements or architectural design",
                "Writing automated tests before implementation code provides immediate regression coverage, simplifies debugging, and enforces modular decoupled design",
                "It guarantees that developers will never need to refactor or change their code in the future",
                "It enables untested code to be directly released to end users without QA"
            ],
            "answer": 1,
            "explanation": "Nile Final Exam Question 68 emphasizes that TDD's primary advantages include drastically reduced regression defects, immediate feedback when errors occur (making debugging trivial since only recent lines changed), and improved code modularity.",
            "why_wrong": {
                "0": "TDD requires clear requirements to formulate test assertions; it does not replace requirements.",
                "2": "Refactoring is an explicit, mandatory third step in the TDD cycle (Red-Green-Refactor).",
                "3": "TDD does not eliminate independent release or acceptance testing."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q68; Beck (2002) TDD by Example"
        },
        {
            "id": "sen201-tq-007",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["black-box", "bva", "equivalence-partitioning"],
            "question": "A banking system accepts a customer transfer amount between 100 Naira and 5,000,000 Naira inclusive. Applying Boundary Value Analysis (BVA), which set of test input values provides optimal boundary coverage?",
            "options": [
                "{500, 1000, 50000, 2000000}",
                "{99, 100, 101, 4999999, 5000000, 5000001}",
                "{0, -100, 100000000}",
                "{100, 200, 300, 400}"
            ],
            "answer": 1,
            "explanation": "Boundary Value Analysis (BVA) dictates testing immediately below the minimum (99), at the minimum (100), immediately above the minimum (101), immediately below the maximum (4,999,999), at the maximum (5,000,000), and immediately above the maximum (5,000,001).",
            "why_wrong": {
                "0": "These are interior nominal values within the valid equivalence partition, which do not test boundary edge conditions.",
                "2": "These values test extreme outliers but fail to test the critical boundary transition points (100 and 5,000,000).",
                "3": "These arbitrary interior values provide zero upper-boundary coverage."
            },
            "source": "Software Engineering Concepts and Principles Lecture Notes; Sommerville Ch. 8"
        },
        {
            "id": "sen201-tq-008",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "multi_select",
            "difficulty": 3,
            "tags": ["testing-limits", "theory", "nile-exam"],
            "question": "Why is exhaustive testing of a commercial software system mathematically and practically impossible? (Select ALL that apply)",
            "options": [
                "The combinatorial explosion of input parameters and system states produces an infinite or astronomically large test space",
                "Complex programs contain an intractable number of execution paths, loops, and concurrency interleavings",
                "Software development is constrained by finite economic budgets and commercial delivery deadlines",
                "Modern compilers automatically execute all possible test combinations during compilation"
            ],
            "answer": [0, 1, 2],
            "explanation": "Nile Final Exam Question 70 addresses why complete exhaustive testing is impossible: combinatorial explosion of inputs and internal state transitions, infinite execution paths through unbounded loops and concurrent threads, and finite real-world project resources and deadlines. Compilers do not execute dynamic tests.",
            "why_wrong": {
                "3": "Compilers verify grammar and generate machine code; they do not dynamically simulate or execute runtime test permutations."
            },
            "source": "Nile University SEN 201 Final Exam Paper Type B Q70; Sommerville Ch. 8"
        },
        {
            "id": "sen201-tq-fc01",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "verification", "validation"],
            "question": "What is the core distinction between Verification and Validation (Barry Boehm's rule)?",
            "answer": "Verification: 'Are we building the product right?' (Ensuring the system conforms to its technical specification).\nValidation: 'Are we building the right product?' (Ensuring the software satisfies the real-world operational needs of the customer).",
            "explanation": "Examined in Nile University SEN 201 Final Exam Paper Type B Question 63.",
            "why_wrong": {},
            "source": "Nile Final Exam Paper Type B Q63; Sommerville Ch. 8"
        },
        {
            "id": "sen201-tq-fc02",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "static-testing"],
            "question": "What is Static Testing, and what are two common examples?",
            "answer": "Testing techniques that evaluate software artifacts WITHOUT executing the source code. Examples include: (1) Fagan formal code inspections and peer reviews, and (2) automated static analysis linter tools (e.g., SonarQube).",
            "explanation": "Examined in Nile University SEN 201 Final Exam Paper Type B Question 64.",
            "why_wrong": {},
            "source": "Nile Final Exam Paper Type B Q64"
        },
        {
            "id": "sen201-tq-fc03",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "regression-testing"],
            "question": "What is Regression Testing, and why is it essential in agile development?",
            "answer": "Re-executing an existing suite of tests to verify that recent code changes or bug fixes have not broken previously functioning features. It is vital in agile because frequent iterative code deployments risk introducing silent regressions.",
            "explanation": "Examined in Nile University SEN 201 Final Exam Paper Type B Question 66.",
            "why_wrong": {},
            "source": "Nile Final Exam Paper Type B Q66"
        },
        {
            "id": "sen201-tq-fc04",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "stress-testing"],
            "question": "What is Stress Testing, and how does it differ from Load Testing?",
            "answer": "Load testing evaluates system performance under expected normal and peak workloads. Stress testing pushes the system BEYOND its maximum design capacity to test failure boundaries, error logging, and graceful degradation.",
            "explanation": "Examined in Nile University SEN 201 Final Exam Paper Type B Question 67.",
            "why_wrong": {},
            "source": "Nile Final Exam Paper Type B Q67"
        },
        {
            "id": "sen201-tq-fc05",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "tdd"],
            "question": "What are the three stages of the Test-Driven Development (TDD) cycle?",
            "answer": "1. Red: Write an automated test for the next unit of functionality and watch it fail.\n2. Green: Write the minimal code necessary to make the test pass.\n3. Refactor: Clean up and optimize the implementation while keeping all tests passing.",
            "explanation": "Examined in Nile University SEN 201 Final Exam Paper Type B Question 68.",
            "why_wrong": {},
            "source": "Nile Final Exam Paper Type B Q68; Beck TDD"
        },
        {
            "id": "sen201-tq-fc06",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "equivalence-partitioning"],
            "question": "What is Equivalence Partitioning in black-box test design?",
            "answer": "A method that divides the input data of a software component into partitions of equivalent data from which test cases can be derived, assuming all inputs in a partition are handled identically.",
            "explanation": "Significantly reduces the number of test cases while maintaining functional coverage.",
            "why_wrong": {},
            "source": "Software Engineering Concepts and Principles Lecture Notes"
        },
        {
            "id": "sen201-tq-fc07",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "bva"],
            "question": "What is Boundary Value Analysis (BVA), and why is it effective?",
            "answer": "A testing technique targeting values at the boundaries of equivalence partitions (min, min-1, min+1, max, max-1, max+1). It is effective because developers most frequently make off-by-one errors at comparison boundaries (< vs <=).",
            "explanation": "Complementary to Equivalence Partitioning.",
            "why_wrong": {},
            "source": "Software Engineering Concepts and Principles Lecture Notes"
        },
        {
            "id": "sen201-tq-fc08",
            "course": "SEN 201",
            "topic": "Software Testing & Quality Assurance",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "cyclomatic-complexity"],
            "question": "What does Cyclomatic Complexity measure, and how is it calculated?",
            "answer": "It measures the quantitative complexity of a program and dictates the minimum number of test cases required for complete branch coverage. Calculated as V(G) = E - N + 2P (Edges - Nodes + 2*Connected Components) or V(G) = Predicate Nodes + 1.",
            "explanation": "Developed by Thomas McCabe for structural white-box testing.",
            "why_wrong": {},
            "source": "Software Engineering Concepts and Principles Lecture Notes"
        }
    ],
    "case_studies": [
        {
            "id": "sen201-tq-cs01",
            "scenario": "A digital commercial bank is testing its automated loan risk scoring engine. The requirements specify: (1) Applicant Age must be between 18 and 65 years inclusive; (2) Monthly Net Income must be at least 150,000 Naira; (3) Credit Bureau Score must range from 300 to 850 inclusive. If any parameter falls outside these valid bounds, the loan application must be rejected with a specific audit validation error. The QA engineering team must design a comprehensive test suite using black-box Equivalence Partitioning and Boundary Value Analysis.",
            "sub_questions": [
                {
                    "id": "sen201-tq-cs01-q1",
                    "course": "SEN 201",
                    "topic": "Software Testing & Quality Assurance",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case-study", "bva", "loan-system"],
                    "question": "To verify the Applicant Age parameter using strict Boundary Value Analysis (BVA), which set of test age inputs is strictly required?",
                    "options": [
                        "{25, 35, 45, 55}",
                        "{17, 18, 19, 64, 65, 66}",
                        "{0, 10, 100, 120}",
                        "{-18, 18, 65, -65}"
                    ],
                    "answer": 1,
                    "explanation": "For an inclusive range of [18, 65], Boundary Value Analysis requires testing the lower boundary points (17: invalid below, 18: valid on boundary, 19: valid just above) and the upper boundary points (64: valid just below, 65: valid on boundary, 66: invalid above).",
                    "why_wrong": {
                        "0": "These are internal nominal values within the partition and do not probe boundary transitions.",
                        "2": "These values test extreme arbitrary outliers rather than the immediate boundary edges.",
                        "3": "Negative values do not reflect the actual upper and lower threshold edges."
                    },
                    "source": "Sommerville Ch. 8; Black-box Test Design"
                },
                {
                    "id": "sen201-tq-cs01-q2",
                    "course": "SEN 201",
                    "topic": "Software Testing & Quality Assurance",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case-study", "white-box", "cyclomatic-complexity"],
                    "question": "The loan scoring algorithm contains 4 nested `if-else` decision conditions and one `while` loop that iterates over historical defaults. Calculate the McCabe Cyclomatic Complexity V(G) of this routine and explain what this number dictates regarding test suite design.",
                    "marking_points": [
                        "Identifies total predicate decision points: 4 `if` statements + 1 `while` loop = 5 predicate nodes.",
                        "Applies formula V(G) = P + 1: 5 + 1 = 6.",
                        "Explains the significance: Dictates that exactly 6 linearly independent paths exist through the control flow graph.",
                        "Concludes that at least 6 distinct test cases are required to achieve 100% branch/basis-path test coverage."
                    ],
                    "answer": "1. Predicate Node Count: The control flow contains 5 binary decision conditions (4 conditional branches from `if-else` and 1 loop condition from `while`).\n2. Complexity Calculation: Using McCabe's formula V(G) = Predicate Nodes (P) + 1, we obtain V(G) = 5 + 1 = 6.\n3. Significance for Testing: A Cyclomatic Complexity of 6 indicates that there are exactly 6 linearly independent execution paths through the function's control flow graph.\n4. Test Suite Implication: The QA team must design a minimum of 6 linearly independent test cases to guarantee 100% basis-path and branch coverage, ensuring that every decision outcome (True and False) is executed at least once.",
                    "explanation": "Cyclomatic complexity provides an objective lower bound on the number of test cases required for complete path coverage.",
                    "why_wrong": {},
                    "source": "Sommerville Ch. 8; McCabe (1976) A Complexity Measure"
                }
            ]
        },
        {
            "id": "sen201-tq-cs02",
            "scenario": "During the release of national university entrance examination results, 500,000 students attempt to check their scores simultaneously within a 30-minute window. During preliminary staging tests, response times jumped from 200ms to 48 seconds when concurrent traffic reached 25,000 users, and at 35,000 users, the database connection pool exhausted, throwing HTTP 500 errors and locking student accounts. The QA lead must design a comprehensive performance, stress, and recovery test strategy.",
            "sub_questions": [
                {
                    "id": "sen201-tq-cs02-q1",
                    "course": "SEN 201",
                    "topic": "Software Testing & Quality Assurance",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case-study", "stress-testing", "capacity"],
                    "question": "Which testing methodology should the QA team execute to determine the EXACT concurrent user threshold at which the portal's connection pool fails, and observe whether the system recovers gracefully once traffic subsides?",
                    "options": [
                        "Equivalence partitioning of student matriculation numbers",
                        "Stress testing using an automated distributed load generator with ramp-up and ramp-down traffic curves",
                        "Static inspection of CSS stylesheets",
                        "Unit testing the student login password hashing algorithm"
                    ],
                    "answer": 1,
                    "explanation": "Stress testing with distributed traffic generators systematically ramps up concurrency beyond normal capacity to determine the exact failure breakpoint, checks if rate-limiting or queuing prevents crashes, and verifies graceful self-recovery as load decreases.",
                    "why_wrong": {
                        "0": "Equivalence partitioning tests functional input validity, not server concurrency limits.",
                        "2": "Static stylesheet inspection cannot measure database connection pool exhaustion.",
                        "3": "Unit testing isolated hash functions does not uncover multi-user concurrency and connection pool exhaustion bottlenecks."
                    },
                    "source": "Nile Final Exam Paper Type B Q67; Sommerville Ch. 8"
                },
                {
                    "id": "sen201-tq-cs02-q2",
                    "course": "SEN 201",
                    "topic": "Software Testing & Quality Assurance",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case-study", "regression", "canary-deployment"],
                    "question": "To prevent faulty updates from causing nationwide portal blackouts on results release day, outline an automated testing and deployment pipeline incorporating regression testing and canary releases.",
                    "marking_points": [
                        "Continuous Integration (CI) regression gate: Automated unit, integration, and end-to-end regression test suite execution upon every commit.",
                        "Performance benchmark gate: Automated load tests run against staging to confirm response times remain under 500ms before release approval.",
                        "Canary deployment strategy: Routing 2% of live student traffic to the new release while monitoring error rates and latency.",
                        "Automated rollback mechanism: Instantaneous, automated traffic routing back to stable baseline if HTTP 5xx errors exceed 0.1%."
                    ],
                    "answer": "1. Automated CI Regression Suite: All code commits must automatically trigger unit, integration, and functional regression test suites in a CI pipeline; a single test failure immediately blocks build progression.\n2. Staging Load Regression Gate: Automated performance tests simulate 50,000 concurrent sessions on a production-mirror staging environment to verify latency stays below 500ms and connection pools do not exhaust.\n3. Canary Deployment: The new release is deployed to a isolated subset of server instances, routing only 2-5% of real user traffic to the canary while 95% remains on the proven baseline.\n4. Real-time Telemetry & Instant Rollback: Automated observability tools monitor HTTP 5xx error rates, response latencies, and CPU metrics. If error thresholds exceed 0.1%, traffic is instantly reverted to the baseline deployment automatically without downtime.",
                    "explanation": "Combining automated CI regression testing with canary deployments and automated rollback eliminates catastrophic release day failures.",
                    "why_wrong": {},
                    "source": "Sommerville Ch. 8; Modern QA & DevOps Principles"
                }
            ]
        }
    ]
}

out_file = r"c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content\SEN 201\software_testing_qa.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(topic_data, f, indent=2)

print(f"Successfully generated {out_file} with {len(topic_data['questions']) + sum(len(cs['sub_questions']) for cs in topic_data.get('case_studies', []))} total questions.")
