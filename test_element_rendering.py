import time
import sys
import io

sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

def test_rendering():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 390, "height": 844})
        page = context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        print("1. Loading Study Buddy app...")
        page.goto("http://localhost:8080/index.html")
        page.wait_for_selector(".course-card")
        time.sleep(0.5)

        print("2. Testing exact question from user screenshot: ift203-hs-fc07")
        # Injected question test using Renderers directly in app context
        res = page.evaluate("""
            async () => {
                const target = document.createElement('div');
                target.id = 'test-fc-container';
                document.getElementById('view-container').prepend(target);

                // Fetch real question from content
                const resp = await fetch('content/IFT 203/html_structure_semantics.json');
                const data = await resp.json();
                const q = data.questions.find(item => item.id === 'ift203-hs-fc07');

                await Renderers.renderQuestion(q, target, () => {});

                const frontText = target.querySelector('.flashcard-front').innerText;
                const frontHtml = target.querySelector('.flashcard-front').innerHTML;
                const promptDiv = target.querySelector('.q-question');

                return {
                    hasPromptDiv: !!promptDiv,
                    frontText,
                    frontHtml,
                    containsHeadTag: frontHtml.includes('&lt;head&gt;') || frontHtml.includes('<code>&lt;head&gt;</code>'),
                    containsBodyTag: frontHtml.includes('&lt;body&gt;') || frontHtml.includes('<code>&lt;body&gt;</code>')
                };
            }
        """)

        print(f"   Prompt Div Present (should be False): {res['hasPromptDiv']}")
        print(f"   Front Text: {res['frontText']}")
        print(f"   Contains Escaped Head Tag: {res['containsHeadTag']}")
        print(f"   Contains Escaped Body Tag: {res['containsBodyTag']}")

        assert res['hasPromptDiv'] is False, "Flashcard should not have duplicate promptDiv above card"
        assert "<head>" in res['frontText'], "Front text must visibly contain '<head>'"
        assert "<body>" in res['frontText'], "Front text must visibly contain '<body>'"
        assert res['containsHeadTag'] is True, "HTML must contain escaped <head> code tag"
        assert res['containsBodyTag'] is True, "HTML must contain escaped <body> code tag"

        print("3. Testing card flip and back content...")
        flip_res = page.evaluate("""
            () => {
                const target = document.getElementById('test-fc-container');
                const wrapper = target.querySelector('.flashcard-wrapper');
                wrapper.click(); // flip card

                const backText = target.querySelector('.flashcard-back').innerText;
                const backHtml = target.querySelector('.flashcard-back').innerHTML;

                return {
                    isFlipped: target.querySelector('.flashcard-inner').classList.contains('flipped'),
                    backText,
                    containsHeadInBack: backText.includes('<head>'),
                    containsBodyInBack: backText.includes('<body>')
                };
            }
        """)
        print(f"   Card is flipped: {flip_res['isFlipped']}")
        print(f"   Back contains <head>: {flip_res['containsHeadInBack']}")
        print(f"   Back contains <body>: {flip_res['containsBodyInBack']}")

        assert flip_res['isFlipped'] is True
        assert flip_res['containsHeadInBack'] is True, "Back of flashcard must display <head>"
        assert flip_res['containsBodyInBack'] is True, "Back of flashcard must display <body>"

        print("4. Testing MCQ with raw HTML / C header tags in options & explanations...")
        mcq_res = page.evaluate("""
            async () => {
                const target = document.createElement('div');
                target.id = 'test-mcq-container';
                document.getElementById('view-container').prepend(target);

                const testQ = {
                    id: 'test-q-tags',
                    course: 'COS 201',
                    type: 'mcq',
                    difficulty: 2,
                    question: 'Which header file provides \`<stdio.h>\` functions like \`printf()\` and compares if \`x < 10 && y > 2\`?',
                    options: [
                        '\`<stdio.h>\` Standard Input Output',
                        '\`<stdlib.h>\` Standard Utility Library',
                        '\`<math.h>\` Math Functions',
                        '\`<string.h>\` String Functions'
                    ],
                    answer: 0,
                    explanation: 'The \`<stdio.h>\` header defines I/O operations such as \`printf()\` and \`scanf()\`. Conditions like \`x < 10 && y > 2\` are boolean expressions.',
                    why_wrong: {
                        "1": "\`<stdlib.h>\` provides memory allocation and conversion routines.",
                        "2": "\`<math.h>\` provides trigonometric and power functions.",
                        "3": "\`<string.h>\` provides string manipulation functions."
                    }
                };

                await Renderers.renderQuestion(testQ, target, () => {});

                const qText = target.querySelector('.q-question').innerText;
                const optA = target.querySelectorAll('.option-btn')[0].innerText;
                const optB = target.querySelectorAll('.option-btn')[1].innerText;

                // Click wrong option B to trigger feedback
                target.querySelectorAll('.option-btn')[1].click();

                // Select confidence rating
                const sureBtn = document.querySelector('.confidence-row button[data-conf="sure"]');
                if (sureBtn) sureBtn.click();

                const feedbackText = target.querySelector('.feedback-area').innerText;

                return {
                    qText,
                    optA,
                    optB,
                    feedbackText
                };
            }
        """)

        print(f"   MCQ Question Text: {mcq_res['qText']}")
        print(f"   Option A Text: {mcq_res['optA']}")
        print(f"   Option B Text: {mcq_res['optB']}")
        print(f"   Feedback Text Preview: {mcq_res['feedbackText'][:120]}...")

        assert "<stdio.h>" in mcq_res['qText'], "MCQ Question must contain <stdio.h>"
        assert "x < 10 && y > 2" in mcq_res['qText'], "MCQ Question must contain x < 10 && y > 2"
        assert "<stdio.h>" in mcq_res['optA'], "Option A must contain <stdio.h>"
        assert "<stdlib.h>" in mcq_res['optB'], "Option B must contain <stdlib.h>"
        assert "<stdlib.h>" in mcq_res['feedbackText'], "Why wrong explanation must display <stdlib.h>"

        print(f"5. Checking console errors: {console_errors}")
        assert len(console_errors) == 0, f"Console errors detected: {console_errors}"

        print("\nALL RENDERING AND SANITIZATION TESTS PASSED PERFECTLY!")
        browser.close()

if __name__ == '__main__':
    test_rendering()
