// Study Buddy Service Worker v1.0
const CACHE_NAME = 'studybuddy-v1';
const CONTENT_CACHE = 'studybuddy-content-v1';

// App shell assets — relative paths for arbitrary base paths (e.g. GitHub Pages or subfolders)
const SHELL_ASSETS = [
  './',
  './index.html',
  './css/app.css',
  './css/highlight.css',
  './js/app.js',
  './js/db.js',
  './js/router.js',
  './js/sr.js',
  './js/renderers.js',
  './js/highlight.min.js',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png'
];

// Install: cache shell
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(SHELL_ASSETS))
      .then(() => self.skipWaiting())
  );
});

// Activate: clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys
        .filter(k => k !== CACHE_NAME && k !== CONTENT_CACHE)
        .map(k => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

// Fetch: network-first for content JSON, cache-first for shell
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // Content JSON: network-first, fallback to cache
  if (url.pathname.includes('/content/')) {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          const clone = response.clone();
          caches.open(CONTENT_CACHE).then(c => c.put(event.request, clone));
          return response;
        })
        .catch(() => caches.match(event.request))
    );
    return;
  }

  // Shell: cache-first
  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;
      return fetch(event.request).then(response => {
        if (response && response.status === 200) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(c => c.put(event.request, clone));
        }
        return response;
      });
    })
  );
});

// Message: cache all content files on demand
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'CACHE_CONTENT') {
    const urls = event.data.urls || [];
    caches.open(CONTENT_CACHE).then(cache =>
      Promise.all(urls.map(u => cache.add(u).catch(() => null)))
    ).then(() => {
      event.ports[0] && event.ports[0].postMessage({ done: true });
    });
  }
});
