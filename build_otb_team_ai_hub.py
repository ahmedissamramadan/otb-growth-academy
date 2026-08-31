import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from generate_master_academy import COURSES_DATA
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

# ==============================================================================
# 1. LUXURY OTB BRAND SYSTEM CSS
# ==============================================================================
master_css = """
/* ==========================================================================
   OTB TEAM AI HUB — LUXURY BRAND & ROLE EMPOWERMENT ENGINE
   Colors: Obsidian Noir (#050609), Charcoal (#0B0E16), Imperial Gold (#C5A059 / #DFBA73)
   Fonts: Felfel (Arabic Display), KOOkies (English Typography), Cinzel (Royal Serif), Readex Pro (Body)
   ========================================================================== */

@font-face {
  font-family: 'Felfel';
  src: url('assets/fonts/Felfel-Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'KOOkies';
  src: url('assets/fonts/KOOkies-Bold.otf') format('opentype');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'KOOkies';
  src: url('assets/fonts/KOOkies-ExtraBold.otf') format('opentype');
  font-weight: 800;
  font-style: normal;
  font-display: swap;
}

:root {
  --bg-app: #050609;
  --bg-sidebar: #080A0F;
  --bg-main: #0B0E16;
  --bg-card: rgba(14, 18, 28, 0.75);
  --bg-card-hover: rgba(22, 30, 48, 0.9);
  --bg-input: #040508;
  --bg-code: #030406;

  --border: rgba(255, 255, 255, 0.08);
  --border-gold: rgba(197, 160, 89, 0.3);
  --border-gold-bright: rgba(197, 160, 89, 0.7);

  --gold: #D4A853;
  --gold-metallic: #C5A059;
  --gold-light: #DFBA73;
  --gold-gradient: linear-gradient(135deg, #F3E5C8 0%, #D4A853 50%, #9E7D3B 100%);
  --gold-dim: rgba(212, 168, 83, 0.08);
  --gold-glow: 0 0 35px rgba(197, 160, 89, 0.22);

  --cyan: #38BDF8;
  --emerald: #10B981;
  --purple: #A855F7;
  --crimson: #E11D48;

  --text-pure: #FFFFFF;
  --text-main: #E2E8F0;
  --text-muted: #94A3B8;
  --text-dim: #64748B;

  --font-felfel: 'Felfel', 'Readex Pro', -apple-system, sans-serif;
  --font-kookies: 'KOOkies', 'Plus Jakarta Sans', sans-serif;
  --font-ar: 'Readex Pro', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --font-royal: 'Cinzel', serif;

  --radius-xs: 6px;
  --radius-sm: 10px;
  --radius-md: 18px;
  --radius-lg: 26px;
  --radius-full: 9999px;

  --transition-fast: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-smooth: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: var(--font-ar);
}

html, body {
  background-color: var(--bg-app);
  color: var(--text-main);
  direction: rtl;
  min-height: 100vh;
  line-height: 1.8;
  font-size: 0.95rem;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* THREE.JS CANVAS BACKGROUND */
#webglCanvas {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  opacity: 0.5;
}

/* SCROLLBAR */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg-app); }
::-webkit-scrollbar-thumb { background: rgba(197, 160, 89, 0.3); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }

/* APP HEADER */
.app-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(8, 10, 15, 0.95);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  height: 72px;
  padding: 0 1.75rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-logo-wrap {
  position: relative;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  padding: 2px;
  background: var(--gold-gradient);
  box-shadow: 0 0 20px rgba(197, 160, 89, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
}

.brand-logo-img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

.brand-info h1 {
  font-family: var(--font-felfel);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-pure);
  letter-spacing: 0.5px;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  line-height: 1.15;
}

.brand-info p {
  font-family: var(--font-kookies);
  font-size: 0.72rem;
  color: var(--gold);
  font-weight: 700;
  letter-spacing: 1px;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.search-input-wrap {
  position: relative;
  width: 280px;
}

.search-input {
  width: 100%;
  background: var(--bg-input);
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  padding: 0.5rem 1rem 0.5rem 2rem;
  color: var(--text-pure);
  font-size: 0.85rem;
  outline: none;
  transition: var(--transition-fast);
}

.search-input:focus {
  border-color: var(--gold);
  box-shadow: 0 0 0 3px rgba(197, 160, 89, 0.15);
}

.internal-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(16, 185, 129, 0.12);
  color: var(--emerald);
  border: 1px solid rgba(16, 185, 129, 0.35);
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 700;
}

/* APP SHELL */
.app-shell {
  display: flex;
  min-height: calc(100vh - 72px);
  position: relative;
  z-index: 1;
}

/* SIDEBAR */
.sidebar {
  width: 320px;
  background: var(--bg-sidebar);
  border-left: 1px solid var(--border);
  overflow-y: auto;
  height: calc(100vh - 72px);
  position: sticky;
  top: 72px;
  padding: 1.25rem 1rem;
}

.sidebar-section {
  margin-bottom: 1.5rem;
}

.sidebar-heading {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--text-dim);
  letter-spacing: 0.5px;
  text-transform: uppercase;
  padding: 0 0.5rem;
  margin-bottom: 0.5rem;
}

.nav-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.65rem 0.85rem;
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 500;
  transition: var(--transition-fast);
  cursor: pointer;
  margin-bottom: 0.25rem;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.04);
  color: var(--text-pure);
}

.nav-item.active {
  background: var(--gold-dim);
  color: var(--gold);
  border: 1px solid var(--border-gold);
  font-weight: 600;
}

.nav-item-icon {
  font-size: 1.1rem;
  margin-left: 0.6rem;
}

/* MAIN CONTENT STAGE */
.main-stage {
  flex: 1;
  background: var(--bg-main);
  padding: 2.5rem 3.5rem 6rem 3.5rem;
  overflow-y: auto;
  max-width: 1160px;
  margin: 0 auto;
}

/* PROGRESS BAR */
.progress-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.25rem 1.5rem;
  margin-bottom: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.progress-track {
  flex: 1;
  min-width: 200px;
  height: 8px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 4px;
  overflow: hidden;
  margin: 0 1rem;
}

.progress-fill {
  height: 100%;
  background: var(--gold-gradient);
  border-radius: 4px;
  width: 0%;
  transition: width 0.4s ease;
}

/* CARDS */
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  margin-bottom: 1.25rem;
  transition: var(--transition-smooth);
}

.card:hover {
  border-color: var(--border-gold);
  background: var(--bg-card-hover);
  transform: translateY(-2px);
}

.card-title {
  font-family: var(--font-felfel);
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--text-pure);
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* BUTTONS */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.65rem 1.45rem;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  transition: var(--transition-fast);
  border: none;
}

.btn-primary {
  background: var(--gold-gradient);
  color: #000;
  font-weight: 700;
}

.btn-primary:hover {
  filter: brightness(1.1);
  transform: translateY(-1px);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.04);
  color: var(--text-pure);
  border: 1px solid var(--border);
}

.btn-secondary:hover {
  border-color: var(--border-gold);
  background: var(--gold-dim);
  color: var(--gold-light);
}

/* TABS */
.tabs-row {
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid var(--border);
  padding-bottom: 0.6rem;
}

.tab-pill {
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-dim);
  padding: 0.45rem 1rem;
  border-radius: var(--radius-sm);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-fast);
}

.tab-pill:hover {
  color: var(--text-pure);
  background: rgba(255, 255, 255, 0.04);
}

.tab-pill.active {
  color: var(--gold);
  background: var(--gold-dim);
  border-color: var(--border-gold);
}

/* CODE / PROMPT BOX (Strict LTR) */
.code-box {
  background: var(--bg-code);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 1rem 1.25rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: #38BDF8;
  direction: ltr !important;
  text-align: left;
  white-space: pre-wrap;
  margin: 0.85rem 0;
  line-height: 1.6;
}

/* FOOLPROOF RTL PHONE NUMBER FORMATTING */
.phone-wrapper {
  display: inline-flex !important;
  flex-direction: row !important;
  align-items: center !important;
  direction: ltr !important;
  unicode-bidi: isolate !important;
  white-space: nowrap !important;
  font-family: var(--font-mono), sans-serif;
  font-variant-numeric: tabular-nums;
  gap: 3px;
  color: var(--gold-light);
  text-decoration: none;
}

.phone-wrapper .phone-code {
  font-weight: 700;
  color: var(--gold);
}

.phone-wrapper .phone-num {
  font-weight: 600;
  letter-spacing: 0.5px;
}

/* TOAST NOTIFICATION */
.toast {
  position: fixed;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%) translateY(100px);
  background: #050609;
  border: 1px solid var(--gold);
  color: var(--gold-light);
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 600;
  opacity: 0;
  transition: var(--transition-smooth);
  z-index: 99999;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8), var(--gold-glow);
}

.toast.show {
  transform: translateX(-50%) translateY(0);
  opacity: 1;
}

/* ROLE SELECTION GRID */
.roles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.role-card-btn {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  cursor: pointer;
  transition: var(--transition-smooth);
  text-align: right;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.role-card-btn:hover {
  border-color: var(--gold);
  background: var(--bg-card-hover);
  transform: translateY(-3px);
  box-shadow: var(--gold-glow);
}

.role-card-btn.active {
  border-color: var(--gold);
  background: var(--gold-dim);
  box-shadow: var(--gold-glow);
}

/* RESPONSIVE */
@media (max-width: 900px) {
  .app-shell { flex-direction: column; }
  .sidebar { width: 100%; height: auto; position: static; border-left: none; border-bottom: 1px solid var(--border); }
  .main-stage { padding: 1.5rem 1rem; }
  .search-input-wrap { display: none; }
}
"""

