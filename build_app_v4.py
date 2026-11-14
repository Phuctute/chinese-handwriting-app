# -*- coding: utf-8 -*-
"""
Builder v4: Complete overhaul with all requested features.
"""

import os

app_dir = r"C:\Users\phucv\.gemini\antigravity\scratch\chinese-handwriting-app"
index_html_path = os.path.join(app_dir, "index.html")

html_code = r'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>Chép Tay AI - Vở Viết Tay Chữ Hán Thông Minh</title>
  <meta name="description" content="Chuyển văn bản tiếng Trung thành chữ viết tay tự nhiên uốn theo dòng kẻ vở học sinh, vẽ lại sơ đồ và bảng thông minh không đè dòng.">

  <!-- PWA Metadata & Favicons -->
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#0d1117">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Chép Tay">
  <link rel="icon" type="image/png" href="assets/favicon.png">
  <link rel="apple-touch-icon" href="assets/apple-touch-icon.png">

  <!-- Preload Authentic Handwriting Fonts -->
  <link rel="preload" href="fonts/JasonHandwriting5.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="preload" href="fonts/JasonHandwriting3.ttf" as="font" type="font/ttf" crossorigin>

  <!-- Google Fonts & OCR Library -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js"></script>

  <style>
    /* Local authentic handwriting fonts (JasonHandwriting 1-7) */
    @font-face {
      font-family: 'JasonHandwriting1';
      src: url('fonts/JasonHandwriting1.ttf') format('truetype');
      font-display: swap;
    }
    @font-face {
      font-family: 'JasonHandwriting2';
      src: url('fonts/JasonHandwriting2.ttf') format('truetype');
      font-display: swap;
    }
    @font-face {
      font-family: 'JasonHandwriting3';
      src: url('fonts/JasonHandwriting3.ttf') format('truetype');
      font-display: swap;
    }
    @font-face {
      font-family: 'JasonHandwriting4';
      src: url('fonts/JasonHandwriting4.ttf') format('truetype');
      font-display: swap;
    }
    @font-face {
      font-family: 'JasonHandwriting5';
      src: url('fonts/JasonHandwriting5.ttf') format('truetype');
      font-display: swap;
    }
    @font-face {
      font-family: 'JasonHandwriting6';
      src: url('fonts/JasonHandwriting6.ttf') format('truetype');
      font-display: swap;
    }
    @font-face {
      font-family: 'JasonHandwriting7';
      src: url('fonts/JasonHandwriting7.ttf') format('truetype');
      font-display: swap;
    }

    :root {
      --bg-base: #0b0d13;
      --bg-card: #131722;
      --bg-card-hover: #181d2b;
      --bg-input: #0e111a;
      --border-color: #232838;
      --border-hover: #333a50;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --accent: #38bdf8;
      --accent-glow: rgba(56, 189, 248, 0.18);
      --accent-hover: #0284c7;
      --success: #10b981;
      --danger: #ef4444;
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 14px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-base);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    /* Top Navigation Bar */
    header.app-header {
      background: rgba(13, 17, 23, 0.92);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      height: 60px;
      padding: 0 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: var(--text-main);
    }
    .brand-icon {
      width: 34px;
      height: 34px;
      background: linear-gradient(135deg, #0284c7, #38bdf8);
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
    }
    .brand-text h1 {
      font-size: 16px;
      font-weight: 700;
      letter-spacing: -0.3px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .brand-text p {
      font-size: 11px;
      color: var(--text-dim);
    }
    .brand-badge {
      font-size: 9px;
      font-weight: 600;
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent);
      padding: 1px 6px;
      border-radius: 99px;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      font-size: 13px;
      font-weight: 600;
      padding: 7px 14px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.15s ease;
      white-space: nowrap;
    }
    .btn-secondary {
      background: var(--bg-card);
      border-color: var(--border-color);
      color: var(--text-main);
    }
    .btn-secondary:hover {
      background: var(--bg-card-hover);
      border-color: var(--border-hover);
    }
    .btn-secondary.active {
      background: var(--accent-glow);
      border-color: var(--accent);
      color: var(--accent);
    }
    .btn-primary {
      background: var(--accent);
      color: #0b0d13;
    }
    .btn-primary:hover {
      background: #7dd3fc;
    }
    .btn-icon {
      padding: 7px;
      border-radius: var(--radius-sm);
    }

    /* Mobile Segmented Switch (Soạn Thảo vs Xem Vở) */
    .mobile-view-switch {
      display: none;
      padding: 8px 14px;
      background: var(--bg-card);
      border-bottom: 1px solid var(--border-color);
    }
    .segmented-switch {
      display: flex;
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 3px;
      gap: 3px;
    }
    .switch-pill {
      flex: 1;
      padding: 7px 12px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      border: none;
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s ease;
    }
    .switch-pill.active {
      background: var(--accent);
      color: #0b0d13;
      box-shadow: 0 1px 4px rgba(0,0,0,0.3);
    }

    /* Main Container Layout */
    .main-layout {
      flex: 1;
      display: grid;
      grid-template-columns: 460px 1fr;
      min-height: calc(100vh - 60px);
    }

    /* Left Panel: Tools & Editor */
    .left-panel {
      background: var(--bg-base);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      height: calc(100vh - 60px);
      overflow-y: auto;
    }

    /* Tab Navigation */
    .nav-tabs {
      display: flex;
      background: var(--bg-card);
      border-bottom: 1px solid var(--border-color);
      padding: 0 10px;
      gap: 4px;
      position: sticky;
      top: 0;
      z-index: 10;
    }
    .nav-tab {
      padding: 12px 14px;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      border: none;
      background: transparent;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      border-bottom: 2px solid transparent;
      transition: all 0.15s ease;
    }
    .nav-tab:hover {
      color: var(--text-main);
    }
    .nav-tab.active {
      color: var(--accent);
      border-bottom-color: var(--accent);
    }

    .tab-panel {
      display: none;
      padding: 16px;
      flex-direction: column;
      gap: 16px;
    }
    .tab-panel.active {
      display: flex;
    }

    /* Section Cards */
    .section-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .card-title {
      font-size: 13px;
      font-weight: 600;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .badge {
      font-size: 11px;
      padding: 2px 7px;
      border-radius: 99px;
      font-weight: 600;
      background: rgba(148, 163, 184, 0.15);
      color: var(--text-muted);
    }

    /* Text Editor Area */
    .editor-wrap {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    textarea.text-input {
      width: 100%;
      height: 220px;
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 12px;
      color: var(--text-main);
      font-family: inherit;
      font-size: 14px;
      line-height: 1.6;
      resize: vertical;
      transition: border-color 0.15s ease;
    }
    textarea.text-input:focus {
      outline: none;
      border-color: var(--accent);
      box-shadow: 0 0 0 2px var(--accent-glow);
    }

    /* Quick Toolbar */
    .quick-toolbar {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    .tool-chip {
      background: var(--bg-base);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 500;
      padding: 5px 10px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
    }
    .tool-chip:hover {
      border-color: var(--border-hover);
      color: var(--text-main);
    }
    .tool-chip.active {
      background: var(--accent-glow);
      border-color: var(--accent);
      color: var(--accent);
    }

    /* Visual Grid Selectors */
    .visual-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
    }
    .visual-card {
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 10px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 6px;
      transition: all 0.15s ease;
      position: relative;
    }
    .visual-card:hover {
      border-color: var(--border-hover);
      background: var(--bg-card-hover);
    }
    .visual-card.active {
      border-color: var(--accent);
      background: var(--accent-glow);
    }
    .visual-card-icon {
      width: 28px;
      height: 28px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.05);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-main);
    }
    .visual-card.active .visual-card-icon {
      background: var(--accent);
      color: #0b0d13;
    }
    .visual-card-title {
      font-size: 12px;
      font-weight: 600;
      color: var(--text-main);
    }
    .visual-card-desc {
      font-size: 10.5px;
      color: var(--text-dim);
      line-height: 1.3;
    }

    /* Template Thumbnails */
    .template-card {
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      overflow: hidden;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      transition: all 0.15s ease;
    }
    .template-card:hover {
      border-color: var(--border-hover);
      transform: translateY(-1px);
    }
    .template-card.active {
      border-color: var(--accent);
      box-shadow: 0 0 0 2px var(--accent-glow);
    }
    .template-preview {
      width: 100%;
      height: 75px;
      object-fit: cover;
      background: #1e2230;
    }
    .template-meta {
      padding: 8px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .template-title {
      font-size: 11.5px;
      font-weight: 600;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .template-sub {
      font-size: 10px;
      color: var(--text-dim);
    }

    /* Controls & Sliders */
    .form-row {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .form-row-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .form-label {
      font-size: 12px;
      font-weight: 500;
      color: var(--text-muted);
    }
    .form-value {
      font-size: 11px;
      font-weight: 600;
      color: var(--accent);
      background: var(--bg-input);
      padding: 1px 6px;
      border-radius: 4px;
      border: 1px solid var(--border-color);
    }
    input[type="range"] {
      -webkit-appearance: none;
      width: 100%;
      height: 5px;
      border-radius: 99px;
      background: var(--border-color);
      outline: none;
    }
    input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--accent);
      cursor: pointer;
      border: 2px solid var(--bg-card);
      box-shadow: 0 1px 3px rgba(0,0,0,0.5);
    }

    select.form-select, input[type="text"].form-input, input[type="number"].form-input {
      width: 100%;
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 8px 10px;
      font-size: 13px;
      border-radius: var(--radius-sm);
      outline: none;
      transition: border-color 0.15s ease;
    }
    select.form-select:focus, input[type="text"].form-input:focus {
      border-color: var(--accent);
    }

    /* Right Panel: Canvas Preview */
    .right-panel {
      background: #080a0f;
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }

    /* Canvas Top Bar (Page navigation & Zoom) */
    .canvas-toolbar {
      background: rgba(13, 17, 23, 0.95);
      border-bottom: 1px solid var(--border-color);
      padding: 8px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      z-index: 10;
    }
    .page-controller {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .page-pill {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-main);
      background: var(--bg-card);
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      min-width: 90px;
      text-align: center;
    }
    .zoom-controller {
      display: flex;
      align-items: center;
      gap: 4px;
    }

    /* Canvas Container */
    .canvas-viewport {
      flex: 1;
      overflow: auto;
      display: flex;
      align-items: flex-start;
      justify-content: center;
      padding: 24px 16px;
      position: relative;
    }
    .canvas-wrapper {
      position: relative;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.75), 0 2px 8px rgba(0, 0, 0, 0.5);
      border-radius: 4px;
      overflow: hidden;
      line-height: 0;
    }
    #renderCanvas {
      display: block;
      max-width: 100%;
      height: auto;
    }

    /* Toast Notification */
    .toast {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #1e293b;
      color: #f8fafc;
      border: 1px solid #334155;
      padding: 10px 18px;
      border-radius: 99px;
      font-size: 13px;
      font-weight: 500;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      display: flex;
      align-items: center;
      gap: 8px;
      z-index: 1000;
      opacity: 0;
      pointer-events: none;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .toast.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
      pointer-events: auto;
    }

    /* Dropzone */
    .dropzone {
      border: 2px dashed var(--border-color);
      border-radius: var(--radius-sm);
      padding: 16px;
      text-align: center;
      background: var(--bg-input);
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .dropzone:hover {
      border-color: var(--accent);
      background: var(--accent-glow);
    }
    .dropzone-title {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-main);
      margin-top: 6px;
    }
    .dropzone-sub {
      font-size: 11px;
      color: var(--text-dim);
      margin-top: 3px;
    }

    /* Responsive Mobile Rules */
    @media (max-width: 991px) {
      .main-layout {
        grid-template-columns: 1fr;
        height: auto;
        min-height: calc(100vh - 110px);
      }
      .mobile-view-switch {
        display: block;
        position: sticky;
        top: 60px;
        z-index: 90;
      }
      .left-panel {
        height: auto;
        border-right: none;
        display: flex;
      }
      .right-panel {
        display: none;
        min-height: calc(100vh - 110px);
      }

      body.view-preview .left-panel {
        display: none;
      }
      body.view-preview .right-panel {
        display: flex;
      }

      .canvas-viewport {
        padding: 12px 6px;
      }
    }
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header class="app-header">
    <a href="#" class="brand">
      <div class="brand-icon">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 20h9"/>
          <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
        </svg>
      </div>
      <div class="brand-text">
        <h1>Chép Tay AI <span class="brand-badge">24/7 Online</span></h1>
        <p>Vở viết tay chữ Hán & Sơ đồ thông minh</p>
      </div>
    </a>

    <div class="header-actions">
      <!-- PWA Install Button -->
      <button class="btn btn-secondary btn-icon" id="btnInstallPwa" onclick="installPWA()" title="Thêm vào màn hình chính điện thoại">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="5" y="2" width="14" height="20" rx="2" ry="2"/>
          <line x1="12" y1="18" x2="12.01" y2="18"/>
        </svg>
      </button>

      <!-- Download Button -->
      <button class="btn btn-primary" onclick="downloadCurrentPageImage()">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
          <polyline points="7 10 12 15 17 10"/>
          <line x1="12" y1="15" x2="12" y2="3"/>
        </svg>
        <span>Tải Ảnh Vở</span>
      </button>
    </div>
  </header>

  <!-- Mobile View Switcher (Sticky below header) -->
  <div class="mobile-view-switch">
    <div class="segmented-switch">
      <button class="switch-pill active" id="btnSwitchEdit" onclick="switchMobileView('editor')">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
        Soạn Thảo
      </button>
      <button class="switch-pill" id="btnSwitchPreview" onclick="switchMobileView('preview')">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
        Xem Trang Vở
      </button>
    </div>
  </div>

  <!-- Main Layout -->
  <main class="main-layout">
    
    <!-- LEFT PANEL: Navigation Tabs & Settings -->
    <section class="left-panel" id="leftPanel">
      <nav class="nav-tabs">
        <button class="nav-tab active" onclick="switchTab('editor-tab')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
          Soạn Bài
        </button>
        <button class="nav-tab" onclick="switchTab('diagram-tab')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>
          Sơ Đồ & Bảng
        </button>
        <button class="nav-tab" onclick="switchTab('style-tab')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          Kiểu Vở & Bút
        </button>
      </nav>

      <!-- TAB 1: SOẠN BÀI (EDITOR) -->
      <div class="tab-panel active" id="editor-tab">
        <div class="section-card">
          <div class="card-header">
            <span class="card-title">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              Nội dung văn bản (Chữ Hán)
            </span>
            <span class="badge" id="charCountBadge">0 chữ • 0 dòng</span>
          </div>

          <div class="editor-wrap">
            <textarea 
              id="textInput" 
              class="text-input" 
              placeholder="Nhập hoặc dán chữ Hán cần chép tay vào đây...&#10;(Gõ ~~từ sai~~ để tạo hiệu ứng gạch chéo tự nhiên)"
            ></textarea>
          </div>

          <!-- Quick Action Tools -->
          <div class="quick-toolbar">
            <button class="tool-chip" onclick="document.getElementById('ocrFileInput').click()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
              Quét ảnh (OCR)
            </button>
            <input type="file" id="ocrFileInput" accept="image/*" style="display:none;" onchange="handleOcrUpload(this.files[0])">

            <button class="tool-chip" onclick="toggleTradSimp()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>
              Phồn ⇄ Giản
            </button>

            <button class="tool-chip" onclick="insertStrikeSnippet()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="12" x2="20" y2="12"/><path d="m16 6-4-2-4 2"/><path d="m8 18 4 2 4-2"/></svg>
              ~~Gạch xóa~~
            </button>

            <button class="tool-chip" onclick="toggleSkipLine()" id="btnSkipLine">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/></svg>
              Cách dòng: Tắt
            </button>

            <button class="tool-chip" onclick="clearText()" style="margin-left:auto; color:#fca5a5;">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
              Xóa
            </button>
          </div>
        </div>

        <!-- Sample Texts -->
        <div class="section-card">
          <div class="card-header">
            <span class="card-title">Bài tập mẫu tham khảo</span>
          </div>
          <div style="display:flex; gap:8px;">
            <button class="btn btn-secondary" style="flex:1; font-size:12px;" onclick="loadSample('taohuayuan')">Đào Hoa Nguyên Ký</button>
            <button class="btn btn-secondary" style="flex:1; font-size:12px;" onclick="loadSample('vocab')">Vở Từ Vựng HSK</button>
          </div>
        </div>
      </div>

      <!-- TAB 2: SƠ ĐỒ & BẢNG (AI HANDWRITTEN DIAGRAMS & TABLES) -->
      <div class="tab-panel" id="diagram-tab">
        
        <!-- AI Photo Extraction Card (Highlighted) -->
        <div class="section-card" style="border: 1px solid var(--accent); background: linear-gradient(180deg, rgba(56, 189, 248, 0.08), var(--bg-card));">
          <div class="card-header">
            <span class="card-title" style="color:var(--accent);">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>
              AI Tự Động Vẽ Lại Từ Ảnh Chụp
            </span>
            <span class="badge" style="background:var(--accent); color:#0b0d13;">Thông minh</span>
          </div>
          <p style="font-size:11.5px; color:var(--text-muted); line-height:1.4;">
            Tải ảnh chụp bảng từ vựng hoặc sơ đồ của bạn. AI sẽ nhận diện cấu trúc, trích xuất chữ và <b>vẽ lại hoàn toàn bằng nét bút viết tay</b> đồng bộ với phông chữ đang chọn.
          </p>

          <div class="dropzone" onclick="document.getElementById('aiPhotoFileInput').click()">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            <div class="dropzone-title">Chạm để chọn ảnh bảng / sơ đồ chụp từ vở</div>
            <div class="dropzone-sub">AI tự phân tích hàng, cột và vẽ lại bằng nét chữ viết tay thật</div>
          </div>
          <input type="file" id="aiPhotoFileInput" accept="image/*" style="display:none;" onchange="handleAiPhotoUpload(this.files[0])">
        </div>

        <!-- Presets Selector Grid -->
        <div class="section-card">
          <div class="card-header">
            <span class="card-title">Mẫu Sơ Đồ & Bảng Viết Tay</span>
            <span class="badge" id="diagramStatusBadge" style="background:#475569; color:#fff;">Đang tắt</span>
          </div>

          <div class="visual-grid">
            <div class="visual-card active" id="cardDiagNone" onclick="selectDiagramType('none')">
              <div class="visual-card-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg>
              </div>
              <div class="visual-card-title">Không dùng</div>
              <div class="visual-card-desc">Chỉ viết văn bản thông thường</div>
            </div>

            <div class="visual-card" id="cardDiagTable2" onclick="selectDiagramType('table2')">
              <div class="visual-card-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M10 3v18"/></svg>
              </div>
              <div class="visual-card-title">Bảng từ vựng (2 cột)</div>
              <div class="visual-card-desc">Chữ Hán & Giải nghĩa / Ví dụ</div>
            </div>

            <div class="visual-card" id="cardDiagTable3" onclick="selectDiagramType('table3')">
              <div class="visual-card-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M9 3v18"/><path d="M15 3v18"/></svg>
              </div>
              <div class="visual-card-title">Bảng từ vựng (3 cột)</div>
              <div class="visual-card-desc">Chữ Hán, Phiên âm Pinyin & Nghĩa</div>
            </div>

            <div class="visual-card" id="cardDiagMindmap" onclick="selectDiagramType('mindmap')">
              <div class="visual-card-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="6" y1="3" x2="6" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/></svg>
              </div>
              <div class="visual-card-title">Sơ đồ tư duy (Mindmap)</div>
              <div class="visual-card-desc">Chủ đề trung tâm & các nhánh cong</div>
            </div>

            <div class="visual-card" id="cardDiagProcess" onclick="selectDiagramType('process')">
              <div class="visual-card-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="6" height="10" rx="1"/><rect x="16" y="7" width="6" height="10" rx="1"/><path d="M8 12h8"/><path d="m13 9 3 3-3 3"/></svg>
              </div>
              <div class="visual-card-title">Sơ đồ quy trình (Flow)</div>
              <div class="visual-card-desc">Các bước nối tiếp bằng mũi tên</div>
            </div>

            <div class="visual-card" id="cardDiagCallout" onclick="selectDiagramType('callout')">
              <div class="visual-card-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
              </div>
              <div class="visual-card-title">Khung ghi chú / Chú thích</div>
              <div class="visual-card-desc">Khung bo tay viền lượn sóng nổi bật</div>
            </div>

            <div class="visual-card" id="cardDiagSketch" onclick="selectDiagramType('sketch')">
              <div class="visual-card-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 19 7-7 3 3-7 7-3-3z"/><path d="m18 13-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/></svg>
              </div>
              <div class="visual-card-title">Bảng vẽ tự do cảm ứng</div>
              <div class="visual-card-desc">Vẽ trực tiếp bằng tay hoặc bút stylus</div>
            </div>
          </div>
        </div>

        <!-- Position & Avoidance Controls -->
        <div class="section-card" id="diagPosBox" style="display:none;">
          <div class="card-header">
            <span class="card-title">Vị trí chèn & Chống đè dòng</span>
          </div>

          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
            <div class="form-row" id="spreadSideRow">
              <span class="form-label">Chọn trang (Trang đôi):</span>
              <select class="form-select" id="diagSpreadSide" onchange="updateDiagramPos()">
                <option value="right" selected>Trang Phải (Khuyên dùng)</option>
                <option value="left">Trang Trái</option>
              </select>
            </div>
            <div class="form-row">
              <span class="form-label">Số trang xuất hiện:</span>
              <input type="number" class="form-input" id="diagTargetPage" value="1" min="1" max="10" onchange="updateDiagramPos()">
            </div>
          </div>

          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px; margin-top: 8px;">
            <div class="form-row">
              <div class="form-row-header">
                <span class="form-label">Dòng bắt đầu:</span>
                <span class="form-value" id="diagStartVal">2</span>
              </div>
              <input type="range" id="diagStartSlider" min="0" max="22" value="2" oninput="updateDiagramPos()">
            </div>
            <div class="form-row">
              <div class="form-row-header">
                <span class="form-label">Số dòng chiếm:</span>
                <span class="form-value" id="diagSpanVal">9</span>
              </div>
              <input type="range" id="diagSpanSlider" min="2" max="18" value="9" oninput="updateDiagramPos()">
            </div>
          </div>
          <p style="font-size:11px; color:var(--success); margin-top:6px;">
            ✓ Chữ trong vở tự động nhảy qua các dòng này và tiếp tục viết bên dưới, không bao giờ bị đè chữ.
          </p>
        </div>

        <!-- SUBPANEL: BẢNG 2 CỘT -->
        <div class="section-card" id="subpanelTable2" style="display:none;">
          <div class="card-header">
            <span class="card-title">Nội dung Bảng từ vựng (2 Cột)</span>
          </div>
          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
            <div class="form-row">
              <span class="form-label">Tiêu đề Cột 1:</span>
              <input type="text" class="form-input" id="t2Col1" value="生詞 (Từ mới)" oninput="updateTable2Content()">
            </div>
            <div class="form-row">
              <span class="form-label">Tiêu đề Cột 2:</span>
              <input type="text" class="form-input" id="t2Col2" value="釋義與例句 (Giải nghĩa)" oninput="updateTable2Content()">
            </div>
          </div>
          <div class="form-row" style="margin-top:8px;">
            <span class="form-label">Các hàng (Từ vựng | Giải nghĩa):</span>
            <textarea class="text-input" id="t2Rows" style="height:100px; font-size:13px;" oninput="updateTable2Content()"></textarea>
          </div>
        </div>

        <!-- SUBPANEL: BẢNG 3 CỘT -->
        <div class="section-card" id="subpanelTable3" style="display:none;">
          <div class="card-header">
            <span class="card-title">Nội dung Bảng từ vựng (3 Cột)</span>
          </div>
          <div style="display:grid; grid-template-columns: 1fr 1fr 1.2fr; gap:8px;">
            <div class="form-row">
              <span class="form-label">Cột 1:</span>
              <input type="text" class="form-input" id="t3Col1" value="漢字" oninput="updateTable3Content()">
            </div>
            <div class="form-row">
              <span class="form-label">Cột 2:</span>
              <input type="text" class="form-input" id="t3Col2" value="拼音" oninput="updateTable3Content()">
            </div>
            <div class="form-row">
              <span class="form-label">Cột 3:</span>
              <input type="text" class="form-input" id="t3Col3" value="釋義 & 詞性" oninput="updateTable3Content()">
            </div>
          </div>
          <div class="form-row" style="margin-top:8px;">
            <span class="form-label">Các hàng (Chữ Hán | Pinyin | Nghĩa):</span>
            <textarea class="text-input" id="t3Rows" style="height:100px; font-size:13px;" oninput="updateTable3Content()"></textarea>
          </div>
        </div>

        <!-- SUBPANEL: MINDMAP -->
        <div class="section-card" id="subpanelMindmap" style="display:none;">
          <div class="card-header">
            <span class="card-title">Cấu trúc Sơ đồ tư duy</span>
          </div>
          <div class="form-row">
            <span class="form-label">Chủ đề trung tâm:</span>
            <input type="text" class="form-input" id="mindmapRootTitle" value="漢語語法 (Ngữ pháp Hán ngữ)" oninput="updateMindmapContent()">
          </div>
          <div class="form-row" style="margin-top:8px;">
            <span class="form-label">Các nhánh con (Mỗi dòng một nhánh):</span>
            <textarea class="text-input" id="mindmapBranchesArea" style="height:90px; font-size:13px;" oninput="updateMindmapContent()"></textarea>
          </div>
        </div>

        <!-- SUBPANEL: PROCESS FLOW -->
        <div class="section-card" id="subpanelProcess" style="display:none;">
          <div class="card-header">
            <span class="card-title">Sơ đồ quy trình / Bước làm</span>
          </div>
          <div class="form-row">
            <span class="form-label">Các bước thực hiện (Mỗi dòng một bước):</span>
            <textarea class="text-input" id="processStepsArea" style="height:90px; font-size:13px;" oninput="updateProcessContent()"></textarea>
          </div>
        </div>

        <!-- SUBPANEL: CALLOUT -->
        <div class="section-card" id="subpanelCallout" style="display:none;">
          <div class="card-header">
            <span class="card-title">Khung ghi chú viết tay</span>
          </div>
          <div class="form-row">
            <span class="form-label">Tiêu đề ghi chú:</span>
            <input type="text" class="form-input" id="calloutTitle" value="★ 重要筆記 (Lưu ý quan trọng)" oninput="updateCalloutContent()">
          </div>
          <div class="form-row" style="margin-top:8px;">
            <span class="form-label">Nội dung ghi chú:</span>
            <textarea class="text-input" id="calloutTextArea" style="height:80px; font-size:13px;" oninput="updateCalloutContent()"></textarea>
          </div>
        </div>

        <!-- SUBPANEL: SKETCHPAD -->
        <div class="section-card" id="subpanelSketch" style="display:none;">
          <div class="card-header">
            <span class="card-title">Bảng vẽ cảm ứng tay</span>
            <button class="btn btn-secondary" style="font-size:11px; padding:3px 8px;" onclick="clearSketch()">Xóa nét vẽ</button>
          </div>
          <div style="background:#fff; border-radius:6px; overflow:hidden; border:1px solid #cbd5e1;">
            <canvas id="sketchCanvas" width="400" height="180" style="width:100%; height:140px; display:block; cursor:crosshair; touch-action:none;"></canvas>
          </div>
        </div>

      </div>

      <!-- TAB 3: KIỂU VỞ & BÚT (STYLE & MARGINS) -->
      <div class="tab-panel" id="style-tab">
        <!-- Notebook Template Selection -->
        <div class="section-card">
          <div class="card-header">
            <span class="card-title">Mẫu Vở Học Sinh</span>
            <span class="badge" id="templateCountBadge">16 mẫu</span>
          </div>

          <!-- Template Category Pills -->
          <div style="display:flex; gap:6px;">
            <button class="tool-chip active" id="filterTplAll" onclick="filterTemplates('all')">Tất cả</button>
            <button class="tool-chip" id="filterTplSpread" onclick="filterTemplates('spread')">Trang Đôi (9)</button>
            <button class="tool-chip" id="filterTplSingle" onclick="filterTemplates('single')">Trang Đơn (7)</button>
          </div>

          <!-- Template Cards Grid -->
          <div class="visual-grid" id="templateGallery" style="max-height: 250px; overflow-y: auto; padding-right: 4px;"></div>
        </div>

        <!-- Pen & Handwriting Style -->
        <div class="section-card">
          <div class="card-header">
            <span class="card-title">Màu Mực & Phông Chữ Viết Tay</span>
          </div>

          <!-- Ink Selection -->
          <div class="form-row">
            <span class="form-label">Màu mực bút viết:</span>
            <div style="display:flex; gap:8px;">
              <button class="btn btn-secondary active" id="btnInkGel" style="flex:1;" onclick="setInkColor('gel_black')">
                <span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:#1c202a; margin-right:4px;"></span>
                Gel đen
              </button>
              <button class="btn btn-secondary" id="btnInkBlue" style="flex:1;" onclick="setInkColor('blue')">
                <span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:#1e3a8a; margin-right:4px;"></span>
                Bút bi xanh
              </button>
              <button class="btn btn-secondary" id="btnInkDeep" style="flex:1;" onclick="setInkColor('deep_black')">
                <span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:#000; margin-right:4px;"></span>
                Đen đậm
              </button>
            </div>
          </div>

          <!-- Font Selection with authentic "Xấu tự nhiên" fonts -->
          <div class="form-row" style="margin-top:6px;">
            <span class="form-label">Kiểu chữ viết tay (Đã tối ưu tự nhiên):</span>
            <select class="form-select" id="fontSelector" onchange="setFont(this.value)">
              <option value="JasonHandwriting5" selected>✨ Jason 5 (Xấu tự nhiên, hơi ẩu, chữ học sinh - Chuẩn nhất)</option>
              <option value="JasonHandwriting4">🌪️ Jason 4 (Nét nghiêng tự do, viết tốc ký nhanh)</option>
              <option value="JasonHandwriting3">🖋️ Jason 3 (Bút gel tự nhiên, nét đều tay)</option>
              <option value="JasonHandwriting2">🌿 Jason 2 (Nét bút thanh mảnh, chữ học trò)</option>
              <option value="JasonHandwriting1">📝 Jason 1 (Chữ nắn nót, bút bi trung học)</option>
              <option value="JasonHandwriting6">✒️ Jason 6 (Bút gel đậm nét, xô lệch ngẫu nhiên)</option>
              <option value="JasonHandwriting7">🖊️ Jason 7 (Nét dày, nét móc rõ ràng)</option>
            </select>
          </div>

          <!-- Size and Messiness -->
          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px; margin-top:8px;">
            <div class="form-row">
              <div class="form-row-header">
                <span class="form-label">Cỡ chữ:</span>
                <span class="form-value" id="fontSizeVal">20px</span>
              </div>
              <input type="range" id="fontSizeSlider" min="15" max="26" value="20" oninput="updateFontSize(this.value)">
            </div>
            <div class="form-row">
              <div class="form-row-header">
                <span class="form-label">Độ ngoáy tự nhiên:</span>
                <span class="form-value" id="messinessVal">45%</span>
              </div>
              <input type="range" id="messinessSlider" min="0" max="90" value="45" oninput="updateMessiness(this.value)">
            </div>
          </div>
        </div>

        <!-- Margin & Line Controls (Căn lề trên dưới đẩy lên/xuống) -->
        <div class="section-card">
          <div class="card-header">
            <span class="card-title">Căn Lề Trang Vở & Canh Dòng Kẻ</span>
          </div>

          <!-- Top / Bottom Margin Shift -->
          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
            <div class="form-row">
              <div class="form-row-header">
                <span class="form-label">Lề trên (Bỏ trống đầu):</span>
                <span class="form-value" id="topMarginVal">0 dòng</span>
              </div>
              <input type="range" id="topMarginSlider" min="0" max="8" value="0" oninput="updateTopMargin(this.value)">
              <span style="font-size:10px; color:var(--text-dim);">Kéo để đẩy chữ thụt xuống dưới</span>
            </div>
            <div class="form-row">
              <div class="form-row-header">
                <span class="form-label">Lề dưới (Bỏ trống cuối):</span>
                <span class="form-value" id="bottomMarginVal">0 dòng</span>
              </div>
              <input type="range" id="bottomMarginSlider" min="0" max="8" value="0" oninput="updateBottomMargin(this.value)">
              <span style="font-size:10px; color:var(--text-dim);">Chừa dòng đáy trang không viết</span>
            </div>
          </div>

          <!-- Baseline micro vertical offset -->
          <div class="form-row" style="margin-top:10px;">
            <div class="form-row-header">
              <span class="form-label">Cao độ chữ trên dòng (Nâng/hạ micro):</span>
              <span class="form-value" id="baselineVal">0px</span>
            </div>
            <input type="range" id="baselineSlider" min="-15" max="15" value="0" oninput="updateBaselineOffset(this.value)">
            <span style="font-size:10.5px; color:var(--text-dim);">Căn chỉnh cho nét chữ nằm khít rịt đúng trên vạch kẻ xanh của vở</span>
          </div>

          <!-- Left / Right Margin -->
          <div class="form-row" style="margin-top:8px;">
            <div class="form-row-header">
              <span class="form-label">Độ rộng thụt lề 2 bên:</span>
              <span class="form-value" id="marginVal">0px</span>
            </div>
            <input type="range" id="marginSlider" min="-20" max="20" value="0" oninput="updateMarginOffset(this.value)">
            <span style="font-size:10.5px; color:var(--text-dim);">Chữ được khóa chặt trong lề vở, không bao giờ viết thò ra ngoài hay chạm gáy</span>
          </div>
        </div>

      </div>
    </section>

    <!-- RIGHT PANEL: Canvas Viewport & Pagination -->
    <section class="right-panel" id="rightPanel">
      <div class="canvas-toolbar">
        <div class="page-controller">
          <button class="btn btn-secondary btn-icon" onclick="prevPage()" title="Trang trước">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
          </button>
          <span class="page-pill" id="pageIndicator">Trang 1 / 1</span>
          <button class="btn btn-secondary btn-icon" onclick="nextPage()" title="Trang tiếp">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
          </button>
        </div>

        <div class="zoom-controller">
          <button class="btn btn-secondary btn-icon" onclick="adjustZoom(-0.1)" title="Thu nhỏ">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
          </button>
          <button class="btn btn-secondary" style="font-size:11.5px; padding:6px 10px;" onclick="resetZoom()" id="zoomLevelBtn">100%</button>
          <button class="btn btn-secondary btn-icon" onclick="adjustZoom(0.1)" title="Phóng to">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
          </button>
          <button class="btn btn-secondary" style="font-size:11.5px; padding:6px 10px;" onclick="fitCanvasToViewport()">Vừa</button>
        </div>
      </div>

      <div class="canvas-viewport" id="viewport">
        <div class="canvas-wrapper" id="canvasWrapper">
          <canvas id="renderCanvas" width="1024" height="768"></canvas>
        </div>
      </div>
    </section>

  </main>

  <!-- Notification Toast -->
  <div class="toast" id="toast">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2.5"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
    <span id="toastMsg">Thao tác thành công</span>
  </div>

  <!-- SCRIPT ENGINE -->
  <script>
    // ========================================================
    // ROOT SCOPE ESSENTIAL HELPERS & PSEUDO-RANDOM GENERATOR
    // ========================================================
    function getActivePageLines(rawLines) {
      if (!rawLines || !Array.isArray(rawLines)) return [];
      if (rawLines.length > 0 && typeof rawLines[0] === 'object' && rawLines[0].y !== undefined) {
        return rawLines.map(l => l.y);
      }
      return rawLines;
    }

    function getCharAdvanceWidth(ch, fontSize) {
      if (!ch) return 0;
      const code = ch.charCodeAt(0);
      if (code < 128) {
        if ('ilI.,:;!\'|'.indexOf(ch) !== -1) return fontSize * 0.32;
        if ('mwMW'.indexOf(ch) !== -1) return fontSize * 0.78;
        if (ch === ' ') return fontSize * 0.38;
        return fontSize * 0.52;
      }
      if ('，。、；：！？）》」』”’'.indexOf(ch) !== -1) {
        return fontSize * 0.65;
      }
      return fontSize * 1.04;
    }

    function mulberry32(a) {
      return function() {
        var t = a += 0x6D2B79F5;
        t = Math.imul(t ^ t >>> 15, t | 1);
        t ^= t + Math.imul(t ^ t >>> 7, t | 61);
        return ((t ^ t >>> 14) >>> 0) / 4294967296;
      };
    }

    // ========================================================
    // NOTEBOOK LINE CURVATURE & CONTOUR BENDING ENGINE
    // (Bends text with the real notebook page contour)
    // ========================================================
    function getNotebookLineContour(baseY, x, leftM, rightM, isSpread, isRightSubpage, templateKey) {
      const span = Math.max(1, rightM - leftM);
      const t = Math.max(0, Math.min(1, (x - leftM) / span));

      if (isSpread) {
        if (isRightSubpage) {
          // Right page: starts lower near center spine (x=565), curves upward to outer margin (x=950)
          const dy = -8.0 * Math.pow(Math.max(0, 1.0 - t), 1.5) + (t - 0.5) * 2.0;
          const slope = 0.035 * Math.pow(Math.max(0, 1.0 - t), 0.5) + 0.005;
          return { y: baseY + dy, angle: slope };
        } else {
          // Left page: flat near outer edge (x=42), bows upward near center spine (x=465)
          const dy = -11.0 * Math.pow(t, 1.6);
          const slope = -0.042 * Math.pow(t, 0.6);
          return { y: baseY + dy, angle: slope };
        }
      } else {
        // Single pages: slight natural slant
        if (templateKey && templateKey.indexOf('hongha_1') !== -1) {
          const dy = -3.0 * t;
          return { y: baseY + dy, angle: -0.005 };
        }
        if (templateKey && templateKey.indexOf('thanhnam') !== -1) {
          const dy = -2.5 * t;
          return { y: baseY + dy, angle: -0.004 };
        }
        return { y: baseY, angle: 0 };
      }
    }

    // ========================================================
    // CALIBRATED NOTEBOOK TEMPLATES CONFIGURATION
    // (Strict safety margins to ensure text never overflows outside paper/spine)
    // ========================================================
    const TN_SPREAD_L = [70, 88, 107, 126, 145, 165, 184, 203, 223, 243, 264, 284, 305, 325, 346, 367, 388, 409, 431, 452, 474, 496, 518, 540, 563, 585, 608, 630, 653, 676, 699];
    const TN_SPREAD_R = [66, 84, 103, 121, 140, 159, 178, 197, 217, 237, 256, 276, 297, 317, 337, 358, 378, 400, 420, 442, 463, 485, 507, 528, 550, 572, 595, 617, 639, 662, 685, 708];

    const HH_SPREAD_L = [72, 93, 113, 135, 156, 178, 200, 222, 245, 268, 291, 314, 337, 361, 384, 408, 433, 457, 482, 508, 533, 559, 585, 611, 638, 664, 690];
    const HH_SPREAD_R = [58, 79, 99, 120, 142, 163, 186, 208, 231, 254, 277, 301, 324, 348, 371, 395, 419, 443, 468, 493, 519, 544, 570, 595, 621, 646, 672, 697];

    const HH_SINGLE_1 = [48, 79, 106, 134, 162, 190, 219, 249, 279, 309, 340, 371, 402, 433, 465, 496, 528, 560, 592, 625, 658, 692, 726, 760, 794, 828, 862, 896, 930, 964];
    const HH_SINGLE_2 = [69, 96, 124, 152, 180, 209, 238, 267, 297, 327, 357, 388, 419, 450, 482, 513, 545, 577, 610, 643, 677, 712, 746, 781, 816, 851, 886, 920, 955];
    const TN_SINGLE_1 = [61, 85, 110, 135, 160, 186, 213, 239, 266, 294, 322, 350, 378, 406, 435, 463, 491, 520, 548, 577, 607, 637, 667, 698, 729, 759, 790, 821, 851, 882, 912, 943];

    const TEMPLATES_CONFIG = {
      // 9 Double Spreads
      'notebook_thanhnam_spread.jpg': {
        name: 'Trang Đôi Thành Nam',
        desc: 'Kẻ ngang tiêu chuẩn học sinh',
        isSpread: true,
        leftPage: { leftMargin: 42, rightMargin: 465, lines: TN_SPREAD_L },
        rightPage: { leftMargin: 565, rightMargin: 950, lines: TN_SPREAD_R }
      },
      'notebook_thanhnam_spread_clean.jpg': {
        name: 'Trang Đôi Thành Nam (Trắng)',
        desc: 'Nền giấy trắng sáng rõ nét',
        isSpread: true,
        leftPage: { leftMargin: 42, rightMargin: 465, lines: TN_SPREAD_L },
        rightPage: { leftMargin: 565, rightMargin: 950, lines: TN_SPREAD_R }
      },
      'notebook_thanhnam_spread_warm.jpg': {
        name: 'Trang Đôi Thành Nam (Ấm)',
        desc: 'Giấy ngà bảo vệ mắt Vintage',
        isSpread: true,
        leftPage: { leftMargin: 42, rightMargin: 465, lines: TN_SPREAD_L },
        rightPage: { leftMargin: 565, rightMargin: 950, lines: TN_SPREAD_R }
      },
      'notebook_hongha_spread.jpg': {
        name: 'Trang Đôi Hồng Hà',
        desc: 'Hồng Hà kẻ ngang truyền thống',
        isSpread: true,
        leftPage: { leftMargin: 46, rightMargin: 465, lines: HH_SPREAD_L },
        rightPage: { leftMargin: 555, rightMargin: 950, lines: HH_SPREAD_R }
      },
      'notebook_hongha_spread_soft.jpg': {
        name: 'Trang Đôi Hồng Hà (Dịu)',
        desc: 'Tone màu êm ái chống lóa',
        isSpread: true,
        leftPage: { leftMargin: 46, rightMargin: 465, lines: HH_SPREAD_L },
        rightPage: { leftMargin: 555, rightMargin: 950, lines: HH_SPREAD_R }
      },
      'notebook_hongha_spread_warm.jpg': {
        name: 'Trang Đôi Hồng Hà (Vàng)',
        desc: 'Giấy bãi bằng vàng học trò',
        isSpread: true,
        leftPage: { leftMargin: 46, rightMargin: 465, lines: HH_SPREAD_L },
        rightPage: { leftMargin: 555, rightMargin: 950, lines: HH_SPREAD_R }
      },
      'notebook_oli_spread.jpg': {
        name: 'Trang Đôi Ô Ly',
        desc: 'Ô ly 4 dòng luyện chữ',
        isSpread: true,
        leftPage: { leftMargin: 48, rightMargin: 465, lines: TN_SPREAD_L },
        rightPage: { leftMargin: 555, rightMargin: 950, lines: TN_SPREAD_R }
      },
      'notebook_tianzige_spread.jpg': {
        name: 'Trang Đôi Điền Tự Cách',
        desc: 'Vở ô vuông Mễ Tự luyện viết chữ Hán',
        isSpread: true,
        leftPage: { leftMargin: 48, rightMargin: 465, lines: TN_SPREAD_L },
        rightPage: { leftMargin: 555, rightMargin: 950, lines: TN_SPREAD_R }
      },
      'notebook_warm_spread.jpg': {
        name: 'Trang Đôi Campus Vintage',
        desc: 'Phong cách tối giản Muji',
        isSpread: true,
        leftPage: { leftMargin: 45, rightMargin: 465, lines: HH_SPREAD_L },
        rightPage: { leftMargin: 555, rightMargin: 950, lines: HH_SPREAD_R }
      },

      // 7 Single Pages (Safe margins preventing overflowing outside desk/paper)
      'notebook_hongha_1.jpg': {
        name: 'Trang Đơn Hồng Hà (Biểu tượng)',
        desc: 'Có đồng hồ, sách vở, bóng đèn góc trên',
        isSpread: false,
        leftMargin: 130,
        rightMargin: 695,
        lines: HH_SINGLE_1
      },
      'notebook_hongha_2.jpg': {
        name: 'Trang Đơn Hồng Hà (Thời tiết)',
        desc: 'Có biểu tượng Thứ ngày & Thời tiết',
        isSpread: false,
        leftMargin: 50,
        rightMargin: 690,
        lines: HH_SINGLE_2
      },
      'notebook_thanhnam_left.jpg': {
        name: 'Trang Đơn Thành Nam',
        desc: 'Dòng kẻ chuẩn có lề đỏ',
        isSpread: false,
        leftMargin: 95,
        rightMargin: 685,
        lines: TN_SINGLE_1
      },
      'notebook_oli.jpg': {
        name: 'Trang Đơn Ô Ly',
        desc: 'Ô ly tiểu học',
        isSpread: false,
        leftMargin: 90,
        rightMargin: 685,
        lines: TN_SINGLE_1
      },
      'notebook_tianzige.jpg': {
        name: 'Trang Đơn Điền Tự Cách',
        desc: 'Ô luyện chữ Hán chuẩn',
        isSpread: false,
        leftMargin: 90,
        rightMargin: 685,
        lines: TN_SINGLE_1
      },
      'notebook_warm.jpg': {
        name: 'Trang Đơn Campus Muji',
        desc: 'Giấy ngà đơn giản',
        isSpread: false,
        leftMargin: 90,
        rightMargin: 685,
        lines: HH_SINGLE_1
      },
      'notebook_default.jpg': {
        name: 'Trang Đơn Tiêu Chuẩn',
        desc: 'Kẻ ngang căn bản',
        isSpread: false,
        leftMargin: 90,
        rightMargin: 685,
        lines: TN_SINGLE_1
      }
    };

    // ========================================================
    // GLOBAL APPLICATION STATE
    // ========================================================
    const state = {
      notebookTemplate: 'notebook_thanhnam_spread.jpg',
      spreadWriteMode: 'both',
      text: '',
      fontSize: 20, // 20px for natural handwriting weight
      inkColor: 'gel_black',
      font: 'JasonHandwriting5', // Default: authentic "xấu tự nhiên" handwriting
      messiness: 45, // 45% natural wobble & micro-tilt
      baselineOffset: 0,
      marginOffset: 0,
      topMarginLines: 0, // Top margin shift
      bottomMarginLines: 0, // Bottom margin reserve
      skipLine: false,
      autoTypo: true,
      zoomLevel: 1.0,

      // Pagination
      currentPage: 0,
      totalPages: 1,
      allPagesLines: [],

      // Smart Diagrams & Tables Configuration
      diagram: {
        enabled: false,
        type: 'none', // 'none', 'table2', 'table3', 'mindmap', 'process', 'callout', 'sketch'
        page: 0,
        spreadSide: 'right',
        startLine: 2,
        lineSpan: 9,

        // Table 2-col
        t2Col1: '生詞 (Từ mới)',
        t2Col2: '釋義與例句 (Giải nghĩa)',
        t2Rows: '落英繽紛 | 形容落花繁多，飄零紛飛。\n豁然開朗 | 眼前頓時間開朗明亮，喻領悟。\n怡然自樂 | 喜樂自得、悠閒自在的樣子。\n阡陌交通 | 田間小路交錯相通。',

        // Table 3-col
        t3Col1: '漢字',
        t3Col2: '拼音',
        t3Col3: '釋義 & 詞性',
        t3Rows: '徘徊 | pái huái | 來回走動，猶豫不決 (動詞)\n繁華 | fán huá | 繁榮熱鬧，指市容 (形容詞)\n闌珊 | lán shān | 將盡、衰落，夜色已深 (形容詞)\n眷戀 | juàn liàn | 深切留戀與懷念 (動詞)',

        // Mindmap
        mindmapRoot: '漢語語法 (Ngữ pháp Hán ngữ)',
        mindmapBranches: '詞類: 實詞與虛詞分類\n句型: 主謂賓定狀補結構\n補語: 結果、方向、程度補語\n時態: 了、著、過標記',

        // Process flow
        processSteps: '1. 提出假設 (Đưa ra giả thuyết)\n2. 蒐集語料 (Thu thập ngữ liệu)\n3. 歸納規律 (Quy nạp quy luật)\n4. 得出結論 (Rút ra kết luận)',

        // Callout
        calloutTitle: '★ 重要筆記 (Lưu ý ôn tập)',
        calloutText: '1. 注意成語之字形與聲調變化。\n2. 書寫時保持橫平豎直，筆畫流暢。\n3. 每日複習新詞彙至少十五分鐘。',

        sketchCanvas: null
      },

      notebookImg: null,
      seed: 42
    };

    const canvas = document.getElementById('renderCanvas');
    const ctx = canvas.getContext('2d');
    const textInput = document.getElementById('textInput');

    // ========================================================
    // INITIALIZATION & FONT PRELOAD CHECK
    // ========================================================
    window.addEventListener('DOMContentLoaded', () => {
      // Register Service Worker for PWA
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js').catch(err => console.log('SW failed', err));
      }

      renderTemplateGallery('all');

      // Populate initial values
      document.getElementById('t2Rows').value = state.diagram.t2Rows;
      document.getElementById('t3Rows').value = state.diagram.t3Rows;
      document.getElementById('mindmapBranchesArea').value = state.diagram.mindmapBranches;
      document.getElementById('processStepsArea').value = state.diagram.processSteps;
      document.getElementById('calloutTextArea').value = state.diagram.calloutText;

      loadNotebookImage('assets/' + state.notebookTemplate);

      // Listen for text input
      textInput.addEventListener('input', () => {
        state.text = textInput.value;
        updateCharCount();
        paginateText();
        renderCanvas();
      });

      // Init sketchpad
      initSketchpad();

      // Wait for fonts to be loaded for pristine first-frame render
      if (document.fonts) {
        document.fonts.ready.then(() => {
          renderCanvas();
        });
      }
    });

    function loadNotebookImage(src) {
      state.notebookImg = new Image();
      state.notebookImg.src = src;
      state.notebookImg.onload = () => {
        canvas.width = state.notebookImg.width;
        canvas.height = state.notebookImg.height;
        if (!state.text) {
          loadSample('taohuayuan');
        } else {
          paginateText();
          renderCanvas();
        }
        if (window.innerWidth < 992) {
          fitCanvasToViewport();
        }
      };
    }

    // ========================================================
    // TEMPLATE GALLERY & FILTERING
    // ========================================================
    function renderTemplateGallery(filter) {
      const gallery = document.getElementById('templateGallery');
      gallery.innerHTML = '';

      Object.entries(TEMPLATES_CONFIG).forEach(([filename, cfg]) => {
        if (filter === 'spread' && !cfg.isSpread) return;
        if (filter === 'single' && cfg.isSpread) return;

        const card = document.createElement('div');
        card.className = 'template-card' + (filename === state.notebookTemplate ? ' active' : '');
        card.onclick = () => selectTemplate(filename);

        card.innerHTML = `
          <img src="assets/${filename}" class="template-preview" alt="${cfg.name}" loading="lazy">
          <div class="template-meta">
            <div class="template-title">${cfg.name}</div>
            <div class="template-sub">${cfg.isSpread ? 'Trang Đôi' : 'Trang Đơn'} • ${cfg.desc}</div>
          </div>
        `;
        gallery.appendChild(card);
      });
    }

    function filterTemplates(type) {
      ['filterTplAll', 'filterTplSpread', 'filterTplSingle'].forEach(id => {
        const b = document.getElementById(id);
        if (b) b.classList.remove('active');
      });
      if (type === 'all') document.getElementById('filterTplAll').classList.add('active');
      if (type === 'spread') document.getElementById('filterTplSpread').classList.add('active');
      if (type === 'single') document.getElementById('filterTplSingle').classList.add('active');

      renderTemplateGallery(type);
    }

    function selectTemplate(filename) {
      state.notebookTemplate = filename;
      const cfg = TEMPLATES_CONFIG[filename];

      const spreadRow = document.getElementById('spreadSideRow');
      if (spreadRow) spreadRow.style.display = cfg.isSpread ? 'flex' : 'none';

      renderTemplateGallery(document.querySelector('.tool-chip.active')?.id.replace('filterTpl', '').toLowerCase() || 'all');
      loadNotebookImage('assets/' + filename);
      showToast('Đã chọn mẫu: ' + cfg.name);
    }

    // ========================================================
    // MOBILE VIEW SWITCHING & TABS
    // ========================================================
    function switchMobileView(view) {
      const btnEdit = document.getElementById('btnSwitchEdit');
      const btnPrev = document.getElementById('btnSwitchPreview');

      if (view === 'editor') {
        document.body.classList.remove('view-preview');
        btnEdit.classList.add('active');
        btnPrev.classList.remove('active');
      } else {
        document.body.classList.add('view-preview');
        btnPrev.classList.add('active');
        btnEdit.classList.remove('active');
        setTimeout(fitCanvasToViewport, 50);
      }
    }

    function switchTab(tabId) {
      document.querySelectorAll('.nav-tab').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

      const activeBtn = Array.from(document.querySelectorAll('.nav-tab')).find(b => b.getAttribute('onclick')?.indexOf(tabId) !== -1);
      if (activeBtn) activeBtn.classList.add('active');

      const targetPanel = document.getElementById(tabId);
      if (targetPanel) targetPanel.classList.add('active');
    }

    // ========================================================
    // AI PHOTO RECOGNITION & REDRAW ENGINE
    // ========================================================
    async function handleAiPhotoUpload(file) {
      if (!file) return;
      showToast('🤖 AI đang phân tích ảnh và trích xuất cấu trúc bảng/sơ đồ...');

      try {
        const worker = await Tesseract.createWorker(['chi_tra', 'chi_sim', 'vie']);
        const ret = await worker.recognize(file);
        await worker.terminate();

        const rawText = ret.data.text.trim();
        if (!rawText) {
          showToast('Không nhận diện được chữ trong ảnh chụp');
          return;
        }

        // Parse lines into table or mindmap
        const lines = rawText.split(/\r?\n/).map(l => l.trim()).filter(l => l.length > 0);
        
        let hasMultiCols = false;
        let maxColsFound = 1;
        const parsedRows = [];

        for (let l of lines) {
          // Check for separator: tab, pipe, colon, or 2+ consecutive spaces
          const parts = l.split(/\s{2,}|\t|\||：|:/).map(p => p.trim()).filter(p => p.length > 0);
          if (parts.length >= 2) {
            hasMultiCols = true;
            maxColsFound = Math.max(maxColsFound, parts.length);
            parsedRows.push(parts);
          } else {
            parsedRows.push([l]);
          }
        }

        if (hasMultiCols && maxColsFound >= 3) {
          // Setup Table 3-col
          selectDiagramType('table3');
          const header = parsedRows[0];
          document.getElementById('t3Col1').value = header[0] || 'Cột 1';
          document.getElementById('t3Col2').value = header[1] || 'Cột 2';
          document.getElementById('t3Col3').value = header[2] || 'Cột 3';
          state.diagram.t3Col1 = header[0] || 'Cột 1';
          state.diagram.t3Col2 = header[1] || 'Cột 2';
          state.diagram.t3Col3 = header[2] || 'Cột 3';

          const rowsText = parsedRows.slice(1).map(r => r.join(' | ')).join('\n');
          document.getElementById('t3Rows').value = rowsText;
          state.diagram.t3Rows = rowsText;
          showToast('✨ AI đã nhận diện và vẽ lại Bảng 3 cột bằng chữ viết tay!');

        } else if (hasMultiCols && maxColsFound === 2) {
          // Setup Table 2-col
          selectDiagramType('table2');
          const header = parsedRows[0];
          document.getElementById('t2Col1').value = header[0] || '生詞';
          document.getElementById('t2Col2').value = header[1] || '釋義';
          state.diagram.t2Col1 = header[0] || '生詞';
          state.diagram.t2Col2 = header[1] || '釋義';

          const rowsText = parsedRows.slice(1).map(r => r.join(' | ')).join('\n');
          document.getElementById('t2Rows').value = rowsText;
          state.diagram.t2Rows = rowsText;
          showToast('✨ AI đã nhận diện và vẽ lại Bảng 2 cột bằng chữ viết tay!');

        } else {
          // Setup Mindmap
          selectDiagramType('mindmap');
          document.getElementById('mindmapRootTitle').value = lines[0] || '主題';
          state.diagram.mindmapRoot = lines[0] || '主題';

          const branches = lines.slice(1).join('\n');
          document.getElementById('mindmapBranchesArea').value = branches;
          state.diagram.mindmapBranches = branches;
          showToast('✨ AI đã nhận diện và vẽ lại Sơ đồ tư duy bằng nét bút viết tay!');
        }

        paginateText();
        renderCanvas();

      } catch (err) {
        console.error(err);
        showToast('Lỗi khi AI phân tích ảnh!');
      }
    }

    // ========================================================
    // DIAGRAM SELECTOR & LIVE EDITORS
    // ========================================================
    function selectDiagramType(type) {
      state.diagram.type = type;
      state.diagram.enabled = (type !== 'none');

      const cardMap = {
        'none': 'cardDiagNone',
        'table2': 'cardDiagTable2',
        'table3': 'cardDiagTable3',
        'mindmap': 'cardDiagMindmap',
        'process': 'cardDiagProcess',
        'callout': 'cardDiagCallout',
        'sketch': 'cardDiagSketch'
      };
      Object.values(cardMap).forEach(cid => {
        document.getElementById(cid)?.classList.remove('active');
      });
      document.getElementById(cardMap[type])?.classList.add('active');

      const subpanels = ['subpanelTable2', 'subpanelTable3', 'subpanelMindmap', 'subpanelProcess', 'subpanelCallout', 'subpanelSketch'];
      subpanels.forEach(sp => {
        const el = document.getElementById(sp);
        if (el) el.style.display = 'none';
      });

      const posBox = document.getElementById('diagPosBox');
      const badge = document.getElementById('diagramStatusBadge');

      if (type === 'none') {
        if (posBox) posBox.style.display = 'none';
        if (badge) { badge.innerText = 'Đang tắt'; badge.style.background = '#475569'; }
      } else {
        if (posBox) posBox.style.display = 'flex';
        if (badge) { badge.innerText = 'Đang bật'; badge.style.background = 'var(--accent)'; badge.style.color = '#0b0d13'; }

        const targetSub = 'subpanel' + type.charAt(0).toUpperCase() + type.slice(1);
        const subEl = document.getElementById(targetSub);
        if (subEl) subEl.style.display = 'flex';

        if (type === 'sketch') {
          setTimeout(initSketchpad, 60);
        }
      }

      paginateText();
      renderCanvas();
    }

    function updateDiagramPos() {
      const start = parseInt(document.getElementById('diagStartSlider').value);
      const span = parseInt(document.getElementById('diagSpanSlider').value);
      const side = document.getElementById('diagSpreadSide').value;
      const targetPage = parseInt(document.getElementById('diagTargetPage').value) - 1;

      state.diagram.startLine = start;
      state.diagram.lineSpan = span;
      state.diagram.spreadSide = side;
      state.diagram.page = Math.max(0, targetPage);

      document.getElementById('diagStartVal').innerText = start;
      document.getElementById('diagSpanVal').innerText = span;

      paginateText();
      renderCanvas();
    }

    function updateTable2Content() {
      state.diagram.t2Col1 = document.getElementById('t2Col1').value;
      state.diagram.t2Col2 = document.getElementById('t2Col2').value;
      state.diagram.t2Rows = document.getElementById('t2Rows').value;
      paginateText();
      renderCanvas();
    }

    function updateTable3Content() {
      state.diagram.t3Col1 = document.getElementById('t3Col1').value;
      state.diagram.t3Col2 = document.getElementById('t3Col2').value;
      state.diagram.t3Col3 = document.getElementById('t3Col3').value;
      state.diagram.t3Rows = document.getElementById('t3Rows').value;
      paginateText();
      renderCanvas();
    }

    function updateMindmapContent() {
      state.diagram.mindmapRoot = document.getElementById('mindmapRootTitle').value;
      state.diagram.mindmapBranches = document.getElementById('mindmapBranchesArea').value;
      paginateText();
      renderCanvas();
    }

    function updateProcessContent() {
      state.diagram.processSteps = document.getElementById('processStepsArea').value;
      paginateText();
      renderCanvas();
    }

    function updateCalloutContent() {
      state.diagram.calloutTitle = document.getElementById('calloutTitle').value;
      state.diagram.calloutText = document.getElementById('calloutTextArea').value;
      paginateText();
      renderCanvas();
    }

    // Touch Sketchpad
    let isDrawing = false;
    let lastX = 0, lastY = 0;
    function initSketchpad() {
      const sCanvas = document.getElementById('sketchCanvas');
      if (!sCanvas) return;
      const sCtx = sCanvas.getContext('2d');

      function startDraw(e) {
        isDrawing = true;
        const rect = sCanvas.getBoundingClientRect();
        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
        const clientY = e.touches ? e.touches[0].clientY : e.clientY;
        lastX = (clientX - rect.left) * (sCanvas.width / rect.width);
        lastY = (clientY - rect.top) * (sCanvas.height / rect.height);
      }

      function moveDraw(e) {
        if (!isDrawing) return;
        const rect = sCanvas.getBoundingClientRect();
        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
        const clientY = e.touches ? e.touches[0].clientY : e.clientY;
        const curX = (clientX - rect.left) * (sCanvas.width / rect.width);
        const curY = (clientY - rect.top) * (sCanvas.height / rect.height);

        sCtx.strokeStyle = (state.inkColor === 'blue') ? '#1e3a8a' : '#111827';
        sCtx.lineWidth = 2.2;
        sCtx.lineCap = 'round';
        sCtx.lineJoin = 'round';

        sCtx.beginPath();
        sCtx.moveTo(lastX, lastY);
        sCtx.lineTo(curX, curY);
        sCtx.stroke();

        lastX = curX;
        lastY = curY;
        e.preventDefault();
      }

      function endDraw() {
        if (isDrawing) {
          isDrawing = false;
          state.diagram.sketchCanvas = sCanvas;
          paginateText();
          renderCanvas();
        }
      }

      sCanvas.onmousedown = startDraw;
      sCanvas.onmousemove = moveDraw;
      window.onmouseup = endDraw;

      sCanvas.ontouchstart = startDraw;
      sCanvas.ontouchmove = moveDraw;
      window.ontouchend = endDraw;
    }

    function clearSketch() {
      const sCanvas = document.getElementById('sketchCanvas');
      if (sCanvas) {
        sCanvas.getContext('2d').clearRect(0, 0, sCanvas.width, sCanvas.height);
        state.diagram.sketchCanvas = null;
        paginateText();
        renderCanvas();
      }
    }

    // ========================================================
    // TEXT PAGINATION WITH TOP/BOTTOM MARGINS & ZERO OVERLAP
    // ========================================================
    function paginateText() {
      const cfg = TEMPLATES_CONFIG[state.notebookTemplate] || TEMPLATES_CONFIG['notebook_thanhnam_spread.jpg'];
      const isSpread = !!cfg.isSpread;

      const leftOff = state.marginOffset || 0;
      const rightOff = state.marginOffset || 0;

      let maxW_Left, maxW_Right, linesLeft, linesRight;
      if (isSpread) {
        const effLeft_L = cfg.leftPage.leftMargin + leftOff;
        const effRight_L = cfg.leftPage.rightMargin + rightOff;
        maxW_Left = Math.max(80, (effRight_L - effLeft_L) - 22);
        linesLeft = getActivePageLines(cfg.leftPage.lines).length;

        const effLeft_R = cfg.rightPage.leftMargin + leftOff;
        const effRight_R = cfg.rightPage.rightMargin + rightOff;
        maxW_Right = Math.max(80, (effRight_R - effLeft_R) - 22);
        linesRight = getActivePageLines(cfg.rightPage.lines).length;
      } else {
        const effLeft = (cfg.leftMargin || 90) + leftOff;
        const effRight = (cfg.rightMargin || 685) + rightOff;
        maxW_Left = maxW_Right = Math.max(80, (effRight - effLeft) - 24);
        linesLeft = linesRight = getActivePageLines(cfg.lines).length;
      }

      const punctuationNoStart = new Set('，。、；：！？）》」』”’');
      const rawText = state.text || '';
      const paragraphs = rawText.split(/\r?\n/);

      const parsedLines = [];
      let charCounterGlobal = 0;

      for (let p of paragraphs) {
        const clean = p.trim();
        if (!clean) {
          parsedLines.push({ isStart: true, chars: [] });
          continue;
        }

        const tokens = [];
        let inStrike = false;

        for (let i = 0; i < clean.length; i++) {
          if (clean[i] === '~' && clean[i+1] === '~') {
            inStrike = !inStrike;
            i++;
            continue;
          }
          const rawChar = clean[i];
          const PUNC_MAP = { ',': '，', '.': '。', ':': '：', ';': '；', '!': '！', '?': '？', '(': '（', ')': '）', '[': '【', ']': '】' };
          const ch = PUNC_MAP[rawChar] || rawChar;
          charCounterGlobal++;

          if (state.autoTypo && !inStrike && charCounterGlobal % 58 === 0 && '，。、；：'.indexOf(ch) === -1) {
            const wrongChars = '了的地是不人在有這我箇';
            const wrongCh = wrongChars[charCounterGlobal % wrongChars.length];
            tokens.push({ char: wrongCh, isCrossedOut: true });
          }

          tokens.push({ char: ch, isCrossedOut: inStrike });
        }

        let currentChars = [];
        let curW = isSpread ? 20 : 30;
        let isStart = true;
        const activeMaxW = maxW_Left;

        for (let tok of tokens) {
          const ch = tok.char;
          const charW = getCharAdvanceWidth(ch, state.fontSize);

          if (curW + charW > activeMaxW) {
            if (punctuationNoStart.has(ch) && currentChars.length > 0 && (curW + charW <= activeMaxW + 8)) {
              currentChars.push(tok);
              parsedLines.push({ isStart: isStart, chars: currentChars });
              currentChars = [];
              curW = 0;
              isStart = false;
              continue;
            }
            parsedLines.push({ isStart: isStart, chars: currentChars });
            currentChars = [];
            curW = 0;
            isStart = false;
          }

          currentChars.push(tok);
          curW += charW;
        }

        if (currentChars.length > 0) {
          parsedLines.push({ isStart: isStart, chars: currentChars });
        }
      }

      // Chunk lines into subpages with top/bottom margin shifts & zero-overlap diagram avoidance
      state.allPagesLines = [];
      const unplaced = [...parsedLines];
      let subpageIdx = 0;

      while (unplaced.length > 0 || (state.diagram.enabled && subpageIdx === 0 && state.allPagesLines.length === 0)) {
        const isRightSubpage = isSpread && (subpageIdx % 2 === 1);
        const subpageCapacity = isRightSubpage ? linesRight : linesLeft;
        const slots = new Array(subpageCapacity).fill(null);

        // Apply Top Margin lines (Skip lines at top)
        const topSkip = Math.min(subpageCapacity - 2, Math.max(0, state.topMarginLines));
        for (let t = 0; t < topSkip; t++) {
          slots[t] = { isMarginPlaceholder: true, chars: [] };
        }

        // Apply Bottom Margin lines (Reserve lines at bottom)
        const botSkip = Math.min(subpageCapacity - topSkip - 1, Math.max(0, state.bottomMarginLines));
        for (let b = subpageCapacity - botSkip; b < subpageCapacity; b++) {
          slots[b] = { isMarginPlaceholder: true, chars: [] };
        }

        // Check if diagram is targeted on this exact subpage
        let hasDiagramOnThisSubpage = false;
        if (state.diagram.enabled) {
          if (isSpread) {
            const targetSub = (state.diagram.page * 2) + (state.diagram.spreadSide === 'right' ? 1 : 0);
            hasDiagramOnThisSubpage = (subpageIdx === targetSub);
          } else {
            hasDiagramOnThisSubpage = (subpageIdx === state.diagram.page);
          }
        }

        if (hasDiagramOnThisSubpage) {
          const dStart = Math.max(topSkip, Math.min(subpageCapacity - botSkip - 2, state.diagram.startLine));
          const dSpan = Math.max(2, Math.min(subpageCapacity - botSkip - dStart, state.diagram.lineSpan));
          for (let s = dStart; s < dStart + dSpan; s++) {
            slots[s] = { isDiagramPlaceholder: true, chars: [] };
          }
        }

        let sIdx = 0;
        while (sIdx < subpageCapacity) {
          if (slots[sIdx] !== null) {
            sIdx++;
            continue;
          }
          if (unplaced.length > 0) {
            slots[sIdx] = unplaced.shift();
            if (state.skipLine) {
              let nextSlot = sIdx + 1;
              while (nextSlot < subpageCapacity && slots[nextSlot] !== null) {
                nextSlot++;
              }
              if (nextSlot < subpageCapacity) {
                slots[nextSlot] = { isSkipLine: true, chars: [] };
                sIdx = nextSlot;
              }
            }
          } else {
            break;
          }
          sIdx++;
        }

        while (slots.length > 0 && slots[slots.length - 1] === null) {
          slots.pop();
        }

        state.allPagesLines.push(slots);
        subpageIdx++;
        if (subpageIdx > 60) break;
      }

      if (state.allPagesLines.length === 0) {
        state.allPagesLines.push([]);
      }

      if (isSpread && state.spreadWriteMode === 'both') {
        state.totalPages = Math.max(1, Math.ceil(state.allPagesLines.length / 2));
      } else {
        state.totalPages = state.allPagesLines.length;
      }

      if (state.currentPage >= state.totalPages) {
        state.currentPage = state.totalPages - 1;
      }

      updatePaginationUI();
    }

    function updatePaginationUI() {
      const ind = document.getElementById('pageIndicator');
      if (!ind) return;
      const cfg = TEMPLATES_CONFIG[state.notebookTemplate] || TEMPLATES_CONFIG['notebook_thanhnam_spread.jpg'];
      if (cfg.isSpread && state.spreadWriteMode === 'both') {
        const p1 = state.currentPage * 2 + 1;
        const p2 = state.currentPage * 2 + 2;
        const totalSubpages = Math.max(2, state.totalPages * 2);
        ind.innerText = `Trang ${p1}-${p2} / ${totalSubpages}`;
      } else {
        ind.innerText = `Trang ${state.currentPage + 1} / ${state.totalPages}`;
      }
    }

    function prevPage() {
      if (state.currentPage > 0) {
        state.currentPage--;
        updatePaginationUI();
        renderCanvas();
      }
    }

    function nextPage() {
      if (state.currentPage < state.totalPages - 1) {
        state.currentPage++;
        updatePaginationUI();
        renderCanvas();
      }
    }

    // ========================================================
    // CANVAS RENDERING ENGINE (ORGANIC LINE FOLLOWING & HANDWRITING)
    // ========================================================
    function renderCanvas() {
      if (!state.notebookImg || !state.notebookImg.complete) return;

      const w = canvas.width;
      const h = canvas.height;

      // 1. Draw notebook background
      ctx.globalCompositeOperation = 'source-over';
      ctx.clearRect(0, 0, w, h);
      ctx.drawImage(state.notebookImg, 0, 0, w, h);

      // 2. Set ink blend mode to Multiply
      ctx.globalCompositeOperation = 'multiply';

      const cfg = TEMPLATES_CONFIG[state.notebookTemplate] || TEMPLATES_CONFIG['notebook_thanhnam_spread.jpg'];
      const isSpread = !!cfg.isSpread;
      const leftOff = state.marginOffset || 0;
      const rightOff = state.marginOffset || 0;
      const blOffset = state.baselineOffset || 0;

      const mFactor = state.messiness / 100.0;
      const prng = mulberry32(state.seed + state.currentPage * 7919);

      let baseR = 24, baseG = 28, baseB = 36;
      if (state.inkColor === 'blue') { baseR = 24; baseG = 56; baseB = 125; }
      else if (state.inkColor === 'deep_black') { baseR = 8; baseG = 8; baseB = 12; }

      if (isSpread) {
        const leftM_L = cfg.leftPage.leftMargin + leftOff;
        const rightM_L = cfg.leftPage.rightMargin + rightOff;
        const leftM_R = cfg.rightPage.leftMargin + leftOff;
        const rightM_R = cfg.rightPage.rightMargin + rightOff;

        const leftSubpage = state.allPagesLines[state.currentPage * 2] || [];
        const rightSubpage = state.allPagesLines[state.currentPage * 2 + 1] || [];

        // Draw diagram on designated spread side
        if (state.diagram.enabled && state.currentPage === state.diagram.page) {
          const isRight = (state.diagram.spreadSide === 'right');
          const sideCfg = isRight ? 
            { lines: cfg.rightPage.lines, leftMargin: leftM_R, rightMargin: rightM_R } : 
            { lines: cfg.leftPage.lines, leftMargin: leftM_L, rightMargin: rightM_L };
          drawDiagramOnCanvas(ctx, prng, `rgb(${baseR}, ${baseG}, ${baseB})`, sideCfg);
        }

        renderLineSet(ctx, leftSubpage, cfg.leftPage.lines, leftM_L, rightM_L, blOffset, prng, baseR, baseG, baseB, mFactor, state.fontSize, state.font, true, false);
        renderLineSet(ctx, rightSubpage, cfg.rightPage.lines, leftM_R, rightM_R, blOffset, prng, baseR, baseG, baseB, mFactor, state.fontSize, state.font, true, true);

      } else {
        const leftM = (cfg.leftMargin || 90) + leftOff;
        const rightM = (cfg.rightMargin || 685) + rightOff;
        const pageLines = state.allPagesLines[state.currentPage] || [];

        if (state.diagram.enabled && state.currentPage === state.diagram.page) {
          drawDiagramOnCanvas(ctx, prng, `rgb(${baseR}, ${baseG}, ${baseB})`, { lines: cfg.lines, leftMargin: leftM, rightMargin: rightM });
        }

        renderLineSet(ctx, pageLines, cfg.lines, leftM, rightM, blOffset, prng, baseR, baseG, baseB, mFactor, state.fontSize, state.font, false, false);
      }
    }

    function renderLineSet(ctx, lineTokensList, linesConfig, leftM, rightM, blOffset, prng, baseR, baseG, baseB, mFactor, fontSize, fontName, isSpread, isRightSubpage) {
      if (!lineTokensList || lineTokensList.length === 0) return;
      const baselines = getActivePageLines(linesConfig);

      for (let lIdx = 0; lIdx < lineTokensList.length; lIdx++) {
        if (lIdx >= baselines.length) break;
        const lineItem = lineTokensList[lIdx];
        if (!lineItem || lineItem.isSkipLine || lineItem.isDiagramPlaceholder || lineItem.isMarginPlaceholder) continue;

        const rawBaseY = baselines[lIdx] + blOffset;
        const lineJitterY = (prng() - 0.5) * 1.4 * mFactor;

        let curX = leftM + (lineItem.isStart ? (fontSize * 1.6) : (prng() * 4 * mFactor));

        for (let tok of lineItem.chars) {
          const ch = tok.char;
          const charAdvance = getCharAdvanceWidth(ch, fontSize);

          // STRICT SAFETY MARGIN CHECK: Never allow writing past right margin or onto desk/spine!
          if (curX + charAdvance > rightM - 4) {
            break;
          }

          if (ch === ' ') {
            curX += charAdvance;
            continue;
          }

          // Exact line curvature & normal slope calculation:
          const contour = getNotebookLineContour(rawBaseY, curX, leftM, rightM, isSpread, isRightSubpage, state.notebookTemplate);
          const effectiveBaseY = contour.y + lineJitterY;

          const chJitterX = (prng() - 0.5) * 2.2 * mFactor;
          const chJitterY = (prng() - 0.5) * 2.2 * mFactor;
          const chAngle = contour.angle + (prng() - 0.5) * 0.12 * mFactor; // Follow line curve + random hand tilt
          const chScale = 1.0 + (prng() - 0.5) * 0.08 * mFactor;

          const rVar = Math.max(0, Math.min(255, baseR + Math.round((prng() - 0.5) * 14)));
          const gVar = Math.max(0, Math.min(255, baseG + Math.round((prng() - 0.5) * 14)));
          const bVar = Math.max(0, Math.min(255, baseB + Math.round((prng() - 0.5) * 14)));
          const alphaVar = 0.85 + prng() * 0.13;

          ctx.save();
          ctx.translate(curX + charAdvance / 2 + chJitterX, effectiveBaseY + chJitterY);
          ctx.rotate(chAngle);
          ctx.scale(chScale, chScale);

          ctx.font = `${fontSize}px "${fontName}", cursive`;
          ctx.fillStyle = `rgba(${rVar}, ${gVar}, ${bVar}, ${alphaVar})`;
          ctx.textBaseline = 'alphabetic';
          ctx.fillText(ch, -charAdvance / 2, 0);

          // Authentic crossed-out strikethrough effect
          if (tok.isCrossedOut) {
            ctx.strokeStyle = `rgba(${rVar}, ${gVar}, ${bVar}, 0.88)`;
            ctx.lineWidth = 1.8;
            ctx.lineCap = 'round';
            ctx.beginPath();
            const strikeY = -fontSize * 0.42 + (prng() - 0.5) * 2.5;
            ctx.moveTo(-charAdvance * 0.6, strikeY);
            ctx.lineTo(charAdvance * 0.6, strikeY + (prng() - 0.5) * 3);
            ctx.stroke();

            // Double scratch for realism
            ctx.beginPath();
            ctx.moveTo(-charAdvance * 0.55, strikeY + 2);
            ctx.lineTo(charAdvance * 0.55, strikeY - 1);
            ctx.stroke();
          }

          ctx.restore();
          curX += charAdvance + (prng() - 0.5) * 1.5 * mFactor;
        }
      }
    }

    // ========================================================
    // ORGANIC HANDWRITTEN DIAGRAM & TABLE DRAWING HELPERS
    // (Full vector redrawing matching active handwriting font)
    // ========================================================
    function drawOrganicLine(ctx, x1, y1, x2, y2, prng, segments = 6, amp = 1.4) {
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      const dx = (x2 - x1) / segments;
      const dy = (y2 - y1) / segments;
      for (let i = 1; i <= segments; i++) {
        const curX = x1 + dx * i;
        const curY = y1 + dy * i;
        const jX = (i === segments) ? 0 : (prng() - 0.5) * amp;
        const jY = (i === segments) ? 0 : (prng() - 0.5) * amp;
        ctx.lineTo(curX + jX, curY + jY);
      }
      ctx.stroke();
    }

    function drawOrganicRect(ctx, x, y, w, h, prng) {
      const o = 2.0; // overshoot
      drawOrganicLine(ctx, x - o, y, x + w + o, y, prng, 8);
      drawOrganicLine(ctx, x + w, y - o, x + w, y + h + o, prng, 6);
      drawOrganicLine(ctx, x + w + o, y + h, x - o, y + h, prng, 8);
      drawOrganicLine(ctx, x, y + h + o, x, y - o, prng, 6);
    }

    function drawDiagramOnCanvas(ctx, prng, inkColor, activePageCfg) {
      const d = state.diagram;
      const allLines = activePageCfg ? activePageCfg.lines : BASELINES;
      const baselines = getActivePageLines(allLines);

      const leftM = activePageCfg ? activePageCfg.leftMargin : 90;
      const rightM = activePageCfg ? activePageCfg.rightMargin : 685;

      const dStart = Math.max(0, Math.min(baselines.length - 2, d.startLine));
      const dSpan = Math.max(2, Math.min(baselines.length - dStart, d.lineSpan));
      const lastLineIdx = dStart + dSpan - 1;

      // Mathematical zero-overlap bounds
      const startY = baselines[dStart] - 16;
      const endY = baselines[lastLineIdx] - 2;
      const boxW = Math.max(60, (rightM - leftM) - 10);
      const boxX = leftM + 5;
      const boxH = Math.max(50, endY - startY);

      ctx.save();
      ctx.strokeStyle = inkColor;
      ctx.fillStyle = inkColor;
      ctx.lineWidth = 1.6;
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';

      if (d.type === 'sketch' && d.sketchCanvas) {
        const cW = d.sketchCanvas.width;
        const cH = d.sketchCanvas.height;
        const scale = Math.min(boxW / cW, boxH / cH);
        const drawW = cW * scale;
        const drawH = cH * scale;
        const offX = boxX + (boxW - drawW) / 2;
        const offY = startY + (boxH - drawH) / 2;
        ctx.drawImage(d.sketchCanvas, offX, offY, drawW, drawH);
      } else if (d.type === 'table2') {
        drawHanddrawnTable2(ctx, boxX, startY, boxW, boxH, prng, d);
      } else if (d.type === 'table3') {
        drawHanddrawnTable3(ctx, boxX, startY, boxW, boxH, prng, d);
      } else if (d.type === 'mindmap') {
        drawHanddrawnMindmap(ctx, boxX, startY, boxW, boxH, prng, d);
      } else if (d.type === 'process') {
        drawHanddrawnProcess(ctx, boxX, startY, boxW, boxH, prng, d);
      } else if (d.type === 'callout') {
        drawHanddrawnCallout(ctx, boxX, startY, boxW, boxH, prng, d);
      }

      ctx.restore();
    }

    // Hand-drawn Table (2 Columns)
    function drawHanddrawnTable2(ctx, x, y, w, h, prng, d) {
      drawOrganicRect(ctx, x, y, w, h, prng);
      const colSplit = x + w * 0.32;
      drawOrganicLine(ctx, colSplit, y, colSplit, y + h, prng, 8);

      const headerH = Math.min(32, Math.max(24, h * 0.22));
      drawOrganicLine(ctx, x, y + headerH, x + w, y + headerH, prng, 8);

      const fSize = Math.max(13, state.fontSize - 3);
      ctx.font = `bold ${fSize}px "${state.font}", cursive`;
      ctx.fillText(d.t2Col1 || '生詞', x + 10, y + headerH * 0.68);
      ctx.fillText(d.t2Col2 || '釋義', colSplit + 10, y + headerH * 0.68);

      const rows = (d.t2Rows || '').split('\n').filter(r => r.trim());
      if (rows.length > 0) {
        const rowH = (h - headerH) / rows.length;
        ctx.font = `${Math.max(12, fSize - 1)}px "${state.font}", cursive`;

        rows.forEach((r, idx) => {
          const rowY = y + headerH + rowH * (idx + 1);
          if (idx < rows.length - 1) {
            drawOrganicLine(ctx, x, rowY, x + w, rowY, prng, 8);
          }
          const parts = r.split('|').map(s => s.trim());
          ctx.fillText(parts[0] || '', x + 8, rowY - rowH * 0.32);
          ctx.fillText(parts[1] || '', colSplit + 8, rowY - rowH * 0.32);
        });
      }
    }

    // Hand-drawn Table (3 Columns)
    function drawHanddrawnTable3(ctx, x, y, w, h, prng, d) {
      drawOrganicRect(ctx, x, y, w, h, prng);
      const c1Split = x + w * 0.28;
      const c2Split = x + w * 0.58;
      drawOrganicLine(ctx, c1Split, y, c1Split, y + h, prng, 8);
      drawOrganicLine(ctx, c2Split, y, c2Split, y + h, prng, 8);

      const headerH = Math.min(32, Math.max(24, h * 0.22));
      drawOrganicLine(ctx, x, y + headerH, x + w, y + headerH, prng, 8);

      const fSize = Math.max(13, state.fontSize - 3);
      ctx.font = `bold ${fSize}px "${state.font}", cursive`;
      ctx.fillText(d.t3Col1 || '漢字', x + 8, y + headerH * 0.68);
      ctx.fillText(d.t3Col2 || '拼音', c1Split + 8, y + headerH * 0.68);
      ctx.fillText(d.t3Col3 || '釋義', c2Split + 8, y + headerH * 0.68);

      const rows = (d.t3Rows || '').split('\n').filter(r => r.trim());
      if (rows.length > 0) {
        const rowH = (h - headerH) / rows.length;
        ctx.font = `${Math.max(12, fSize - 1)}px "${state.font}", cursive`;

        rows.forEach((r, idx) => {
          const rowY = y + headerH + rowH * (idx + 1);
          if (idx < rows.length - 1) {
            drawOrganicLine(ctx, x, rowY, x + w, rowY, prng, 8);
          }
          const parts = r.split('|').map(s => s.trim());
          ctx.fillText(parts[0] || '', x + 8, rowY - rowH * 0.32);
          ctx.fillText(parts[1] || '', c1Split + 8, rowY - rowH * 0.32);
          ctx.fillText(parts[2] || '', c2Split + 8, rowY - rowH * 0.32);
        });
      }
    }

    // Hand-drawn Mindmap
    function drawHanddrawnMindmap(ctx, x, y, w, h, prng, d) {
      const cx = x + w * 0.30;
      const cy = y + h * 0.5;

      const rootW = Math.min(145, w * 0.32);
      const rootH = Math.min(36, h * 0.30);
      drawOrganicRect(ctx, cx - rootW / 2, cy - rootH / 2, rootW, rootH, prng);

      ctx.font = `bold 13.5px "${state.font}", cursive`;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(d.mindmapRoot || '主題', cx, cy);

      const branches = (d.mindmapBranches || '').split('\n').filter(b => b.trim());
      if (branches.length > 0) {
        const branchGap = h / (branches.length + 1);
        ctx.font = `12px "${state.font}", cursive`;
        ctx.textAlign = 'left';

        branches.forEach((bText, idx) => {
          const bY = y + branchGap * (idx + 1);
          const bX = x + w * 0.54;

          ctx.beginPath();
          ctx.moveTo(cx + rootW / 2, cy);
          const cpX = (cx + rootW / 2 + bX) / 2 + (prng() - 0.5) * 8;
          ctx.quadraticCurveTo(cpX, bY, bX, bY);
          ctx.stroke();

          drawOrganicLine(ctx, bX, bY, x + w - 8, bY, prng, 6);
          ctx.fillText(bText, bX + 6, bY - 4);
        });
      }
      ctx.textAlign = 'start';
    }

    // Hand-drawn Process Flow
    function drawHanddrawnProcess(ctx, x, y, w, h, prng, d) {
      const steps = (d.processSteps || '').split('\n').filter(s => s.trim());
      if (steps.length === 0) return;

      const stepW = (w - 20) / steps.length;
      const boxH = Math.min(48, h * 0.55);
      const boxY = y + (h - boxH) / 2;

      ctx.font = `12.5px "${state.font}", cursive`;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';

      steps.forEach((st, idx) => {
        const bX = x + idx * stepW + 6;
        const curW = stepW - 22;
        drawOrganicRect(ctx, bX, boxY, curW, boxH, prng);
        ctx.fillText(st, bX + curW / 2, boxY + boxH / 2);

        // Arrow to next step
        if (idx < steps.length - 1) {
          const arrowX1 = bX + curW + 2;
          const arrowX2 = arrowX1 + 14;
          const arrowY = boxY + boxH / 2;
          drawOrganicLine(ctx, arrowX1, arrowY, arrowX2, arrowY, prng, 3);
          drawOrganicLine(ctx, arrowX2 - 4, arrowY - 4, arrowX2, arrowY, prng, 2);
          drawOrganicLine(ctx, arrowX2 - 4, arrowY + 4, arrowX2, arrowY, prng, 2);
        }
      });
      ctx.textAlign = 'start';
    }

    // Hand-drawn Callout
    function drawHanddrawnCallout(ctx, x, y, w, h, prng, d) {
      drawOrganicRect(ctx, x, y, w, h, prng);
      drawOrganicLine(ctx, x + 4, y + 4, x + 4, y + h - 4, prng, 6);

      ctx.font = `bold 14px "${state.font}", cursive`;
      ctx.fillText(d.calloutTitle || '★ Lưu ý', x + 14, y + 22);

      const lines = (d.calloutText || '').split('\n');
      ctx.font = `12.5px "${state.font}", cursive`;
      lines.forEach((l, idx) => {
        ctx.fillText(l, x + 14, y + 44 + idx * 20);
      });
    }

    // ========================================================
    // STYLE CONTROLS & EVENT HANDLERS
    // ========================================================
    function setInkColor(color) {
      state.inkColor = color;
      ['btnInkGel', 'btnInkBlue', 'btnInkDeep'].forEach(id => document.getElementById(id)?.classList.remove('active'));
      if (color === 'gel_black') document.getElementById('btnInkGel')?.classList.add('active');
      if (color === 'blue') document.getElementById('btnInkBlue')?.classList.add('active');
      if (color === 'deep_black') document.getElementById('btnInkDeep')?.classList.add('active');

      renderCanvas();
    }

    function setFont(fontName) {
      state.font = fontName;
      paginateText();
      renderCanvas();
      showToast('Đã đổi font: ' + fontName);
    }

    function updateFontSize(val) {
      state.fontSize = parseInt(val);
      document.getElementById('fontSizeVal').innerText = val + 'px';
      paginateText();
      renderCanvas();
    }

    function updateMessiness(val) {
      state.messiness = parseInt(val);
      document.getElementById('messinessVal').innerText = val + '%';
      renderCanvas();
    }

    function updateBaselineOffset(val) {
      state.baselineOffset = parseInt(val);
      document.getElementById('baselineVal').innerText = val + 'px';
      renderCanvas();
    }

    function updateMarginOffset(val) {
      state.marginOffset = parseInt(val);
      document.getElementById('marginVal').innerText = val + 'px';
      paginateText();
      renderCanvas();
    }

    function updateTopMargin(val) {
      state.topMarginLines = parseInt(val);
      document.getElementById('topMarginVal').innerText = val + ' dòng';
      paginateText();
      renderCanvas();
    }

    function updateBottomMargin(val) {
      state.bottomMarginLines = parseInt(val);
      document.getElementById('bottomMarginVal').innerText = val + ' dòng';
      paginateText();
      renderCanvas();
    }

    function toggleSkipLine() {
      state.skipLine = !state.skipLine;
      const b = document.getElementById('btnSkipLine');
      if (b) {
        b.innerText = state.skipLine ? 'Cách dòng: Bật' : 'Cách dòng: Tắt';
        b.classList.toggle('active', state.skipLine);
      }
      paginateText();
      renderCanvas();
    }

    function toggleTradSimp() {
      showToast('Đang chuyển đổi Phồn thể / Giản thể...');
      const simp = '门见为来还进国听说话书练习时汉语言学习';
      const trad = '門見為來還進國聽說話書練習時漢語言學習';
      let val = textInput.value;
      let isSimpToTrad = false;
      for (let ch of val) {
        if (simp.indexOf(ch) !== -1) { isSimpToTrad = true; break; }
      }

      let res = '';
      for (let ch of val) {
        if (isSimpToTrad) {
          const idx = simp.indexOf(ch);
          res += (idx !== -1) ? trad[idx] : ch;
        } else {
          const idx = trad.indexOf(ch);
          res += (idx !== -1) ? simp[idx] : ch;
        }
      }
      textInput.value = res;
      state.text = res;
      updateCharCount();
      paginateText();
      renderCanvas();
      showToast(isSimpToTrad ? 'Đã chuyển sang Phồn thể' : 'Đã chuyển sang Giản thể');
    }

    function insertStrikeSnippet() {
      const start = textInput.selectionStart;
      const end = textInput.selectionEnd;
      const sel = textInput.value.substring(start, end);
      const repl = `~~${sel || 'từ sai'}~~`;
      textInput.setRangeText(repl, start, end, 'end');
      state.text = textInput.value;
      updateCharCount();
      paginateText();
      renderCanvas();
    }

    function clearText() {
      if (confirm('Bạn có chắc muốn xóa toàn bộ nội dung đã nhập?')) {
        textInput.value = '';
        state.text = '';
        updateCharCount();
        paginateText();
        renderCanvas();
      }
    }

    function updateCharCount() {
      const len = (state.text || '').replace(/\s+/g, '').length;
      const lines = (state.text || '').split('\n').length;
      document.getElementById('charCountBadge').innerText = `${len} chữ • ${lines} dòng`;
    }

    function loadSample(key) {
      if (key === 'taohuayuan') {
        textInput.value = `晉太元中，武陵人捕魚為業。緣溪行，忘路之遠近。忽逢桃花林，夾岸數百步，中無雜樹，芳草鮮美，落英繽紛。漁人甚異之，復前行，欲窮其林。\n林盡水源，便得一山，山有小口，彷彿若有光。便捨船，從口入。初極狹，才通人。復行數十步，豁然開朗。土地平曠，屋舍儼然，有良田美池桑竹之屬。阡陌交通，雞犬相聞。其中往來種作，男女衣著，悉如外人。黃髮垂髫，並怡然自樂。\n見漁人，乃大驚，問所從來。具答之。便要還家，設酒殺雞作食。村中聞有此人，咸來問訊。自云先世避秦時亂，率妻子邑人來此絕境，不復出焉，遂與外人間隔。問今是何世，乃不知有漢，無論魏晉。此人一一為具言所聞，皆嘆惋。餘人各復延至其家，皆出酒食。停數日，辭去。此中人語云：「不足為外人道也。」`;
      } else if (key === 'vocab') {
        textInput.value = `生詞筆記表（HSK 5 語彙整理）：\n1. 繽紛 (bīnfēn) : 多種顏色錯雜繁複的樣子。\n2. 豁然開朗 (huòrán kāilǎng) : 比喻突然領悟。\n3. 怡然自樂 (yírán zìlè) : 喜悅自得、悠然自樂。`;
      }
      state.text = textInput.value;
      updateCharCount();
      paginateText();
      renderCanvas();
      showToast('Đã nạp bài tập mẫu!');
    }

    // OCR via Tesseract.js
    async function handleOcrUpload(file) {
      if (!file) return;
      showToast('Đang nhận diện chữ Hán từ ảnh...');
      try {
        const worker = await Tesseract.createWorker(['chi_tra', 'chi_sim']);
        const ret = await worker.recognize(file);
        await worker.terminate();

        const cleaned = ret.data.text.trim();
        if (cleaned) {
          textInput.value = cleaned;
          state.text = cleaned;
          updateCharCount();
          paginateText();
          renderCanvas();
          showToast('Quét chữ hoàn tất!');
        } else {
          showToast('Không tìm thấy chữ Hán trong ảnh');
        }
      } catch (err) {
        console.error(err);
        showToast('Lỗi nhận diện ảnh!');
      }
    }

    // Zoom & Canvas View Controls
    function adjustZoom(delta) {
      state.zoomLevel = Math.max(0.4, Math.min(2.5, state.zoomLevel + delta));
      applyZoom();
    }
    function resetZoom() {
      state.zoomLevel = 1.0;
      applyZoom();
    }
    function fitCanvasToViewport() {
      const vp = document.getElementById('viewport');
      if (!vp) return;
      const pad = 24;
      const availW = vp.clientWidth - pad;
      const fitScale = availW / canvas.width;
      state.zoomLevel = Math.min(1.0, Math.max(0.35, fitScale));
      applyZoom();
    }
    function applyZoom() {
      const wrap = document.getElementById('canvasWrapper');
      if (wrap) {
        wrap.style.transform = `scale(${state.zoomLevel})`;
        wrap.style.transformOrigin = 'top center';
      }
      const b = document.getElementById('zoomLevelBtn');
      if (b) b.innerText = Math.round(state.zoomLevel * 100) + '%';
    }

    // Download Image
    function downloadCurrentPageImage() {
      const link = document.createElement('a');
      link.download = `chep-tay-trang-${state.currentPage + 1}.jpg`;
      link.href = canvas.toDataURL('image/jpeg', 0.95);
      link.click();
      showToast('Đã tải ảnh vở về máy thành công!');
    }

    // PWA Install prompt handling
    let deferredPrompt = null;
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      deferredPrompt = e;
      const btn = document.getElementById('btnInstallPwa');
      if (btn) btn.style.display = 'inline-flex';
    });

    function installPWA() {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.then((choiceResult) => {
          if (choiceResult.outcome === 'accepted') {
            showToast('Đang cài đặt app vào màn hình chính...');
          }
          deferredPrompt = null;
        });
      } else {
        alert('Để thêm app vào màn hình chính:\n• Trên iPhone/Safari: Bấm nút Chia sẻ (hình vuông mũi tên lên) -> Chọn "Thêm vào MH chính (Add to Home Screen)".\n• Trên Android/Chrome: Bấm menu 3 chấm góc trên -> Chọn "Cài đặt ứng dụng / Thêm vào màn hình chính".');
      }
    }

    // Toast helper
    function showToast(msg) {
      const t = document.getElementById('toast');
      const tm = document.getElementById('toastMsg');
      if (!t || !tm) return;
      tm.innerText = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2800);
    }
  </script>
</body>
</html>
'''

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html_code)

print("Successfully written v4 index.html! Bytes:", len(html_code.encode('utf-8')))
