# IFT 205: Introduction to Information Technology — Condensed Exam Cheatsheet
*Nile University of Nigeria • Department of Information Technology (200 Level, First Semester)*
*Lecturer: Zakariyya Abdullahi Adamu • Faculty Examiner Quick-Reference Sheet*

---

## 1. IT Foundations & The Triad
- **Data vs Information**: Data consists of raw, unprocessed, unorganized facts and figures without inherent context. Information is data that has been processed, organized, structured, or contextualized to possess meaning and value for decision-making.
- **The 3 Building Blocks of IT**:
  1. **Hardware**: Tangible electronic machinery and peripherals.
  2. **Software**: Intangible programs, scripts, and instructions.
  3. **People**: Users, administrators, engineers, and decision-makers who direct and consume systems.
- **Computer vs Network vs Internet**:
  - *Computer*: Autonomous electronic machine executing Input $\to$ Processing $\to$ Output $\to$ Storage under electrical power.
  - *Network*: Two or more interconnected computers sharing resources and communicating via protocols.
  - *Internet*: Global "network of networks" interconnected through TCP/IP protocols.
- **Networks vs Networking vs Networkers**:
  - *Networks*: Physical and logical infrastructure.
  - *Networking*: The practice and protocol methods of connecting computers.
  - *Networkers*: The human engineers who design and maintain systems.
- **Processing Paradigms**:
  - *Batch Processing*: Collecting transactions and executing them collectively at a scheduled off-peak time (e.g. monthly payroll, student semester GPA computation).
  - *Real-time / OLTP*: Processing transactions instantaneously as they occur (e.g. ATM cash withdrawals, airline flight seat reservation).

---

## 2. Hardware Architecture & Memory Hierarchy
- **Von Neumann Architecture**: Central Processing Unit (CPU), Primary Memory, and I/O interfaces; instructions and data reside in the same memory (*Stored-Program Concept*).
- **CPU Internals**:
  - *Control Unit (CU)*: Directs and coordinates system operations, fetches instructions, decodes opcodes.
  - *Arithmetic Logic Unit (ALU)*: Performs arithmetic ($+,-,\times$) and logical comparisons ($\text{AND}, \text{OR}, \text{NOT}$).
  - *Registers*: High-speed, tiny internal CPU storage (Program Counter holds next instruction address; Accumulator holds working results).
  - *Cache (L1, L2, L3)*: Ultra-fast Static RAM (SRAM) on CPU die bridging processor-DRAM speed gap.
- **4-Stage Machine Cycle**: **Fetch** $\to$ **Decode** $\to$ **Execute** $\to$ **Store (Writeback)**.
- **Memory & Storage Comparison**:
  - *RAM (Random Access Memory)*: Primary volatile working memory; lost upon power termination. More RAM enables multitasking without disk paging, but does not alter CPU clock frequency.
  - *ROM (Read-Only Memory) & Firmware*: Non-volatile startup chips holding BIOS/UEFI bootstrap code.
  - *HDD (Hard Disk Drive)*: Magnetic platters, mechanical read/write heads; high latency, lower cost/GB.
  - *SSD (Solid-State Drive)*: NAND flash memory, zero moving parts; low latency, silent, shock-resilient.
- **Data Protection & Backups**:
  - **The 3-2-1 Rule**: **3** copies of data, across **2** different storage media types, with at least **1** copy kept offsite (cloud or remote facility).
  - *Full Backup*: Copies all files; slowest to run, fastest to restore (requires only 1 backup set).
  - *Incremental Backup*: Copies only files modified since the *last backup of any kind*; fastest to run, slowest to restore (requires Full + every incremental in sequence).
  - *Differential Backup*: Copies all files modified since the *last Full backup*; requires Full + latest Differential.
  - *Backup vs Sync*: Synchronization mirrors changes and deletions in real time (propagating ransomware/accidental deletes!). Backups create point-in-time independent recovery archives.

---

## 3. Operating Systems & Software
- **Software Categories**:
  - *System Software*: Operating Systems, Device Drivers, Utilities (antivirus, defragmenter), Firmware.
  - *Application Software*: General-purpose (word processors, spreadsheets), Specialised (CAD), Custom/Bespoke (university grading portal).
- **5 Core OS Functions**: Process Management, Memory Management (Virtual Memory/Paging), Device Management (Drivers), File System Management, Security & Access Control.
- **User Interfaces**:
  - *GUI*: WIMP (Windows, Icons, Menus, Pointers); intuitive, accessible, high resource footprint.
  - *CLI*: Text command syntax; fast, scriptable, lightweight, essential for headless server administration.
- **File Systems & Paths**:
  - *Default OS File Systems*: Windows internal = **NTFS**; Linux = **ext4**; Removable = **FAT32 / exFAT**.
  - *Absolute Path*: Starts from system root/drive (`C:\Users\Student\file.txt`).
  - *Relative Path*: Evaluated from current working directory (`..\images\banner.png`).