with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(master_css)

print("Generated Cleaned style.css")

# ==============================================================================
# 2. MASTER OTB TEAM AI HUB TEMPLATE (index.html)
# ==============================================================================
p_master_lms = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Team AI Hub — منصة تمكين الذكاء الاصطناعي لفريق العمل</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=JetBrains+Mono:wght@500;600;700&family=Readex+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>

  <!-- WEBGL BACKGROUND CANVAS -->
  <canvas id="webglCanvas"></canvas>

  <!-- APP HEADER -->
  <header class="app-header">
    <div class="brand-section">
      <div class="brand-logo-wrap">
        <img src="assets/images/otb_official_logo.jpg" alt="OTB Logo" class="brand-logo-img">
      </div>
      <div class="brand-info">
        <h1>OTB TEAM AI HUB <span>👑</span></h1>
        <p>WE ARE OTB, THE CITY KINGS · 5X AI PRODUCTIVITY ENGINE</p>
      </div>
    </div>

    <div class="search-input-wrap">
      <input type="text" id="globalSearch" class="search-input" placeholder="🔍 بحث في الأدوار والأوامر والمناهج..." oninput="handleGlobalSearch()">
    </div>

    <div class="header-actions">
      <span class="internal-badge">🔒 خاص بفريق عمل OTB</span>
      <a href="https://www.facebook.com/otbagency5" target="_blank" class="btn btn-secondary" style="font-size: 0.78rem; padding: 0.35rem 0.85rem;">
        🌐 فيسبوك الوكالة (+33K)
      </a>
    </div>
  </header>

  <!-- APP SHELL -->
  <div class="app-shell">
    
    <!-- LEFT SIDEBAR -->
    <aside class="sidebar">
      
      <div class="sidebar-section">
        <div class="sidebar-heading">بوابات التمكين الرئيسية</div>
        <div class="nav-item active" onclick="switchView('roles', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">🎯</span>
            <span>تمكين الذكاء الاصطناعي لكل دور</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--gold);">AI Hub</span>
        </div>
        <div class="nav-item" onclick="switchView('courses', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">📚</span>
            <span>مناهج الـ 19 تخصصاً المعتمدة</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--text-dim);">19 P.</span>
        </div>
        <div class="nav-item" onclick="switchView('sprint', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">⚡</span>
            <span>معسكر الـ 5 أيام السريع</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--text-dim);">5 Days</span>
        </div>
      </div>

      <div class="sidebar-section">
        <div class="sidebar-heading">استوديو الأوامر والإثباتات</div>
        <div class="nav-item" onclick="switchView('prompts', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">🤖</span>
            <span>استوديو أوامر الـ AI التفاعلي</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--cyan);">RCIC</span>
        </div>
        <div class="nav-item" onclick="switchView('cases', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">💼</span>
            <span>نتائج ودراسات حالة عملاء OTB</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--emerald);">ROI</span>
        </div>
        <div class="nav-item" onclick="switchView('gallery', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">🎨</span>
            <span>معرض الهوية والأعمال البصرية</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--gold);">Showcase</span>
        </div>
      </div>

      <div class="sidebar-section">
        <div class="sidebar-heading">الشهادة والموارد</div>
        <div class="nav-item" onclick="switchView('quiz', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">📝</span>
            <span>تقييم الكفاءة وإصدار الشهادة</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--gold);">Cert</span>
        </div>
        <div class="nav-item" onclick="switchView('downloads', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">📥</span>
            <span>مركز تحميل المستندات والأوامر</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--text-dim);">Files</span>
        </div>
      </div>

      <!-- SIDEBAR FOOTER CONTACT WITH FOOLPROOF LTR NUMBER -->
      <div style="border-top: 1px solid var(--border); padding-top: 1.25rem; margin-top: 2rem; font-size: 0.8rem; color: var(--text-dim);">
        <div style="margin-bottom: 0.35rem; color: var(--text-pure); font-weight: 700; font-family: var(--font-felfel);">OTB Agency — City Kings 👑</div>
        <div style="display: flex; align-items: center; gap: 0.35rem; margin-bottom: 0.25rem;">
          <span>📞 هاتف:</span>
          <a href="tel:+201008080295" class="phone-wrapper">
            <span class="phone-code">+20</span>
            <span class="phone-num">100 808 0295</span>
          </a>
        </div>
        <div>✉️ otbagency5@gmail.com</div>
      </div>
    </aside>

    <!-- CENTER MAIN STAGE -->
    <main class="main-stage">
      
      <!-- PROGRESS METER -->
      <div class="progress-card">
        <div>
          <div style="font-size: 0.8rem; color: var(--text-dim); font-weight: 600;">نسبة الإنجاز والتطبيق في الأكاديمية:</div>
          <div style="font-size: 1.15rem; font-weight: 800; color: var(--gold);" id="progressText">0% مكتمل</div>
        </div>
        <div class="progress-track">
          <div class="progress-fill" id="progressFill"></div>
        </div>
        <button class="btn btn-secondary" style="font-size: 0.78rem; padding: 0.35rem 0.85rem;" onclick="resetProgress()">إعادة ضبط</button>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 1: ROLE AI SUPERPOWER HUB (MAIN FOCUS) -->
      <!-- ========================================== -->
      <div id="view-roles" class="lms-view">
        <div style="margin-bottom: 2rem;">
          <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700; letter-spacing: 2px;">OTB INTERNAL SUPERPOWER ENGINE</span>
          <h2 style="font-family: var(--font-felfel); font-size: 2.2rem; color: var(--text-pure); margin: 0.2rem 0 0.5rem 0; font-weight: 900;">
            اختر مجالك.. واكتشف كيف يضاعف الـ AI إنتاجيتك 5x 🚀
          </h2>
          <p style="color: var(--text-muted); font-size: 0.95rem;">
            هذه المنظومة مصممة لتجيبك فورياً: ما هو دورك في OTB؟ أين يضيع وقتك؟ ما هي أدوات الذكاء الاصطناعي الخاصة بك؟ والأوامر الجاهزة لخدمة عملاء الوكالة بأعلى جودة.
          </p>
        </div>

        <!-- ROLES SELECTOR CARDS GRID -->
        <div class="roles-grid" id="rolesGrid"></div>

        <!-- SELECTED ROLE DEEP DIVE STAGE -->
        <div id="roleStage" class="card" style="border: 2px solid var(--border-gold); padding: 2rem; margin-top: 1.5rem;"></div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 2: 19 COURSES -->
      <!-- ========================================== -->
      <div id="view-courses" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">📚 مناهج الـ 19 تخصصاً المعتمدة في الوكالة</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">تفكيك شامل لـ 2,400+ صفحة إلى وحدات دراسية وتطبيقات عملية وأوامر ذكاء اصطناعي فورية.</p>
        </div>

        <div class="tabs-row">
          <button class="tab-pill active" onclick="filterCourses('all', this)">الكل (19)</button>
          <button class="tab-pill" onclick="filterCourses('strategy', this)">الاستراتيجية والهوية (4)</button>
          <button class="tab-pill" onclick="filterCourses('creative', this)">المحتوى والسيو (4)</button>
          <button class="tab-pill" onclick="filterCourses('media', this)">الميديا بايينج (5)</button>
          <button class="tab-pill" onclick="filterCourses('ai', this)">الذكاء الاصطناعي (4)</button>
          <button class="tab-pill" onclick="filterCourses('career', this)">عقود الوكالة (2)</button>
        </div>

        <div id="coursesAccordionList"></div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 3: SPRINT -->
      <!-- ========================================== -->
      <div id="view-sprint" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">⚡ معسكر الـ 5 أيام السريع (Fast-Track Sprint)</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">الكبسولة اليومية المكثفة لفريق العمل مع تكليفات وتطبيقات فورية.</p>
        </div>

        <div class="tabs-row">
          <button class="tab-pill active" onclick="loadSprintDay(1, this)">اليوم 01: STP والتموضع</button>
          <button class="tab-pill" onclick="loadSprintDay(2, this)">اليوم 02: الكرييتف وريلز</button>
          <button class="tab-pill" onclick="loadSprintDay(3, this)">اليوم 03: ميديا بايينج ROAS</button>
          <button class="tab-pill" onclick="loadSprintDay(4, this)">اليوم 04: AI وأتمتة الواتساب</button>
          <button class="tab-pill" onclick="loadSprintDay(5, this)">اليوم 05: عقود الريتينر الشهرية</button>
        </div>

        <div id="sprintLessonStage" class="card" style="padding: 1.75rem;"></div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 4: PROMPTS STUDIO -->
      <!-- ========================================== -->
      <div id="view-prompts" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">🤖 استوديو أوامر الذكاء الاصطناعي التفاعلي (RCIC Engine)</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">اختر المهمة واكتب اسم العميل، وسيقوم المحرك بتوليد أمر الذكاء الاصطناعي فورياً وجاهزاً للنسخ.</p>
        </div>

        <div class="card" style="border: 2px solid var(--border-gold); margin-bottom: 2rem;">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
            <div>
              <label style="display: block; font-size: 0.85rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 600;">التكليف المطلوب:</label>
              <select id="promptTask" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input);" onchange="updateLivePrompt()">
                <option value="copy">كتابة إعلانات تحويلية (PAS Framework)</option>
                <option value="reels">اسكريبت ريلز 15 ثانية (Viral Hook)</option>
                <option value="media">تشخيص حساب إعلاني وسكيلينج (Media Buying)</option>
                <option value="design">لقطات برودكت شوت 3D لـ Midjourney</option>
                <option value="retainer">مقترح عقد ريتينر شهري ($2,500/mo)</option>
              </select>
            </div>
            <div>
              <label style="display: block; font-size: 0.85rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 600;">اسم البراند والقطاع:</label>
              <input type="text" id="promptBrand" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input);" value="MIX Coffee (Specialty Coffee)" oninput="updateLivePrompt()">
            </div>
          </div>

          <div style="margin-bottom: 1rem;">
            <label style="display: block; font-size: 0.85rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 600;">الأمر المولد فورياً:</label>
            <div id="livePromptCode" class="code-box" style="max-height: 220px; overflow-y: auto;"></div>
          </div>

          <button class="btn btn-primary" onclick="copyText(document.getElementById('livePromptCode').innerText)">📋 نسخ الأمر المخصص للحافظة</button>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 5: CASE STUDIES -->
      <!-- ========================================== -->
      <div id="view-cases" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">💼 دراسات حالة وأرقام عملاء OTB المعتمدين</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">أرقام حقيقية واستراتيجيات موثقة لحملات عملاء الوكالة.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.25rem;">
          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Specialty Coffee</span>
              <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700;">تفاعل +180%</span>
            </div>
            <h4 class="card-title">☕ MIX Coffee</h4>
            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
              إعادة التموضع كوجهة أولى لرواد الأعمال، هوية داكنة راقية، وفيديوهات ASMR لتحضير القهوة، مما ضاعف مبيعات الفروع.
            </p>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Gourmet Burgers</span>
              <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700;">Retention 36.8%</span>
            </div>
            <h4 class="card-title">🍔 Rancho's EG</h4>
            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
              الخروج من فخ الخصومات، تموضع البرجر الملحمي، وإعلانات ريلز PAS حققت 450 ألف مشاهدة وزيادة المبيعات بنسبة 65%.
            </p>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Luxury Jewelry</span>
              <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700;">ROAS 7.5x+</span>
            </div>
            <h4 class="card-title">💍 Dr. Zaghloul Jewelry</h4>
            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
              بناء الثقة وسرد قصص التصاميم الحصرية بجودة سينمائية وهيكل حملات TOFU/MOFU/BOFU محققاً عائداً إعلانيا تجاوز 7.5x.
            </p>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Industrial & B2B</span>
              <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700;">10M ➔ 30M EGP</span>
            </div>
            <h4 class="card-title">🏭 Franks EG</h4>
            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
              القفز من المركز 25 إلى المركز الثاني في السوق، ومضاعفة المبيعات الرقمية من 10 إلى 30 مليون جنيه عبر حملات تحويلية استراتيجية.
            </p>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">E-Commerce</span>
              <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700;">CPA -32%</span>
            </div>
            <h4 class="card-title">📦 Sakr Store</h4>
            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
              إعادة هيكلة إعلانات Advantage+ وتتبع CAPI مع عروض الباقات، مما خفض تكلفة الشراء بنسبة 32% ورفع متوسط السلة بنسبة 50%.
            </p>
          </div>

          <div class="card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Clinics & Labs</span>
              <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700;">800+ Leads / mo</span>
            </div>
            <h4 class="card-title">🧪 Elag Labs</h4>
            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
              إعلانات تحويلية سريعة مع مسار واتساب مؤتمت لاستقبال وتأهيل حجوزات التحاليل والزيارات المنزلية بنجاح.
            </p>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 6: GALLERY SHOWCASE -->
      <!-- ========================================== -->
      <div id="view-gallery" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">🎨 معرض الهوية والإنتاج البصري</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">نماذج حقيقية من إبداعات مصممي وفريق وكالة OTB لبراندات النخبة.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
          <div class="card" style="padding: 0.75rem; overflow: hidden;">
            <img src="assets/images/otb_official_showcase.jpg" alt="OTB Showcase" style="width: 100%; height: 200px; object-fit: cover; border-radius: var(--radius-sm);">
            <div style="padding: 0.75rem 0.5rem 0.25rem 0.5rem;">
              <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">Brand Identity</span>
              <h4 style="font-family: var(--font-felfel); font-size: 1.1rem; color: #fff;">OTB Official 3D Masterpiece</h4>
            </div>
          </div>

          <div class="card" style="padding: 0.75rem; overflow: hidden;">
            <img src="assets/images/portfolio1.jpg" alt="MIX Coffee Portfolio" style="width: 100%; height: 200px; object-fit: cover; border-radius: var(--radius-sm);">
            <div style="padding: 0.75rem 0.5rem 0.25rem 0.5rem;">
              <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">Specialty Coffee</span>
              <h4 style="font-family: var(--font-felfel); font-size: 1.1rem; color: #fff;">MIX Coffee Visual Identity</h4>
            </div>
          </div>

          <div class="card" style="padding: 0.75rem; overflow: hidden;">
            <img src="assets/images/portfolio2.jpg" alt="Rancho's Portfolio" style="width: 100%; height: 200px; object-fit: cover; border-radius: var(--radius-sm);">
            <div style="padding: 0.75rem 0.5rem 0.25rem 0.5rem;">
              <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">Gourmet Burger</span>
              <h4 style="font-family: var(--font-felfel); font-size: 1.1rem; color: #fff;">Rancho's Epic Campaigns</h4>
            </div>
          </div>

          <div class="card" style="padding: 0.75rem; overflow: hidden;">
            <img src="assets/images/arabic_portfolio.jpg" alt="Arabic Portfolio" style="width: 100%; height: 200px; object-fit: cover; border-radius: var(--radius-sm);">
            <div style="padding: 0.75rem 0.5rem 0.25rem 0.5rem;">
              <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">Luxury Gold</span>
              <h4 style="font-family: var(--font-felfel); font-size: 1.1rem; color: #fff;">Dr. Zaghloul Luxury Campaigns</h4>
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 7: QUIZ & CERTIFICATE -->
      <!-- ========================================== -->
      <div id="view-quiz" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">📝 تقييم الكفاءة وإصدار شهادة ملوك المدينة</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">أدخل اسمك وأجب عن الأسئلة الخمسة لإصدار شهادة الاعتماد الملكية الرسمية.</p>
        </div>

        <div class="card" style="margin-bottom: 1.25rem;">
          <label style="display: block; font-size: 0.85rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 600;">الاسم الرسمي على الشهادة:</label>
          <input type="text" id="certName" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input); font-size: 1rem;" value="أحمد عصام رمضان">
        </div>

        <div class="card">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.5rem;">1. ما هو التموضع والنمط النفسي المعتمد لوكالة OTB؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.88rem;"><input type="radio" name="q0" value="0"> المنافسة على أقل سعر</label>
          <label style="display:block; font-size:0.88rem;"><input type="radio" name="q0" value="1" checked> The Ruler & The Creator (ملوك المدينة: الهيبة والجرأة والتركيز على العائد)</label>
        </div>

        <div class="card">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.5rem;">2. كيف يساعد الذكاء الاصطناعي صانع المحتوى بشكل سليم؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.88rem;"><input type="radio" name="q1" value="1" checked> كـ شريك عصف ذهني وسرعة صياغة بدقة المعطيات (Context) مع مراجعة بشرية</label>
          <label style="display:block; font-size:0.88rem;"><input type="radio" name="q1" value="0"> نسخ ولصق الردود بدون قراءة</label>
        </div>

        <div class="card">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.5rem;">3. إذا كان هامش الربح 25%، فما هو الـ Break-Even ROAS؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.88rem;"><input type="radio" name="q2" value="1" checked> 4.0x (حيث 1 / 0.25 = 4)</label>
          <label style="display:block; font-size:0.88rem;"><input type="radio" name="q2" value="0"> 1.5x</label>
        </div>

        <div class="card">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.5rem;">4. ما هي النسبة الآمنة لزيادة ميزانية الحملات الرابحة (Scaling)؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.88rem;"><input type="radio" name="q3" value="1" checked> زيادة 20% كل 48-72 ساعة لحماية استقرار الحملة</label>
          <label style="display:block; font-size:0.88rem;"><input type="radio" name="q3" value="0"> مضاعفة الميزانية 200% كل ساعة</label>
        </div>

        <div class="card">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.5rem;">5. ما هو السعر القياسي لباقة الـ Dominance Retainer لـ OTB؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.88rem;"><input type="radio" name="q4" value="1" checked> $2,500 / شهر (هوية + 24 محتوى + ميديا بايينج + أتمتة)</label>
          <label style="display:block; font-size:0.88rem;"><input type="radio" name="q4" value="0"> $300 / شهر</label>
        </div>

        <div style="text-align: center; margin: 2rem 0;">
          <button class="btn btn-primary" style="padding: 0.85rem 3rem;" onclick="generateOfficialCert()">👑 إصدار شهادة الاعتماد الملكية</button>
        </div>

        <div id="certContainer" style="display: none;"></div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 8: DOWNLOADS -->
      <!-- ========================================== -->
      <div id="view-downloads" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">📥 مركز المستندات والأوامر المباشرة</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">تحميل التقارير الاستراتيجية، وموسوعات الأوامر، وقوائم الفحص بصيغ مباشرة.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
          <div class="card">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">50+ Prompts</span>
            <h4 class="card-title" style="margin-top: 0.35rem;">📖 موسوعة الأوامر التكتيكية</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;">أوامر الذكاء الاصطناعي المعتمدة لأدوار OTB.</p>
            <a href="track_a_fast_track_sprint/cheatsheets/OTB_Prompt_Engineering_Bible.md" download class="btn btn-primary" style="width: 100%; font-size: 0.82rem; padding: 0.45rem;">📥 تحميل الموسوعة</a>
          </div>

          <div class="card">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Checklist</span>
            <h4 class="card-title" style="margin-top: 0.35rem;">✈️ فحص الميديا بايينج</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;">قائمة فحص الحملات قبل الإطلاق وقواعد السكيلينج.</p>
            <a href="track_a_fast_track_sprint/cheatsheets/OTB_Media_Buying_Checklist.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.82rem; padding: 0.45rem;">📥 تحميل الفحص</a>
          </div>

          <div class="card">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Markdown Doc</span>
            <h4 class="card-title" style="margin-top: 0.35rem;">📑 التقرير الاستراتيجي الشامل</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;">وثيقة التوجيه التنفيذي لنمو الوكالة.</p>
            <a href="track_b_4week_masterclass/studio_artifacts/OTB_Executive_Strategic_Briefing.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.82rem; padding: 0.45rem;">📥 تحميل التقرير</a>
          </div>
        </div>
      </div>

    </main>
  </div>

  <script src="shared_ui.js"></script>
  <script>
    const coursesData = {courses_json};

    // 9 CORE ROLES EMPOWERMENT MATRIX (PRO-REASONED)
    const rolesSuperpowers = [
      {{
        id: "copywriter",
        icon: "✍️",
        name: "صانع وكاتب المحتوى",
        eng: "Content Creator & Copywriter",
        challenge: "متلازمة الصفحة البيضاء (Writer's Block)، استهلاك وقت طويل في البحث، وصياغة المحتوى ليناسب منصات متعددة بنبرات وأطوال مختلفة.",
        tools: ["Claude 3.5 Sonnet (للسرد الإبداعي)", "ChatGPT Plus (للعصف الذهني)", "Notion AI (لتنظيم الخطط)"],
        impact: "تحويل فكرة واحدة إلى حملة محتوى كاملة (مقال، 5 منشورات، سكريبت ريلز) في دقائق معدودة.",
        beforeVsAfter: {{
          before: "4 ساعات لكتابة خطة محتوى أسبوعية لعميل واحد.",
          after: "45 دقيقة فقط لتوليد الأفكار، تحسين الصياغة، وضبط النبرة عبر الـ AI ثم مراجعتها بلمسة بشرية."
        }},
        prompt: "أنت خبير Copywriter في وكالة OTB. اكتب لي 3 نصوص إعلانية (Ad Copies) لمنتج [اسم المنتج] باستخدام إطار عمل PAS (Problem, Agitate, Solution). يجب أن تكون النبرة [مرحة/احترافية/جريئة]، موجهة لجمهور [وصف الجمهور]. أضف Call to Action قوي، واقترح فكرة للصورة المرفقة مع كل نص.",
        goldenRule: "لا تستخدم الذكاء الاصطناعي ككاتب بديل، بل كـ 'شريك عصف ذهني خارق'. السر دائماً يكمن في دقة السياق والمعطيات (Context) التي تغذي بها النموذج."
      }},
      {{
        id: "designer",
        icon: "🎨",
        name: "مصمم الجرافيك والهوية",
        eng: "Graphic Designer",
        challenge: "البحث المرهق عن صور Stock مناسبة، تفريغ الصور، توسيع الإطارات، والتعديلات المتكررة للمقاسات المختلفة للمنصات.",
        tools: ["Midjourney v6 (لتوليد الأصول 3D)", "Adobe Firefly (Generative Fill)", "Magnific AI (لرفع الدقة 8K)", "Canva Magic Studio"],
        impact: "إنتاج أصول مرئية حصرية ومعدلة خصيصاً للعميل دون الحاجة لجلسات تصوير واقعية مكلفة.",
        beforeVsAfter: {{
          before: "ساعات طويلة لدمج صور Freepik وضبط الإضاءة لتبدو مقبولة.",
          after: "توليد صورة فوتوغرافية دقيقة بـ Midjourney في ثوانٍ وتعديلها بـ Generative Fill في 15 دقيقة."
        }},
        prompt: "/imagine prompt: Commercial product photography of [Product Name], placed on a sleek matte noir obsidian podium, soft royal gold rim lighting, dynamic shadows, high fashion editorial style, 8k, photorealistic, vibrant colors, shot on 35mm lens --ar 4:5 --style raw --v 6.0",
        goldenRule: "إتقان هندسة الأوامر (Prompt Engineering) في Midjourney هو سلاحك الأهم؛ افهم مصطلحات الإضاءة وزوايا وعدسات الكاميرا لتتحكم في المخرجات الفنية."
      }},
      {{
        id: "video",
        icon: "🎬",
        name: "مونتير ومخرج الفيديو والريلز",
        eng: "Video Editor & Motion Designer",
        challenge: "تقطيع الفترات الصامتة (Dead Air)، كتابة الترجمة (Captions) يدوياً، البحث عن B-roll مناسب، وتلوين المشاهد.",
        tools: ["Premiere Pro (Text-based editing)", "CapCut Pro (Dynamic Captions)", "Opus Clip (لاستخراج الريلز)", "Runway Gen-3 (توليد B-Roll)"],
        impact: "تقليص وقت التقطيع والترجمة بنسبة 80%، والتفرغ التام للإخراج الإبداعي والمؤثرات البصرية.",
        beforeVsAfter: {{
          before: "يوم كامل لقص بودكاست ساعة واستخراج 3 مقاطع ريلز قصيرة.",
          after: "استخراج أفضل 10 لحظات تلقائياً مع الكابشنز عبر Opus Clip، ورندرتها في Premiere خلال ساعتين فقط."
        }},
        prompt: "Cinematic slow-motion shot of [Action/Subject], glowing royal gold lighting in the background, luxury modern aesthetic, highly detailed, 4k, photorealistic movement.",
        goldenRule: "الذكاء الاصطناعي لا يعرف 'الإيقاع العاطفي' للفيديو. استخدم الـ AI للمهام الشاقة (التقطيع والترجمة)، واحتفظ بحسك الفني لضبط الموسيقى والانتقالات."
      }},
      {{
        id: "media_buyer",
        icon: "📊",
        name: "أخصائي الإعلانات والميديا بايينج",
        eng: "Media Buyer & Performance Marketer",
        challenge: "تحليل جداول البيانات المعقدة، مراقبة إرهاق الإعلانات (Ad Fatigue)، وتوزيع الميزانيات واختبار الـ A/B Testing.",
        tools: ["ChatGPT (Advanced Data Analysis)", "AdCreative.ai (لتوليد مئات التصاميم)", "Madgicx (أتمتة الحملات)"],
        impact: "تحويل الأرقام الصماء إلى رؤى استراتيجية (Insights) في ثوانٍ، واختبار عدد مضاعف من الإعلانات بتكلفة أقل.",
        beforeVsAfter: {{
          before: "تصدير CSV من Meta وقضاء 3 ساعات في Excel لمعرفة الإعلانات الرابحة.",
          after: "رفع الـ CSV لـ ChatGPT وسؤاله: 'حلل البيانات وأعطني أفضل 3 إعلانات من حيث الـ ROAS' في 10 ثوانٍ."
        }},
        prompt: "أنا أدير حملة إعلانية على فيسبوك بهدف [الهدف: Lead Gen/Sales] لعميل في قطاع [القطاع]. هذه هي مؤشرات الأداء الحالية: [أدخل الأرقام مثل CTR, CPC, ROAS]. بصفتك خبير Media Buying، قم بتحليل هذه الأرقام وحدد الخلل، ثم أعطني 3 خطوات عملية لتحسين الأداء فوراً.",
        goldenRule: "لا تثق بأتمتة المنصات ثقة عمياء. استخدم الـ AI للتحليل واستخراج الأنماط، لكن قرار رفع أو إيقاف الميزانية يجب أن يكون قرارك الاستراتيجي."
      }},
      {{
        id: "account_manager",
        icon: "🤝",
        name: "مدير الحسابات وخدمة العملاء",
        eng: "Account Manager",
        challenge: "صياغة إيميلات المتابعة، كتابة محاضر الاجتماعات (Meeting Minutes)، وتنظيم طلبات العميل وتوزيعها على الفريق.",
        tools: ["Fireflies.ai / Fathom (لتسجيل وتلخيص الاجتماعات)", "ChatGPT (لصياغة الإيميلات والتقارير)", "Grammarly"],
        impact: "القضاء التام على الأعمال الورقية الإدارية، وتوجيه وقتك لبناء علاقة استراتيجية قوية وزيادة ولاء العميل.",
        beforeVsAfter: {{
          before: "الانشغال بكتابة النوتس أثناء الاجتماع، ثم قضاء ساعة لتنسيقها وإرسالها للفريق.",
          after: "التركيز الكامل مع العميل، بينما يسجل Fireflies الاجتماع ويستخرج الـ Action Items ويرسلها تلقائياً."
        }},
        prompt: "إليك تفاصيل غير مرتبة لمكالمة مع عميل غاضب بسبب تأخر التسليم: [ضع الملاحظات]. اكتب بريداً إلكترونياً احترافياً ومطمئناً للعميل، تعتذر فيه بلباقة، وتشرح أن التأخير كان لضمان الجودة، وتحدد موعد تسليم نهائي غداً صباحاً.",
        goldenRule: "الذكاء الاصطناعي يفتقر إلى التعاطف البشري. راجع دائماً رسائل الـ AI لتنقيح النبرة الروبوتية وإضافة اللمسة الودية الخاصة بعميلك."
      }},
      {{
        id: "brand_strategist",
        icon: "👑",
        name: "استراتيجي البراند والهوية",
        eng: "Brand & Strategy Specialist",
        challenge: "إجراء أبحاث السوق، تحليل المنافسين، دراسة شخصية المشتري (Buyer Personas)، وبناء أدلة الهوية ونبرة الصوت.",
        tools: ["Perplexity AI (للبحث بالمصادر الحية)", "ChatGPT Plus (لبناء هياكل STP/SWOT)", "Claude 3.5 Sonnet (لسرد قصة البراند)"],
        impact: "إنجاز بحث سوقي كان يستغرق أسابيع في غضون أيام قليلة ببيانات أعمق وأدق.",
        beforeVsAfter: {{
          before: "قراءة 20 مقالاً وتقرير سوق لتحديد تموضع براند جديد.",
          after: "استخدام Perplexity لجمع أحدث تقارير السوق و ChatGPT لبناء جدول تحليل المنافسين وشخصيات المشتري بدقة مذهلة."
        }},
        prompt: "تخيل أنك استراتيجي علامات تجارية عالمي. قم بإنشاء 3 شخصيات مشترين (Buyer Personas) مفصلة لعلامة تجارية متخصصة في [مجال العميل]. لكل شخصية، اذكر: التركيبة السكانية، الأهداف، نقاط الألم (Pain Points)، كيف يحل منتجنا مشكلتها، وأفضل القنوات التسويقية للوصول إليها.",
        goldenRule: "الـ AI يعطيك المتوسط العام للسوق. لكي تكون OTB استثنائية، استخدم مخرجات الـ AI كنقطة انطلاق، ثم أضف رؤيتك (Insight) الإبداعية التي تكسر المألوف."
      }},
      {{
        id: "moderator",
        icon: "💬",
        name: "مسؤول الردود والموديريشن",
        eng: "Community Moderator & Sales Chat",
        challenge: "الرد على الأسئلة المتكررة (السعر، المواعيد)، الحفاظ على سرعة الاستجابة، واستيعاب العملاء الغاضبين وتأهيل الشراء.",
        tools: ["ManyChat مدعوم بـ OpenAI API", "Typebot", "Custom GPTs (مدربة على داتا العميل)"],
        impact: "الرد الفوري على 80% من الاستفسارات الشائعة على مدار الساعة، وتحويل العملاء الجادين فقط للمسؤول البشري.",
        beforeVsAfter: {{
          before: "نسخ ولصق نفس الرد 100 مرة يومياً وضياع العملاء الجادين في زحمة الرسائل.",
          after: "الشات بوت الذكي يجيب على الأسئلة ويجمع أرقام الهواتف، ثم ينبهك للتدخل الفوري وإتمام صفقة البيع."
        }},
        prompt: "أنت مسؤول خدمة عملاء ومبيعات يمثل علامة [اسم البراند]. هدفك الأساسي هو الرد على استفسارات العملاء بأسلوب [ودود/محترف/شعبي]، وتحفيزهم بلباقة على ترك رقم هواتفهم لحجز موعد. لا تختلق أسعاراً من عندك. إذا سأل العميل عن معلومات خارج الملف المرفق، اعتذر بلطف واطلب منه الانتظار لتحويله للمدير.",
        goldenRule: "الشفافية ترفع من تقبل العميل. دع البوت يقدم نفسه كمساعد ذكي لـ OTB، وتدخل أنت في اللحظة الحاسمة لإغلاق البيع."
      }},
      {{
        id: "sales_pr",
        icon: "💼",
        name: "مدير المبيعات والعلاقات العامة",
        eng: "Sales & PR Specialist",
        challenge: "البحث عن عملاء محتملين (Prospecting)، كتابة إيميلات باردة (Cold Outreach) مخصصة لا يتم تجاهلها، ومتابعة الصفقات.",
        tools: ["Apollo.io (لجلب بيانات صناع القرار)", "Instantly (أتمتة الإيميلات)", "ChatGPT (لتخصيص الرسائل)"],
        impact: "تخصيص (Personalization) مئات الرسائل البيعية يومياً لتبدو وكأنها مكتوبة خصيصاً لكل عميل، مما يرفع معدلات الرد بجنون.",
        beforeVsAfter: {{
          before: "إرسال إيميل موحد لـ 500 شركة والحصول على معدل فتح 5%.",
          after: "توليد رسائل مخصصة لكل شركة تذكر إنجازاً حديثاً لها عبر الـ AI، مما يرفع معدل الرد إلى 25%."
        }},
        prompt: "أنا مدير مبيعات في وكالة OTB. اكتب لي رسالة LinkedIn للتشبيك مع [اسم الشخص]، وهو [المسمى الوظيفي] في شركة [اسم الشركة]. أريد أن أبدأ الرسالة بتهنئته على [خبر أو إنجاز حديث للشركة]، ثم أعرض باختصار كيف يمكن لوكالتنا مساعدته في زيادة مبيعاته عبر الذكاء الاصطناعي. اجعل الرسالة أقل من 75 كلمة وبدون طابع بيعي فج.",
        goldenRule: "التخصيص هو الملك. الإيميل الذي يبدو آلياً سيذهب للـ Spam فوراً. استخدم الـ AI لاصطياد 'صنارة' (Hook) شخصية لكل صانع قرار."
      }},
      {{
        id: "operations",
        icon: "⚡",
        name: "القيادة وتطوير العمليات",
        eng: "Leadership & Operations",
        challenge: "مراقبة جودة المخرجات، تحديد الاختناقات في تدفق العمل، توثيق أدلة العمل القياسية (SOPs)، وإدارة الموارد والربحية.",
        tools: ["Make.com / n8n (لأتمتة سير العمل)", "Notion AI (لإدارة المشاريع)", "ChatGPT (لتحليل الأداء وبناء الأنظمة)"],
        impact: "تحويل الوكالة لمنظومة تعمل بدقة كالساعة السويسرية؛ تقليل الأخطاء البشرية، تسريع التسليم، ولوحات تحكم حية.",
        beforeVsAfter: {{
          before: "تتبع كل مهمة يدوياً عبر جروبات الواتساب وضياع الملفات واستنزاف أيام لتدريب موظف جديد.",
          after: "بمجرد توقيع العقد، يتم آلياً إنشاء المجلدات وتوليد المهام وإرسال رسائل الترحيب في ثوانٍ معدودة."
        }},
        prompt: "بصفتك خبير عمليات (Operations Manager)، قم بإنشاء إجراء تشغيل قياسي (SOP) مفصل خطوة بخطوة لعملية [اسم العملية، مثلاً: إطلاق حملة إعلانية جديدة لعميل]. قم بتضمين: الأدوار والمسؤوليات، الأدوات المستخدمة، قائمة التحقق (Checklist) قبل الإطلاق، ومؤشرات الأداء الرئيسية (KPIs) لقياس نجاح العملية.",
        goldenRule: "الأتمتة لا تصلح العمليات المكسورة. قم بتبسيط سير العمل (Workflow) ذهنياً وعلى الورق أولاً، ثم استخدم الـ AI لأتمتته بالكامل."
      }}
    ];

    function switchView(viewName, navEl) {{
      document.querySelectorAll(".lms-view").forEach(v => v.style.display = "none");
      const target = document.getElementById("view-" + viewName);
      if (target) target.style.display = "block";

      if (navEl) {{
        document.querySelectorAll(".sidebar .nav-item").forEach(item => item.classList.remove("active"));
        navEl.classList.add("active");
      }}
      window.scrollTo({{ top: 0, behavior: "smooth" }});
    }}

    function renderRolesGrid() {{
      const grid = document.getElementById("rolesGrid");
      let html = "";
      rolesSuperpowers.forEach((r, idx) => {{
        html += `
          <div class="role-card-btn ${{idx === 0 ? 'active' : ''}}" id="btn_role_${{r.id}}" onclick="selectRole('${{r.id}}')">
            <div>
              <span style="font-size: 2rem; display: block; margin-bottom: 0.5rem;">${{r.icon}}</span>
              <h3 style="font-family: var(--font-felfel); font-size: 1.15rem; color: var(--text-pure); line-height: 1.2;">${{r.name}}</h3>
              <p style="font-size: 0.75rem; color: var(--gold); font-family: var(--font-kookies); font-weight: 700;">${{r.eng}}</p>
            </div>
            <span style="font-size: 0.75rem; color: var(--cyan); margin-top: 1rem; font-weight: 600;">استعراض أدوات الـ AI ▾</span>
          </div>
        `;
      }});
      grid.innerHTML = html;
      selectRole(rolesSuperpowers[0].id);
    }}

    function selectRole(roleId) {{
      document.querySelectorAll(".role-card-btn").forEach(b => b.classList.remove("active"));
      const activeBtn = document.getElementById("btn_role_" + roleId);
      if (activeBtn) activeBtn.classList.add("active");

      const r = rolesSuperpowers.find(item => item.id === roleId);
      if (!r) return;

      let toolsHtml = "";
      r.tools.forEach(t => {{
        toolsHtml += `<span style="background: rgba(56, 189, 248, 0.1); color: var(--cyan); border: 1px solid rgba(56, 189, 248, 0.3); padding: 0.3rem 0.75rem; border-radius: var(--radius-full); font-size: 0.8rem; font-weight: 600;">🛠️ ${{t}}</span>`;
      }});

      const stage = document.getElementById("roleStage");
      stage.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 1rem; margin-bottom: 1.5rem;">
          <div>
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">دليل التمكين والتفوق اليومي</span>
            <h2 style="font-family: var(--font-felfel); font-size: 1.85rem; color: var(--text-pure); margin-top: 0.2rem;">${{r.icon}} ${{r.name}} (${{r.eng}})</h2>
          </div>
          <button class="btn btn-primary" onclick="copyText(document.getElementById('rolePromptBox').innerText)">📋 نسخ أمر الـ AI المعتمد</button>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">
          <div style="background: rgba(225, 29, 72, 0.08); border: 1px solid rgba(225, 29, 72, 0.25); border-radius: var(--radius-sm); padding: 1.25rem;">
            <h4 style="color: var(--crimson); font-size: 0.95rem; margin-bottom: 0.4rem; font-weight: 700;">🛑 أين يضيع وقتك يومياً؟ (التحدي المعتاد):</h4>
            <p style="font-size: 0.88rem; color: var(--text-main); line-height: 1.7;">${{r.challenge}}</p>
          </div>

          <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: var(--radius-sm); padding: 1.25rem;">
            <h4 style="color: var(--emerald); font-size: 0.95rem; margin-bottom: 0.4rem; font-weight: 700;">🚀 كيف يضاعف الـ AI إنتاجيتك 5 أضعاف؟:</h4>
            <p style="font-size: 0.88rem; color: var(--text-main); line-height: 1.7;">${{r.impact}}</p>
          </div>
        </div>

        <div style="margin-bottom: 1.5rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.6rem; font-weight: 700;">🛠️ ترسانة الأدوات الموصى بها لتخصصك:</h4>
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">${{toolsHtml}}</div>
        </div>

        <div class="card" style="background: var(--bg-code); margin-bottom: 1.5rem;">
          <h4 style="font-size: 0.95rem; color: var(--gold); margin-bottom: 0.6rem; font-weight: 700;">🔄 التحول الجذري في طريقة الشغل:</h4>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; font-size: 0.88rem;">
            <div style="border-left: 1px solid var(--border); padding-left: 1rem;">
              <span style="color: var(--text-dim); font-weight: 700; display: block; margin-bottom: 0.25rem;">❌ قبل استخدام الذكاء الاصطناعي:</span>
              <p style="color: var(--text-muted);">${{r.beforeVsAfter.before}}</p>
            </div>
            <div>
              <span style="color: var(--emerald); font-weight: 700; display: block; margin-bottom: 0.25rem;">✅ بعد استخدام أدوات الـ AI:</span>
              <p style="color: var(--text-pure);">${{r.beforeVsAfter.after}}</p>
            </div>
          </div>
        </div>

        <div style="margin-bottom: 1.5rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <h4 style="font-size: 0.95rem; color: var(--cyan); font-weight: 700;">📋 الأمر الجاهز الفوري (Plug-and-Play Prompt):</h4>
            <span style="font-size: 0.75rem; color: var(--text-dim);">جاهز للتطبيق لعملاء OTB</span>
          </div>
          <div id="rolePromptBox" class="code-box">${{r.prompt}}</div>
        </div>

        <div style="background: var(--gold-dim); border: 1px solid var(--border-gold); border-radius: var(--radius-sm); padding: 1.25rem;">
          <h4 style="color: var(--gold); font-size: 0.95rem; margin-bottom: 0.35rem; font-weight: 700;">💡 النصيحة الذهبية لملوك المدينة:</h4>
          <p style="font-size: 0.9rem; color: var(--text-main); line-height: 1.8;">${{r.goldenRule}}</p>
        </div>
      `;
    }}

    function renderCoursesAccordion(list) {{
      const container = document.getElementById("coursesAccordionList");
      let html = "";
      list.forEach(c => {{
        const isDone = localStorage.getItem("otb_done_" + c.id) === "true";
        let unitsHtml = "";
        c.units.forEach((u, i) => {{
          unitsHtml += `<li style="margin-bottom: 0.35rem;"><b>الوحدة ${{i + 1}}:</b> ${{u}}</li>`;
        }});

        html += `
          <div class="card course-card" id="card_${{c.id}}" style="padding: 1.25rem 1.5rem; margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; cursor: pointer;" onclick="toggleCourseDetails('${{c.id}}')">
              <div>
                <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">المرحلة 0${{c.phase}} · ${{c.badge}}</span>
                <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-top: 0.2rem;">${{c.icon}} ${{c.title}}</h3>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem;">
                <span style="font-size: 0.8rem; color: ${{isDone ? 'var(--emerald)' : 'var(--text-dim)'}};">${{isDone ? '✅ مكتمل' : '○ قيد الانتظار'}}</span>
                <span style="font-size: 0.9rem; color: var(--text-dim);">▾</span>
              </div>
            </div>

            <div id="details_${{c.id}}" style="display: none; margin-top: 1.25rem; padding-top: 1.25rem; border-top: 1px solid var(--border);">
              <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.25rem;">${{c.desc}}</p>
              
              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.4rem;">📖 الوحدات التدريبية (${{c.pages}} صفحة منهج):</h4>
                <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-muted); line-height: 1.8;">
                  ${{unitsHtml}}
                </ul>
              </div>

              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--cyan); margin-bottom: 0.35rem;">🤖 أمر الذكاء الاصطناعي المعتمد (RCIC Prompt):</h4>
                <div class="code-box">${{c.prompt}}</div>
                <button class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.35rem 0.8rem;" onclick="copyText(this.previousElementSibling.innerText)">📋 نسخ الأمر</button>
              </div>

              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--emerald); margin-bottom: 0.3rem;">💼 دراسة الحالة التطبيقية:</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">${{c.case_study}}</p>
              </div>

              <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--border);">
                <div>
                  <h4 style="font-size: 0.95rem; color: var(--gold-light); margin-bottom: 0.2rem;">🧪 التكليف العملي:</h4>
                  <p style="font-size: 0.85rem; color: var(--text-muted);">${{c.lab}}</p>
                </div>
                <button class="btn ${{isDone ? 'btn-secondary' : 'btn-primary'}}" style="font-size: 0.8rem; padding: 0.4rem 1rem;" onclick="toggleCourseDone('${{c.id}}')">
                  ${{isDone ? '✅ تم إكمال المقرر' : '🎯 تحديد كـ مكتمل'}}
                </button>
              </div>
            </div>
          </div>
        `;
      }});
      container.innerHTML = html;
    }}

    function toggleCourseDetails(id) {{
      const d = document.getElementById("details_" + id);
      if (d) d.style.display = (d.style.display === "none") ? "block" : "none";
    }}

    function toggleCourseDone(id) {{
      const key = "otb_done_" + id;
      const cur = localStorage.getItem(key) === "true";
      localStorage.setItem(key, !cur);
      showToast(!cur ? "👑 تم تسجيل إكمال المقرر بنجاح!" : "تم إلغاء التحديد");
      updateLmsProgress();
      renderCoursesAccordion(coursesData);
    }}

    function filterCourses(cat, btn) {{
      document.querySelectorAll("#view-courses .tab-pill").forEach(p => p.classList.remove("active"));
      btn.classList.add("active");

      if (cat === "all") renderCoursesAccordion(coursesData);
      else renderCoursesAccordion(coursesData.filter(c => c.cat === cat));
    }}

    function updateLmsProgress() {{
      let doneCount = 0;
      coursesData.forEach(c => {{
        if (localStorage.getItem("otb_done_" + c.id) === "true") doneCount++;
      }});
      const pct = Math.round((doneCount / coursesData.length) * 100);
      document.getElementById("progressText").innerText = pct + "% مكتمل (" + doneCount + " من 19)";
      document.getElementById("progressFill").style.width = pct + "%";
    }}

    function resetProgress() {{
      coursesData.forEach(c => localStorage.removeItem("otb_done_" + c.id));
      showToast("تمت إعادة ضبط التقدم بنجاح");
      updateLmsProgress();
      renderCoursesAccordion(coursesData);
    }}

    // SPRINT DATA
    const sprintLessons = [
      {{
        day: 1,
        title: "اليوم الأول: تحليل السوق والتموضع وبناء الهوية (STP & Positioning)",
        audience: "الاستراتيجيون ومدراء الحسابات",
        concepts: "• <b>Segmentation:</b> تقسيم السوق جغرافياً وسلوكياً.<br>• <b>Targeting:</b> استهداف الشريحة الأعلى ربحية (LTV).<br>• <b>Positioning:</b> حفر تموضع ملكي لا يُنسى في ذهن العميل.",
        caseStudy: "تحويل MIX Coffee من كافيه تقليدي إلى وجهة شبابية أولى بهوية داكنة فاخرة، مما رفع التفاعل بنسبة 180%.",
        prompt: "معادلة التموضع (Positioning Statement):\\n[Target Audience] + [Category] + [Differentiating Benefit] + [Reason to Believe]",
        lab: "اختيار عميل وتعبئة وثيقة البريف واستخراج 3 زوايا تسويقية تستغل فجوات المنافسين."
      }},
      {{
        day: 2,
        title: "اليوم الثاني: الكوبي رايتنج الإعلاني وسيكولوجية الفيديو القصير",
        audience: "صناع المحتوى والمصممون والمونتيرون",
        concepts: "• <b>قاعدة الـ 3 ثوانٍ (Hook Rate > 35%):</b> كسر التمرير بصرياً وصوتياً.<br>• <b>صيغة PAS:</b> توضيح المشكلة (Problem)، تهويل أثرها (Agitation)، ثم تقديم الحل الفوري (Solution).<br>• <b>صوتيات الـ ASMR:</b> رفع الإشباع البصري والصوتي في فيديوهات المنتجات.",
        caseStudy: "فيديو ريلز لـ Rancho's EG يبرز تفاصيل تقطيع البرجر الملحمي، محققاً 450 ألف مشاهدة ورفع مبيعات الواتساب بنسبة 65%.",
        prompt: "Problem: تعبت من ساندوتشات البرجر اللي كلها عيش؟\\nAgitation: بتدفع مبلغ وفي الآخر بيجيلك بارد وتندم.\\nSolution: في Rancho's قطمة واحدة من الـ Smoked Beef بالصوص السري هتعرف يعني إيه برجر ملوك!",
        lab: "كتابة 3 نصوص إعلانية بـ 3 زوايا مختلفة واسكريبت فيديو 15 ثانية."
      }},
      {{
        day: 3,
        title: "اليوم الثالث: ميديا بايينج الأداء وسكيلينج الـ ROAS",
        audience: "الميديا بايرز وهندسة النمو",
        concepts: "• <b>Advantage+ & Broad Targeting:</b> الاستهداف المفتوح مع تغذية الخوارزمية بكرييتفز قوية.<br>• <b>Conversions API (CAPI):</b> ربط التتبع بالسيرفر لتجاوز قيود iOS 14.5+.<br>• <b>قاعدة الـ 20%:</b> رفع الميزانية 20% فقط كل 48-72 ساعة لحماية استقرار الحملة.",
        caseStudy: "إعادة هيكلة إعلانات Dr. Zaghloul Jewelry بحملات Advantage+ محققة ROAS تجاوز 7.5x.",
        prompt: "Break-Even ROAS = 1 / Gross Profit Margin %\\n(إذا كان الهامش 25%، التعادل = 4.0x)",
        lab: "تدقيق حساب إعلاني نشط، فحص جودة مطابقة CAPI، وإعداد مصفوفة الميزانية الأسبوعية."
      }},
      {{
        day: 4,
        title: "اليوم الرابع: الذكاء الاصطناعي وهندسة الأوامر وأتمتة الواتساب",
        audience: "جميع أعضاء الفريق",
        concepts: "• <b>إطار RCIC:</b> Role (الدور) + Context (السياق) + Instruction (التعليمات) + Constraints (القيود).<br>• <b>مسار WhatsApp Business API:</b> ترحيب فوري، تصنيف الطلب، إرسال الكتالوج، وتسجيل البيع تلقائياً.",
        caseStudy: "بناء بوت واتساب لمختبرات علاج (Elag Labs) يستقبل ويؤهل أكثر من 800 حجز منزلي شهرياً.",
        prompt: "Role: Senior Direct-Response Copywriter at OTB Agency.\\nContext: Client is [Brand] in Egypt. Target: 20-35.\\nTask: Write 3 ad copies using PAS framework in refined modern Egyptian Arabic.\\nConstraints: Bold tone, high-urgency CTA for WhatsApp ordering.",
        lab: "توليد 5 إعلانات وبرودكت شوت 3D عبر الـ AI، ورسم مخطط لمسار ردود الواتساب."
      }},
      {{
        day: 5,
        title: "اليوم الخامس: عقود الريتينر الشهرية وتوسيع الأعمال",
        audience: "الإدارة ومدراء الحسابات",
        concepts: "• <b>منع الهدر:</b> التسليمات الذكية وتأمين سير العمل.<br>• <b>اتفاقية مستوى الخدمة (SLA):</b> مراجعة خلال 24 ساعة والتصعيد بعد 48 ساعة.<br>• <b>باقة Dominance Retainer ($2,500/شهر):</b> هوية كاملة + 24 محتوى + ميديا بايينج + أتمتة.",
        caseStudy: "إغلاق عقود ريتينر طويلة الأجل مع عملاء OTB بالاعتماد على إثبات العائد المالي بدلاً من عدد البوستات.",
        prompt: "نحن في OTB لا نبيع مجرد بوستات وتصاميم، بل نبني لك محرك نمو متكامل يربط الهوية بالإعلانات الممولة لتحقيق أعلى عائد مالي مضمون.",
        lab: "تقديم مقترح خطة نمو شهرية مصغرة لعميل حقيقي تتضمن الاستراتيجية وعينة المحتوى ومسار الأتمتة."
      }}
    ];

    function loadSprintDay(dNum, btn) {{
      if (btn) {{
        document.querySelectorAll("#view-sprint .tab-pill").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
      }}
      const d = sprintLessons.find(item => item.day === dNum);
      document.getElementById("sprintLessonStage").innerHTML = `
        <div style="font-size: 0.8rem; color: var(--gold); font-weight: 700; margin-bottom: 0.35rem;">المستهدفون: ${{d.audience}}</div>
        <h3 style="font-family: var(--font-felfel); font-size: 1.35rem; color: var(--text-pure); margin-bottom: 1.25rem;">${{d.title}}</h3>

        <div style="margin-bottom: 1.25rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.35rem;">📖 المفاهيم والنماذج الأساسية:</h4>
          <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.8;">${{d.concepts}}</p>
        </div>

        <div style="margin-bottom: 1.25rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.35rem;">💼 دراسة الحالة التطبيقية:</h4>
          <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.7;">${{d.caseStudy}}</p>
        </div>

        <div style="margin-bottom: 1.25rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.35rem;">📐 القالب / المعادلة:</h4>
          <div class="code-box">${{d.prompt}}</div>
        </div>

        <div>
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.35rem;">🧪 التكليف اليومي:</h4>
          <p style="font-size: 0.9rem; color: var(--gold-light); line-height: 1.7;"><b>المطلوب تسليمه:</b> ${{d.lab}}</p>
        </div>
      `;
    }}

    // PROMPTS STUDIO
    function updateLivePrompt() {{
      const task = document.getElementById("promptTask").value;
      const brand = document.getElementById("promptBrand").value || "البراند";
      const out = document.getElementById("livePromptCode");

      if (task === "copy") {{
        out.innerText = "Role: Senior Direct-Response Copywriter at OTB Agency.\\n" +
          "Context: Running high-performance Meta Ads for " + brand + " in Egypt.\\n" +
          "Task: Write 3 ad copy variations using PAS framework in refined modern Egyptian Arabic.\\n" +
          "Constraints: Hook under 8 words, bold royal tone, strong urgency CTA linking to WhatsApp menu.";
      }} else if (task === "reels") {{
        out.innerText = "Role: Short-Form Video Director at OTB Agency.\\n" +
          "Context: Instagram Reel / TikTok for " + brand + ".\\n" +
          "Task: Write a shot-by-shot 15-second script with 3-second hook, fast ASMR cuts, and direct promotional offer.\\n" +
          "Format: Table [Time (Sec) | Visual Action | Audio SFX | Voiceover].";
      }} else if (task === "media") {{
        out.innerText = "Role: Principal Media Buyer and Growth Architect at OTB Agency.\\n" +
          "Context: Analyzing Meta Ads performance for " + brand + ". Target ROAS is 4.0x.\\n" +
          "Task: Diagnose Hook Rate and Click-to-Purchase conversion drop-offs and provide a 48-hour scaling plan.";
      }} else if (task === "design") {{
        out.innerText = "/imagine prompt: Ultra-realistic commercial 3D product shot of " + brand + ", obsidian noir stone podium, royal gold accents and droplets, dramatic rim lighting, cinematic 8k render --ar 9:16 --style raw --v 6.0";
      }} else if (task === "retainer") {{
        out.innerText = "Role: Commercial Director at OTB Agency.\\n" +
          "Context: Drafting a $2,500/month Dominance Retainer Proposal for " + brand + ".\\n" +
          "Task: Write a 1-page executive proposal covering market positioning, 90-day growth roadmap, and expected ROAS targets.";
      }}
    }}

    // CERTIFICATE GENERATOR
    function generateOfficialCert() {{
      const name = document.getElementById("certName").value || "خريج الأكاديمية";
      const certId = "OTB-" + Math.floor(100000 + Math.random() * 900000);
      const date = new Date().toLocaleDateString('ar-EG', {{ year: 'numeric', month: 'long', day: 'numeric' }});
      const wrap = document.getElementById("certContainer");

      wrap.style.display = "block";
      wrap.innerHTML = `
        <div style="background: #030406; border: 4px solid var(--gold); border-radius: 20px; padding: 3.5rem 2.5rem; text-align: center; margin-top: 2rem; box-shadow: 0 0 60px rgba(197, 160, 89, 0.35);">
          <div style="font-size: 3.2rem; margin-bottom: 0.5rem;">👑</div>
          <div style="font-size: 0.85rem; letter-spacing: 3px; color: var(--gold); text-transform: uppercase; font-family: var(--font-kookies); font-weight: 700;">OTB Marketing Studio · City Kings</div>
          <div style="font-family: var(--font-royal); font-size: 2.2rem; color: var(--text-pure); margin: 0.85rem 0; font-weight: 900; letter-spacing: 1px;">CERTIFICATE OF AI MASTERY</div>
          <p style="color: var(--text-dim); font-size: 1rem;">تشهد أكاديمية وكالة OTB لتمكين الذكاء الاصطناعي وهندسة النمو بأن</p>
          <h2 style="font-family: var(--font-felfel); font-size: 2.5rem; color: var(--gold); margin: 0.85rem 0; font-weight: 900;">${{name}}</h2>
          <p style="color: var(--text-main); max-width: 580px; margin: 0 auto 2rem auto; font-size: 0.95rem; line-height: 1.8;">
            قد أتم بنجاح متطلبات أكاديمية <b>الذكاء الاصطناعي التوليدي والنمو الرقمي (AI-Powered Marketing & Growth Engineering)</b> وأصبح مؤهلاً لمضاعفة الإنتاجية 5x وتطبيق استراتيجيات ملوك المدينة.
          </p>
          <div style="display: flex; justify-content: space-around; border-top: 1px solid var(--border-gold); padding-top: 1.5rem; font-size: 0.88rem;">
            <div>
              <div style="color: var(--text-dim); font-size: 0.75rem;">رقم الاعتماد الرسمي</div>
              <div style="font-family: var(--font-mono); color: var(--gold); font-weight: 700;">${{certId}}</div>
            </div>
            <div>
              <div style="color: var(--text-dim); font-size: 0.75rem;">تاريخ المنح</div>
              <div style="color: var(--text-pure); font-weight: 600;">${{date}}</div>
            </div>
            <div>
              <div style="color: var(--text-dim); font-size: 0.75rem;">الاعتماد الرقمي</div>
              <div style="color: var(--gold); font-weight: 800;">OTB Agency 👑</div>
            </div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 1.5rem;">
          <button class="btn btn-secondary" onclick="window.print()">🖨️ طباعة الشهادة / حفظ PDF</button>
        </div>
      `;
      wrap.scrollIntoView({{ behavior: "smooth" }});
      showToast("👑 تم إصدار شهادة الاعتماد بنجاح!");
    }}

    // GLOBAL SEARCH
    function handleGlobalSearch() {{
      const q = document.getElementById("globalSearch").value.toLowerCase();
      if (!q) {{
        renderCoursesAccordion(coursesData);
        return;
      }}
      switchView('courses');
      const filtered = coursesData.filter(c => 
        c.title.toLowerCase().includes(q) || 
        c.desc.toLowerCase().includes(q) ||
        c.badge.toLowerCase().includes(q) ||
        c.prompt.toLowerCase().includes(q)
      );
      renderCoursesAccordion(filtered);
    }}

    // INITIALIZATION
    renderRolesGrid();
    renderCoursesAccordion(coursesData);
    loadSprintDay(1);
    updateLivePrompt();
    updateLmsProgress();
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(p_master_lms)

print("Generated clean index.html focused on Role AI Superpowers")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
