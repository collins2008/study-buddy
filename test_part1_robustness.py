import os
import sys
import json
import shutil
from playwright.sync_api import sync_playwright

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CHROME_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE_URL = "http://localhost:8080"
APP_DIR = os.path.abspath("app")

def test_robustness():
    print("=" * 70)
    print("HOSTILE EXAMINER: TESTING APP ROBUSTNESS & FAULT TOLERANCE (PART 1.5)")
    print("=" * 70)

    # -------------------------------------------------------------
    # 1.5.1 Content File Corruption & Graceful Recovery
    # -------------------------------------------------------------
    print("\n--- [1.5.1] Testing Corrupted Content File Isolation ---")
    target_file = os.path.join(APP_DIR, "content", "COS 201", "pointers_memory.json")
    backup_file = target_file + ".bak"
    
    # Create backup
    shutil.copyfile(target_file, backup_file)
    
    try:
        # Corrupt file with malformed JSON
        with open(target_file, "w", encoding="utf-8") as f:
            f.write("{\n  \"corrupted\": true,\n  \"broken_syntax: [NOT VALID JSON!}\n")
            
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
            page = browser.new_page()
            
            page_errors = []
            page.on("pageerror", lambda err: page_errors.append(str(err)))
            
            page.goto(BASE_URL, wait_until="networkidle")
            
            # Navigate to COS 201
            page.evaluate("Router.navigate('course', { code: 'COS 201' })")
            page.wait_for_timeout(500)
            
            # Verify course view still rendered other topics
            topics_rendered = page.locator(".topic-item").count()
            print(f"  Topics rendered while pointers_memory is corrupted: {topics_rendered}")
            assert topics_rendered >= 8, f"Corrupted topic crashed the course page! Rendered topics: {topics_rendered}"
            
            # Try to practice corrupted topic specifically
            res = page.evaluate("""async () => {
                try {
                    const data = await App.loadTopicContent('COS 201', 'pointers_memory');
                    return { ok: true, questions: data.questions.length };
                } catch (e) {
                    return { ok: false, error: e.message };
                }
            }""")
            print(f"  Corrupted topic fallback result: {res}")
            assert res['ok'] is True, "loadTopicContent threw unhandled exception on corrupted file!"
            assert res['questions'] == 0, "Corrupted file should safely fallback to empty question array"
            assert len(page_errors) == 0, f"Uncaught page exceptions during corrupted file access: {page_errors}"
            
            browser.close()
            print("  ✓ Corrupted Content File Isolated Gracefully Without App Crash")
    finally:
        # Restore backup
        if os.path.exists(backup_file):
            shutil.copyfile(backup_file, target_file)
            os.remove(backup_file)
            print("  ✓ Restored original pointers_memory.json from backup")

    # -------------------------------------------------------------
    # 1.5.2 Cold Boot With Cleared Storage
    # -------------------------------------------------------------
    print("\n--- [1.5.2] Testing Cold Boot After Clearing Storage ---")
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL, wait_until="networkidle")
        
        # Clear storage and delete IndexedDB
        clear_res = page.evaluate("""async () => {
            localStorage.clear();
            sessionStorage.clear();
            const dbs = await indexedDB.databases();
            for (const db of dbs) {
                indexedDB.deleteDatabase(db.name);
            }
            return true;
        }""")
        
        # Reload cold
        page.reload(wait_until="networkidle")
        page.wait_for_timeout(800)
        
        # Check clean start
        courses_count = page.locator(".course-card").count()
        app_title = page.title()
        streak_val = page.locator("#streak-count").text_content()
        
        print(f"  Courses after wipe: {courses_count}, Title: '{app_title}', Initial Streak: {streak_val}")
        assert courses_count == 7, f"Expected 7 courses after clean storage cold boot, found {courses_count}"
        assert "Study Buddy" in app_title, "App failed to boot after storage wipe"
        browser.close()
        print("  ✓ Cold Boot With Completely Cleared Storage Verified")

    # -------------------------------------------------------------
    # 1.5.3 Duplicate Questions in One Session Check
    # -------------------------------------------------------------
    print("\n--- [1.5.3] Testing Duplicate Question Prevention in Session ---")
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
        page = browser.new_page()
        page.goto(BASE_URL, wait_until="networkidle")
        
        dup_check = page.evaluate("""async () => {
            // Load 40 mock questions for COS 201
            const qs = await App.loadMockQuestions('COS 201', 40);
            const ids = qs.map(q => q.id);
            const uniqueIds = new Set(ids);
            
            // Also check a large practice pool of 50
            const practiceQs = await App.loadQuestionsForPractice('COS 201', 'all', 'all', 50);
            const pIds = practiceQs.map(q => q.id);
            const uniquePIds = new Set(pIds);
            
            return {
                mockCount: qs.length,
                mockUnique: uniqueIds.size,
                practiceCount: practiceQs.length,
                practiceUnique: uniquePIds.size
            };
        }""")
        print(f"  Mock exam pool: {dup_check['mockCount']} questions, {dup_check['mockUnique']} unique IDs")
        print(f"  Practice pool : {dup_check['practiceCount']} questions, {dup_check['practiceUnique']} unique IDs")
        assert dup_check['mockCount'] == dup_check['mockUnique'], "Duplicate questions found in mock exam session!"
        assert dup_check['practiceCount'] == dup_check['practiceUnique'], "Duplicate questions found in practice session!"
        browser.close()
        print("  ✓ Zero Duplicate Questions in Session Verified")

    # -------------------------------------------------------------
    # 1.5.4 Navigation Dead-End Audit
    # -------------------------------------------------------------
    print("\n--- [1.5.4] Testing Navigation Dead-Ends Across All Screens ---")
    views_to_test = [
        ("course", {"code": "COS 201"}),
        ("practice", {"course": "COS 201"}),
        ("mock", {"course": "COS 201"}),
        ("stats", {}),
        ("games", {}),
        ("weak", {}),
        ("cheatsheet", {"code": "COS 201"}),
        ("settings", {})
    ]
    
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
        page = browser.new_page()
        page.goto(BASE_URL, wait_until="networkidle")
        
        for view_name, params in views_to_test:
            # Navigate to view
            page.evaluate(f"Router.navigate('{view_name}', {json.dumps(params)})")
            page.wait_for_timeout(300)
            
            # Check back button visible
            back_btn = page.locator("#btn-back")
            is_visible = back_btn.is_visible()
            assert is_visible is True, f"Back button missing on view: {view_name} (Dead End!)"
            
            # Click back button and verify return to home
            back_btn.click()
            page.wait_for_timeout(300)
            
            cur_view = page.evaluate("Router.currentView")
            assert cur_view == "home", f"Back button on view {view_name} failed to return to home, currently at: {cur_view}"
            print(f"  ✓ Screen '{view_name}': Back button visible & successfully navigates to home")
            
        browser.close()
        print("  ✓ All Screens Verified Free of Navigation Dead-Ends")

    print("\n✓ [PART 1.5] ROBUSTNESS & FAULT TOLERANCE VERIFIED 100% OPERATIONAL!\n")

if __name__ == "__main__":
    test_robustness()
