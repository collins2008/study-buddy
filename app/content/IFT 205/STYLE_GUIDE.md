# Course Style Guide: IFT 205 (Introduction to Information Technology)
*Nile University of Nigeria • Department of Information Technology (200 Level, First Semester)*
*Lecturer: Zakariyya Abdullahi Adamu*

---

## 1. Course Nature & Examination Pedagogy
- **Subject Type**: Foundational Systems Theory, IT Infrastructure & Applied Computer Architecture.
- **Reference Texts**:
  - Shelly, G. B., & Vermaat, M. E. *Discovering Computers: Tools, Apps, Devices, and the Impact of Technology*. Cengage Learning.
  - Stair, R. M., & Reynolds, G. W. *Principles of Information Systems*. Cengage Learning.
  - Williams, B. K. *Using Information Technology: A Practical Introduction to Computers & Communications*. McGraw-Hill.
- **Lecturer Focus & High-Priority Signals (Direct from Lecture Decks & Notebooks)**:
  - **Foundational Triad**: Data (raw unorganized facts) vs Information (processed, structured, meaningful data). The 3 Building Blocks: Hardware, Software, and People/Users.
  - **Hardware Architecture**: Von Neumann architecture (Stored-program concept); CPU internals: Control Unit (CU), Arithmetic Logic Unit (ALU), Registers, Cache (L1, L2, L3).
  - **Memory & Storage Hierarchy**: Primary storage (RAM — volatile, working memory; ROM/firmware — non-volatile startup) vs Secondary storage (HDD — magnetic platters, moving parts; SSD — flash memory, no moving parts, low latency). The 3-2-1 backup strategy and backup types (Full, Incremental, Differential). Backup vs Sync.
  - **Operating Systems & Software**: System software (OS, Device Drivers, Utilities) vs Application software (General-purpose, Specialised, Custom).
  - **OS Core Functions**: Process management (scheduling, multitasking), Memory management, Device management (drivers), File system management, Security & User accounts.
  - **User Interface Trade-offs**: GUI (windows, icons, menus, pointers — intuitive, resource-intensive) vs CLI (typed commands — fast, low resource, powerful, steep learning curve).
  - **OS Installation & Disk Formatting**: BIOS/UEFI boot order, bootable installation media, disk partitioning (MBR vs GPT), file system formatting (NTFS, FAT32, ext4), formatting implications (erasing partition tables/data structures).
  - **Computer Evolution & Generations**:
    - Pioneers: Abacus, Babbage (Difference & Analytical Engines), Ada Lovelace (first programmer / algorithm sequence), Herman Hollerith (punched cards, 1890 US Census, IBM roots), Alan Turing (theoretical model of computation), ENIAC (first general-purpose electronic computer), John von Neumann (stored-program concept).
    - Generations: 1st (Vacuum Tubes), 2nd (Transistors), 3rd (Integrated Circuits), 4th (Microprocessors), 5th (AI & Parallel Processing).
    - Classification by size/capacity: Microcomputers (desktops, laptops, mobiles), Workstations, Servers, Mainframes (high-volume concurrent transactions), Supercomputers (HPC, floating point calculations), Embedded Systems (single dedicated function).
  - **Networking & Communications**:
    - Definition of Network: Interconnected computing devices sharing resources and exchanging data.
    - **CRITICAL LECTURER HINT**: *"A Local Area Network (LAN) does NOT require an active internet connection to function."*
    - Topologies: Star (central switch/hub, single cable failure doesn't break network), Bus (backbone cable, terminators required), Ring (token passing), Mesh (high redundancy, expensive), Tree/Hybrid.
    - Network Devices: Switch (OSI Layer 2, MAC addresses, local segment forwarding), Router (OSI Layer 3, IP addresses, internetwork packet routing), Modem (modulation/demodulation), Access Point (WLAN bridge).
    - Bandwidth (theoretical maximum channel capacity) vs Throughput (actual achieved data transfer rate) vs Latency (round-trip transit delay).
    - **IPv4 Address Classes (Mandatory Lecturer Note)**:
      - **Class A**: 1.0.0.0 – 126.255.255.255 | Default Subnet Mask: `255.0.0.0` (/8) | Huge networks (127.x.x.x reserved for loopback/diagnostics).
      - **Class B**: 128.0.0.0 – 191.255.255.255 | Default Subnet Mask: `255.255.0.0` (/16) | Medium networks.
      - **Class C**: 192.0.0.0 – 223.255.255.255 | Default Subnet Mask: `255.255.255.0` (/24) | Small LANs.
      - **Class D**: 224.0.0.0 – 239.255.255.255 | Multicasting (no default host mask).
      - **Class E**: 240.0.0.0 – 255.255.255.255 | Experimental / Research.
      - **Private IP Ranges (RFC 1918)**: Class A: `10.0.0.0/8`, Class B: `172.16.0.0/12` (`172.16.x.x`–`172.31.x.x`), Class C: `192.168.0.0/16`.
    - ISPs (Internet Service Providers) and their tiered infrastructure (Tier 1 backbones, Tier 2 regional, Tier 3 retail).

---

## 2. Examination Blueprint & Question Formats
All generated questions must rigorously test concepts and practical IT scenarios:
- **MCQ (Single Answer)**: Misconception-based distractors with deep pedagogical `why_wrong` explanations.
- **Multi-Select**: Comprehensive identification of functions, components, or characteristics.
- **True/False with Justification (`true_false_why`)**: Counter-intuitive assertions (e.g. LAN operating without internet, RAM capacity vs processor clock speed).
- **Type Answer**: Normalised technical terms, subnet masks, generation hardware components, IP class boundaries.
- **Cloze**: Multi-blank structural definitions and architectural flows.
- **Matching**: Matching generations to technologies, IP classes to address ranges/default masks, computer types to enterprise roles.
- **Sequencing**: Ordering historical computing milestones, the 4-step information processing cycle (Input $\to$ Process $\to$ Output $\to$ Storage), OS clean installation steps, DNS resolution steps.
- **Explain (Free-text with Marking Points)**: Analytical comparisons (HDD vs SSD, CLI vs GUI, Backup vs Sync, LAN vs WAN, Server vs Client).
- **Case Studies**: Real-world university, banking, hospital, or enterprise IT deployment scenarios with 3–5 multi-part questions evaluating hardware selection, IP allocation, network design, and storage backup strategies.

---

## 3. Difficulty Level Distribution
- **Level 1 (Recall)**: Definitions, inventors, year milestones, standard default masks (~25%).
- **Level 2 (Understand)**: Explaining operational mechanisms, device roles, storage technologies (~30%).
- **Level 3 (Apply)**: Choosing hardware for an engineering firm, assigning valid host IP addresses in a Class C subnet, diagnosing network disconnections (~30%).
- **Level 4 (Analyze/Evaluate)**: Evaluating backup vs replication strategies after ransomware, sizing network topologies, analyzing performance bottlenecks (~15%).
- **Target**: At least 40% Level 3–4 across all topics.
