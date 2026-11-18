import os
import sys
import json
import time

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from playwright.sync_api import sync_playwright

CHROME_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE_URL = "http://localhost:8080"

def test_offline_capability():
    print("--- [1.1.4] Testing Offline Mode & Service Worker Cache ---")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
        # Use an isolated browser context
        context = browser.new_context(viewport={"width": 412, "height": 915})
        page = context.new_page()
        
        console_msgs = []
        page.on("console", lambda m: console_msgs.append(f"[{m.type}] {m.text}"))
        
        # 1. First load: Online
        print("  1. Loading app online to register SW and populate cache...")
        page.goto(BASE_URL, wait_until="networkidle")
        
        # Wait for SW registration and cacheAllContent to execute
        page.wait_for_timeout(3500)
        
        # Verify Cache Storage in browser
        caches_info = page.evaluate("""async () => {
            const keys = await caches.keys();
            const details = {};
            for (const k of keys) {
                const c = await caches.open(k);
                const reqs = await c.keys();
                details[k] = reqs.length;
            }
            return details;
        }""")
        print(f"  Caches found in browser: {caches_info}")
        assert len(caches_info) > 0, "No CacheStorage entries found!"
        assert caches_info.get("studybuddy-v1", 0) > 0, "Shell cache missing or empty!"
        assert caches_info.get("studybuddy-content-v1", 0) >= 50, f"Expected at least 50 content items in cache, got {caches_info.get('studybuddy-content-v1', 0)}"
        print(f"  ✓ Cache verified: Shell ({caches_info['studybuddy-v1']} assets), Content ({caches_info['studybuddy-content-v1']} files)")
        
        # 2. Go Offline
        print("  2. Disconnecting network (Going 100% OFFLINE)...")
        context.set_offline(True)
        
        # 3. Reload while offline
        print("  3. Reloading page while offline...")
        page.reload(wait_until="domcontentloaded")
        page.wait_for_timeout(1000)
        
        # Confirm app shell rendered
        title = page.title()
        print(f"  Page title after offline reload: '{title}'")
        assert "Study Buddy" in title, "App shell failed to render while offline!"
        
        # Confirm course list rendered
        course_cards = page.locator(".course-card").count()
        print(f"  Course cards rendered offline: {course_cards}")
        assert course_cards == 7, f"Expected 7 course cards offline, found {course_cards}"
        
        # 4. Navigate to course page while offline
        print("  4. Navigating to COS 201 topic list offline...")
        page.click(".course-card[data-code='COS 201']")
        page.wait_for_timeout(1000)
        html = page.inner_html("#view-container")
        topic_items = page.locator(".topic-item").count()
        print(f"  Container HTML snippet: {html[:250]}...")
        print(f"  COS 201 topics rendered offline: {topic_items}")
        assert topic_items >= 9, f"Expected at least 9 topics offline, found {topic_items}"
        
        # 5. Start Practice session while offline
        print("  5. Starting Practice session offline...")
        page.click("#btn-course-practice")
        page.wait_for_timeout(600)
        
        # Click start practice button
        page.click("#btn-start-practice")
        page.wait_for_timeout(800)
        
        # Check if question text rendered
        q_text = page.locator(".q-question").first.text_content()
        print(f"  Practice question loaded offline: '{q_text[:60]}...'")
        assert len(q_text.strip()) > 5, "Question text empty in offline mode!"
        
        # 6. Check Cheatsheet offline
        print("  6. Loading Cheatsheet offline...")
        page.evaluate("Router.navigate('cheatsheet', { code: 'COS 201' })")
        page.wait_for_timeout(800)
        cs_text = page.inner_text("body")
        assert "COS 201" in cs_text, "Cheatsheet content missing offline!"
        print("  ✓ Cheatsheet rendered offline successfully.")
        
        browser.close()
        
    print("\n✓ [1.1.4] OFFLINE MODE AND SERVICE WORKER CACHE VERIFIED 100% OPERATIONAL!\n")

if __name__ == "__main__":
    test_offline_capability()
