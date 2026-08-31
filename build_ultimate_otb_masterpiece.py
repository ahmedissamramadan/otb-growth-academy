import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from generate_master_academy import COURSES_DATA
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

# ==============================================================================
# 1. LUXURY OTB BRAND SYSTEM CSS WITH BESPOKE FONTS & WEBDESIGN STANDARDS
# ==============================================================================
master_css = """
/* ==========================================================================
   OTB GROWTH ACADEMY — ULTIMATE ENTERPRISE KNOWLEDGE MASTERPIECE
   Official Luxury Brand System: Obsidian Noir (#050608), Charcoal (#0B0E17), Imperial Gold (#C5A059 / #DFBA73)
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

@font-face {
  font-family: 'Guesswhat';
  src: url('assets/fonts/Guesswhat-Exceptional.otf') format('opentype');
  font-weight: 700;
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
  --gold-ivory: #FDFBF7;
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
  opacity: 0.55;
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
  width: 48px;
  height: 48px;
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
  width: 330px;
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

/* AUDIO STRIP */
.audio-player-box {
  background: var(--bg-input);
  border: 1px solid var(--border-gold);
  border-radius: var(--radius-sm);
  padding: 1rem 1.25rem;
  margin-bottom: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  box-shadow: var(--gold-glow);
}

.audio-player-box audio {
  height: 32px;
  direction: ltr !important;
  max-width: 340px;
  outline: none;
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

/* GALLERY GRID */
.showcase-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
  margin: 1.5rem 0;
}

.showcase-item {
  position: relative;
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid var(--border);
  height: 220px;
  background: #000;
  cursor: pointer;
  transition: var(--transition-smooth);
}

.showcase-item:hover {
  border-color: var(--gold);
  transform: scale(1.02);
  box-shadow: var(--gold-glow);
}

.showcase-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: var(--transition-smooth);
}

.showcase-item:hover img {
  transform: scale(1.08);
}

.showcase-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, transparent 60%);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 1rem 1.25rem;
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

print("Generated Ultimate style.css with bespoke fonts and WebGL")

# ==============================================================================
# 2. ADVANCED THREE.JS WEBGL PARTICLE SYSTEM (shared_ui.js)
# ==============================================================================
master_js = """
// OTB Agency WebGL 3D Particle Starfield & UI Engine
function initWebGLParticles() {
  const canvas = document.getElementById("webglCanvas");
  if (!canvas || typeof THREE === "undefined") return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 80;

  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Golden Geometric Dust Particles
  const particleCount = 450;
  const geometry = new THREE.BufferGeometry();
  const positions = new Float32Array(particleCount * 3);
  const colors = new Float32Array(particleCount * 3);

  const goldColor = new THREE.Color(0xD4A853);
  const lightColor = new THREE.Color(0xF3E5C8);

  for (let i = 0; i < particleCount; i++) {
    positions[i * 3] = (Math.random() - 0.5) * 200;
    positions[i * 3 + 1] = (Math.random() - 0.5) * 200;
    positions[i * 3 + 2] = (Math.random() - 0.5) * 120;

    const mixedColor = goldColor.clone().lerp(lightColor, Math.random());
    colors[i * 3] = mixedColor.r;
    colors[i * 3 + 1] = mixedColor.g;
    colors[i * 3 + 2] = mixedColor.b;
  }

  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

  const material = new THREE.PointsMaterial({
    size: 2.2,
    vertexColors: true,
    transparent: true,
    opacity: 0.65,
    blending: THREE.AdditiveBlending
  });

  const particleSystem = new THREE.Points(geometry, material);
  scene.add(particleSystem);

  let mouseX = 0, mouseY = 0;
  window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX - window.innerWidth / 2) * 0.03;
    mouseY = (e.clientY - window.innerHeight / 2) * 0.03;
  });

  function animate() {
    requestAnimationFrame(animate);
    particleSystem.rotation.y += 0.0008;
    particleSystem.rotation.x += 0.0004;

    camera.position.x += (mouseX - camera.position.x) * 0.03;
    camera.position.y += (-mouseY - camera.position.y) * 0.03;
    camera.lookAt(scene.position);

    renderer.render(scene, camera);
  }
  animate();

  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
}

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

