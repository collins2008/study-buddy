import os
import sys
import json

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from PIL import Image
from playwright.sync_api import sync_playwright

CHROME_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE_URL = "http://localhost:8080"
APP_DIR = os.path.abspath("app")

def test_manifest_and_icons():
    print("--- [1.1.1] Testing manifest.json and icons ---")
    manifest_path = os.path.join(APP_DIR, "manifest.json")
    assert os.path.exists(manifest_path), "manifest.json missing"
    
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    
    required_fields = ["name", "short_name", "start_url", "display", "icons"]
    for field in required_fields:
        assert field in manifest, f"Missing required manifest field: {field}"
        print(f"  ✓ Found manifest field '{field}': {manifest[field] if field != 'icons' else len(manifest['icons'])} icons")
    
    icons = manifest.get("icons", [])
    assert len(icons) > 0, "No icons defined in manifest"
    
    for icon_def in icons:
        icon_rel = icon_def["src"]
        icon_path = os.path.join(APP_DIR, icon_rel)
        assert os.path.exists(icon_path), f"Icon file does not exist: {icon_rel}"
        
        # Verify image using Pillow
        with Image.open(icon_path) as img:
            expected_sizes = [int(s) for s in icon_def["sizes"].split("x")]
            assert img.size == tuple(expected_sizes), f"Icon {icon_rel} size mismatch: got {img.size}, expected {expected_sizes}"
            print(f"  ✓ Icon verified: {icon_rel} ({img.size[0]}x{img.size[1]}, format {img.format})")
            
    print("Manifest & icon checks passed!\n")

def test_content_index_integrity():
    print("--- [1.1.2] Testing /content/index.json vs Disk ---")
    index_path = os.path.join(APP_DIR, "content", "index.json")
    assert os.path.exists(index_path), "content/index.json missing"
    
    with open(index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)
        
    courses = index_data.get("courses", [])
    assert len(courses) == 7, f"Expected 7 courses in index.json, got {len(courses)}"
    
    referenced_files = {os.path.abspath(index_path)}
    total_topics = 0
    
    for c in courses:
        code = c["code"]
        topics = c.get("topics", [])
        total_topics += len(topics)
        print(f"  Course {code}: {len(topics)} topics")
        for t in topics:
            file_path = os.path.join(APP_DIR, "content", code, f"{t['slug']}.json")
            assert os.path.exists(file_path), f"Referenced topic file missing: {file_path}"
            referenced_files.add(os.path.abspath(file_path))
            
        mock_file = os.path.join(APP_DIR, "content", c["mock_file"])
        assert os.path.exists(mock_file), f"Referenced mock file missing: {mock_file}"
        referenced_files.add(os.path.abspath(mock_file))
        
        cheatsheet_file = os.path.join(APP_DIR, "content", c["cheatsheet_file"])
        assert os.path.exists(cheatsheet_file), f"Referenced cheatsheet missing: {cheatsheet_file}"
        referenced_files.add(os.path.abspath(cheatsheet_file))
        
        # Also style guide exists
        style_guide = os.path.join(APP_DIR, "content", code, "STYLE_GUIDE.md")
        if os.path.exists(style_guide):
            referenced_files.add(os.path.abspath(style_guide))
            
    print(f"  ✓ All {total_topics} topic files, 7 mock files, and 7 cheatsheets referenced in index.json exist on disk.")
    
    # Check if any content file on disk is unreferenced
    content_dir = os.path.join(APP_DIR, "content")
    disk_content_files = []
    for root, _, files in os.walk(content_dir):
        for f in files:
            disk_content_files.append(os.path.abspath(os.path.join(root, f)))
                
    unreferenced = set(disk_content_files) - referenced_files
    assert len(unreferenced) == 0, f"Found unreferenced files on disk in content/: {unreferenced}"
    print(f"  ✓ Zero unreferenced content files on disk. (Total: {len(disk_content_files)})\n")

def test_headless_browser_routes():
    print("--- [1.1.3] Testing Headless Browser Navigation & Console Errors ---")
    routes_to_test = [
        "",
        "#home",
        "#course?code=COS%20201",
        "#course?code=IFT%20211",
        "#course?code=SEN%20201",
        "#course?code=IFT%20203",
        "#course?code=IFT%20205",
        "#course?code=INS%20202",
        "#course?code=ENT%20211",
        "#practice?course=COS%20201&topic=all&diff=all&type=all",
        "#learn?course=COS%20201",
        "#mock?course=COS%20201",
        "#stats",
        "#games",
        "#weak",
        "#cheatsheet?code=COS%20201",
        "#settings"
    ]
    
    console_logs = []
    console_errors = []
    page_errors = []
    failed_requests = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
        context = browser.new_context(viewport={"width": 412, "height": 915}) # Mobile viewport
        page = context.new_page()
        
        page.on("console", lambda msg: (
            console_errors.append(f"[{msg.type}] {msg.text}") if msg.type in ["error"]
            else console_logs.append(f"[{msg.type}] {msg.text}")
        ))
        page.on("pageerror", lambda err: page_errors.append(str(err)))
        page.on("requestfailed", lambda req: failed_requests.append(f"{req.method} {req.url}: {req.failure}"))
        
        for route in routes_to_test:
            url = f"{BASE_URL}/{route}"
            print(f"  Navigating to {url} ...")
            resp = page.goto(url, wait_until="networkidle", timeout=10000)
            if resp is not None:
                assert resp.status == 200 or resp.status == 304, f"Failed HTTP response {resp.status} for {url}"
            page.wait_for_timeout(600)
            
            # Check for dead-end or blank page
            body_text = page.inner_text("body")
            assert len(body_text.strip()) > 10, f"Page rendered empty or blank for route {route}!"
            
        browser.close()
        
    print(f"  Page errors: {len(page_errors)}")
    if page_errors:
        for err in page_errors:
            print(f"    ERROR: {err}")
            
    print(f"  Console errors: {len(console_errors)}")
    if console_errors:
        for err in console_errors:
            print(f"    CONSOLE ERROR: {err}")
            
    print(f"  Failed requests: {len(failed_requests)}")
    if failed_requests:
        for err in failed_requests:
            print(f"    FAILED REQ: {err}")
            
    assert len(page_errors) == 0, f"Uncaught JS exceptions encountered: {page_errors}"
    assert len(console_errors) == 0, f"Console errors encountered: {console_errors}"
    print("Headless browser navigation & console checks passed!\n")

if __name__ == "__main__":
    try:
        test_manifest_and_icons()
        test_content_index_integrity()
        test_headless_browser_routes()
        print("=== PART 1.1 INITIAL VERIFICATION COMPLETE ===")
    except Exception as e:
        print("VERIFICATION FAILED:", e)
        raise e
