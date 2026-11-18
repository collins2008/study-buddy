# Topic Inventory: IFT 203 Topic 7 — Web Hosting, HTTP Status Codes & Best Practices
**Topic Slug**: `web_security_servers`
**Source Materials**:
- IFT 203 Syllabus & Web Technology Lecture Notes (Web Servers, Hosting, HTTP Status Codes, Security, Performance)
- IETF RFC 9110 HTTP Semantics & RFC 9112 HTTP/1.1
- W3C Web Performance & OWASP Web Security Fundamentals

---

## 1. Exhaustive Concept Inventory

### A. Web Server Architecture & Hosting Models
- **Web Server Definition**: Dual concept: (1) Hardware computer connected to the Internet with public IP; (2) Software daemon (Apache, Nginx, Microsoft IIS, Node.js) listening on TCP port 80/443 that serves files or reverse-proxies requests.
- **Hosting Models**:
  - *Shared Hosting*: Multiple customer sites hosted on one OS/server instance; cheap, shared IP, resource contention risk.
  - *Virtual Private Server (VPS)*: Hypervisor virtualization carving dedicated CPU/RAM slices per tenant.
  - *Dedicated Hosting*: Exclusive physical machine; maximum security and control, high cost.
  - *Cloud & Edge Hosting*: Elastic distributed compute (AWS EC2, Google Cloud, Vercel, Netlify).
  - *Content Delivery Network (CDN)*: Distributed edge caching nodes (Cloudflare) caching static assets near users.

### B. Standard HTTP Response Status Codes
- **1xx Informational**: `100 Continue`.
- **2xx Success**:
  - `200 OK`: Request succeeded, body contains payload.
  - `201 Created`: Request fulfilled, new resource created (POST response).
  - `204 No Content`: Succeeded, but response body is intentionally empty.
- **3xx Redirection**:
  - `301 Moved Permanently`: Permanent redirect; search engines transfer SEO ranking equity.
  - `302 Found`: Temporary redirect.
  - `304 Not Modified`: Cached copy in browser is fresh; zero payload transmitted.
- **4xx Client Error**:
  - `400 Bad Request`: Malformed syntax or invalid parameters.
  - `401 Unauthorized`: Authentication required (missing or invalid credentials).
  - `403 Forbidden`: Authenticated, but lacking permission/rights to access resource.
  - `404 Not Found`: Target URL does not exist on server.
  - `405 Method Not Allowed`: HTTP method not supported for target resource.
- **5xx Server Error**:
  - `500 Internal Server Error`: Unhandled crash/exception in backend code.
  - `502 Bad Gateway`: Reverse proxy received an invalid response from upstream server.
  - `503 Service Unavailable`: Server overloaded or temporarily down for maintenance.
  - `504 Gateway Timeout`: Upstream server failed to respond within proxy timeout limit.

### C. Web Security & Browser Isolation
- **HTTPS & TLS**: Symmetric AES encryption for data stream + asymmetric RSA/ECC handshake for key exchange + X.509 certificates verified by trusted CAs.
- **Same-Origin Policy (SOP)**: Restricts scripts on origin A (`protocol://domain:port`) from reading data from origin B.
- **Cross-Origin Resource Sharing (CORS)**: Server HTTP response header `Access-Control-Allow-Origin: https://portal.nileuniversity.edu.ng` explicitly allowing browser cross-origin requests.
- **Secure Cookie Flags**:
  - `HttpOnly`: Prevents client-side JavaScript (`document.cookie`) from accessing the cookie, blocking XSS theft.
  - `Secure`: Ensures cookie is only transmitted over encrypted HTTPS connections.
  - `SameSite=Strict|Lax`: Mitigates Cross-Site Request Forgery (CSRF).

### D. Web Performance Optimization
- Minification: Removing whitespace and shortening variable names.
- Compression: Gzip and Brotli compression algorithms.
- Browser Caching: `Cache-Control: public, max-age=31536000, immutable`.
- Lazy Loading: `<img src="pic.jpg" loading="lazy">` delays off-screen image downloads until user scrolls.
