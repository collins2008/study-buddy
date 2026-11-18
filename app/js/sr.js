// sr.js — Spaced Repetition (SM-2 based)
// Ratings: 0=Again, 1=Hard, 2=Good, 3=Easy

const SR = {
  MIN_EF: 1.3,
  DEFAULT_EF: 2.5,

  /**
   * Get or create SR state for a question
   */
  async getState(id) {
    let state = await DB.getSR(id);
    if (!state) {
      state = { id, interval: 0, ef: SR.DEFAULT_EF, due: Date.now(), reps: 0 };
    }
    return state;
  },

  /**
   * Update SR state after answering
   * rating: 0 (Again), 1 (Hard), 2 (Good), 3 (Easy)
   */
  async update(id, rating) {
    const state = await SR.getState(id);
    const now = Date.now();
    const DAY = 86400000;

    // Map rating to SM-2 quality q: 0→0, 1→3, 2→4, 3→5
    const q = [0, 3, 4, 5][rating];

    if (q < 3) {
      // Reset
      state.reps = 0;
      state.interval = 1;
    } else {
      if (state.reps === 0)      state.interval = 1;
      else if (state.reps === 1) state.interval = 6;
      else                       state.interval = Math.round(state.interval * state.ef);
      state.reps++;
      // Update EF
      state.ef = Math.max(SR.MIN_EF, state.ef + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)));
    }

    state.due = now + state.interval * DAY;
    await DB.putSR(state);
    return state;
  },

  /**
   * Get all due question IDs (due <= now)
   */
  async getDueIds() {
    const all = await DB.getAllSR();
    const now = Date.now();
    return all.filter(s => s.due <= now).map(s => s.id);
  },

  /**
   * Get due count
   */
  async getDueCount() {
    return (await SR.getDueIds()).length;
  },

  /**
   * Schedule a question NOW (force due) — used for wrong answers
   */
  async scheduleSoon(id) {
    const state = await SR.getState(id);
    state.due = Date.now();
    state.interval = 1;
    state.reps = 0;
    await DB.putSR(state);
  },

  /**
   * Get mastery % for a list of question IDs
   * Mastery = % of questions with interval >= 7 days
   */
  async getMastery(ids) {
    if (!ids || ids.length === 0) return 0;
    const states = await Promise.all(ids.map(id => SR.getState(id)));
    const mastered = states.filter(s => s.interval >= 7).length;
    return Math.round((mastered / ids.length) * 100);
  }
};

window.SR = SR;