- **Clean OS Installation Steps**:
  1. Create bootable USB using official ISO image (Rufus / Media Creation Tool).
  2. Enter motherboard BIOS/UEFI firmware (F2/F12/Del) and configure boot order priority to USB drive.
  3. Boot into installer; select Custom (Advanced) installation.
  4. Delete existing partitions to Unallocated Space; partition drive (GPT for UEFI) and format partition with NTFS.
  5. Complete file installation and configure Out-of-Box Experience (OOBE) user accounts and drivers.
- **Quick vs Full Format**: Quick format merely rewrites file system allocation tables (MFT) making disk appear empty; Full format rewrites tables AND scans every sector for bad blocks while zeroing sectors.

---

## 4. Networking & IPv4 Addressing Table
- **CRITICAL EXAM PRINCIPLE**: *"A Local Area Network (LAN) does NOT require an active internet connection to operate!"* (File sharing and network printing function completely over local switches).
- **Network Devices**:
  - *Switch*: Layer 2 device; inspects MAC addresses to forward frames locally without collisions.
  - *Router*: Layer 3 device; inspects IP addresses to route packets between different networks.
- **Network Performance**: Bandwidth = theoretical capacity; Throughput = actual achieved transfer speed; Latency = transit delay (ms).

### IPv4 Address Classes Reference Table (Mandatory Examiner Standard)

| Class | First Octet Range | Leading Bits | Default Subnet Mask | CIDR | Network / Host Bits | Usable Hosts per Network ($2^h - 2$) | Primary Intended Purpose |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **A** | **1 – 126** | `0` | **`255.0.0.0`** | `/8` | 8 net / 24 host | **16,777,214** | Enormous global corporations |
| *Loop* | **127** | `01111111` | Reserved | `/8` | — | — | **Internal Loopback / Localhost** (`127.0.0.1`) |
| **B** | **128 – 191** | `10` | **`255.255.0.0`** | `/16` | 16 net / 16 host | **65,534** | Medium-to-large enterprises & universities |
| **C** | **192 – 223** | `110` | **`255.255.255.0`** | `/24` | 24 net / 8 host | **254** | Small departmental LANs & home networks |
| **D** | **224 – 239** | `1110` | *None* | — | — | — | **Multicasting** (group streaming) |
| **E** | **240 – 255** | `1111` | *None* | — | — | — | **Experimental & Future Research** |

- **RFC 1918 Private IP Ranges (Non-routable over Internet)**:
  - Class A Private: `10.0.0.0` to `10.255.255.255` (`10.0.0.0/8`)
  - Class B Private: `172.16.0.0` to `172.31.255.255` (`172.16.0.0/12`)
  - Class C Private: `192.168.0.0` to `192.168.255.255` (`192.168.0.0/16`)

---

## 5. Computer Evolution & Classification
- **Pioneers**:
  - *Charles Babbage*: Father of Computing; Difference Engine (math tables) & Analytical Engine (Store + Mill).
  - *Ada Lovelace*: First Computer Programmer; published algorithm for Bernoulli numbers.
  - *Herman Hollerith*: Punched-card tabulators for 1890 US Census; founded Tabulating Machine Co. (later IBM).
  - *Alan Turing*: Formalized algorithm theory via the Turing Machine; Enigma codebreaking.
  - *ENIAC (1945)*: First large-scale general-purpose electronic computer; 18,000 vacuum tubes, hardwire-programmed.
  - *John von Neumann*: Stored-Program Concept; instructions and data share internal electronic memory.

### The Five Computer Generations

| Gen | Dominant Hardware Technology | Memory Medium | Programming Languages | Defining Characteristics |
| :---: | :--- | :--- | :--- | :--- |
| **1st** (1940s-50s) | **Vacuum Tubes** | Magnetic drums | Machine language (binary) | Room-sized, extreme heat, high power, frequent failures (ENIAC, UNIVAC). |
| **2nd** (1950s-60s) | **Transistors** | Magnetic core | FORTRAN, COBOL, Assembly | Drastically smaller, faster, cooler, higher reliability. |
| **3rd** (1960s-70s) | **Integrated Circuits (ICs)** | Silicon semiconductor RAM | BASIC, Pascal, Timesharing OS | Keyboards and monitors replace punched cards (IBM System/360). |
| **4th** (1970s-Pres) | **Microprocessors** (VLSI/ULSI) | Semiconductor DRAM & Flash | High-level (C, C++, Java, Python) | Entire CPU on a single silicon chip; Personal Computers, laptops, Internet. |
| **5th** (Present+) | **AI & Parallel Architectures** | Distributed / Optical / Quantum | Natural Language, Neural Nets | Artificial Intelligence, Machine Learning, Exaflop supercomputing. |

- **Classification by Scale & Role**:
  - *Microcomputer*: Single-user PC, laptop, smartphone powered by a microprocessor.
  - *Workstation*: High-performance single-user engineering desktop with ECC RAM and professional GPUs for 3D CAD.
  - *Server*: High-availability networked computer providing 24/7 centralized services (web, database).
  - *Mainframe*: Enterprise powerhouse built for massive concurrent transaction processing (banking, reservations).
  - *Supercomputer*: Thousands of parallel CPUs executing quadrillions of floating-point calculations per second (**FLOPS**) for scientific simulations (weather, molecular modeling).
  - *Embedded System*: Dedicated microcontroller built into appliances/vehicles (microwave, ABS) for a specific task.
