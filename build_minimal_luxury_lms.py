import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from generate_master_academy import COURSES_DATA
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

# ==============================================================================
# 1. ULTRA-CLEAN LUXURY CSS WITH SMOOTH ANIMATIONS & LUCIDE INTEGRATION
# ==============================================================================
master_css = """
/* ==========================================================================
   OTB TEAM AI HUB — MINIMAL LUXURY & BREATHABLE INTERFACE
   Inspired by Apple, Linear & Stripe Luxury Guidelines
   Colors: Obsidian Noir (#050608), Surface (#0B0E14), Pure Gold (#D4A853 / #C5A059)
   Fonts: Felfel (Arabic Display), KOOkies (English Typography), Readex Pro (Body)
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
  --bg-app: #050608;
  --bg-surface: #090C12;
  --bg-card: rgba(14, 18, 26, 0.6);
  --bg-card-hover: rgba(22, 28, 40, 0.85);
  --bg-input: #040507;
  --bg-code: #030406;

  --border: rgba(255, 255, 255, 0.07);
  --border-gold: rgba(212, 168, 83, 0.25);
  --border-gold-bright: rgba(212, 168, 83, 0.7);

  --gold: #D4A853;
  --gold-metallic: #C5A059;
  --gold-light: #F3E5C8;
  --gold-gradient: linear-gradient(135deg, #F3E5C8 0%, #D4A853 50%, #9B7023 100%);
  --gold-dim: rgba(212, 168, 83, 0.08);
  --gold-glow: 0 0 35px rgba(212, 168, 83, 0.18);

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
  --radius-sm: 12px;
  --radius-md: 20px;
  --radius-lg: 32px;
  --radius-full: 9999px;

  --transition-fast: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-smooth: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-spring: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
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
  font-size: 0.96rem;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* THREE.JS PARTICLES BACKGROUND */
#webglCanvas {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  opacity: 0.45;
}

/* SCROLLBAR */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg-app); }
::-webkit-scrollbar-thumb { background: rgba(212, 168, 83, 0.25); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }

/* ULTRA-SLEEK BLURRED NAVBAR */
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(5, 6, 8, 0.85);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border-bottom: 1px solid var(--border);
  padding: 0.85rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: var(--transition-smooth);
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  text-decoration: none;
}

.brand-badge-img {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  padding: 2px;
  background: var(--gold-gradient);
  box-shadow: 0 0 20px rgba(212, 168, 83, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
}

.brand-badge-img img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

.brand-text h1 {
  font-family: var(--font-felfel);
  font-size: 1.25rem;
  color: var(--text-pure);
  line-height: 1.1;
}

.brand-text span {
  font-family: var(--font-kookies);
  font-size: 0.72rem;
  color: var(--gold);
  font-weight: 700;
  letter-spacing: 1px;
}

/* NAVBAR NAVIGATION LINKS (Pills) */
.nav-pills {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.03);
  padding: 0.3rem 0.4rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border);
}

.nav-pill-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 0.45rem 1.15rem;
  border-radius: var(--radius-full);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-fast);
  display: flex;
  align-items: center;
  gap: 0.4rem;
  text-decoration: none;
}

.nav-pill-btn:hover {
  color: var(--text-pure);
  background: rgba(255, 255, 255, 0.05);
}

.nav-pill-btn.active {
  color: #000;
  background: var(--gold-gradient);
  font-weight: 700;
  box-shadow: 0 0 20px rgba(212, 168, 83, 0.35);
}

/* MAIN CONTAINER (Centered, Breathable, No Clutter) */
.app-container {
  max-width: 1120px;
  margin: 0 auto;
  padding: 3rem 1.5rem 6rem 1.5rem;
  position: relative;
  z-index: 1;
}

/* HERO BANNER (Simple & Inspiring) */
.hero-wrapper {
  text-align: center;
  margin-bottom: 3.5rem;
  animation: fadeIn 0.8s ease-out;
}

.hero-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--gold-dim);
  border: 1px solid var(--border-gold);
  color: var(--gold);
  padding: 0.35rem 1rem;
  border-radius: var(--radius-full);
  font-size: 0.8rem;
  font-weight: 700;
  margin-bottom: 1.25rem;
}

.hero-title {
  font-family: var(--font-felfel);
  font-size: 2.75rem;
  color: var(--text-pure);
  line-height: 1.2;
  margin-bottom: 0.85rem;
  font-weight: 900;
}

.hero-title span {
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  color: var(--text-muted);
  font-size: 1.05rem;
  max-width: 650px;
  margin: 0 auto;
  line-height: 1.8;
}

/* ROLE SELECTOR GRID (Clean, Minimal, Non-Overwhelming) */
.role-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 0.85rem;
  margin-bottom: 2.5rem;
}

.role-tab {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.25rem 1rem;
  text-align: center;
  cursor: pointer;
  transition: var(--transition-spring);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.role-tab:hover {
  border-color: var(--gold);
  background: var(--bg-card-hover);
  transform: translateY(-4px);
  box-shadow: var(--gold-glow);
}

.role-tab.active {
  border-color: var(--gold);
  background: var(--gold-dim);
  box-shadow: var(--gold-glow);
  transform: translateY(-2px);
}

.role-icon-box {
  font-size: 2rem;
  transition: var(--transition-fast);
}

.role-tab:hover .role-icon-box {
  transform: scale(1.15);
}

.role-name {
  font-family: var(--font-felfel);
  font-size: 1rem;
  color: var(--text-pure);
  line-height: 1.2;
}

.role-eng {
  font-family: var(--font-kookies);
  font-size: 0.68rem;
  color: var(--gold);
  font-weight: 700;
}

/* ROLE DISPLAY STAGE (Sleek, Focus-Driven) */
.role-stage {
  background: var(--bg-surface);
  border: 1px solid var(--border-gold);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6), var(--gold-glow);
  animation: slideUp 0.4s ease-out;
}

.role-header-strip {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border);
  padding-bottom: 1.25rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.role-heading {
  font-family: var(--font-felfel);
  font-size: 1.85rem;
  color: var(--text-pure);
}

/* CARDS & CONTAINERS */
.glass-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  transition: var(--transition-smooth);
}

.glass-card:hover {
  border-color: var(--border-gold);
  background: var(--bg-card-hover);
}

/* TOOL BADGES */
.tool-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(56, 189, 248, 0.1);
  color: var(--cyan);
  border: 1px solid rgba(56, 189, 248, 0.3);
  padding: 0.4rem 0.9rem;
  border-radius: var(--radius-full);
  font-size: 0.82rem;
  font-weight: 600;
  transition: var(--transition-fast);
}

.tool-pill:hover {
  background: rgba(56, 189, 248, 0.2);
  transform: translateY(-2px);
}

/* CODE / PROMPT BOX (Strict LTR) */
.code-box {
  background: var(--bg-code);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 1.25rem;
  font-family: var(--font-mono);
  font-size: 0.88rem;
  color: #38BDF8;
  direction: ltr !important;
  text-align: left;
  white-space: pre-wrap;
  margin: 1rem 0;
  line-height: 1.7;
}

/* BUTTONS */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.65rem 1.45rem;
  border-radius: var(--radius-full);
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
  box-shadow: 0 4px 20px rgba(212, 168, 83, 0.3);
}

.btn-primary:hover {
  filter: brightness(1.1);
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(212, 168, 83, 0.45);
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

/* FOOLPROOF RTL PHONE NUMBER */
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
  bottom: 2.5rem;
  left: 50%;
  transform: translateX(-50%) translateY(100px);
  background: #090C12;
  border: 1px solid var(--gold);
  color: var(--gold-light);
  padding: 0.85rem 1.75rem;
  border-radius: var(--radius-full);
  font-size: 0.9rem;
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

/* ANIMATIONS */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* RESPONSIVE */
@media (max-width: 768px) {
  .navbar { flex-direction: column; gap: 0.85rem; padding: 1rem; }
  .nav-pills { flex-wrap: wrap; justify-content: center; }
  .hero-title { font-size: 2rem; }
  .role-stage { padding: 1.5rem 1rem; }
}
"""

