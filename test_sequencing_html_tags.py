import time
import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

def test_sequencing():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 412, "height": 915})
        page = context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        print("1. Loading Study Buddy app...")
        page.goto("http://localhost:8080/index.html")
        page.wait_for_selector(".course-card")
        time.sleep(0.3)

        print("2. Testing question ift203-hs-006 (HTML5 skeleton sequencing)...")
        res = page.evaluate("""
            async () => {
                const target = document.createElement('div');
                target.id = 'seq-test-container';
                document.getElementById('view-container').prepend(target);

                const resp = await fetch('content/IFT 203/html_structure_semantics.json');
                const data = await resp.json();
                const q = data.questions.find(item => item.id === 'ift203-hs-006');

                await Renderers.renderQuestion(q, target, () => {});

                const items = Array.from(target.querySelectorAll('.seq-item'));
                const itemTexts = items.map(el => el.querySelector('.flex-1').innerText.trim());
                const itemHtmls = items.map(el => el.querySelector('.flex-1').innerHTML);
                
                // Check if any slot has empty text
                const hasEmpty = itemTexts.some(t => t.length === 0);

                // Check if live <h1> or <p> tags were created as HTML DOM children of .flex-1
                const hasLiveH1 = items.some(el => !!el.querySelector('.flex-1 h1'));
                const hasLiveP = items.some(el => !!el.querySelector('.flex-1 p'));

                // Check if code tags were created
                const codeTagsCount = items.filter(el => !!el.querySelector('.flex-1 code')).length;

                return {
                    itemCount: items.length,
                    itemTexts,
                    itemHtmls,
                    hasEmpty,
                    hasLiveH1,
                    hasLiveP,
                    codeTagsCount
                };
            }
        """)

        print(f"   Item count: {res['itemCount']}")
        print(f"   Any item blank: {res['hasEmpty']}")
        print(f"   Has Live <h1> heading (must be False): {res['hasLiveH1']}")
        print(f"   Has Live <p> paragraph (must be False): {res['hasLiveP']}")
        print(f"   Code tags count (should be 5): {res['codeTagsCount']}")
        for idx, text in enumerate(res['itemTexts']):
            print(f"   Slot {idx + 1}: {text}")

        assert res['itemCount'] == 5, f"Expected 5 items, got {res['itemCount']}"
        assert res['hasEmpty'] is False, "No sequencing slot should be blank!"
        assert res['hasLiveH1'] is False, "HTML <h1> tag must NOT render as live DOM heading!"
        assert res['hasLiveP'] is False, "HTML <p> tag must NOT render as live DOM paragraph!"
        assert res['codeTagsCount'] == 5, "All 5 slots must be styled code tags!"

        # Verify that all 5 key tags are visible in the texts
        all_text = " ".join(res['itemTexts'])
        assert "<!DOCTYPE html>" in all_text, "Missing <!DOCTYPE html>"
        assert "<html" in all_text, "Missing <html>"
        assert "<head>" in all_text, "Missing <head>"
        assert "<body>" in all_text, "Missing <body>"
        assert "</html>" in all_text, "Missing </html>"

        print("3. Testing reorder and submit evaluation...")
        eval_res = page.evaluate("""
            () => {
                const target = document.getElementById('seq-test-container');
                const list = target.querySelector('.sequence-list');
                const submitBtn = target.querySelector('.btn-primary');

                // Sort items by data-orig-idx into perfect 0, 1, 2, 3, 4 order
                const items = Array.from(list.querySelectorAll('.seq-item'));
                items.sort((a, b) => parseInt(a.getAttribute('data-orig-idx')) - parseInt(b.getAttribute('data-orig-idx')));
                items.forEach(item => list.appendChild(item));

                // Click submit
                submitBtn.click();

                // Select confidence 'sure'
                const sureBtn = document.querySelector('.confidence-row button[data-conf="sure"]');
                if (sureBtn) sureBtn.click();

                const correctCount = list.querySelectorAll('.seq-item.correct-pos').length;
                return { correctCount };
            }
        """)

        print(f"   Correct items after sequence solved: {eval_res['correctCount']}/5")
        assert eval_res['correctCount'] == 5, "Expected all 5 items to be correct-pos!"

        print(f"4. Checking console errors: {console_errors}")
        assert len(console_errors) == 0, f"Console errors: {console_errors}"

        print("\nALL SEQUENCING HTML TAG TESTS PASSED WITH 100% SUCCESS!")
        browser.close()

if __name__ == '__main__':
    test_sequencing()
