import sys
import time
from playwright.sync_api import sync_playwright

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_tests():
    print("=" * 70)
    print("PLAYWRIGHT VERIFICATION: CONFIDENCE MODAL DEDUP & WRITTEN MODE")
    print("=" * 70)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Mobile viewport similar to user's phone screenshot (e.g. 390x844)
        context = browser.new_context(viewport={"width": 390, "height": 844})
        page = context.new_page()

        # Track console errors
        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: errors.append(str(err)))

        print("1. Loading Study Buddy PWA...")
        page.goto("http://localhost:8080/index.html#practice?course=IFT%20205")
        page.wait_for_selector("#btn-start-practice", timeout=10000)
        print("  ✓ Practice setup loaded cleanly.")

        # Test A: Start practice session and test clicking options repeatedly
        print("2. Starting Practice Session for IFT 205...")
        page.click("#btn-start-practice")
        page.wait_for_selector(".options-list", timeout=10000)
        print("  ✓ Question loaded with options.")

        # Check options count
        options = page.query_selector_all(".option-btn")
        assert len(options) >= 2, f"Expected at least 2 options, found {len(options)}"

        # Step 1: Click Option 0
        print("3. Tapping Option A...")
        options[0].click()
        time.sleep(0.3)

        # Verify exactly 1 confidence modal exists
        modals = page.query_selector_all(".confidence-modal")
        print(f"  Confidence modals present after Option A: {len(modals)}")
        assert len(modals) == 1, f"Expected 1 modal, found {len(modals)}"

        # Step 2: Try to click or change option
        # In our fixed version, the modal has a "Change Selection" button and backdrop
        print("4. Tapping 'Change Selection' to switch answers...")
        change_btn = page.query_selector(".confidence-cancel-btn")
        assert change_btn is not None, "Change Selection button should be present"
        change_btn.click()
        time.sleep(0.3)

        modals = page.query_selector_all(".confidence-modal")
        print(f"  Confidence modals present after cancel: {len(modals)}")
        assert len(modals) == 0, f"Expected 0 modals after cancel, found {len(modals)}"

        # Step 3: Now tap Option B
        print("5. Tapping Option B...")
        options[1].click()
        time.sleep(0.3)

        modals = page.query_selector_all(".confidence-modal")
        print(f"  Confidence modals present after Option B: {len(modals)}")
        assert len(modals) == 1, f"Expected exactly 1 modal, found {len(modals)}"

        # Step 4: Click 'Sure'
        print("6. Confirming confidence with '🎯 Sure'...")
        sure_btn = page.query_selector(".confidence-row button[data-conf='sure']")
        assert sure_btn is not None, "Sure button should be present"
        sure_btn.click()
        time.sleep(0.5)

        # Modal must be gone
        modals = page.query_selector_all(".confidence-modal")
        print(f"  Confidence modals present after rating: {len(modals)}")
        assert len(modals) == 0, f"Expected 0 modals after rating, found {len(modals)}"

        # Verify question is evaluated (buttons disabled, explanation shown)
        explanation = page.query_selector(".explanation-box")
        assert explanation is not None, "Explanation box should be revealed after answer"
        print("  ✓ Answer evaluated and explanation revealed.")

        # Step 5: Advance to next question
        print("7. Advancing to next question...")
        next_btn = page.query_selector("#btn-next-q")
        assert next_btn is not None, "Next Question button should be visible"
        next_btn.click()
        time.sleep(0.5)

        # Verify no orphaned confidence modals on next question
        modals = page.query_selector_all(".confidence-modal")
        assert len(modals) == 0, f"Expected 0 orphaned modals on next question, found {len(modals)}"
        print("  ✓ Zero orphaned modals on next question.")

        # Test B: Written Mode Filter
        print("\n8. Testing '✍️ Written / Type-In Only' Filter in Practice Setup...")
        page.goto("http://localhost:8080/index.html#practice?course=COS%20201")
        page.wait_for_selector("#btn-start-practice", timeout=10000)

        # Select '✍️ Written / Type-In Only' chip
        written_chip = page.query_selector("#type-chips button[data-type='written']")
        assert written_chip is not None, "Written filter chip should exist"
        written_chip.click()
        time.sleep(0.2)

        # Start practice with written filter
        page.click("#btn-start-practice")
        time.sleep(0.8)

        # Check that the question rendered has an input or textarea
        text_input = page.query_selector("input.answer-input, textarea.answer-input, input.cloze-blank")
        assert text_input is not None, "Written practice question must provide an input or textarea!"
        input_tag = page.evaluate("el => el.tagName.toLowerCase()", text_input)
        input_ph = page.evaluate("el => el.getAttribute('placeholder')", text_input)
        print(f"  ✓ Written question rendered with <{input_tag}> (placeholder: '{input_ph}')")

        # Type an answer into the input
        text_input.fill("test answer")
        time.sleep(0.2)
        print("  ✓ Successfully typed answer into input box!")

        # Verify zero console errors throughout the entire test
        print(f"\n9. Console errors recorded: {len(errors)}")
        if errors:
            print("Errors:", errors)
        assert len(errors) == 0, "Zero console errors expected"

        browser.close()
        print("\n" + "=" * 70)
        print("ALL TESTS PASSED! CONFIDENCE DEDUP AND WRITTEN MODE 100% VERIFIED!")
        print("=" * 70)

if __name__ == "__main__":
    run_tests()