document.addEventListener("DOMContentLoaded", () => {
  initWebGLParticles();
});
"""

with open(os.path.join(BASE_DIR, "shared_ui.js"), "w", encoding="utf-8") as f:
    f.write(master_js)

print("Generated shared_ui.js with WebGL particle engine")

# ==============================================================================
# 3. MASTER HTML FILE (index.html)
# ==============================================================================
p_master_lms = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Growth Academy — التحفة المعرفية لملوك المدينة</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=JetBrains+Mono:wght@500;600;700&family=Readex+Pro:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;0,900;1,700&display=swap" rel="stylesheet">
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
        <h1>OTB GROWTH ACADEMY <span>👑</span></h1>
        <p>WE ARE OTB, THE CITY KINGS · BOLD STRATEGIES · REAL RESULTS</p>
      </div>
    </div>

    <div class="search-input-wrap">
      <input type="text" id="globalSearch" class="search-input" placeholder="🔍 بحث في المناهج والأوامر والـ SOPs..." oninput="handleGlobalSearch()">
    </div>

    <div class="header-actions">
      <span class="internal-badge">🔒 بوابة داخلية لفريق OTB</span>
      <a href="https://www.facebook.com/otbagency5" target="_blank" class="btn btn-secondary" style="font-size: 0.78rem; padding: 0.35rem 0.85rem;">
        🌐 مجتمع فيسبوك (+33K)
      </a>
      <a href="https://notebooklm.google.com/notebook/76ef5be2-d7d2-4a33-a88d-f88fc0fe1148" target="_blank" class="btn btn-secondary" style="font-size: 0.78rem; padding: 0.35rem 0.85rem;">
        ✨ استوديو Gemini
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
            <span>نظرة عامة وهوية الوكالة</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--gold);">DNA</span>
        </div>
        <div class="nav-item" onclick="switchView('gallery', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">🎨</span>
            <span>معرض الأعمال البصرية الفاخرة</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--gold);">Visuals</span>
        </div>
        <div class="nav-item" onclick="switchView('roles', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">🏛️</span>
            <span>الهيكل والـ 16 دوراً وظيفياً</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--gold);">16 Roles</span>
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
        <div class="nav-item" onclick="switchView('discovery', this)">
          <div style="display: flex; align-items: center;">
            <span class="nav-item-icon">🎯</span>
            <span>نظام بريف الاكتشاف (9 مراحل)</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--purple);">Manus</span>
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
        <div style="display: flex; align-items: center; gap: 0.75rem;">
          <span style="font-size: 1.4rem;">🎙️</span>
          <div>
            <div style="font-family: var(--font-felfel); font-size: 1rem; color: var(--text-pure);">التدريب الصوتي الاستراتيجي المعتمد</div>
            <div style="font-size: 0.75rem; color: var(--gold);">Gemini Studio Growth Engineering Deep Dive Podcast (34 MB)</div>
          </div>
        </div>
        <audio controls>
          <source src="track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" type="audio/mp4">
        </audio>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 1: OVERVIEW & BRAND DNA -->
      <!-- ========================================== -->
      <div id="view-overview" class="lms-view">
        <div style="position: relative; border-radius: var(--radius-lg); overflow: hidden; margin-bottom: 2.5rem; border: 1px solid var(--border-gold);">
          <img src="assets/images/hero.jpg" alt="OTB Hero" style="width: 100%; height: 260px; object-fit: cover; filter: brightness(0.65);">
          <div style="position: absolute; inset: 0; background: linear-gradient(to top, #050609 0%, rgba(5, 6, 9, 0.4) 100%); display: flex; flex-direction: column; justify-content: flex-end; padding: 2rem 2.5rem;">
            <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700; letter-spacing: 2px;">OFFICIAL AGENCY VISION · 2026</span>
            <h2 style="font-family: var(--font-felfel); font-size: 2.4rem; color: var(--text-pure); font-weight: 900; margin-top: 0.2rem; line-height: 1.2;">WE ARE OTB, THE CITY KINGS 👑</h2>
            <p style="color: var(--gold-light); font-size: 1rem; font-weight: 600;">استراتيجيات جريئة.. نتائج حقيقية | Bold Strategies · Real Results</p>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2.5rem;">
          <div class="card" style="text-align: center; padding: 1.25rem;">
            <div style="font-family: var(--font-royal); font-size: 2rem; font-weight: 900; color: var(--gold);">7+</div>
            <div style="font-size: 0.82rem; color: var(--text-muted);">سنوات من الخبرة والريادة</div>
          </div>
          <div class="card" style="text-align: center; padding: 1.25rem;">
            <div style="font-family: var(--font-royal); font-size: 2rem; font-weight: 900; color: var(--cyan);">33K+</div>
            <div style="font-size: 0.82rem; color: var(--text-muted);">مجتمع فيسبوك الرسمي</div>
          </div>
          <div class="card" style="text-align: center; padding: 1.25rem;">
            <div style="font-family: var(--font-royal); font-size: 2rem; font-weight: 900; color: var(--emerald);">11+</div>
            <div style="font-size: 0.82rem; color: var(--text-muted);">براندات تجارية كبرى مخدومة</div>
          </div>
          <div class="card" style="text-align: center; padding: 1.25rem;">
            <div style="font-family: var(--font-royal); font-size: 2rem; font-weight: 900; color: var(--purple);">16</div>
            <div style="font-size: 0.82rem; color: var(--text-muted);">دوراً وظيفياً متخصصاً</div>
          </div>
        </div>

        <h3 style="font-family: var(--font-felfel); font-size: 1.35rem; color: var(--text-pure); margin-bottom: 1.25rem;">المراحل المعمارية الـ 4 للمنهج:</h3>
        
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
      <!-- VIEW: VISUAL GALLERY SHOWCASE -->
      <!-- ========================================== -->
      <div id="view-gallery" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">🎨 معرض الأعمال والإنتاج البصري الفاخر</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">نماذج حقيقية من إبداعات مصممي وفريق وكالة OTB لبراندات النخبة.</p>
        </div>

        <div class="showcase-grid">
          <div class="showcase-item" onclick="showToast('👑 كراسة الهوية البصرية الرسمية لـ OTB Agency')">
            <img src="assets/images/otb_official_showcase.jpg" alt="OTB Showcase">
            <div class="showcase-overlay">
              <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">Brand Identity & 3D Art</span>
              <h4 style="font-family: var(--font-felfel); font-size: 1.1rem; color: #fff;">OTB Official Brand Masterpiece</h4>
            </div>
          </div>

          <div class="showcase-item" onclick="showToast('☕ تصاميم وهوية MIX Coffee الفاخرة')">
            <img src="assets/images/portfolio1.jpg" alt="MIX Coffee Portfolio">
            <div class="showcase-overlay">
              <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">Specialty Coffee Brand</span>
              <h4 style="font-family: var(--font-felfel); font-size: 1.1rem; color: #fff;">MIX Coffee Visual Identity</h4>
            </div>
          </div>

          <div class="showcase-item" onclick="showToast('🍔 تصاميم وإعلانات Rancho\'s EG الملحمية')">
            <img src="assets/images/portfolio2.jpg" alt="Rancho's Portfolio">
            <div class="showcase-overlay">
              <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">Gourmet Burger F&B</span>
              <h4 style="font-family: var(--font-felfel); font-size: 1.1rem; color: #fff;">Rancho's Epic Campaigns</h4>
            </div>
          </div>

          <div class="showcase-item" onclick="showToast('💎 تصاميم وسرديات مجوهرات دكتور زغلول')">
            <img src="assets/images/arabic_portfolio.jpg" alt="Arabic Portfolio">
            <div class="showcase-overlay">
              <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">Luxury Jewelry & Gold</span>
              <h4 style="font-family: var(--font-felfel); font-size: 1.1rem; color: #fff;">Dr. Zaghloul Luxury Campaigns</h4>
            </div>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW: 16 ROLES (الهيكل التنظيمي) -->
      <!-- ========================================== -->
      <div id="view-roles" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">🏛️ الدليل الرسمي للمسميات والـ 16 دوراً وظيفياً</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">المرجع التنظيمي المعتمد لتنظيم العمل والتشغيل والتقييم داخل OTB Agency.</p>
        </div>

        <div class="tabs-row">
          <button class="tab-pill active" onclick="filterRoles('all', this)">كل الأدوار (16)</button>
          <button class="tab-pill" onclick="filterRoles('exec', this)">القيادة العليا (2)</button>
          <button class="tab-pill" onclick="filterRoles('ops', this)">العمليات والإنتاج (9)</button>
          <button class="tab-pill" onclick="filterRoles('admin', this)">الإدارة المساندة (5)</button>
        </div>

        <div id="rolesListContainer"></div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 2: 19 COURSES -->
      <!-- ========================================== -->
      <div id="view-courses" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">📚 موسوعة المقررات الـ 19 المفصلة</h2>
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
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">🗺️ الخريطة الذهنية والتفكيك الهيكلي</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">شجرة مفاهيمية تقسم المنهج إلى 4 مراحل و 80+ تخصصاً فرعياً مصممة لأقسام الوكالة.</p>
        </div>

        <div class="card" style="margin-bottom: 1.25rem;">
          <h4 style="color: var(--gold); font-family: var(--font-felfel); font-size: 1.15rem; margin-bottom: 0.6rem;">👑 المرحلة 01: الأساسات وبناء الهوية والتشغيل</h4>
          <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-muted); line-height: 1.8;">
            <li><b>مبادئ التسويق الحديث:</b> 4Ps إلى 4Cs، سيكولوجية اتخاذ القرار، رحلة العميل وبناء الـ Persona.</li>
            <li><b>الاستراتيجية والتخطيط:</b> تحليل STP، إطار SOSTAC، ومؤشرات الأداء الذكية (SMART KPIs).</li>
            <li><b>بناء الهوية والعلامة:</b> النمط النفسي The Ruler لـ OTB، كراسة الهوية ونبرة الصوت، وتموضع الهيبة.</li>
            <li><b>الانضباط التشغيلي CoreLink CRM:</b> نماذج البريف الإلزامي، قفل التبعيات، واتفاقيات الـ SLA.</li>
          </ul>
        </div>

        <div class="card" style="margin-bottom: 1.25rem;">
          <h4 style="color: var(--cyan); font-family: var(--font-felfel); font-size: 1.15rem; margin-bottom: 0.6rem;">✍️ المرحلة 02: الكرييتف، المحتوى الفيرال، والسيو</h4>
          <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-muted); line-height: 1.8;">
            <li><b>تسويق المحتوى والكوبي رايتنج:</b> قاعدة الـ 3 ثوانٍ الأولى (Hook > 35%)، صيغ PAS/AIDA، وجداول النشر.</li>
            <li><b>احتراف إنستغرام والريلز:</b> خوارزمية الريلز، سلاسل الستوري اليومية للبيع، وأتمتة الرسائل (IG DM).</li>
            <li><b>سيو محركات البحث:</b> الكلمات المفتاحية التنافسية، السيو الداخلي والتقني، وسيو نتائج الذكاء الاصطناعي.</li>
            <li><b>يوتيوب وسيو الفيديو:</b> سيكولوجية الصورة المصغرة (CTR > 10%)، هندسة وقت المشاهدة، واستراتيجية Shorts.</li>
          </ul>
        </div>

        <div class="card" style="margin-bottom: 1.25rem;">
          <h4 style="color: var(--emerald); font-family: var(--font-felfel); font-size: 1.15rem; margin-bottom: 0.6rem;">📊 المرحلة 03: ميديا بايينج الأداء والسيطرة الإعلانية</h4>
          <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-muted); line-height: 1.8;">
            <li><b>إعلانات Meta للأداء:</b> هيكل TOFU/MOFU/BOFU، حملات Advantage+، تتبع CAPI، وقواعد السكيلينج (+20%).</li>
            <li><b>إعلانات ونمو تيك توك:</b> خوارزمية FYP، إعلانات Spark Ads، وسيو تيك توك للمتاجر الإلكترونية.</li>
            <li><b>إعلانات سناب شات والخليج:</b> استهداف السوق السعودي، عدسات الواقع المعزز (AR)، وإعلانات المجموعات.</li>
            <li><b>لينكد إن B2B ومنصة إكس:</b> استقطاب صناع القرار، المحتوى القيادي، والثريدات التحليلية الفيرال.</li>
          </ul>
        </div>

        <div class="card">
          <h4 style="color: var(--purple); font-family: var(--font-felfel); font-size: 1.15rem; margin-bottom: 0.6rem;">🤖 المرحلة 04: الذكاء الاصطناعي، الأتمتة، وعقود الريتينر</h4>
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
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">⚡ معسكر الـ 5 أيام السريع (Sprint)</h2>
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
      <!-- VIEW 5: PROMPTS STUDIO -->
      <!-- ========================================== -->
      <div id="view-prompts" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">🤖 استوديو أوامر الذكاء الاصطناعي (RCIC Engine)</h2>
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
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">💼 دراسات حالة عملاء OTB المعتمدين</h2>
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
      <!-- VIEW 7: SOPS & CORELINK -->
      <!-- ========================================== -->
      <div id="view-sops" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">📋 إجراءات CoreLink CRM ومولد البريفات</h2>
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
      <!-- VIEW: DISCOVERY (9-STAGE BRIEF SYSTEM) -->
      <!-- ========================================== -->
      <div id="view-discovery" class="lms-view" style="display: none;">
        <div style="margin-bottom: 1.75rem;">
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">🎯 نظام بريف الاكتشاف الاستراتيجي (9 مراحل)</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">نظام استقبال وتأهيل العملاء الاستراتيجيين المعتمد في منظومة Manus للوكالة.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
          <div class="card">
            <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">المرحلة 01</span>
            <h4 class="card-title">🌱 الجذور (Who You Are)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">قصة تأسيس البراند، الرؤية والرسالة، والقيمة الجوهرية غير القابلة للتقليد.</p>
          </div>
          <div class="card">
            <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">المرحلة 02</span>
            <h4 class="card-title">💎 العرض القيمي (The Offer)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">المنتجات الرئيسية، هوامش الربح، وما الذي يجعل العميل يشتري بدون تردد.</p>
          </div>
          <div class="card">
            <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">المرحلة 03</span>
            <h4 class="card-title">👥 الجمهور المستهدف (Audience)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">الشرائح الأعلى ربحية، الآلام العميقة، ونمط الحياة والقدرة الشرائية.</p>
          </div>
          <div class="card">
            <span style="font-size: 0.75rem; color: var(--cyan); font-weight: 700;">المرحلة 04</span>
            <h4 class="card-title">🔍 المشهد التنافسي (Landscape)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">أبرز 3 منافسين، الفجوات السعرية والخدمية في السوق المصري والخليجي.</p>
          </div>
          <div class="card">
            <span style="font-size: 0.75rem; color: var(--cyan); font-weight: 700;">المرحلة 05</span>
            <h4 class="card-title">🎭 النمط ونبرة الصوت (Tone)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">تحديد شخصية البراند (The Ruler / The Creator) ومفردات التواصل.</p>
          </div>
          <div class="card">
            <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700;">المرحلة 06</span>
            <h4 class="card-title">📈 أهداف الـ 90 يوماً (KPIs)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">المستهدفات المالية الملموسة (ROAS، المبيعات الشهرية، عدد العملاء الجدد).</p>
          </div>
          <div class="card">
            <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700;">المرحلة 07</span>
            <h4 class="card-title">⚙️ التشغيل والميزانية (Budget)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">الميزانيات الإعلانية المرصودة، الأدوات الحالية، وفريق خدمة العملاء.</p>
          </div>
          <div class="card">
            <span style="font-size: 0.75rem; color: var(--purple); font-weight: 700;">المرحلة 08</span>
            <h4 class="card-title">⚠️ المخاوف والدروس (Context)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">تجارب الوكالات السابقة الفاشلة، ما يجب تجنبه، والخطوط الحمراء.</p>
          </div>
          <div class="card">
            <span style="font-size: 0.75rem; color: var(--gold); font-weight: 700;">المرحلة 09</span>
            <h4 class="card-title">✍️ المراجعة والاعتماد (Sign-Off)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">إصدار كود البريف المرجعي وتوزيعه الفوري على منظومة CoreLink CRM.</p>
          </div>
        </div>
      </div>

      <!-- ========================================== -->
      <!-- VIEW 8: QUIZ & CERTIFICATE -->
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
          <h2 style="font-family: var(--font-felfel); font-size: 1.8rem; color: var(--text-pure); margin-bottom: 0.35rem;">📥 مركز الموارد والتحميلات المباشرة</h2>
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

    // 16 OFFICIAL ROLES DATA
    const rolesData = [
      {{
        title: "1. Chief Executive Officer (CEO)",
        category: "exec",
        desc: "وضع الرؤية العامة للشركة، تحديد الاتجاهات الاستراتيجية، وضمان النمو والاستدامة والربحية وإدارة العلاقات مع العملاء الاستراتيجيين.",
        kpis: "نمو الإيراد الإجمالي، هامش الربحية (قاعدة 50/50)، وتوسيع محفظة العملاء الكبار."
      }},
      {{
        title: "2. General Manager (GM)",
        category: "exec",
        desc: "إدارة التشغيل اليومي للشركة وضمان تنفيذ الاستراتيجيات بكفاءة عالية، متابعة تقارير رؤساء الأقسام وحل المشكلات التشغيلية.",
        kpis: "نسبة الالتزام بالـ SLA، معدل رضا العملاء، وسلاسة تدفق المشاريع."
      }},
      {{
        title: "3. Head of Account Management",
        category: "ops",
        desc: "الإشراف على مديري الحسابات، اعتماد البريفات والاستراتيجيات الخاصة بالعملاء، والتدخل في الأزمات والمشكلات الكبرى.",
        kpis: "معدل تجديد العقود (Retention Rate > 85%)، وتأمين مستحقات الوكالة في مواعيدها."
      }},
      {{
        title: "4. Account Manager",
        category: "ops",
        desc: "إدارة العلاقة اليومية مع العميل، توثيق البريف بدقة، توزيع المهام على الأقسام عبر CoreLink، ومتابعة الديدلاينز.",
        kpis: "اكتمال تسليمات العميل الشهرية في موعدها، وجودة التواصل ومنع سوء الفهم."
      }},
      {{
        title: "5. Head of Brand & Strategy",
        category: "ops",
        desc: "بناء استراتيجيات البراند، تحديد شخصية ونبرة الصوت (The Ruler & The Creator)، ومراجعة المحتوى والتصميم لضمان التوافق.",
        kpis: "قوة تموضع العميل في السوق، وابتكار زوايا تسويقية غير تقليدية تحقق مبيعات."
      }},
      {{
        title: "6. Head of Content",
        category: "ops",
        desc: "إدارة فريق صناع المحتوى، اعتماد خطط النشر والسكريبتات الإعلانية، وتطوير الأفكار الإبداعية وزوايا الطرح الفيرال.",
        kpis: "معدل تفاعل المحتوى، جودة الهوكس الإعلانية (Hook Rate > 35%)، والالتزام بالجدول."
      }},
      {{
        title: "7. Content Creator",
        category: "ops",
        desc: "إعداد المحتوى الكتابي والسكريبتات الإعلانية والفيديو بصيغ PAS/AIDA والالتزام بنبرة الصوت المعتمدة وتسليم المهام في موعدها.",
        kpis: "جودة النصوص، سرعة التسليم، ومطابقة متطلبات البريف الإلزامي."
      }},
      {{
        title: "8. Head of Graphic Design",
        category: "ops",
        desc: "إدارة المخرجات البصرية، ضمان الالتزام الصارم بدليل الهوية البصرية، وتطوير المهارات الفنية لفريق التصميم.",
        kpis: "تناسق وجودة المخرجات البصرية، تقليص جولات التعديل (Rework Rate < 15%)."
      }},
      {{
        title: "9. Graphic Designer",
        category: "ops",
        desc: "تنفيذ التصميمات طبقاً للبريف الفني المسلم، الالتزام بالهوية والخطوط، وتجهيز الملفات بمقاسات المنصات المختلفة.",
        kpis: "الدقة الفنية، الإبداع البصري، وتسليم الأصول عبر Cloudflare R2 في الموعد."
      }},
      {{
        title: "10. Head of Media Buying",
        category: "ops",
        desc: "وضع الاستراتيجية الإعلانية العامة وتوزيع الميزانيات، مراجعة الحملات وتحليل الـ ROAS، وإدارة الميزانيات بكفاءة.",
        kpis: "تحقيق متوسط ROAS أعلى من نقطة التعادل، وتقليص تكلفة الاستحواذ (CPA)."
      }},
      {{
        title: "11. Media Buyer",
        category: "ops",
        desc: "إطلاق وإدارة الحملات الإعلانية الممولة (Meta, TikTok, Snapchat, Google)، المتابعة اليومية والسكيلينج الآمن (+20%).",
        kpis: "سلامة التتبع (CAPI Match Quality > 8/10)، وثبات الـ ROAS أثناء السكيلينج."
      }},
      {{
        title: "12. Head of Moderation",
        category: "ops",
        desc: "إدارة فريق الموديريشن، اعتماد أسلوب وسياسات الرد وسيناريوهات المحادثة، ومتابعة سرعة وجودة الاستجابة.",
        kpis: "متوسط سرعة الاستجابة (FRT < 5 دقائق)، ونسبة تحويل الاستفسارات إلى مبيعات مؤكدة."
      }},
      {{
        title: "13. Moderator",
        category: "ops",
        desc: "الرد الفوري والاحترافي على الرسائل والتعليقات، توجيه العملاء لمسارات الشراء، وتصعيد الشكاوى الفنية.",
        kpis: "سرعة الرد، الالتزام التام بنبرة البراند، ورفع تقارير نوعية الأسئلة المتكررة."
      }},
      {{
        title: "14. HR Manager",
        category: "admin",
        desc: "استقطاب وتوظيف الكفاءات النوعية، إدارة مسيرات الرواتب والانضباط الوظيفي، وتطبيق برامج التدريب الداخلية.",
        kpis: "معدل استقرار الفريق، سرعة سد الشواغر الوظيفية، وعدالة تقييمات الأداء."
      }},
      {{
        title: "15. Finance Manager",
        category: "admin",
        desc: "إدارة الشؤون المالية والتدفقات النقدية، تدقيق الإيرادات والمصروفات، التحصيل، ومتابعة الالتزامات والأرباح.",
        kpis: "دقة التقارير المالية، انتظام التدفقات النقدية، وتحقيق قاعدة 50/50 للربحية."
      }},
      {{
        title: "16. Sales & PR Manager",
        category: "admin",
        desc: "استقطاب عملاء B2B استراتيجيين كبار، بناء الشراكات المؤسسية، وإغلاق صفقات باقات الـ Dominance Retainer ($2,500/mo).",
        kpis: "حجم الصفقات الجديدة المغلقة، ومعدل تحويل العملاء المحتملين إلى شركاء دائمين."
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

    function renderRolesList(list) {{
      const container = document.getElementById("rolesListContainer");
      let html = "";
      list.forEach(r => {{
        html += `
          <div class="card" style="margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
              <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--gold);">${{r.title}}</h3>
              <span style="font-size: 0.75rem; color: var(--text-dim); text-transform: uppercase;">${{r.category}}</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--text-main); margin-bottom: 0.6rem; line-height: 1.7;">${{r.desc}}</p>
            <div style="font-size: 0.85rem; color: var(--emerald); font-weight: 600;">🎯 مؤشرات الأداء (KPIs): ${{r.kpis}}</div>
          </div>
        `;
      }});
      container.innerHTML = html;
    }}

    function filterRoles(cat, btn) {{
      document.querySelectorAll("#view-roles .tab-pill").forEach(p => p.classList.remove("active"));
      btn.classList.add("active");

      if (cat === "all") renderRolesList(rolesData);
      else renderRolesList(rolesData.filter(r => r.category === cat));
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
        <div style="background: #030406; border: 4px solid var(--gold); border-radius: 20px; padding: 3.5rem 2.5rem; text-align: center; margin-top: 2rem; box-shadow: 0 0 60px rgba(197, 160, 89, 0.35);">
          <div style="font-size: 3.2rem; margin-bottom: 0.5rem;">👑</div>
          <div style="font-size: 0.85rem; letter-spacing: 3px; color: var(--gold); text-transform: uppercase; font-family: var(--font-kookies); font-weight: 700;">OTB Marketing Studio · City Kings</div>
          <div style="font-family: var(--font-royal); font-size: 2.2rem; color: var(--text-pure); margin: 0.85rem 0; font-weight: 900; letter-spacing: 1px;">CERTIFICATE OF GROWTH MASTERY</div>
          <p style="color: var(--text-dim); font-size: 1rem;">تشهد أكاديمية وكالة OTB للتسويق وهندسة النمو بأن</p>
          <h2 style="font-family: var(--font-felfel); font-size: 2.5rem; color: var(--gold); margin: 0.85rem 0; font-weight: 900;">${{name}}</h2>
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
    renderRolesList(rolesData);
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

print("Generated master LMS index.html with Felfel font and Visual Showcase Gallery")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
