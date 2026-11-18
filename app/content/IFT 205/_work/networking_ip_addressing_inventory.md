# Exhaustive Inventory: Topic 4 — Networking, Topologies & IPv4 Address Classes
*Course: IFT 205 (Introduction to Information Technology) — Nile University of Nigeria*
*Source Materials: Week 6 PDF (Networking, Internet & Digital Communication), Student Notebook (WhatsApp Image 21.46.54, 21.46.55, 21.47.02), Networking RFCs*

---

## 1. Computer Network Foundations
- **Computer Network**: An interconnected group of two or more autonomous computing devices linked via transmission media and communication protocols to exchange data and share hardware/software resources.
- **Protocol**: A formal set of rules, standards, and conventions that govern how devices format, address, transmit, route, receive, and verify data across a network (e.g., HTTP, TCP, IP, DNS).
- **Core Lecturer Exam Highlight**:
  - *"A Local Area Network (LAN) does NOT require an active internet connection to function."*
  - Within a local building or lab, computers connected through a switch can share files, print to networked printers, stream local media, and communicate via intranet without any external ISP or internet connection.
- **Client vs Server Architecture**:
  - *Client*: An end-user device or application program that initiates requests for network resources, files, or services (e.g., web browser, email client).
  - *Server*: A dedicated, high-availability computing system that listens for, processes, and responds to requests from clients (e.g., web server, database server, DNS server, file server).
- **Client-Server vs Peer-to-Peer (P2P)**:
  - *Client-Server*: Centralized management, centralized backups, dedicated server hardware, role-based access control, but server is a single point of failure and costly.
  - *Peer-to-Peer (P2P)*: Every workstation has equal capabilities and can act as both client and server; decentralized, cheap, simple, but lacks centralized security and slows down under scale.

---

## 2. Network Geographies & Topologies
- **Geographic Network Classifications**:
  - *PAN (Personal Area Network)*: Centered around a single individual within ~10 meters (Bluetooth earbuds, smartwatch, smartphone).
  - *LAN (Local Area Network)*: Confined to a discrete geographical area such as a room, office, laboratory, or building. High data transfer rates and low latency.
  - *WLAN (Wireless LAN)*: A LAN utilizing high-frequency radio waves (Wi-Fi, IEEE 802.11) rather than physical cables.
  - *MAN (Metropolitan Area Network)*: Spans a city or municipal district (e.g., municipal fiber loops, cable television distribution).
  - *WAN (Wide Area Network)*: Spans extensive geographical distances (regions, nations, continents); composed of interconnected LANs linked via telecom providers, fiber backbones, and satellite links. The Internet is the premier example.
- **Physical Network Topologies**:
  - *Star Topology*: All nodes connect individually to a central hub or switch. Most common modern LAN topology. Advantage: failure of one cable/device affects only that single node; easy to troubleshoot. Disadvantage: failure of the central switch disables the entire network.
  - *Bus Topology*: All nodes attach to a single common backbone cable terminated with resistors at both ends. Inexpensive, but a break anywhere in the backbone collapses the entire network; high data collisions.
  - *Ring Topology*: Nodes are connected in a closed circular loop. Signals travel sequentially in one direction using token passing. Break in cable halts the ring unless a redundant dual-ring is used.
  - *Mesh Topology*: Every device has dedicated point-to-point links to every other device (Full Mesh: $n(n-1)/2$ physical links). Maximum fault tolerance and redundancy, but prohibitively expensive and complex.
  - *Tree / Hybrid Topology*: Combines characteristics of star and bus layouts (hierarchical branching).

---

## 3. Network Hardware Devices
1. *Network Switch*: Operates at OSI Layer 2 (Data Link). Inspects incoming Ethernet frames, learns hardware MAC addresses, and forwards data strictly to the specific destination port, eliminating packet collisions.
2. *Network Router*: Operates at OSI Layer 3 (Network). Connects two or more disparate networks (e.g. connecting a private home LAN to the public Internet). Reads IP addresses and determines optimal packet routing paths.
3. *Hub*: Layer 1 legacy repeater that blindly broadcasts incoming signals to all ports, creating massive packet collisions.
4. *Modem (Modulator/Demodulator)*: Converts digital computer signals into analog waveforms for transmission over analog telephone/cable lines, and demodulates received analog signals back to digital.
5. *Wireless Access Point (WAP)*: Connects to a wired switch via Ethernet and broadcasts radio signals (Wi-Fi) to allow wireless laptops and phones to join the wired LAN.
6. *Firewall*: Hardware or software barrier monitoring and filtering traffic based on predetermined security access rules.

