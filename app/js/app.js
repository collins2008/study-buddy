// app.js — Main Application Controller for Study Buddy PWA

const App = {
  contentCache: {},
  contentIndex: null,

  init: async function() {
    // 1. Initialize DB
    await DB.openDB();
    await DB.updateStreak();

    // 2. Register Service Worker for offline PWA
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('./sw.js').then((reg) => {
        reg.update();
        setTimeout(() => this.cacheAllContent(), 1200);
      }).catch(err => {
        console.warn('SW registration failed:', err);
      });
    }

    // 3. Setup UI bindings
    this.setupTheme();
    this.setupMenu();
    this.setupImport();

    // 4. Init Router
    Router.init();
    const hash = window.location.hash.replace('#', '') || 'home';
    Router.navigate(hash, {}, false);
  },

  // Content Loader (loads index.json and topic files)
  getContentIndex: async function() {
    if (this.contentIndex) return this.contentIndex;
    try {
      const res = await fetch('content/index.json');
      if (!res.ok) throw new Error('Failed to load content index');
      this.contentIndex = await res.json();
    } catch (e) {
      console.warn('Loading fallback empty index:', e);
      this.contentIndex = { courses: [] };
    }
    return this.contentIndex;
  },

  loadTopicContent: async function(courseCode, topicSlug) {
    const key = `${courseCode}/${topicSlug}`;
    if (this.contentCache[key]) return this.contentCache[key];
    try {
      const res = await fetch(`content/${courseCode}/${topicSlug}.json`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      this.contentCache[key] = data;
      return data;
    } catch (e) {
      console.warn(`Failed loading topic ${key}:`, e);
      return { questions: [], case_studies: [] };
    }
  },

  loadAllQuestionsForCourse: async function(courseCode) {
    const index = await this.getContentIndex();
    const course = (index.courses || []).find(c => c.code === courseCode);
    if (!course) return [];

    let allQuestions = [];
    for (const t of course.topics) {
      const topicData = await this.loadTopicContent(courseCode, t.slug);
      const qs = topicData.questions || [];
      allQuestions = allQuestions.concat(qs);
      for (const cs of topicData.case_studies || []) {
        for (const sq of cs.sub_questions || []) {
          allQuestions.push({
            ...sq,
            scenario: cs.scenario
          });
        }
      }
    }
    return allQuestions;
  },

  loadQuestionsForPractice: async function(courseCode, topicSlug, diffFilter, limit = 20, typeFilter = 'all') {
    let pool = [];
    if (topicSlug && topicSlug !== 'all') {
      const topicData = await this.loadTopicContent(courseCode, topicSlug);
      pool = topicData.questions || [];
      // Also flatten case studies sub-questions if needed
      (topicData.case_studies || []).forEach(cs => {
        pool.push({ ...cs, type: 'case_study' });
      });
    } else {
      pool = await this.loadAllQuestionsForCourse(courseCode);
    }

    if (diffFilter && diffFilter !== 'all') {
      const targetDiff = parseInt(diffFilter);
      pool = pool.filter(q => q.difficulty === targetDiff);
    }

    // Filter by question format / type
    if (typeFilter && typeFilter !== 'all') {
      if (typeFilter === 'written') {
        const writtenTypes = new Set(['type_answer', 'explain', 'code_write', 'calculation', 'cloze', 'code_fill']);
        pool = pool.filter(q => writtenTypes.has(q.type));
      } else if (typeFilter === 'mcq') {
        const mcqTypes = new Set(['mcq', 'multi_select', 'true_false_why']);
        pool = pool.filter(q => mcqTypes.has(q.type));
      } else if (typeFilter === 'flashcard') {
        pool = pool.filter(q => q.type === 'flashcard');
      } else if (typeFilter === 'code') {
        const codeTypes = new Set(['code_output', 'code_bug', 'code_fill', 'code_write', 'code_trace']);
        pool = pool.filter(q => codeTypes.has(q.type));
      } else if (typeFilter === 'case_study') {
        pool = pool.filter(q => q.type === 'case_study');
      } else {
        pool = pool.filter(q => q.type === typeFilter);
      }
    }

    // Deduplicate pool by question ID
    const seen = new Set();
    const uniquePool = pool.filter(q => {
      if (!q.id || seen.has(q.id)) return false;
      seen.add(q.id);
      return true;
    });

    // Shuffle pool
    const shuffled = [...uniquePool].sort(() => Math.random() - 0.5);
    return shuffled.slice(0, limit);
  },

  loadQuestionsByType: async function(courseCode, qType) {
    const pool = await this.loadAllQuestionsForCourse(courseCode);
    const seen = new Set();
    return pool.filter(q => {
      if (!q.id || seen.has(q.id)) return false;
      seen.add(q.id);
      return q.type === qType;
    });
  },

  loadMockQuestions: async function(courseCode, count = 40) {
    const rawPool = await this.loadAllQuestionsForCourse(courseCode);
    const seen = new Set();
    const pool = rawPool.filter(q => {
      if (!q.id || seen.has(q.id)) return false;
      seen.add(q.id);
      return true;
    });

    // Weighted selection: prioritize L3 & L4 (at least 40%)
    const highDiff = pool.filter(q => (q.difficulty || 1) >= 3);
    const lowDiff = pool.filter(q => (q.difficulty || 1) < 3);

    const highCount = Math.min(Math.round(count * 0.45), highDiff.length);
    const lowCount = count - highCount;

    const selectedHigh = [...highDiff].sort(() => Math.random() - 0.5).slice(0, highCount);
    const selectedLow = [...lowDiff].sort(() => Math.random() - 0.5).slice(0, lowCount);

    return [...selectedHigh, ...selectedLow].sort(() => Math.random() - 0.5);
  },

  getQuestionsByIds: async function(ids) {
    const index = await this.getContentIndex();
    const idSet = new Set(ids);
    let matched = [];

    for (const c of (index.courses || [])) {
      for (const t of c.topics) {
        const topicData = await this.loadTopicContent(c.code, t.slug);
        (topicData.questions || []).forEach(q => {
          if (idSet.has(q.id)) matched.push(q);
        });
      }
    }
    return matched;
  },

  getRandomQuestionPool: async function(limit = 30) {
    const index = await this.getContentIndex();
    let all = [];
    for (const c of (index.courses || [])) {
      const courseQs = await this.loadAllQuestionsForCourse(c.code);
      all = all.concat(courseQs);
    }
    return [...all].sort(() => Math.random() - 0.5).slice(0, limit);
  },

  getBossQuestions: async function(limit = 20) {
    const all = await this.getRandomQuestionPool(100);
    const hard = all.filter(q => (q.difficulty || 1) >= 3);
    return hard.slice(0, limit);
  },

  cacheAllContent: async function() {
    const index = await this.getContentIndex();
    const urlsToCache = ['content/index.json'];

    for (const c of (index.courses || [])) {
      for (const t of c.topics) {
        urlsToCache.push(`content/${c.code}/${t.slug}.json`);
      }
      if (c.mock_file) urlsToCache.push(`content/${c.mock_file}`);
      if (c.cheatsheet_file) urlsToCache.push(`content/${c.cheatsheet_file}`);
    }

    if (navigator.serviceWorker && navigator.serviceWorker.controller) {
      navigator.serviceWorker.controller.postMessage({
        type: 'CACHE_CONTENT',
        urls: urlsToCache
      });
    }
    if ('caches' in window) {
      try {
        const cache = await caches.open('studybuddy-content-v1');
        await Promise.all(urlsToCache.map(u => cache.add(u).catch(() => null)));
      } catch (e) {
        // Cached in background
      }
    }
  },

  // UI Handlers: Theme, Menu, Toast, Flags
  setupTheme: function() {
    const saved = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', saved);
    const themeBtn = document.getElementById('btn-theme');
    themeBtn.textContent = saved === 'dark' ? '☀️' : '🌙';

    themeBtn.onclick = () => {
      const cur = document.documentElement.getAttribute('data-theme');
      const next = cur === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      themeBtn.textContent = next === 'dark' ? '☀️' : '🌙';
    };
  },

  setupMenu: function() {
    const menuBtn = document.getElementById('btn-menu');
    const menuCloseBtn = document.getElementById('btn-menu-close');
    const overlay = document.getElementById('menu-overlay');
    const sideMenu = document.getElementById('side-menu');

    const openMenu = () => {
      sideMenu.classList.remove('hidden');
      overlay.classList.remove('hidden');
      setTimeout(() => sideMenu.classList.add('open'), 10);
    };

    const closeMenu = () => {
      sideMenu.classList.remove('open');
      setTimeout(() => {
        sideMenu.classList.add('hidden');
        overlay.classList.add('hidden');
      }, 250);
    };

    this.closeMenu = closeMenu;

    menuBtn.onclick = openMenu;
    menuCloseBtn.onclick = closeMenu;
    overlay.onclick = closeMenu;
  },

  setupImport: function() {
    const fileInput = document.getElementById('import-file');
    document.querySelector('.menu-item[data-action="import"]').onclick = () => {
      this.closeMenu();
      fileInput.click();
    };

    fileInput.onchange = async (e) => {
      const file = e.target.files[0];
      if (!file) return;
      try {
        const text = await file.text();
        const json = JSON.parse(text);
        await DB.importProgress(json);
        this.showToast('Progress imported successfully!');
        Router.navigate('home');
      } catch (err) {
        alert('Failed to import progress: ' + err.message);
      }
      fileInput.value = '';
    };
  },

  showToast: function(msg) {
    const toast = document.getElementById('toast');
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(this._toastTimer);
    this._toastTimer = setTimeout(() => {
      toast.classList.remove('show');
    }, 2800);
  },

  promptReport: function(questionId) {
    const note = prompt(`Report issue with question ${questionId} (e.g. ambiguity, typo, wrong key):`);
    if (note !== null) {
      DB.addFlag(questionId, note);
      this.showToast('Report saved! Thank you.');
    }
  }
};

window.App = App;
window.addEventListener('DOMContentLoaded', () => App.init());
