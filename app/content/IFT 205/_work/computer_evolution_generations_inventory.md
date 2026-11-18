# Exhaustive Inventory: Topic 5 — Evolution & Classification of Computers
*Course: IFT 205 (Introduction to Information Technology) — Nile University of Nigeria*
*Source Materials: Evolution_and_Classification_of_Computers.pptx (45 slides), Standard Computer Science Histories*

---

## 1. Computing Milestones & Pioneers
- **Abacus**: Ancient manual calculating tool using beads on rods to represent positional values; reusable, low-cost, zero electricity required.
- **Mechanical Calculators**:
  - *Blaise Pascal (Pascaline, 1642)*: Gear-driven mechanical adding machine using rotating dials and carry mechanisms.
  - *Gottfried Wilhelm Leibniz (Step Reckoner, 1670s)*: Expanded mechanical calculation to perform multiplication and division via a stepped drum.
  - *Joseph Marie Jacquard (1804)*: Jacquard Loom utilizing punched wooden cards to automate complex fabric weaving patterns (early automated stored instruction concept).
- **Charles Babbage ("Father of Computing")**:
  - *Difference Engine (1820s)*: Designed to calculate and tabulate mathematical and astronomical polynomial tables mechanically using finite differences.
  - *Analytical Engine (1830s)*: The first conceptual design of a general-purpose, programmable mechanical computer. Incorporated modern computing architecture components: the "Store" (memory), the "Mill" (CPU/ALU), and input via punched cards.
- **Ada Lovelace ("First Computer Programmer")**:
  - Collaborated with Babbage; wrote the first published algorithm intended for implementation on the Analytical Engine (to compute Bernoulli numbers); recognized that computers could manipulate symbols beyond pure numbers.
- **Herman Hollerith & Punched Cards**:
  - Invented electromechanical punched card tabulating machines to process the 1890 US Census, completing in months what took years manually; founded the Tabulating Machine Company, which later became IBM (International Business Machines).
- **Alan Turing**:
  - Father of theoretical computer science and AI; formalized the mathematical concept of algorithms and computation via the abstract *Turing Machine* (1936); broke Enigma naval ciphers at Bletchley Park; formulated the Turing Test for machine intelligence.
- **The First Electronic Computers & ENIAC**:
  - *Vacuum Tubes*: Enabled electronic switching thousands of times faster than mechanical relays, but generated massive heat, consumed high electrical wattage, and failed frequently.
  - *ENIAC (Electronic Numerical Integrator and Computer, 1945)*: Built by J. Presper Eckert and John Mauchly at UPenn; the first large-scale, general-purpose electronic digital computer. Weighed 30 tons, occupied a 50-foot room, contained over 17,000 vacuum tubes, and was programmed by manually re-routing physical cables and patch switches.
- **John von Neumann & The Stored-Program Concept**:
  - Authored the *First Draft of a Report on the EDVAC* (1945). Proposed storing program instructions and working data together in the same internal electronic memory (the Von Neumann Architecture). This eliminated the need to physically rewire cables to run different programs.

---

## 2. The Five Computer Generations
1. **First Generation (approx. 1940s – 1956)**:
   - *Core Technology*: **Vacuum Tubes** for circuitry; magnetic drums for memory.
   - *Programming Language*: Machine language (binary 0s and 1s); primitive assembly.
   - *Characteristics*: Enormous physical size (room-sized), massive electricity consumption, extreme heat generation, frequent component failures, slow processing (milliseconds).
   - *Examples*: ENIAC, EDVAC, UNIVAC I, IBM 701.
2. **Second Generation (approx. 1956 – 1963)**:
   - *Core Technology*: **Transistors** (invented 1947 at Bell Labs by Bardeen, Brattain, Shockley).
   - *Programming Language*: Early high-level assembly and procedural languages (**FORTRAN, COBOL**).
   - *Memory*: Magnetic core memory; magnetic tape and early disk storage.
   - *Characteristics*: Drastically smaller, faster, cooler, more reliable, and more energy-efficient than vacuum tubes.
   - *Examples*: IBM 1401, IBM 7090, CDC 1604.