---

## 4. Network Performance Metrics
- **Bandwidth**: The maximum theoretical data-carrying capacity of a communication channel, measured in bits per second (bps, Mbps, Gbps).
- **Throughput**: The actual measured rate of successful data delivery achieved across a network under real-world conditions (affected by protocol overhead, congestion, signal attenuation, and server load). Always $\le$ Bandwidth.
- **Latency**: The time delay required for a data packet to travel from source to destination across a network path, measured in milliseconds (ms).

---

## 5. IPv4 Address Classes & Addressing (High-Priority Lecturer Note)
- **IPv4 Address Structure**: 32-bit numerical identifier expressed as four 8-bit octets separated by decimal dots (e.g., `192.168.10.15`). Range: `0.0.0.0` to `255.255.255.255`.
- **The Five Classes of IPv4 Addresses**:
  - **Class A**:
    - *First Octet Range*: **1 to 126** (Leading binary bit: `0`).
    - *Default Subnet Mask*: **`255.0.0.0`** (/8 prefix).
    - *Structure*: 8 Network bits, 24 Host bits.
    - *Capacity*: 126 networks, each supporting $2^{24} - 2 = 16,777,214$ usable hosts.
    - *Purpose*: Enormous multinational organizations and global institutions.
    - *Special Note*: Octet **127** (`127.0.0.0/8`) is strictly reserved for internal loopback testing (e.g. `127.0.0.1` localhost) and cannot be assigned to hosts.
  - **Class B**:
    - *First Octet Range*: **128 to 191** (Leading binary bits: `10`).
    - *Default Subnet Mask*: **`255.255.0.0`** (/16 prefix).
    - *Structure*: 16 Network bits, 16 Host bits.
    - *Capacity*: 16,384 networks, each supporting $2^{16} - 2 = 65,534$ usable hosts.
    - *Purpose*: Medium-to-large organizations, universities, and government bodies.
  - **Class C**:
    - *First Octet Range*: **192 to 223** (Leading binary bits: `110`).
    - *Default Subnet Mask*: **`255.255.255.0`** (/24 prefix).
    - *Structure*: 24 Network bits, 8 Host bits.
    - *Capacity*: 2,097,152 networks, each supporting $2^8 - 2 = 254$ usable hosts.
    - *Purpose*: Small businesses, departmental LANs, and residential networks.
  - **Class D**:
    - *First Octet Range*: **224 to 239** (Leading binary bits: `1110`).
    - *Default Subnet Mask*: *None* (no network/host division).
    - *Purpose*: **Multicasting** (transmitting packets to a defined subscriber group).
  - **Class E**:
    - *First Octet Range*: **240 to 255** (Leading binary bits: `1111`).
    - *Purpose*: **Experimental, research, and future allocation**.
- **Private IP Address Ranges (RFC 1918)**:
  - *Class A Private*: `10.0.0.0` to `10.255.255.255` (`10.0.0.0/8`)
  - *Class B Private*: `172.16.0.0` to `172.31.255.255` (`172.16.0.0/12`)
  - *Class C Private*: `192.168.0.0` to `192.168.255.255` (`192.168.0.0/16`)
  *(Private IPs are non-routable on the public Internet and require NAT - Network Address Translation).*

---

## 6. Internet, WWW, ISPs & Domain Name System
- **Internet Service Provider (ISP)**: An organization providing subscriber access to the Internet.
  - *Tier 1 ISPs*: Global backbone operators (AT&T, Lumen, Telia) that own transcontinental fiber and peer freely without transit fees.
  - *Tier 2 ISPs*: Regional networks purchasing transit from Tier 1 while peering with other Tier 2s.
  - *Tier 3 ISPs*: Retail consumer ISPs (e.g. MTN, Airtel, Spectranet in Nigeria) selling end-user access to homes and businesses.
- **Domain Name System (DNS)**: The distributed directory service translating human-friendly names (e.g., `www.nileuniversity.edu.ng`) into machine-routable IP addresses (e.g., `197.210.44.12`).
- **Internet vs World Wide Web**:
  - *Internet*: The global physical and logical networking infrastructure communicating via TCP/IP.
  - *World Wide Web (WWW)*: The information space of hyperlinked hypertext documents and multimedia resources accessed over the Internet via HTTP/HTTPS protocols.
