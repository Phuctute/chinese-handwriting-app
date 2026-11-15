// Service Worker for Chép Tay Tiếng Trung PWA
const CACHE_NAME = 'cheptay-v5.8.3-pure-spreads';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json',
  './assets/favicon.png',
  './assets/icon-192.png',
  './assets/icon-512.png',
  './assets/apple-touch-icon.png',
  './assets/notebook_thanhnam_spread.jpg',
  './assets/notebook_hongha_spread.jpg',
  './assets/notebook_thanhnam_spread_clean.jpg',
  './assets/notebook_campus_spread.jpg',
  './assets/notebook_thanhnam_left.jpg',
  './assets/notebook_hongha_2.jpg',
  './assets/notebook_clean_single.jpg',
  './assets/notebook_campus_single.jpg',
  './fonts/JasonHandwriting5.ttf',
  './fonts/JasonHandwriting3.ttf'
];

self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE).catch((err) => {
        console.warn('Pre-cache partial warning:', err);
      });
    })
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('Purging old cache:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  // For navigation & HTML, try network first to ensure latest updates
  if (req.mode === 'navigate' || req.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      fetch(req).catch(() => caches.match('./index.html'))
    );
    return;
  }

  // Network-first for assets with version query parameter (?v=...) to ensure instant update
  if (req.url.includes('?v=') || req.url.includes('&v=')) {
    event.respondWith(
      fetch(req).then((res) => {
        if (res && res.status === 200 && req.method === 'GET') {
          const resClone = res.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(req, resClone));
        }
        return res;
      }).catch(() => caches.match(req))
    );
    return;
  }

  // For static assets, try cache first, then network
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req).then((res) => {
        if (res && res.status === 200 && req.method === 'GET' && !req.url.startsWith('chrome-extension')) {
          const resClone = res.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(req, resClone));
        }
        return res;
      }).catch(() => cached);
    })
  );
});
