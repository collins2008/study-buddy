# add_all_flashcards.py - Comprehensive Flashcard Generation for IFT 205, INS 202, and ENT 211
import json
import os

IFT205_FLASHCARDS = {
    "it_foundations_building_blocks.json": [
        {
            "id": "ift205-fnd-fc01",
            "course": "IFT 205",
            "topic": "IT Foundations: Hardware, Software & People",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "definition", "building-blocks"],
            "question": "What is Information Technology (IT), and what are its three fundamental sociotechnical building blocks?",
            "answer": "Information Technology (IT) is the study, design, development, implementation, support, and management of computer-based information systems.\nIts three core building blocks are:\n1. Hardware: Physical electronic circuitry, processors, storage, and peripherals.\n2. Software: Programs, algorithms, and operating instructions directing hardware.\n3. People: End-users who supply data and IT professionals who design, secure, and maintain systems.",
            "explanation": "Fundamental definition and sociotechnical model from IFT 205 Lecture 1, Slide 3-4.",
            "why_wrong": {},
            "source": "IFT 205 Lecture 1 Slides 3-4"
        },
        {
            "id": "ift205-fnd-fc02",
            "course": "IFT 205",
            "topic": "IT Foundations: Hardware, Software & People",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "data-vs-information", "context"],
            "question": "How does raw Data fundamentally differ from Information?",
            "answer": "- Data: Raw, unorganized, unprocessed facts, numbers, symbols, or observations lacking contextual meaning (e.g., `105.8`, `A+`, `404`).\n- Information: Data that has been processed, organized, structured, and contextualized so that it possesses meaning and utility for decision-making (e.g., `Patient Body Temperature: 105.8°F - Severe Hyperthermia`).",
            "explanation": "Core DIKW hierarchy concept covered in IFT 205 Week 2 & Week 5.",
            "why_wrong": {},
            "source": "IFT 205 Week 2 & Week 5 Slides"
        },
        {
            "id": "ift205-fnd-fc03",
            "course": "IFT 205",
            "topic": "IT Foundations: Hardware, Software & People",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "ipos", "cycle"],
            "question": "Name and describe the four sequential stages of the Information Processing Cycle (IPOS).",
            "answer": "1. Input: Capturing raw data from users or sensors via input devices (keyboard, barcode scanner, microphone).\n2. Processing: Manipulating, computing, and transforming input data within the CPU and memory.\n3. Output: Presenting processed information to humans in a usable format (monitors, printers, speakers).\n4. Storage: Persisting data, files, and programs permanently on secondary storage media for future retrieval.",
            "explanation": "The foundational computing paradigm (IPOS) covered in IFT 205 Lecture 1, Slide 6.",
            "why_wrong": {},
            "source": "IFT 205 Lecture 1 Slide 6"
        },
        {
            "id": "ift205-fnd-fc04",
            "course": "IFT 205",
            "topic": "IT Foundations: Hardware, Software & People",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "batch-vs-realtime", "processing"],
            "question": "Contrast Batch Processing with Real-Time Processing, providing an enterprise example of each.",
            "answer": "- Batch Processing: Transactions are accumulated over a specific time window and processed together as a single batch during scheduled off-peak hours without user interaction (e.g., monthly university payroll calculation or utility bill generation).\n- Real-Time (OLTP) Processing: Transactions are validated, processed, and confirmed instantaneously as they occur, updating database records with zero latency (e.g., ATM cash withdrawals or airline flight reservations).",
            "explanation": "Data processing paradigms detailed in IFT 205 Week 5 slides.",
            "why_wrong": {},
            "source": "IFT 205 Week 5 Slides; Data Processing"
        },
        {
            "id": "ift205-fnd-fc05",
            "course": "IFT 205",
            "topic": "IT Foundations: Hardware, Software & People",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "validation-vs-verification", "data-quality"],
            "question": "Distinguish between Data Validation and Data Verification.",
            "answer": "- Data Validation: An automated, programmatic check performed by software to ensure entered data conforms to predefined constraints, formats, data types, and reasonable ranges (e.g., checking that an email contains `@` or age is between 1-120).\n- Data Verification: A procedure (human proofreading or double-entry comparison) checking that entered data exactly matches the authentic original source document.",
            "explanation": "Input controls and data governance covered in IFT 205 Week 5.",
            "why_wrong": {},
            "source": "IFT 205 Week 5 Slides"
        },
        {
            "id": "ift205-fnd-fc06",
            "course": "IFT 205",
            "topic": "IT Foundations: Hardware, Software & People",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "data-quality", "dimensions"],
            "question": "List and define the four critical dimensions of Data Quality.",
            "answer": "1. Accuracy: Data is correct, truthful, and reliably reflects real-world events.\n2. Completeness: All required data values and attributes are present without missing fields.\n3. Consistency: Data does not conflict across different tables, files, or departmental databases.\n4. Timeliness: Data is recorded, processed, and available quickly enough to remain relevant for decision-making.",
            "explanation": "Core dimensions of data governance in IFT 205 Week 5.",
            "why_wrong": {},
            "source": "IFT 205 Week 5 Slides"
        },
        {
            "id": "ift205-fnd-fc07",
            "course": "IFT 205",
            "topic": "IT Foundations: Hardware, Software & People",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "people-element", "roles"],
            "question": "Why is the 'People' component considered the most critical building block of an IT system?",
            "answer": "Hardware and software are merely inert physical and logical tools. People supply the initial data, define business objectives, design the algorithms, interpret the output, and make executive decisions based on system results.\nAdditionally, human error (misconfiguration, weak passwords, accidental deletion) remains the leading cause of security breaches and operational failures.",
            "explanation": "Sociotechnical perspectives in IFT 205 Lecture 1.",
            "why_wrong": {},
            "source": "IFT 205 Lecture 1 Slide 4"
        },
        {
            "id": "ift205-fnd-fc08",
            "course": "IFT 205",
            "topic": "IT Foundations: Hardware, Software & People",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "terminology", "networks"],
            "question": "How does IFT 205 distinguish between a Network, the Internet, Networking, and Networkers?",
            "answer": "- Computer Network: Two or more interconnected devices sharing hardware, data, and software resources.\n- The Internet: The global public network of interconnected computer networks communicating via standard TCP/IP protocols.\n- Networking: The engineering discipline and technical process of designing, configuring, and managing network communication links.\n- Networkers: The human administrators and network engineers who install and maintain network infrastructure.",
            "explanation": "Core terminology taxonomy introduced in IFT 205 Lecture 1 & Week 6.",
            "why_wrong": {},
            "source": "IFT 205 Lecture 1 & Week 6 Slides"
        }
    ],

    "computer_hardware_architecture.json": [
        {
            "id": "ift205-hwd-fc01",
            "course": "IFT 205",
            "topic": "Hardware Components: Input, CPU, Memory & Storage",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "cpu", "cu-vs-alu"],
            "question": "What are the two primary functional units inside a Central Processing Unit (CPU), and what are their duties?",
            "answer": "1. Control Unit (CU): Acts as the CPU's supervisor. It fetches binary instructions from RAM, decodes them, and manages the timing and data flow across all system buses and components.\n2. Arithmetic Logic Unit (ALU): Executes all mathematical arithmetic calculations (addition, subtraction, multiplication) and logical comparisons (AND, OR, NOT, `>`, `<`, `=`).",
            "explanation": "Internal CPU architecture from IFT 205 Lecture 1, Slide 8.",
            "why_wrong": {},
            "source": "IFT 205 Lecture 1 Slide 8"
        },
        {
            "id": "ift205-hwd-fc02",
            "course": "IFT 205",
            "topic": "Hardware Components: Input, CPU, Memory & Storage",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "machine-cycle", "cpu"],
            "question": "Explain the four steps of the CPU Machine Instruction Cycle.",
            "answer": "1. Fetch: The Control Unit retrieves the next instruction from RAM into the instruction register.\n2. Decode: The CU interprets the opcode to determine what operation must be performed and locates required data operands.\n3. Execute: The ALU or CU carries out the requested operation (e.g., adding numbers or loading data).\n4. Store (Writeback): The result of the execution is saved back into an internal CPU register or main RAM address.",
            "explanation": "Fetch-Decode-Execute cycle explained in IFT 205 Lecture 1.",
            "why_wrong": {},
            "source": "IFT 205 Lecture 1 Slides"
        },
        {
            "id": "ift205-hwd-fc03",
            "course": "IFT 205",
            "topic": "Hardware Components: Input, CPU, Memory & Storage",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "ram-vs-rom", "memory"],
            "question": "Contrast RAM with ROM across volatility, speed, and typical use cases.",
            "answer": "- RAM (Random Access Memory): Volatile primary memory; loses all data instantly when power is cut. High-speed read/write access used to hold active operating system components, open applications, and working data.\n- ROM (Read-Only Memory): Non-volatile permanent memory; retains stored contents indefinitely without power. Stores essential firmware (BIOS/UEFI) and hardware startup bootstrap routines; cannot be easily overwritten during normal operation.",
            "explanation": "Primary memory classification in IFT 205 Lecture 1, Slide 9.",
            "why_wrong": {},
            "source": "IFT 205 Lecture 1 Slide 9"
        },
        {
            "id": "ift205-hwd-fc04",
            "course": "IFT 205",
            "topic": "Hardware Components: Input, CPU, Memory & Storage",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "ssd-vs-hdd", "storage"],
            "question": "Contrast Solid-State Drives (SSDs) with Hard Disk Drives (HDDs) in physical mechanism, speed, and durability.",
            "answer": "- SSD (Solid-State Drive): Utilizes non-volatile NAND flash memory chips with zero moving parts. Delivers near-instant access times (500–7,000+ MB/s), completely silent operation, low power consumption, and high resistance to physical shock.\n- HDD (Hard Disk Drive): Uses rotating magnetic platters and mechanical read/write actuator heads. Slower access speeds (80–200 MB/s), audible spinning noise, and highly susceptible to physical head crashes if dropped.",
            "explanation": "Secondary storage technologies in IFT 205 Lecture 1, Slide 10 & Week 5.",
            "why_wrong": {},
            "source": "IFT 205 Lecture 1 Slide 10"
        },
        {
            "id": "ift205-hwd-fc05",
            "course": "IFT 205",
            "topic": "Hardware Components: Input, CPU, Memory & Storage",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "motherboard", "system-buses"],
            "question": "What is the Motherboard, and what are the specific functions of the Address, Data, and Control buses?",
            "answer": "The Motherboard is the central printed circuit board (PCB) connecting the CPU, RAM, expansion cards, and storage devices.\nIt links components using three system buses:\n- Data Bus: Bi-directional lines carrying the actual data being read or written.\n- Address Bus: Uni-directional lines carrying memory addresses from the CPU to identify specific physical memory cells.\n- Control Bus: Transmits synchronization clock pulses, read/write commands, and interrupt signals.",
            "explanation": "System bus anatomy from IFT 205 Lecture 1, Slide 12.",
            "why_wrong": {},
            "source": "IFT 205 Lecture 1 Slide 12"
        },
        {
            "id": "ift205-hwd-fc06",
            "course": "IFT 205",
            "topic": "Hardware Components: Input, CPU, Memory & Storage",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "cache", "memory-hierarchy"],
            "question": "What is Cache Memory, and why is it divided into levels (L1, L2, L3)?",
            "answer": "Cache memory is ultra-fast Static RAM (SRAM) placed on or next to the CPU to store frequently accessed instructions and data, reducing the latency of accessing slower main DRAM.\n- L1 Cache: Smallest (32–128 KB), fastest, integrated directly into each CPU core running at full core clock speed.\n- L2 Cache: Slightly larger (512 KB–2 MB) and slightly slower than L1.\n- L3 Cache: Largest (8–64+ MB), shared across all CPU cores on the processor die.",
            "explanation": "Memory hierarchy and cache performance in IFT 205 Lecture 1.",
            "why_wrong": {},
            "source": "IFT 205 Lecture 1 Slides"
        },
        {
            "id": "ift205-hwd-fc07",
            "course": "IFT 205",
            "topic": "Hardware Components: Input, CPU, Memory & Storage",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "backup", "3-2-1-rule"],
            "question": "Explain the 3-2-1 Backup Rule for data protection and disaster recovery.",
            "answer": "The 3-2-1 Backup Rule requires:\n- 3 total copies of critical data (1 primary working copy + 2 backup copies).\n- 2 different physical media types (e.g., internal SSD + external magnetic drive or local NAS).\n- 1 copy kept completely offsite (e.g., in a secure cloud repository or remote geographical facility) to survive fire, flood, or site theft.",
            "explanation": "Disaster recovery strategy covered in IFT 205 Week 5 storage slides.",
            "why_wrong": {},
            "source": "IFT 205 Week 5 Slides"
        },
        {
            "id": "ift205-hwd-fc08",
            "course": "IFT 205",
            "topic": "Hardware Components: Input, CPU, Memory & Storage",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "backup-types", "incremental-differential"],
            "question": "Contrast Incremental Backups with Differential Backups in speed and restoration complexity.",
            "answer": "- Incremental Backup: Copies only files created or modified since the last backup of any kind (Full or Incremental). Fastest to perform and uses the least storage, but restoration requires restoring the Full backup plus every consecutive incremental set in chronological order.\n- Differential Backup: Copies all files created or modified since the last Full backup. Takes longer to back up as time progresses, but restoration is simpler, requiring only two sets: the last Full backup and the latest Differential backup.",
            "explanation": "Backup methodologies detailed in IFT 205 Week 5.",
            "why_wrong": {},
            "source": "IFT 205 Week 5 Slides"
        }
    ],

    "operating_systems_software.json": [
        {
            "id": "ift205-ops-fc01",
            "course": "IFT 205",
            "topic": "Operating Systems, System vs Application Software",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "system-vs-application", "software"],
            "question": "Contrast System Software with Application Software, giving two examples of each.",
            "answer": "- System Software: Low-level programs designed to run, manage, and maintain computer hardware resources, providing a stable platform upon which application software can execute (e.g., Microsoft Windows 11, Linux kernel, device drivers, disk utilities).\n- Application Software: End-user programs designed to help humans perform specific productive, business, creative, or communication tasks (e.g., Microsoft Word, Google Chrome, Zoom, Adobe Illustrator).",
            "explanation": "Software taxonomy in IFT 205 Lecture 1, Slide 14 & Software/OS Slide 3.",
            "why_wrong": {},
            "source": "IFT 205 Software and Operating Systems Slides 3-4"
        },
        {
            "id": "ift205-ops-fc02",
            "course": "IFT 205",
            "topic": "Operating Systems, System vs Application Software",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "os-functions", "management"],
            "question": "List five primary resource management functions performed by an Operating System.",
            "answer": "1. Processor Management: Allocating CPU time slices to active processes using scheduling algorithms.\n2. Memory Management: Allocating and tracking RAM blocks; swapping inactive pages to virtual memory.\n3. File System Management: Structuring, naming, locating, and securing files and folders on storage drives.\n4. Device / I/O Management: Communicating with hardware peripherals via dedicated device drivers.\n5. User Interface & Security: Providing CLI/GUI interfaces and managing user authentication and access control lists.",
            "explanation": "Core responsibilities of an OS (IFT 205 Software & OS Slides 7-11).",
            "why_wrong": {},
            "source": "IFT 205 Software and Operating Systems Slides 7-11"
        },
        {
            "id": "ift205-ops-fc03",
            "course": "IFT 205",
            "topic": "Operating Systems, System vs Application Software",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "device-drivers", "hardware"],
            "question": "What is a Device Driver, and what role does it serve between the OS and hardware?",
            "answer": "A Device Driver is a specialized system software program that acts as a translator between the operating system and a specific hardware peripheral (e.g., graphics card, network card, printer).\nIt translates generic high-level OS commands (such as `read()` or `write()`) into the exact hardware-level electrical signals and register instructions understood by the device controller.",
            "explanation": "Peripheral interfacing in IFT 205 Software and OS Slide 6.",
            "why_wrong": {},
            "source": "IFT 205 Software and Operating Systems Slide 6"
        },
        {
            "id": "ift205-ops-fc04",
            "course": "IFT 205",
            "topic": "Operating Systems, System vs Application Software",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "gui-vs-cli", "user-interface"],
            "question": "Contrast a Graphical User Interface (GUI) with a Command-Line Interface (CLI).",
            "answer": "- GUI (Graphical User Interface): Employs visual WIMP elements (Windows, Icons, Menus, Pointers). Highly intuitive and easy for beginners, but consumes significant RAM and GPU resources.\n- CLI (Command-Line Interface): Text-based prompt where users type exact command strings and arguments. Consumes minimal memory/CPU resources, enables rapid administrative scripting and automation, but requires memorizing syntax.",
            "explanation": "UI paradigms in IFT 205 Software and OS Slide 8.",
            "why_wrong": {},
            "source": "IFT 205 Software and Operating Systems Slide 8"
        },
        {
            "id": "ift205-ops-fc05",
            "course": "IFT 205",
            "topic": "Operating Systems, System vs Application Software",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "utilities", "disk-maintenance"],
            "question": "What is Utility Software, and what do Disk Defragmentation and Disk Cleanup utilities accomplish?",
            "answer": "Utility Software consists of maintenance programs designed to analyze, configure, optimize, and maintain computer systems.\n- Disk Defragmentation: Rearranges non-contiguous file clusters on mechanical HDDs so that entire files reside in sequential sectors, minimizing read-head travel and improving file read speeds.\n- Disk Cleanup: Scans storage drives to identify and permanently delete temporary cache files, crash dumps, and recycle bin contents to free up storage space.",
            "explanation": "System maintenance utilities in IFT 205 Software & OS Slide 12.",
            "why_wrong": {},
            "source": "IFT 205 Software and Operating Systems Slide 12"
        },
        {
            "id": "ift205-ops-fc06",
            "course": "IFT 205",
            "topic": "Operating Systems, System vs Application Software",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "formatting", "file-systems"],
            "question": "What is Disk Formatting, and what is the difference between Low-Level and High-Level formatting?",
            "answer": "- Disk Formatting: The process of preparing a storage medium for file storage.\n- Low-Level Formatting: Typically done at the factory; marks physical tracks, sectors, and sector boundaries on the disk surface.\n- High-Level Formatting: Performed by the operating system; writes a file system structure (e.g., NTFS, FAT32, ext4), initializes file allocation tables, and creates directory indexing structures.",
            "explanation": "Storage preparation in IFT 205 Software & OS Slide 14.",
            "why_wrong": {},
            "source": "IFT 205 Software and Operating Systems Slide 14"
        },
        {
            "id": "ift205-ops-fc07",
            "course": "IFT 205",
            "topic": "Operating Systems, System vs Application Software",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "file-paths", "filesystem"],
            "question": "Differentiate between an Absolute File Path and a Relative File Path.",
            "answer": "- Absolute File Path: Specifies the complete, unambiguous location of a file or folder starting from the root directory or drive letter (e.g., `C:\\Users\\Student\\Documents\\project.docx` or `/home/student/project.py`). It points to the same file regardless of the current working directory.\n- Relative File Path: Specifies a file's location starting from the current active working directory (e.g., `../images/diagram.png` or `assets/style.css`).",
            "explanation": "File path structures in IFT 205 Software & OS Slide 15.",
            "why_wrong": {},
            "source": "IFT 205 Software and Operating Systems Slide 15"
        },
        {
            "id": "ift205-ops-fc08",
            "course": "IFT 205",
            "topic": "Operating Systems, System vs Application Software",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "licensing", "open-source"],
            "question": "Compare Proprietary Software, Open-Source Software (OSS), Freeware, and Shareware.",
            "answer": "- Proprietary Software: Commercial software whose source code is private and copyrighted; users purchase a non-exclusive license to use the compiled binaries under EULA constraints (e.g., Windows, macOS).\n- Open-Source Software (OSS): Source code is publicly available under open licenses (GPL, MIT, Apache); users may inspect, modify, and redistribute it freely (e.g., Linux, Apache, Blender).\n- Freeware: Distributed free of monetary charge for use, but source code remains closed and proprietary.\n- Shareware: Trial software provided free for an evaluation period, requiring payment to unlock full features.",
            "explanation": "Software licensing models in IFT 205 Software & OS Slides 17-19.",
            "why_wrong": {},
            "source": "IFT 205 Software and Operating Systems Slides 17-19"
        }
    ],

    "networking_ip_addressing.json": [
        {
            "id": "ift205-net-fc01",
            "course": "IFT 205",
            "topic": "Networking, Topologies & IPv4 Address Classes",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "networks", "protocols"],
            "question": "What is a Computer Network, and why are Network Protocols essential?",
            "answer": "A Computer Network is an interconnection of two or more autonomous computing devices linked by communication media (cables, fiber, wireless radio) to share data, applications, and hardware resources.\nNetwork Protocols are formalized, agreed-upon sets of rules and standards (like TCP/IP and HTTP) governing data syntax, error checking, and transmission timing, ensuring heterogeneous devices can communicate reliably.",
            "explanation": "Network foundations from IFT 205 Week 6, Slides 3-5.",
            "why_wrong": {},
            "source": "IFT 205 Week 6 Slides 3-5"
        },
        {
            "id": "ift205-net-fc02",
            "course": "IFT 205",
            "topic": "Networking, Topologies & IPv4 Address Classes",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "lan-man-wan", "network-geography"],
            "question": "Compare LAN, MAN, and WAN in geographical scope and typical administration.",
            "answer": "- LAN (Local Area Network): Confined to a small geographical area (single room, building, home, or campus); typically owned and managed by a single organization; high data transfer rates (1–10 Gbps).\n- MAN (Metropolitan Area Network): Covers a city or metropolitan region (e.g., municipal Wi-Fi or city cable network); often run by a consortium or telecom utility.\n- WAN (Wide Area Network): Spans large geographical regions across countries or the globe (e.g., the Internet); connects multiple LANs using leased telecommunication lines and satellite links.",
            "explanation": "Network classification by scale in IFT 205 Week 6, Slide 7.",
            "why_wrong": {},
            "source": "IFT 205 Week 6 Slide 7"
        },
        {
            "id": "ift205-net-fc03",
            "course": "IFT 205",
            "topic": "Networking, Topologies & IPv4 Address Classes",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "topologies", "star-vs-bus"],
            "question": "Contrast Star Topology with Bus Topology in layout, fault tolerance, and single points of failure.",
            "answer": "- Star Topology: All nodes connect to a central hub or switch via individual dedicated cables. If one node's cable breaks, only that node is disconnected. However, the central switch is a single point of failure—if it dies, the whole network fails.\n- Bus Topology: All devices tap into a single shared linear backbone cable terminated at both ends. Inexpensive and uses minimal cabling, but a break anywhere along the central cable halts all communication, and cable troubleshooting is difficult.",
            "explanation": "Network physical topologies in IFT 205 Week 6, Slide 10.",
            "why_wrong": {},
            "source": "IFT 205 Week 6 Slide 10"
        },
        {
            "id": "ift205-net-fc04",
            "course": "IFT 205",
            "topic": "Networking, Topologies & IPv4 Address Classes",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "switch-vs-router", "hardware"],
            "question": "How does a Network Switch (Layer 2) fundamentally differ from a Router (Layer 3)?",
            "answer": "- Network Switch (Layer 2 - Data Link): Connects devices together within the SAME Local Area Network (LAN). It inspects physical hardware MAC addresses to forward data frames directly to the specific destination port, eliminating collisions.\n- Router (Layer 3 - Network): Connects DIFFERENT, separate networks together (e.g., linking a local office LAN to the Internet WAN). It inspects logical IP addresses and uses routing tables to forward packets across optimal internetwork paths.",
            "explanation": "Networking hardware roles in IFT 205 Week 6, Slides 12-14.",
            "why_wrong": {},
            "source": "IFT 205 Week 6 Slides 12-14"
        },
        {
            "id": "ift205-net-fc05",
            "course": "IFT 205",
            "topic": "Networking, Topologies & IPv4 Address Classes",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "ipv4", "netid-hostid"],
            "question": "Explain the 32-bit structure of an IPv4 address and the roles of Network ID and Host ID.",
            "answer": "An IPv4 address consists of 32 bits divided into four 8-bit octets, written in dotted-decimal notation (e.g., `192.168.1.100`).\n- Network ID (Net ID): Identifies the specific physical or logical network to which the host belongs. All devices on the same subnet share the exact same Network ID.\n- Host ID: Uniquely identifies an individual device or network interface on that network. The Subnet Mask determines where the Network ID ends and the Host ID begins.",
            "explanation": "IPv4 addressing principles in IFT 205 Week 6, Slides 18-20.",
            "why_wrong": {},
            "source": "IFT 205 Week 6 Slides 18-20"
        },
        {
            "id": "ift205-net-fc06",
            "course": "IFT 205",
            "topic": "Networking, Topologies & IPv4 Address Classes",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "ipv4-classes", "subnet-mask"],
            "question": "State the first-octet range, default subnet mask, and capacity for IPv4 Classes A, B, and C.",
            "answer": "- Class A: First octet `1–126`. Default Mask: `255.0.0.0` (`/8`). High host capacity: 126 networks, each supporting up to 16,777,214 hosts.\n- Class B: First octet `128–191`. Default Mask: `255.255.0.0` (`/16`). Medium capacity: 16,384 networks, each supporting up to 65,534 hosts.\n- Class C: First octet `192–223`. Default Mask: `255.255.255.0` (`/24`). Small networks: Over 2 million networks, each supporting up to 254 hosts.",
            "explanation": "Classful IPv4 addressing architecture in IFT 205 Week 6, Slides 22-25.",
            "why_wrong": {},
            "source": "IFT 205 Week 6 Slides 22-25"
        },
        {
            "id": "ift205-net-fc07",
            "course": "IFT 205",
            "topic": "Networking, Topologies & IPv4 Address Classes",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "reserved-ip", "loopback-apipa"],
            "question": "What are the dedicated functions of the `127.0.0.1` and `169.254.x.x` IPv4 address ranges?",
            "answer": "- `127.0.0.1` (Loopback / Localhost): Reserved within `127.0.0.0/8` to test a computer's internal TCP/IP software stack. Packets sent to this address loop back internally without leaving the network adapter.\n- `169.254.x.x` (APIPA - Automatic Private IP Addressing): A link-local address automatically self-assigned by Windows/macOS when a DHCP client fails to receive a response from a DHCP server, allowing local subnet communication only.",
            "explanation": "Special reserved IPv4 address blocks in IFT 205 Week 6, Slide 26.",
            "why_wrong": {},
            "source": "IFT 205 Week 6 Slide 26"
        },
        {
            "id": "ift205-net-fc08",
            "course": "IFT 205",
            "topic": "Networking, Topologies & IPv4 Address Classes",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "client-server-vs-p2p", "architecture"],
            "question": "Contrast Client-Server network architecture with Peer-to-Peer (P2P) network architecture.",
            "answer": "- Client-Server: Centralized powerful server systems manage files, user accounts, and security permissions, responding to service requests from client workstations. Highly secure, easy to back up centrally, and scalable, but expensive and reliant on server uptime.\n- Peer-to-Peer (P2P): Every connected computer (peer) operates as both a client and a server with equal privileges, sharing files directly. Low cost and simple for small setups, but difficult to secure and administer as network size grows.",
            "explanation": "Network models in IFT 205 Week 6, Slide 8.",
            "why_wrong": {},
            "source": "IFT 205 Week 6 Slide 8"
        }
    ],

    "computer_evolution_generations.json": [
        {
            "id": "ift205-evo-fc01",
            "course": "IFT 205",
            "topic": "Evolution & Classification of Computers",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "history", "babbage-lovelace"],
            "question": "What was the significance of Charles Babbage's Analytical Engine and Ada Lovelace's contributions to computing?",
            "answer": "- Charles Babbage: Designed the mechanical Analytical Engine (1837), widely regarded as the first conceptual design for a general-purpose programmable computer, featuring a Store (memory) and a Mill (CPU).\n- Ada Lovelace: Created the first published algorithm intended for implementation on the Analytical Engine, foreseeing that computers could process symbols and music rather than just numbers, making her the world's first computer programmer.",
            "explanation": "Pioneers of computing history in IFT 205 Evolution Slides 4-6.",
            "why_wrong": {},
            "source": "IFT 205 Evolution Slides 4-6"
        },
        {
            "id": "ift205-evo-fc02",
            "course": "IFT 205",
            "topic": "Evolution & Classification of Computers",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "von-neumann", "stored-program"],
            "question": "What is the Stored-Program Concept, and how did it change computer operation?",
            "answer": "Introduced by John von Neumann in 1945, the Stored-Program Concept states that program instructions and data are stored together electronically in the same addressable read/write memory (RAM).\nBefore this, early computers (like ENIAC) had to be physically rewired and manually re-patched with patch cords to change programs. Stored-program computers can switch tasks instantaneously simply by loading a new program into RAM.",
            "explanation": "Von Neumann architecture foundation in IFT 205 Evolution Slides 8-10.",
            "why_wrong": {},
            "source": "IFT 205 Evolution Slides 8-10"
        },
        {
            "id": "ift205-evo-fc03",
            "course": "IFT 205",
            "topic": "Evolution & Classification of Computers",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "first-generation", "vacuum-tubes"],
            "question": "State the core electronic switching technology, memory media, and primary limitations of First-Generation computers (1940–1956).",
            "answer": "- Electronic Technology: Vacuum tubes (thermionic valves) used as logic switches.\n- Memory / Storage: Magnetic drums, delay lines, and punched cards.\n- Programming: Pure machine code (binary 0s and 1s).\n- Limitations: Massive room-sized footprint, enormous electrical power consumption, generated extreme heat, and suffered frequent tube burnout breakdowns (e.g., ENIAC, UNIVAC I).",
            "explanation": "First generation computing in IFT 205 Evolution Slide 12.",
            "why_wrong": {},
            "source": "IFT 205 Evolution Slide 12"
        },
        {
            "id": "ift205-evo-fc04",
            "course": "IFT 205",
            "topic": "Evolution & Classification of Computers",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "second-generation", "transistors"],
            "question": "What major electronic invention characterized Second-Generation computers (1956–1963), and what programming advances occurred?",
            "answer": "- Hardware Breakthrough: The Transistor replaced fragile vacuum tubes. Transistors were drastically smaller, faster, cheaper, produced far less heat, and were far more reliable.\n- Software Breakthrough: Introduced early high-level programming languages (FORTRAN for scientific computation, COBOL for business data), replacing low-level machine and assembly code.",
            "explanation": "Second generation computing in IFT 205 Evolution Slide 14.",
            "why_wrong": {},
            "source": "IFT 205 Evolution Slide 14"
        },
        {
            "id": "ift205-evo-fc05",
            "course": "IFT 205",
            "topic": "Evolution & Classification of Computers",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "third-generation", "integrated-circuits"],
            "question": "What technological innovation defined Third-Generation computers (1964–1971), and how did user interaction change?",
            "answer": "- Innovation: The Integrated Circuit (IC), a miniature silicon semiconductor wafer combining thousands of transistors on a single chip.\n- Interaction & Software: Keyboards and monitor screens replaced punched cards; primitive Operating Systems emerged allowing multiple concurrent users to interact via time-sharing (e.g., IBM System/360).",
            "explanation": "Third generation computing in IFT 205 Evolution Slide 16.",
            "why_wrong": {},
            "source": "IFT 205 Evolution Slide 16"
        },
        {
            "id": "ift205-evo-fc06",
            "course": "IFT 205",
            "topic": "Evolution & Classification of Computers",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "fourth-generation", "microprocessors"],
            "question": "What invention sparked the Fourth Generation of computing (1971–Present), leading to the personal computer revolution?",
            "answer": "The invention of the Microprocessor—an entire Central Processing Unit fabricated onto a single silicon chip using Very Large-Scale Integration (VLSI) and ULSI (pioneered by the Intel 4004 in 1971).\nThis extreme miniaturization made computers small and affordable enough for personal desktops, leading to home PCs (Apple II, IBM PC), laptops, and mobile smartphones.",
            "explanation": "Fourth generation computing in IFT 205 Evolution Slide 18.",
            "why_wrong": {},
            "source": "IFT 205 Evolution Slide 18"
        },
        {
            "id": "ift205-evo-fc07",
            "course": "IFT 205",
            "topic": "Evolution & Classification of Computers",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "fifth-generation", "ai-quantum"],
            "question": "What technologies and computational paradigms define Fifth-Generation computing?",
            "answer": "Fifth-Generation computing focuses on Artificial Intelligence (AI), parallel processing, natural language processing, neural networks, and Quantum Computing.\nInstead of simple sequential arithmetic instructions, Fifth-Gen systems aim for automated reasoning, computer vision, voice recognition, and quantum qubits to solve previously intractable mathematical and scientific problems.",
            "explanation": "Fifth generation computing in IFT 205 Evolution Slide 20.",
            "why_wrong": {},
            "source": "IFT 205 Evolution Slide 20"
        },
        {
            "id": "ift205-evo-fc08",
            "course": "IFT 205",
            "topic": "Evolution & Classification of Computers",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "classification", "supercomputer-mainframe-embedded"],
            "question": "Compare Microcomputers, Mainframes, Supercomputers, and Embedded Systems by primary operational role.",
            "answer": "- Microcomputer: Single-user personal computers designed for general individual productivity (desktops, laptops, tablets, smartphones).\n- Mainframe: High-end enterprise systems optimized for high-volume concurrent transaction processing and 24/7 reliability for banks and governments.\n- Supercomputer: Extreme performance multi-processor systems built to process complex mathematical simulations at quadrillions of FLOPS (weather modeling, nuclear physics).\n- Embedded System: Dedicated microcontrollers permanently built into non-computing machines (cars, microwaves, medical pacemakers) to perform a single dedicated control function.",
            "explanation": "Computer classification taxonomy in IFT 205 Evolution Slides 24-28.",
            "why_wrong": {},
            "source": "IFT 205 Evolution Slides 24-28"
        }
    ]
}

