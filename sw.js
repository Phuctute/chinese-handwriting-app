// Service Worker for Chép Tay Tiếng Trung PWA
const CACHE_NAME = 'cheptay-v2.1';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json',
  './assets/favicon.png',
  './assets/icon-192.png',
  './assets/icon-512.png',
  './assets/apple-touch-icon.png',
  './assets/notebook_thanhnam_spread.jpg',
  './assets/notebook_thanhnam_spread_warm.jpg',
  './assets/notebook_hongha_spread.jpg',
  './assets/notebook_hongha_spread_warm.jpg',
  './assets/notebook_tianzige_spread.jpg',
  './assets/notebook_oli_spread.jpg',
  './assets/notebook_warm_spread.jpg',
  './assets/notebook_default.jpg',
  './assets/notebook_thanhnam_right.jpg',
  './assets/notebook_thanhnam_left.jpg',
  './assets/notebook_thanhnam_warm.jpg',
  './assets/notebook_hongha_1.jpg',
  './assets/notebook_hongha_2.jpg',
  './assets/notebook_hongha_warm.jpg',
  './assets/notebook_tianzige.jpg',
  './assets/notebook_oli.jpg',
  './assets/notebook_warm.jpg',
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
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  // For navigation requests, try network first, then cache
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req).catch(() => caches.match('./index.html'))
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
      }).catch(() => {
        // Fallback if offline
        return cached;
      });
    })
  );
});
