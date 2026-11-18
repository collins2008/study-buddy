// db.js — IndexedDB wrapper for Study Buddy
// Stores: progress, sr_state, stars, flags, settings

const DB_NAME = 'studybuddy';
const DB_VERSION = 1;

let _db = null;

function openDB() {
  if (_db) return Promise.resolve(_db);
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(DB_NAME, DB_VERSION);
    req.onupgradeneeded = e => {
      const db = e.target.result;
      // Question history: { id, correct, wrong, skipped, lastSeen, confidences[] }
      if (!db.objectStoreNames.contains('history')) {
        const hs = db.createObjectStore('history', { keyPath: 'id' });
        hs.createIndex('course', 'course');
        hs.createIndex('topic', 'topic');
      }
      // SR state: { id, interval, ef, due, reps }
      if (!db.objectStoreNames.contains('sr')) {
        db.createObjectStore('sr', { keyPath: 'id' });
      }
      // Stars: { id, starred: bool }
      if (!db.objectStoreNames.contains('stars')) {
        db.createObjectStore('stars', { keyPath: 'id' });
      }
      // Flags (reports): { id, note, ts }
      if (!db.objectStoreNames.contains('flags')) {
        const fs = db.createObjectStore('flags', { keyPath: 'id' });
        fs.createIndex('ts', 'ts');
      }
      // Settings: { key, value }
      if (!db.objectStoreNames.contains('settings')) {
        db.createObjectStore('settings', { keyPath: 'key' });
      }
    };
    req.onsuccess = e => { _db = e.target.result; resolve(_db); };
    req.onerror = () => reject(req.error);
  });
}

function tx(storeName, mode = 'readonly') {
  return _db.transaction(storeName, mode).objectStore(storeName);
}

function dbGet(store, key) {
  return openDB().then(db => new Promise((res, rej) => {
    const r = db.transaction(store).objectStore(store).get(key);
    r.onsuccess = () => res(r.result);
    r.onerror = () => rej(r.error);
  }));
}

function dbPut(store, value) {
  return openDB().then(db => new Promise((res, rej) => {
    const r = db.transaction(store, 'readwrite').objectStore(store).put(value);
    r.onsuccess = () => res(r.result);
    r.onerror = () => rej(r.error);
  }));
}

function dbGetAll(store) {
  return openDB().then(db => new Promise((res, rej) => {
    const r = db.transaction(store).objectStore(store).getAll();
    r.onsuccess = () => res(r.result);
    r.onerror = () => rej(r.error);
  }));
}

function dbDelete(store, key) {
  return openDB().then(db => new Promise((res, rej) => {
    const r = db.transaction(store, 'readwrite').objectStore(store).delete(key);
    r.onsuccess = () => res();
    r.onerror = () => rej(r.error);
  }));
}

// ---- High-level API ----

async function getSetting(key, defaultVal = null) {
  const r = await dbGet('settings', key);
  return r ? r.value : defaultVal;
}

async function setSetting(key, value) {
  return dbPut('settings', { key, value });
}

async function getHistory(id) {
  return dbGet('history', id);
}

async function getAllHistory() {
  return dbGetAll('history');
}

async function recordAnswer(questionId, course, topic, correct, confidence) {
  const existing = await dbGet('history', questionId) || {
    id: questionId, course, topic,
    correct: 0, wrong: 0, skipped: 0,
    lastSeen: null, confidences: []
  };
  if (correct === true)       existing.correct++;
  else if (correct === false) existing.wrong++;
  else                        existing.skipped++;
  existing.lastSeen = Date.now();
  if (confidence !== undefined) {
    existing.confidences.push({ confidence, correct, ts: Date.now() });
    if (existing.confidences.length > 100) existing.confidences.shift();
  }
  return dbPut('history', existing);
}

async function getSR(id) {
  return dbGet('sr', id);
}

async function putSR(srObj) {
  return dbPut('sr', srObj);
}

async function getAllSR() {
  return dbGetAll('sr');
}

async function getStars() {
  const all = await dbGetAll('stars');
  return new Set(all.filter(s => s.starred).map(s => s.id));
}

async function toggleStar(id) {
  const existing = await dbGet('stars', id);
  const starred = existing ? !existing.starred : true;
  await dbPut('stars', { id, starred });
  return starred;
}

async function addFlag(questionId, note) {
  const existing = await dbGet('flags', questionId);
  await dbPut('flags', {
    id: questionId,
    note: note || '',
    ts: Date.now(),
    count: existing ? (existing.count + 1) : 1
  });
}

async function getAllFlags() {
  return dbGetAll('flags');
}

async function clearFlag(id) {
  return dbDelete('flags', id);
}

// ---- Export / Import ----

async function exportProgress() {
  const [history, sr, stars, flags, settings] = await Promise.all([
    dbGetAll('history'),
    dbGetAll('sr'),
    dbGetAll('stars'),
    dbGetAll('flags'),
    dbGetAll('settings')
  ]);
  return { version: 1, exportedAt: new Date().toISOString(), history, sr, stars, flags, settings };
}

async function importProgress(data) {
  if (!data || data.version !== 1) throw new Error('Invalid progress file format');
  const stores = ['history', 'sr', 'stars', 'flags', 'settings'];
  const keys   = ['history', 'sr', 'stars', 'flags', 'settings'];
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const t = db.transaction(stores, 'readwrite');
    t.oncomplete = resolve;
    t.onerror = () => reject(t.error);
    keys.forEach(k => {
      const store = t.objectStore(k);
      store.clear();
      (data[k] || []).forEach(r => store.put(r));
    });
  });
}

// ---- Streak ----

async function updateStreak() {
  const today = new Date().toDateString();
  const lastActive = await getSetting('lastActive', null);
  let streak = await getSetting('streak', 0);
  const yesterday = new Date(Date.now() - 86400000).toDateString();

  if (lastActive === today) return streak; // already counted today
  if (lastActive === yesterday) streak++; // consecutive day
  else streak = 1; // reset

  await setSetting('lastActive', today);
  await setSetting('streak', streak);
  return streak;
}

async function getStreak() {
  return getSetting('streak', 0);
}

// ---- Daily Goal ----
async function getDailyGoalProgress() {
  const goal = await getSetting('dailyGoal', 20);
  const today = new Date().toDateString();
  const done = await getSetting('dailyDone_' + today, 0);
  return { done, goal };
}

async function incrementDailyDone() {
  const today = new Date().toDateString();
  const key = 'dailyDone_' + today;
  const done = await getSetting(key, 0);
  await setSetting(key, done + 1);
  return done + 1;
}

// Expose globally
window.DB = {
  openDB, getSetting, setSetting,
  getHistory, getAllHistory, recordAnswer,
  getSR, putSR, getAllSR,
  getStars, toggleStar,
  addFlag, getAllFlags, clearFlag,
  exportProgress, importProgress,
  updateStreak, getStreak,
  getDailyGoalProgress, incrementDailyDone
};
