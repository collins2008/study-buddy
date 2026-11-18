# Topic Inventory: IFT 203 Topic 1 — Internet, WWW, Protocols & Client-Server
**Topic Slug**: `internet_web_architecture`
**Source Materials**:
- IFT 203 Slide 2: "Basic Terminologies, Abbreviations & Meanings" (Lecturer: Zakariyya Abdullahi Adamu)
- Lecturer Notebook Hints (Internet vs WWW, Browser vs Search Engine, Webpage vs Website vs Web App, URL, DNS, TCP)
- W3C & IETF Web Architecture Standards

---

## 1. Exhaustive Concept Inventory

### A. The Internet vs The World Wide Web (WWW)
- **The Internet**: The global physical network of billions of interconnected computers, routers, fiber-optic cables, and wireless links communicating via the standardized TCP/IP protocol suite. Began as ARPANET (1969).
- **The World Wide Web (WWW / W3)**: An information space and service operating on top of the Internet, comprising interlinked hypertext documents and multimedia resources accessible via Uniform Resource Locators (URLs) and transferred via HTTP/HTTPS. Invented by Sir Tim Berners-Lee at CERN in 1989.
- **Analogy**: The Internet is the highway infrastructure; the Web consists of the vehicles traveling on it.

### B. Core Web Distinctions & Terminologies
1. **Webpage**: A single electronic document written in HTML, typically styled with CSS and enhanced with JavaScript, identified by a distinct URL.
2. **Website**: A structured collection of related, interlinked webpages stored on a web server under a unified domain name (e.g., `www.nileuniversity.edu.ng`).
3. **Web Application**: An interactive software program hosted on a web server that executes complex business logic, processes user input, and dynamically interacts with databases (e.g., Nile Student Portal, Google Docs, Banking apps).
4. **Web Browser vs Search Engine (Crucial Exam Hint)**:
   - *Web Browser*: Client software installed locally on an end-user device (e.g., Google Chrome, Mozilla Firefox, Apple Safari, Microsoft Edge) whose primary function is to fetch HTML/CSS/JS files from servers, parse markup, and render graphical pages.
   - *Search Engine*: A web service accessible via a browser (e.g., Google, Bing, DuckDuckGo) that employs automated crawlers/spiders to index the web and return relevant URL results based on keyword search queries.
5. **Front-End (Client-Side) vs Back-End (Server-Side)**:
   - *Front-End*: Everything executing in the user's browser; responsible for visual presentation, layout, and immediate user interactions (HTML, CSS, JavaScript).
   - *Back-End*: Everything executing on the remote web server; responsible for data persistence, database transactions, authentication, and API endpoints (PHP, Node.js, Python, Java, SQL).

### C. Client-Server Architecture & The HTTP Request-Response Cycle
1. **Client (User Agent)**: Initiates communication by sending an HTTP request.
2. **Server**: Listens on a network port (port 80 for HTTP, port 443 for HTTPS), receives requests, processes data, and returns an HTTP response.
3. **The 6-Step Web Page Lifecycle**:
   - Step 1: User types URL into browser address bar.
   - Step 2: Browser queries DNS cache/servers to resolve domain name into target server IP address.
   - Step 3: Browser establishes a TCP connection with the server (TCP 3-way handshake: SYN $\to$ SYN-ACK $\to$ ACK) and negotiates TLS encryption if HTTPS.
   - Step 4: Browser transmits an HTTP Request (e.g., `GET /index.html HTTP/1.1`).
   - Step 5: Web server parses request, fetches/generates file, and returns HTTP Response with status code (e.g., `200 OK`) and payload.
   - Step 6: Browser parses HTML, builds DOM tree, requests referenced resources (CSS, JS, images), and renders visual page.

### D. Protocols & Web Addressing (URLs & DNS)
1. **HTTP vs HTTPS**:
   - HTTP: Unencrypted plain-text transmission over TCP port 80.
   - HTTPS: Encrypted via TLS/SSL (Transport Layer Security) over TCP port 443, ensuring confidentiality, integrity, and server authentication.
2. **TCP/IP Protocol Suite**:
   - IP (Internet Protocol): Responsible for addressing and routing packets between source and destination IP addresses.
   - TCP (Transmission Control Protocol): Connection-oriented protocol providing reliable, ordered, error-checked delivery of packet streams.
3. **DNS (Domain Name System)**:
   - Distributed hierarchical database translating alphanumeric domain names (e.g., `nileuniversity.edu.ng`) into binary/dotted-decimal IP addresses (e.g., `104.21.54.212`).
4. **Anatomy of a Uniform Resource Locator (URL)**:
   - `https://portal.nileuniversity.edu.ng:443/admissions/register?session=2026#step2`
   - *Protocol/Scheme*: `https://`
   - *Subdomain*: `portal.`
   - *Second-level Domain*: `nileuniversity`
   - *Top-Level Domain (TLD) / ccTLD*: `.edu.ng`
   - *Port*: `:443` (default for HTTPS)
   - *Path*: `/admissions/register`
   - *Query String*: `?session=2026` (key-value parameters)
   - *Fragment Identifier / Anchor*: `#step2` (in-page element ID)

### E. Static vs Dynamic Web Pages
- **Static Pages**: Pre-written files stored on the server disk; sent unchanged to all visitors; fast and simple but inflexible.
- **Dynamic Pages**: Generated on-the-fly at runtime by server-side scripts pulling data from databases; customized per user, session, or request.
