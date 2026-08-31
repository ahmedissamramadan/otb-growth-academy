import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from generate_master_academy import COURSES_DATA

courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

# ==============================================================================
# 1. ENTERPRISE LMS STYLESHEET (style.css)
# ==============================================================================
lms_css = """
:root {
  --bg-app: #080A0F;
  --bg-sidebar: #0C0F17;
  --bg-main: #0F131D;
  --bg-card: rgba(18, 24, 38, 0.7);
  --bg-card-hover: rgba(26, 34, 52, 0.85);
  --bg-input: #090C12;
  --bg-code: #05070A;

  --border: rgba(255, 255, 255, 0.08);
  --border-focus: rgba(212, 168, 83, 0.5);
  --border-gold: rgba(212, 168, 83, 0.25);

  --gold: #D4A853;
  --gold-light: #F3E5C8;
  --gold-gradient: linear-gradient(135deg, #F3E5C8 0%, #D4A853 50%, #9B7023 100%);
  --gold-dim: rgba(212, 168, 83, 0.1);
  --gold-glow: 0 0 30px rgba(212, 168, 83, 0.15);

  --cyan: #38BDF8;
  --emerald: #10B981;
  --crimson: #E11D48;
  --purple: #A855F7;

  --text-pure: #FFFFFF;
  --text-main: #E2E8F0;
  --text-muted: #94A3B8;
  --text-dim: #64748B;

  --font-ar: 'Readex Pro', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --font-royal: 'Cinzel', serif;

  --radius-xs: 6px;
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-full: 9999px;

  --transition-fast: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-smooth: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
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
  line-height: 1.75;
  font-size: 0.95rem;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* SCROLLBAR */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg-app); }
::-webkit-scrollbar-thumb { background: rgba(212, 168, 83, 0.25); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }

/* APP LAYOUT */
.app-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(12, 15, 23, 0.92);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  height: 64px;
  padding: 0 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-section {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.brand-crown {
  font-size: 1.6rem;
  filter: drop-shadow(0 0 8px rgba(212, 168, 83, 0.4));
}

.brand-info h1 {
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--text-pure);
  line-height: 1.2;
}

.brand-info p {
  font-size: 0.7rem;
  color: var(--gold);
  font-weight: 600;
  letter-spacing: 0.5px;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
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
  padding: 0.45rem 1rem 0.45rem 2rem;
  color: var(--text-pure);
  font-size: 0.85rem;
  outline: none;
  transition: var(--transition-fast);
}

.search-input:focus {
  border-color: var(--gold);
  box-shadow: 0 0 0 3px rgba(212, 168, 83, 0.15);
}

.internal-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(16, 185, 129, 0.1);
  color: var(--emerald);
  border: 1px solid rgba(16, 185, 129, 0.3);
  padding: 0.3rem 0.75rem;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 700;
}

/* APP SHELL CONTAINER */
.app-shell {
  display: flex;
  min-height: calc(100vh - 64px);
}

/* LEFT SIDEBAR */
.sidebar {
  width: 320px;
  background: var(--bg-sidebar);
  border-left: 1px solid var(--border);
  overflow-y: auto;
  height: calc(100vh - 64px);
  position: sticky;
  top: 64px;
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
  padding: 0.6rem 0.75rem;
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 500;
  transition: var(--transition-fast);
  cursor: pointer;
  margin-bottom: 0.2rem;
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
  margin-left: 0.5rem;
}

/* MAIN CONTENT STAGE */
.main-stage {
  flex: 1;
  background: var(--bg-main);
  padding: 2.5rem 3rem 6rem 3rem;
  overflow-y: auto;
  max-width: 1100px;
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

/* AUDIO STRIP */
.audio-player-box {
  background: var(--bg-input);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 0.85rem 1.25rem;
  margin-bottom: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.audio-player-box audio {
  height: 32px;
  direction: ltr !important;
  max-width: 320px;
  outline: none;
}

/* CARDS */
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  margin-bottom: 1.25rem;
  transition: var(--transition-fast);
}

.card:hover {
  border-color: var(--border-gold);
  background: var(--bg-card-hover);
}

.card-title {
  font-size: 1.15rem;
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
  padding: 0.6rem 1.35rem;
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
  background: #06070A;
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

/* RESPONSIVE */
@media (max-width: 900px) {
  .app-shell { flex-direction: column; }
  .sidebar { width: 100%; height: auto; position: static; border-left: none; border-bottom: 1px solid var(--border); }
  .main-stage { padding: 1.5rem 1rem; }
  .search-input-wrap { display: none; }
}
"""

