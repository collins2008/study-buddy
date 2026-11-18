# Exhaustive Inventory: Topic 2 — Hardware Components: Input, CPU, Memory & Storage
*Course: IFT 205 (Introduction to Information Technology) — Nile University of Nigeria*
*Source Materials: IFT205_Week2 (Part B Slides 5–13), Week 5 (Part 2 Slides 23–48), Textbooks*

---

## 1. Central Processing Unit (CPU) & Architecture
- **CPU (Central Processing Unit / Processor)**: The primary electronic chip that interprets, fetches, decodes, and executes program instructions.
- **Von Neumann Architecture**: The foundational computer architecture comprising CPU, Memory, and Input/Output interfaces, with instructions and data stored together in memory (Stored-Program Concept).
- **CPU Internal Components**:
  - *Control Unit (CU)*: Directs and coordinates the entire computer system's operations; fetches instructions from memory, decodes them, and manages signal routing.
  - *Arithmetic Logic Unit (ALU)*: Performs all arithmetic calculations (addition, subtraction, multiplication) and logical decisions/comparisons (AND, OR, NOT, equal to, greater than).
  - *Registers*: High-speed, tiny internal CPU memory storage locations holding data currently being processed, memory addresses, or condition flags (e.g., Program Counter, Accumulator, Instruction Register).
  - *Cache Memory (L1, L2, L3)*: Extremely fast SRAM located on or adjacent to the CPU chip, buffering frequently accessed instructions/data to reduce high-latency trips to main RAM. L1 is smallest and fastest; L3 is largest and shared among cores.
- **Machine Cycle (Instruction Cycle)**:
  1. *Fetch*: Retrieve the next instruction from RAM/cache using the Program Counter.
  2. *Decode*: The Control Unit translates the instruction into internal micro-operations.
  3. *Execute*: The ALU or internal hardware carries out the instruction.
  4. *Store*: Results are written back to registers or main memory.

---

## 2. Memory Hierarchy: Primary vs Secondary Storage
- **Memory Hierarchy**: Registers $\to$ CPU Cache $\to$ Primary Storage (RAM) $\to$ Secondary Storage (SSD/HDD) $\to$ Tertiary/Offline Storage (Cloud/Tape). Speed decreases down the hierarchy; capacity increases; cost per gigabyte decreases.
- **Primary Storage (Main Memory)**: Directly accessible by the CPU over high-speed buses.
  - *RAM (Random Access Memory)*: Volatile working memory holding active operating system files, application programs, and unsaved documents. When power is lost, all data in RAM disappears. More RAM enables greater multitasking without excessive paging/swapping.
  - *ROM (Read-Only Memory) & Firmware*: Non-volatile memory retaining permanent startup instructions (BIOS/UEFI) required to boot the system and initialize hardware peripherals.
- **Secondary Storage**: Non-volatile storage designed to retain operating systems, software applications, and user files permanently.
  - *Hard Disk Drive (HDD)*: Uses magnetized spinning aluminum/glass platters and moving actuator arms with electromagnetic read/write heads. Characterized by mechanical seek time, rotational latency, vulnerability to physical shock, and low cost per terabyte.
  - *Solid-State Drive (SSD)*: Uses non-volatile NAND flash memory chips with electrical floating-gate or charge-trap transistors. No moving mechanical parts, silent operation, high read/write speeds, low power consumption, and high shock resistance.
- **Other Secondary & Removable Media**: USB flash drives, SD cards, Optical discs (CD, DVD, Blu-ray), External hard drives.

---

## 3. Motherboard, Buses, Ports & Power
- **Motherboard**: The main printed circuit board (PCB) connecting CPU, RAM, expansion cards, storage drives, and peripheral ports.
- **System Buses**: Electrical pathways transferring signals:
  - *Data Bus*: Carries actual bidirectional data between CPU, RAM, and devices.
  - *Address Bus*: Unidirectional bus specifying the physical memory address for read/write operations.
  - *Control Bus*: Carries control signals (read, write, interrupt requests, clock pulses).
- **Common Ports**: USB (Type-A, Type-C), HDMI, DisplayPort, RJ-45 Ethernet, 3.5mm Audio jack.
- **Power Supply Unit (PSU)**: Converts AC wall power into regulated low-voltage DC power.

---

## 4. Input & Output Hardware
- **Input Devices**: Keyboard, optical mouse, trackpad, flatbed document scanner, barcode reader, RFID scanner, microphone, webcam.
- **Output Devices**:
  - *Monitors*: LCD (LED-backlit), OLED. Measured by resolution (pixels) and refresh rate (Hz).
  - *Printers*:
    - *Inkjet*: Sprays liquid ink droplets; excellent for photo printing; high ink replacement cost.
    - *Laser*: Uses powdered toner, an electrostatic drum, and a heated fuser roller; fast, economical for high-volume office text documents.
    - *Thermal*: Uses heat-sensitive paper; used in POS receipt printers and ATM slips.
  - *Speakers & Headphones*: Convert digital audio streams to analog sound waves.

---

## 5. Storage Protection, Backups & Cloud Storage
- **The 3-2-1 Backup Rule**:
  - **3** copies of critical data (1 primary working copy + 2 separate backup copies).
  - **2** different storage media types (e.g., local SSD + external magnetic HDD or NAS).
  - **1** copy stored offsite (e.g., remote cloud storage or geographically separate facility).
- **Backup Types**:
  - *Full Backup*: Copies all selected data files completely. Slowest to perform and consumes the most storage space, but fastest and simplest to restore (requires only 1 media set).
  - *Incremental Backup*: Copies only files created or modified since the *last backup of any kind* (full or incremental). Fastest to run and uses minimal space, but slowest to restore (requires the last full backup PLUS every consecutive incremental backup).
  - *Differential Backup*: Copies all files created or modified since the *last Full backup*. Moderate speed and space; restoration requires only the last full backup PLUS the single latest differential backup.
- **Backup vs Synchronization**:
  - *Backup*: Creates point-in-time independent recovery snapshots. Accidental file deletion on the source does not delete the backup copy.
  - *Synchronization (Sync)*: Mirrors files between locations in real time or near-real time. If a file is corrupted, deleted, or encrypted by ransomware on the source, the deletion/corruption is automatically mirrored to the synced destination!
- **Cloud Storage & Service Models**:
  - *IaaS (Infrastructure as a Service)*: Virtual machines, raw storage, networks (e.g., AWS EC2, Azure VMs).
  - *PaaS (Platform as a Service)*: Development environments and databases (e.g., Heroku, Google App Engine).
  - *SaaS (Software as a Service)*: Complete applications accessible via browser (e.g., Google Docs, Microsoft 365).
