import json
import os

topic_data = {
    "course": "INS 202",
    "topic": "hci_introduction_goals",
    "title": "HCI Fundamentals & Core Goals (Safety, Utility, etc.)",
    "summary": "Foundational study of Human-Computer Interaction (HCI) definitions, history, interdisciplinary roots, and core goals. Examines the formal ACM SIGCHI definition and the historic economic cost shift from 1953 (IBM 701, ~33 kb, where human programmer time was sacrificed to save scarce machine time) to modern computing (where computing is ubiquitous and human attention is the scarce, expensive resource). Focuses intensely on the Five Core Goals of HCI explicitly flagged by the lecturer as critical for examinations: Safety (user and data protection in critical environments like avionics and healthcare), Utility (available functional services), Effectiveness (successful goal attainment), Efficiency (rapid task execution with minimal effort), and Usability (learnability, memorability, error recovery, appeal). Explores the crucial distinction between Utility and Effectiveness, and quantifies the business benefits of usable systems (conversion rates, productivity, and customer support call reduction from $12 to $250 per call).",
    "key_terms": [
        {"term": "Human-Computer Interaction (HCI)", "definition": "A multidisciplinary field concerned with the design, evaluation, and implementation of interactive computing systems for human use and the study of major phenomena surrounding them (ACM SIGCHI)."},
        {"term": "Safety", "definition": "A foundational HCI goal focused on protecting human users from physical danger or catastrophic harm, and safeguarding critical data from unrecoverable destruction."},
        {"term": "Utility", "definition": "The functional capabilities, operations, and services that an interactive system provides to users."},
        {"term": "Effectiveness", "definition": "A measure of whether users can successfully and accurately achieve their intended goals using the system's available services."},
        {"term": "Efficiency", "definition": "A measure of the speed, resources, clicks, and physical/cognitive effort required for users to accomplish their goals once proficient."},
        {"term": "Usability", "definition": "The qualitative and quantitative ease of learning, ease of use, error tolerance, and satisfaction experienced when interacting with a system."},
        {"term": "Conversion Rate", "definition": "The percentage of website visitors or app users who successfully take a desired target action (e.g. completing a purchase or submitting an enrollment)."},
        {"term": "IBM 701 (1953)", "definition": "An early landmark commercial electronic scientific computer featuring approximately 33 kb of electrostatic Williams tube memory, representing the era when human labor served machine efficiency."}
    ],
    "questions": [
        {
            "id": "ins202-fnd-001",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "multi_select",
            "difficulty": 2,
            "tags": ["hci_goals", "lecturer_flagged", "exam_critical"],
            "question": "In the student lecture notes, the lecturer explicitly highlighted: 'list the goals of HCI => IMPORTANT FOR EXAM!!!'. Which of the following constitute the FIVE foundational goals of Human-Computer Interaction? (Select FIVE)",
            "options": [
                "Safety (protecting users and data from harm or catastrophe)",
                "Utility (the services and functional capabilities provided)",
                "Effectiveness (users successfully achieving their intended tasks)",
                "Efficiency (completing tasks quickly with minimal effort/time)",
                "Usability (ease of learning, ease of use, and satisfaction)",
                "Cryptographic Bitwise Shuffling",
                "Monetary Stock Inflation"
            ],
            "answer": [0, 1, 2, 3, 4],
            "explanation": "As prominently flagged in the course materials and lecturer notes, the five core goals of HCI are: 1. Safety, 2. Utility, 3. Effectiveness, 4. Efficiency, and 5. Usability. Cryptographic shuffling and financial inflation are unrelated domains.",
            "why_wrong": {
                "5": "Bitwise shuffling is a cryptographic security function, not an HCI usability goal.",
                "6": "Stock inflation is macroeconomic financial theory, not an HCI system goal."
            },
            "marking_points": [],
            "source": "Student Notebook Image 21.47.02 (1); Module 01 Slides 19-24",
            "verified": True,
            "verified_output": "Safety, Utility, Effectiveness, Efficiency, Usability."
        },
        {
            "id": "ins202-fnd-002",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "explain",
            "difficulty": 3,
            "tags": ["utility_vs_effectiveness", "hci_goals"],
            "question": "In HCI theory, 'Utility' and 'Effectiveness' are distinct concepts. Explain the precise difference between them, and provide a concrete e-commerce website example where high utility coexists with low effectiveness.",
            "options": [],
            "answer": "Utility refers to whether an interactive system possesses the functional capabilities and services required to perform a task (i.e. *what* the system can do). Effectiveness refers to whether human users can successfully and accurately accomplish their intended goals using those services (i.e. *how well* users succeed). A concrete example: An online university bookstore provides a fully functional payment gateway, search engine, and inventory catalog containing all required textbooks (high utility). However, the search bar requires obscure 13-digit ISBN codes without keyword search, category links are hidden behind ambiguous icons, and the checkout button is placed in an unnoticeable footer; consequently, 85% of students abandon their carts without purchasing books. Because users cannot accomplish their goal despite the services existing, the website possesses high utility but suffers from severe lack of effectiveness.",
            "explanation": "Utility is feature availability; Effectiveness is user task success. Features that cannot be found or completed lack effectiveness.",
            "why_wrong": {},
            "marking_points": [
                "Defines Utility as the availability of features, functions, and services provided by the system.",
                "Defines Effectiveness as whether users can successfully and accurately achieve their intended goals.",
                "Explicitly articulates that a feature may exist (utility) but remain unused or failed by users (lack of effectiveness).",
                "Provides a valid concrete example (e.g. e-commerce bookstore with inventory and checkout where users fail to complete purchases due to bad navigation)."
            ],
            "source": "Module 01 Slides 21-22",
            "verified": True,
            "verified_output": "Utility vs Effectiveness."
        },
        {
            "id": "ins202-fnd-003",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["history", "cost_shift", "ibm_1953"],
            "question": "According to the course history of computing (highlighted in the student notebook as '1st computer from IBM 1953, 33kb'), how did the economic relationship between computer hardware and human programmer time fundamental shift between 1953 and today?",
            "options": [
                "In 1953, computer hardware was so expensive that one machine equaled the annual salaries of 200 programmers, forcing humans to adapt to the machine; today, hardware is cheap and human cognitive time is the expensive, scarce resource.",
                "In 1953, human programmers were paid in physical gold bars while computers were distributed for free to elementary schools.",
                "In 1953, computers ran with zero latency, but modern microprocessors take several hours to process a single punched card.",
                "There has been zero economic or technological shift in computer costs since 1953."
            ],
            "answer": 0,
            "explanation": "In 1953 (the era of the IBM 701 with ~33 kb memory), computer hardware was astronomically expensive; a machine cost equaled 200 programmer salaries, so humans spent days preparing batch punch cards to save seconds of CPU time. Today, hardware is ubiquitous and inexpensive, so system design is inverted: computing systems must be designed around human cognitive convenience.",
            "why_wrong": {
                "1": "Computers were multi-million dollar investments in 1953, not free school toys.",
                "2": "Early machines took hours for simple batch jobs, whereas modern CPUs execute billions of operations per second.",
                "3": "The cost of computing has plummeted by many orders of magnitude."
            },
            "marking_points": [],
            "source": "Student Notebook Image 21.47.02 (1); Module 01 Slides 15, 18",
            "verified": True,
            "verified_output": "Hardware was scarce in 1953; today human time and cognitive bandwidth are scarce."
        },
        {
            "id": "ins202-fnd-004",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "matching",
            "difficulty": 3,
            "tags": ["interdisciplinary_fields", "hci_roots"],
            "question": "Match each foundational academic discipline contributing to HCI to its primary contribution to interactive system design:",
            "options": [
                "Computer Science",
                "Cognitive Psychology",
                "Ergonomics / Human Factors",
                "Graphic & Visual Design"
            ],
            "answer": {
                "Computer Science": "Provides software architecture, programming languages, algorithms, and technical implementation of interactive systems.",
                "Cognitive Psychology": "Provides models of human perception, memory limitations (7±2 chunks), mental models, and decision-making processes.",
                "Ergonomics / Human Factors": "Evaluates physical human biomechanics, workstation posture, visual fatigue, and physical button/hardware dimensions.",
                "Graphic & Visual Design": "Establishes visual hierarchy, typography, aesthetic appeal, alignment, and color contrast principles."
            },
            "explanation": "HCI is inherently cross-disciplinary: Computer Science builds the technical engine, Cognitive Psychology models the user's mind, Ergonomics accounts for the physical human body, and Visual Design shapes aesthetics and layout.",
            "why_wrong": {},
            "marking_points": [],
            "source": "Module 01 Slides 12, 28-29",
            "verified": True,
            "verified_output": "Matched interdisciplinary fields."
        },
        {
            "id": "ins202-fnd-005",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["business_benefits", "conversion_rate"],
            "question": "In web-based commercial applications, what technical term defines the percentage of site visitors who successfully perform a targeted, desired business action (such as completing an e-commerce purchase or signing up for a course)?",
            "options": [
                "Conversion Rate",
                "Bounce Attenuation",
                "Packet Throughput",
                "Clock Cycle Yield"
            ],
            "answer": 0,
            "explanation": "Conversion Rate is the standard commercial metric defining the percentage of visitors who complete a desired goal (e.g., buying a product). Improving website usability directly increases the conversion rate, lowering customer acquisition costs.",
            "why_wrong": {
                "1": "Bounce rate measures visitors leaving immediately, not successful conversions.",
                "2": "Packet throughput is a networking metric measuring data delivery rates.",
                "3": "Clock cycle yield is a semiconductor silicon manufacturing metric."
            },
            "marking_points": [],
            "source": "Module 01 Slide 7",
            "verified": True,
            "verified_output": "Conversion Rate."
        },
        {
            "id": "ins202-fnd-006",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["business_benefits", "support_costs"],
            "question": "According to industry research cited in the course lectures, approximately how much does an individual technical customer support telephone call cost a software vendor when users encounter confusing interfaces?",
            "options": [
                "Estimates range from $12 to $250 per call",
                "Exactly $0.05 per call",
                "More than $50,000 per call",
                "Customer support calls have zero financial cost to the vendor"
            ],
            "answer": 0,
            "explanation": "As cited in Module 01 Slide 10: 'Calls to customer support are very expensive for the vendor: estimates range from $12 to $250 per call.' A well-designed, usable interface drastically reduces call center volumes, saving enterprises millions of dollars annually.",
            "why_wrong": {
                "1": "Staffed telephone support requires trained human technicians and telecom infrastructure, costing far more than five cents.",
                "2": "$50,000 is an absurd overestimation for a routine phone call.",
                "3": "Salaries, facilities, and phone lines represent major vendor overhead costs."
            },
            "marking_points": [],
            "source": "Module 01 Slide 10",
            "verified": True,
            "verified_output": "$12 to $250 per call."
        },
        {
            "id": "ins202-fnd-007",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "true_false_why",
            "difficulty": 2,
            "tags": ["hci_goals", "safety"],
            "question": "The HCI goal of 'Safety' applies exclusively to industrial and military systems such as air traffic control towers and nuclear power plants, with zero relevance to ordinary consumer websites.",
            "options": [
                "True — consumer websites only deal with amusement and fashion, so human errors never have serious consequences.",
                "False — safety in general computing encompasses both physical safety and the safety of data (e.g. preventing accidental permanent deletion of tax records, bank fund transfers, or unrecoverable medical files)."
            ],
            "answer": 1,
            "explanation": "As taught in Module 01 Slide 20: Safety covers both Safety of Users (preventing physical catastrophe in aviation, automotive, and hospital care) AND Safety of Data (preventing accidental deletion of critical customer records, financial accounts, or thesis dissertations through destructive, non-reversible actions).",
            "why_wrong": {
                "0": "Accidental deletion of bank databases or patient medical charts can result in devastating financial ruin and loss of life."
            },
            "marking_points": [],
            "source": "Module 01 Slide 20",
            "verified": True,
            "verified_output": "False. Safety includes data safety and preventing catastrophic loss."
        },
        {
            "id": "ins202-fnd-008",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "cloze",
            "difficulty": 2,
            "tags": ["acm_sigchi", "definition"],
            "question": "The Association for Computing Machinery's Special Interest Group on Computer-Human Interaction (ACM SIGCHI) defines HCI as a discipline concerned with the {{c1::design}}, {{c2::evaluation}}, and {{c3::implementation}} of interactive computing systems for human use.",
            "options": ["design", "evaluation", "implementation", "fabrication", "marketing", "monetization"],
            "answer": ["design", "evaluation", "implementation"],
            "explanation": "The official ACM SIGCHI definition states: 'Human-Computer Interaction is a discipline concerned with the design, evaluation, and implementation of interactive computing systems for human use and with the study of the major phenomena surrounding them.'",
            "why_wrong": {},
            "marking_points": [],
            "source": "Module 01 Slide 11",
            "verified": True,
            "verified_output": "design, evaluation, implementation"
        },
        {
            "id": "ins202-fnd-009",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["hci_goals", "efficiency_metric"],
            "question": "Which of the following measurements is the most valid objective metric for evaluating the 'Efficiency' goal of an airline ticketing check-in kiosk?",
            "options": [
                "The average time in seconds and number of screen taps required for a frequent traveler to print their boarding pass.",
                "The total weight of the aluminum kiosk stand in kilograms.",
                "The artistic popularity of the airline's corporate logo among social media influencers.",
                "The number of lines of C++ code compiled into the backend check-in daemon."
            ],
            "answer": 0,
            "explanation": "Efficiency measures how quickly and with what effort users can achieve their goals once proficient. Measuring task completion time (seconds) and keystroke/tap counts directly reflects operational efficiency.",
            "why_wrong": {
                "1": "Physical weight is a mechanical hardware property, not a software interaction efficiency metric.",
                "2": "Logo popularity measures aesthetic brand marketing, not user task efficiency.",
                "3": "Source code lines measure code volume, not human interaction speed."
            },
            "marking_points": [],
            "source": "Module 01 Slide 23",
            "verified": True,
            "verified_output": "Average time and screen taps required."
        },
        {
            "id": "ins202-fnd-010",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "type_answer",
            "difficulty": 2,
            "tags": ["usability_dimensions"],
            "question": "What is the technical term in usability engineering that describes how easily a first-time user can accomplish basic tasks the very first time they encounter an interactive interface?",
            "answer": "learnability",
            "accepted_answers": ["learnability", "ease of learning"],
            "explanation": "Learnability is the ease with which novices can understand and navigate an interface upon their initial exposure, without requiring formal training or extensive manuals.",
            "marking_points": [
                "Identifies 'learnability' or 'ease of learning'."
            ],
            "source": "Module 01 Slide 24; Usability Standards",
            "verified": True,
            "verified_output": "learnability"
        },
        {
            "id": "ins202-fnd-011",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["practitioner_role"],
            "question": "In the software development lifecycle, what is the primary professional role of an HCI practitioner according to the course overview?",
            "options": [
                "To act as the dedicated advocate for the human user throughout system design and development.",
                "To optimize SQL database queries to reduce hard disk seek times.",
                "To negotiate vendor discount pricing for bulk fiber-optic cable procurement.",
                "To enforce strict binary assembly language coding standards among junior developers."
            ],
            "answer": 0,
            "explanation": "As stated in Module 01 Slide 16: 'How do we make computers easy to use? By applying the principles of Human-Computer Interaction; By being, as an HCI practitioner, the advocate for the user.'",
            "why_wrong": {
                "1": "Database query optimization is performed by database administrators (DBAs).",
                "2": "Procurement officers negotiate cable purchase contracts.",
                "3": "Assembly coding standards are managed by software systems architects."
            },
            "marking_points": [],
            "source": "Module 01 Slide 16",
            "verified": True,
            "verified_output": "Advocate for the user."
        },
        {
            "id": "ins202-fnd-012",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "true_false_why",
            "difficulty": 3,
            "tags": ["development_costs", "user_research"],
            "question": "Conducting user research and usability testing before writing code actually reduces total software development and maintenance costs over the system lifecycle.",
            "options": [
                "False — user research is a pure financial waste that always adds 50% overhead to project costs without benefit.",
                "True — learning about users first prevents teams from building complex features users never use, and finding interface design defects during early requirements is up to 100 times cheaper than fixing them after software deployment."
            ],
            "answer": 1,
            "explanation": "As taught in Module 01 Slide 8: 'Learn about users first, and you will avoid implementing features users don't want.' Software engineering economics (e.g. Boehm's cost-of-change curve) confirms that fixing usability mistakes after product rollout is vastly more expensive than discovering them during early user analysis.",
            "why_wrong": {
                "0": "User research saves substantial money by preventing re-coding of unwanted or flawed features."
            },
            "marking_points": [],
            "source": "Module 01 Slide 8",
            "verified": True,
            "verified_output": "True. Early user research reduces development and rework costs."
        },
        {
            "id": "ins202-fnd-013",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["hci_goals", "usability_memorability"],
            "question": "A tax filing portal is used by self-employed accountants only once every twelve months. Which specific usability attribute is most critical for this portal to ensure returning accountants do not have to completely re-learn the system every year?",
            "options": [
                "Memorability (retention of operational proficiency over time)",
                "Paging File Allocation Velocity",
                "RGB Color Gamut Calibration",
                "Server Cache Overclocking"
            ],
            "answer": 0,
            "explanation": "Memorability measures how easily returning users can re-establish proficiency after an extended period of non-use. For intermittent systems (like annual tax software), high memorability ensures users can complete tasks without re-reading user guides.",
            "why_wrong": {
                "1": "Paging file allocation is an OS memory management concern.",
                "2": "RGB gamut is a graphic display calibration standard.",
                "3": "Cache overclocking is hardware tuning, not human memorability."
            },
            "marking_points": [],
            "source": "Module 01 Slide 24",
            "verified": True,
            "verified_output": "Memorability."
        },
        {
            "id": "ins202-fnd-014",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "type_answer",
            "difficulty": 2,
            "tags": ["textbook_author", "lecturer_note"],
            "question": "In the student's handwritten lecture notes, the author of the primary recommended course textbook for INS 202 was noted as 'Gerard Kym'. What is the full, formal academic name of this textbook author?",
            "answer": "Gerard Jounghyun Kim",
            "accepted_answers": ["Gerard Jounghyun Kim", "Gerard Kim", "Gerard J. Kim"],
            "explanation": "The textbook author is Dr. Gerard Jounghyun Kim, author of *Human-Computer Interaction: Fundamentals and Practice* (CRC Press), cited throughout the lecture slides and referenced in the student notebook.",
            "marking_points": [
                "Identifies 'Gerard Jounghyun Kim' (or 'Gerard Kim')."
            ],
            "source": "Student Notebook Image 21.46.55; Module 01 Slide 2",
            "verified": True,
            "verified_output": "Gerard Jounghyun Kim"
        },
        {
            "id": "ins202-fnd-015",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["hci_goals", "error_prevention"],
            "question": "When designing an intensive-care patient monitor in a hospital, a medical software team uses distinct auditory alert tones, unmistakable color coding, and requires a two-step confirmation before stopping intravenous drug delivery. Which HCI goal is being prioritized?",
            "options": [
                "Safety",
                "Entertainment appeal",
                "Monetary conversion rate",
                "Search engine optimization (SEO)"
            ],
            "answer": 0,
            "explanation": "Preventing accidental or mistaken shutdown of life-support systems directly addresses the HCI goal of Safety (protecting human users from physical harm, medical errors, or fatality).",
            "why_wrong": {
                "1": "Hospital medical systems prioritize patient survival over entertainment.",
                "2": "Conversion rates apply to commercial shopping carts, not clinical infusion pumps.",
                "3": "SEO optimizes search engine rankings for public web pages."
            },
            "marking_points": [],
            "source": "Module 01 Slide 20",
            "verified": True,
            "verified_output": "Safety."
        },
        {
            "id": "ins202-fnd-016",
            "course": "INS 202",
            "topic": "hci_introduction_goals",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["ucd_characteristics"],
            "question": "Which of the following describes a foundational characteristic of the User-Centered Development (UCD) methodology?",
            "options": [
                "It is user-centric rather than data-centric, actively involves users throughout the design lifecycle, measures usability quantitatively, and is highly iterative.",
                "It designs the complete software architecture in secret without ever showing drafts or prototypes to human users until product release.",
                "It treats managers as the only users whose opinions matter, ignoring workers in the field.",
                "It mandates that all applications must run exclusively on mechanical punched cards."
            ],
            "answer": 0,
            "explanation": "As defined in Module 01 Slide 27: User-Centered Development is user-centric (not data-centric), involves real users in early stages, quantifies usability metrics, and operates iteratively through continuous prototype testing and refinement.",
            "why_wrong": {
                "1": "Designing in secret without user contact violates user-centered development.",
                "2": "Managers are not users; their assumptions often contradict actual user workflows.",
                "3": "UCD applies across modern graphical, touch, mobile, and web interfaces."
            },
            "marking_points": [],
            "source": "Module 01 Slide 27",
            "verified": True,
            "verified_output": "User-centric, iterative, measures usability with users."
        }
    ],
    "case_studies": [
        {
            "id": "ins202-fnd-cs1",
            "scenario": "Nile University deploys a new online Course Registration Portal for 8,000 undergraduate students. The portal database has full functional capability (Utility): courses can be registered, prerequisites checked, fees verified, and timetables generated. However, on registration day, 3,200 students flood the IT support desk in panic: (1) The 'Confirm & Submit Registration' button is disguised as a tiny gray text hyperlink at the bottom of a 2,000-word legal disclaimer; (2) When a student selects a course with a timetable clash, the portal displays a cryptic error code: 'FATAL EXCEPTION 0x80041002: CLR_INVALID_SLOT' without stating which course conflicted; (3) If a student accidentally hits the browser Back button, their entire course selection is wiped clean without any recovery confirmation.",
            "sub_questions": [
                {
                    "id": "ins202-fnd-cs1-q1",
                    "course": "INS 202",
                    "topic": "hci_introduction_goals",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case_study", "utility_vs_effectiveness"],
                    "question": "Analyzing the portal under the 5 Goals of HCI, how would an expert HCI evaluator classify the portal's state regarding Utility and Effectiveness?",
                    "options": [
                        "High Utility (the required database features and services exist), but severely deficient Effectiveness (students fail to complete registration due to unnavigable submission links and indecipherable errors).",
                        "Zero Utility because the portal does not support cryptocurrency transactions.",
                        "High Effectiveness because students were forced to visit the IT support desk in person.",
                        "High Usability because the cryptic hex codes teach students low-level machine architecture."
                    ],
                    "answer": 0,
                    "explanation": "The portal has high utility because all required registration functions, fee calculations, and database procedures exist. However, it lacks effectiveness because students cannot successfully achieve their goal of registering due to invisible controls, destructive data loss, and unhelpful error messages.",
                    "why_wrong": {
                        "1": "Cryptocurrency is irrelevant to academic course registration utility.",
                        "2": "Forcing thousands of students to crowd the help desk in panic indicates catastrophic failure of effectiveness.",
                        "3": "Displaying hex crash codes to students violates basic error handling usability."
                    },
                    "marking_points": [],
                    "source": "Module 01 Slide 21-22",
                    "verified": True,
                    "verified_output": "High Utility, Deficient Effectiveness."
                },
                {
                    "id": "ins202-fnd-cs1-q2",
                    "course": "INS 202",
                    "topic": "hci_introduction_goals",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case_study", "hci_goals_redesign"],
                    "question": "Apply the HCI goals of 'Safety', 'Usability', and 'Efficiency' to propose three concrete interface improvements to resolve the registration portal's crises.",
                    "options": [],
                    "answer": "The university should implement: (1) Safety (Data Safety & Error Prevention): Introduce state persistence and auto-save so that hitting the browser Back button or experiencing an interrupted network session does not erase selected courses, and add a warning dialog before any destructive cancellation; (2) Usability (Error Recovery & Learnability): Replace the cryptic hex code 'FATAL EXCEPTION 0x80041002' with a clear, actionable human-language error message indicating the exact conflict (e.g., 'Timetable Clash: COS 201 at 10:00 AM overlaps with IFT 211. Please choose an alternative section'); (3) Efficiency & Visual Affordance: Redesign the 'Confirm & Submit' link as a prominent, high-contrast, primary action button placed directly below the course selection summary with a visible progress indicator.",
                    "explanation": "Applies Safety (state persistence), Usability (clear error messaging), and Efficiency (prominent submit button).",
                    "why_wrong": {},
                    "marking_points": [
                        "Applies Safety: auto-saving course selections and preventing accidental data wiping on Back button.",
                        "Applies Usability: translating cryptic hex codes into clear, actionable human language identifying the conflicting courses.",
                        "Applies Efficiency: converting tiny hidden text links into a prominent, high-contrast submit button with progress indicators.",
                        "Shows how these improvements restore student registration completion rates."
                    ],
                    "source": "Module 01 Slides 20, 23, 24",
                    "verified": True,
                    "verified_output": "Safety, Usability, and Efficiency redesign proposals."
                }
            ]
        },
        {
            "id": "ins202-fnd-cs2",
            "scenario": "A fast-growing fintech startup in Lagos launches a peer-to-peer mobile payments app. In version 1.0, to send money to a friend, the user must navigate through 6 separate menus, manually type the recipient's 10-digit account number, memorize the bank's 3-digit sort code, and manually type a transaction memo. The app's customer support center receives over 4,000 phone calls daily from frustrated users who transferred money to the wrong account or got stuck at step 4. In version 2.0, after conducting user-centered research, the team introduces phone contact book syncing, biometric fingerprint confirmation, and a 'Favorites' quick-transfer carousel. Customer support call volume immediately drops by 78%, and daily completed transactions jump from 20,000 to 110,000.",
            "sub_questions": [
                {
                    "id": "ins202-fnd-cs2-q1",
                    "course": "INS 202",
                    "topic": "hci_introduction_goals",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case_study", "business_roi"],
                    "question": "If each customer support phone call costs the fintech company an estimated $15 in personnel and telecom expenses, approximately how much money does the 78% reduction on 4,000 daily calls save the company over a 30-day month?",
                    "options": [
                        "$1,404,000 saved per month (3,120 fewer calls/day * $15 * 30 days)",
                        "$500 saved per month",
                        "$15 saved per month",
                        "Zero dollars because mobile apps eliminate telecom costs entirely"
                    ],
                    "answer": 0,
                    "explanation": "A 78% reduction of 4,000 calls = $4,000 \\times 0.78 = 3,120$ fewer calls per day. At $15 per call, the daily savings is $3,120 \\times 15 = \\$46,800$. Over a 30-day month, total savings equals $46,800 \\times 30 = \\$1,404,000$. This directly illustrates the massive business ROI of good HCI design.",
                    "why_wrong": {
                        "1": "Grossly underestimates call reduction volume and staff overhead.",
                        "2": "Represents the cost of a single phone call, not monthly aggregate savings.",
                        "3": "Customer support agents earn salaries and infrastructure costs remain real."
                    },
                    "marking_points": [],
                    "source": "Module 01 Slide 10",
                    "verified": True,
                    "verified_output": "$1,404,000 monthly savings."
                },
                {
                    "id": "ins202-fnd-cs2-q2",
                    "course": "INS 202",
                    "topic": "hci_introduction_goals",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case_study", "efficiency_and_usability"],
                    "question": "Analyze how the introduction of contact book syncing and the 'Favorites' carousel improved both 'Efficiency' and 'Usability' (specifically memory load) in version 2.0.",
                    "options": [],
                    "answer": "In version 1.0, requiring users to recall and manually type 10-digit account numbers and bank codes placed heavy cognitive strain on human short-term memory (violating George Miller's $7 \\pm 2$ limit) and created extreme friction. Version 2.0 improved Usability by replacing 'recall' with 'recognition': users simply recognize a friend's familiar name or profile picture in their synced contact list. Version 2.0 dramatically improved Efficiency by reducing the multi-step navigation from 6 cumbersome screens down to a 2-tap workflow (tapping the Favorite avatar and confirming via biometrics), reducing task completion time from 90 seconds to under 4 seconds while virtually eliminating costly typographical transfer errors.",
                    "explanation": "Replaces recall with recognition, cuts task time from 90s to 4s, and eliminates memory overload.",
                    "why_wrong": {},
                    "marking_points": [
                        "Identifies that manual typing placed heavy load on limited short-term memory.",
                        "Explains how contact syncing replaces difficult 'recall' with effortless 'recognition'.",
                        "Shows that the 'Favorites' carousel elevates Efficiency by slashing screens, clicks, and transaction time.",
                        "Notes the sharp reduction in user transfer errors and call center volume."
                    ],
                    "source": "Module 01 Slide 23; Module 02 Slide 39, 50",
                    "verified": True,
                    "verified_output": "Efficiency and Usability analysis (recognition vs recall)."
                }
            ]
        }
    ]
}

out_dir = os.path.join("app", "content", "INS 202")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "hci_introduction_goals.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(topic_data, f, indent=2)

print(f"Generated {out_path} with {len(topic_data['questions'])} questions and {len(topic_data['case_studies'])} case studies.")