with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(master_css)

print("Generated Minimal Luxury style.css")

# ==============================================================================
# 2. MASTER HTML TEMPLATE WITH CLEAN MINIMAL UX (index.html)
# ==============================================================================
p_master_lms = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Team AI Hub — منصة تمكين الذكاء الاصطناعي لملوك المدينة</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=JetBrains+Mono:wght@500;600;700&family=Readex+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>

  <!-- WEBGL BACKGROUND CANVAS -->
  <canvas id="webglCanvas"></canvas>

  <!-- MINIMAL LUXURY NAVBAR -->
  <header class="navbar">
    <a href="#" class="nav-brand" onclick="switchMainTab('roles')">
      <div class="brand-badge-img">
        <img src="assets/images/otb_official_logo.jpg" alt="OTB Logo">
      </div>
      <div class="brand-text">
        <h1>OTB TEAM AI HUB <span>👑</span></h1>
        <span>WE ARE OTB · THE CITY KINGS</span>
      </div>
    </a>

    <!-- TOP NAVIGATION PILLS -->
    <nav class="nav-pills">
      <button class="nav-pill-btn active" id="tabBtn-roles" onclick="switchMainTab('roles')">🎯 أدوار الفريق</button>
      <button class="nav-pill-btn" id="tabBtn-courses" onclick="switchMainTab('courses')">📚 المناهج (19)</button>
      <button class="nav-pill-btn" id="tabBtn-prompts" onclick="switchMainTab('prompts')">🤖 استوديو الأوامر</button>
      <button class="nav-pill-btn" id="tabBtn-cases" onclick="switchMainTab('cases')">💼 عملاء OTB</button>
      <button class="nav-pill-btn" id="tabBtn-quiz" onclick="switchMainTab('quiz')">🏆 الشهادة</button>
      <button class="nav-pill-btn" id="tabBtn-downloads" onclick="switchMainTab('downloads')">📥 التحميلات</button>
    </nav>

    <div>
      <a href="tel:+201008080295" class="phone-wrapper" style="font-size: 0.85rem;">
        <span class="phone-code">+20</span>
        <span class="phone-num">100 808 0295</span>
      </a>
    </div>
  </header>

  <!-- APP CONTAINER -->
  <main class="app-container">

    <!-- ========================================== -->
    <!-- SECTION 1: ROLE AI SUPERPOWERS (DEFAULT) -->
    <!-- ========================================== -->
    <section id="section-roles" class="hub-section">
      
      <!-- HERO -->
      <div class="hero-wrapper">
        <div class="hero-pill">✨ OTB AI SUPERPOWER ENGINE · 2026</div>
        <h2 class="hero-title">اختر تخصصك.. واكتشف قوة الـ <span>AI الخارقة 🚀</span></h2>
        <p class="hero-subtitle">
          صُممت هذه المنصة خصيصاً لكل فرد في فريق عمل OTB Agency لتقضي على الروتين، تضاعف سرعتك 5 أضعاف، وتمنحك أوامر جاهزة لخدمة عملاء الوكالة بأعلى جودة.
        </p>
      </div>

      <!-- ROLE SELECTOR CARDS GRID (9 ROLES) -->
      <div class="role-grid" id="rolesGrid"></div>

      <!-- SELECTED ROLE STAGE -->
      <div id="roleDetailsStage" class="role-stage"></div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 2: 19 COURSES -->
    <!-- ========================================== -->
    <section id="section-courses" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <h2 class="hero-title">📚 مناهج الـ 19 تخصصاً المعتمدة</h2>
        <p class="hero-subtitle">موسوعة تدريبية مكثفة تغطي كافة جوانب التسويق الرقمي وإعلانات الأداء وأوامر الذكاء الاصطناعي.</p>
      </div>

      <div class="tabs-row" style="justify-content: center; margin-bottom: 2rem;">
        <button class="tab-pill active" onclick="filterCourses('all', this)">الكل (19)</button>
        <button class="tab-pill" onclick="filterCourses('strategy', this)">الاستراتيجية والهوية (4)</button>
        <button class="tab-pill" onclick="filterCourses('creative', this)">المحتوى والسيو (4)</button>
        <button class="tab-pill" onclick="filterCourses('media', this)">الميديا بايينج (5)</button>
        <button class="tab-pill" onclick="filterCourses('ai', this)">الذكاء الاصطناعي (4)</button>
        <button class="tab-pill" onclick="filterCourses('career', this)">عقود الوكالة (2)</button>
      </div>

      <div id="coursesList"></div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 3: PROMPTS STUDIO -->
    <!-- ========================================== -->
    <section id="section-prompts" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <h2 class="hero-title">🤖 استوديو أوامر الذكاء الاصطناعي</h2>
        <p class="hero-subtitle">ولد أوامر RCIC احترافية فورياً لأي براند أو حملة بضغطة زر واحدة.</p>
      </div>

      <div class="glass-card" style="border: 2px solid var(--border-gold); padding: 2.5rem; max-width: 850px; margin: 0 auto;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 1.5rem;">
          <div>
            <label style="display: block; font-size: 0.88rem; color: var(--text-pure); margin-bottom: 0.4rem; font-weight: 700;">نوع التكليف المطلوب:</label>
            <select id="promptTask" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input); border-radius: var(--radius-sm);" onchange="updateLivePrompt()">
              <option value="copy">كتابة إعلانات تحويلية (PAS Framework)</option>
              <option value="reels">اسكريبت ريلز 15 ثانية (Viral Hook)</option>
              <option value="media">تشخيص حساب إعلاني وسكيلينج (Media Buying)</option>
              <option value="design">لقطات برودكت شوت 3D لـ Midjourney</option>
              <option value="retainer">مقترح عقد ريتينر شهري ($2,500/mo)</option>
            </select>
          </div>
          <div>
            <label style="display: block; font-size: 0.88rem; color: var(--text-pure); margin-bottom: 0.4rem; font-weight: 700;">اسم البراند والقطاع:</label>
            <input type="text" id="promptBrand" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input); border-radius: var(--radius-sm);" value="MIX Coffee (Specialty Coffee)" oninput="updateLivePrompt()">
          </div>
        </div>

        <div style="margin-bottom: 1.5rem;">
          <label style="display: block; font-size: 0.88rem; color: var(--text-pure); margin-bottom: 0.4rem; font-weight: 700;">الأمر المولد فورياً:</label>
          <div id="livePromptCode" class="code-box" style="max-height: 240px; overflow-y: auto;"></div>
        </div>

        <button class="btn btn-primary" style="width: 100%; padding: 0.85rem;" onclick="copyText(document.getElementById('livePromptCode').innerText)">📋 نسخ الأمر المخصص للحافظة</button>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 4: CASE STUDIES -->
    <!-- ========================================== -->
    <section id="section-cases" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <h2 class="hero-title">💼 نتائج وأرقام عملاء OTB المعتمدين</h2>
        <p class="hero-subtitle">استراتيجيات موثقة وأرقام حقيقية أثبتت تموضع ملوك المدينة في السوق.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem;">
        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Specialty Coffee</span>
            <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700; background: rgba(16, 185, 129, 0.1); padding: 0.2rem 0.6rem; border-radius: var(--radius-full);">تفاعل +180%</span>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin-bottom: 0.4rem;">☕ MIX Coffee</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">إعادة التموضع كوجهة أولى لرواد الأعمال، هوية داكنة راقية، وفيديوهات ASMR لتحضير القهوة، مما ضاعف مبيعات الفروع.</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Gourmet Burgers</span>
            <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700; background: rgba(16, 185, 129, 0.1); padding: 0.2rem 0.6rem; border-radius: var(--radius-full);">Retention 36.8%</span>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin-bottom: 0.4rem;">🍔 Rancho's EG</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">الخروج من فخ الخصومات، تموضع البرجر الملحمي، وإعلانات ريلز PAS حققت 450 ألف مشاهدة وزيادة المبيعات بنسبة 65%.</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Luxury Jewelry</span>
            <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700; background: rgba(16, 185, 129, 0.1); padding: 0.2rem 0.6rem; border-radius: var(--radius-full);">ROAS 7.5x+</span>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin-bottom: 0.4rem;">💍 Dr. Zaghloul Jewelry</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">بناء الثقة وسرد قصص التصاميم الحصرية بجودة سينمائية وهيكل حملات TOFU/MOFU/BOFU محققاً عائداً إعلانيا تجاوز 7.5x.</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Industrial & B2B</span>
            <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700; background: rgba(16, 185, 129, 0.1); padding: 0.2rem 0.6rem; border-radius: var(--radius-full);">10M ➔ 30M EGP</span>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin-bottom: 0.4rem;">🏭 Franks EG</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">القفز من المركز 25 إلى المركز الثاني في السوق، ومضاعفة المبيعات الرقمية من 10 إلى 30 مليون جنيه عبر حملات تحويلية استراتيجية.</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">E-Commerce</span>
            <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700; background: rgba(16, 185, 129, 0.1); padding: 0.2rem 0.6rem; border-radius: var(--radius-full);">CPA -32%</span>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin-bottom: 0.4rem;">📦 Sakr Store</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">إعادة هيكلة إعلانات Advantage+ وتتبع CAPI مع عروض الباقات، مما خفض تكلفة الشراء بنسبة 32% ورفع متوسط السلة بنسبة 50%.</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Clinics & Labs</span>
            <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700; background: rgba(16, 185, 129, 0.1); padding: 0.2rem 0.6rem; border-radius: var(--radius-full);">800+ Leads / mo</span>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin-bottom: 0.4rem;">🧪 Elag Labs</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">إعلانات تحويلية سريعة مع مسار واتساب مؤتمت لاستقبال وتأهيل حجوزات التحاليل والزيارات المنزلية بنجاح.</p>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 5: QUIZ & CERTIFICATE -->
    <!-- ========================================== -->
    <section id="section-quiz" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <h2 class="hero-title">🏆 تقييم الكفاءة وإصدار شهادة ملوك المدينة</h2>
        <p class="hero-subtitle">أدخل اسمك وأجب عن الأسئلة الخمسة لإصدار شهادة الاعتماد الملكية الرسمية المعتمدة.</p>
      </div>

      <div class="glass-card" style="max-width: 750px; margin: 0 auto 2rem auto;">
        <label style="display: block; font-size: 0.9rem; color: var(--text-pure); margin-bottom: 0.5rem; font-weight: 700;">الاسم الرسمي المطبوع على الشهادة:</label>
        <input type="text" id="certName" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input); font-size: 1.05rem; border-radius: var(--radius-sm);" value="أحمد عصام رمضان">
      </div>

      <div style="max-width: 750px; margin: 0 auto;">
        <div class="glass-card" style="margin-bottom: 1rem;">
          <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.6rem;">1. ما هو التموضع والنمط النفسي المعتمد لوكالة OTB؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q0" value="0"> المنافسة على أقل سعر</label>
          <label style="display:block; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q0" value="1" checked> The Ruler & The Creator (ملوك المدينة: الهيبة والجرأة والتركيز على العائد)</label>
        </div>

        <div class="glass-card" style="margin-bottom: 1rem;">
          <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.6rem;">2. كيف يساعد الذكاء الاصطناعي صانع المحتوى بشكل سليم؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q1" value="1" checked> كـ شريك عصف ذهني وسرعة صياغة بدقة المعطيات (Context) مع مراجعة بشرية</label>
          <label style="display:block; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q1" value="0"> نسخ ولصق الردود بدون قراءة</label>
        </div>

        <div class="glass-card" style="margin-bottom: 1rem;">
          <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.6rem;">3. إذا كان هامش الربح 25%، فما هو الـ Break-Even ROAS؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q2" value="1" checked> 4.0x (حيث 1 / 0.25 = 4)</label>
          <label style="display:block; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q2" value="0"> 1.5x</label>
        </div>

        <div class="glass-card" style="margin-bottom: 1rem;">
          <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.6rem;">4. ما هي النسبة الآمنة لزيادة ميزانية الحملات الرابحة (Scaling)؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q3" value="1" checked> زيادة 20% كل 48-72 ساعة لحماية استقرار الحملة</label>
          <label style="display:block; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q3" value="0"> مضاعفة الميزانية 200% كل ساعة</label>
        </div>

        <div class="glass-card" style="margin-bottom: 2rem;">
          <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.6rem;">5. ما هو السعر القياسي لباقة الـ Dominance Retainer لـ OTB؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q4" value="1" checked> $2,500 / شهر (هوية + 24 محتوى + ميديا بايينج + أتمتة)</label>
          <label style="display:block; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q4" value="0"> $300 / شهر</label>
        </div>

        <div style="text-align: center;">
          <button class="btn btn-primary" style="padding: 0.9rem 3.5rem; font-size: 1rem;" onclick="generateOfficialCert()">👑 إصدار شهادة الاعتماد الملكية</button>
        </div>

        <div id="certContainer" style="display: none;"></div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 6: DOWNLOADS -->
    <!-- ========================================== -->
    <section id="section-downloads" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <h2 class="hero-title">📥 مركز المستندات والأوامر المباشرة</h2>
        <p class="hero-subtitle">تحميل التقارير الاستراتيجية، وموسوعات الأوامر، وقوائم الفحص بصيغ مباشرة.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">50+ Prompts</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin: 0.4rem 0;">📖 موسوعة الأوامر التكتيكية</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1.25rem;">أوامر الذكاء الاصطناعي المعتمدة لأدوار OTB.</p>
          <a href="track_a_fast_track_sprint/cheatsheets/OTB_Prompt_Engineering_Bible.md" download class="btn btn-primary" style="width: 100%; font-size: 0.85rem;">📥 تحميل الموسوعة</a>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Checklist</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin: 0.4rem 0;">✈️ فحص الميديا بايينج</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1.25rem;">قائمة فحص الحملات قبل الإطلاق وقواعد السكيلينج.</p>
          <a href="track_a_fast_track_sprint/cheatsheets/OTB_Media_Buying_Checklist.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.85rem;">📥 تحميل الفحص</a>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Markdown Doc</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin: 0.4rem 0;">📑 التقرير الاستراتيجي الشامل</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1.25rem;">وثيقة التوجيه التنفيذي لنمو الوكالة.</p>
          <a href="track_b_4week_masterclass/studio_artifacts/OTB_Executive_Strategic_Briefing.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.85rem;">📥 تحميل التقرير</a>
        </div>
      </div>
    </section>

  </main>

  <script src="shared_ui.js"></script>
  <script>
    const coursesData = {courses_json};

    // 9 ROLES SUPERPOWER MATRIX
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

    function switchMainTab(tabName) {{
      document.querySelectorAll(".hub-section").forEach(s => s.style.display = "none");
      const target = document.getElementById("section-" + tabName);
      if (target) target.style.display = "block";

      document.querySelectorAll(".nav-pill-btn").forEach(b => b.classList.remove("active"));
      const btn = document.getElementById("tabBtn-" + tabName);
      if (btn) btn.classList.add("active");

      window.scrollTo({{ top: 0, behavior: "smooth" }});
    }}

    function renderRolesGrid() {{
      const grid = document.getElementById("rolesGrid");
      let html = "";
      rolesSuperpowers.forEach((r, idx) => {{
        html += `
          <div class="role-tab ${{idx === 0 ? 'active' : ''}}" id="roleTab_${{r.id}}" onclick="selectRole('${{r.id}}')">
            <div class="role-icon-box">${{r.icon}}</div>
            <div class="role-name">${{r.name}}</div>
            <div class="role-eng">${{r.eng}}</div>
          </div>
        `;
      }});
      grid.innerHTML = html;
      selectRole(rolesSuperpowers[0].id);
    }}

    function selectRole(roleId) {{
      document.querySelectorAll(".role-tab").forEach(t => t.classList.remove("active"));
      const activeTab = document.getElementById("roleTab_" + roleId);
      if (activeTab) activeTab.classList.add("active");

      const r = rolesSuperpowers.find(item => item.id === roleId);
      if (!r) return;

      let toolsHtml = "";
      r.tools.forEach(t => {{
        toolsHtml += `<span class="tool-pill">${{t}}</span>`;
      }});

      const stage = document.getElementById("roleDetailsStage");
      stage.innerHTML = `
        <div class="role-header-strip">
          <div>
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">دليل التمكين والتفوق اليومي لـ OTB</span>
            <h2 class="role-heading">${{r.icon}} ${{r.name}} <span style="font-family: var(--font-kookies); font-size: 1.1rem; color: var(--gold-light);">(${{r.eng}})</span></h2>
          </div>
          <button class="btn btn-primary" onclick="copyText(document.getElementById('rolePromptBox').innerText)">📋 نسخ الأمر المعتمد</button>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
          <div class="glass-card" style="background: rgba(225, 29, 72, 0.06); border-color: rgba(225, 29, 72, 0.25);">
            <h4 style="color: var(--crimson); font-size: 0.95rem; margin-bottom: 0.35rem; font-weight: 700;">🛑 أين يضيع وقتك يومياً؟:</h4>
            <p style="font-size: 0.88rem; color: var(--text-main);">${{r.challenge}}</p>
          </div>

          <div class="glass-card" style="background: rgba(16, 185, 129, 0.06); border-color: rgba(16, 185, 129, 0.25);">
            <h4 style="color: var(--emerald); font-size: 0.95rem; margin-bottom: 0.35rem; font-weight: 700;">🚀 كيف يضاعف الـ AI إنتاجيتك 5x؟:</h4>
            <p style="font-size: 0.88rem; color: var(--text-main);">${{r.impact}}</p>
          </div>
        </div>

        <div style="margin-bottom: 1.5rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.6rem; font-weight: 700;">🛠️ ترسانة الأدوات الموصى بها لتخصصك:</h4>
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">${{toolsHtml}}</div>
        </div>

        <div class="glass-card" style="background: var(--bg-code); margin-bottom: 1.5rem;">
          <h4 style="font-size: 0.95rem; color: var(--gold); margin-bottom: 0.6rem; font-weight: 700;">🔄 التحول الجذري في طريقة الشغل:</h4>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; font-size: 0.88rem;">
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

        <div class="glass-card" style="background: var(--gold-dim); border-color: var(--border-gold);">
          <h4 style="color: var(--gold); font-size: 0.95rem; margin-bottom: 0.35rem; font-weight: 700;">💡 النصيحة الذهبية لملوك المدينة:</h4>
          <p style="font-size: 0.9rem; color: var(--text-main); line-height: 1.8;">${{r.goldenRule}}</p>
        </div>
      `;
    }}

    function renderCoursesList(list) {{
      const container = document.getElementById("coursesList");
      let html = "";
      list.forEach(c => {{
        const isDone = localStorage.getItem("otb_done_" + c.id) === "true";
        let unitsHtml = "";
        c.units.forEach((u, i) => {{
          unitsHtml += `<li style="margin-bottom: 0.35rem;"><b>الوحدة ${{i + 1}}:</b> ${{u}}</li>`;
        }});

        html += `
          <div class="glass-card" style="margin-bottom: 1rem; padding: 1.25rem 1.5rem;">
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
      renderCoursesList(coursesData);
    }}

    function filterCourses(cat, btn) {{
      document.querySelectorAll("#section-courses .tab-pill").forEach(p => p.classList.remove("active"));
      btn.classList.add("active");

      if (cat === "all") renderCoursesList(coursesData);
      else renderCoursesList(coursesData.filter(c => c.cat === cat));
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
        <div style="background: #030406; border: 3px solid var(--gold); border-radius: 24px; padding: 3.5rem 2.5rem; text-align: center; margin-top: 2rem; box-shadow: 0 0 60px rgba(212, 168, 83, 0.35);">
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

    // INITIALIZATION
    renderRolesGrid();
    renderCoursesList(coursesData);
    updateLivePrompt();
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(p_master_lms)

print("Generated Breathable Luxury index.html")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
