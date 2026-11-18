import json
import os

topic_data = {
    "course": "IFT 203",
    "topic": "Web Hosting, HTTP Status Codes & Best Practices",
    "summary": "This topic synthesizes deployment infrastructure, protocol diagnostics, web security, and performance engineering. Web servers combine specialized hardware with daemon software (Apache, Nginx, Node.js) listening on network ports 80/443. Hosting architectures range from cost-effective Shared Hosting to isolated Virtual Private Servers (VPS), Dedicated bare-metal servers, and elastic Cloud/CDN edge networks. HTTP response status codes provide standardized diagnostics categorized into 1xx (Informational), 2xx (Success, e.g., 200 OK, 201 Created), 3xx (Redirection, e.g., 301 Permanent vs 302 Temporary), 4xx (Client Errors, e.g., 400 Bad Request, 401 Unauthorized vs 403 Forbidden, 404 Not Found), and 5xx (Server Errors, e.g., 500 Internal Error, 502 Bad Gateway, 504 Gateway Timeout). Web security is governed by HTTPS/TLS cryptographic handshakes, the browser's Same-Origin Policy (SOP), Cross-Origin Resource Sharing (CORS), and hardened cookie flags (`HttpOnly`, `Secure`, `SameSite`). Finally, production performance optimization incorporates asset minification, Gzip/Brotli compression, HTTP caching headers, and lazy image loading.",
    "key_terms": [
        {
            "term": "HTTP Status Code",
            "definition": "A 3-digit standardized integer returned by a web server indicating the outcome of a client's HTTP request, categorized into 1xx, 2xx, 3xx, 4xx, and 5xx classes."
        },
        {
            "term": "401 vs 403",
            "definition": "'401 Unauthorized' means the client is unauthenticated and must log in; '403 Forbidden' means the client's identity is authenticated, but they lack permission to access the resource."
        },
        {
            "term": "502 vs 504",
            "definition": "'502 Bad Gateway' means a proxy or load balancer received an invalid response from an upstream backend server; '504 Gateway Timeout' means the upstream server took too long to reply before the proxy timed out."
        },
        {
            "term": "Same-Origin Policy (SOP)",
            "definition": "A foundational browser security mechanism that restricts a script loaded from one origin (protocol + host + port) from reading or interacting with resources from a different origin."
        },
        {
            "term": "CORS (Cross-Origin Resource Sharing)",
            "definition": "An HTTP-header-based mechanism that allows a server to explicitly indicate any origins other than its own from which a browser should permit loading resources."
        },
        {
            "term": "HttpOnly Cookie",
            "definition": "A security flag on a Set-Cookie header preventing client-side JavaScript (e.g., document.cookie) from accessing the cookie, immunizing it from Cross-Site Scripting (XSS) theft."
        },
        {
            "term": "Content Delivery Network (CDN)",
            "definition": "A geographically distributed network of proxy edge servers that cache static web assets (images, CSS, JS) close to end-users to reduce latency and server load."
        },
        {
            "term": "Asset Minification",
            "definition": "The process of removing unnecessary characters (whitespace, comments, newlines, shortening variable names) from source code files without altering functionality, reducing download file size."
        }
    ],
    "questions": [
        {
            "id": "ift203-ws-001",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["http-status-codes", "diagnostics", "client-errors"],
            "question": "A student attempts to access the Nile University lecturer grading portal. The student logs in successfully with valid student credentials, but the server returns an HTTP error page displaying `403 Forbidden`. Why did this happen, and how does it differ from a `401 Unauthorized` error?",
            "options": [
                "`403 Forbidden` means the server has crashed and needs to be formatted",
                "`403 Forbidden` means the server recognized the student's authenticated identity, but refuses authorization because students lack permission to access the grading module; `401 Unauthorized` occurs when the user is not authenticated at all (missing or invalid credentials)",
                "`403 Forbidden` means the requested URL has been permanently deleted from the web",
                "`401` and `403` are identical numbers with no difference in HTTP standards"
            ],
            "answer": 1,
            "explanation": "This is a quintessential web engineering distinction. `401 Unauthorized` means authentication is missing or failed (the client must supply valid credentials). `403 Forbidden` means the client IS successfully authenticated, but the authorization layer refuses access because the user's role/permissions do not permit accessing that resource (e.g., a student trying to edit exam grades).",
            "why_wrong": {
                "0": "Server crashes produce 5xx errors (e.g., `500 Internal Server Error`), not 4xx client errors.",
                "2": "Deleted URLs return `404 Not Found` or `410 Gone`.",
                "3": "Every HTTP status code has a strictly defined, distinct semantic meaning under RFC 9110."
            },
            "source": "RFC 9110 HTTP Semantics; IFT 203 Web Servers Lecture Notes"
        },
        {
            "id": "ift203-ws-002",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "mcq",
            "difficulty": 2,
            "tags": ["web-hosting", "servers", "infrastructure"],
            "question": "An IT department is deciding on web hosting for a new low-budget student club portfolio that receives fewer than 50 visitors a month. Which hosting tier is most cost-effective and appropriate?",
            "options": [
                "A multi-million dollar private mainframe data center",
                "Shared Web Hosting, where multiple small websites share the physical CPU, RAM, and web server software of a single hosting machine",
                "A dedicated high-availability Kubernetes cluster spanning three cloud regions",
                "Purchasing an undersea fiber-optic cable"
            ],
            "answer": 1,
            "explanation": "Shared web hosting is the most economical solution for small, low-traffic static websites. Multiple websites share server resources (OS, web server, hardware) managed by the hosting provider at minimal monthly cost. Dedicated servers and multi-region Kubernetes clusters represent massive, unjustifiable financial and operational overhead for a small club portfolio.",
            "why_wrong": {
                "0": "Mainframe data centers cost hundreds of thousands of dollars and are designed for high-throughput banking ledgers.",
                "2": "Multi-region Kubernetes clusters are designed for high-scale enterprise cloud applications.",
                "3": "Fiber-optic cables are international telecommunications infrastructure, not a website hosting option."
            },
            "source": "IFT 203 Syllabus; Web Hosting Principles"
        },
        {
            "id": "ift203-ws-003",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["http-redirects", "seo", "status-codes"],
            "question": "A university relocates its official admissions page permanently from `nileuniversity.edu.ng/admit` to `nileuniversity.edu.ng/admissions`. Which HTTP status code should the web server return to redirect incoming traffic while transferring search engine ranking authority (SEO link equity)?",
            "options": [
                "`302 Found` (Temporary Redirect)",
                "`301 Moved Permanently`",
                "`404 Not Found`",
                "`500 Internal Server Error`"
            ],
            "answer": 1,
            "explanation": "`301 Moved Permanently` informs web browsers and search engine crawlers that the requested URL has permanently migrated to a new location. Search engines update their indices to index the new URL and pass along all accumulated SEO ranking signals and backlinks. `302 Found` indicates only a temporary detour, so search engines retain the old URL in their index.",
            "why_wrong": {
                "0": "`302 Found` is for temporary redirects and does not transfer long-term search engine ranking equity.",
                "2": "`404 Not Found` drops the page from search engine indexes and breaks user links.",
                "3": "`500 Internal Server Error` indicates a crash and severely penalizes search rankings."
            },
            "source": "RFC 9110 HTTP Semantics; Google Search Central Redirection Guidelines"
        },
        {
            "id": "ift203-ws-004",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["server-errors", "reverse-proxy", "status-codes"],
            "question": "In a modern web architecture, an Nginx reverse proxy forwards incoming student requests to an internal Node.js application server. During peak exam registration, student browsers receive an HTTP `504 Gateway Timeout` error. What is the root cause of this error?",
            "options": [
                "The student entered an invalid email syntax in a form input",
                "The Nginx reverse proxy server contacted the upstream Node.js application server, but the Node.js server took too long to complete its work and failed to reply before the proxy's timeout threshold expired",
                "The student's computer has run out of hard drive space",
                "The Nginx proxy was deleted from the Internet"
            ],
            "answer": 1,
            "explanation": "A `504 Gateway Timeout` occurs in multi-tier server architectures when an intermediary proxy or gateway (e.g., Nginx, Cloudflare, AWS ALB) successfully sends a request to an upstream application server or database, but does not receive a timely response before its pre-configured read-timeout limit expires (often caused by database deadlock or heavy query load).",
            "why_wrong": {
                "0": "Invalid form input causes a client error, returning `400 Bad Request`, not `504 Gateway Timeout`.",
                "2": "Client hard drive space does not cause upstream server proxy timeouts.",
                "3": "If Nginx was gone, the browser would report connection refused, not receive an HTTP 504 response generated by Nginx."
            },
            "source": "RFC 9110 HTTP Semantics; Nginx Reverse Proxy Documentation"
        },
        {
            "id": "ift203-ws-005",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "matching",
            "difficulty": 3,
            "tags": ["http-codes", "matching", "diagnostics"],
            "question": "Match each HTTP status code to its exact category and standard operational trigger:",
            "options": [
                {"left": "200 OK", "right": "Standard successful HTTP response containing requested resource payload"},
                {"left": "301 Moved Permanently", "right": "Permanent redirection signaling browsers and search crawlers to update bookmarks and indices"},
                {"left": "400 Bad Request", "right": "Client error indicating the server cannot process the request due to malformed syntax"},
                {"left": "403 Forbidden", "right": "Client error where server recognizes authenticated identity but refuses permission"},
                {"left": "503 Service Unavailable", "right": "Server error indicating the server is currently unable to handle request due to overload or maintenance"}
            ],
            "answer": [
                {"left": "200 OK", "right": "Standard successful HTTP response containing requested resource payload"},
                {"left": "301 Moved Permanently", "right": "Permanent redirection signaling browsers and search crawlers to update bookmarks and indices"},
                {"left": "400 Bad Request", "right": "Client error indicating the server cannot process the request due to malformed syntax"},
                {"left": "403 Forbidden", "right": "Client error where server recognizes authenticated identity but refuses permission"},
                {"left": "503 Service Unavailable", "right": "Server error indicating the server is currently unable to handle request due to overload or maintenance"}
            ],
            "explanation": "Mastery of standard HTTP status codes is an indispensable diagnostic skill for university examinations and full-stack engineering.",
            "why_wrong": {},
            "source": "RFC 9110 HTTP Semantics"
        },
        {
            "id": "ift203-ws-006",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "sequencing",
            "difficulty": 2,
            "tags": ["tls-handshake", "https", "security", "sequencing"],
            "question": "Arrange the simplified stages of an HTTPS (TLS) Handshake in the correct chronological sequence:",
            "options": [
                "Client Hello: Browser sends supported TLS versions and cryptographic cipher suites to the server",
                "Server Hello & Certificate: Server replies with chosen cipher suite and presents its digital SSL/TLS Certificate signed by a trusted CA",
                "Certificate Verification: Browser verifies the digital signature of the certificate against its pre-installed list of trusted Certificate Authorities",
                "Session Key Exchange: Client and server exchange/derive symmetric encryption session keys using asymmetric cryptography",
                "Encrypted Session: Secure, symmetric-encrypted HTTP communication begins over port 443"
            ],
            "answer": [
                "Client Hello: Browser sends supported TLS versions and cryptographic cipher suites to the server",
                "Server Hello & Certificate: Server replies with chosen cipher suite and presents its digital SSL/TLS Certificate signed by a trusted CA",
                "Certificate Verification: Browser verifies the digital signature of the certificate against its pre-installed list of trusted Certificate Authorities",
                "Session Key Exchange: Client and server exchange/derive symmetric encryption session keys using asymmetric cryptography",
                "Encrypted Session: Secure, symmetric-encrypted HTTP communication begins over port 443"
            ],
            "explanation": "The TLS handshake negotiates encryption ciphers, verifies server identity through CA-signed certificates, securely exchanges a symmetric session key, and transitions to encrypted communication.",
            "why_wrong": {},
            "source": "RFC 8446 The Transport Layer Security (TLS) Protocol Version 1.3"
        },
        {
            "id": "ift203-ws-007",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "mcq",
            "difficulty": 3,
            "tags": ["same-origin-policy", "sop", "security"],
            "question": "Under the browser's fundamental Same-Origin Policy (SOP), which of the following URLs shares the EXACT SAME ORIGIN as `https://portal.nileuniversity.edu.ng:443/students`?",
            "options": [
                "`http://portal.nileuniversity.edu.ng:443/students` (different protocol)",
                "`https://portal.nileuniversity.edu.ng:443/lecturers/grades` (identical protocol, domain, and port)",
                "`https://api.nileuniversity.edu.ng:443/students` (different subdomain/host)",
                "`https://portal.nileuniversity.edu.ng:8080/students` (different port)"
            ],
            "answer": 1,
            "explanation": "The Same-Origin Policy dictates that two URLs have the same origin if and only if their Protocol, Host/Domain, and Port match EXACTLY. `https://portal.nileuniversity.edu.ng:443/lecturers/grades` shares `https`, `portal.nileuniversity.edu.ng`, and `443`; only the path differs, so they share the exact same origin.",
            "why_wrong": {
                "0": "`http` differs from `https` (protocol mismatch).",
                "2": "`api.` differs from `portal.` (subdomain/host mismatch).",
                "3": "Port `8080` differs from port `443` (port mismatch)."
            },
            "source": "MDN Same-Origin Policy; Web Security Standards"
        },
        {
            "id": "ift203-ws-008",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "multi_select",
            "difficulty": 3,
            "tags": ["best-practices", "security", "performance"],
            "question": "Which of the following represent established production best practices for web performance and application security? (Select ALL that apply)",
            "options": [
                "Setting the `HttpOnly` flag on sensitive authentication session cookies so malicious client-side JavaScript injected via XSS cannot access them",
                "Enabling Gzip or Brotli compression on the web server to drastically compress HTML, CSS, and JavaScript text files over the network",
                "Minifying production CSS and JavaScript files to eliminate whitespace, comments, and reduce payload transfer sizes",
                "Storing plain-text database root passwords inside a public HTML comment `<!-- db_pass=secret -->`"
            ],
            "answer": [0, 1, 2],
            "explanation": "Options 0, 1, and 2 are pillars of web engineering: `HttpOnly` cookies mitigate session hijacking, text compression (Gzip/Brotli) cuts bandwidth by up to 70%, and minification speeds up DOM parsing. Option 3 is a catastrophic security disaster; HTML comments are delivered to all users and easily inspected via View Source.",
            "why_wrong": {
                "3": "Writing passwords in HTML comments exposes critical credentials to the entire public Internet."
            },
            "source": "OWASP Security Guidelines; Google Web Fundamentals Performance"
        },
        {
            "id": "ift203-ws-fc01",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "web-server"],
            "question": "What is a Web Server? Distinguish between its hardware and software definitions.",
            "answer": "Hardware: A physical or virtual computer connected to the Internet with a public IP.\nSoftware: A daemon program (e.g., Apache, Nginx, IIS) that listens on port 80/443, processes HTTP requests, and serves files or routes requests.",
            "explanation": "Foundational web architecture definition.",
            "why_wrong": {},
            "source": "IFT 203 Web Servers Lecture"
        },
        {
            "id": "ift203-ws-fc02",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "401-vs-403"],
            "question": "Explain the difference between HTTP `401 Unauthorized` and `403 Forbidden`.",
            "answer": "- 401 Unauthorized: The user is unauthenticated (missing or invalid login credentials).\n- 403 Forbidden: The user's identity is authenticated, but they lack permission/authorization to access the resource.",
            "explanation": "Standard security error distinction.",
            "why_wrong": {},
            "source": "RFC 9110 HTTP Semantics"
        },
        {
            "id": "ift203-ws-fc03",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "301-vs-302"],
            "question": "What is the difference between a `301` and a `302` HTTP redirect?",
            "answer": "- 301 Moved Permanently: The URL migration is permanent. Browsers cache the redirect and search engines transfer SEO ranking equity.\n- 302 Found: The redirection is temporary. Search engines retain the original URL in their index.",
            "explanation": "Crucial distinction for SEO and URL routing.",
            "why_wrong": {},
            "source": "RFC 9110"
        },
        {
            "id": "ift203-ws-fc04",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "502-vs-504"],
            "question": "Compare HTTP `502 Bad Gateway` with `504 Gateway Timeout`.",
            "answer": "- 502 Bad Gateway: A proxy or gateway received an invalid or corrupt response from an upstream server.\n- 504 Gateway Timeout: The upstream server failed to respond within the gateway's timeout window.",
            "explanation": "Standard reverse proxy diagnostic codes.",
            "why_wrong": {},
            "source": "RFC 9110"
        },
        {
            "id": "ift203-ws-fc05",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "same-origin-policy"],
            "question": "What is the Same-Origin Policy (SOP)?",
            "answer": "A core browser security policy restricting client-side scripts running on one origin from accessing or reading DOM content, cookies, or data from another origin (where Origin = Protocol + Host + Port).",
            "explanation": "Prevents malicious websites from reading private data from bank accounts.",
            "why_wrong": {},
            "source": "MDN Same-Origin Policy"
        },
        {
            "id": "ift203-ws-fc06",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "cors"],
            "question": "What is CORS (Cross-Origin Resource Sharing)?",
            "answer": "An HTTP header mechanism allowing servers to relax the Same-Origin Policy and explicitly tell browsers which external domains (e.g., `Access-Control-Allow-Origin: *`) are permitted to access their API endpoints.",
            "explanation": "Essential for modern frontend SPA and microservice communication.",
            "why_wrong": {},
            "source": "MDN CORS"
        },
        {
            "id": "ift203-ws-fc07",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "httponly-cookie"],
            "question": "What does the `HttpOnly` cookie flag do?",
            "answer": "It blocks client-side JavaScript (`document.cookie`) from reading or modifying the cookie, protecting session authentication tokens from theft via Cross-Site Scripting (XSS) attacks.",
            "explanation": "Mandatory cookie security flag.",
            "why_wrong": {},
            "source": "OWASP Cookie Security"
        },
        {
            "id": "ift203-ws-fc08",
            "course": "IFT 203",
            "topic": "Web Hosting, HTTP Status Codes & Best Practices",
            "type": "flashcard",
            "difficulty": 1,
            "tags": ["flashcard", "minification"],
            "question": "What is code minification, and why is it used?",
            "answer": "The automated process of removing all unnecessary whitespace, line breaks, comments, and shortening variable names in HTML/CSS/JS files without changing functionality, drastically reducing payload sizes.",
            "explanation": "Standard production build step.",
            "why_wrong": {},
            "source": "Google Web Performance"
        }
    ],
    "case_studies": [
        {
            "id": "ift203-ws-cs01",
            "scenario": "During the first hour of Nile University course registration, 8,000 students log into `portal.nileuniversity.edu.ng`. The portal architecture features an Nginx reverse proxy routing traffic to an internal Node.js/PHP backend connected to a MySQL database. Within 15 minutes, student browsers start failing with `504 Gateway Timeout` and `502 Bad Gateway` errors. Nginx server logs show that Nginx is running normally, but the upstream application processes are pinned at 100% CPU and database connection pools are exhausted.",
            "sub_questions": [
                {
                    "id": "ift203-ws-cs01-q1",
                    "course": "IFT 203",
                    "topic": "Web Hosting, HTTP Status Codes & Best Practices",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case-study", "504-timeout", "proxy-architecture"],
                    "question": "Why did Nginx return `504 Gateway Timeout` instead of `404 Not Found` or `200 OK`?",
                    "options": [
                        "Because the portal files were deleted from the server hard drive",
                        "Because Nginx successfully forwarded student registration requests to the upstream application servers, but the application servers became backlogged in database queries and failed to reply within Nginx's proxy read timeout threshold",
                        "Because students typed the URL wrong on their phones",
                        "Because the student registration fee was unpaid"
                    ],
                    "answer": 1,
                    "explanation": "`504 Gateway Timeout` is a server error generated by a reverse proxy (Nginx) when the upstream backend cluster becomes completely unresponsive under load and fails to return an HTTP response before the timeout expires. `404` indicates a missing URL, and `200` indicates success.",
                    "why_wrong": {
                        "0": "If files were deleted, the server would return `404 Not Found`.",
                        "2": "Client URL syntax errors produce 4xx errors, not 504 proxy timeouts.",
                        "3": "Billing status is business logic handled inside application code, not proxy gateway timeouts."
                    },
                    "source": "RFC 9110; Nginx High Concurrency Diagnostics"
                },
                {
                    "id": "ift203-ws-cs01-q2",
                    "course": "IFT 203",
                    "topic": "Web Hosting, HTTP Status Codes & Best Practices",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case-study", "system-scaling", "caching-architecture"],
                    "question": "Propose an architectural remediation strategy to eliminate `504 Gateway Timeout` errors and scale the registration portal for 20,000 concurrent students without database crashes.",
                    "marking_points": [
                        "Static asset offloading: Configure Nginx or a CDN (Cloudflare) to serve all static CSS, JS, and image files directly with long cache headers, preventing static asset requests from touching application servers.",
                        "Application horizontal scaling & load balancing: Run multiple instances of the Node.js/PHP backend across multiple cores/servers behind Nginx using round-robin or least-connections load balancing.",
                        "Database connection pooling & Redis caching: Implement database connection pools (e.g., pooling max 100 connections) and cache read-heavy course catalogs in an in-memory Redis cache.",
                        "Asynchronous queuing: Place write-heavy course registration seat claims onto an asynchronous message queue (e.g., RabbitMQ or Redis Streams) with rate-limiting to smooth peak database load."
                    ],
                    "answer": "1. Static Asset CDN Offloading:\nConfigure Nginx and a CDN (e.g., Cloudflare) to intercept and serve all static CSS, JavaScript, fonts, and images directly with `Cache-Control: public, max-age=31536000`. This instantly relieves 80% of total HTTP requests from reaching backend application processes.\n\n2. Horizontal Application Load Balancing:\nScale the backend into multiple clustered Node.js/PHP processes (e.g., via PM2 or containerized Docker pods) balanced by Nginx using `least_conn` routing, distributing computational load across all available CPU cores.\n\n3. Database Connection Pooling & In-Memory Caching:\n- Implement strict database connection pooling to prevent thousands of simultaneous TCP database connections from exhausting server memory.\n- Cache read-heavy data (e.g., available courses, lecturer names, timetable schedules) inside an in-memory Redis store, transforming costly multi-table SQL queries into sub-millisecond key lookups.\n\n4. Asynchronous Queue Processing:\nFor course registration enrollments, utilize an asynchronous queue (e.g., Redis Streams/RabbitMQ) to buffer concurrent enrollments, ensuring transactional consistency and preventing database locks from timing out HTTP proxy requests.",
                    "explanation": "Combining CDN caching, horizontal process load balancing, Redis caching, and connection pooling permanently resolves gateway timeout bottlenecks.",
                    "why_wrong": {},
                    "source": "Nginx Scaling Best Practices; Web Systems Architecture"
                }
            ]
        },
        {
            "id": "ift203-ws-cs02",
            "scenario": "A student builds a single-page web application hosted on GitHub Pages at `https://student.github.io/portal`. The frontend uses JavaScript `fetch('https://api.nileuniversity.edu.ng/courses')` to load course data. In Chrome DevTools, the fetch call fails with the error:\n`Access to fetch at 'https://api.nileuniversity.edu.ng/courses' from origin 'https://student.github.io' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.`",
            "sub_questions": [
                {
                    "id": "ift203-ws-cs02-q1",
                    "course": "IFT 203",
                    "topic": "Web Hosting, HTTP Status Codes & Best Practices",
                    "type": "mcq",
                    "difficulty": 3,
                    "tags": ["case-study", "cors", "same-origin-policy"],
                    "question": "Why did the browser block the student's JavaScript fetch request, and on which server must the fix be implemented?",
                    "options": [
                        "The browser blocked it because GitHub Pages is illegal in Nigeria; the fix is to use Firefox",
                        "The browser's Same-Origin Policy blocked the response because `https://student.github.io` and `https://api.nileuniversity.edu.ng` are different origins. The fix MUST be implemented on the API server (`api.nileuniversity.edu.ng`) by adding the HTTP response header `Access-Control-Allow-Origin`",
                        "The fix must be implemented by purchasing a new domain name from GitHub",
                        "The browser blocked it because the student forgot to add a CSS stylesheet"
                    ],
                    "answer": 1,
                    "explanation": "Under the Same-Origin Policy, browsers prohibit client-side JavaScript from reading responses from a different origin unless the target server explicitly grants permission via Cross-Origin Resource Sharing (CORS) headers. Because `student.github.io` is a different domain from `api.nileuniversity.edu.ng`, the API server must send the response header `Access-Control-Allow-Origin: https://student.github.io` (or `*`). This CANNOT be fixed in client-side JavaScript.",
                    "why_wrong": {
                        "0": "GitHub Pages is globally supported; switching browsers does not bypass W3C CORS security.",
                        "2": "Purchasing new domains does not eliminate cross-origin requirements.",
                        "3": "CSS stylesheets have zero relation to network CORS security policies."
                    },
                    "source": "MDN CORS Guide; W3C Fetch Specification"
                },
                {
                    "id": "ift203-ws-cs02-q2",
                    "course": "IFT 203",
                    "topic": "Web Hosting, HTTP Status Codes & Best Practices",
                    "type": "explain",
                    "difficulty": 4,
                    "tags": ["case-study", "cors-headers", "cookie-security"],
                    "question": "Specify the exact HTTP response headers the Nile API server must send to authorize cross-origin requests, and configure secure session cookie flags (`HttpOnly`, `Secure`, `SameSite`) to protect user authentication.",
                    "marking_points": [
                        "CORS Header 1: `Access-Control-Allow-Origin: https://student.github.io` (or configured origin).",
                        "CORS Header 2: `Access-Control-Allow-Methods: GET, POST, OPTIONS`.",
                        "CORS Header 3: `Access-Control-Allow-Headers: Content-Type, Authorization`.",
                        "CORS Header 4: `Access-Control-Allow-Credentials: true` if credentials/cookies are included.",
                        "Cookie configuration: `Set-Cookie: session_id=xyz123; HttpOnly; Secure; SameSite=Strict; Path=/`.",
                        "Explains how `HttpOnly` stops XSS token theft and `SameSite=Strict` stops CSRF."
                    ],
                    "answer": "1. Server CORS Response Headers:\nThe Nile API server must be configured to append the following HTTP headers on responses (and handle preflight `OPTIONS` requests):\n```http\nAccess-Control-Allow-Origin: https://student.github.io\nAccess-Control-Allow-Methods: GET, POST, OPTIONS\nAccess-Control-Allow-Headers: Content-Type, Authorization\nAccess-Control-Allow-Credentials: true\n```\n\n2. Hardened Session Cookie Configuration:\nWhen authenticating users, the server must issue the session token with three vital security attributes:\n```http\nSet-Cookie: session_token=abc987xyz; Path=/; Secure; HttpOnly; SameSite=Strict\n```\n- `HttpOnly`: Completely blocks client-side JavaScript (`document.cookie`) from reading the cookie, neutralizing session hijacking via Cross-Site Scripting (XSS).\n- `Secure`: Guarantees that the browser transmits the cookie strictly over encrypted HTTPS connections, preventing plain-text packet sniffing on Wi-Fi networks.\n- `SameSite=Strict`: Instructs the browser never to send the cookie along with cross-site requests originating from external third-party sites, preventing Cross-Site Request Forgery (CSRF) attacks.",
                    "explanation": "Configuring standard CORS headers and hardened cookie flags establishes enterprise-grade client-server security.",
                    "why_wrong": {},
                    "source": "MDN CORS; OWASP Session Management Cheat Sheet"
                }
            ]
        }
    ]
}

out_file = r"c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content\IFT 203\web_security_servers.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(topic_data, f, indent=2)

print(f"Successfully generated {out_file} with {len(topic_data['questions']) + sum(len(cs['sub_questions']) for cs in topic_data.get('case_studies', []))} total questions.")
