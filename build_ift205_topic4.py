import json
import os

topic_data = {
    "course": "IFT 205",
    "topic": "networking_ip_addressing",
    "title": "Networking, Topologies & IPv4 Address Classes",
    "summary": "Exhaustive treatment of data communications, network architectures, and IPv4 addressing. Explores core definitions of computer networks, communication protocols, and the fundamental distinction between the Internet (global TCP/IP infrastructure) and the World Wide Web (HTTP/URL hypertext space). Highlights the lecturer's key exam assertion that a Local Area Network (LAN) does NOT require an active internet connection to operate. Compares geographic network scopes (PAN, LAN, WLAN, MAN, WAN) and physical topologies (Star, Bus, Ring, Mesh, Tree). Analyzes network devices including Layer 2 Switches, Layer 3 Routers, Modems, Access Points, and Firewalls. Detailed examination of network performance metrics: Bandwidth, Throughput, and Latency. Thoroughly covers IPv4 Address Classes (A, B, C, D, E) with binary prefixes, octet boundaries, default subnet masks, host formulas (2^h - 2), loopback reservation (127.0.0.0/8), RFC 1918 Private IP blocks, and Internet Service Provider (ISP) tiered hierarchy.",
    "key_terms": [
        {"term": "Computer Network", "definition": "A collection of autonomous computing devices interconnected by communication media and protocols to exchange data and share resources."},
        {"term": "Protocol", "definition": "A formalized set of rules, formats, and procedures that govern how computers exchange data across a network."},
        {"term": "Local Area Network (LAN)", "definition": "A network spanning a restricted geographical area (room, lab, or building) that functions fully for local resource sharing without requiring internet access."},
        {"term": "Network Switch", "definition": "A Layer 2 networking device that forwards data frames selectively to specific destination ports using physical MAC addresses."},
        {"term": "Router", "definition": "A Layer 3 internetworking device that examines logical IP addresses to forward data packets between different networks across optimal paths."},
        {"term": "Class A IP Address", "definition": "An IPv4 address with first octet 1–126 and default subnet mask 255.0.0.0 (/8), supporting up to 16,777,214 hosts per network."},
        {"term": "Class B IP Address", "definition": "An IPv4 address with first octet 128–191 and default subnet mask 255.255.0.0 (/16), supporting up to 65,534 hosts per network."},
        {"term": "Class C IP Address", "definition": "An IPv4 address with first octet 192–223 and default subnet mask 255.255.255.0 (/24), supporting up to 254 hosts per network."}
    ],
    "questions": [
        {
            "id": "ift205-net-001",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "true_false_why",
            "difficulty": 2,
            "tags": ["lan_concepts", "lecturer_hint"],
            "question": "A Local Area Network (LAN) deployed in a university computer laboratory cannot function or allow students to share files and print documents unless there is an active, paid connection to the Internet.",
            "options": [
                "True — modern network interface cards (NICs) automatically disable their physical Ethernet ports if they cannot ping a public Google DNS server.",
                "False — a LAN operates independently at the local link and network layers; devices connected via a switch can communicate, share files, and print locally even when completely isolated from the Internet."
            ],
            "answer": 1,
            "explanation": "As explicitly highlighted by the lecturer in student lecture notes: 'A LAN does not need an active internet connection.' A LAN exists whenever two or more devices are interconnected locally through a switch or access point. Local file sharing, intranet services, database access, and network printing operate completely within the local IP subnet without requiring any WAN/ISP internet connectivity.",
            "why_wrong": {
                "0": "NICs operate based on local electrical carrier detection and Ethernet standards; they do not require public internet connectivity or pinging external DNS to function."
            },
            "marking_points": [],
            "source": "Student Notebook Image 21.47.02 ('LAN Doesn\\'t need internet'); Week 6 Slide 4",
            "verified": True,
            "verified_output": "False. LAN operates without internet."
        },
        {
            "id": "ift205-net-002",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["ip_classes", "class_c"],
            "question": "An IP address begins with the decimal value 197 in its first octet (e.g. 197.210.45.12). To which standard IPv4 address class does this address belong, and what is its default subnet mask?",
            "options": [
                "Class C with default subnet mask 255.255.255.0",
                "Class A with default subnet mask 255.0.0.0",
                "Class B with default subnet mask 255.255.0.0",
                "Class D with default subnet mask 255.255.255.255"
            ],
            "answer": 0,
            "explanation": "IPv4 Class C spans first octet values from 192 to 223. Because 197 falls within 192–223, it is a Class C address. Class C addresses allocate 24 bits to the network ID and 8 bits to the host ID, giving a default subnet mask of 255.255.255.0 (/24).",
            "why_wrong": {
                "1": "Class A covers first octets 1–126 with default mask 255.0.0.0.",
                "2": "Class B covers first octets 128–191 with default mask 255.255.0.0.",
                "3": "Class D covers 224–239 for multicasting and does not have a default host subnet mask."
            },
            "marking_points": [],
            "source": "Student Notebook Image 21.47.02 ('Learn abt IPV4 classes'); Week 6 Slide 12",
            "verified": True,
            "verified_output": "Class C, 255.255.255.0."
        },
        {
            "id": "ift205-net-003",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "matching",
            "difficulty": 3,
            "tags": ["ip_classes", "octet_ranges"],
            "question": "Match each IPv4 Address Class to its defining first-octet decimal range and primary purpose:",
            "options": [
                "Class A",
                "Class B",
                "Class C",
                "Class D",
                "Class E"
            ],
            "answer": {
                "Class A": "First octet: 1 to 126; Default mask 255.0.0.0; Designed for massive networks with millions of hosts.",
                "Class B": "First octet: 128 to 191; Default mask 255.255.0.0; Designed for medium-to-large organizations and universities.",
                "Class C": "First octet: 192 to 223; Default mask 255.255.255.0; Designed for small departmental LANs (up to 254 hosts).",
                "Class D": "First octet: 224 to 239; No subnet mask; Strictly reserved for network Multicasting transmissions.",
                "Class E": "First octet: 240 to 255; No subnet mask; Strictly reserved for experimental and research purposes."
            },
            "explanation": "The standard classful IPv4 allocation defines: Class A (1-126), Class B (128-191), Class C (192-223), Class D (224-239 for multicast), and Class E (240-255 for research). Octet 127 is reserved for loopback testing.",
            "why_wrong": {},
            "marking_points": [],
            "source": "Student Notebook Image 21.47.02; Week 6 Slide 12",
            "verified": True,
            "verified_output": "Matched all 5 IPv4 classes."
        },
        {
            "id": "ift205-net-004",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "type_answer",
            "difficulty": 2,
            "tags": ["ip_addressing", "loopback"],
            "question": "Which specific first-octet number in the IPv4 space (from 1 to 255) is omitted from Class A and reserved globally for internal diagnostic loopback testing (such as 127.0.0.1)?",
            "answer": "127",
            "accepted_answers": ["127", "127.0.0.0", "127.0.0.1"],
            "explanation": "The entire 127.0.0.0/8 address block (first octet 127) is reserved by the Internet Engineering Task Force (IETF) for internal host loopback functions. Packets sent to 127.0.0.1 (localhost) never leave the local machine's TCP/IP stack.",
            "marking_points": [
                "Identifies '127' as the loopback reserved octet."
            ],
            "source": "Week 6 Slide 12; Networking RFC 791",
            "verified": True,
            "verified_output": "127"
        },
        {
            "id": "ift205-net-005",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["network_topologies", "star_topology"],
            "question": "In a university computer laboratory, 30 desktop PCs are connected to a central 48-port Ethernet switch. If the network cable connecting PC #12 is accidentally severed by a student's chair, what is the impact on the rest of the laboratory network?",
            "options": [
                "Only PC #12 loses network connectivity; the remaining 29 computers continue communicating normally through the central switch.",
                "The entire network immediately collapses because the electrical ring loop has been broken.",
                "All 30 computers immediately lose connectivity due to impedance reflection on the backbone cable.",
                "The central switch shuts down permanently and must be factory reformatted."
            ],
            "answer": 0,
            "explanation": "This setup is a Star Topology. In a star network, each host connects via a dedicated point-to-point cable to a central switch. A cable cut affects strictly that individual host. In contrast, in a Bus topology, a severed cable brings down the entire network.",
            "why_wrong": {
                "1": "A ring network collapses on a cable cut, but this laboratory uses a central star switch.",
                "2": "Backbone impedance reflection occurs in Bus networks, not switched star networks.",
                "3": "Switches are designed to isolate link drop events without hardware failure."
            },
            "marking_points": [],
            "source": "Week 6 Slide 4; Networking Theory",
            "verified": True,
            "verified_output": "Only PC #12 loses connection in a Star topology."
        },
        {
            "id": "ift205-net-006",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["network_devices", "switch_vs_router"],
            "question": "What is the primary architectural difference between a Network Switch and a Network Router?",
            "options": [
                "A switch operates at Layer 2 forwarding frames within the same local network using MAC addresses, whereas a router operates at Layer 3 forwarding packets between different networks using IP addresses.",
                "A switch connects computers to the electrical power grid, whereas a router is an analog speaker that generates sound waves.",
                "A switch is strictly used for wireless Wi-Fi signals, whereas a router can only be connected to satellite dishes.",
                "A switch modifies the text of web pages, whereas a router formats the computer's hard disk."
            ],
            "answer": 0,
            "explanation": "A switch connects devices within the same Local Area Network (LAN) and uses Layer 2 Data Link hardware MAC addresses to forward traffic. A router connects two or more different networks together (e.g. connecting a university LAN to an ISP) and uses Layer 3 Network IP addresses to route packets.",
            "why_wrong": {
                "1": "Switches and routers are data communications equipment, not electrical mains or audio speakers.",
                "2": "Switches are predominantly wired Ethernet devices, and routers handle both wired and wireless internetworking.",
                "3": "Network infrastructure devices do not rewrite web page HTML text or format disk partitions."
            },
            "marking_points": [],
            "source": "Week 6 Slide 4, 8; IFT205_Week2 Slide 26",
            "verified": True,
            "verified_output": "Switch operates at L2 (MAC); Router operates at L3 (IP)."
        },
        {
            "id": "ift205-net-007",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "cloze",
            "difficulty": 2,
            "tags": ["performance_metrics"],
            "question": "In computer networking, {{c1::bandwidth}} refers to the maximum theoretical data transmission capacity of a link, whereas {{c2::throughput}} is the actual rate of data successfully transferred under real-world conditions, and {{c3::latency}} measures the time delay required for a packet to travel from sender to destination.",
            "options": ["bandwidth", "throughput", "latency", "frequency", "attenuation", "jitter"],
            "answer": ["bandwidth", "throughput", "latency"],
            "explanation": "Bandwidth is the channel width (e.g. a 1 Gbps fiber link). Throughput is the actual achieved transfer rate (e.g. 650 Mbps after protocol overhead and congestion). Latency is the round-trip propagation delay measured in milliseconds.",
            "why_wrong": {},
            "marking_points": [],
            "source": "Week 6 Slide 10; IFT205_Week2 Slide 30",
            "verified": True,
            "verified_output": "bandwidth, throughput, latency"
        },
        {
            "id": "ift205-net-008",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["ip_classes", "host_capacity"],
            "question": "A standard unsubnetted Class C network uses a default subnet mask of 255.255.255.0. How many valid, usable host IP addresses can be assigned to computers in this network?",
            "options": [
                "254 hosts (because 2^8 = 256 minus network address and broadcast address)",
                "256 hosts (all combinations from 0 to 255)",
                "65,534 hosts (because 2^16 = 65,536 minus 2)",
                "16,777,214 hosts"
            ],
            "answer": 0,
            "explanation": "In Class C, 8 bits are reserved for host IDs ($2^8 = 256$ total bit patterns). However, the formula for usable hosts is always $2^h - 2$, because the first address (all host bits 0, e.g. .0) represents the Network ID, and the last address (all host bits 1, e.g. .255) represents the Directed Broadcast Address. Thus, $256 - 2 = 254$ usable hosts.",
            "why_wrong": {
                "1": "Fails to subtract the two reserved addresses (network ID and broadcast address).",
                "2": "65,534 is the host capacity of a Class B network ($2^{16} - 2$).",
                "3": "16,777,214 is the host capacity of a Class A network ($2^{24} - 2$)."
            },
            "marking_points": [],
            "source": "Student Notebook Image 21.47.02; Networking Standards",
            "verified": True,
            "verified_output": "254 hosts (2^8 - 2)."
        },
        {
            "id": "ift205-net-009",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "multi_select",
            "difficulty": 3,
            "tags": ["private_ip_addresses", "rfc1918"],
            "question": "According to RFC 1918 private networking standards, which of the following IP address blocks are reserved strictly for PRIVATE internal local networks and cannot be routed across the public Internet? (Select THREE)",
            "options": [
                "10.0.0.0 to 10.255.255.255 (Class A Private)",
                "172.16.0.0 to 172.31.255.255 (Class B Private)",
                "192.168.0.0 to 192.168.255.255 (Class C Private)",
                "8.8.8.8 to 8.8.4.4 (Google Public DNS)",
                "197.210.0.0 to 197.210.255.255 (Public Telecom IP Block)"
            ],
            "answer": [0, 1, 2],
            "explanation": "RFC 1918 reserves three private address ranges: 10.0.0.0/8 (Class A), 172.16.0.0/12 (Class B), and 192.168.0.0/16 (Class C). These addresses are non-routable over the public Internet and are used inside homes, enterprises, and university campuses behind NAT routers.",
            "why_wrong": {
                "3": "8.8.8.8 is a globally routable public Anycast IP address owned by Google.",
                "4": "197.210.x.x is a public routable IP block allocated to Nigerian telecommunication providers."
            },
            "marking_points": [],
            "source": "Student Notebook Image 21.47.02; RFC 1918",
            "verified": True,
            "verified_output": "10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16."
        },
        {
            "id": "ift205-net-010",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["isp_hierarchy", "telecom"],
            "question": "What is an Internet Service Provider (ISP), and how does a Tier 1 ISP differ from a Tier 3 retail ISP?",
            "options": [
                "An ISP provides subscriber connectivity to the Internet; Tier 1 ISPs operate transcontinental fiber-optic backbones with settlement-free peering, whereas Tier 3 retail ISPs sell last-mile Internet access directly to consumers.",
                "An ISP is a software program that compiles C programs into machine code.",
                "Tier 1 ISPs only operate inside bank vaults, while Tier 3 ISPs build personal laptops.",
                "An ISP is an electrical power company that generates alternating current."
            ],
            "answer": 0,
            "explanation": "As noted in student notes ('ISP - Internet Service providers'): An ISP provides connectivity to the Internet. Tier 1 providers (e.g. AT&T, Lumen, NTT) form the global backbone and exchange traffic freely without paying transit. Tier 3 retail ISPs (e.g. local consumer providers) purchase bandwidth and resell it to consumers and small businesses.",
            "why_wrong": {
                "1": "Compilers (like GCC) translate C code, not ISPs.",
                "2": "ISPs are telecommunication providers, not bank vaults or PC manufacturers.",
                "3": "Power distribution companies provide electrical energy, not data internet service."
            },
            "marking_points": [],
            "source": "Student Notebook Image 21.47.02; Week 6 Slide 9",
            "verified": True,
            "verified_output": "ISP definition and Tier 1 vs Tier 3 distinction."
        },
        {
            "id": "ift205-net-011",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["dns", "domain_resolution"],
            "question": "When a university student types 'www.nileuniversity.edu.ng' into a browser address bar, which network service translates this human-readable domain name into the destination computer's numerical IP address?",
            "options": [
                "Domain Name System (DNS)",
                "Dynamic Host Configuration Protocol (DHCP)",
                "Simple Mail Transfer Protocol (SMTP)",
                "File Transfer Protocol (FTP)"
            ],
            "answer": 0,
            "explanation": "The Domain Name System (DNS) acts as the phonebook of the Internet, translating human-friendly alphanumeric domain names into machine-routable numerical IP addresses so that browsers can connect to web servers.",
            "why_wrong": {
                "1": "DHCP automatically assigns local IP addresses and subnet masks to connecting devices.",
                "2": "SMTP is used for sending electronic mail.",
                "3": "FTP is used for transferring binary and text files between computers."
            },
            "marking_points": [],
            "source": "Week 6 Slide 12; IFT205_Week2 Slide 29",
            "verified": True,
            "verified_output": "Domain Name System (DNS)."
        },
        {
            "id": "ift205-net-012",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "type_answer",
            "difficulty": 2,
            "tags": ["protocols", "definition"],
            "question": "In computer networking, what is the technical term for the agreed-upon formal 'set of rules' and conventions that determine how computing devices format, transmit, and receive data?",
            "answer": "protocol",
            "accepted_answers": ["protocol", "network protocol", "communication protocol"],
            "explanation": "As defined in the student lecture notes: 'What is a protocol? (It is a set of rules)'. A protocol defines syntax, semantics, synchronization, and error recovery for communications.",
            "marking_points": [
                "Identifies 'protocol' as the set of rules governing network communication."
            ],
            "source": "Student Notebook Image 21.46.54; Week 6 Slide 5",
            "verified": True,
            "verified_output": "protocol"
        },
        {
            "id": "ift205-net-013",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["mesh_topology", "redundancy"],
            "question": "A national military defense command center requires a physical network architecture where every critical server node has a direct, dedicated physical communication link to every other server node, guaranteeing zero single points of failure. Which topology is being described?",
            "options": [
                "Full Mesh Topology",
                "Single Bus Topology",
                "Unidirectional Ring Topology",
                "Daisy-Chain Linear Topology"
            ],
            "answer": 0,
            "explanation": "In a Full Mesh Topology, every device is connected via point-to-point physical links to every other device on the network. This provides the highest fault tolerance and redundant routing paths, though it requires $n(n-1)/2$ cables, making it expensive.",
            "why_wrong": {
                "1": "A Bus topology has a single backbone cable representing a catastrophic single point of failure.",
                "2": "A Ring topology suffers from loop breaks if any single node fails.",
                "3": "Daisy-chaining creates a serial dependency where an intermediate failure disconnects all downstream nodes."
            },
            "marking_points": [],
            "source": "Week 6 Slide 4; Networking Standards",
            "verified": True,
            "verified_output": "Full Mesh Topology."
        },
        {
            "id": "ift205-net-014",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "explain",
            "difficulty": 3,
            "tags": ["internet_vs_www"],
            "question": "Distinguish clearly between 'The Internet' and 'The World Wide Web (WWW)'. Why is it technically inaccurate to use these terms interchangeably?",
            "options": [],
            "answer": "The Internet is the massive, global physical and logical networking infrastructure—the underlying 'hardware and communication highways' consisting of cables, routers, switches, servers, and satellites communicating via the TCP/IP protocol suite. In contrast, the World Wide Web (WWW) is an application service that runs on top of the Internet infrastructure. Invented by Tim Berners-Lee in 1989, the Web is a vast collection of interlinked hypertext documents, multimedia web pages, and web applications identified by URLs and transmitted via HTTP/HTTPS. The Internet supports many other services besides the Web, including email (SMTP/IMAP), file transfer (FTP), remote access (SSH), streaming media, and gaming.",
            "explanation": "Internet is the physical/logical network infrastructure; Web is an information service running on top of it.",
            "why_wrong": {},
            "marking_points": [
                "Defines the Internet as the global physical/logical network infrastructure operating on TCP/IP.",
                "Defines the World Wide Web as an information application service running on the Internet.",
                "Mentions that the Web relies on HTTP/HTTPS, URLs, and HTML documents.",
                "Explicitly notes that other non-web services run on the Internet (e.g. Email, FTP, SSH)."
            ],
            "source": "Week 6 Slide 14; Student Notebook Hint",
            "verified": True,
            "verified_output": "Internet vs World Wide Web distinction."
        },
        {
            "id": "ift205-net-015",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["ip_classes", "multicast_class_d"],
            "question": "A video conferencing application transmits a live university convocation stream to 400 registered students simultaneously using an address beginning with 230.15.4.1. Which IPv4 address class does this belong to?",
            "options": [
                "Class D (Multicast)",
                "Class A (Unicast)",
                "Class B (Directed Broadcast)",
                "Class C (Private Subnet)"
            ],
            "answer": 0,
            "explanation": "Class D addresses cover the range 224.0.0.0 to 239.255.255.255 (first octet 224 to 239). They are strictly reserved for multicast groups, where a single packet sent from a server is delivered simultaneously to multiple subscribed hosts without flooding the entire network.",
            "why_wrong": {
                "1": "Class A covers first octets 1 to 126.",
                "2": "Class B covers first octets 128 to 191.",
                "3": "Class C covers first octets 192 to 223."
            },
            "marking_points": [],
            "source": "Student Notebook Image 21.47.02; Week 6 Slide 12",
            "verified": True,
            "verified_output": "Class D (Multicast)."
        },
        {
            "id": "ift205-net-016",
            "course": "IFT 205",
            "topic": "networking_ip_addressing",
            "type": "true_false_why",
            "difficulty": 2,
            "tags": ["network_geography", "pan_vs_lan"],
            "question": "A Personal Area Network (PAN) typically spans an entire university campus and is linked using underground fiber-optic cables.",
            "options": [
                "True — PANs are designed for campus-wide high-speed computing clusters.",
                "False — a PAN is centered around a single person within a short range of approximately 10 meters (using Bluetooth or USB), whereas a campus-wide network is a Campus Area Network (CAN) or LAN."
            ],
            "answer": 1,
            "explanation": "A Personal Area Network (PAN) covers a very small personal space (typically within 10 meters / 30 feet) connecting personal devices such as smartphones, smartwatches, and wireless earbuds via Bluetooth. A campus network is a LAN or CAN.",
            "why_wrong": {
                "0": "Campuses are served by LANs or CANs using fiber optics, not personal Bluetooth PANs."
            },
            "marking_points": [],
            "source": "Week 6 Slide 5; IFT205_Week2 Slide 25",
            "verified": True,
            "verified_output": "False. PAN is personal ~10m range."
        }
    ],
    "case_studies": [
        {
            "id": "ift205-net-cs1",
            "scenario": "A newly established branch of Nile University in Kaduna sets up an administrative office building with 45 staff desktop computers, 4 networked heavy-duty departmental printers, and a local file server. The IT engineer installs a 48-port Layer 2 managed switch in the server room and runs Cat6 Ethernet cables to each wall jack in a Star topology. Because the external fiber link from the regional ISP (Tier 3) will not be activated for another two weeks, the registrar is furious, believing that staff cannot print student admission letters or share administrative files until the internet connection is connected.",
            "sub_questions": [
                {
                    "id": "ift205-net-cs1-q1",
                    "course": "IFT 205",
                    "topic": "networking_ip_addressing",
                    "type": "explain",
                    "difficulty": 3,
                    "tags": ["case_study", "lan_no_internet"],
                    "question": "Applying the foundational networking concepts emphasized by the lecturer, explain why the registrar's assumption is incorrect, and describe what network services can function immediately in this office.",
                    "options": [],
                    "answer": "The registrar's assumption is factually incorrect because a Local Area Network (LAN) does NOT require an active internet connection to operate. The 45 desktop PCs, 4 printers, and the local file server are physically connected to a local Layer 2 switch in a Star topology. By configuring local private IP addresses (e.g. within a Class C subnet like 192.168.1.0/24), the computers can immediately resolve local addresses, communicate across the switch, transfer files to/from the local file server, and send print jobs to the networked printers over Ethernet without needing external ISP or internet access.",
                    "explanation": "LAN functions independently of the Internet. File sharing and printing are local Layer 2/3 LAN services.",
                    "why_wrong": {},
                    "marking_points": [
                        "Directly articulates the lecturer hint: 'LAN does not require an active internet connection'.",
                        "Explains that the local switch handles frame forwarding within the local subnet via MAC addresses.",
                        "Identifies that local network printing and internal file sharing function seamlessly on an isolated LAN.",
                        "Notes that only external services (browsing external websites, public email) are unavailable until the ISP link goes live."
                    ],
                    "source": "Student Notebook Image 21.47.02; Week 6 Slide 4",
                    "verified": True,
                    "verified_output": "LAN operates file sharing and printing without internet connection."
                },
                {
                    "id": "ift205-net-cs1-q2",
                    "course": "IFT 205",
                    "topic": "networking_ip_addressing",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case_study", "ip_assignment"],
                    "question": "The network engineer decides to configure a static Class C private IP addressing scheme for the 45 computers and 4 printers. Which of the following configurations represents a valid, non-conflicting IP assignment scheme on the same subnet?",
                    "options": [
                        "Network ID: 192.168.10.0; Subnet Mask: 255.255.255.0; Host range: 192.168.10.1 to 192.168.10.50.",
                        "Network ID: 10.0.0.0; Subnet Mask: 255.0.0.0; Assigning all 49 devices the identical IP address 10.0.0.1.",
                        "Network ID: 192.168.10.0; Subnet Mask: 255.255.255.0; Assigning hosts 192.168.10.0 and 192.168.10.255 to the printers.",
                        "Network ID: 224.0.0.1; Subnet Mask: 255.255.255.0; Assigning Class D multicast addresses to each PC."
                    ],
                    "answer": 0,
                    "explanation": "In the Class C private subnet 192.168.10.0/24 with default mask 255.255.255.0, usable host IPs run from 192.168.10.1 to 192.168.10.254. Assigning unique IPs from .1 to .50 provides 50 unique host addresses, perfectly accommodating the 49 devices.",
                    "why_wrong": {
                        "1": "Assigning the identical IP address to multiple devices causes immediate IP address collision errors.",
                        "2": ".0 is the Network ID and .255 is the Broadcast address; neither can be assigned to a host device.",
                        "3": "224.x is Class D multicast, which cannot be assigned as a standard unicast host address."
                    },
                    "marking_points": [],
                    "source": "Student Notebook Image 21.47.02; RFC 1918",
                    "verified": True,
                    "verified_output": "192.168.10.0/24 with unique host IPs .1 to .50."
                }
            ]
        },
        {
            "id": "ift205-net-cs2",
            "scenario": "A financial payment gateway company in Abuja operates an online billing portal. The company purchases a 500 Mbps dedicated fiber internet leased line from a Tier 2 regional telecommunications provider. During normal hours, payment confirmations take 150 milliseconds. However, between 12:00 PM and 2:00 PM on Friday, users experience extreme lag, with payment transactions taking over 12 seconds or timing out entirely. The network engineer conducts an audit and observes: (1) Total traffic bandwidth consumed on the 500 Mbps connection peaked at only 95 Mbps; (2) Latency between the gateway and the clearinghouse bank server spiked from 25 ms to 8,500 ms due to an overloaded intermediary upstream router; (3) The company's staff members were streaming high-definition World Cup football matches on the office Wi-Fi.",
            "sub_questions": [
                {
                    "id": "ift205-net-cs2-q1",
                    "course": "IFT 205",
                    "topic": "networking_ip_addressing",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case_study", "bandwidth_vs_latency"],
                    "question": "Based on the network audit, what was the primary cause of the payment transaction delays between 12:00 PM and 2:00 PM?",
                    "options": [
                        "Severe latency and upstream packet transit delay, rather than local bandwidth saturation (since only 95 Mbps of the 500 Mbps capacity was utilized).",
                        "Total exhaustion of the 500 Mbps local fiber cable bandwidth.",
                        "The payment server's solid-state drive ran out of optical light.",
                        "The DNS server converted all IP addresses to roman numerals."
                    ],
                    "answer": 0,
                    "explanation": "Bandwidth utilization was only 95 Mbps out of 500 Mbps (~19%), proving the local link was not saturated. The failure was caused by extreme Latency (spiking from 25 ms to 8,500 ms) due to bufferbloat/congestion on an upstream bank router, delaying packet delivery.",
                    "why_wrong": {
                        "1": "The audit showed only 95 Mbps of 500 Mbps was consumed, meaning 405 Mbps of bandwidth was still free.",
                        "2": "SSDs use flash memory cells, not optical light beams.",
                        "3": "DNS translates domain names to dotted-decimal 32-bit IP addresses, never roman numerals."
                    },
                    "marking_points": [],
                    "source": "Week 6 Slide 10-11",
                    "verified": True,
                    "verified_output": "High latency rather than bandwidth exhaustion."
                },
                {
                    "id": "ift205-net-cs2-q2",
                    "course": "IFT 205",
                    "topic": "networking_ip_addressing",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case_study", "qos_network_management"],
                    "question": "Propose two specific network management and security policies the company must implement to protect critical payment transactions from staff video streaming interference.",
                    "options": [],
                    "answer": "The company should implement: (1) Quality of Service (QoS) and Traffic Prioritization: Configure the edge router/firewall to classify payment transaction traffic (HTTPS/API calls) as highest priority, reserving guaranteed bandwidth and low latency for financial transactions while assigning video streaming to best-effort lowest priority; (2) Network Segmentation and VLANs: Segregate the network into distinct Virtual LANs (VLANs)—one secure, isolated VLAN for production payment servers and corporate operations, and a separate Guest/Staff Wi-Fi VLAN with bandwidth caps and firewall content filtering that blocks non-work entertainment/video streaming during business hours.",
                    "explanation": "QoS guarantees priority and low latency for critical transactions; VLAN segmentation isolates production traffic from entertainment bandwidth.",
                    "why_wrong": {},
                    "marking_points": [
                        "Recommends Quality of Service (QoS) to prioritize financial API traffic over streaming media.",
                        "Recommends Network Segmentation / VLANs separating payment processing from staff office Wi-Fi.",
                        "Suggests bandwidth throttling or content filtering rules for video streaming during peak business hours.",
                        "Explains how these policies guarantee low latency and prevent transaction timeouts."
                    ],
                    "source": "Week 6 Slide 11, 23",
                    "verified": True,
                    "verified_output": "QoS traffic prioritization and VLAN segmentation."
                }
            ]
        }
    ]
}

out_dir = os.path.join("app", "content", "IFT 205")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "networking_ip_addressing.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(topic_data, f, indent=2)

print(f"Generated {out_path} with {len(topic_data['questions'])} questions and {len(topic_data['case_studies'])} case studies.")
