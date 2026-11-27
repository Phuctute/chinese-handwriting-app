// Service Worker for Chép Tay Tiếng Trung PWA
const CACHE_NAME = 'cheptay-v6.5.1-clean-templates-strict-baseline';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json',
  './assets/favicon.png',
  './assets/icon-192.png',
  './assets/icon-512.png',
  './assets/apple-touch-icon.png',
  './assets/ai_calibrated_lines.json',
  './assets/so_do_ve_tay_but_bi_xanh.jpg',
  './assets/so_do_sgk_goc.jpg',
  './assets/so_do_chatgpt_but_bi.jpg',
  './assets/so_do_chep_but_bi_xanh.jpg',
  './assets/notebook_thanhnam_spread.jpg',
  './assets/notebook_thanhnam_left.jpg',
  './assets/notebook_thanhnam_right.jpg',
  './assets/notebook_thanhnam_single2.jpg',
  './fonts/JasonHandwriting5.woff2',
  './fonts/JasonHandwriting3.woff2',
  './fonts/JasonHandwriting5.ttf',
  './fonts/JasonHandwriting3.ttf',
  './fonts/LongCang.ttf',
  './fonts/ZhiMangXing.ttf',
  './fonts/KleeOne.ttf',
  './fonts/LiuJianMaoCao.ttf'
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

  // Only handle same-origin requests; allow external CDNs (Tesseract, wasm, tessdata) to stream directly
  if (!req.url.startsWith(self.location.origin)) {
    return;
  }

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
      }).catch(() => caches.match(req, { ignoreSearch: true }))
    );
    return;
  }

  // For static assets, try cache first, then network
  event.respondWith(
    caches.match(req, { ignoreSearch: true }).then((cached) => {
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
