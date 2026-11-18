# Hostile Pedagogical & Technical Audit: IFT 203 Topic 7
**Topic**: Web Hosting, HTTP Status Codes & Best Practices (`web_security_servers.json`)
**Auditor**: Senior University Examiner & Web Architecture Lead

---

## 1. Inventory & Exam Blueprint Coverage
- [x] HTTP Status Codes: `401 Unauthorized` (missing credentials) vs `403 Forbidden` (authenticated, but lacking rights/permissions).
- [x] Web Hosting Models: Shared vs VPS vs Dedicated vs Cloud/CDN edge hosting.
- [x] HTTP Redirection: `301 Moved Permanently` (transfers SEO equity) vs `302 Found` (temporary detour).
- [x] Gateway & Server Error Diagnostics: `500 Internal Error` vs `502 Bad Gateway` vs `504 Gateway Timeout`.
- [x] Status code matching: 200, 301, 400, 403, 503.
- [x] Cryptographic HTTPS / TLS Handshake sequencing: Client Hello -> Server Hello -> CA Certificate Verification -> Symmetric Session Key -> Encrypted Session.
- [x] Same-Origin Policy (SOP): Triple identity match on Protocol + Host + Port.
- [x] Performance & Security Best Practices: `HttpOnly` and `Secure` cookie flags, Gzip/Brotli compression, image lazy-loading, code minification.
- [x] 2 Multi-part Case Studies:
  1. Nile Portal Registration Crash: Diagnosing `504 Gateway Timeout` under high concurrency, analyzing upstream queue saturation, and formulating an end-to-end scaling architecture (Nginx load balancing, Redis caching, DB connection pooling, CDN offload).
  2. Cross-Origin API & Cookie Security: Diagnosing browser CORS blocking, writing server CORS authorization response headers, and securing session cookies with `HttpOnly`, `Secure`, and `SameSite=Strict`.

---

## 2. Statistical Breakdown
- Total Main Questions: 16
- Total Case Studies: 2 (4 sub-questions)
- Total Questions: 20
- Difficulty 1: 8 (40.0%)
- Difficulty 2: 3 (15.0%)
- Difficulty 3: 7 (35.0%)
- Difficulty 4: 2 (10.0%)
- **Higher-Order (L3-L4) Ratio**: **45.0%** (Target: $\ge 30\%$) -> **PASSED**
- Distractor Quality: 100% of distractors contain explicit, pedagogical `why_wrong` explanations dissecting server architecture and security misconceptions.

---

## 3. Final Verdict
**APPROVED - ZERO DEFECTS**. Ready for index registration and app consumption.