print("IFT 205 flashcard definitions compiled.")

INS202_FLASHCARDS = {
    "hci_introduction_goals.json": [
        {
            "id": "ins202-hig-fc01",
            "course": "INS 202",
            "topic": "HCI Fundamentals & Core Goals (Safety, Utility, etc.)",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "hci-definition", "multidisciplinary"],
            "question": "What is Human-Computer Interaction (HCI), and why is it inherently a multidisciplinary field?",
            "answer": "Human-Computer Interaction (HCI) is a discipline concerned with the design, evaluation, and implementation of interactive computing systems for human use, and with the study of major phenomena surrounding them.\nIt is multidisciplinary because it synthesizes:\n- Computer Science (software engineering, UI architectures)\n- Cognitive Psychology (human perception, memory, mental models)\n- Ergonomics / Human Factors (physical workspace, fatigue, anatomy)\n- Graphic & Industrial Design (visual hierarchy, aesthetics, typography).",
            "explanation": "Foundational definition of HCI from Gerard Kim and INS 202 Module 1, Slide 3.",
            "why_wrong": {},
            "source": "INS 202 Module 01 Slide 3"
        },
        {
            "id": "ins202-hig-fc02",
            "course": "INS 202",
            "topic": "HCI Fundamentals & Core Goals (Safety, Utility, etc.)",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "usability-goals", "metrics"],
            "question": "List and define the six primary Usability Goals in HCI.",
            "answer": "1. Effectiveness: How well a system executes the tasks it was designed to accomplish.\n2. Efficiency: The level of resources (time, clicks, mental effort) expended to achieve goals.\n3. Safety: Protecting users from hazardous situations and unintended errors, and offering easy recovery (Undo).\n4. Utility: Providing the appropriate set of functions that users actually need to perform their work.\n5. Learnability: How easy it is for first-time or novice users to master basic functionality.\n6. Memorability: How easily users re-establish proficiency after a period of non-use.",
            "explanation": "The 6 core usability dimensions (Preece, Rogers, Sharp / INS 202 Module 1).",
            "why_wrong": {},
            "source": "INS 202 Module 01 Slides 10-15"
        },
        {
            "id": "ins202-hig-fc03",
            "course": "INS 202",
            "topic": "HCI Fundamentals & Core Goals (Safety, Utility, etc.)",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "usability-vs-ux", "goals"],
            "question": "How do Usability Goals fundamentally differ from User Experience (UX) Goals?",
            "answer": "- Usability Goals: Objective, measurable performance benchmarks focused on productivity, error reduction, task speed, and functional capability (e.g., 'Can the user complete checkout in under 60 seconds with 0 errors?').\n- User Experience (UX) Goals: Subjective, qualitative criteria focused on human emotion, feelings, and psychological engagement during interaction (e.g., 'Is the interface satisfying, enjoyable, aesthetically pleasing, motivating, or engaging?').",
            "explanation": "Objective usability vs subjective UX distinction from INS 202 Module 1.",
            "why_wrong": {},
            "source": "INS 202 Module 01 Slides 16-18"
        },
        {
            "id": "ins202-hig-fc04",
            "course": "INS 202",
            "topic": "HCI Fundamentals & Core Goals (Safety, Utility, etc.)",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "safety", "error-prevention"],
            "question": "In the context of Usability Goals, how does a system designer ensure 'Safety'?",
            "answer": "Safety is achieved through two complementary design strategies:\n1. Error Prevention: Designing interfaces that prevent destructive actions before they happen (e.g., graying out invalid options, clear constraints, destructive action confirmation prompts).\n2. Error Recovery: Providing safe, non-punitive escape mechanisms when mistakes occur, such as multi-level `Undo` (`Ctrl+Z`), auto-saved document drafts, and non-destructive trash/recycle bins.",
            "explanation": "Safety principles in interface design from INS 202 Module 1, Slide 12.",
            "why_wrong": {},
            "source": "INS 202 Module 01 Slide 12"
        },
        {
            "id": "ins202-hig-fc05",
            "course": "INS 202",
            "topic": "HCI Fundamentals & Core Goals (Safety, Utility, etc.)",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "learnability-vs-memorability"],
            "question": "Contrast Learnability with Memorability in user interface evaluation.",
            "answer": "- Learnability: Measures how quickly and easily a brand-new or novice user can grasp an interface and achieve basic task proficiency without formal training.\n- Memorability: Measures how easily a casual or intermittent user remembers how to use the interface after being away from it for weeks or months, without having to relearn basic commands from scratch.",
            "explanation": "Learnability vs memorability in usability metrics (INS 202 Module 1).",
            "why_wrong": {},
            "source": "INS 202 Module 01 Slides 14-15"
        },
        {
            "id": "ins202-hig-fc06",
            "course": "INS 202",
            "topic": "HCI Fundamentals & Core Goals (Safety, Utility, etc.)",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "business-benefits", "roi"],
            "question": "What are the tangible financial and operational benefits of incorporating HCI and usability engineering into commercial software development?",
            "answer": "1. Reduced Development & Maintenance Costs: Identifying design flaws during early wireframing is up to 100x cheaper than rewriting production code after deployment.\n2. Increased Employee Productivity: Streamlined workflows reduce keystrokes, task time, and operator fatigue.\n3. Decreased Training and Customer Support Costs: Intuitive self-explanatory UI slashes technical support calls and onboarding manuals.\n4. Increased Conversion & Customer Retention: Users abandon frustrating websites for competitors; usable systems foster brand loyalty and higher sales.",
            "explanation": "The business ROI of usability from INS 202 Module 1, Slides 6-9.",
            "why_wrong": {},
            "source": "INS 202 Module 01 Slides 6-9"
        },
        {
            "id": "ins202-hig-fc07",
            "course": "INS 202",
            "topic": "HCI Fundamentals & Core Goals (Safety, Utility, etc.)",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "poor-usability", "consequences"],
            "question": "What are the catastrophic consequences of poor usability in safety-critical systems?",
            "answer": "In safety-critical domains (aviation cockpits, nuclear power control rooms, intensive care medical monitors, military defense systems), poor interface usability (such as ambiguous warning displays, confusing mode switches, or cluttered dials) induces cognitive overload, leading to fatal human operator error, vehicle crashes, and catastrophic loss of life (e.g., the Three Mile Island nuclear incident or Therac-25 radiation accidents).",
            "explanation": "Safety-critical usability impacts covered in INS 202 Module 1.",
            "why_wrong": {},
            "source": "INS 202 Module 01 Slides 4-5"
        },
        {
            "id": "ins202-hig-fc08",
            "course": "INS 202",
            "topic": "HCI Fundamentals & Core Goals (Safety, Utility, etc.)",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "iterative-design", "lifecycle"],
            "question": "What is the Iterative Design Lifecycle in HCI, and why is single-pass waterfall design ineffective for interactive systems?",
            "answer": "The Iterative Design Lifecycle is a continuous repeating loop of:\n1. Requirements Gathering (understanding user needs)\n2. Design (ideating alternative concepts)\n3. Prototyping (building low/high fidelity interactive models)\n4. Evaluation (testing with real users to discover defects)\nSingle-pass linear waterfall models fail for user interfaces because designers cannot anticipate emergent human behavioral nuances, cognitive limits, and subjective emotional reactions prior to physical interaction.",
            "explanation": "The iterative cycle in HCI development (INS 202 Module 1 & 4).",
            "why_wrong": {},
            "source": "INS 202 Module 01 & 04"
        }
    ],

    "principles_interaction_interface.json": [
        {
            "id": "ins202-pii-fc01",
            "course": "INS 202",
            "topic": "Interaction vs Interface & Design Principles",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "interaction-vs-interface"],
            "question": "What is the fundamental difference between an Interface and an Interaction in HCI?",
            "answer": "- Interface: The physical and graphical surface mediating the human and machine (the tangible hardware, pixels, buttons, sliders, icons, menus, and typography).\n- Interaction: The ongoing behavioral dialogue, action exchange, and cognitive communication loop occurring between the human user and the system over time as the user executes tasks.",
            "explanation": "Core conceptual distinction from INS 202 Module 2, Slide 3.",
            "why_wrong": {},
            "source": "INS 202 Module 02 Slide 3"
        },
        {
            "id": "ins202-pii-fc02",
            "course": "INS 202",
            "topic": "Interaction vs Interface & Design Principles",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "norman-principles", "visibility"],
            "question": "Explain Don Norman's design principle of 'Visibility'.",
            "answer": "Visibility dictates that available controls, functions, and options should be clearly noticeable and visually prominent to the user, rather than concealed behind convoluted menus.\nWhen system functions are visible, users can immediately deduce what actions are possible without memorizing complex hidden keyboard shortcuts.",
            "explanation": "Norman's 6 design principles (INS 202 Module 2, Slide 6).",
            "why_wrong": {},
            "source": "INS 202 Module 02 Slide 6"
        },
        {
            "id": "ins202-pii-fc03",
            "course": "INS 202",
            "topic": "Interaction vs Interface & Design Principles",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "norman-principles", "feedback"],
            "question": "Explain Don Norman's design principle of 'Feedback' and give three modalities of feedback.",
            "answer": "Feedback ensures that every user action produces an immediate, clear, and unambiguous response indicating what action was performed and what result was achieved.\nModalities of feedback:\n1. Visual: Loading spinners, button depression animations, color state changes.\n2. Auditory: Success chimes, shutter clicks on phone cameras, error beeps.\n3. Haptic: Subtle vibration pulses on mobile touchscreens confirming a virtual keypress.",
            "explanation": "Feedback principles in interactive systems (INS 202 Module 2, Slide 8).",
            "why_wrong": {},
            "source": "INS 202 Module 02 Slide 8"
        },
        {
            "id": "ins202-pii-fc04",
            "course": "INS 202",
            "topic": "Interaction vs Interface & Design Principles",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "norman-principles", "affordance"],
            "question": "What is an 'Affordance', and how did Don Norman distinguish Perceived Affordance from Real Affordance?",
            "answer": "- Real Affordance: The actual physical properties of an object that determine how it can be manipulated (e.g., a physical door handle affords pulling; a flat plate affords pushing).\n- Perceived Affordance: The visual clues and signifiers that communicate to the user how an interface element can be interacted with (e.g., a 3D beveled button looks 'clickable' on a 2D glass screen, inviting finger taps).",
            "explanation": "Affordance theory in HCI (INS 202 Module 2, Slide 10).",
            "why_wrong": {},
            "source": "INS 202 Module 02 Slide 10"
        },
        {
            "id": "ins202-pii-fc05",
            "course": "INS 202",
            "topic": "Interaction vs Interface & Design Principles",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "norman-principles", "mapping"],
            "question": "What is 'Mapping' in user interface design, and what constitutes 'Natural Mapping'?",
            "answer": "Mapping refers to the relationship between controls and their resulting effects in the physical or digital environment.\nNatural Mapping exploits physical analogies or spatial layout correspondence:\n- E.g., arranging a stove's four burner knobs in the identical rectangular pattern as the burners themselves.\n- E.g., turning an audio knob clockwise to increase volume, or pushing a steering wheel right to turn right.",
            "explanation": "Spatial correspondence and mapping from INS 202 Module 2, Slide 12.",
            "why_wrong": {},
            "source": "INS 202 Module 02 Slide 12"
        },
        {
            "id": "ins202-pii-fc06",
            "course": "INS 202",
            "topic": "Interaction vs Interface & Design Principles",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "norman-principles", "consistency"],
            "question": "Contrast Internal Consistency with External Consistency in user interface design.",
            "answer": "- Internal Consistency: Applying identical design rules, color palettes, button styles, terminology, and layout patterns across all screens within the SAME application.\n- External Consistency: Conforming to established cross-application standards, conventions, and platform guidelines (e.g., standardizing `Ctrl+C` for copy, putting a shopping cart icon in the top-right header, or using a blue magnifying glass for search).",
            "explanation": "Consistency dimensions from INS 202 Module 2, Slide 14.",
            "why_wrong": {},
            "source": "INS 202 Module 02 Slide 14"
        },
        {
            "id": "ins202-pii-fc07",
            "course": "INS 202",
            "topic": "Interaction vs Interface & Design Principles",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "norman-principles", "constraints"],
            "question": "List and explain the four types of Constraints described by Don Norman.",
            "answer": "1. Physical Constraints: Physical boundaries restricting movement (e.g., a USB-A plug physically cannot enter a socket upside down).\n2. Logical Constraints: Exploiting human reasoning and deduction (e.g., if a wizard has 3 steps and steps 1 and 2 are finished, step 3 is the only remaining action).\n3. Semantic Constraints: Relying on the real-world meaning and common sense of situations to limit possible actions.\n4. Cultural Constraints: Learned social conventions and standardized symbols (e.g., red meaning stop/danger and green meaning go/success).",
            "explanation": "Norman's constraint taxonomy (INS 202 Module 2, Slide 16).",
            "why_wrong": {},
            "source": "INS 202 Module 02 Slide 16"
        },
        {
            "id": "ins202-pii-fc08",
            "course": "INS 202",
            "topic": "Interaction vs Interface & Design Principles",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "signifiers-vs-affordances"],
            "question": "What is the difference between an Affordance and a Signifier according to Don Norman's revised design model?",
            "answer": "- Affordance: Determines what actions are physically possible between an actor and an object (e.g., a touch screen affordance allows touching anywhere on the surface).\n- Signifier: Any perceivable indicator (text, mark, icon, border, arrow, sound) that communicates WHERE the action should take place and WHAT action is expected (e.g., a painted word 'PUSH' on a door or a blue button with 'Submit Order' on a glass touchscreen).",
            "explanation": "Norman's revised Design of Everyday Things framework (INS 202 Module 2).",
            "why_wrong": {},
            "source": "INS 202 Module 02 Slide 18"
        }
    ],

    "human_factors_ergonomics.json": [
        {
            "id": "ins202-hfe-fc01",
            "course": "INS 202",
            "topic": "Human Factors, Cognitive Psychology & Ergonomics",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "fitts-law", "motor-control"],
            "question": "State Fitts's Law and explain its direct practical implications for user interface and button design.",
            "answer": "Fitts's Law models human motor movement time to a target:\n`MT = a + b * log2(2D / W)`\nWhere `D` is distance to the target and `W` is the target's width along the axis of motion.\nDesign Implications:\n1. Make critical buttons larger (increasing `W`) and locate them closer to the user's cursor (decreasing `D`).\n2. The corners and edges of a screen have effectively infinite width (`W = infinity`) because the mouse cursor cannot overshoot them, making screen corners ideal for menus (e.g., Windows Start button or macOS menu bar).",
            "explanation": "Fitts's Law human motor performance model (INS 202 Module 3, Slide 8).",
            "why_wrong": {},
            "source": "INS 202 Module 03 Slide 8"
        },
        {
            "id": "ins202-hfe-fc02",
            "course": "INS 202",
            "topic": "Human Factors, Cognitive Psychology & Ergonomics",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "hick-law", "decision-time"],
            "question": "State Hick-Hyman Law and its key lesson for menu navigation architecture.",
            "answer": "Hick's Law states that the time taken to make a decision increases logarithmically with the number of alternatives:\n`T = b * log2(n + 1)`\nWhere `n` is the number of options.\nKey Design Lesson: Menus should not overwhelm users with dozens of unordered options. Designers should group options hierarchically or categorize items to minimize choice overload and reduce decision latency.",
            "explanation": "Hick-Hyman Law in cognitive ergonomics (INS 202 Module 3, Slide 10).",
            "why_wrong": {},
            "source": "INS 202 Module 03 Slide 10"
        },
        {
            "id": "ins202-hfe-fc03",
            "course": "INS 202",
            "topic": "Human Factors, Cognitive Psychology & Ergonomics",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "millers-law", "working-memory"],
            "question": "What is Miller's Magical Number 7 ± 2, and how does it relate to 'Chunking' in UI design?",
            "answer": "George Miller (1956) demonstrated that human short-term working memory capacity is strictly limited to 7 ± 2 (5 to 9) chunks of information.\nIn UI design, 'Chunking' breaks long unbroken strings of data into smaller, manageable cognitive clusters (e.g., formatting a 10-digit phone number as `(123) 456-7890` or dividing a 16-digit credit card into blocks of 4), preventing cognitive overload.",
            "explanation": "Cognitive psychology limits in HCI (INS 202 Module 3, Slide 12).",
            "why_wrong": {},
            "source": "INS 202 Module 03 Slide 12"
        },
        {
            "id": "ins202-hfe-fc04",
            "course": "INS 202",
            "topic": "Human Factors, Cognitive Psychology & Ergonomics",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "gulf-execution-evaluation", "action-cycle"],
            "question": "Contrast Don Norman's Gulf of Execution with the Gulf of Evaluation.",
            "answer": "- Gulf of Execution: The mental barrier a user faces when trying to translate their psychological goal into actual physical system actions ('How do I make the system do what I want?'). Bridged by clear signifiers, affordances, and natural mappings.\n- Gulf of Evaluation: The difficulty a user faces in assessing the system's state after taking action ('Did the system do what I intended? What is its state now?'). Bridged by immediate, unambiguous visual/auditory feedback.",
            "explanation": "Norman's 7 stages of action (INS 202 Module 3, Slide 14).",
            "why_wrong": {},
            "source": "INS 202 Module 03 Slide 14"
        },
        {
            "id": "ins202-hfe-fc04b", # rename to fc05
            "id": "ins202-hfe-fc05",
            "course": "INS 202",
            "topic": "Human Factors, Cognitive Psychology & Ergonomics",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "mental-models-vs-conceptual"],
            "question": "Contrast a User's Mental Model with a Designer's Conceptual Model.",
            "answer": "- User's Mental Model: The internal psychological representation and belief structure held by the user about how the system works, formed by prior life experiences and interface metaphors.\n- Designer's Conceptual Model: The actual formal blueprint, architecture, and logic devised by software engineers.\nUsability breakdowns occur when there is a mismatch between the conceptual model and the user's mental model.",
            "explanation": "Mental models in cognitive ergonomics (INS 202 Module 3, Slide 16).",
            "why_wrong": {},
            "source": "INS 202 Module 03 Slide 16"
        },
        {
            "id": "ins202-hfe-fc06",
            "course": "INS 202",
            "topic": "Human Factors, Cognitive Psychology & Ergonomics",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "color-blindness", "contrast"],
            "question": "Why must user interface designers never rely solely on color to convey information?",
            "answer": "Approximately 8% of males and 0.5% of females experience color vision deficiency (most commonly red-green color blindness: deuteranopia and protanopia).\nIf an interface signals status using only red/green circles without redundant iconography (like checkmarks or warning crosses) or text labels, color-blind users cannot differentiate success from failure.\nWCAG requires a minimum contrast ratio of 4.5:1 for standard text.",
            "explanation": "Visual perception and accessible ergonomics (INS 202 Module 3, Slide 18).",
            "why_wrong": {},
            "source": "INS 202 Module 03 Slide 18"
        },
        {
            "id": "ins202-hfe-fc07",
            "course": "INS 202",
            "topic": "Human Factors, Cognitive Psychology & Ergonomics",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "physical-ergonomics", "rsi"],
            "question": "What is Physical Ergonomics, and how can workstation design prevent Repetitive Strain Injury (RSI)?",
            "answer": "Physical Ergonomics studies human anatomical, physiological, and biomechanical characteristics as they relate to physical activity.\nWorkstation design prevents RSI and musculoskeletal disorders by:\n1. Positioning the top of the monitor screen at or slightly below eye level (preventing neck strain).\n2. Maintaining elbows, hips, and knees at 90° angles with feet flat on the floor.\n3. Keeping wrists straight in a neutral posture using wrist rests, avoiding sharp desk edges and prolonged claw grips.",
            "explanation": "Physical workplace ergonomics from INS 202 Module 3, Slide 20.",
            "why_wrong": {},
            "source": "INS 202 Module 03 Slide 20"
        },
        {
            "id": "ins202-hfe-fc08",
            "course": "INS 202",
            "topic": "Human Factors, Cognitive Psychology & Ergonomics",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "selective-attention", "banner-blindness"],
            "question": "What is 'Banner Blindness', and how does Cognitive Psychology explain it through Selective Attention?",
            "answer": "Banner Blindness is a phenomenon where web users consciously or unconsciously ignore page elements that look like advertisements, promotional banners, or animations.\nCognitive Psychology explains this through Selective Attention: when users are focused on a goal-oriented task (such as researching an article), their cognitive filter suppresses peripheral visual clutter that shares visual characteristics with ads, even if the banner contains vital navigation information.",
            "explanation": "Attention mechanisms and web ergonomics (INS 202 Module 3, Slide 22).",
            "why_wrong": {},
            "source": "INS 202 Module 03 Slide 22"
        }
    ],

    "user_centered_development.json": [
        {
            "id": "ins202-ucd-fc01",
            "course": "INS 202",
            "topic": "User-Centered Development (UCD) & Prototyping",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "ucd", "four-activities"],
            "question": "What are the four core iterative activities that define User-Centered Development (UCD)?",
            "answer": "1. Understanding Context & Establishing Requirements: Identifying who the users are, their environments, and their goals.\n2. Producing Design Alternatives: Ideating conceptual frameworks and interaction workflows.\n3. Building Interactive Prototypes: Creating low- and high-fidelity mockups for testing.\n4. Evaluating Designs Against Requirements: Conducting empirical user testing to validate usability and uncover problems.",
            "explanation": "The 4 fundamental UCD activities from INS 202 Module 4, Slide 4.",
            "why_wrong": {},
            "source": "INS 202 Module 04 Slide 4"
        },
        {
            "id": "ins202-ucd-fc02",
            "course": "INS 202",
            "topic": "User-Centered Development (UCD) & Prototyping",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "low-fi-vs-high-fi", "prototyping"],
            "question": "Contrast Low-Fidelity Prototyping with High-Fidelity Prototyping.",
            "answer": "- Low-Fidelity Prototyping: Simple, low-cost representations using paper sketches, index cards, or post-it notes. Fast to create, encourages rapid exploration of concepts, and users feel comfortable critiquing rough work.\n- High-Fidelity Prototyping: Realistic, interactive digital mockups built in tools like Figma or HTML/CSS. Closely mimics final aesthetics and interactions, ideal for detailed user testing, but expensive and time-consuming to build.",
            "explanation": "Prototyping fidelity trade-offs from INS 202 Module 4, Slide 8.",
            "why_wrong": {},
            "source": "INS 202 Module 04 Slide 8"
        },
        {
            "id": "ins202-ucd-fc03",
            "course": "INS 202",
            "topic": "User-Centered Development (UCD) & Prototyping",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "horizontal-vs-vertical", "prototyping"],
            "question": "Differentiate between Horizontal Prototyping and Vertical Prototyping.",
            "answer": "- Horizontal Prototype: Broad but shallow. Covers the full surface breadth of the interface (all top-level menus, screens, and navigation paths), but none of the deep operational functions work.\n- Vertical Prototype: Narrow but deep. Implements a single, specific feature or user workflow from the UI down to the database with full functionality, allowing thorough end-to-end performance testing of that slice.",
            "explanation": "Prototyping scope dimensions in INS 202 Module 4, Slide 10.",
            "why_wrong": {},
            "source": "INS 202 Module 04 Slide 10"
        },
        {
            "id": "ins202-ucd-fc04",
            "course": "INS 202",
            "topic": "User-Centered Development (UCD) & Prototyping",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "formative-vs-summative", "evaluation"],
            "question": "Contrast Formative Evaluation with Summative Evaluation in UCD.",
            "answer": "- Formative Evaluation: Conducted continuously DURING the active design and development process. Its goal is diagnostic: to discover what is broken, why users struggle, and guide iterative redesign.\n- Summative Evaluation: Conducted at the CONCLUSION of development on the finished product. Its goal is judgmental: assessing whether the system meets contractual usability benchmarks, SLAs, and performance metrics.",
            "explanation": "Evaluation stages in user-centered design (INS 202 Module 4 & 5).",
            "why_wrong": {},
            "source": "INS 202 Module 04 Slide 12"
        },
        {
            "id": "ins202-ucd-fc05",
            "course": "INS 202",
            "topic": "User-Centered Development (UCD) & Prototyping",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "personas", "requirements"],
            "question": "What is a Persona in UCD, and what key elements should it contain?",
            "answer": "A Persona is a fictional, realistic archetype representing a distinct user segment synthesized from real empirical user research data.\nIt typically includes:\n1. Demographic profile (name, age, photo, job role)\n2. Primary goals and core motivations\n3. Key frustrations, pain points, and technical limitations\n4. Environmental context and technical proficiency level.\nPersonas keep developers focused on real user needs rather than designing for themselves.",
            "explanation": "User modeling with personas from INS 202 Module 4, Slide 14.",
            "why_wrong": {},
            "source": "INS 202 Module 04 Slide 14"
        },
        {
            "id": "ins202-ucd-fc06",
            "course": "INS 202",
            "topic": "User-Centered Development (UCD) & Prototyping",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "scenarios", "use-cases"],
            "question": "What is a Scenario in user interface design, and how does it support UCD?",
            "answer": "A Scenario is an informal narrative story describing a persona carrying out specific tasks within a real-world contextual setting to achieve a meaningful goal.\nScenarios humanize requirements, illustrating the physical environment, social context, time pressures, emotional state, and sequence of steps leading to interaction.",
            "explanation": "Contextual narratives in UCD (INS 202 Module 4, Slide 16).",
            "why_wrong": {},
            "source": "INS 202 Module 04 Slide 16"
        },
        {
            "id": "ins202-ucd-fc07",
            "course": "INS 202",
            "topic": "User-Centered Development (UCD) & Prototyping",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "wizard-of-oz", "testing"],
            "question": "What is the 'Wizard of Oz' testing methodology in HCI prototyping?",
            "answer": "In Wizard of Oz testing, a user interacts with what appears to be a fully automated system (e.g., AI chatbot or voice assistant), but the complex backend intelligence is actually secretly operated by a hidden human experimenter (the 'Wizard') simulating computer responses in real time.\nThis enables teams to evaluate user reactions and conversational flows before investing months coding expensive backend logic.",
            "explanation": "Rapid interactive prototyping techniques (INS 202 Module 4, Slide 18).",
            "why_wrong": {},
            "source": "INS 202 Module 04 Slide 18"
        },
        {
            "id": "ins202-ucd-fc08",
            "course": "INS 202",
            "topic": "User-Centered Development (UCD) & Prototyping",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "participatory-design", "co-design"],
            "question": "What is Participatory Design, and how does it differ from traditional user testing?",
            "answer": "- Traditional User Testing: Users are treated as passive evaluators who test prototypes already created by software engineers.\n- Participatory Design (Co-Design): End-users are included as full, active co-designers in workshops throughout the design process, sketching layouts, prioritizing features, and co-creating solutions directly with engineers.",
            "explanation": "Collaborative design methodologies from INS 202 Module 4, Slide 20.",
            "why_wrong": {},
            "source": "INS 202 Module 04 Slide 20"
        }
    ],

    "evaluation_techniques_likert.json": [
        {
            "id": "ins202-etl-fc04",
            "course": "INS 202",
            "topic": "UI Evaluation Techniques, Heuristics & Likert Scales",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "nielsen-heuristics", "visibility-error-prevention"],
            "question": "Explain Jakob Nielsen's Heuristics #1 (Visibility of System Status) and #5 (Error Prevention).",
            "answer": "- Heuristic #1 (Visibility of System Status): The system should always keep users informed about what is going on, through appropriate and timely feedback within a reasonable time (e.g., progress bars, upload percentages).\n- Heuristic #5 (Error Prevention): A careful design that prevents a problem from occurring in the first place is even better than good error messages. Eliminate error-prone conditions or check for them and present users with a confirmation option before they commit to destructive actions.",
            "explanation": "Nielsen's 10 usability heuristics (INS 202 Module 5, Slide 6).",
            "why_wrong": {},
            "source": "INS 202 Module 05 Slide 6"
        },
        {
            "id": "ins202-etl-fc05",
            "course": "INS 202",
            "topic": "UI Evaluation Techniques, Heuristics & Likert Scales",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "cognitive-walkthrough", "learnability"],
            "question": "What is a Cognitive Walkthrough, and what four questions does an evaluator ask at each step?",
            "answer": "A Cognitive Walkthrough is a task-oriented usability inspection method focusing on first-time learnability for novice users.\nAt each action step, evaluators ask:\n1. Will the user try to achieve the right effect?\n2. Will the user notice that the correct action is available?\n3. Will the user associate the correct action with the effect they are trying to achieve?\n4. If the correct action is performed, will the user see that progress is being made toward their goal?",
            "explanation": "Wharton et al. cognitive walkthrough framework (INS 202 Module 5, Slide 10).",
            "why_wrong": {},
            "source": "INS 202 Module 05 Slide 10"
        },
        {
            "id": "ins202-etl-fc06",
            "course": "INS 202",
            "topic": "UI Evaluation Techniques, Heuristics & Likert Scales",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "sus", "system-usability-scale"],
            "question": "What is the System Usability Scale (SUS), how is it scored, and what is the industry average benchmark?",
            "answer": "The System Usability Scale (SUS) is a 10-item Likert-scale questionnaire giving a standardized view of subjective usability.\n- Items alternate between positive and negative statements (scored 1 to 5).\n- Total scores range from 0 to 100 via a specialized conversion formula.\n- Industry Average Benchmark: A score of 68 represents the 50th percentile (average). Scores above 80 indicate excellent usability.",
            "explanation": "Brooke (1996) System Usability Scale from INS 202 Module 5, Slide 14.",
            "why_wrong": {},
            "source": "INS 202 Module 05 Slide 14"
        },
        {
            "id": "ins202-etl-fc07",
            "course": "INS 202",
            "topic": "UI Evaluation Techniques, Heuristics & Likert Scales",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "think-aloud", "usability-testing"],
            "question": "What is the Think-Aloud Protocol, and why is it considered the 'gold standard' in usability testing?",
            "answer": "In a Think-Aloud study, test participants are asked to verbalize their thoughts, expectations, confusions, and intentions continuously as they interact with an interface.\nIt is the gold standard because it directly reveals the user's mental model and internal reasoning in real time, exposing why a user made an error rather than just recording that an error occurred.",
            "explanation": "Qualitative usability evaluation from INS 202 Module 5, Slide 16.",
            "why_wrong": {},
            "source": "INS 202 Module 05 Slide 16"
        },
        {
            "id": "ins202-etl-fc08",
            "course": "INS 202",
            "topic": "UI Evaluation Techniques, Heuristics & Likert Scales",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "five-users-rule", "nielsen"],
            "question": "What is Jakob Nielsen's 'Rule of 5 Users' in empirical usability testing?",
            "answer": "Jakob Nielsen and Thomas Landauer demonstrated mathematically that testing with 5 users uncovers approximately 75% to 85% of all usability problems in an interface.\nTesting additional users yields diminishing returns, as later users repeatedly encounter the same defects. The most cost-effective approach is testing 5 users, fixing the discovered defects, and testing another 5 users in the next iteration.",
            "explanation": "Usability testing economics and sample size (INS 202 Module 5, Slide 18).",
            "why_wrong": {},
            "source": "INS 202 Module 05 Slide 18"
        }
    ],

    "ui_ux_design_patterns.json": [
        {
            "id": "ins202-udp-fc05",
            "course": "INS 202",
            "topic": "UI/UX Design Patterns & Templates (Figma, Webflow)",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "gestalt", "proximity-similarity"],
            "question": "Explain the Gestalt Principles of Proximity and Similarity in UI design.",
            "answer": "- Principle of Proximity: Objects placed close together are perceived as a related group, whereas distant objects are perceived as separate (e.g., placing form field labels directly above their inputs rather than closer to the previous input).\n- Principle of Similarity: Visual elements that share visual attributes (color, shape, size, typography) are perceived to belong together or share the same function (e.g., all primary action buttons having the same blue fill).",
            "explanation": "Gestalt perceptual laws in visual UI design (INS 202 Module 6, Slide 6).",
            "why_wrong": {},
            "source": "INS 202 Module 06 Slide 6"
        },
        {
            "id": "ins202-udp-fc06",
            "course": "INS 202",
            "topic": "UI/UX Design Patterns & Templates (Figma, Webflow)",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "gestalt", "closure-figure-ground"],
            "question": "Explain the Gestalt Principles of Closure and Figure-Ground.",
            "answer": "- Principle of Closure: Human perception visually completes incomplete or broken shapes, perceiving a recognizable whole rather than fragmented lines (e.g., modern minimalist company logos or icons).\n- Principle of Figure-Ground: The human eye instinctively separates visual scenes into a focal object (the figure) and a background (the ground). In UI, modals dim or blur the background ground to isolate the active dialogue figure.",
            "explanation": "Gestalt grouping principles from INS 202 Module 6, Slide 8.",
            "why_wrong": {},
            "source": "INS 202 Module 06 Slide 8"
        },
        {
            "id": "ins202-udp-fc07",
            "course": "INS 202",
            "topic": "UI/UX Design Patterns & Templates (Figma, Webflow)",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "design-patterns", "accordions-tabs"],
            "question": "When should a UI designer select an Accordion pattern versus a Tabbed Navigation pattern?",
            "answer": "- Tabbed Navigation: Best when content sections are mutually exclusive, interrelated, and users need to rapidly switch between 2 to 5 distinct categories without losing vertical scroll position.\n- Accordion: Best when organizing long, content-heavy vertical lists (such as FAQs) where users only need to read 1 or 2 specific sections, keeping the page compact on mobile viewports.",
            "explanation": "Interactive UI layout patterns (INS 202 Module 6, Slide 12).",
            "why_wrong": {},
            "source": "INS 202 Module 06 Slide 12"
        },
        {
            "id": "ins202-udp-fc08",
            "course": "INS 202",
            "topic": "UI/UX Design Patterns & Templates (Figma, Webflow)",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "visual-hierarchy", "scale-whitespace"],
            "question": "What is Visual Hierarchy, and how do Scale, Contrast, and Whitespace guide the user's eye?",
            "answer": "Visual Hierarchy is the deliberate arrangement and presentation of visual elements in order of cognitive importance.\n- Scale: Larger headings instantly signal importance, establishing reading order.\n- Contrast: High color contrast draws immediate focal attention to call-to-action buttons.\n- Whitespace (Negative Space): Generous breathing room around elements isolates important content, prevents visual clutter, and reduces cognitive load.",
            "explanation": "Visual organization in web and app design (INS 202 Module 6, Slide 14).",
            "why_wrong": {},
            "source": "INS 202 Module 06 Slide 14"
        }
    ],

    "emerging_interfaces_accessibility.json": [
        {
            "id": "ins202-eia-fc05",
            "course": "INS 202",
            "topic": "Accessibility, Universal Design & Emerging Interfaces",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "pour-principles", "wcag"],
            "question": "What are the four foundational POUR Principles of Web Accessibility (WCAG 2.1)?",
            "answer": "1. Perceivable: Information and UI components must be presentable to users in ways they can perceive (e.g., text alternatives for images, captions for video).\n2. Operable: UI components and navigation must be operable via diverse inputs (e.g., full keyboard navigability, sufficient time to read).\n3. Understandable: Information and UI operation must be understandable (clear language, predictable layouts, input assistance).\n4. Robust: Content must be robust enough to be reliably interpreted by a wide variety of user agents, including assistive screen readers.",
            "explanation": "W3C Web Content Accessibility Guidelines (WCAG 2.1) POUR framework.",
            "why_wrong": {},
            "source": "INS 202 Module 07 Slide 6"
        },
        {
            "id": "ins202-eia-fc06",
            "course": "INS 202",
            "topic": "Accessibility, Universal Design & Emerging Interfaces",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "aria", "screen-readers"],
            "question": "What is WAI-ARIA, and why should semantic HTML elements always be preferred over ARIA roles?",
            "answer": "WAI-ARIA (Accessible Rich Internet Applications) provides HTML attributes to communicate roles, states, and properties of dynamic widgets to screen readers.\nFirst Rule of ARIA: If an existing native HTML5 semantic element can handle the job (e.g., `<button>`, `<nav>`, `<dialog>`), use it instead of recreating the element using `<div role=\"button\">`.\nNative elements provide automatic keyboard handling, focus management, and accessibility APIs out of the box.",
            "explanation": "Accessible web architecture from INS 202 Module 7, Slide 8.",
            "why_wrong": {},
            "source": "INS 202 Module 07 Slide 8"
        },
        {
            "id": "ins202-eia-fc07",
            "course": "INS 202",
            "topic": "Accessibility, Universal Design & Emerging Interfaces",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "vui", "voice-interfaces"],
            "question": "What are Voice User Interfaces (VUIs), and what unique usability challenge arises from the absence of a visual screen?",
            "answer": "VUIs (e.g., Apple Siri, Amazon Alexa) allow humans to interact with computers using natural spoken voice.\nKey Usability Challenge: The lack of visual persistence. Spoken audio is transient and serial—users cannot scan a spoken list as they would a visual webpage. If a voice assistant recites 8 choices, the user's working memory forgets the first options before the list finishes.",
            "explanation": "Emerging conversational interfaces in INS 202 Module 7, Slide 14.",
            "why_wrong": {},
            "source": "INS 202 Module 07 Slide 14"
        },
        {
            "id": "ins202-eia-fc08",
            "course": "INS 202",
            "topic": "Accessibility, Universal Design & Emerging Interfaces",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "haptics", "tactile-feedback"],
            "question": "What is Haptic Feedback, and how does it improve touchscreen accessibility and usability?",
            "answer": "Haptic Feedback utilizes tactile actuator sensations (vibrations, force resistance, thermal pulses) to simulate physical touch on virtual interfaces.\nIt improves touchscreen usability by confirming button taps, keystrokes, and toggles through the skin, compensating for the lack of tactile mechanical click on flat glass and providing vital non-visual feedback for visually impaired users.",
            "explanation": "Tactile sensory interfaces from INS 202 Module 7, Slide 16.",
            "why_wrong": {},
            "source": "INS 202 Module 07 Slide 16"
        }
    ]
}

