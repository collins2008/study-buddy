// router.js — Client-Side View Manager for Study Buddy
// Handles view transitions, filters, study sessions, and history state

const Router = {
  currentView: 'home',
  activeSession: null,

  init: function() {
    window.addEventListener('popstate', (e) => {
      const hash = window.location.hash.replace('#', '') || 'home';
      this.navigate(hash, (e.state && e.state.params) || {}, false);
    });

    document.querySelectorAll('.menu-item[data-view]').forEach(item => {
      item.onclick = () => {
        const view = item.getAttribute('data-view');
        App.closeMenu();
        this.navigate(view);
      };
    });

    document.getElementById('btn-back').onclick = () => {
      if (this.currentView === 'home') return;
      this.navigate('home');
    };
  },

  navigate: function(viewInput, params = {}, push = true) {
    let view = viewInput;
    if (typeof viewInput === 'string' && viewInput.includes('?')) {
      const parts = viewInput.split('?');
      view = parts[0];
      const searchParams = new URLSearchParams(parts[1]);
      const parsed = {};
      for (const [k, v] of searchParams.entries()) {
        parsed[k] = v;
      }
      params = { ...parsed, ...params };
    }

    this.currentView = view;
    if (push) {
      const query = params && Object.keys(params).length ? '?' + new URLSearchParams(params).toString() : '';
      history.pushState({ view, params }, '', `#${view}${query}`);
    }

    const backBtn = document.getElementById('btn-back');
    const titleEl = document.getElementById('app-title');
    const container = document.getElementById('view-container');

    if (view === 'home') {
      backBtn.hidden = true;
      titleEl.textContent = 'Study Buddy';
      this.renderHome(container);
    } else {
      backBtn.hidden = false;
      switch (view) {
        case 'course':
          this.renderCourseDetail(container, params.code);
          break;
        case 'practice':
          this.renderPracticeSetup(container, params);
          break;
        case 'session':
          this.renderSession(container, params);
          break;
        case 'learn':
          this.renderLearnSetup(container, params);
          break;
        case 'spaced':
          this.renderSpacedQueue(container);
          break;
        case 'weak':
          this.renderWeakSpots(container);
          break;
        case 'starred':
          this.renderStarredQueue(container);
          break;
        case 'mock':
          this.renderMockSetup(container, params);
          break;
        case 'games':
          this.renderGamesHub(container);
          break;
        case 'stats':
          this.renderStats(container);
          break;
        case 'flags':
          this.renderFlags(container);
          break;
        case 'export':
          this.renderExport(container);
          break;
        case 'offline':
          this.renderOffline(container);
          break;
        default:
          this.renderHome(container);
      }
    }
    window.scrollTo(0, 0);
  },

  // 1. HOME VIEW
  renderHome: async function(container) {
    container.innerHTML = '<div class="spinner"></div>';
    const index = await App.getContentIndex();
    const dueCount = await SR.getDueCount();
    const streak = await DB.getStreak();
    const goal = await DB.getDailyGoalProgress();

    // Update streak header
    const streakBar = document.getElementById('streak-bar');
    streakBar.hidden = false;
    document.body.classList.add('has-streak');
    document.getElementById('streak-count').textContent = streak;
    document.getElementById('goal-done').textContent = goal.done;
    document.getElementById('goal-total').textContent = goal.goal;

    let coursesHtml = '';
    for (const c of (index.courses || [])) {
      // Calculate course mastery
      const qIds = c.topics.flatMap(t => t.question_ids || []);
      const mastery = qIds.length ? await SR.getMastery(qIds) : 0;

      coursesHtml += `
        <div class="card course-card" data-code="${c.code}">
          <div class="course-card-header">
            <div class="course-icon" style="background:${c.color || 'var(--primary)'}22; color:${c.color || 'var(--primary)'}">
              ${c.icon || '📚'}
            </div>
            <div class="course-info">
              <span class="course-code">${c.code}</span>
              <h3 class="course-name">${c.title}</h3>
              <span class="course-type">${c.type}</span>
            </div>
          </div>
          <div class="progress-bar">
            <div class="progress-fill" style="width:${mastery}%"></div>
          </div>
          <div class="course-stats">
            <span class="stat-pill">📈 <strong>${mastery}%</strong> mastery</span>
            <span class="stat-pill">📖 <strong>${c.topics.length}</strong> topics</span>
            <span class="stat-pill">❓ <strong>${c.total_questions || 0}</strong> Qs</span>
          </div>
        </div>
      `;
    }

    container.innerHTML = `
      <div class="fade-in">
        ${dueCount > 0 ? `
          <div class="card mb-md flex" style="background:rgba(255,107,157,0.12); border-color:var(--accent); align-items:center; justify-content:space-between;">
            <div>
              <div style="font-weight:700; color:var(--accent);">⏰ ${dueCount} questions due for review today</div>
              <div class="text-sm text-muted">Spaced repetition queue is waiting for you</div>
            </div>
            <button class="btn btn-sm btn-warn" id="btn-start-due">Review Now</button>
          </div>
        ` : ''}

        <div class="flex" style="justify-content:space-between; align-items:center; margin-bottom:16px;">
          <h2 class="section-title">My Courses</h2>
          <button class="btn btn-sm btn-secondary" id="btn-quick-weak">🎯 Practice Weak Spots</button>
        </div>

        <div class="card-grid">
          ${coursesHtml || '<div class="empty-state">No courses loaded in content index.</div>'}
        </div>
      </div>
    `;

    container.querySelectorAll('.course-card').forEach(card => {
      card.onclick = () => {
        const code = card.getAttribute('data-code');
        this.navigate('course', { code });
      };
    });

    const dueBtn = container.querySelector('#btn-start-due');
    if (dueBtn) dueBtn.onclick = () => this.navigate('spaced');

    const weakBtn = container.querySelector('#btn-quick-weak');
    if (weakBtn) weakBtn.onclick = () => this.navigate('weak');
  },

  // 2. COURSE DETAIL VIEW
  renderCourseDetail: async function(container, code) {
    container.innerHTML = '<div class="spinner"></div>';
    const index = await App.getContentIndex();
    const course = (index.courses || []).find(c => c.code === code);
    if (!course) {
      container.innerHTML = '<div class="empty-state">Course not found.</div>';
      return;
    }

    document.getElementById('app-title').textContent = `${course.code}: ${course.title}`;

    let topicsHtml = '';
    for (const t of course.topics) {
      const qIds = t.question_ids || [];
      const mastery = qIds.length ? await SR.getMastery(qIds) : 0;
      topicsHtml += `
        <div class="topic-item" data-topic="${t.slug}">
          <div class="flex-1">
            <div class="topic-name">${t.title}</div>
            <div class="topic-count">${t.question_count || 0} questions • ${t.has_case_studies ? 'Has scenarios' : 'Standard'}</div>
          </div>
          <span class="topic-mastery" style="color:${mastery > 70 ? 'var(--success)' : (mastery > 30 ? 'var(--warn)' : 'var(--text2)')}">${mastery}%</span>
        </div>
      `;
    }

    container.innerHTML = `
      <div class="fade-in">
        <div class="card mb-md">
          <div class="flex gap-md" style="align-items:center;">
            <div class="course-icon" style="background:${course.color || 'var(--primary)'}22; color:${course.color || 'var(--primary)'}">
              ${course.icon || '📚'}
            </div>
            <div>
              <h2>${course.title}</h2>
              <p class="text-sm text-muted">${course.type} • ${course.topics.length} Topics</p>
            </div>
          </div>
          <div class="flex gap-sm mt-md" style="flex-wrap:wrap;">
            <button class="btn btn-primary btn-sm" id="btn-course-practice">Practice All</button>
            <button class="btn btn-secondary btn-sm" id="btn-course-flashcards">Flashcards</button>
            <button class="btn btn-secondary btn-sm" id="btn-course-mock">Mock Exam</button>
          </div>
        </div>

        <h3 class="section-title">Topics & Modules</h3>
        <div class="topic-list mb-lg">
          ${topicsHtml}
        </div>
      </div>
    `;

    container.querySelectorAll('.topic-item').forEach(item => {
      item.onclick = () => {
        const topicSlug = item.getAttribute('data-topic');
        this.navigate('practice', { course: course.code, topic: topicSlug });
      };
    });

    container.querySelector('#btn-course-practice').onclick = () => {
      this.navigate('practice', { course: course.code });
    };

    container.querySelector('#btn-course-flashcards').onclick = () => {
      this.navigate('learn', { course: course.code });
    };

    container.querySelector('#btn-course-mock').onclick = () => {
      this.navigate('mock', { course: course.code });
    };
  },

  // 3. PRACTICE SETUP VIEW
  renderPracticeSetup: async function(container, params) {
    container.innerHTML = '<div class="spinner"></div>';
    const index = await App.getContentIndex();
    const courses = index.courses || [];
    const selectedCourseCode = params.course || (courses[0] ? courses[0].code : '');
    const course = courses.find(c => c.code === selectedCourseCode);

    document.getElementById('app-title').textContent = 'Practice Mode';

    container.innerHTML = `
      <div class="fade-in q-card">
        <h2 class="section-title">Custom Practice Session</h2>
        <div class="card flex flex-col gap-md">
          <div>
            <label>Select Course:</label>
            <select id="sel-course" class="w-full">
              ${courses.map(c => `<option value="${c.code}" ${c.code === selectedCourseCode ? 'selected' : ''}>${c.code} — ${c.title}</option>`).join('')}
            </select>
          </div>

          <div>
            <label>Select Topic:</label>
            <select id="sel-topic" class="w-full">
              <option value="all">All Topics in Course</option>
              ${course ? course.topics.map(t => `<option value="${t.slug}" ${t.slug === params.topic ? 'selected' : ''}>${t.title}</option>`).join('') : ''}
            </select>
          </div>

          <div>
            <label>Difficulty Filter:</label>
            <div class="filter-row" id="diff-chips">
              <button class="chip active" data-diff="all">All Levels</button>
              <button class="chip" data-diff="1">Level 1 (Recall)</button>
              <button class="chip" data-diff="2">Level 2 (Understand)</button>
              <button class="chip" data-diff="3">Level 3 (Apply)</button>
              <button class="chip" data-diff="4">Level 4 (Analyze)</button>
            </div>
          </div>

          <div>
            <label>Question Count:</label>
            <select id="sel-count" class="w-full">
              <option value="10">10 Questions</option>
              <option value="20" selected>20 Questions</option>
              <option value="40">40 Questions (Full Set)</option>
              <option value="all">All Available</option>
            </select>
          </div>

          <button class="btn btn-primary btn-full mt-sm" id="btn-start-practice">Start Practice ➔</button>
        </div>
      </div>
    `;

    const selCourse = container.querySelector('#sel-course');
    const selTopic = container.querySelector('#sel-topic');
    selCourse.onchange = () => {
      this.navigate('practice', { course: selCourse.value }, false);
    };

    let selectedDiff = 'all';
    container.querySelectorAll('#diff-chips .chip').forEach(chip => {
      chip.onclick = () => {
        container.querySelectorAll('#diff-chips .chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        selectedDiff = chip.getAttribute('data-diff');
      };
    });

    container.querySelector('#btn-start-practice').onclick = async () => {
      const topic = selTopic.value;
      const countVal = container.querySelector('#sel-count').value;
      const count = countVal === 'all' ? 999 : parseInt(countVal);

      const questions = await App.loadQuestionsForPractice(selCourse.value, topic, selectedDiff, count);
      if (!questions.length) {
        App.showToast('No questions matched the selected filters.');
        return;
      }
      this.startSession({
        title: `Practice: ${selCourse.value}`,
        mode: 'practice',
        questions: questions,
        timed: false
      });
    };
  },

  // 4. ACTIVE STUDY SESSION (One Question at a Time)
  startSession: function(sessionConfig) {
    if (this._examTimer) {
      clearInterval(this._examTimer);
      this._examTimer = null;
    }
    this.activeSession = {
      ...sessionConfig,
      currentIndex: 0,
      scores: [],
      startTime: Date.now(),
      lives: sessionConfig.mode === 'lives' ? 3 : null,
      timeLeft: sessionConfig.timeLimitSecs || null
    };
    this.navigate('session', {}, false);
  },

  renderSession: function(container) {
    const s = this.activeSession;
    if (!s || !s.questions || s.currentIndex >= s.questions.length) {
      this.renderSessionSummary(container);
      return;
    }

    const curQ = s.questions[s.currentIndex];
    document.getElementById('app-title').textContent = `${s.title} (${s.currentIndex + 1}/${s.questions.length})`;

    // Format timer
    let timerHtml = '';
    if (s.timeLeft !== null) {
      const min = Math.floor(s.timeLeft / 60);
      const sec = s.timeLeft % 60;
      timerHtml = `
        <div class="exam-timer-pill" id="exam-timer-box" style="display:inline-flex; align-items:center; gap:6px; background:rgba(255,107,107,0.15); border:1px solid var(--danger); padding:4px 12px; border-radius:20px; font-weight:700; margin-bottom:12px;">
          <span>⏱️ Remaining:</span>
          <span id="timer-val">${min}:${sec < 10 ? '0' : ''}${sec}</span>
        </div>
      `;
    }

    container.innerHTML = `
      <div>
        <div class="flex" style="justify-content:space-between; align-items:center;">
          ${timerHtml}
          ${s.lives !== null ? `
            <div class="lives-display">
              ${Array.from({ length: 3 }).map((_, i) => `<span style="opacity:${i < s.lives ? 1 : 0.2}">❤️</span>`).join('')}
            </div>
          ` : ''}
        </div>

        <div class="progress-bar mb-md">
          <div class="progress-fill" style="width:${((s.currentIndex) / s.questions.length) * 100}%"></div>
        </div>

        <div id="q-render-target"></div>

        <div class="mt-md flex gap-md" id="session-controls" style="display:none;">
          <button class="btn btn-primary flex-1" id="btn-next-q">Next Question ➔</button>
        </div>
      </div>
    `;

    // Manage timer interval
    if (s.timeLeft !== null && !this._examTimer) {
      this._examTimer = setInterval(() => {
        if (!this.activeSession || this.activeSession.timeLeft === null) {
          clearInterval(this._examTimer);
          this._examTimer = null;
          return;
        }
        this.activeSession.timeLeft--;
        const min = Math.floor(this.activeSession.timeLeft / 60);
        const sec = this.activeSession.timeLeft % 60;
        const timerEl = document.getElementById('timer-val');
        if (timerEl) timerEl.textContent = `${min}:${sec < 10 ? '0' : ''}${sec}`;
        if (this.activeSession.timeLeft <= 0) {
          clearInterval(this._examTimer);
          this._examTimer = null;
          App.showToast('⏰ Time is up! Exam auto-submitted.');
          this.renderSessionSummary(container);
        }
      }, 1000);
    }

    const target = container.querySelector('#q-render-target');
    const controls = container.querySelector('#session-controls');
    const nextBtn = container.querySelector('#btn-next-q');

    const renderOpts = { examMode: s.mode === 'mock' };
    Renderers.renderQuestion(curQ, target, async (result) => {
      s.scores.push({ questionId: curQ.id, ...result });

      // Record in DB
      await DB.recordAnswer(curQ.id, curQ.course, curQ.topic, result.isCorrect, result.confidence);
      await DB.incrementDailyDone();
      await DB.updateStreak();

      // If wrong, schedule soon in SR
      if (!result.isCorrect) {
        await SR.scheduleSoon(curQ.id);
      }

      // Check lives in games mode
      if (s.lives !== null && !result.isCorrect) {
        s.lives--;
        if (s.lives <= 0) {
          App.showToast('💔 Out of lives!');
          setTimeout(() => this.renderSessionSummary(container), 1500);
          return;
        }
      }

      controls.style.display = 'flex';
      nextBtn.focus();
    }, renderOpts);

    nextBtn.onclick = () => {
      s.currentIndex++;
      this.renderSession(container);
    };
  },

  // 5. SESSION SUMMARY VIEW
  renderSessionSummary: function(container) {
    if (this._examTimer) {
      clearInterval(this._examTimer);
      this._examTimer = null;
    }
    const s = this.activeSession || { scores: [], questions: [] };
    const total = s.scores.length || 1;
    const correctCount = s.scores.filter(r => r.isCorrect).length;
    const pct = Math.round((correctCount / total) * 100);

    // Filter confident wrong
    const confidentWrong = s.scores.filter(r => !r.isCorrect && r.confidence === 'sure');

    // Per-topic breakdown
    const topicStats = {};
    (s.questions || []).forEach(q => {
      const t = q.topic || 'General';
      if (!topicStats[t]) topicStats[t] = { total: 0, correct: 0, course: q.course };
      topicStats[t].total++;
      const matched = s.scores.find(sc => sc.questionId === q.id);
      if (matched && matched.isCorrect) topicStats[t].correct++;
    });

    const topicBreakdownHtml = Object.entries(topicStats).map(([topic, stat]) => {
      const topicPct = stat.total ? Math.round((stat.correct / stat.total) * 100) : 0;
      return `
        <div class="mb-sm text-left">
          <div class="flex" style="justify-content:space-between; font-size:0.85rem; margin-bottom:4px;">
            <span>${topic.replace(/_/g, ' ')}</span>
            <span><strong>${stat.correct}/${stat.total}</strong> (${topicPct}%)</span>
          </div>
          <div class="progress-bar" style="height:6px;">
            <div class="progress-fill" style="width:${topicPct}%; background:${topicPct >= 70 ? 'var(--success)' : (topicPct >= 40 ? 'var(--warn)' : 'var(--danger)')};"></div>
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="q-card fade-in text-center">
        <h2>${s.mode === 'mock' ? 'Exam Scored Review' : 'Session Complete!'}</h2>
        <div class="score-circle" style="--pct:${pct}%">
          <span class="score-number">${pct}%</span>
        </div>
        <p class="text-sm text-muted mb-md">
          Answered <strong>${correctCount} of ${total}</strong> questions correctly (${pct >= 50 ? '✓ PASS' : '✗ NEEDS WORK'})
        </p>

        ${confidentWrong.length > 0 ? `
          <div class="card mb-md text-left" style="border-color:var(--danger); background:rgba(255,71,87,0.08);">
            <h4 style="color:var(--danger);">⚠️ ${confidentWrong.length} Confident Blind Spots</h4>
            <p class="text-sm text-muted">You marked these as "Sure" but were incorrect. Review them in Weak Spots!</p>
          </div>
        ` : ''}

        <div class="card mb-md text-left">
          <h3 class="mb-sm" style="font-size:1rem;">📊 Diagnostic Breakdown by Topic</h3>
          ${topicBreakdownHtml || '<p class="text-sm text-muted">No topic data available</p>'}
        </div>

        <div class="flex gap-md mt-lg">
          <button class="btn btn-secondary flex-1" id="btn-summary-home">Back to Home</button>
          <button class="btn btn-primary flex-1" id="btn-summary-retry">Drill Weak Spots</button>
        </div>
      </div>
    `;

    container.querySelector('#btn-summary-home').onclick = () => this.navigate('home');
    container.querySelector('#btn-summary-retry').onclick = () => this.navigate('weak');
  },

  // 6. LEARN (Flashcards Mode)
  renderLearnSetup: async function(container, params) {
    const questions = await App.loadQuestionsByType(params.course, 'flashcard');
    if (!questions.length) {
      container.innerHTML = `
        <div class="empty-state">
          <h3>No flashcards available for this course yet.</h3>
          <button class="btn btn-secondary mt-md" onclick="Router.navigate('home')">Back to Home</button>
        </div>
      `;
      return;
    }
    this.startSession({
      title: `Flashcards: ${params.course || 'All'}`,
      mode: 'flashcards',
      questions: questions,
      timed: false
    });
  },

  // 7. SPACED REPETITION (Due Queue)
  renderSpacedQueue: async function(container) {
    container.innerHTML = '<div class="spinner"></div>';
    const dueIds = await SR.getDueIds();
    if (!dueIds.length) {
      container.innerHTML = `
        <div class="empty-state fade-in">
          <div class="empty-icon">🎉</div>
          <h3>You're All Caught Up!</h3>
          <p class="mt-sm">No items due right now in your spaced repetition queue.</p>
          <button class="btn btn-primary mt-md" onclick="Router.navigate('practice')">Do Custom Practice</button>
        </div>
      `;
      return;
    }

    const questions = await App.getQuestionsByIds(dueIds);
    this.startSession({
      title: 'Due Today (Spaced Repetition)',
      mode: 'spaced',
      questions: questions,
      timed: false
    });
  },

  // 8. WEAK SPOTS
  renderWeakSpots: async function(container) {
    container.innerHTML = '<div class="spinner"></div>';
    const history = await DB.getAllHistory();

    // Group by Topic
    const topicAgg = {};
    history.forEach(h => {
      const topicKey = h.topic || 'unknown';
      if (!topicAgg[topicKey]) {
        topicAgg[topicKey] = { topic: topicKey, course: h.course, correct: 0, wrong: 0 };
      }
      topicAgg[topicKey].correct += (h.correct || 0);
      topicAgg[topicKey].wrong += (h.wrong || 0);
    });

    const rankedTopics = Object.values(topicAgg)
      .map(t => {
        const total = t.correct + t.wrong;
        const errRate = total > 0 ? Math.round((t.wrong / total) * 100) : 0;
        return { ...t, total, errRate };
      })
      .filter(t => t.total >= 1 && t.errRate > 20)
      .sort((a, b) => b.errRate - a.errRate);

    // Rank individual questions by error rate
    const ranked = history
      .filter(h => (h.correct + h.wrong) > 0)
      .map(h => {
        const total = h.correct + h.wrong;
        const errRate = Math.round((h.wrong / total) * 100);
        return { ...h, total, errRate };
      })
      .filter(h => h.errRate > 25)
      .sort((a, b) => b.errRate - a.errRate);

    if (!ranked.length && !rankedTopics.length) {
      container.innerHTML = `
        <div class="empty-state fade-in">
          <div class="empty-icon">🌟</div>
          <h3>No Weak Spots Detected!</h3>
          <p class="mt-sm">You haven't accumulated high-error questions yet. Keep practicing!</p>
          <button class="btn btn-primary mt-md" onclick="Router.navigate('practice')">Start Practice</button>
        </div>
      `;
      return;
    }

    const topicsHtml = rankedTopics.slice(0, 5).map(t => `
      <div class="card mb-sm flex" style="align-items:center; justify-content:space-between;">
        <div>
          <div class="bold text-sm weak-topic-title">${t.topic.replace(/_/g, ' ')}</div>
          <div class="text-sm text-muted">${t.course || ''} • ${t.wrong} wrong out of ${t.total}</div>
        </div>
        <span class="tag tag-danger weak-topic-rate">${t.errRate}% error</span>
      </div>
    `).join('');

    const itemsHtml = ranked.slice(0, 15).map(r => `
      <div class="weak-item">
        <div style="flex:1;">
          <div class="bold text-sm">${r.id}</div>
          <div class="text-sm text-muted">${r.course || ''} • ${r.topic || ''}</div>
        </div>
        <div class="weak-bar">
          <div class="weak-fill" style="width:${r.errRate}%"></div>
        </div>
        <span class="weak-pct">${r.errRate}% err</span>
      </div>
    `).join('');

    container.innerHTML = `
      <div class="fade-in q-card">
        <h2 class="section-title">Weak Spots & Diagnostics</h2>
        ${rankedTopics.length > 0 ? `
          <div class="mb-lg">
            <h3 class="mb-sm" style="font-size:1rem;">⚠️ High-Error Topics</h3>
            ${topicsHtml}
            <button class="btn btn-primary btn-full mt-sm" id="btn-practice-weakest-topic">
              🎯 Practice Weakest Topic: ${rankedTopics[0].topic.replace(/_/g, ' ')}
            </button>
          </div>
        ` : ''}

        <h3 class="mb-sm" style="font-size:1rem;">📌 High-Error Individual Questions</h3>
        <p class="text-sm text-muted mb-md">Questions where your error rate is highest</p>
        <button class="btn btn-secondary btn-full mb-md" id="btn-drill-weak">Drill My Weakest Questions Now</button>
        <div>${itemsHtml}</div>
      </div>
    `;

    const topicBtn = container.querySelector('#btn-practice-weakest-topic');
    if (topicBtn && rankedTopics.length > 0) {
      topicBtn.onclick = () => {
        const top = rankedTopics[0];
        this.navigate('practice', { course: top.course, topic: top.topic });
      };
    }

    container.querySelector('#btn-drill-weak').onclick = async () => {
      const topIds = ranked.slice(0, 20).map(r => r.id);
      const questions = await App.getQuestionsByIds(topIds);
      this.startSession({
        title: 'Weak Spot Drill',
        mode: 'weak',
        questions: questions,
        timed: false
      });
    };
  },

  // 9. STARRED QUESTIONS
  renderStarredQueue: async function(container) {
    container.innerHTML = '<div class="spinner"></div>';
    const stars = await DB.getStars();
    if (!stars.size) {
      container.innerHTML = `
        <div class="empty-state fade-in">
          <div class="empty-icon">⭐</div>
          <h3>No Starred Questions Yet</h3>
          <p class="mt-sm">Tap the star icon on any question during practice to bookmark it here.</p>
        </div>
      `;
      return;
    }

    const questions = await App.getQuestionsByIds([...stars]);
    this.startSession({
      title: 'Starred Questions',
      mode: 'starred',
      questions: questions,
      timed: false
    });
  },

  // 10. MOCK EXAM
  renderMockSetup: async function(container, params) {
    const index = await App.getContentIndex();
    const courses = index.courses || [];
    const selected = params.course || (courses[0] ? courses[0].code : '');

    container.innerHTML = `
      <div class="fade-in q-card">
        <h2 class="section-title">Simulated Exam (Mock)</h2>
        <div class="card flex flex-col gap-md">
          <div>
            <label>Course:</label>
            <select id="mock-course" class="w-full">
              ${courses.map(c => `<option value="${c.code}" ${c.code === selected ? 'selected' : ''}>${c.code} — ${c.title}</option>`).join('')}
            </select>
          </div>
          <div>
            <label>Exam Length:</label>
            <select id="mock-count" class="w-full">
              <option value="20">20 Questions (30 Minutes)</option>
              <option value="40" selected>40 Questions (60 Minutes) — Midterm Standard</option>
              <option value="60">60 Questions (90 Minutes)</option>
            </select>
          </div>
          <p class="text-sm text-muted">⚠️ Exam mode rules: No instant feedback during the test. Mixed question types weighted toward Apply & Analyze levels.</p>
          <button class="btn btn-danger btn-full mt-sm" id="btn-begin-mock">Begin Timed Exam ➔</button>
        </div>
      </div>
    `;

    container.querySelector('#btn-begin-mock').onclick = async () => {
      const code = container.querySelector('#mock-course').value;
      const count = parseInt(container.querySelector('#mock-count').value);
      const questions = await App.loadMockQuestions(code, count);
      this.startSession({
        title: `MOCK EXAM: ${code}`,
        mode: 'mock',
        questions: questions,
        timeLimitSecs: count === 20 ? 1800 : (count === 40 ? 3600 : 5400)
      });
    };
  },

  // 11. GAMES HUB
  renderGamesHub: function(container) {
    container.innerHTML = `
      <div class="fade-in q-card">
        <h2 class="section-title">🎮 Gamified Revision Hub</h2>
        <div class="card-grid">
          <div class="card game-card" id="game-lives">
            <span style="font-size:2rem;">❤️</span>
            <h3 class="mt-sm">3 Lives Mode</h3>
            <p class="text-sm text-muted mt-sm">Answer as many consecutive questions as possible. 3 mistakes and game over!</p>
            <button class="btn btn-primary btn-sm mt-md">Play Lives Mode</button>
          </div>

          <div class="card game-card" id="game-boss">
            <span style="font-size:2rem;">👾</span>
            <h3 class="mt-sm">Topic Boss Round</h3>
            <p class="text-sm text-muted mt-sm">Only Level 3 & Level 4 difficulty questions. High cognitive challenge.</p>
            <button class="btn btn-danger btn-sm mt-md">Fight Boss</button>
          </div>
        </div>
      </div>
    `;

    container.querySelector('#game-lives').onclick = async () => {
      const qs = await App.getRandomQuestionPool(30);
      this.startSession({ title: 'Lives Mode (3 Strikes)', mode: 'lives', questions: qs });
    };

    container.querySelector('#game-boss').onclick = async () => {
      const qs = await App.getBossQuestions(20);
      this.startSession({ title: 'Boss Battle (Level 3 & 4)', mode: 'boss', questions: qs });
    };
  },

  // 12. STATS & ANALYTICS
  renderStats: async function(container) {
    container.innerHTML = '<div class="spinner"></div>';
    const history = await DB.getAllHistory();
    const streak = await DB.getStreak();
    const flags = await DB.getAllFlags();

    const totalAnswered = history.reduce((acc, h) => acc + h.correct + h.wrong, 0);
    const totalCorrect = history.reduce((acc, h) => acc + h.correct, 0);
    const overallPct = totalAnswered ? Math.round((totalCorrect / totalAnswered) * 100) : 0;

    // Confident wrong count
    let confidentWrongTotal = 0;
    history.forEach(h => {
      if (h.confidences) {
        confidentWrongTotal += h.confidences.filter(c => c.confidence === 'sure' && !c.correct).length;
      }
    });

    container.innerHTML = `
      <div class="fade-in q-card">
        <h2 class="section-title">My Learning Analytics</h2>
        <div class="stats-grid mb-md">
          <div class="stat-card">
            <div class="stat-value">${totalAnswered}</div>
            <div class="stat-label">Total Answers</div>
          </div>
          <div class="stat-card">
            <div class="stat-value" style="color:var(--success);">${overallPct}%</div>
            <div class="stat-label">Accuracy</div>
          </div>
          <div class="stat-card">
            <div class="stat-value" style="color:var(--warn);">${streak} 🔥</div>
            <div class="stat-label">Day Streak</div>
          </div>
          <div class="stat-card">
            <div class="stat-value" style="color:var(--danger);">${confidentWrongTotal}</div>
            <div class="stat-label">Confident Mistakes</div>
          </div>
        </div>

        <div class="card mb-md">
          <h4>Performance Breakdown</h4>
          <p class="text-sm text-muted mt-sm">Correct: <strong>${totalCorrect}</strong> | Wrong: <strong>${totalAnswered - totalCorrect}</strong> | Flagged: <strong>${flags.length}</strong></p>
        </div>
      </div>
    `;
  },

  // 13. FLAGGED QUESTIONS (Review and export flags)
  renderFlags: async function(container) {
    container.innerHTML = '<div class="spinner"></div>';
    const flags = await DB.getAllFlags();
    if (!flags.length) {
      container.innerHTML = `
        <div class="empty-state fade-in">
          <div class="empty-icon">🚩</div>
          <h3>No Flagged Questions</h3>
          <p class="mt-sm">If you spot any issue or ambiguity, tap "Report" on the question card.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = `
      <div class="fade-in q-card">
        <div class="flex" style="justify-content:space-between; align-items:center; margin-bottom:16px;">
          <h2 class="section-title">Flagged Questions (${flags.length})</h2>
          <button class="btn btn-sm btn-secondary" id="btn-export-flags">Export JSON</button>
        </div>
        <div class="flex flex-col gap-sm">
          ${flags.map(f => `
            <div class="card flex" style="align-items:center; justify-content:space-between;">
              <div>
                <strong>${f.id}</strong>
                <p class="text-sm text-muted">${f.note || 'No note attached'}</p>
              </div>
              <button class="btn btn-sm btn-danger clear-flag-btn" data-id="${f.id}">Dismiss</button>
            </div>
          `).join('')}
        </div>
      </div>
    `;

    container.querySelector('#btn-export-flags').onclick = () => {
      const blob = new Blob([JSON.stringify(flags, null, 2)], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `studybuddy_flags_${Date.now()}.json`;
      a.click();
    };

    container.querySelectorAll('.clear-flag-btn').forEach(b => {
      b.onclick = async () => {
        await DB.clearFlag(b.getAttribute('data-id'));
        this.renderFlags(container);
      };
    });
  },

  // 14. EXPORT & IMPORT PROGRESS
  renderExport: function(container) {
    container.innerHTML = `
      <div class="fade-in q-card">
        <h2 class="section-title">Progress Backup & Sync</h2>
        <div class="card flex flex-col gap-md">
          <p>Export all your question history, spaced repetition intervals, stars, and flags to a single backup file so you never lose progress.</p>
          <button class="btn btn-primary" id="btn-export-file">💾 Download Progress JSON</button>
          <div class="separator"></div>
          <p>Restore progress from a previous export:</p>
          <button class="btn btn-secondary" id="btn-trigger-import">📥 Upload Progress Backup</button>
        </div>
      </div>
    `;

    container.querySelector('#btn-export-file').onclick = async () => {
      const data = await DB.exportProgress();
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `studybuddy_progress_${new Date().toISOString().slice(0, 10)}.json`;
      a.click();
      App.showToast('Progress exported!');
    };

    container.querySelector('#btn-trigger-import').onclick = () => {
      document.getElementById('import-file').click();
    };
  },

  // 15. OFFLINE CACHE STATUS
  renderOffline: function(container) {
    container.innerHTML = `
      <div class="fade-in q-card">
        <h2 class="section-title">Offline Cache Manager</h2>
        <div class="card flex flex-col gap-md">
          <p>Ensure all course content files are cached for 100% offline study on your phone.</p>
          <button class="btn btn-primary" id="btn-cache-now">⚡ Cache All Course Materials Now</button>
          <div id="cache-status" class="text-sm text-muted"></div>
        </div>
      </div>
    `;

    container.querySelector('#btn-cache-now').onclick = async () => {
      const statusEl = container.querySelector('#cache-status');
      statusEl.textContent = 'Caching course files in background...';
      await App.cacheAllContent();
      statusEl.textContent = '✓ All course content and shell assets cached offline!';
      App.showToast('Offline cache ready!');
    };
  }
};

window.Router = Router;
