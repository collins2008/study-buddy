import json
import glob
import os
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

IFT203_DIR = "app/content/IFT 203"

EXAMINER_ENRICHMENTS = {
    # CSS Box Model
    "ift203-bm-fc01": "The W3C CSS Box Model consists of four concentric rectangular layers from inside out: 1) Content (text/media dimensions defined by width and height); 2) Padding (transparent clearance area around content inside the border); 3) Border (visible boundary stroke wrapping padding and content); and 4) Margin (transparent buffer clearing external surrounding elements). (W3C CSS Box Model Level 3).",
    "ift203-bm-fc05": "In CSS layout, 'display: none' removes the element entirely from the document flow as if it did not exist, causing surrounding elements to collapse into its space. In contrast, 'visibility: hidden' hides the element visually while preserving its exact physical dimensions and layout footprint on the page. (MDN Web Docs; W3C CSS Display).",
    "ift203-bm-fc08": "The modern CSS Flexbox two-axis centering technique requires three declarations on the parent container: 1) 'display: flex;' (creates flex formatting context); 2) 'justify-content: center;' (centers flex items along the primary horizontal axis); and 3) 'align-items: center;' (centers items along the perpendicular cross axis). Alternatively, CSS Grid uses 'display: grid; place-items: center;'. (W3C CSS Flexible Box Layout).",

    # CSS Selectors & Specificity
    "ift203-cs-fc04": "W3C CSS Specificity is evaluated as a 4-tier tuple (a, b, c, d): a = inline styles (style attribute, 1,0,0,0); b = ID selectors (#nav, 0,1,0,0); c = class selectors, attribute selectors, and pseudo-classes (.btn, [type='text'], :hover, 0,0,1,0); d = type/element selectors and pseudo-elements (div, p, ::before, 0,0,0,1). The universal selector (*) and combinators have zero specificity (0,0,0,0). (W3C CSS Selectors Level 4).",
    "ift203-cs-fc08": "The '!important' declaration in CSS overrides all standard cascade specificity calculations within that declaration's origin. It should be strictly avoided in application stylesheets because it breaks the natural cascade, forces subsequent developers to write even more '!important' rules, and creates maintainability nightmares. (MDN Web Docs).",

    # HTML Forms, Tables & Media
    "ift203-ft-fc03": "To create a mutually exclusive radio button group, all '<input type=\"radio\">' elements in the group must share the exact same 'name' attribute value. The browser will then permit only one radio button in that group to be checked at any given time. (W3C HTML5 Specification).",
    "ift203-ft-fc04": "The '<label for=\"element-id\">' element provides a programmatic association between a descriptive text label and a form control. Clicking the label focuses or toggles the input (vital for small mobile touch targets on checkboxes/radios), and screen readers announce the label text when the input receives focus. (W3C Web Content Accessibility Guidelines - WCAG 2.1).",
    "ift203-ft-fc06": "The fundamental difference between form control states: A 'readonly' input prevents user editing but its value IS submitted with the form payload during submission. A 'disabled' input is greyed out, cannot be focused or modified, and its value is strictly EXCLUDED from the submitted form data payload. (W3C HTML5 Form Submission).",
    "ift203-ft-fc07": "The 'alt' (alternative text) attribute on '<img>' elements is mandatory under WCAG guidelines: screen readers read it aloud to visually impaired users, web crawlers use it for search engine indexing, and browsers display it as a fallback if the image asset fails to load. Empty 'alt=\"\"' is reserved only for purely decorative images. (WCAG 2.1 Principle 1: Perceivable).",
    "ift203-ft-fc08": "When opening links in a new tab via 'target=\"_blank\"', modern web security requires adding 'rel=\"noopener noreferrer\"'. Without 'noopener', the target page gains access to the originating window's 'window.opener' object, enabling malicious reverse tabnabbing phishing attacks. (MDN Web Security; OWASP Foundation).",

    # HTML Structure & Semantics
    "ift203-hs-fc06": "Semantic HTML means using HTML markup tags according to their inherent meaning and purpose (e.g. '<nav>', '<main>', '<article>', '<header>', '<footer>') rather than generic presentational wrappers ('<div>', '<span>'). It enhances accessibility for screen readers, improves search engine indexing (SEO), and provides clean document structure for team maintainability. (W3C HTML5 Semantics).",
    "ift203-hs-fc08": "The viewport meta tag '<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">' instructs mobile browser rendering engines to set the logical layout viewport width equal to the physical screen width of the device and establish a 1:1 initial zoom scale, preventing mobile browsers from defaulting to a zoomed-out 980px desktop view. (W3C Responsive Web Design).",

    # Internet & Web Architecture
    "ift203-wa-fc02": "A Web Browser (client-side user agent) requests resources over HTTP/HTTPS, parses HTML/CSS/JS, executes scripts, and renders visual web pages to the user. A Web Server (host daemon like Nginx or Apache) listens on network ports (80/443), handles incoming HTTP requests, enforces security/authentication, executes backend scripts, and serves static or dynamic response documents. (RFC 7230).",
    "ift203-wa-fc06": "Under RFC 3986, a Uniform Resource Identifier (URI/URL) consists of five primary components: 1) Scheme/Protocol (http, https); 2) Authority (host domain and optional port, e.g. example.com:8080); 3) Path (/courses/ift203); 4) Query string (?id=12&sort=asc); and 5) Fragment identifier (#section3).",
    "ift203-wa-fc08": "Front-End development focuses on client-side code executed directly inside the user's browser (HTML, CSS, JavaScript, responsive UI, accessibility, client routing). Back-End development focuses on server-side architecture (databases, API microservices, server routing, business logic, session security, encryption, and third-party integrations). (Nile Course Syllabus).",

    # JavaScript DOM Basics
    "ift203-js-fc02": "In modern ECMAScript (ES6+): 'var' is function-scoped and hoisted with undefined initialization (prone to bugs); 'let' is block-scoped, not accessible before declaration (Temporal Dead Zone), and allows reassignment; 'const' is block-scoped, cannot be reassigned after declaration, and requires immediate initialization. (MDN JavaScript Reference).",
    "ift203-js-fc04": "The Document Object Model (DOM) is a cross-platform, language-independent W3C programming interface that represents HTML and XML documents as a hierarchical tree of objects and nodes, allowing programming languages (such as JavaScript) to dynamically inspect, modify, add, or delete document content, structure, and styles. (W3C DOM Level 4).",
    "ift203-js-fc05": "The method 'document.querySelector(selector)' returns the first Element within the document that matches the specified CSS selector, or null if no match is found. In contrast, 'document.querySelectorAll(selector)' returns a static NodeList representing all matching elements in document order. (W3C Selectors API).",
    "ift203-js-fc06": "Assigning unvalidated user input to 'element.innerHTML' parses strings as executable HTML markup, exposing the application to catastrophic Cross-Site Scripting (XSS) attacks. Using 'element.textContent' ensures the browser treats data strictly as raw literal text, automatically neutralizing malicious script injection tags. (OWASP Top 10: XSS Prevention).",
    "ift203-js-fc08": "Event Delegation is a high-performance DOM event handling design pattern where a single event listener is attached to a common ancestor element rather than attaching individual listeners to multiple child elements. It leverages the DOM Event Bubbling phase ('event.target') to handle clicks on current and dynamically added children with minimal memory overhead. (MDN Event Reference).",

    # Web Security & Servers
    "ift203-ws-fc01": "A Web Server can refer to hardware (a physical or virtual computer connected to the internet) or software (an HTTP server daemon such as Nginx, Apache HTTPD, or Caddy) responsible for receiving client requests, resolving URI routes, and returning HTTP responses with corresponding MIME types. (RFC 7230).",
    "ift203-ws-fc02": "HTTP '401 Unauthorized' indicates that the request lacks valid authentication credentials (e.g. missing or expired API token/session cookie) and must include a 'WWW-Authenticate' header. In contrast, HTTP '403 Forbidden' means the server recognizes the user's authenticated identity, but that identity is strictly unauthorized/forbidden from accessing the requested resource (RBAC permission denial). (RFC 7231).",
    "ift203-ws-fc03": "HTTP '301 Moved Permanently' indicates the requested URI resource has been assigned a new permanent URI; browsers and search engines cache the redirection and transfer SEO page rank to the target URL. HTTP '302 Found' (or 307 Temporary Redirect) indicates the redirection is temporary; clients continue using the original URI for future requests. (RFC 7231).",
    "ift203-ws-fc04": "HTTP '502 Bad Gateway' indicates that a reverse proxy or gateway server (such as Nginx or Cloudflare) received an invalid, malformed, or dropped response from the upstream application server. HTTP '504 Gateway Timeout' indicates the proxy server did not receive a timely response from the upstream server before its timeout threshold expired. (RFC 7231).",
    "ift203-ws-fc07": "The 'HttpOnly' attribute on a Set-Cookie header instructs the web browser that the cookie must not be accessible via client-side JavaScript APIs (such as 'document.cookie'). This critical security defense mitigates session hijacking by preventing malicious XSS scripts from stealing authenticated session tokens. (RFC 6265).",
    "ift203-ws-fc08": "Code minification is a production optimization process that removes all unnecessary whitespace, newline characters, code comments, and shortens variable identifiers without altering program functionality. It substantially reduces payload byte size, minimizes network transfer latency, and accelerates web page load times. (W3C Web Performance)."
}