print("INS 202 flashcard definitions compiled.")

ENT211_FLASHCARDS = {
    "entrepreneurship_core_concepts.json": [
        {
            "id": "ent211-fnd-fc05",
            "course": "ENT 211",
            "topic": "Entrepreneurship Foundations: Value, Risk & Thinkers",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "risk-vs-uncertainty", "knight"],
            "question": "How did economist Frank Knight fundamentally distinguish between 'Risk' and 'Uncertainty' in entrepreneurship?",
            "answer": "- Risk: Situations where future outcomes are unknown, but the mathematical probability distribution of possible outcomes can be calculated or insured against (e.g., life insurance or rolling a fair die).\n- True Uncertainty: Situations where outcomes are fundamentally unique and unprecedented, making mathematical probabilities impossible to compute.\nKnight argued that true entrepreneurship exists solely in bearing non-insurable uncertainty.",
            "explanation": "Frank Knight (1921) Risk, Uncertainty and Profit from ENT 211 Lecture 1.",
            "why_wrong": {},
            "source": "ENT 211 Lecture 1 Slides; Knightian Uncertainty"
        },
        {
            "id": "ent211-fnd-fc06",
            "course": "ENT 211",
            "topic": "Entrepreneurship Foundations: Value, Risk & Thinkers",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "intrapreneurship", "corporate"],
            "question": "What is Intrapreneurship, and how does it differ from traditional independent Entrepreneurship?",
            "answer": "- Intrapreneurship (Corporate Entrepreneurship): The practice of acting like an entrepreneur while working inside an existing, established corporation, innovating new products or divisions using company funding and resources without risking personal capital.\n- Entrepreneurship: Founding and operating an independent new venture, assuming direct personal financial, career, and legal risks.",
            "explanation": "Pinchot (1985) intrapreneurship concept in ENT 211.",
            "why_wrong": {},
            "source": "ENT 211 Lecture 1 Slides"
        },
        {
            "id": "ent211-fnd-fc07",
            "course": "ENT 211",
            "topic": "Entrepreneurship Foundations: Value, Risk & Thinkers",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "value-creation-capture"],
            "question": "Contrast Value Creation with Value Capture in entrepreneurial business models.",
            "answer": "- Value Creation: The total utility, problem resolution, and economic benefit delivered to customers by a company's product or service.\n- Value Capture: The portion of that created value that the enterprise monetizes and retains as gross profit through pricing, monetization mechanics, and sustainable competitive advantage.\nA venture that creates immense value but cannot capture it will inevitably fail.",
            "explanation": "Business model mechanics from ENT 211 Topic 1.",
            "why_wrong": {},
            "source": "ENT 211 Topic 1 Slides"
        },
        {
            "id": "ent211-fnd-fc08",
            "course": "ENT 211",
            "topic": "Entrepreneurship Foundations: Value, Risk & Thinkers",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "schumpeter", "creative-destruction"],
            "question": "What did Joseph Schumpeter mean by the economic term 'Creative Destruction'?",
            "answer": "Creative Destruction is the relentless process of industrial mutation that incessantly revolutionizes the economic structure from within, destroying obsolete industries, legacy companies, and technologies while creating innovative, superior replacements (e.g., digital streaming destroying video rental stores, or smartphones rendering standalone pocket calculators and GPS units obsolete).",
            "explanation": "Schumpeterian economics from ENT 211 Lecture 1 & Theories.",
            "why_wrong": {},
            "source": "ENT 211 Lecture 1 Slides; Schumpeter (1942)"
        }
    ],

    "innovation_types_sources.json": [
        {
            "id": "ent211-inn-fc05",
            "course": "ENT 211",
            "topic": "Innovation vs Invention: Types, Sources & Strategy",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "incremental-vs-radical"],
            "question": "Contrast Incremental Innovation with Radical (Breakthrough) Innovation.",
            "answer": "- Incremental Innovation: Continuous, small-scale improvements made to existing products, services, or manufacturing processes to enhance efficiency, reduce costs, or extend lifecycle (e.g., annual smartphone camera spec updates).\n- Radical Innovation: Groundbreaking technological paradigm shifts that create entirely new markets, establish new industries, and render existing products obsolete (e.g., the invention of the automobile or commercial personal computers).",
            "explanation": "Innovation classification from ENT 211 Topic 2.",
            "why_wrong": {},
            "source": "ENT 211 Topic 2 Slides"
        },
        {
            "id": "ent211-inn-fc06",
            "course": "ENT 211",
            "topic": "Innovation vs Invention: Types, Sources & Strategy",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "architectural-vs-modular"],
            "question": "Differentiate between Architectural Innovation and Modular Innovation.",
            "answer": "- Architectural Innovation: Reconfigures the way existing components are linked together without fundamentally changing the underlying core technologies (e.g., shrinking desktop computer parts into a portable laptop).\n- Modular Innovation: Significantly overhauls a core component's internal technology while leaving the overall system architecture unchanged (e.g., replacing an analog car dashboard gauge with a digital LCD cluster).",
            "explanation": "Henderson and Clark (1990) innovation matrix in ENT 211.",
            "why_wrong": {},
            "source": "ENT 211 Topic 2 Slides"
        },
        {
            "id": "ent211-inn-fc07",
            "course": "ENT 211",
            "topic": "Innovation vs Invention: Types, Sources & Strategy",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "drucker", "seven-sources"],
            "question": "List Peter Drucker's Seven Sources of Innovative Opportunity.",
            "answer": "Internal Sources:\n1. The Unexpected (unexpected success or failure)\n2. Incongruities (gaps between reality and expectations)\n3. Process Need (bottlenecks in an existing workflow)\n4. Industry and Market Structure Changes.\nExternal Sources:\n5. Demographics (population shifts, aging, education)\n6. Changes in Perception and Meaning\n7. New Knowledge (scientific breakthroughs and patents).",
            "explanation": "Peter Drucker (1985) Innovation and Entrepreneurship from ENT 211.",
            "why_wrong": {},
            "source": "ENT 211 Topic 2 Slides; Drucker (1985)"
        },
        {
            "id": "ent211-inn-fc08",
            "course": "ENT 211",
            "topic": "Innovation vs Invention: Types, Sources & Strategy",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "disruptive-innovation", "christensen"],
            "question": "Explain Clayton Christensen's Theory of Disruptive Innovation.",
            "answer": "Disruptive Innovation describes a process whereby a smaller company with fewer resources successfully challenges established incumbent businesses.\nThe entrant targets overlooked, low-end market tiers or non-consumers with a simpler, cheaper, or more accessible solution. As the entrant's quality steadily improves, it moves upmarket, eventually displacing the market leaders who were focused solely on sustaining high-margin customers (e.g., Netflix displacing Blockbuster).",
            "explanation": "Clayton Christensen (1997) The Innovator's Dilemma in ENT 211.",
            "why_wrong": {},
            "source": "ENT 211 Topic 2 Slides"
        }
    ],

    "entrepreneurship_theories.json": [
        {
            "id": "ent211-thy-fc05",
            "course": "ENT 211",
            "topic": "Theories of Entrepreneurship (Schumpeter, Knight, Kirzner)",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "kirzner", "alertness"],
            "question": "How does Israel Kirzner's Theory of Entrepreneurial Alertness differ from Schumpeter's Theory of Innovation?",
            "answer": "- Israel Kirzner: The entrepreneur is an 'alert arbitrageur' who spots existing market imperfections, price discrepancies, and unmet demands that others have overlooked, moving the market TOWARD equilibrium without necessarily inventing new technology.\n- Joseph Schumpeter: The entrepreneur is a 'dynamic disruptor' who introduces radical innovations (new goods, new methods, new markets), violently throwing the market OUT of equilibrium through Creative Destruction.",
            "explanation": "Kirzner vs Schumpeter schools of entrepreneurship in ENT 211 Theories.",
            "why_wrong": {},
            "source": "ENT 211 Theories Slides; Kirzner (1973)"
        },
        {
            "id": "ent211-thy-fc06",
            "course": "ENT 211",
            "topic": "Theories of Entrepreneurship (Schumpeter, Knight, Kirzner)",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "mcclelland", "nach"],
            "question": "Explain David McClelland's Theory of Needs and the role of 'nAch' in entrepreneurship.",
            "answer": "McClelland posited that human motivation is driven by three needs: Need for Affiliation (nAff), Need for Power (nPower), and Need for Achievement (nAch).\nEntrepreneurs are overwhelmingly characterized by high nAch: they possess an internal drive to excel, prefer calculated moderate risks over reckless gambles, take personal responsibility for problem-solving, and actively seek continuous feedback on their performance.",
            "explanation": "David McClelland (1961) The Achieving Society in ENT 211.",
            "why_wrong": {},
            "source": "ENT 211 Theories Slides; McClelland (1961)"
        },
        {
            "id": "ent211-thy-fc07",
            "course": "ENT 211",
            "topic": "Theories of Entrepreneurship (Schumpeter, Knight, Kirzner)",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "knight-profit", "theories"],
            "question": "Why did Frank Knight argue that economic profit is purely the reward for bearing uninsurable uncertainty?",
            "answer": "In perfect competition with quantifiable risks, all predictable costs (labor, capital, insurance premiums) are factored into market prices, driving economic profit to zero.\nTherefore, true positive economic profit can only arise from navigating unpredictable, non-insurable events and unique uncertainties where the entrepreneur's superior judgment and foresight prove accurate.",
            "explanation": "Knightian economic theory of profit from ENT 211 Theories.",
            "why_wrong": {},
            "source": "ENT 211 Theories Slides; Knight (1921)"
        },
        {
            "id": "ent211-thy-fc08",
            "course": "ENT 211",
            "topic": "Theories of Entrepreneurship (Schumpeter, Knight, Kirzner)",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "weber", "protestant-ethic"],
            "question": "What was Max Weber's Sociological Perspective on the rise of entrepreneurship?",
            "answer": "In 'The Protestant Ethic and the Spirit of Capitalism' (1905), Max Weber argued that modern entrepreneurship was catalyzed by cultural and religious values—specifically ascetic Protestantism (Calvinism), which promoted hard work, frugality, rational investment, worldly calling, and the reinvestment of wealth rather than hedonistic personal consumption.",
            "explanation": "Sociological theories of entrepreneurship in ENT 211 Theories.",
            "why_wrong": {},
            "source": "ENT 211 Theories Slides; Weber (1905)"
        }
    ],

    "opportunity_identification_feasibility.json": [
        {
            "id": "ent211-opp-fc05",
            "course": "ENT 211",
            "topic": "Opportunity Identification, Evaluation & Feasibility",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "pestel", "environmental-scanning"],
            "question": "What is the PESTEL Framework in entrepreneurial environmental opportunity scanning?",
            "answer": "PESTEL analyzes external macro-environmental forces that create business opportunities or threats:\n- P: Political (tax policies, trade tariffs, government stability)\n- E: Economic (interest rates, inflation, consumer disposable income)\n- S: Social (demographics, cultural shifts, consumer lifestyle trends)\n- T: Technological (AI, automation, broadband adoption)\n- E: Environmental (climate change policies, sustainability)\n- L: Legal (consumer protection, labor laws, patents).",
            "explanation": "Macro-environmental opportunity identification from ENT 211 Opportunity Slides.",
            "why_wrong": {},
            "source": "ENT 211 Opportunity Slides"
        },
        {
            "id": "ent211-opp-fc06",
            "course": "ENT 211",
            "topic": "Opportunity Identification, Evaluation & Feasibility",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "porters-five-forces", "industry-attractiveness"],
            "question": "Name Michael Porter's Five Forces and explain how they evaluate industry attractiveness.",
            "answer": "1. Threat of New Entrants: Ease of entry for new competitors.\n2. Bargaining Power of Buyers: Customers' ability to drive down prices.\n3. Bargaining Power of Suppliers: Key suppliers' control over input prices.\n4. Threat of Substitute Products: Availability of alternative ways to satisfy user needs.\n5. Intensity of Competitive Rivalry: Existing competition among incumbent firms.\nIndustries where all five forces are strong exhibit low profit margins; industries where forces are weak are highly attractive for new entrepreneurial entry.",
            "explanation": "Porter (1979) industry structural analysis in ENT 211.",
            "why_wrong": {},
            "source": "ENT 211 Opportunity Slides"
        },
        {
            "id": "ent211-opp-fc07",
            "course": "ENT 211",
            "topic": "Opportunity Identification, Evaluation & Feasibility",
            "type": "flashcard",
            "difficulty": 2,
            "tags": ["flashcard", "feasibility-analysis", "four-pillars"],
            "question": "What are the four pillars of a comprehensive Feasibility Analysis before launching a venture?",
            "answer": "1. Product / Service Feasibility: Assessing product desirability, problem-solution fit, and willingness-to-buy via concept testing.\n2. Industry / Target Market Feasibility: Evaluating industry attractiveness, market growth rate, and target market niche accessibility.\n3. Organizational Feasibility: Determining whether the founding team possesses the management prowess, technical competence, and key resources needed.\n4. Financial Feasibility: Projecting total start-up cash needed, financial performance of similar businesses, and overall venture profitability.",
            "explanation": "Feasibility analysis framework from ENT 211 Opportunity Slides.",
            "why_wrong": {},
            "source": "ENT 211 Opportunity Slides"
        },
        {
            "id": "ent211-opp-fc08",
            "course": "ENT 211",
            "topic": "Opportunity Identification, Evaluation & Feasibility",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "lean-startup", "mvp"],
            "question": "What is the Minimum Viable Product (MVP) in the Lean Startup methodology?",
            "answer": "An MVP is the simplest, most stripped-down version of a new product that enables a founding team to complete one full turn of the Build-Measure-Learn feedback loop with the minimum amount of effort and development time.\nIts purpose is to test fundamental business hypotheses and gather validated learning from early adopters, preventing teams from spending months building products nobody wants.",
            "explanation": "Eric Ries (2011) Lean Startup framework in ENT 211.",
            "why_wrong": {},
            "source": "ENT 211 Opportunity Slides"
        }
    ]
}

