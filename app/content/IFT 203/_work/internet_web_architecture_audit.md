# Hostile Pedagogical & Technical Audit: IFT 203 Topic 1
**Topic**: Internet, WWW, Protocols & Client-Server (`internet_web_architecture.json`)
**Auditor**: Senior University Examiner & Web Architecture Lead

---

## 1. Inventory & Exam Blueprint Coverage
- [x] Internet vs World Wide Web (WWW): Physical global network infrastructure (TCP/IP) vs application-level information sharing service (Tim Berners-Lee 1989).
- [x] Web Browser vs Search Engine (Lecturer notebook explicit hint): Local client rendering engine (Chrome, Firefox) vs remote web server crawler/indexing service (Google, Bing).
- [x] Webpage vs Website vs Web Application: Single HTML document vs collection of pages vs dynamic interactive database-driven software.
- [x] URL Anatomy: Scheme/Protocol (`https`), Subdomain (`portal`), Domain (`nileuniversity.edu.ng`), Port (`443`), Path (`/students/results`), Query string (`?semester=first`), Fragment (`#grades`).
- [x] Protocol mapping: HTTP (port 80 plain text), HTTPS (port 443 TLS encrypted), TCP (3-way handshake reliability), IP (addressing/routing), DNS (domain-to-IP resolution).
- [x] HTTP Web page retrieval lifecycle sequencing: 6 chronological stages from URL entry to DOM rendering.
- [x] Security: HTTP clear text packet sniffing vulnerabilities vs HTTPS TLS encryption.
- [x] Front-end vs Back-end: Client-side UI execution (HTML/CSS/JS) vs server-side persistence and API endpoints.
- [x] 2 Multi-part Case Studies:
  1. Nile University Portal Network & DNS Diagnostics: Analyzing `DNS_PROBE_FINISHED_NXDOMAIN`, hierarchical DNS resolution flow, and local operating system `hosts` file override workaround.
  2. Architectural Modernization Case Study: Evaluating why a static hosting tier (GitHub Pages) cannot run a transactional course registration portal, and designing a decoupled CDN brochure + secure multi-tier cluster architecture.

---

## 2. Statistical Breakdown
- Total Main Questions: 16
- Total Case Studies: 2 (4 sub-questions)
- Total Questions: 20
- Difficulty 1: 9 (45.0%)
- Difficulty 2: 2 (10.0%)
- Difficulty 3: 7 (35.0%)
- Difficulty 4: 2 (10.0%)
- **Higher-Order (L3-L4) Ratio**: **45.0%** (Target: $\ge 30\%$) -> **PASSED**
- Distractor Quality: 100% of distractors contain explicit, pedagogical `why_wrong` explanations dissecting networking and web misconceptions.

---

## 3. Final Verdict
**APPROVED - ZERO DEFECTS**. Ready for index registration and app consumption.
