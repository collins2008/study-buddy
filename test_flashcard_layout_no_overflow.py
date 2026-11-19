import time
import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

def test_flashcard_layout():
    viewports = [
        {"name": "360px Small Mobile", "width": 360, "height": 740},
        {"name": "390px iPhone", "width": 390, "height": 844},
        {"name": "412px Galaxy", "width": 412, "height": 915},
        {"name": "1280px Desktop", "width": 1280, "height": 800}
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for vp in viewports:
            print(f"\n=======================================================")
            print(f"Testing Viewport: {vp['name']} ({vp['width']}x{vp['height']})")
            print(f"=======================================================")

            context = browser.new_context(viewport={"width": vp["width"], "height": vp["height"]})
            page = context.new_page()

            console_errors = []
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

            page.goto("http://localhost:8080/index.html")
            page.wait_for_selector(".course-card")
            time.sleep(0.3)

            # Test the exact question from user's latest screenshot: ift203-hs-fc03
            metrics = page.evaluate("""
                async () => {
                    const target = document.createElement('div');
                    target.id = 'fc-layout-test';
                    document.getElementById('view-container').prepend(target);

                    const resp = await fetch('content/IFT 203/html_structure_semantics.json');
                    const data = await resp.json();
                    const q = data.questions.find(item => item.id === 'ift203-hs-fc03');

                    await Renderers.renderQuestion(q, target, () => {});

                    const meta = target.querySelector('.q-meta');
                    const card = target.querySelector('.flashcard-box');
                    const ratingRow = target.querySelector('.rating-row');
                    const promptDiv = target.querySelector('.q-question');

                    const metaBox = meta.getBoundingClientRect();
                    const cardBoxBefore = card.getBoundingClientRect();
                    const frontText = card.innerText;

                    // Click to flip
                    card.click();
                    // Wait for flip transition (150ms + margin)
                    await new Promise(r => setTimeout(r, 220));

                    const cardBoxFlipped = card.getBoundingClientRect();
                    const ratingBox = ratingRow.getBoundingClientRect();
                    const backText = card.innerText;
                    const badge = card.querySelector('.flashcard-badge-row');
                    const badgeBox = badge.getBoundingClientRect();

                    return {
                        hasPromptDiv: !!promptDiv,
                        frontText,
                        backText,
                        metaBottom: metaBox.bottom,
                        cardTop: cardBoxFlipped.top,
                        cardBottom: cardBoxFlipped.bottom,
                        cardHeight: cardBoxFlipped.height,
                        badgeTop: badgeBox.top,
                        ratingTop: ratingBox.top,
                        // Bounding box collision checks:
                        // Card must start below meta header
                        overlapsHeader: cardBoxFlipped.top < metaBox.bottom,
                        // Card must end above rating row
                        overlapsRating: cardBoxFlipped.bottom > ratingBox.top,
                        // Badge must be strictly inside card
                        badgeInsideCard: badgeBox.top >= cardBoxFlipped.top && badgeBox.bottom <= cardBoxFlipped.bottom
                    };
                }
            """)

            print(f"  Prompt div present (must be False): {metrics['hasPromptDiv']}")
            print(f"  Meta Header Bottom: {metrics['metaBottom']:.1f}px")
            print(f"  Card Top: {metrics['cardTop']:.1f}px")
            print(f"  Badge Top: {metrics['badgeTop']:.1f}px")
            print(f"  Card Bottom: {metrics['cardBottom']:.1f}px")
            print(f"  Card Height: {metrics['cardHeight']:.1f}px")
            print(f"  Rating Row Top: {metrics['ratingTop']:.1f}px")
            print(f"  Overlaps Header Meta: {metrics['overlapsHeader']}")
            print(f"  Overlaps Rating Row: {metrics['overlapsRating']}")
            print(f"  Badge Strictly Inside Card: {metrics['badgeInsideCard']}")
            print(f"  Back Text Preview:\n    {metrics['backText'][:140]}...")

            assert metrics['hasPromptDiv'] is False, "Flashcard promptDiv should be omitted"
            assert metrics['overlapsHeader'] is False, f"Flashcard overlaps header in {vp['name']}!"
            assert metrics['overlapsRating'] is False, f"Flashcard overlaps rating buttons in {vp['name']}!"
            assert metrics['badgeInsideCard'] is True, f"Badge not inside card in {vp['name']}!"

            # Verify that all HTML tags are visible and formatted
            assert "<div>" in metrics['backText'], "Back must contain visible <div>"
            assert "<p>" in metrics['backText'], "Back must contain visible <p>"
            assert "<h1>" in metrics['backText'], "Back must contain visible <h1>"
            assert "<span>" in metrics['backText'], "Back must contain visible <span>"
            assert "<a>" in metrics['backText'], "Back must contain visible <a>"
            assert "<strong>" in metrics['backText'], "Back must contain visible <strong>"

            assert len(console_errors) == 0, f"Console errors: {console_errors}"
            print(f"  ✓ {vp['name']} PASSED PERFECT ZERO-OVERFLOW & SPACING TEST!")

            context.close()

        browser.close()
        print("\n=======================================================")
        print("ALL VIEWPORTS VERIFIED: 100% COLLISION-FREE & RESPONSIVE!")
        print("=======================================================")

if __name__ == '__main__':
    test_flashcard_layout()