print("ENT 211 flashcard definitions compiled.")


def apply_flashcards():
    courses_to_update = [
        ("IFT 205", IFT205_FLASHCARDS),
        ("INS 202", INS202_FLASHCARDS),
        ("ENT 211", ENT211_FLASHCARDS)
    ]

    total_added = 0
    updated_files = []

    for course_code, card_dict in courses_to_update:
        course_dir = os.path.join("app", "content", course_code)
        for fname, flashcards in card_dict.items():
            filepath = os.path.join(course_dir, fname)
            if not os.path.exists(filepath):
                print(f"Warning: file {filepath} not found!")
                continue

            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            existing_qs = data.get("questions", [])
            existing_ids = {q.get("id") for q in existing_qs}

            new_cards_to_add = []
            for fc in flashcards:
                if fc["id"] not in existing_ids:
                    new_cards_to_add.append(fc)
                else:
                    print(f"Card {fc['id']} already exists in {fname}, skipping.")

            if new_cards_to_add:
                # Append flashcards to questions list
                data["questions"] = existing_qs + new_cards_to_add
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                total_added += len(new_cards_to_add)
                updated_files.append((course_code, fname, len(new_cards_to_add), len(data["questions"])))
                print(f"Added {len(new_cards_to_add)} flashcards to {course_code}/{fname} (Now {len(data['questions'])} total)")

    print(f"\nSuccessfully added {total_added} total flashcards across {len(updated_files)} files!")

    # Now update app/content/index.json
    index_path = os.path.join("app", "content", "index.json")
    with open(index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)

    for course in index_data.get("courses", []):
        c_code = course.get("code")
        c_dir = os.path.join("app", "content", c_code)
        course_total_qs = 0

        for topic in course.get("topics", []):
            t_file = topic.get("file")
            # t_file looks like "IFT 205/it_foundations_building_blocks.json"
            full_t_path = os.path.join("app", "content", t_file)
            if os.path.exists(full_t_path):
                with open(full_t_path, "r", encoding="utf-8") as tf:
                    t_data = json.load(tf)
                
                # Collect question IDs from questions + case studies
                all_ids = [q.get("id") for q in t_data.get("questions", []) if q.get("id")]
                for cs in t_data.get("case_studies", []):
                    for sq in cs.get("sub_questions", []):
                        if sq.get("id"):
                            all_ids.append(sq.get("id"))

                topic["question_count"] = len(all_ids)
                topic["question_ids"] = all_ids
                course_total_qs += len(all_ids)

        course["total_questions"] = course_total_qs
        print(f"Updated index.json: Course {c_code} total active questions = {course_total_qs}")

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    print("index.json successfully updated with fresh question counts and IDs.")


if __name__ == "__main__":
    apply_flashcards()


