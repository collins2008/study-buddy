# Exhaustive Inventory: Topic 3 — Operating Systems, System vs Application Software
*Course: IFT 205 (Introduction to Information Technology) — Nile University of Nigeria*
*Source Materials: Software and Operating Systems.pptx (24 slides), Student Notebook (WhatsApp Image 21.46.55 & 21.47.02), Standard Systems Texts*

---

## 1. Software Foundations & Categorisation
- **Software**: A collection of programs, scripts, instructions, and associated documentation that tells hardware how to perform tasks and manage resources.
- **Main Categories of Software**:
  1. *System Software*: Programs that manage and support the computer hardware and provide a foundational platform for running application software.
     - *Operating System (OS)*: The principal system software coordinating hardware, files, and programs.
     - *Device Drivers*: Low-level specialized programs that enable the OS to communicate with specific hardware peripherals (e.g., graphics card driver, printer driver).
     - *Utility Software*: Maintenance, diagnostic, and optimization tools (antivirus, disk defragmenter/cleanup, backup software, file compression utilities).
     - *Firmware*: Low-level permanent software programmed into non-volatile ROM/flash memory chips controlling basic hardware operation (BIOS/UEFI).
  2. *Application Software*: Programs designed to assist human users in performing specific personal, academic, or business tasks.
     - *General-Purpose Applications*: Versatile programs capable of performing a wide variety of tasks (e.g., word processors, spreadsheets, web browsers).
     - *Specialised Applications*: Designed for a specific narrow domain or professional workflow (e.g., CAD software for civil engineers, medical imaging software).
     - *Custom (Bespoke) Software*: Specially commissioned and developed to satisfy the unique requirements of a single organisation (e.g., Nile University's student grading and registration portal).

---

## 2. Operating System Functions & Architecture
- **Five Core Functions of an OS**:
  1. *Process Management*: Controls the execution of programs (processes). Allocates CPU time slices, handles multitasking, manages process states (Ready, Running, Blocked/Waiting), and resolves deadlocks.
  2. *Memory Management*: Allocates and deallocates RAM addresses to active programs; tracks memory usage; implements *Virtual Memory* (paging active memory blocks to secondary storage when physical RAM is exhausted).
  3. *Device (I/O) Management*: Coordinates communication with hardware peripherals via device drivers; manages I/O queues and device interrupts.
  4. *File System Management*: Organises files and directories into a logical hierarchy; tracks disk block allocation, file names, sizes, access permissions, and paths.
  5. *Security & Access Control*: Provides authentication (usernames, passwords, biometrics), establishes authorization permissions (Read, Write, Execute), and protects memory spaces between competing processes.
- **User Interface (UI) Modalities**:
  - *Graphical User Interface (GUI)*: Employs the WIMP paradigm (Windows, Icons, Menus, Pointers). Intuitive, user-friendly, visually rich, but consumes more RAM, GPU, and CPU processing power.
  - *Command Line Interface (CLI)*: Requires users to type textual commands with strict syntax into a prompt or terminal. Fast, extremely low resource footprint, ideal for remote headless servers and batch scripting, but has a steep learning curve.
  - *Touch & Voice Interfaces*: Natural interfaces common on smartphones and smart assistants.

---

## 3. File Systems, Extensions & Paths
- **File System**: The underlying method and data structure that an operating system uses to name, organize, store, and retrieve files on a storage medium (e.g., NTFS in Windows, ext4 in Linux, APFS in macOS, FAT32/exFAT on removable USB drives).
- **Common File Extensions**:
  - Documents: `.docx` (Word), `.pdf` (Portable Document Format), `.xlsx` (Excel), `.txt` (Plain Text), `.csv` (Comma-Separated Values).
  - Media: `.jpg` / `.png` (Images), `.mp3` / `.wav` (Audio), `.mp4` (Video).
  - Web & Executables: `.html`, `.css`, `.js`, `.exe` (Windows Executable), `.sh` (Shell Script).
- **File Paths**:
  - *Absolute Path*: Specifies the complete, unambiguous location from the system root directory or drive letter (e.g., `C:\Users\Student\Documents\assignment.docx` or `/var/log/syslog`).
  - *Relative Path*: Specifies location relative to the current working directory (e.g., `..\images\logo.png`).
- **File Permissions**:
  - *Read (r)*: View file contents or list directory files.
  - *Write (w)*: Modify, overwrite, or delete file contents or add/remove files in a directory.
  - *Execute (x)*: Run a program, binary, or script.

---

## 4. Software Licensing & Integrity
- **Proprietary (Closed-Source)**: Software owned by an individual or corporation; source code is kept secret; users purchase a restricted licence to use the compiled binary without rights to modify, reverse-engineer, or redistribute (e.g., Microsoft Windows, Adobe Photoshop).
- **Open-Source Software (OSS)**: Source code is publicly available under open-source licenses (GPL, MIT, Apache); users are legally permitted to inspect, modify, enhance, and redistribute the code (e.g., Linux, Apache Web Server, Python, LibreOffice).
- **Freeware**: Proprietary software distributed at no monetary cost, but source code is closed and rights to modify or redistribute are withheld (e.g., Adobe Acrobat Reader, Skype).
- **Shareware**: Trial software provided free for an evaluation period, after which payment is required.
- **Risks of Software Piracy (Cracked Software)**:
  - Security compromises: crack tools and keygens frequently contain trojans, spyware, keyloggers, and ransomware.
  - Lack of vendor security updates and bug patches.
  - Legal liability and ethical violations of intellectual property.

---

## 5. OS Installation & Disk Formatting (High-Priority Lecturer Note)
- **Steps to Install a New Operating System**:
  1. *Preparation*: Download official OS ISO image; write to a USB drive using a tool (Rufus/Media Creation Tool) to create bootable media.
  2. *Firmware Configuration*: Insert bootable USB; boot computer; press key (F2, F12, Del) to enter BIOS/UEFI firmware; set boot order to prioritize USB drive.
  3. *Setup Initialization*: Save BIOS changes and boot from USB into OS setup wizard; select language, region, and keyboard layout.
  4. *Disk Partitioning & Formatting*: Select 'Custom/Advanced' installation; review existing storage drives; delete old obsolete partitions or create new partition(s); partition table selection (MBR for legacy BIOS vs GPT for modern UEFI); format designated partition with target file system (e.g., NTFS for Windows, ext4 for Linux).
  5. *File Copy & Extraction*: The installer copies setup files, expands system archives, installs OS features and drivers, and reboots.
  6. *Out-of-Box Experience (OOBE)*: Create administrative user account, configure passwords/PINs, privacy settings, and connect to network; install chipset/hardware drivers and system updates.
- **Formatting a Storage Drive**:
  - *Definition*: The process of preparing a data storage device (HDD, SSD, USB drive) for initial use by writing a file system structure (Master File Table / File Allocation Table, boot sector, cluster geometry) onto the partition.
  - *Quick Format*: Overwrites the file system indexing tables (MFT/FAT), making the disk appear empty and reallocating sectors, but leaves underlying data intact until overwritten. Does not scan for bad sectors.
  - *Full Format*: Overwrites file system tables AND thoroughly scans the entire disk surface sector-by-sector for physical defects/bad blocks, zero-filling sectors.
