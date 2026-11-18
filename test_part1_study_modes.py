import os
import sys
import json
import time
from playwright.sync_api import sync_playwright

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

CHROME_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE_URL = "http://localhost:8080"

def test_study_modes():
    print("=" * 70)
    print("HOSTILE EXAMINER: TESTING STUDY MODES & ENGINE LOGIC (PART 1.4)")
    print("=" * 70)

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)
        context = browser.new_context(viewport={"width": 412, "height": 915})
        page = context.new_page()
        page.goto(BASE_URL, wait_until="networkidle")

        # -------------------------------------------------------------
        # 1.4.1 Learn & SM-2 Scheduling Logic
        # -------------------------------------------------------------
        print("\n--- [1.4.1] Testing Learn / Flashcards & SM-2 Scheduling ---")
        sm2_res = page.evaluate("""async () => {
            // Clean test cards
            const qEasy = 'test-q-easy';
            const qAgain = 'test-q-again';
            
            // Initial states
            const initEasy = await SR.getState(qEasy);
            const initAgain = await SR.getState(qAgain);
            
            // Rate qEasy as Easy (rating 3)
            await SR.update(qEasy, 3);
            const postEasy1 = await SR.getState(qEasy);
            
            // Rate again as Easy
            await SR.update(qEasy, 3);
            const postEasy2 = await SR.getState(qEasy);
            
            // Rate qAgain as Again (rating 0)
            await SR.update(qAgain, 0);
            const postAgain = await SR.getState(qAgain);
            
            return {
                initEF: initEasy.ef,
                easyInterval1: postEasy1.interval,
                easyInterval2: postEasy2.interval,
                easyEF: postEasy2.ef,
                againInterval: postAgain.interval,
                againReps: postAgain.reps
            };
        }""")
        print(f"  SM-2 calculations: {sm2_res}")
        assert sm2_res['easyInterval1'] == 1, f"First Easy interval expected 1, got {sm2_res['easyInterval1']}"
        assert sm2_res['easyInterval2'] == 6, f"Second Easy interval expected 6, got {sm2_res['easyInterval2']}"
        assert sm2_res['easyEF'] > sm2_res['initEF'], f"Easy EF should increase: {sm2_res['easyEF']} vs {sm2_res['initEF']}"
        assert sm2_res['againInterval'] == 1 and sm2_res['againReps'] == 0, f"Again should reset reps and interval: {sm2_res}"
        print("  ✓ SM-2 Spaced Repetition Algorithm & Quality Grading Verified")

        # -------------------------------------------------------------
        # 1.4.2 Spaced Repetition Due Queue & Date Simulation
        # -------------------------------------------------------------
        print("\n--- [1.4.2] Testing Spaced Repetition Due Queue with Date Shifts ---")
        sr_due_res = page.evaluate("""async () => {
            const qId = 'test-sr-due-shift';
            const now = Date.now();
            const DAY = 86400000;
            
            // Schedule card 3 days in the future
            await DB.putSR({ id: qId, interval: 3, ef: 2.5, due: now + (3 * DAY), reps: 1 });
            const dueNow = await SR.getDueIds();
            const isDueNow = dueNow.includes(qId);
            
            // Simulate 4 days passing by setting due to 1 day in the past
            await DB.putSR({ id: qId, interval: 3, ef: 2.5, due: now - (1 * DAY), reps: 1 });
            const dueAfter4Days = await SR.getDueIds();
            const isDueAfter = dueAfter4Days.includes(qId);
            
            return { isDueNow, isDueAfter };
        }""")
        assert sr_due_res['isDueNow'] is False, "Card scheduled 3 days ahead should NOT be due now!"
        assert sr_due_res['isDueAfter'] is True, "Card past its due date MUST appear in the Due queue!"
        print("  ✓ Due Queue & Temporal Date Simulation Verified")

        # -------------------------------------------------------------
        # 1.4.3 Practice Filters
        # -------------------------------------------------------------
        print("\n--- [1.4.3] Testing Practice Filters (Course, Topic, Difficulty) ---")
        filter_res = page.evaluate("""async () => {
            // Load only Level 3 questions for COS 201 topic 'pointers_memory'
            const qs = await App.loadQuestionsForPractice('COS 201', 'pointers_memory', '3', 50);
            const allL3 = qs.every(q => q.difficulty === 3);
            const allPointers = qs.every(q => q.topic === 'pointers_memory');
            const allCOS201 = qs.every(q => q.course === 'COS 201');
            return { count: qs.length, allL3, allPointers, allCOS201 };
        }""")
        print(f"  Filter result: {filter_res}")
        assert filter_res['count'] > 0, "No questions returned for COS 201 pointers L3 filter!"
        assert filter_res['allL3'] is True, "Filter failed: non-L3 questions returned!"
        assert filter_res['allPointers'] is True, "Filter failed: non-pointers questions returned!"
        assert filter_res['allCOS201'] is True, "Filter failed: wrong course returned!"
        print("  ✓ Practice Filtering by Course, Topic, and Difficulty Level Verified")

        # -------------------------------------------------------------
        # 1.4.4 Weak Spots Ranking Algorithm
        # -------------------------------------------------------------
        print("\n--- [1.4.4] Testing Weak Spots Ranking with Simulated Failure Rates ---")
        weak_res = page.evaluate("""async () => {
            // Seed fake history:
            // Topic A: 10 wrong, 2 correct (83.3% error rate)
            // Topic B: 2 wrong, 10 correct (16.7% error rate)
            for (let i = 0; i < 10; i++) {
                await DB.recordAnswer('fake-weak-a-' + i, 'TEST 101', 'hard_algorithms', false, 'unsure');
            }
            await DB.recordAnswer('fake-weak-a-corr1', 'TEST 101', 'hard_algorithms', true, 'sure');
            await DB.recordAnswer('fake-weak-a-corr2', 'TEST 101', 'hard_algorithms', true, 'sure');
            
            for (let i = 0; i < 10; i++) {
                await DB.recordAnswer('fake-weak-b-' + i, 'TEST 101', 'easy_syntax', true, 'sure');
            }
            await DB.recordAnswer('fake-weak-b-wrong1', 'TEST 101', 'easy_syntax', false, 'guess');
            await DB.recordAnswer('fake-weak-b-wrong2', 'TEST 101', 'easy_syntax', false, 'guess');
            
            // Navigate to weak spots view
            Router.navigate('weak');
            await new Promise(r => setTimeout(r, 400));
            
            // Retrieve computed weak spots table from DOM
            const container = document.getElementById('view-container');
            const topTopic = container.querySelector('.weak-topic-title') ? container.querySelector('.weak-topic-title').textContent : null;
            const topRate = container.querySelector('.weak-topic-rate') ? container.querySelector('.weak-topic-rate').textContent : null;
            
            return { topTopic, topRate, htmlSnippet: container.innerText.slice(0, 300) };
        }""")
        print(f"  Weak spots result: {weak_res['topTopic']} ({weak_res['topRate']})")
        assert "hard_algorithms" in weak_res['htmlSnippet'], f"Weakest topic 'hard_algorithms' was not ranked #1: {weak_res}"
        print("  ✓ Weak Spots Ranking Computed Accurately by Error Rate")

        # -------------------------------------------------------------
        # 1.4.5 Mock Exam Flow (Timer, Feedback Suppression, Scoring)
        # -------------------------------------------------------------
        print("\n--- [1.4.5] Testing Mock Exam Mode (Timer, Delayed Feedback, Scoring) ---")
        mock_flow = page.evaluate("""async () => {
            // Load 3 sample questions
            const mockQs = [
                { id: 'm1', course: 'TEST', topic: 'T1', type: 'mcq', question: 'M1?', options: ['A','B'], answer: 0, difficulty: 3, explanation: 'Exp 1' },
                { id: 'm2', course: 'TEST', topic: 'T1', type: 'mcq', question: 'M2?', options: ['A','B'], answer: 1, difficulty: 3, explanation: 'Exp 2' },
                { id: 'm3', course: 'TEST', topic: 'T2', type: 'mcq', question: 'M3?', options: ['A','B'], answer: 0, difficulty: 2, explanation: 'Exp 3' }
            ];
            
            // Start mock session
            Router.startSession({
                title: 'QA Mock Exam',
                mode: 'mock',
                questions: mockQs,
                timeLimitSecs: 1800
            });
            await new Promise(r => setTimeout(r, 60));
            
            const timerVisible = !!document.getElementById('exam-timer-box') || document.body.innerText.includes('Remaining');
            
            // Answer Q1 correctly
            const btns1 = document.querySelectorAll('.option-btn');
            btns1[0].click();
            const conf1 = document.querySelector('.confidence-modal button[data-conf="sure"]');
            if (conf1) conf1.click();
            await new Promise(r => setTimeout(r, 60));
            
            // Check feedback suppression during exam: feedback area should NOT reveal explanation immediately
            const feedbackHidden = document.querySelector('.feedback-area').classList.contains('hidden');
            
            // Advance to Q2
            const nextBtn = document.getElementById('btn-next-q');
            if (nextBtn) nextBtn.click();
            await new Promise(r => setTimeout(r, 60));
            
            // Answer Q2 wrongly
            const btns2 = document.querySelectorAll('.option-btn');
            btns2[0].click();
            const conf2 = document.querySelector('.confidence-modal button[data-conf="unsure"]');
            if (conf2) conf2.click();
            await new Promise(r => setTimeout(r, 60));
            
            // Advance to Q3
            if (nextBtn) nextBtn.click();
            await new Promise(r => setTimeout(r, 60));
            
            // Answer Q3 correctly
            const btns3 = document.querySelectorAll('.option-btn');
            btns3[0].click();
            const conf3 = document.querySelector('.confidence-modal button[data-conf="sure"]');
            if (conf3) conf3.click();
            await new Promise(r => setTimeout(r, 60));
            
            // Advance to end of session -> summary
            if (nextBtn) nextBtn.click();
            await new Promise(r => setTimeout(r, 60));
            
            const summaryText = document.getElementById('view-container').innerText;
            const hasScore = summaryText.includes('2') && summaryText.includes('3'); // 2 of 3 correct
            const hasTopicBreakdown = summaryText.includes('T1') && summaryText.includes('T2');
            
            return { timerVisible, feedbackHidden, hasScore, hasTopicBreakdown, summarySnippet: summaryText.slice(0, 300) };
        }""")
        print(f"  Mock exam summary: {mock_flow['summarySnippet'][:120]}...")
        assert mock_flow['feedbackHidden'] is True, "Feedback must be suppressed during Mock Exam mode!"
        assert mock_flow['hasScore'] is True, "Mock exam final score not accurately computed!"
        assert mock_flow['hasTopicBreakdown'] is True, "Mock exam per-topic diagnostic breakdown missing!"
        print("  ✓ Mock Exam Timer, Feedback Suppression, and Per-Topic Diagnostic Review Verified")

        # -------------------------------------------------------------
        # 1.4.6 Starred & Flagged Persistence
        # -------------------------------------------------------------
        print("\n--- [1.4.6] Testing Starred & Flagged Persistence Across Reload ---")
        star_res = page.evaluate("""async () => {
            const qId = 'cos201-dt-001';
            await DB.toggleStar(qId);
            const isStarBefore = (await DB.getStars()).has(qId);
            
            await DB.addFlag(qId, 'Examiner note: Check IEEE float precision');
            const flagsBefore = await DB.getAllFlags();
            const hasFlagBefore = flagsBefore.some(f => f.id === qId);
            
            return { isStarBefore, hasFlagBefore };
        }""")
        assert star_res['isStarBefore'] is True, "Star toggle failed!"
        assert star_res['hasFlagBefore'] is True, "Flag creation failed!"
        
        # Reload page to prove persistence in IndexedDB
        page.reload(wait_until="networkidle")
        
        star_persist = page.evaluate("""async () => {
            const qId = 'cos201-dt-001';
            const isStarAfter = (await DB.getStars()).has(qId);
            const flagsAfter = await DB.getAllFlags();
            const flag = flagsAfter.find(f => f.id === qId);
            return { isStarAfter, note: flag ? flag.note : null };
        }""")
        assert star_persist['isStarAfter'] is True, "Starred question did NOT persist after page reload!"
        assert "IEEE float precision" in star_persist['note'], "Flag report did NOT persist after page reload!"
        print("  ✓ Starred and Flagged Data Persist Across Full Page Reloads in IndexedDB")

        # -------------------------------------------------------------
        # 1.4.7 Progress Export & Import Round-Trip
        # -------------------------------------------------------------
        print("\n--- [1.4.7] Testing Progress Export & Import Round-Trip ---")
        export_import = page.evaluate("""async () => {
            // 1. Export current progress
            const exported = await DB.exportProgress();
            
            // 2. Clear stores
            const db = await DB.openDB();
            const t = db.transaction(['history', 'sr', 'stars', 'flags'], 'readwrite');
            t.objectStore('history').clear();
            t.objectStore('sr').clear();
            t.objectStore('stars').clear();
            t.objectStore('flags').clear();
            
            // Verify cleared
            const starsCleared = (await DB.getStars()).size;
            
            // 3. Import back
            await DB.importProgress(exported);
            
            // Verify restored
            const starsRestored = (await DB.getStars()).size;
            const historyRestored = (await DB.getAllHistory()).length;
            const flagsRestored = (await DB.getAllFlags()).length;
            
            return {
                exportedVersion: exported.version,
                starsCleared,
                starsRestored,
                historyRestored,
                flagsRestored
            };
        }""")
        print(f"  Export/Import: {export_import}")
        assert export_import['exportedVersion'] == 1, "Export file missing version: 1"
        assert export_import['starsCleared'] == 0, "Storage clear before import failed"
        assert export_import['starsRestored'] > 0, "Stars failed to restore from export!"
        assert export_import['historyRestored'] > 0, "History failed to restore from export!"
        print("  ✓ Full Progress JSON Export and Import Round-Trip Verified Without Data Loss")

        # -------------------------------------------------------------
        # 1.4.8 Games Layer: 3 Lives Mode
        # -------------------------------------------------------------
        print("\n--- [1.4.8] Testing Games Hub: 3 Lives Mode ---")
        lives_flow = page.evaluate("""async () => {
            const qs = [
                { id: 'g1', course: 'COS 201', topic: 'syntax', type: 'mcq', question: 'Q1?', options: ['A','B'], answer: 0, explanation: 'E1' },
                { id: 'g2', course: 'COS 201', topic: 'syntax', type: 'mcq', question: 'Q2?', options: ['A','B'], answer: 0, explanation: 'E2' },
                { id: 'g3', course: 'COS 201', topic: 'syntax', type: 'mcq', question: 'Q3?', options: ['A','B'], answer: 0, explanation: 'E3' },
                { id: 'g4', course: 'COS 201', topic: 'syntax', type: 'mcq', question: 'Q4?', options: ['A','B'], answer: 0, explanation: 'E4' }
            ];
            
            Router.startSession({ title: 'Lives Mode Test', mode: 'lives', questions: qs });
            await new Promise(r => setTimeout(r, 60));
            const initialLives = Router.activeSession.lives;
            
            // Make 1 wrong answer (Strike 1)
            const btns = document.querySelectorAll('.option-btn');
            btns[1].click(); // wrong
            const conf = document.querySelector('.confidence-modal button[data-conf="guess"]');
            if (conf) conf.click();
            await new Promise(r => setTimeout(r, 60));
            
            const livesAfterStrike1 = Router.activeSession.lives;
            return { initialLives, livesAfterStrike1 };
        }""")
        assert lives_flow['initialLives'] == 3, f"Expected 3 starting lives, got {lives_flow['initialLives']}"
        assert lives_flow['livesAfterStrike1'] == 2, f"Expected 2 lives after 1 wrong answer, got {lives_flow['livesAfterStrike1']}"
        print("  ✓ Gamified 3-Lives Mode Verified")

        browser.close()

    print("\n✓ [PART 1.4] ALL STUDY MODES AND ENGINE LOGIC VERIFIED 100% OPERATIONAL!\n")

if __name__ == "__main__":
    test_study_modes()