def enrich_and_fix_ift203():
    files = sorted(glob.glob(os.path.join(IFT203_DIR, "*.json")))
    
    updated_expl = 0
    id_map = {}
    
    for f in files:
        if "mock_exams" in f:
            continue
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            
        modified = False
        for q in data.get("questions", []):
            qid = q.get("id")
            if qid in EXAMINER_ENRICHMENTS:
                q["explanation"] = EXAMINER_ENRICHMENTS[qid]
                updated_expl += 1
                modified = True
            id_map[qid] = q
            
        if modified:
            with open(f, "w", encoding="utf-8") as fp:
                json.dump(data, fp, indent=2, ensure_ascii=False)
                
    # Sync mock_exams.json
    mock_file = os.path.join(IFT203_DIR, "mock_exams.json")
    if os.path.exists(mock_file):
        with open(mock_file, "r", encoding="utf-8") as fp:
            mdata = json.load(fp)
        synced = 0
        for exam in mdata.get("exams", []):
            for q in exam.get("questions", []):
                qid = q.get("id")
                if qid in id_map:
                    src = id_map[qid]
                    q["explanation"] = src["explanation"]
                    if "why_wrong" in src:
                        q["why_wrong"] = src["why_wrong"]
                    synced += 1
        with open(mock_file, "w", encoding="utf-8") as fp:
            json.dump(mdata, fp, indent=2, ensure_ascii=False)
        print(f"Synced {synced} questions in IFT 203 mock_exams.json")

    print(f"Applied {updated_expl} explanation enrichments in IFT 203.")

if __name__ == "__main__":
    enrich_and_fix_ift203()
