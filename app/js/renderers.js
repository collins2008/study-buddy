// renderers.js — Comprehensive Question Renderers for Study Buddy
// Supports all 18 question types with feedback, self-grading, and interactive widgets

const Renderers = {
  // Utility: Levenshtein distance for fuzzy matching
  levenshtein: function(a, b) {
    if (!a || !b) return (a || '').length + (b || '').length;
    const m = a.length, n = b.length;
    const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 0; i <= m; i++) dp[i][0] = i;
    for (let j = 0; j <= n; j++) dp[0][j] = j;
    for (let i = 1; i <= m; i++) {
      for (let j = 1; j <= n; j++) {
        if (a[i - 1] === b[j - 1]) dp[i][j] = dp[i - 1][j - 1];
        else dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
      }
    }
    return dp[m][n];
  },

  normalizeText: function(str) {
    return (str || '')
      .toLowerCase()
      .trim()
      .replace(/[.,\/#!$%\^&\*;:{}=\-_`~()?"']/g, '')
      .replace(/\s+/g, ' ');
  },

  fuzzyMatch: function(userInput, target) {
    const u = this.normalizeText(userInput);
    const t = this.normalizeText(target);
    if (u === t) return true;
    const dist = this.levenshtein(u, t);
    // Allow 1 typo for words length 4-7, 2 typos for longer words
    if (t.length <= 4 && dist <= 0) return true;
    if (t.length <= 7 && dist <= 1) return true;
    if (t.length > 7 && dist <= 2) return true;
    return false;
  },

  // Utility: HTML Escaping
  escapeHtml: function(str) {
    if (str === null || str === undefined) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  },

  // Comprehensive Markdown & Text Formatter:
  // Handles triple backtick code blocks, single backtick inline code, bold, italics,
  // newlines, and safely escapes raw HTML tags and mathematical operators.
  formatText: function(text) {
    if (text === null || text === undefined) return '';
    let str = String(text);

    // 1. Extract triple backtick code blocks
    const codeBlocks = [];
    str = str.replace(/```([a-zA-Z0-9_-]*)\n?([\s\S]*?)```/g, (match, lang, code) => {
      const placeholder = `___CODE_BLOCK_${codeBlocks.length}___`;
      codeBlocks.push({ lang: lang || 'c', code: code.trim() });
      return placeholder;
    });

    // 2. Extract single backtick inline code
    const inlineCodes = [];
    str = str.replace(/`([^`]+)`/g, (match, code) => {
      const placeholder = `___INLINE_CODE_${inlineCodes.length}___`;
      inlineCodes.push(code);
      return placeholder;
    });

    // 3. Escape HTML on prose text
    str = this.escapeHtml(str);

    // 4. Bold: **text**
    str = str.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');

    // 5. Italics: *text* (when not part of a larger asterisk construct)
    str = str.replace(/(^|[\s\(\[\{\.,;:\-_])\*([^*]+)\*([\s\)\]\}\.,;:\-_]|$)/g, '$1<em>$2</em>$3');

    // 6. Convert newlines to <br>
    str = str.replace(/\r?\n/g, '<br>');

    // 7. Restore inline code (safely escaped inside <code>)
    str = str.replace(/___INLINE_CODE_(\d+)___/g, (match, idx) => {
      const code = inlineCodes[parseInt(idx, 10)];
      return `<code>${this.escapeHtml(code)}</code>`;
    });

    // 8. Restore code blocks
    str = str.replace(/___CODE_BLOCK_(\d+)___/g, (match, idx) => {
      const block = codeBlocks[parseInt(idx, 10)];
      return this.renderCodeBlock(block.code, block.lang);
    });

    return str;
  },

  // Highlight helper
  renderCodeBlock: function(codeStr, lang = 'c') {
    const pre = document.createElement('pre');
    const code = document.createElement('code');
    code.className = `language-${lang}`;
    code.textContent = codeStr;
    pre.className = 'hljs';
    pre.appendChild(code);
    if (window.hljs) {
      window.hljs.highlightElement(code);
    }
    return pre.outerHTML;
  },

  // Main question dispatcher
  renderQuestion: async function(q, container, onSubmit, options = {}) {
    // Ensure any open confidence modals are dismissed when switching/loading questions
    document.querySelectorAll('.confidence-modal').forEach(m => m.remove());
    container.innerHTML = '';
    const qWrapper = document.createElement('div');
    qWrapper.className = 'q-card fade-in';

    // Header: Tags, difficulty, star, flag
    const isStarred = (await DB.getStars()).has(q.id);
    const diffLabels = { 1: 'Recall (L1)', 2: 'Understand (L2)', 3: 'Apply (L3)', 4: 'Analyze (L4)' };

    const meta = document.createElement('div');
    meta.className = 'q-meta';
    meta.innerHTML = `
      <span class="tag tag-difficulty-${q.difficulty || 1}">${diffLabels[q.difficulty || 1]}</span>
      <span class="tag">${q.course || ''}</span>
      <span class="tag">${(q.type || 'mcq').replace('_', ' ')}</span>
      <button class="icon-btn star-btn" style="margin-left:auto; font-size:1.2rem;" title="Star Question">${isStarred ? '⭐' : '☆'}</button>
      <button class="report-btn flag-btn" title="Report Issue">🚩 Report</button>
    `;

    meta.querySelector('.star-btn').onclick = async (e) => {
      const nowStarred = await DB.toggleStar(q.id);
      e.target.textContent = nowStarred ? '⭐' : '☆';
      App.showToast(nowStarred ? 'Question starred!' : 'Star removed');
    };

    meta.querySelector('.flag-btn').onclick = () => {
      App.promptReport(q.id);
    };

    qWrapper.appendChild(meta);

    // Question statement (omit for flashcards where the card itself is the prompt)
    if (q.type !== 'flashcard') {
      const promptDiv = document.createElement('div');
      promptDiv.className = 'q-question';
      promptDiv.innerHTML = this.formatText(q.question);
      qWrapper.appendChild(promptDiv);
    }

    // If there is code snippet attached
    if (q.code) {
      const codeContainer = document.createElement('div');
      codeContainer.className = 'code-block';
      codeContainer.innerHTML = this.renderCodeBlock(q.code, q.code_lang || 'c');
      qWrapper.appendChild(codeContainer);
    }

    // Interactive Renderer by type
    const interactionArea = document.createElement('div');
    interactionArea.className = 'interaction-area';
    qWrapper.appendChild(interactionArea);

    // Feedback area
    const feedbackArea = document.createElement('div');
    feedbackArea.className = 'feedback-area hidden';
    qWrapper.appendChild(feedbackArea);

    container.appendChild(qWrapper);

    // Dispatch to specific renderer
    const rendererMap = {
      'mcq': this.renderMCQ,
      'multi_select': this.renderMultiSelect,
      'true_false_why': this.renderTrueFalseWhy,
      'type_answer': this.renderTypeAnswer,
      'cloze': this.renderCloze,
      'matching': this.renderMatching,
      'sequencing': this.renderSequencing,
      'flashcard': this.renderFlashcard,
      'explain': this.renderExplain,
      'case_study': this.renderCaseStudy,
      'code_output': this.renderCodeOutput,
      'code_bug': this.renderCodeBug,
      'code_fill': this.renderCodeFill,
      'code_write': this.renderCodeWrite,
      'code_trace': this.renderCodeTrace,
      'html_render': this.renderHtmlRender,
      'calculation': this.renderCalculation,
      'diagram_label': this.renderDiagramLabel
    };

    const handler = rendererMap[q.type] || this.renderMCQ;
    handler.call(this, q, interactionArea, feedbackArea, onSubmit, options);
  },

  // 1. MCQ (Single Answer)
  renderMCQ: function(q, area, feedback, onSubmit, options = {}) {
    const list = document.createElement('div');
    list.className = 'options-list';
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    q.options.forEach((opt, idx) => {
      const btn = document.createElement('button');
      btn.className = 'option-btn';
      btn.innerHTML = `<span class="option-label">${alphabet[idx]}.</span> <span>${this.formatText(opt)}</span>`;
      btn.onclick = () => {
        if (btn.disabled || list.getAttribute('data-evaluated') === 'true') return;

        // In exam mode, immediately select option without popup interruption
        if (options && options.examMode) {
          this.evaluateMCQ(q, idx, list, feedback, onSubmit, 'sure', options);
          return;
        }

        // Highlight chosen option visually with pending state
        Array.from(list.children).forEach(b => b.classList.remove('selected-pending'));
        btn.classList.add('selected-pending');

        this.askConfidence((confidence) => {
          this.evaluateMCQ(q, idx, list, feedback, onSubmit, confidence, options);
        }, () => {
          // If user cancels or changes option, remove the pending highlight
          btn.classList.remove('selected-pending');
        });
      };
      list.appendChild(btn);
    });
    area.appendChild(list);
  },

  evaluateMCQ: function(q, selectedIdx, list, feedback, onSubmit, confidence, options = {}) {
    list.setAttribute('data-evaluated', 'true');
    Array.from(list.children).forEach(btn => {
      btn.disabled = true;
      btn.classList.remove('selected-pending');
    });

    let targetIdx = q.answer;
    if (typeof targetIdx === 'string') {
      const trimmed = targetIdx.trim();
      const inOptions = q.options ? q.options.indexOf(trimmed) : -1;
      if (inOptions !== -1) {
        targetIdx = inOptions;
      } else {
        const parsed = parseInt(trimmed, 10);
        targetIdx = isNaN(parsed) ? 0 : parsed;
      }
    } else {
      targetIdx = parseInt(targetIdx, 10);
    }
    const isCorrect = (selectedIdx === targetIdx);
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    if (options && options.examMode) {
      // Exam mode: no instant right/wrong revelation during test
      Array.from(list.children).forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === selectedIdx) btn.classList.add('selected');
      });
      if (onSubmit) onSubmit({ isCorrect, confidence, selected: selectedIdx, targetIdx });
      return;
    }

    Array.from(list.children).forEach((btn, idx) => {
      btn.disabled = true;
      if (idx === targetIdx) btn.classList.add('correct');
      if (idx === selectedIdx && !isCorrect) btn.classList.add('wrong');
    });

    this.showExplanation(q, isCorrect, feedback, selectedIdx, confidence);
    if (onSubmit) onSubmit({ isCorrect, confidence, selected: selectedIdx, targetIdx });
  },

  // 2. Multi Select
  renderMultiSelect: function(q, area, feedback, onSubmit) {
    const list = document.createElement('div');
    list.className = 'options-list';
    const selected = new Set();
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    q.options.forEach((opt, idx) => {
      const btn = document.createElement('button');
      btn.className = 'option-btn';
      btn.innerHTML = `<span class="option-label">${alphabet[idx]}.</span> <span>${this.formatText(opt)}</span>`;
      btn.onclick = () => {
        if (selected.has(idx)) {
          selected.delete(idx);
          btn.classList.remove('selected');
        } else {
          selected.add(idx);
          btn.classList.add('selected');
        }
      };
      list.appendChild(btn);
    });
    area.appendChild(list);

    const submitBtn = document.createElement('button');
    submitBtn.className = 'btn btn-primary btn-full mt-md';
    submitBtn.textContent = 'Submit Selection';
    submitBtn.onclick = () => {
      if (selected.size === 0) {
        App.showToast('Please select at least one option.');
        return;
      }
      submitBtn.disabled = true;
      this.askConfidence((confidence) => {
        const correctSet = new Set(Array.isArray(q.answer) ? q.answer.map(Number) : [Number(q.answer)]);
        let isCorrect = selected.size === correctSet.size && [...selected].every(x => correctSet.has(x));

        Array.from(list.children).forEach((btn, idx) => {
          btn.disabled = true;
          if (correctSet.has(idx)) btn.classList.add('correct');
          else if (selected.has(idx)) btn.classList.add('wrong');
        });

        this.showExplanation(q, isCorrect, feedback, null, confidence);
        if (onSubmit) onSubmit({ isCorrect, confidence, selected: [...selected] });
      }, () => {
        submitBtn.disabled = false;
      });
    };
    area.appendChild(submitBtn);
  },

  // 3. True False Why
  renderTrueFalseWhy: function(q, area, feedback, onSubmit) {
    area.innerHTML = `
      <div class="mb-md">
        <label>1. Select Verdict:</label>
        <div class="flex gap-md">
          <button class="btn btn-secondary flex-1 tf-btn" data-val="true">True</button>
          <button class="btn btn-secondary flex-1 tf-btn" data-val="false">False</button>
        </div>
      </div>
      <div class="mb-md why-section hidden">
        <label>2. Choose the Valid Justification:</label>
        <div class="options-list why-options"></div>
      </div>
    `;

    let chosenTF = null;
    const tfBtns = area.querySelectorAll('.tf-btn');
    const whySection = area.querySelector('.why-section');
    const whyList = area.querySelector('.why-options');

    tfBtns.forEach(btn => {
      btn.onclick = () => {
        tfBtns.forEach(b => b.classList.remove('btn-primary'));
        btn.classList.add('btn-primary');
        chosenTF = btn.getAttribute('data-val') === 'true';

        whySection.classList.remove('hidden');
        whyList.innerHTML = '';

        (q.why_options || q.options || []).forEach((wOpt, idx) => {
          const wBtn = document.createElement('button');
          wBtn.className = 'option-btn';
          wBtn.innerHTML = this.formatText(wOpt);
          wBtn.onclick = () => {
            if (wBtn.disabled || whyList.getAttribute('data-evaluated') === 'true') return;

            Array.from(whyList.children).forEach(b => b.classList.remove('selected-pending'));
            wBtn.classList.add('selected-pending');

            this.askConfidence((confidence) => {
              whyList.setAttribute('data-evaluated', 'true');
              tfBtns.forEach(b => b.disabled = true);
              Array.from(whyList.children).forEach(b => {
                b.disabled = true;
                b.classList.remove('selected-pending');
              });

              const correctTF = (q.answer === true || q.answer === 'true' || q.tf_answer === true);
              const correctWhyIdx = q.why_answer !== undefined ? q.why_answer : q.answer_why;
              const isCorrect = (chosenTF === correctTF) && (idx === correctWhyIdx || correctWhyIdx === undefined);

              if (idx === correctWhyIdx) wBtn.classList.add('correct');
              else wBtn.classList.add('wrong');

              this.showExplanation(q, isCorrect, feedback, null, confidence);
              if (onSubmit) onSubmit({ isCorrect, confidence });
            }, () => {
              wBtn.classList.remove('selected-pending');
            });
          };
          whyList.appendChild(wBtn);
        });
      };
    });
  },

  // 4. Type Answer
  renderTypeAnswer: function(q, area, feedback, onSubmit) {
    const input = document.createElement('input');
    input.type = 'text';
    input.className = 'answer-input';
    input.placeholder = 'Type your answer here...';

    const submitBtn = document.createElement('button');
    submitBtn.className = 'btn btn-primary btn-full mt-md';
    submitBtn.textContent = 'Submit Answer';

    const evaluate = () => {
      const val = input.value.trim();
      if (!val) {
        App.showToast('Please type an answer first.');
        return;
      }
      input.disabled = true;
      submitBtn.disabled = true;

      this.askConfidence((confidence) => {
        const accepted = q.accepted_answers || [q.answer];
        const isCorrect = accepted.some(acc => this.fuzzyMatch(val, acc));

        if (isCorrect) input.classList.add('correct');
        else input.classList.add('wrong');

        let modelAnswerHtml = `<div class="mb-sm"><strong>Accepted Answer:</strong> <code>${this.escapeHtml(accepted[0])}</code></div>`;
        this.showExplanation(q, isCorrect, feedback, null, confidence, modelAnswerHtml);
        if (onSubmit) onSubmit({ isCorrect, confidence, answer: val });
      }, () => {
        input.disabled = false;
        submitBtn.disabled = false;
        input.focus();
      });
    };

    submitBtn.onclick = evaluate;
    input.onkeydown = (e) => { if (e.key === 'Enter') evaluate(); };

    area.appendChild(input);
    area.appendChild(submitBtn);
    setTimeout(() => input.focus(), 100);
  },

  // 5. Cloze (Fill in the blanks)
  renderCloze: function(q, area, feedback, onSubmit) {
    const container = document.createElement('div');
    container.className = 'cloze-text mb-md';

    // Replace [[blank]] or ___ with input fields
    const blanks = q.blanks || [q.answer];
    let counter = 0;
    const escapedTemplate = this.escapeHtml(q.template || q.question);
    const textWithInputs = escapedTemplate.replace(/\[\[(.*?)\]\]|___+/g, (match, p1) => {
      const idx = counter++;
      return `<input type="text" class="cloze-blank" data-idx="${idx}" placeholder="blank ${idx + 1}" autocomplete="off">`;
    });

    container.innerHTML = textWithInputs;
    area.appendChild(container);

    const submitBtn = document.createElement('button');
    submitBtn.className = 'btn btn-primary btn-full';
    submitBtn.textContent = 'Check Blanks';

    submitBtn.onclick = () => {
      const inputs = area.querySelectorAll('.cloze-blank');
      let allCorrect = true;

      this.askConfidence((confidence) => {
        inputs.forEach((inp, idx) => {
          inp.disabled = true;
          const target = blanks[idx] || '';
          const match = this.fuzzyMatch(inp.value, target);
          if (match) {
            inp.classList.add('correct');
          } else {
            inp.classList.add('wrong');
            allCorrect = false;
          }
        });

        submitBtn.disabled = true;
        const answersHtml = `<div><strong>Answers:</strong> ${blanks.map((b, i) => `(${i+1}) <code>${this.escapeHtml(b)}</code>`).join(', ')}</div>`;
        this.showExplanation(q, allCorrect, feedback, null, confidence, answersHtml);
        if (onSubmit) onSubmit({ isCorrect: allCorrect, confidence });
      }, () => {
        submitBtn.disabled = false;
      });
    };

    area.appendChild(submitBtn);
  },

  // 6. Matching
  renderMatching: function(q, area, feedback, onSubmit) {
    const pairs = q.pairs || []; // [{left: '', right: ''}]
    const leftItems = pairs.map(p => p.left);
    const rightItems = [...pairs.map(p => p.right)].sort(() => Math.random() - 0.5);

    const container = document.createElement('div');
    container.className = 'matching-container';

    let selectedLeft = null;
    let userMatches = {};

    leftItems.forEach(left => {
      const row = document.createElement('div');
      row.className = 'matching-row';
      row.innerHTML = `
        <div class="match-term">${this.formatText(left)}</div>
        <div class="match-arrow">➔</div>
        <div class="match-def" data-left="${this.escapeHtml(left)}">Select matching definition...</div>
      `;
      container.appendChild(row);
    });

    area.appendChild(container);

    const choicesDiv = document.createElement('div');
    choicesDiv.className = 'filter-row mt-md';
    choicesDiv.innerHTML = '<label class="w-full">Available Definitions (tap to assign to active item):</label>';

    rightItems.forEach(right => {
      const chip = document.createElement('button');
      chip.className = 'chip';
      chip.innerHTML = this.formatText(right);
      chip.onclick = () => {
        if (!selectedLeft) {
          App.showToast('First tap a term row above to link!');
          return;
        }
        userMatches[selectedLeft] = right;
        const targetEl = container.querySelector(`.match-def[data-left="${CSS.escape(selectedLeft)}"]`);
        if (targetEl) {
          targetEl.innerHTML = this.formatText(right);
          targetEl.classList.add('selected');
        }
      };
      choicesDiv.appendChild(chip);
    });
    area.appendChild(choicesDiv);

    // Click handler for rows / left items
    container.querySelectorAll('.matching-row').forEach(row => {
      row.onclick = () => {
        const defEl = row.querySelector('.match-def');
        container.querySelectorAll('.matching-row').forEach(r => r.classList.remove('selected-row'));
        row.classList.add('selected-row');
        container.querySelectorAll('.match-def').forEach(d => d.style.borderColor = 'var(--border)');
        defEl.style.borderColor = 'var(--primary)';
        selectedLeft = defEl.getAttribute('data-left');
      };
    });

    const submitBtn = document.createElement('button');
    submitBtn.className = 'btn btn-primary btn-full mt-md';
    submitBtn.textContent = 'Submit Matches';
    submitBtn.onclick = () => {
      if (Object.keys(userMatches).length < leftItems.length) {
        App.showToast('Please match all items first.');
        return;
      }
      submitBtn.disabled = true;
      this.askConfidence((confidence) => {
        let allCorrect = true;
        pairs.forEach(p => {
          const matched = userMatches[p.left];
          const defEl = container.querySelector(`.match-def[data-left="${CSS.escape(p.left)}"]`);
          if (matched === p.right) {
            defEl.classList.remove('selected');
            defEl.classList.add('matched');
            defEl.innerHTML = this.formatText(matched);
          } else {
            defEl.classList.remove('selected');
            defEl.classList.add('wrong-match');
            defEl.innerHTML = `<s>${this.formatText(matched)}</s> ➔ <strong>${this.formatText(p.right)}</strong>`;
            allCorrect = false;
          }
        });

        this.showExplanation(q, allCorrect, feedback, null, confidence);
        if (onSubmit) onSubmit({ isCorrect: allCorrect, confidence });
      }, () => {
        submitBtn.disabled = false;
      });
    };
    area.appendChild(submitBtn);
  },

  // 7. Sequencing
  renderSequencing: function(q, area, feedback, onSubmit) {
    const original = [...(q.steps || q.options || [])];
    const items = [...original].sort(() => Math.random() - 0.5);

    const list = document.createElement('div');
    list.className = 'sequence-list';

    items.forEach((itemText, i) => {
      const itemEl = document.createElement('div');
      itemEl.className = 'seq-item';
      itemEl.innerHTML = `
        <span class="seq-num">${i + 1}</span>
        <span class="flex-1">${this.formatText(itemText)}</span>
        <button class="icon-btn up-btn" title="Move Up">▲</button>
        <button class="icon-btn dn-btn" title="Move Down">▼</button>
      `;

      itemEl.querySelector('.up-btn').onclick = () => {
        if (itemEl.previousElementSibling) {
          list.insertBefore(itemEl, itemEl.previousElementSibling);
          updateNums();
        }
      };
      itemEl.querySelector('.dn-btn').onclick = () => {
        if (itemEl.nextElementSibling) {
          list.insertBefore(itemEl.nextElementSibling, itemEl);
          updateNums();
        }
      };
      list.appendChild(itemEl);
    });

    function updateNums() {
      list.querySelectorAll('.seq-item').forEach((el, idx) => {
        el.querySelector('.seq-num').textContent = idx + 1;
      });
    }

    area.appendChild(list);

    const submitBtn = document.createElement('button');
    submitBtn.className = 'btn btn-primary btn-full mt-md';
    submitBtn.textContent = 'Check Sequence';
    submitBtn.onclick = () => {
      submitBtn.disabled = true;
      this.askConfidence((confidence) => {
        const currentOrder = Array.from(list.querySelectorAll('.seq-item')).map(el => el.querySelector('.flex-1').textContent.trim());
        let allCorrect = true;

        list.querySelectorAll('.seq-item').forEach((el, idx) => {
          el.querySelectorAll('button').forEach(b => b.disabled = true);
          if (currentOrder[idx] === original[idx]) {
            el.classList.add('correct-pos');
          } else {
            el.classList.add('wrong-pos');
            allCorrect = false;
          }
        });

        const correctOrderHtml = `<div class="mb-sm"><strong>Correct Sequence:</strong><ol style="padding-left:20px; margin-top:8px;">${original.map(s => `<li>${this.formatText(s)}</li>`).join('')}</ol></div>`;
        this.showExplanation(q, allCorrect, feedback, null, confidence, correctOrderHtml);
        if (onSubmit) onSubmit({ isCorrect: allCorrect, confidence });
      }, () => {
        submitBtn.disabled = false;
      });
    };
    area.appendChild(submitBtn);
  },

  // 8. Flashcard (Flip, rate Again/Hard/Good/Easy)
  renderFlashcard: function(q, area, feedback, onSubmit) {
    const card = document.createElement('div');
    card.className = 'flashcard-box';

    const renderSide = (isFlipped) => {
      if (!isFlipped) {
        card.classList.remove('is-flipped');
        card.innerHTML = `
          <div class="flashcard-badge-row">
            <span class="tag">Front</span>
          </div>
          <div class="flashcard-text">${this.formatText(q.question || q.front)}</div>
          <div class="flashcard-hint">Tap card to flip ↻</div>
        `;
      } else {
        card.classList.add('is-flipped');
        card.innerHTML = `
          <div class="flashcard-badge-row">
            <span class="tag" style="background:var(--primary); color:white;">Back / Definition</span>
          </div>
          <div class="flashcard-text">${this.formatText(q.answer || q.back)}</div>
          ${q.explanation ? `<div class="text-sm text-muted mt-md">${this.formatText(q.explanation)}</div>` : ''}
          <div class="flashcard-hint">Tap card to flip back ↻</div>
        `;
      }
    };

    let isFlipped = false;
    let isAnimating = false;

    renderSide(false);

    card.onclick = () => {
      if (isAnimating) return;
      isAnimating = true;

      // Smooth 3D perspective flip transition
      card.style.transform = 'scale(0.97) rotateY(90deg)';
      setTimeout(() => {
        isFlipped = !isFlipped;
        renderSide(isFlipped);
        card.style.transform = 'scale(1) rotateY(0deg)';
        if (isFlipped) ratingRow.classList.remove('hidden');
        setTimeout(() => { isAnimating = false; }, 200);
      }, 150);
    };

    area.appendChild(card);

    const ratingRow = document.createElement('div');
    ratingRow.className = 'rating-row hidden';
    ratingRow.innerHTML = `
      <button class="btn btn-danger" data-rate="0">1. Again</button>
      <button class="btn btn-warn" data-rate="1">2. Hard</button>
      <button class="btn btn-secondary" data-rate="2">3. Good</button>
      <button class="btn btn-success" data-rate="3">4. Easy</button>
    `;

    ratingRow.querySelectorAll('button').forEach(btn => {
      btn.onclick = async () => {
        const rating = parseInt(btn.getAttribute('data-rate'));
        await SR.update(q.id, rating);
        if (onSubmit) onSubmit({ isCorrect: rating >= 2, rating });
      };
    });
    area.appendChild(ratingRow);
  },

  // 9. Explain (Free-text with checklist self-grading)
  renderExplain: function(q, area, feedback, onSubmit) {
    const textarea = document.createElement('textarea');
    textarea.className = 'answer-input mb-md';
    textarea.placeholder = 'Write out your explanation / definition here...';
    area.appendChild(textarea);

    const revealBtn = document.createElement('button');
    revealBtn.className = 'btn btn-primary btn-full';
    revealBtn.textContent = 'Reveal Model Answer & Mark Points';
    area.appendChild(revealBtn);

    const markingBox = document.createElement('div');
    markingBox.className = 'mt-md hidden';
    area.appendChild(markingBox);

    revealBtn.onclick = () => {
      textarea.disabled = true;
      revealBtn.disabled = true;
      markingBox.classList.remove('hidden');

      const points = q.marking_points || [
        'Clear conceptual definition',
        'Key characteristics / mechanisms accurately described',
        'Direct connection to the question scenario'
      ];

      markingBox.innerHTML = `
        <div class="explanation-box mb-md">
          <h4>Reference Model Answer</h4>
          <div class="model-answer-text">${this.formatText(q.answer || q.explanation)}</div>
        </div>
        <h4>Self-Marking Checklist (tick points you covered):</h4>
        <div class="marking-points mb-md">
          ${points.map((pt, i) => `
            <div class="mark-point">
              <div class="mark-check" data-idx="${i}">✓</div>
              <div class="flex-1">${this.formatText(pt)}</div>
            </div>
          `).join('')}
        </div>
        <button class="btn btn-success btn-full submit-grade-btn">Submit Self-Grade</button>
      `;

      const checks = markingBox.querySelectorAll('.mark-check');
      checks.forEach(chk => {
        chk.onclick = () => chk.classList.toggle('checked');
      });

      markingBox.querySelector('.submit-grade-btn').onclick = () => {
        const ticked = markingBox.querySelectorAll('.mark-check.checked').length;
        const total = points.length;
        const isCorrect = (ticked / total) >= 0.6;

        this.showExplanation(q, isCorrect, feedback);
        if (onSubmit) onSubmit({ isCorrect, score: ticked, total });
      };
    };
  },

  // 10. Case Study
  renderCaseStudy: function(cs, area, feedback, onSubmit) {
    area.innerHTML = `
      <div class="case-scenario">
        <h4>Scenario: ${this.escapeHtml(cs.title || 'Case Analysis')}</h4>
        <div class="scenario-text">${this.formatText(cs.scenario)}</div>
      </div>
      <div class="case-sub-container"></div>
    `;

    const subContainer = area.querySelector('.case-sub-container');
    const questions = cs.sub_questions || cs.questions || [];
    let curSubIdx = 0;
    let scores = [];

    const loadSubQ = () => {
      if (curSubIdx >= questions.length) {
        const overallCorrect = scores.filter(s => s.isCorrect).length >= (questions.length / 2);
        area.innerHTML = `
          <div class="card text-center">
            <h3>Case Study Completed!</h3>
            <p class="mt-sm">You answered ${scores.filter(s => s.isCorrect).length} of ${questions.length} sub-questions correctly.</p>
            <button class="btn btn-primary mt-md finish-cs-btn">Next Item</button>
          </div>
        `;
        area.querySelector('.finish-cs-btn').onclick = () => {
          if (onSubmit) onSubmit({ isCorrect: overallCorrect, scores });
        };
        return;
      }

      subContainer.innerHTML = `<div class="sub-question-counter">Sub-question ${curSubIdx + 1} of ${questions.length}</div><div class="sub-target"></div>`;
      const q = questions[curSubIdx];
      this.renderQuestion(q, subContainer.querySelector('.sub-target'), (res) => {
        scores.push(res);
        curSubIdx++;
        setTimeout(loadSubQ, 1200);
      });
    };

    loadSubQ();
  },

  // 11. Code Output
  renderCodeOutput: function(q, area, feedback, onSubmit) {
    if (q.options && q.options.length > 0) {
      this.renderMCQ(q, area, feedback, onSubmit);
    } else {
      this.renderTypeAnswer(q, area, feedback, onSubmit);
    }
  },

  // 12. Code Bug (Locate and fix the bug)
  renderCodeBug: function(q, area, feedback, onSubmit) {
    if (q.options && q.options.length > 0) {
      this.renderMCQ(q, area, feedback, onSubmit);
    } else {
      this.renderExplain(q, area, feedback, onSubmit);
    }
  },

  // 13. Code Fill
  renderCodeFill: function(q, area, feedback, onSubmit) {
    this.renderCloze(q, area, feedback, onSubmit);
  },

  // 14. Code Write
  renderCodeWrite: function(q, area, feedback, onSubmit) {
    area.innerHTML = `
      <label>Write C/HTML/CSS code to meet specification:</label>
      <textarea class="answer-input mb-md" rows="8" placeholder="// Write code here..."></textarea>
      <button class="btn btn-primary btn-full reveal-code-btn">Submit Code & View Reference Solution</button>
      <div class="code-ref-area hidden mt-md"></div>
    `;

    const txt = area.querySelector('textarea');
    const btn = area.querySelector('.reveal-code-btn');
    const refArea = area.querySelector('.code-ref-area');

    btn.onclick = () => {
      txt.disabled = true;
      btn.disabled = true;
      refArea.classList.remove('hidden');

      const refCode = q.reference_solution || q.answer || '';
      const points = q.marking_points || [
        'Correct syntax and types',
        'Logic correctly handles required conditions',
        'Clean edge case handling or return code'
      ];

      refArea.innerHTML = `
        <div class="code-block mb-md">
          <span class="code-lang">Verified Reference Solution</span>
          ${this.renderCodeBlock(refCode, q.code_lang || 'c')}
        </div>
        <h4>Self-Marking Checklist:</h4>
        <div class="marking-points mb-md">
          ${points.map((pt, i) => `
            <div class="mark-point">
              <div class="mark-check" data-idx="${i}">✓</div>
              <div class="flex-1">${this.formatText(pt)}</div>
            </div>
          `).join('')}
        </div>
        <button class="btn btn-success btn-full finish-write-btn">Confirm Self-Grade</button>
      `;

      refArea.querySelectorAll('.mark-check').forEach(c => {
        c.onclick = () => c.classList.toggle('checked');
      });

      refArea.querySelector('.finish-write-btn').onclick = () => {
        const ticked = refArea.querySelectorAll('.mark-check.checked').length;
        const isCorrect = (ticked / points.length) >= 0.6;
        this.showExplanation(q, isCorrect, feedback);
        if (onSubmit) onSubmit({ isCorrect, score: ticked, total: points.length });
      };
    };
  },

  // 15. Code Trace
  renderCodeTrace: function(q, area, feedback, onSubmit) {
    if (q.options && q.options.length > 0) {
      this.renderMCQ(q, area, feedback, onSubmit);
    } else {
      this.renderTypeAnswer(q, area, feedback, onSubmit);
    }
  },

  // 16. HTML Render (Sandboxed iframe)
  renderHtmlRender: function(q, area, feedback, onSubmit) {
    const rawHtml = q.html_code || q.code || '<h1>Hello World</h1>';
    const iframeHtml = `
      <div class="iframe-toggle">
        <span class="tag">Sandboxed Render Preview</span>
      </div>
      <iframe class="html-sandbox mb-md" sandbox="allow-same-origin" srcdoc="${rawHtml.replace(/"/g, '&quot;')}"></iframe>
    `;

    const previewDiv = document.createElement('div');
    previewDiv.innerHTML = iframeHtml;
    area.appendChild(previewDiv);

    const questionSubArea = document.createElement('div');
    area.appendChild(questionSubArea);

    if (q.options && q.options.length > 0) {
      this.renderMCQ(q, questionSubArea, feedback, onSubmit);
    } else {
      this.renderTypeAnswer(q, questionSubArea, feedback, onSubmit);
    }
  },

  // 17. Calculation
  renderCalculation: function(q, area, feedback, onSubmit) {
    const input = document.createElement('input');
    input.type = 'number';
    input.step = 'any';
    input.className = 'answer-input mb-md';
    input.placeholder = 'Enter numerical value...';

    const submitBtn = document.createElement('button');
    submitBtn.className = 'btn btn-primary btn-full';
    submitBtn.textContent = 'Submit Calculation';

    submitBtn.onclick = () => {
      const val = parseFloat(input.value);
      if (isNaN(val)) {
        App.showToast('Please enter a valid number');
        return;
      }
      input.disabled = true;
      submitBtn.disabled = true;

      this.askConfidence((confidence) => {
        const target = parseFloat(q.answer);
        const tol = q.tolerance !== undefined ? parseFloat(q.tolerance) : 0.01;
        const isCorrect = Math.abs(val - target) <= tol;

        if (isCorrect) input.classList.add('correct');
        else input.classList.add('wrong');

        const calcHtml = `<div><strong>Exact Value:</strong> <code>${target}</code> (allowed margin ±${tol})</div>`;
        this.showExplanation(q, isCorrect, feedback, null, confidence, calcHtml);
        if (onSubmit) onSubmit({ isCorrect, confidence, value: val });
      }, () => {
        input.disabled = false;
        submitBtn.disabled = false;
        input.focus();
      });
    };

    area.appendChild(input);
    area.appendChild(submitBtn);
  },

  // 18. Diagram Label
  renderDiagramLabel: function(q, area, feedback, onSubmit) {
    if (q.svg) {
      const svgDiv = document.createElement('div');
      svgDiv.className = 'card mb-md text-center';
      svgDiv.innerHTML = q.svg;
      area.appendChild(svgDiv);
    }
    if (q.options && q.options.length > 0) {
      this.renderMCQ(q, area, feedback, onSubmit);
    } else {
      this.renderTypeAnswer(q, area, feedback, onSubmit);
    }
  },

  // Confidence Rating Dialog
  askConfidence: function(callback, onCancel = null) {
    // 1. Immediately eliminate any existing confidence modals to guarantee no duplicates
    document.querySelectorAll('.confidence-modal').forEach(m => m.remove());

    // Check if user disabled confidence ratings in settings
    const setting = localStorage.getItem('study_buddy_confidence_prompt');
    if (setting === 'off') {
      callback('sure');
      return;
    }

    const modal = document.createElement('div');
    modal.className = 'confidence-modal';
    modal.innerHTML = `
      <div class="confidence-sheet card">
        <div class="confidence-header">
          <h4>Before Revealing: How confident are you?</h4>
          <button class="icon-btn close-btn" title="Cancel & change selection" style="font-size:1.2rem; line-height:1;">✕</button>
        </div>
        <p class="confidence-sub">Rate your confidence before seeing the explanation to track blind spots:</p>
        <div class="confidence-row">
          <button class="btn btn-success" data-conf="sure">🎯 Sure</button>
          <button class="btn btn-warn" data-conf="unsure">🤔 Unsure</button>
          <button class="btn btn-secondary" data-conf="guess">🎲 Guess</button>
        </div>
        <button class="confidence-cancel-btn">Change Selection</button>
      </div>
    `;

    document.body.appendChild(modal);

    const closeModal = () => {
      modal.remove();
      if (onCancel) onCancel();
    };

    // Backdrop click dismisses
    modal.onclick = (e) => {
      if (e.target === modal) closeModal();
    };

    modal.querySelector('.close-btn').onclick = closeModal;
    modal.querySelector('.confidence-cancel-btn').onclick = closeModal;

    modal.querySelectorAll('.confidence-row button').forEach(btn => {
      btn.onclick = () => {
        const conf = btn.getAttribute('data-conf');
        modal.remove();
        callback(conf);
      };
    });
  },

  // Detailed Feedback / Explanation View
  showExplanation: function(q, isCorrect, feedbackEl, selectedIdx = null, confidence = null, extraHtml = '') {
    feedbackEl.classList.remove('hidden');

    // Confidently wrong warning
    let confidentWrongHtml = '';
    if (!isCorrect && confidence === 'sure') {
      confidentWrongHtml = `
        <div class="confidently-wrong-banner">
          ⚠️ <strong>Watch Out:</strong> You answered this incorrectly with HIGH confidence! This is an active blind spot.
        </div>
      `;
    }

    // Why Wrong item for selected option
    let whyWrongHtml = '';
    const wwKey = selectedIdx !== null && selectedIdx !== undefined ? String(selectedIdx) : null;
    const wwText = (q.why_wrong && wwKey && (q.why_wrong[wwKey] || (q.options && q.why_wrong[q.options[selectedIdx]]))) || '';
    if (wwText) {
      whyWrongHtml = `
        <div class="why-wrong-item">
          <strong>Why option (${'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[selectedIdx]}) was incorrect:</strong><br>
          ${this.formatText(wwText)}
        </div>
      `;
    }

    // Verified output for code questions
    let verifiedHtml = '';
    if (q.verified && q.verified_output) {
      verifiedHtml = `
        <div class="mt-sm" style="font-size:0.85rem; color:var(--secondary);">
          ✓ <em>Verified Compiler Output:</em> <code>${this.escapeHtml(q.verified_output.replace(/\n/g, ' '))}</code>
        </div>
      `;
    }

    feedbackEl.innerHTML = `
      <div class="explanation-box fade-in">
        ${confidentWrongHtml}
        <h4 style="color:${isCorrect ? 'var(--success)' : 'var(--danger)'}">
          ${isCorrect ? '✓ Correct!' : '✗ Needs Revision'}
        </h4>
        <div class="explanation-text">${this.formatText(q.explanation || 'No detailed explanation provided.')}</div>
        ${whyWrongHtml}
        ${extraHtml}
        ${verifiedHtml}
        ${q.source ? `<div class="text-sm text-muted mt-md">📖 <em>Source: ${this.escapeHtml(q.source)}</em></div>` : ''}
      </div>
    `;
  }
};

window.Renderers = Renderers;