with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(lms_css)

print("Generated Enterprise LMS style.css")

# ==============================================================================
# 2. SHARED_UI.JS WITH FOOLPROOF STATE MANAGEMENT & SEARCH
# ==============================================================================
shared_lms_js = """
// OTB Agency Enterprise LMS Engine
function showToast(msg) {
  let toast = document.getElementById("otbToast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "otbToast";
    toast.className = "toast";
    document.body.appendChild(toast);
  }
  toast.innerText = msg;
  toast.classList.add("show");
  setTimeout(() => { toast.classList.remove("show"); }, 2500);
}

function copyText(txt, successMsg = "تم النسخ بنجاح للحافظة! 👑") {
  if (!txt) return;
  navigator.clipboard.writeText(txt).then(() => {
    showToast(successMsg);
  }).catch(err => {
    console.error("Copy failed", err);
  });
}
"""

with open(os.path.join(BASE_DIR, "shared_ui.js"), "w", encoding="utf-8") as f:
    f.write(shared_lms_js)

print("Generated shared_ui.js")

# ==============================================================================
# 3. ENTERPRISE LMS MASTER TEMPLATE (index.html)
# ==============================================================================
p_master_lms = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Growth Academy — البوابة المعرفية الموحدة</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=JetBrains+Mono:wght@500;600;700&family=Readex+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- APP HEADER -->
  <header class="app-header">
    <div class="brand-section">
      <span class="brand-crown">👑</span>
      <div class="brand-info">
        <h1>OTB GROWTH ACADEMY</h1>
        <p>THE CITY KINGS · INTERNAL LMS & KNOWLEDGE ENGINE</p>
      </div>
    </div>

    <div class="search-input-wrap">
      <input type="text" id="globalSearch" class="search-input" placeholder="🔍 بحث في المناهج والأوامر..." oninput="handleGlobalSearch()">
    </div>

    <div class="header-actions">
      <span class="internal-badge">🔒 بوابة داخلية لفريق OTB</span>
      <a href="https://notebooklm.google.com/notebook/76ef5be2-d7d2-4a33-a88d-f88fc0fe1148" target="_blank" class="btn btn-secondary" style="font-size: 0.78rem; padding: 0.35rem 0.85rem;">
        ✨ مشروع NotebookLM
      </a>
    </div>
  </header>

  <!-- APP SHELL -->
  <div class="app-shell">
    
    <!-- LEFT SIDEBAR -->
    <aside class="sidebar">
      
      <!-- NAVIGATION SECTIONS -->
      <div class="sidebar-section">
        <div class="sidebar-heading">المسارات الرئيسية</div>
        <div class="nav-item active" onclick="switchView('overview', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">🏠</span>
            <span>نظرة عامة والمنهج</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--gold);">Overview</span>
        </div>
        <div class="nav-item" onclick="switchView('courses', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">📚</span>
            <span>المقررات الـ 19 المفصلة</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--text-dim);">19 P.</span>
        </div>
        <div class="nav-item" onclick="switchView('mindmap', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">🗺️</span>
            <span>الخريطة الذهنية والتفكيك</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--text-dim);">Map</span>
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
        <div class="sidebar-heading">أدوات الاستوديو والتشغيل</div>
        <div class="nav-item" onclick="switchView('prompts', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">🤖</span>
            <span>استوديو أوامر الذكاء الاصطناعي</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--cyan);">RCIC</span>
        </div>
        <div class="nav-item" onclick="switchView('cases', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">💼</span>
            <span>دراسات حالة عملاء OTB</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--emerald);">ROI</span>
        </div>
        <div class="nav-item" onclick="switchView('sops', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">📋</span>
            <span>إجراءات CoreLink ومولد البريفات</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--text-dim);">SOPs</span>
        </div>
      </div>

      <div class="sidebar-section">
        <div class="sidebar-heading">الاعتماد والموارد</div>
        <div class="nav-item" onclick="switchView('quiz', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">📝</span>
            <span>اختبار الكفاءة والشهادة</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--gold);">Cert</span>
        </div>
        <div class="nav-item" onclick="switchView('downloads', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">📥</span>
            <span>مركز تحميل الأصول والمستندات</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--text-dim);">Files</span>
        </div>
      </div>

      <!-- SIDEBAR FOOTER CONTACT WITH FOOLPROOF LTR NUMBER -->
      <div style="border-top: 1px solid var(--border); padding-top: 1rem; margin-top: 2rem; font-size: 0.8rem; color: var(--text-dim);">
        <div style="margin-bottom: 0.35rem; color: var(--text-pure); font-weight: 700;">OTB Agency — City Kings 👑</div>
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
          <div style="font-size: 0.8rem; color: var(--text-dim); font-weight: 600;">نسبة الإنجاز في الأكاديمية:</div>
          <div style="font-size: 1.15rem; font-weight: 800; color: var(--gold);" id="progressText">0% مكتمل</div>
        </div>
        <div class="progress-track">
          <div class="progress-fill" id="progressFill"></div>
        </div>
        <button class="btn btn-secondary" style="font-size: 0.78rem; padding: 0.35rem 0.85rem;" onclick="resetProgress()">إعادة ضبط</button>
      </div>

      <!-- AUDIO PLAYER BOX -->
      <div class="audio-player-box">
        <div style="display: flex; align-items: center; gap: 0.6rem;">
          <span style="font-size: 1.2rem;">🎙️</span>
          <div>
            <div style="font-size: 0.88rem; font-weight: 700; color: var(--text-pure);">التدريب الصوتي الاستراتيجي المعتمد</div>
            <div style="font-size: 0.75rem; color: var(--gold);">Gemini Studio Growth Engineering Deep Dive Podcast</div>
          </div>
        </div>
        <audio controls>
          <source src="track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" type="audio/mp4">
        </audio>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 1: OVERVIEW -->
      <!-- ========================================== -->
      <div id="view-overview" class="lms-view">
        <div style="margin-bottom: 2.5rem;">
          <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700; letter-spacing: 1px;">THE CITY KINGS INTERNAL ACADEMY 2026</span>
          <h2 style="font-size: 1.85rem; color: var(--text-pure); margin: 0.35rem 0 0.75rem 0; font-weight: 800;">بوابة التعلم وهندسة النمو</h2>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8;">
            هذه المنظومة هي البوابة المعرفية والتشغيلية الموحدة لفرق عمل وكالة OTB (16 دوراً وظيفياً). تم تفكيك المنهج المستخلص من 2,400+ صفحة إلى 19 مساراً تدريبياً، وأكثر من 50 أمر ذكاء اصطناعي، ودراسات حالة بالأرقام لعملاء الوكالة.
          </p>
        </div>

        <h3 style="font-size: 1.15rem; color: var(--text-pure); margin-bottom: 1.25rem; font-weight: 700;">المراحل المعمارية الـ 4 للمنهج:</h3>
        
        <div class="card" onclick="switchView('courses'); filterCoursesByPhase(1);" style="cursor: pointer;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <h4 class="card-title" style="margin: 0;">👑 المرحلة 01: الاستراتيجية، التموضع، وبناء الهوية</h4>
            <span style="font-size: 0.78rem; color: var(--gold);">4 مقررات</span>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted);">
            مبادئ التسويق الحديث، نموذج التموضع STP، كراسة الهوية ونبرة الصوت The Ruler، وإجراءات CoreLink CRM لمنع الهدر.
          </p>
        </div>

        <div class="card" onclick="switchView('courses'); filterCoursesByPhase(2);" style="cursor: pointer;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <h4 class="card-title" style="margin: 0;">✍️ المرحلة 02: الكرييتف، المحتوى الفيرال، وسيو محركات البحث</h4>
            <span style="font-size: 0.78rem; color: var(--cyan);">4 مقررات</span>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted);">
            الكوبي رايتنج وصيغ PAS/AIDA، سيكولوجية الفيديو القصير وريلز 3-Sec Hooks، سيو محركات البحث الشامل، وسيو يوتيوب.
          </p>
        </div>

        <div class="card" onclick="switchView('courses'); filterCoursesByPhase(3);" style="cursor: pointer;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <h4 class="card-title" style="margin: 0;">📊 المرحلة 03: ميديا بايينج الأداء وسكيلينج الـ ROAS</h4>
            <span style="font-size: 0.78rem; color: var(--emerald);">5 مقررات</span>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted);">
            إعلانات Meta وحملات Advantage+ وتتبع CAPI، إعلانات تيك توك، إعلانات سناب شات للخليج، لينكد إن B2B، ومنصة إكس.
          </p>
        </div>

        <div class="card" onclick="switchView('courses'); filterCoursesByPhase(4);" style="cursor: pointer;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <h4 class="card-title" style="margin: 0;">🤖 المرحلة 04: الذكاء الاصطناعي، الأتمتة، وعقود الريتينر</h4>
            <span style="font-size: 0.78rem; color: var(--purple);">6 مقررات</span>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted);">
            أوامر RCIC التوليدية، أتمتة WhatsApp API، الإيميل ماركتنج، الجروث هاكينج، إغلاق عقود الريتينر ($2,500/شهر)، والتميز المهني.
          </p>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 2: 19 COURSES -->
      <!-- ========================================== -->
      <div id="view-courses" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-size: 1.6rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 800;">📚 موسوعة المقررات الـ 19 المفصلة</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">انقر على أي مقرر لاستعراض وحداته الدراسية، أمر الـ AI المعتمد، ودراسة الحالة والتكليف العملي.</p>
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
      <!-- VIEW 3: MINDMAP -->
      <!-- ========================================== -->
      <div id="view-mindmap" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-size: 1.6rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 800;">🗺️ الخريطة الذهنية والتفكيك الهيكلي</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">شجرة مفاهيمية تقسم المنهج إلى 4 مراحل و 80+ تخصصاً فرعياً مصممة لأقسام الوكالة.</p>
        </div>

        <div class="card" style="margin-bottom: 1.25rem;">
          <h4 style="color: var(--gold); font-size: 1.05rem; margin-bottom: 0.6rem;">👑 المرحلة 01: الأساسات وبناء الهوية والتشغيل</h4>
          <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-muted); line-height: 1.8;">
            <li><b>مبادئ التسويق الحديث:</b> 4Ps إلى 4Cs، سيكولوجية اتخاذ القرار، رحلة العميل وبناء الـ Persona.</li>
            <li><b>الاستراتيجية والتخطيط:</b> تحليل STP، إطار SOSTAC، ومؤشرات الأداء الذكية (SMART KPIs).</li>
            <li><b>بناء الهوية والعلامة:</b> النمط النفسي The Ruler لـ OTB، كراسة الهوية ونبرة الصوت، وتموضع الهيبة.</li>
            <li><b>الانضباط التشغيلي CoreLink CRM:</b> نماذج البريف الإلزامي، قفل التبعيات، واتفاقيات الـ SLA.</li>
          </ul>
        </div>

        <div class="card" style="margin-bottom: 1.25rem;">
          <h4 style="color: var(--cyan); font-size: 1.05rem; margin-bottom: 0.6rem;">✍️ المرحلة 02: الكرييتف، المحتوى الفيرال، والسيو</h4>
          <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-muted); line-height: 1.8;">
            <li><b>تسويق المحتوى والكوبي رايتنج:</b> قاعدة الـ 3 ثوانٍ الأولى (Hook > 35%)، صيغ PAS/AIDA، وجداول النشر.</li>
            <li><b>احتراف إنستغرام والريلز:</b> خوارزمية الريلز، سلاسل الستوري اليومية للبيع، وأتمتة الرسائل (IG DM).</li>
            <li><b>سيو محركات البحث:</b> الكلمات المفتاحية التنافسية، السيو الداخلي والتقني، وسيو نتائج الذكاء الاصطناعي.</li>
            <li><b>يوتيوب وسيو الفيديو:</b> سيكولوجية الصورة المصغرة (CTR > 10%)، هندسة وقت المشاهدة، واستراتيجية Shorts.</li>
          </ul>
        </div>

        <div class="card" style="margin-bottom: 1.25rem;">
          <h4 style="color: var(--emerald); font-size: 1.05rem; margin-bottom: 0.6rem;">📊 المرحلة 03: ميديا بايينج الأداء والسيطرة الإعلانية</h4>
          <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-muted); line-height: 1.8;">
            <li><b>إعلانات Meta للأداء:</b> هيكل TOFU/MOFU/BOFU، حملات Advantage+، تتبع CAPI، وقواعد السكيلينج (+20%).</li>
            <li><b>إعلانات ونمو تيك توك:</b> خوارزمية FYP، إعلانات Spark Ads، وسيو تيك توك للمتاجر الإلكترونية.</li>
            <li><b>إعلانات سناب شات والخليج:</b> استهداف السوق السعودي، عدسات الواقع المعزز (AR)، وإعلانات المجموعات.</li>
            <li><b>لينكد إن B2B ومنصة إكس:</b> استقطاب صناع القرار، المحتوى القيادي، والثريدات التحليلية الفيرال.</li>
          </ul>
        </div>

        <div class="card">
          <h4 style="color: var(--purple); font-size: 1.05rem; margin-bottom: 0.6rem;">🤖 المرحلة 04: الذكاء الاصطناعي، الأتمتة، وعقود الريتينر</h4>
          <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-muted); line-height: 1.8;">
            <li><b>الذكاء الاصطناعي وهندسة الأوامر:</b> إطار RCIC، تصوير منتجات 3D عبر Midjourney، وأتمتة WhatsApp API.</li>
            <li><b>الإيميل ماركتنج وتدفقات الأتمتة:</b> استعادة السلات المتروكة، سلاسل الترحيب، وقمع AARRR.</li>
            <li><b>عقود الريتينر الشهرية ($2,500/شهر):</b> التسعير القائم على القيمة وإغلاق صفقات ملوك المدينة.</li>
            <li><b>التميز المهني والمقابلات:</b> السيرة الذاتية القائمة على الأرقام واجتياز المقابلات بنموذج STAR.</li>
          </ul>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 4: SPRINT -->
      <!-- ========================================== -->
      <div id="view-sprint" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-size: 1.6rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 800;">⚡ معسكر الـ 5 أيام السريع (Sprint)</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">الكبسولة اليومية المكثفة لفريق العمل مع تكليفات العمل الفورية.</p>
        </div>

        <div class="tabs-row">
          <button class="tab-pill active" onclick="loadSprintDay(1, this)">اليوم 01: STP والتموضع</button>
          <button class="tab-pill" onclick="loadSprintDay(2, this)">اليوم 02: الكرييتف وريلز</button>
          <button class="tab-pill" onclick="loadSprintDay(3, this)">اليوم 03: ميديا بايينج ROAS</button>
          <button class="tab-pill" onclick="loadSprintDay(4, this)">اليوم 04: AI وأتمتة الواتساب</button>
          <button class="tab-pill" onclick="loadSprintDay(5, this)">اليوم 05: التشغيل والريتينر</button>
        </div>

        <div id="sprintLessonStage" class="card" style="padding: 1.75rem;"></div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 5: PROMPTS -->
      <!-- ========================================== -->
      <div id="view-prompts" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-size: 1.6rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 800;">🤖 استوديو أوامر الذكاء الاصطناعي (RCIC Engine)</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">ولد أوامرك المعتمدة فورياً وانسخها بضغطة زر واحدة.</p>
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
      <!-- VIEW 6: CASE STUDIES -->
      <!-- ========================================== -->
      <div id="view-cases" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-size: 1.6rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 800;">💼 دراسات حالة عملاء OTB المعتمدين</h2>
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
              <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Pastry & Sweets</span>
              <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700;">100% Sold Out</span>
            </div>
            <h4 class="card-title">🍰 Rice Patisserie</h4>
            <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">
              حملات حجز مسبق قبل المناسبات مع أتمتة رسائل العروض الحصرية، مما أدى لنفاد كامل الكميات قبل 48 ساعة من كل موسم.
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
      <!-- VIEW 7: SOPS -->
      <!-- ========================================== -->
      <div id="view-sops" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-size: 1.6rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 800;">📋 إجراءات CoreLink CRM ومولد البريفات</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">القضاء على التوجيه الفارغ وتوليد بريفات المهام الإلزامية بنقرة زر.</p>
        </div>

        <div class="card" style="border: 2px solid var(--border-gold); margin-bottom: 2rem;">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
            <div>
              <label style="display: block; font-size: 0.85rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 600;">اسم العميل / البراند:</label>
              <input type="text" id="briefClient" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input);" value="Rancho's EG" oninput="buildSopBrief()">
            </div>
            <div>
              <label style="display: block; font-size: 0.85rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 600;">القسم والتكليف:</label>
              <select id="briefType" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input);" onchange="buildSopBrief()">
                <option>كتابة محتوى وكوبي رايتنج إعلاني</option>
                <option>تصميم سوشيال ميديا وموشن جرافيك</option>
                <option>إطلاق وإدارة حملات ميديا بايينج ممولة</option>
                <option>أتمتة رسائل واتساب وخدمة عملاء</option>
              </select>
            </div>
          </div>

          <div style="margin-bottom: 1rem;">
            <label style="display: block; font-size: 0.85rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 600;">البريف المولد للإسناد في CoreLink CRM:</label>
            <textarea id="briefResult" class="code-box" style="height: 200px; width: 100%; resize: vertical;" readonly></textarea>
          </div>

          <button class="btn btn-primary" onclick="copyText(document.getElementById('briefResult').value, '👑 تم نسخ البريف للإسناد المباشر في CoreLink CRM!')">📋 نسخ البريف للإسناد الفوري</button>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 8: QUIZ & CERTIFICATE -->
      <!-- ========================================== -->
      <div id="view-quiz" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-size: 1.6rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 800;">📝 تقييم الكفاءة وإصدار شهادة ملوك المدينة</h2>
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
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.5rem;">2. ما هو الهدف الأساسي من أول 3 ثوانٍ في ريلز الإعلانات؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.88rem;"><input type="radio" name="q1" value="1" checked> كسر التمرير (Pattern Interrupt) وجذب انتباه المشاهد (Hook Rate > 35%)</label>
          <label style="display:block; font-size:0.88rem;"><input type="radio" name="q1" value="0"> كتابة أرقام السجل التجاري</label>
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
      <!-- VIEW 9: DOWNLOADS -->
      <!-- ========================================== -->
      <div id="view-downloads" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-size: 1.6rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 800;">📥 مركز الموارد والتحميلات المباشرة</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">تحميل ملفات الصوت، التقارير التنفيذية، وموسوعات الأوامر بصيغ مباشرة.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
          <div class="card">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">MP4 Audio · 34 MB</span>
            <h4 class="card-title" style="margin-top: 0.35rem;">🎙️ بودكاست التدريب الصوتي</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;">حلقة صوتية معمقة من Gemini Studio.</p>
            <a href="track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" download class="btn btn-primary" style="width: 100%; font-size: 0.82rem; padding: 0.45rem;">📥 تحميل الصوت</a>
          </div>

          <div class="card">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Markdown Doc</span>
            <h4 class="card-title" style="margin-top: 0.35rem;">📑 التقرير الاستراتيجي الشامل</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;">وثيقة التوجيه التنفيذي الصادرة من الاستوديو.</p>
            <a href="track_b_4week_masterclass/studio_artifacts/OTB_Executive_Strategic_Briefing.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.82rem; padding: 0.45rem;">📥 تحميل التقرير</a>
          </div>

          <div class="card">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">50+ Prompts</span>
            <h4 class="card-title" style="margin-top: 0.35rem;">📖 موسوعة الأوامر التكتيكية</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;">أوامر الذكاء الاصطناعي المعتمدة لأدوار OTB.</p>
            <a href="track_a_fast_track_sprint/cheatsheets/OTB_Prompt_Engineering_Bible.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.82rem; padding: 0.45rem;">📥 تحميل الموسوعة</a>
          </div>

          <div class="card">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Checklist</span>
            <h4 class="card-title" style="margin-top: 0.35rem;">✈️ فحص الميديا بايينج</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;">قائمة فحص الحملات قبل الإطلاق وقواعد السكيلينج.</p>
            <a href="track_a_fast_track_sprint/cheatsheets/OTB_Media_Buying_Checklist.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.82rem; padding: 0.45rem;">📥 تحميل الفحص</a>
          </div>
        </div>
      </div>

    </main>
  </div>

  <script src="shared_ui.js"></script>
  <script>
    const coursesData = {courses_json};

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
                <h3 style="font-size: 1.15rem; color: var(--text-pure); margin-top: 0.2rem;">${{c.icon}} ${{c.title}}</h3>
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

    function filterCoursesByPhase(phaseNum) {{
      renderCoursesAccordion(coursesData.filter(c => c.phase === phaseNum));
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
        title: "اليوم الخامس: الانضباط التشغيلي وعقود الريتينر الشهرية",
        audience: "الإدارة ومدراء الحسابات",
        concepts: "• <b>منع الهدر التشغيلي:</b> لا مهمة بدون بريف إلزامي، وقفل التبعيات (Sequential Locking).<br>• <b>اتفاقية مستوى الخدمة (SLA):</b> مراجعة خلال 24 ساعة والتصعيد بعد 48 ساعة.<br>• <b>باقة Dominance Retainer ($2,500/شهر):</b> هوية كاملة + 24 محتوى + ميديا بايينج + أتمتة.",
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
        <h3 style="font-size: 1.3rem; color: var(--text-pure); margin-bottom: 1.25rem;">${{d.title}}</h3>

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

    // SOPS BRIEF BUILDER
    function buildSopBrief() {{
      const client = document.getElementById("briefClient").value || "العميل";
      const type = document.getElementById("briefType").value;
      const date = new Date().toLocaleDateString('ar-EG');

      const brief = "### 👑 OTB OFFICIAL TASK BRIEF\\n" +
        "==================================================\\n" +
        "* العميل / المشروع: " + client + "\\n" +
        "* القسم والتكليف: " + type + "\\n" +
        "* تاريخ الإسناد: " + date + "\\n" +
        "* نظام التتبع: CoreLink CRM (Live System)\\n" +
        "==================================================\\n" +
        "🎯 الهدف التسويقي: تحقيق أعلى عائد مالي (ROAS) لـ " + client + "\\n" +
        "💡 الزاوية الإعلانية: التموضع الملكي وإبراز القيمة التنافسية الحصرية.\\n" +
        "⚠️ المحددات: النبرة واثقة، ممنوع العبارات المستهلكة، والتسليم عبر Cloudflare R2.\\n" +
        "📦 مهلة المراجعة (SLA): 24 ساعة من تاريخ الرفع.\\n" +
        "==================================================\\n" +
        "👑 OTB Agency — We Are The City Kings";

      document.getElementById("briefResult").value = brief;
    }}

    // CERTIFICATE GENERATOR
    function generateOfficialCert() {{
      const name = document.getElementById("certName").value || "خريج الأكاديمية";
      const certId = "OTB-" + Math.floor(100000 + Math.random() * 900000);
      const date = new Date().toLocaleDateString('ar-EG', {{ year: 'numeric', month: 'long', day: 'numeric' }});
      const wrap = document.getElementById("certContainer");

      wrap.style.display = "block";
      wrap.innerHTML = `
        <div style="background: #040507; border: 4px solid var(--gold); border-radius: 20px; padding: 3rem 2rem; text-align: center; margin-top: 2rem; box-shadow: 0 0 60px rgba(212, 168, 83, 0.3);">
          <div style="font-size: 3rem; margin-bottom: 0.5rem;">👑</div>
          <div style="font-size: 0.85rem; letter-spacing: 3px; color: var(--gold); text-transform: uppercase; font-family: var(--font-royal); font-weight: 700;">OTB Marketing Studio · City Kings</div>
          <div style="font-family: var(--font-royal); font-size: 2rem; color: var(--text-pure); margin: 0.85rem 0; font-weight: 900; letter-spacing: 1px;">CERTIFICATE OF GROWTH MASTERY</div>
          <p style="color: var(--text-dim); font-size: 1rem;">تشهد أكاديمية وكالة OTB للتسويق وهندسة النمو بأن</p>
          <h2 style="font-size: 2.2rem; color: var(--gold); margin: 0.85rem 0; font-weight: 900;">${{name}}</h2>
          <p style="color: var(--text-main); max-width: 580px; margin: 0 auto 2rem auto; font-size: 0.95rem; line-height: 1.8;">
            قد أتم بنجاح متطلبات أكاديمية <b>النمو والتسويق الرقمي والذكاء الاصطناعي (Full-Stack Growth Engineering)</b> وأصبح مؤهلاً لتطبيق استراتيجيات وإعلانات ملوك المدينة.
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
    renderCoursesAccordion(coursesData);
    loadSprintDay(1);
    updateLivePrompt();
    buildSopBrief();
    updateLmsProgress();
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(p_master_lms)

print("Generated master LMS index.html")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