3. **Third Generation (approx. 1964 – 1971)**:
   - *Core Technology*: **Integrated Circuits (ICs)** (invented by Jack Kilby and Robert Noyce; multiple miniature transistors etched onto a single silicon semiconductor wafer).
   - *Programming & OS*: Operating systems introduced multiprogramming and timesharing; high-level languages like BASIC, Pascal.
   - *Interaction*: Keyboards and visual monitors replaced punched cards and paper printouts.
   - *Characteristics*: Greatly reduced cost and size, increased computational speed (nanoseconds).
   - *Examples*: IBM System/360 series, PDP-8 minicomputer.
4. **Fourth Generation (approx. 1971 – Present)**:
   - *Core Technology*: **Microprocessors** (VLSI — Very Large Scale Integration and ULSI — Ultra Large Scale Integration), placing the entire CPU onto a single silicon chip (Intel 4004 in 1971).
   - *Milestones*: Rise of Personal Computers (Apple II, IBM PC in 1981); Graphical User Interfaces (macOS, Windows); optical storage, flash memory, local networking, and the Internet.
   - *Characteristics*: Highly compact, affordable for individuals, reliable, powerful, portable (laptops, smartphones).
5. **Fifth Generation (Present & Future)**:
   - *Core Technology*: **Artificial Intelligence (AI), Parallel and Distributed Processing, Machine Learning, and Quantum Computing**.
   - *Interaction*: Natural language processing, voice recognition, neural networks.
   - *Characteristics*: Adaptive learning, autonomous decision support, massive parallel processing.

---

## 3. Classification of Computers by Size, Capacity & Role
1. **Microcomputers (Personal Computers - PCs)**:
   - Designed for single-user operation; powered by microprocessors.
   - *Subtypes*: Desktop PCs, Laptops/Notebooks (integrated screen, keyboard, battery), Tablets, Smartphones.
2. **Workstations**:
   - High-end, powerful single-user desktop computers optimized for demanding technical, scientific, or artistic workloads (e.g., 3D CAD modeling, video rendering, geospatial analysis).
   - Features: High-core-count workstation CPUs (Intel Xeon, AMD Threadripper), ECC (Error-Correcting Code) RAM, dedicated professional GPUs (NVIDIA RTX/Quadro).
3. **Servers**:
   - High-performance, highly reliable computers dedicated to providing shared services and resources (web pages, files, databases, user authentication) to client devices over a network.
   - Focus on continuous 24/7/365 uptime, hot-swappable drives (RAID), redundant power supplies, and multi-gigabit network interfaces.
4. **Mainframe Computers**:
   - Massive enterprise systems capable of supporting thousands of simultaneous users and executing millions of concurrent high-volume transactions.
   - *Primary Strengths*: Unmatched I/O data throughput, absolute reliability (RAS — Reliability, Availability, Serviceability), and fault tolerance.
   - *Typical Use Cases*: Core banking transactions, airline flight reservations, government tax databases, credit card processing.
5. **Supercomputers (High-Performance Computing - HPC)**:
   - The fastest, most powerful, and most expensive computers in existence, consisting of thousands or tens of thousands of processors working in parallel.
   - *Performance Metric*: Measured in **FLOPS** (Floating-Point Operations Per Second), currently operating in the Petaflops ($10^{15}$) and Exaflops ($10^{18}$) range.
   - *Use Cases*: Complex scientific simulations: global weather forecasting, climate modeling, nuclear astrophysics, molecular dynamics for drug discovery, advanced cryptography.
6. **Embedded Systems**:
   - Specialized microcontrollers or microprocessors permanently built into a physical device to perform a specific dedicated monitoring or control function.
   - Characterized by real-time operating constraints, minimal user interface, low power consumption, and firmware stored in ROM.
   - *Examples*: Automobile Engine Control Units (ECUs), antilock braking systems (ABS), microwave ovens, washing machines, smart thermostats, digital watches, pacemakers.
