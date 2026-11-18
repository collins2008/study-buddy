# Study Buddy — Nile University 200L Midterms PWA

A high-performance, offline-capable Progressive Web App (PWA) built specifically for Nile University 200-Level First Semester students.

---

## 📱 Features

- **100% Offline Capable**: Built with standard Service Workers and IndexedDB. Once loaded or cached, works anywhere without internet.
- **Mobile-First & Installable**: Add to home screen on iOS (Safari Share ➔ Add to Home Screen) and Android (Chrome Install App banner).
- **18 Exam Question Renderers**:
  - Multiple Choice (MCQ) & Multi-Select
  - True/False with Justification
  - Text Input with Fuzzy Matching & Normalization
  - Cloze (Fill-in-the-Blanks)
  - Interactive Term-Definition Matching
  - Drag / Step Sequencing
  - Leitner / SM-2 Spaced Repetition Flashcards
  - Free-Text Explanations with Self-Grading Checklists
  - Multi-Part Case Study Scenarios
  - Code Output, Code Bug, Code Fill & Monospace Code Writing
  - Sandboxed HTML/CSS Live Rendering
  - Calculation with Tolerance
- **Spaced Repetition (SM-2)**: Smart review queues that automatically schedule wrong answers sooner and mastered concepts later.
- **Weak Spots & Blind Spot Hunter**: Highlights "confidently wrong" questions where you marked *Sure* but answered incorrectly.
- **Mock Exam Simulator**: Timed, scored tests mimicking real exam constraints with per-topic performance breakdowns.
- **Gamified Drills**: 3-Lives mode, Boss Battles (Levels 3 & 4 only), and streak tracking.

---

## 🚀 How to Run Locally

Because Service Workers require `http://localhost` or `https://`, run a lightweight local web server:

```powershell
# Navigate into the app folder
cd "c:\Users\Collins Ibilibor\Downloads\Study Buddy\app"

# Start Python's built-in HTTP server on port 8000
python -m http.server 8000
```

Open your browser and visit:
👉 **`http://localhost:8000`**

---

## 🌐 How to Host for Free (For Phone Installation over HTTPS)

To install this app on your phone as a native PWA, it must be served over HTTPS.

### Option A: GitHub Pages (Recommended, 2 Minutes)
1. Initialize a git repository in the `app` folder (or push this repo to GitHub).
2. Go to your GitHub repository **Settings** ➔ **Pages**.
3. Under **Branch**, select `main` (or root) and click **Save**.
4. GitHub will give you a free HTTPS URL: `https://<your-username>.github.io/<repo-name>/`.
5. Open that link on your phone in Safari (iOS) or Chrome (Android) and tap **Add to Home Screen / Install**.

### Option B: Netlify Drop (Instant, No Git Required)
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag and drop the `app` folder into the upload box.
3. Netlify will instantly provide a live HTTPS URL (e.g., `https://friendly-studybuddy.netlify.app`).
4. Open the link on your phone and install!

---

## 🧩 Adding New Content & Topics

Content is strictly decoupled from app code:
1. All course metadata and topic paths live in `app/content/index.json`.
2. Each topic has its own JSON file at `app/content/<course_code>/<topic_slug>.json`.
3. To validate question structure and verify that all schemas conform:
   ```powershell
   python validate_content.py
   ```
