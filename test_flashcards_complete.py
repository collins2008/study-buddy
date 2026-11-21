# test_flashcards_complete.py - Verify complete flashcard decks for IFT 205, INS 202, and ENT 211
import asyncio
from playwright.async_api import async_playwright

async def run_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 412, 'height': 915})
        page = await context.new_page()

        console_errors = []
        page.on('console', lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)

        print("1. Loading Study Buddy app...")
        await page.goto("http://localhost:8080/index.html")
        await page.wait_for_selector(".course-card", state="visible")

        # Test IFT 205 Flashcards
        print("\n2. Testing IFT 205 Flashcards Deck...")
        await page.click(".course-card[data-code='IFT 205']")
        await page.wait_for_selector("#btn-course-flashcards", state="visible")
        
        await page.click("#btn-course-flashcards")
        await page.wait_for_selector(".flashcard-box", state="visible")

        # Check total cards in app-title header
        app_title = await page.inner_text("#app-title")
        print(f"   App Header Title: {app_title}")
        assert "Flashcards: IFT 205" in app_title
        assert "(1/40)" in app_title, f"Expected (1/40) in title, got {app_title}"

        # Check front text
        front_text = await page.inner_text(".flashcard-box .flashcard-text")
        print(f"   Front Card Text: {front_text[:80]}...")
        assert len(front_text) > 5

        # Tap to flip
        print("   Tapping card to flip...")
        await page.click(".flashcard-box")
        await page.wait_for_selector(".flashcard-box.is-flipped", state="visible")
        back_text = await page.inner_text(".flashcard-box .flashcard-text")
        print(f"   Back Card Text: {back_text[:80]}...")
        assert len(back_text) > 5

        # Rating row visible
        rating_btn = page.locator(".rating-row button[data-rate='3']")
        await rating_btn.wait_for(state="visible")
        print("   Rating '4. Easy'...")
        await rating_btn.click()

        # Next question button appears
        next_btn = page.locator("#btn-next-q")
        await next_btn.wait_for(state="visible")
        print("   Clicking Next Button...")
        await next_btn.click()

        # Confirm next card rendered
        await page.wait_for_timeout(300)
        app_title_2 = await page.inner_text("#app-title")
        print(f"   New Title after advancing: {app_title_2}")
        assert "(2/40)" in app_title_2

        # Exit session via back button
        await page.click("#btn-back")
        await page.wait_for_selector(".course-card", state="visible")

        # Test INS 202 Flashcards Deck
        print("\n3. Testing INS 202 Flashcards Deck...")
        await page.click(".course-card[data-code='INS 202']")
        await page.wait_for_selector("#btn-course-flashcards", state="visible")
        await page.click("#btn-course-flashcards")
        await page.wait_for_selector(".flashcard-box", state="visible")

        ins_title = await page.inner_text("#app-title")
        print(f"   INS 202 Title: {ins_title}")
        assert "(1/56)" in ins_title, f"Expected 56 flashcards in INS 202, got {ins_title}"
        await page.click("#btn-back")
        await page.wait_for_selector(".course-card", state="visible")

        # Test ENT 211 Flashcards Deck
        print("\n4. Testing ENT 211 Flashcards Deck...")
        await page.click(".course-card[data-code='ENT 211']")
        await page.wait_for_selector("#btn-course-flashcards", state="visible")
        await page.click("#btn-course-flashcards")
        await page.wait_for_selector(".flashcard-box", state="visible")

        ent_title = await page.inner_text("#app-title")
        print(f"   ENT 211 Title: {ent_title}")
        assert "(1/32)" in ent_title, f"Expected 32 flashcards in ENT 211, got {ent_title}"
        await page.click("#btn-back")
        await page.wait_for_selector(".course-card", state="visible")

        # Test Practice Filter for Flashcards
        print("\n5. Testing Practice Mode 'Flashcard' Filter for IFT 205...")
        await page.goto("http://localhost:8080/index.html#practice")
        await page.wait_for_selector("#sel-course", state="visible")
        await page.select_option("#sel-course", "IFT 205")
        
        # Click flashcard chip
        fc_chip = page.locator("#type-chips button[data-type='flashcard']")
        await fc_chip.click()
        await page.click("#btn-start-practice")

        await page.wait_for_selector(".flashcard-box", state="visible")
        practice_title = await page.inner_text("#app-title")
        print(f"   Practice Mode Flashcard Session Loaded: {practice_title}")
        assert "Practice: IFT 205" in practice_title
        assert "flashcard" in (await page.inner_text(".tag")).lower() or await page.locator(".flashcard-box").is_visible()

        print(f"\n6. Console Errors Recorded: {console_errors}")
        assert len(console_errors) == 0, f"Found console errors: {console_errors}"

        print("\n=======================================================")
        print("ALL FLASHCARD DECK VERIFICATION TESTS PASSED 100%!")
        print("=======================================================")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_test())
