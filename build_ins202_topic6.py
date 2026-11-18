import json

data = {
    "course": "INS 202",
    "topic": "ui_ux_design_patterns",
    "summary": "This topic explores Information Architecture (IA), visual organization principles, UI design patterns, and modern prototyping ecosystems. Information architecture classifies content through exact schemes (alphabetical, chronological, geographical—objective, predictable, but requiring known targets) and ambiguous schemes (topical, task-oriented, audience-specific, metaphor-driven—vital for exploration, but subjective). Information structures balance breadth versus depth in hierarchical trees, hypertext meshes, and faceted databases. Card sorting serves as the primary generative (open sorting) and evaluative (closed sorting) user research technique for discovering taxonomies. Visual organization relies on four core principles: Proximity (Gestalt grouping), Alignment (grid anchor lines), Consistency (internal and external UI uniformity), and Contrast (visual hierarchy and CTA salience). Finally, the modern UX workflow utilizes dedicated prototyping tools (Figma, Balsamiq, Sketch, Axure) and evaluates trade-offs of commercial template platforms (WordPress, Webflow, Wix, Colorlib) regarding speed, semantic code quality, responsive reflow, and technical debt.",
    "key_terms": [
        {"term": "Exact Organizational Scheme", "definition": "An objective classification system (alphabetical, chronological, or geographical) where content boundaries are mutually exclusive and item placement is indisputable."},
        {"term": "Ambiguous Organizational Scheme", "definition": "A subjective classification system (topical, task-oriented, audience-specific, or metaphor-driven) where categories are conceptually defined, supporting open exploratory browsing."},
        {"term": "Open Card Sorting", "definition": "A user research method where participants group content cards into categories and create their own descriptive labels to reveal mental models."},
        {"term": "Closed Card Sorting", "definition": "An evaluative research method where participants sort content cards into pre-established, fixed categories to test taxonomy intuitiveness."},
        {"term": "Breadth vs Depth", "definition": "The structural trade-off in hierarchical navigation trees between the number of items per level (breadth) and the number of nested menu tiers (depth)."},
        {"term": "Visual Proximity", "definition": "The Gestalt-derived principle stating that elements placed physically close to each other are perceived as belonging to a unified conceptual group."},
        {"term": "Visual Alignment", "definition": "The principle that every screen element must visually connect to an alignment edge or grid line, creating visual order and smooth eye-tracking scanpaths."},
        {"term": "Visual Contrast", "definition": "Using stark differences in size, weight, and color to establish visual hierarchy and draw immediate attention to primary focal elements."},
        {"term": "Figma", "definition": "A collaborative, cloud-based vector interface design and prototyping tool featuring auto-layout, component variants, and interactive prototyping."},
        {"term": "Webflow vs Wix vs WordPress", "definition": "Web authoring and CMS platforms offering varying balances between visual design freedom, semantic HTML/CSS code generation, and plugin ecosystem trade-offs."}
    ],
    "questions": [
        {
            "id": "ins202-ui-001",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["information-architecture", "organizational-schemes", "exact-schemes"],
            "question": "Which of the following navigation structures represents an 'Exact Organizational Scheme' as defined in Information Architecture?",
            "options": [
                "A nationwide retail store directory organized alphabetically by city name (e.g., Aba, Abuja, Benin, Calabar)",
                "An e-commerce clothing menu divided into 'Workwear', 'Weekend Casual', and 'Party Outfits'",
                "A university homepage navigation section titled 'Resources for Prospective Students'",
                "A banking application button labeled 'Pay Utility Bills'"
            ],
            "answer": 0,
            "explanation": "Exact organizational schemes divide content into well-defined, mutually exclusive, objective categories: alphabetical, chronological, or geographical. A store directory organized alphabetically by city name is an exact geographical/alphabetical scheme. Options 1 (topical), 2 (audience-specific), and 3 (task-oriented) are ambiguous schemes.",
            "why_wrong": {
                "1": "'Workwear' and 'Casual' represent a topical/contextual scheme, which is ambiguous because clothing items can overlap across categories.",
                "2": "'Resources for Prospective Students' is an audience-specific ambiguous scheme.",
                "3": "'Pay Utility Bills' is a task-oriented ambiguous scheme."
            },
            "source": "Module 04 (Content Organization), Slides 2-10: Exact vs Ambiguous Schemes"
        },
        {
            "id": "ins202-ui-002",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["visual-organization", "proximity", "dan-clothing"],
            "question": "In the lecture example of 'Dan's Clothing', the instructor illustrates how a 'mindless' alphabetical list of store links (Accessories, Belts, Caps, Coats, Men's, Women's...) severely damages usability. What core principle of visual organization does such an alphabetical list violate?",
            "options": [
                "Proximity, because conceptually related categories (e.g., Women's clothes, Sales, Account status) are scattered randomly across the list based purely on starting letters",
                "Fitts's Law, because the alphabetical letters require users to move their mouse in a circular spiral path",
                "Consistency, because each item in an alphabetical list must use a different font family",
                "Nielsen's Error Prevention, because alphabetical sorting causes web browsers to produce HTTP 404 errors"
            ],
            "answer": 0,
            "explanation": "The 'Dan's Clothing' case demonstrates that mindless alphabetical sorting scatters conceptually related items across the page, violating the principle of Proximity. Instead of grouping items logically (e.g., Department groupings: Men, Women, Kids; Customer service: Hours, Locations; Transactions: Cart, Checkout), alphabetical sorting forces unrelated items together merely because they share an initial letter.",
            "why_wrong": {
                "1": "Fitts's law deals with target distance and size, not circular spiral mouse paths.",
                "2": "Alphabetical lists do not require different fonts; they fail because of broken conceptual grouping.",
                "3": "Alphabetical sorting is a visual IA choice and has no bearing on web server HTTP 404 response codes."
            },
            "source": "Module 05 (Visual Organization), Slides 3-6: Dan's Clothing & Proximity"
        },
        {
            "id": "ins202-ui-003",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["card-sorting", "user-research", "taxonomies"],
            "question": "An HCI team is planning the menu structure for a large municipal e-government portal. They give 40 citizens index cards representing 80 public services and ask them to group related cards together and write their own label on a blank card for each pile. What research methodology is being employed, and what is its primary outcome?",
            "options": [
                "Open Card Sorting, used generatively to discover the natural mental models and taxonomic vocabulary of end users",
                "Closed Card Sorting, used evaluatively to test whether users can find services within an established departmental hierarchy",
                "Cognitive Walkthrough, used to calculate the mean task completion time of paying municipal parking fines",
                "Heuristic Evaluation, used by usability specialists to audit compliance with ISO standards"
            ],
            "answer": 0,
            "explanation": "In Open Card Sorting, participants sort items into groups and invent their own category names. This generative technique allows researchers to discover how users conceptualize the domain and what terminology makes intuitive sense to them. In contrast, Closed Card Sorting forces cards into pre-established categories to test an existing architecture.",
            "why_wrong": {
                "1": "Closed card sorting does not allow users to create their own labels; categories are fixed in advance.",
                "2": "Cognitive walkthrough is an expert inspection method focusing on action sequences, not card-based taxonomy sorting.",
                "3": "Heuristic evaluation is performed by usability experts inspecting screens, not end citizens sorting physical cards."
            },
            "source": "Module 04 (Content Organization), Card Sorting Methodology"
        },
        {
            "id": "ins202-ui-004",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["information-architecture", "breadth-vs-depth"],
            "question": "When designing a hierarchical menu structure for an e-commerce website with 500 product categories, what is the primary usability risk of designing a 'narrow-and-deep' hierarchy (e.g., 2 options per level across 9 nested levels) compared to a 'broad-and-shallow' hierarchy (e.g., 8-10 options per level across 3 levels)?",
            "options": [
                "Narrow-and-deep hierarchies force excessive clicking, increase user disorientation ('getting lost'), and rely on guessing at high-level ambiguous nodes",
                "Narrow-and-deep hierarchies violate Miller's Magic Number 7 +/- 2 by presenting too many choices simultaneously",
                "Broad-and-shallow hierarchies take significantly longer to render in web browsers due to DOM nesting limitations",
                "Broad-and-shallow hierarchies prevent web crawlers from indexing deeper pages in search engines"
            ],
            "answer": 0,
            "explanation": "Extensive HCI research shows that users perform substantially better with broad-and-shallow hierarchies than narrow-and-deep ones. Deep hierarchies require excessive navigation clicks, hide lower-level content, and force users to make guesses at top-level nodes; if an early guess is wrong, recovering requires deep backtracking. Broad-and-shallow structures expose navigational scent immediately.",
            "why_wrong": {
                "1": "Miller's 7 +/- 2 applies to short-term memory capacity, not visual recognition menus where items are visible on screen.",
                "2": "DOM rendering performance is completely unaffected by whether a menu is shallow or deep.",
                "3": "Search engine crawlers traverse broad hierarchies much faster and index pages more reliably than deeply buried link trees."
            },
            "source": "Module 04 (Content Organization), Organizational Structures (Breadth vs Depth)"
        },
        {
            "id": "ins202-ui-005",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["visual-organization", "principles", "alignment"],
            "question": "Which visual organization principle states that every element placed on a user interface should visually connect to a horizontal or vertical grid line with at least one other element on the screen?",
            "options": [
                "Alignment",
                "Proximity",
                "Affordance",
                "Symmetry"
            ],
            "answer": 0,
            "explanation": "Alignment is the visual principle that nothing should be placed arbitrarily on a screen; every item should have a visual connection to something else. Clean horizontal and vertical alignment creates visual anchor lines, reduces visual clutter, and guides the eye smoothly down scanning paths.",
            "why_wrong": {
                "1": "Proximity governs the distance between related items.",
                "2": "Affordance refers to the visual property that indicates how an object can be used (e.g., a 3D button affordance).",
                "3": "Symmetry requires balanced mirrored layouts, whereas alignment merely requires shared grid edges."
            },
            "source": "Module 05 (Visual Organization), Slide 2: Four Principles of Visual Organization"
        },
        {
            "id": "ins202-ui-006",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["prototyping-tools", "figma", "balsamiq"],
            "question": "A UX design agency is kicking off an interface project. In the first week, they want to sketch out raw layout ideas and workflow logic without getting distracted by colors, typography, or UI polish. Later, they need to create interactive, pixel-perfect, cloud-collaborative components. Which two tools from the course materials correspond best to these two phases?",
            "options": [
                "Balsamiq for rapid low-fidelity wireframing, followed by Figma for high-fidelity collaborative prototyping",
                "Adobe Photoshop for wireframing, followed by Notepad++ for production code",
                "Microsoft Word for paper sketching, followed by Wix for high-fidelity code export",
                "Webflow for low-fidelity sketches, followed by Axure RP for vector icon creation"
            ],
            "answer": 0,
            "explanation": "Module 07 explicitly reviews UX prototyping tools: Balsamiq is designed specifically for rapid, low-fidelity wireframing (simulating hand-drawn sketches to keep focus on layout and content rather than aesthetics), while Figma is the industry standard cloud-based tool for high-fidelity vector UI design, design systems, and interactive clickable prototypes.",
            "why_wrong": {
                "1": "Photoshop is a bitmap photo editor unsuited for wireframing, and Notepad++ is a raw text editor.",
                "2": "Word is a word processor, and Wix is a website builder, not a collaborative UI prototyping tool.",
                "3": "Webflow produces production HTML/CSS websites rather than low-fi sketches, and Axure is not a vector icon creator."
            },
            "source": "Module 07 (Prototyping), Slide 39: Prototyping Tools"
        },
        {
            "id": "ins202-ui-007",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "true_false_why",
            "difficulty": 2,
            "tags": ["templates", "tradeoffs", "webflow-wordpress"],
            "question": "Using a pre-built commercial website template (such as from WordPress, Wix, or Colorlib) guarantees that the resulting application will have zero accessibility barriers and optimal page-load performance.",
            "options": [
                "True",
                "False"
            ],
            "answer": 1,
            "explanation": "False. While commercial templates offer rapid deployment and pre-built styling, they frequently suffer from severe code bloat (unnecessary JavaScript/CSS libraries), rigid HTML structures that break responsive reflow, and widespread accessibility violations (such as missing ARIA attributes, unlabelled icons, and poor color contrast) that must be audited and remedied by developers.",
            "why_wrong": {
                "0": "Templates often introduce bloat and hidden accessibility violations; they never guarantee zero accessibility barriers or optimal performance."
            },
            "source": "Student Notebook ('templates: wordpress, figma, wix, webflow, color-lib') & UI/UX Architectural Trade-offs"
        },
        {
            "id": "ins202-ui-008",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["design-patterns", "breadcrumbs", "navigation"],
            "question": "Consider the following navigation trail displayed at the top of an online store: 'Home > Electronics > Audio > Headphones > Wireless Noise-Cancelling'. What is this UI design pattern called, and what specific usability benefit does it provide?",
            "options": [
                "Breadcrumb trail; it displays the user's current location within the site hierarchy and provides one-click shortcuts to parent levels",
                "Hamburger navigation; it compresses menu options into a single 3-bar icon to conserve mobile screen space",
                "Carousel slider; it automatically rotates promotional banners across the top of the viewport",
                "Accordion panel; it collapses secondary content vertically until toggled by the user"
            ],
            "answer": 0,
            "explanation": "A breadcrumb trail is a standard hierarchical navigation design pattern. It provides two major benefits: (1) it establishes situational awareness by indicating exactly where the user is within the site's information architecture, and (2) it enables rapid one-click navigation back to any ancestor category without hitting the browser Back button repeatedly.",
            "why_wrong": {
                "1": "A hamburger menu is an icon of three horizontal stripes hiding off-canvas links, not a hierarchical trail.",
                "2": "Carousels rotate multimedia slides or banners horizontally.",
                "3": "Accordions are vertically stacked headers that expand and collapse to reveal body content."
            },
            "source": "Module 06 (Navigation), Slide 2: Page-Level Navigation & Standard UI Design Patterns"
        },
        {
            "id": "ins202-ui-009",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "cloze",
            "difficulty": 2,
            "tags": ["visual-organization", "principles", "cloze"],
            "question": "Complete the statements regarding the four principles of visual organization:\nThe principle of [blank1] dictates that related items should be grouped physically together to form distinct visual units. The principle of [blank2] dictates that every item on a page should line up with an invisible grid edge. The principle of [blank3] ensures that recurring elements (like button shapes and headers) remain uniform across all pages, while [blank4] uses distinct visual differences to draw attention to primary calls to action.",
            "answer": ["proximity", "alignment", "consistency", "contrast"],
            "explanation": "Module 05 defines the four universal principles of visual organization: Proximity (grouping related items), Alignment (shared grid lines), Consistency (uniform styling and behavior), and Contrast (making distinct elements visually prominent).",
            "source": "Module 05 (Visual Organization), Slide 2: Four Principles of Visual Organization"
        },
        {
            "id": "ins202-ui-010",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "matching",
            "difficulty": 3,
            "tags": ["prototyping-tools", "matching"],
            "question": "Match each tool or platform from the course curriculum to its primary architectural characteristic:",
            "options": [
                "Figma",
                "Balsamiq",
                "Webflow",
                "WordPress"
            ],
            "answer": [
                "Cloud-based collaborative vector UI design and high-fidelity interactive component prototyping",
                "Low-fidelity wireframing software intentionally simulating hand-drawn sketches for rapid concept validation",
                "Visual web design platform that generates semantic, production-ready HTML5, CSS3, and JavaScript code",
                "Database-driven Content Management System (CMS) powering themes, dynamic templates, and blog architectures"
            ],
            "explanation": "Figma is the industry leader for collaborative vector UI design. Balsamiq focuses on sketch-like low-fi wireframing. Webflow generates production-clean semantic front-end code visually. WordPress is the premier CMS for dynamic template-driven sites.",
            "source": "Module 07 (Slide 39) & Student Notebook ('templates: wordpress, figma, wix, webflow, color-lib')"
        },
        {
            "id": "ins202-ui-011",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "sequencing",
            "difficulty": 3,
            "tags": ["user-centered-design", "workflow", "sequencing"],
            "question": "Arrange the following UI/UX design workflow stages in the correct logical sequence from earliest to latest:",
            "options": [
                "Conduct Open Card Sorting with target users to discover information architecture categories",
                "Create low-fidelity paper wireframes or Balsamiq sketches to validate layout and content hierarchy",
                "Build interactive vector prototypes with design system components in Figma",
                "Implement production front-end code using semantic HTML/CSS in Webflow or a CMS template"
            ],
            "answer": [0, 1, 2, 3],
            "explanation": "A disciplined UCD process begins with user research / IA discovery (card sorting) to determine content structure, progresses to rapid low-fidelity wireframing (paper or Balsamiq) to validate layouts cheaply, advances to high-fidelity interactive component prototyping (Figma), and concludes with front-end implementation (Webflow/CMS).",
            "source": "Module 04, 05, 07 Integrated Design Process"
        },
        {
            "id": "ins202-ui-012",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["information-architecture", "schemes", "definition"],
            "question": "What is the difference between an Exact Organizational Scheme and an Ambiguous Organizational Scheme?",
            "answer": "An Exact Scheme divides information into objective, mutually exclusive, well-defined categories (alphabetical, chronological, geographical) where item placement is indisputable. An Ambiguous Scheme divides information into subjective, conceptual categories (topical, task-oriented, audience-specific, metaphor-driven) where boundaries can overlap but exploratory browsing is supported.",
            "explanation": "Exact schemes are best when users know precisely what they are looking for; ambiguous schemes are best when users need guidance or have broad informational goals.",
            "source": "Module 04 (Content Organization), Slides 2-10"
        },
        {
            "id": "ins202-ui-013",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["card-sorting", "definition"],
            "question": "What is the key methodological difference between Open Card Sorting and Closed Card Sorting?",
            "answer": "In Open Card Sorting, participants sort content cards into piles and create their own category names (used generatively to discover mental models and taxonomy). In Closed Card Sorting, participants sort cards into pre-established, fixed categories (used evaluatively to test the clarity of an existing structure).",
            "explanation": "Open sorting creates the architecture; closed sorting validates it.",
            "source": "Module 04 (Content Organization), Card Sorting"
        },
        {
            "id": "ins202-ui-014",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["visual-organization", "principles"],
            "question": "Name and briefly define the four foundational principles of visual organization presented in INS 202.",
            "answer": "1. Proximity: Grouping conceptually related items close together.\n2. Alignment: Connecting every element to a visual grid line or edge.\n3. Consistency: Maintaining uniform visual styles, layouts, and behaviors throughout the interface.\n4. Contrast: Making elements that differ visually distinct to establish clear focal hierarchy.",
            "explanation": "These four principles ensure that visual layout directly communicates information architecture to the user.",
            "source": "Module 05 (Visual Organization), Slide 2"
        },
        {
            "id": "ins202-ui-015",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["templates", "tradeoffs"],
            "question": "What are two advantages and two disadvantages of utilizing pre-built website templates (such as WordPress themes or Colorlib templates)?",
            "answer": "Advantages:\n1. Rapid time-to-market / low initial development cost.\n2. Built-in responsive design and pre-tested UI patterns.\n\nDisadvantages:\n1. Code bloat (loading unused JavaScript/CSS libraries slowing performance).\n2. Rigid customization constraints and potential hidden accessibility violations.",
            "explanation": "Templates provide speed at the expense of architectural flexibility, performance optimization, and custom brand identity.",
            "source": "Student Notebook ('templates: wordpress, figma, wix, webflow, color-lib')"
        },
        {
            "id": "ins202-ui-016",
            "course": "INS 202",
            "topic": "ui_ux_design_patterns",
            "type": "explain",
            "difficulty": 3,
            "tags": ["information-architecture", "card-sorting", "case-study"],
            "question": "Explain how an Information Architect should combine Open Card Sorting and Closed Card Sorting when restructuring a chaotic university website. Describe the specific purpose of each phase and how the outputs of the first phase feed into the second.",
            "answer": "When restructuring a disorganized university website, an Information Architect should execute a two-stage card sorting workflow:\n\n1. Phase 1: Open Card Sorting (Generative Exploration)\n- Purpose: To uncover the natural mental models, conceptual groupings, and vocabulary of real users (students, faculty, applicants) without imposing administrative department biases.\n- Execution: Researchers provide ~50–80 cards representing individual university web tasks and content items (e.g., 'Pay Tuition', 'Transcript Request', 'Library Database Access', 'Hostel Booking'). Participants independently sort cards into logical clusters and write their own descriptive category titles.\n- Output: Cluster analysis matrix and common taxonomic labels revealing how users naturally think about the university's services.\n\n2. Phase 2: Synthesis & Information Architecture Draft\n- The architect synthesizes the Open Card Sorting results to draft a standardized menu hierarchy with clear, non-overlapping categories.\n\n3. Phase 3: Closed Card Sorting (Evaluative Validation)\n- Purpose: To test whether the newly synthesized categories are intuitive, mutually exclusive, and predictable for a fresh cohort of users.\n- Execution: A new group of participants is given the content cards and instructed to place each card into the fixed categories established in Phase 2.\n- Output: Placement agreement scores. If certain cards have low agreement or are placed inconsistently, it reveals ambiguous labels or overlapping category definitions that require immediate refinement before building the site navigation.",
            "explanation": "Open sorting generates the category taxonomy; closed sorting verifies its usability and robustness.",
            "marking_points": [
                "Defines Open Card Sorting as a generative method where users create their own categories and labels",
                "Explains that Open Card Sorting discovers user mental models and avoids internal organizational bias",
                "Explains the synthesis step that creates the proposed navigation taxonomy",
                "Defines Closed Card Sorting as an evaluative validation method using pre-established categories",
                "Describes how placement agreement rates in Closed Sorting validate or expose weaknesses in the architecture"
            ],
            "source": "Module 04 (Content Organization), Card Sorting Methodology"
        }
    ],
    "case_studies": [
        {
            "id": "ins202-ui-cs1",
            "scenario": "Nile University's student web portal currently contains 120 disorganized links on its homepage. The administration hired an HCI consultant to redesign the portal. The consultant conducted an open card sorting session with 30 undergraduate students, followed by a closed card sorting test. The findings revealed that students overwhelmingly rejected the university's internal administrative structure (e.g., categorizing 'Course Add/Drop' under 'Office of the Registrar' and 'Hostel Maintenance' under 'Department of Works and Physical Planning'). Instead, students grouped items into high-level task-oriented categories: 'Academics & Registration', 'Finance & Fees', 'Campus Life & Housing', and 'Student Support'. Furthermore, the consultant restructured the navigation from a deep 7-level nested menu into a 3-level broad-and-shallow hierarchy with clear breadcrumb navigation.",
            "sub_questions": [
                {
                    "id": "ins202-ui-cs1-q1",
                    "course": "INS 202",
                    "topic": "ui_ux_design_patterns",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["information-architecture", "schemes", "case-study"],
                    "question": "What type of organizational scheme did the university originally use, and what scheme did the students successfully establish through the open card sorting study?",
                    "options": [
                        "Originally an internal organizational/administrative scheme; replaced by a user-centered task-oriented scheme",
                        "Originally an exact chronological scheme; replaced by an exact geographical scheme",
                        "Originally an ambiguous metaphor scheme; replaced by an exact alphabetical scheme",
                        "Originally a hypertext mesh; replaced by a relational database schema"
                    ],
                    "answer": 0,
                    "explanation": "Universities often mistakenly organize portals around their internal administrative organogram (Registrar, Bursary, Works), which reflects how the university is managed rather than how students think. Through open card sorting, students established a user-centered, task-oriented ambiguous scheme ('Academics & Registration', 'Campus Life & Housing') focused on student workflows.",
                    "why_wrong": {
                        "1": "Neither structure was sorted by timestamps (chronological) or physical coordinates (geographical).",
                        "2": "The original was not a metaphor (like a virtual desktop), and students did not demand an alphabetical directory.",
                        "3": "These describe technical hyperlinking or database models, not Information Architecture classification schemes."
                    },
                    "source": "Module 04 (Content Organization), Slides 2-10: Schemes"
                },
                {
                    "id": "ins202-ui-cs1-q2",
                    "course": "INS 202",
                    "topic": "ui_ux_design_patterns",
                    "type": "mcq",
                    "difficulty": 4,
                    "tags": ["navigation", "breadth-depth", "case-study"],
                    "question": "Why did shifting from a 7-level deep menu to a 3-level broad-and-shallow menu with breadcrumbs significantly reduce student task failure rates?",
                    "options": [
                        "Broad-and-shallow structures reduce navigational depth and guessing, while breadcrumbs maintain context and provide instant ancestor backtracking",
                        "Deep menus require too much RAM memory on modern mobile smartphones, causing browsers to freeze",
                        "Shallow menus completely eliminate the need for visual search and Gestalt proximity",
                        "Breadcrumb navigation replaces the need for search bars and databases"
                    ],
                    "answer": 0,
                    "explanation": "In deep menus, users must drill through many speculative tiers; making a single wrong choice forces tedious multi-level backtracking. Broad-and-shallow hierarchies expose categories at higher levels, providing strong navigational scent. Adding breadcrumbs reinforces orientation and enables instant one-tap navigation back to parent categories.",
                    "why_wrong": {
                        "1": "Menu depth has zero noticeable impact on smartphone RAM memory consumption.",
                        "2": "Shallow menus still require effective visual layout, visual search, and proximity grouping.",
                        "3": "Breadcrumbs complement search and faceted filtering; they do not replace database search engines."
                    },
                    "source": "Module 04 & Module 06 (Navigation Systems)"
                }
            ]
        },
        {
            "id": "ins202-ui-cs2",
            "scenario": "A health-tech startup in Abuja is launching 'DokitaOnline', a telehealth platform connecting patients with specialist doctors. The development team debates whether to use a pre-built WordPress theme from Colorlib, an absolute-positioning site builder like Wix, or design custom components in Figma and export via Webflow.\n\nThe lead developer argues: 'Let's just download a $40 WordPress theme from Colorlib; it's already built, has sliders, and will save us 4 weeks.' However, the UX examiner notes that the telemedicine platform requires HIPAA-like patient privacy, extreme mobile responsiveness on low-end Android phones running Opera Mini, strict WCAG 2.1 AA accessibility for visually impaired patients, and precise custom booking flows.",
            "sub_questions": [
                {
                    "id": "ins202-ui-cs2-q1",
                    "course": "INS 202",
                    "topic": "ui_ux_design_patterns",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["templates", "tradeoffs", "webflow-vs-wordpress", "case-study"],
                    "question": "Evaluate the lead developer's proposal to use a pre-built commercial WordPress theme from Colorlib for this health-tech platform. Identify three significant HCI, architectural, and accessibility risks associated with this decision.",
                    "answer": "While the pre-built WordPress theme offers rapid initial setup and low upfront cost, it presents severe risks for a medical platform:\n\n1. Code Bloat and Performance Degradation on Low-End Mobile Devices: Pre-built themes bundle numerous unneeded JavaScript sliders, heavy animation libraries, and bloated CSS frameworks. On low-end Android smartphones running on 3G networks in Nigeria, this causes massive page weight, high latency, and browser stutter, directly violating HCI efficiency goals.\n\n2. Hidden Accessibility (WCAG 2.1 AA) Failures: Commercial themes frequently contain unlabelled icon buttons, poor default color contrast ratios, broken heading hierarchies (e.g., jumping from H1 to H4 for styling reasons), and inaccessible form modals that break screen reader navigation for visually impaired patients.\n\n3. Rigid Layout Constraints and Custom Workflow Friction: Telehealth booking requires multi-step triage workflows and secure data validation. Modifying a rigid pre-built WordPress theme to accommodate non-standard custom booking interactions often results in brittle CSS overrides ('!important' hacks) and broken responsive reflow across device screen sizes.",
                    "explanation": "Off-the-shelf templates carry heavy technical and UX debt when applied to specialized, accessible domains.",
                    "marking_points": [
                        "Identifies code bloat and performance penalties affecting mobile users on constrained networks",
                        "Highlights accessibility risks (WCAG failures, screen reader incompatibility, unlabelled form elements)",
                        "Discusses the rigidity of pre-built templates when implementing custom medical workflows",
                        "Mentions maintenance and technical debt arising from modifying third-party themes"
                    ],
                    "source": "Student Notebook ('templates: wordpress, figma, wix, webflow, color-lib') & UI/UX Architectural Trade-offs"
                },
                {
                    "id": "ins202-ui-cs2-q2",
                    "course": "INS 202",
                    "topic": "ui_ux_design_patterns",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["prototyping-tools", "figma", "webflow", "case-study"],
                    "question": "Why would designing the interface components in Figma and building them with Webflow be superior to using Wix for the 'DokitaOnline' medical platform?",
                    "options": [
                        "Figma enables collaborative design system component prototyping, and Webflow generates clean, semantic, responsive HTML/CSS code adhering to the box model, whereas Wix relies heavily on absolute positioning",
                        "Wix is only compatible with Apple iOS devices and cannot be accessed from Android smartphones",
                        "Figma automatically executes all PHP backend database queries without requiring a server",
                        "Webflow completely eliminates the need for human doctors by using automated AI diagnostic scripts"
                    ],
                    "answer": 0,
                    "explanation": "Figma provides professional vector UI design, design tokens, and component variants for strict UI consistency. Webflow translates visual layouts directly into clean, semantic, responsive HTML5/CSS3 adhering strictly to the CSS box model. In contrast, Wix has historically relied on free-form absolute positioning, which can cause erratic reflow across diverse mobile screen dimensions.",
                    "why_wrong": {
                        "1": "Wix sites run in any modern web browser across iOS and Android.",
                        "2": "Figma is a front-end prototyping tool and does not execute back-end PHP database queries.",
                        "3": "Webflow is a front-end web design tool and has nothing to do with replacing medical doctors."
                    },
                    "source": "Student Notebook & Prototyping Platform Analysis"
                }
            ]
        }
    ]
}

with open("app/content/INS 202/ui_ux_design_patterns.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Saved ui_ux_design_patterns.json successfully!")
