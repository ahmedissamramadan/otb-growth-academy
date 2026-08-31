import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from generate_master_academy import COURSES_DATA

courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

# ==============================================================================
# 1. AWWWARDS LUXURY STYLESHEET (style.css)
# ==============================================================================
awwwards_css = """
:root {
  --bg-deep: #06070A;
  --bg-surface: #0C0F17;
  --bg-surface-elevated: #111520;
  --bg-card: rgba(14, 18, 28, 0.7);
  --bg-card-hover: rgba(20, 26, 40, 0.9);
  --bg-code: #040508;

  --border: rgba(255, 255, 255, 0.07);
  --border-gold: rgba(212, 168, 83, 0.22);
  --border-gold-hover: rgba(212, 168, 83, 0.6);

  --gold: #D4A853;
  --gold-light: #F3E5C8;
  --gold-gradient: linear-gradient(135deg, #F3E5C8 0%, #D4A853 50%, #9B7023 100%);
  --gold-dim: rgba(212, 168, 83, 0.1);
  --gold-glow: 0 0 40px rgba(212, 168, 83, 0.18);

  --text-pure: #FFFFFF;
  --text-body: #94A3B8;
  --text-dim: #64748B;
  --text-accent: #E2E8F0;

  --font-ar: 'Readex Pro', -apple-system, sans-serif;
  --font-royal: 'Cinzel', serif;
  --font-mono: 'JetBrains Mono', monospace;

  --radius-xs: 6px;
  --radius-sm: 10px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-full: 9999px;

  --transition-fast: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-smooth: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: var(--font-ar);
}

html {
  scroll-behavior: smooth;
}

body {
  background-color: var(--bg-deep);
  color: var(--text-body);
  direction: rtl;
  min-height: 100vh;
  line-height: 1.75;
  font-size: 0.96rem;
  overflow-x: hidden;
  position: relative;
  -webkit-font-smoothing: antialiased;
}

/* THREE.JS BACKGROUND CANVAS */
#webgl-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  pointer-events: none;
}

/* SCROLLBAR */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg-deep); }
::-webkit-scrollbar-thumb { background: rgba(212, 168, 83, 0.3); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }

/* NAVBAR */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(6, 7, 10, 0.85);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 1rem 2.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: var(--transition-smooth);
}

.brand-wrapper {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  text-decoration: none;
}

.brand-crown {
  font-size: 1.8rem;
  filter: drop-shadow(0 0 10px rgba(212, 168, 83, 0.5));
}

.brand-text h1 {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text-pure);
  letter-spacing: -0.3px;
  line-height: 1.2;
}

.brand-text p {
  font-size: 0.72rem;
  color: var(--gold);
  letter-spacing: 1px;
  font-weight: 600;
  text-transform: uppercase;
}

.nav-menu {
  display: flex;
  gap: 0.4rem;
  list-style: none;
}

.nav-link {
  color: var(--text-dim);
  text-decoration: none;
  padding: 0.5rem 0.95rem;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 500;
  transition: var(--transition-fast);
}

.nav-link:hover {
  color: var(--text-pure);
  background: rgba(255, 255, 255, 0.04);
}

.nav-link.active {
  color: var(--gold);
  background: var(--gold-dim);
  border: 1px solid var(--border-gold);
  font-weight: 600;
}

.btn-notebook-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  background: var(--gold-dim);
  border: 1px solid var(--border-gold);
  color: var(--gold-light);
  padding: 0.45rem 1rem;
  border-radius: var(--radius-full);
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 600;
  transition: var(--transition-smooth);
}

.btn-notebook-badge:hover {
  background: var(--gold);
  color: #000;
  border-color: var(--gold);
  box-shadow: var(--gold-glow);
}

/* PODCAST STRIP (Selective RTL: Audio remains LTR) */
.podcast-bar {
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border);
  padding: 0.75rem 2.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.podcast-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.86rem;
  color: var(--text-accent);
  font-weight: 600;
}

.audio-wrap audio {
  height: 32px;
  max-width: 320px;
  outline: none;
  direction: ltr;
}

/* CONTAINER */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 3.5rem 2rem 6rem 2rem;
}

/* HERO SECTION */
.hero-section {
  text-align: center;
  padding: 4rem 1rem 5rem 1rem;
  position: relative;
}

.hero-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 1.5px;
  color: var(--gold);
  background: var(--gold-dim);
  border: 1px solid var(--border-gold);
  padding: 0.35rem 1.1rem;
  border-radius: var(--radius-full);
  margin-bottom: 1.5rem;
  text-transform: uppercase;
}

.hero-headline {
  font-size: 3rem;
  font-weight: 900;
  color: var(--text-pure);
  line-height: 1.25;
  margin-bottom: 1.25rem;
  letter-spacing: -0.8px;
}

.hero-headline span {
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtext {
  font-size: 1.1rem;
  color: var(--text-body);
  max-width: 720px;
  margin: 0 auto 2.25rem auto;
  line-height: 1.8;
}

.hero-ctas {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

/* BUTTONS */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.75rem;
  border-radius: var(--radius-sm);
  font-size: 0.92rem;
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
  transform: translateY(-2px);
  box-shadow: var(--gold-glow);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.03);
  color: var(--text-pure);
  border: 1px solid var(--border);
}

.btn-secondary:hover {
  border-color: var(--border-gold);
  background: var(--gold-dim);
  color: var(--gold-light);
  transform: translateY(-2px);
}

/* STATS GRID */
.stats-strip {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.25rem;
  margin-bottom: 4.5rem;
}

.stat-box {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  text-align: center;
  backdrop-filter: blur(16px);
  transition: var(--transition-smooth);
}

.stat-box:hover {
  border-color: var(--border-gold);
  background: var(--bg-card-hover);
  transform: translateY(-3px);
}

.stat-num {
  font-family: var(--font-mono);
  font-size: 2.1rem;
  font-weight: 700;
  color: var(--gold);
}

.stat-label {
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--text-pure);
  margin-top: 0.25rem;
}

.stat-sub {
  font-size: 0.78rem;
  color: var(--text-dim);
}

/* SECTION HEADINGS */
.section-header {
  margin-bottom: 2.25rem;
}

.section-tag {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--gold);
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-bottom: 0.4rem;
  display: block;
}

.section-title {
  font-size: 1.85rem;
  font-weight: 800;
  color: var(--text-pure);
}

.section-desc {
  font-size: 0.95rem;
  color: var(--text-body);
  max-width: 680px;
  margin-top: 0.4rem;
}

/* CARDS */
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  backdrop-filter: blur(16px);
  transition: var(--transition-smooth);
  position: relative;
}

.card:hover {
  border-color: var(--border-gold);
  background: var(--bg-card-hover);
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4), var(--gold-glow);
}

.card-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--text-pure);
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* GRIDS */
.grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 1.5rem; }
.grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; }
.grid-4 { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem; }

/* TABS */
.tabs-bar {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 1.75rem;
  border-bottom: 1px solid var(--border);
  padding-bottom: 0.75rem;
}

.tab-btn {
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-dim);
  padding: 0.5rem 1.15rem;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-fast);
}

.tab-btn:hover {
  color: var(--text-pure);
  background: rgba(255, 255, 255, 0.04);
}

.tab-btn.active {
  color: var(--gold);
  background: var(--gold-dim);
  border-color: var(--border-gold);
}

/* PROMPT / CODE BOX (Selective LTR) */
.code-box {
  background: var(--bg-code);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 1.15rem 1.35rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: #38BDF8;
  direction: ltr;
  text-align: left;
  white-space: pre-wrap;
  margin: 0.85rem 0;
  line-height: 1.6;
}

/* MODAL */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(6, 7, 10, 0.9);
  backdrop-filter: blur(20px);
  z-index: 99999;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}

.modal-overlay.active {
  display: flex;
}

.modal-box {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-gold);
  border-radius: var(--radius-md);
  width: 100%;
  max-width: 880px;
  max-height: 88vh;
  overflow-y: auto;
  padding: 2.25rem;
  position: relative;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.9), var(--gold-glow);
}

.modal-close {
  position: absolute;
  top: 1.25rem;
  left: 1.25rem;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--border);
  color: var(--text-pure);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition-fast);
}

.modal-close:hover {
  background: rgba(225, 29, 72, 0.2);
  border-color: #E11D48;
}

/* TOAST */
.toast {
  position: fixed;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%) translateY(100px);
  background: #000;
  border: 1px solid var(--gold);
  color: var(--gold-light);
  padding: 0.8rem 1.75rem;
  border-radius: var(--radius-sm);
  font-size: 0.9rem;
  font-weight: 600;
  opacity: 0;
  transition: var(--transition-smooth);
  z-index: 10000;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8), var(--gold-glow);
}

.toast.show {
  transform: translateX(-50%) translateY(0);
  opacity: 1;
}

/* FOOTER */
.footer {
  background: var(--bg-surface);
  border-top: 1px solid var(--border);
  padding: 3.5rem 2rem 2.5rem 2rem;
  margin-top: 5rem;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 2rem;
}

.footer-links {
  display: flex;
  gap: 1.5rem;
  font-size: 0.88rem;
}

.footer-links a {
  color: var(--text-dim);
  text-decoration: none;
  transition: var(--transition-fast);
}

.footer-links a:hover {
  color: var(--gold);
}

@media (max-width: 860px) {
  .navbar { flex-direction: column; gap: 1rem; padding: 1rem; }
  .nav-menu { flex-wrap: wrap; justify-content: center; }
  .hero-headline { font-size: 2.1rem; }
  .grid-2 { grid-template-columns: 1fr; }
}
"""

with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(awwwards_css)

print("Generated Awwwards-caliber style.css")

# ==============================================================================
# 2. SHARED_UI.JS (THREE.JS PARTICLES + GSAP + STATE)
# ==============================================================================
shared_js = """
// OTB Academy — Interactive WebGL & UI Engine
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

function copyText(txt, successMsg = "تم النسخ للحافظة بنجاح! 👑") {
  if (!txt) return;
  navigator.clipboard.writeText(txt).then(() => {
    showToast(successMsg);
  }).catch(err => {
    console.error("Copy failed", err);
  });
}

// THREE.JS AMBIENT PARTICLES
window.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("webgl-bg");
  if (!canvas || typeof THREE === "undefined") return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 80;

  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Gold star particles
  const count = 350;
  const geometry = new THREE.BufferGeometry();
  const positions = new Float32Array(count * 3);

  for (let i = 0; i < count * 3; i += 3) {
    positions[i] = (Math.random() - 0.5) * 160;
    positions[i + 1] = (Math.random() - 0.5) * 160;
    positions[i + 2] = (Math.random() - 0.5) * 80;
  }
  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

  const material = new THREE.PointsMaterial({
    size: 1.4,
    color: 0xD4A853,
    transparent: true,
    opacity: 0.45
  });

  const particles = new THREE.Points(geometry, material);
  scene.add(particles);

  let mouseX = 0, mouseY = 0;
  window.addEventListener("mousemove", (e) => {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 4;
    mouseY = (e.clientY / window.innerHeight - 0.5) * 4;
  });

  function animate() {
    requestAnimationFrame(animate);
    particles.rotation.y += 0.0005;
    particles.rotation.x += 0.0003;
    camera.position.x += (mouseX - camera.position.x) * 0.03;
    camera.position.y += (-mouseY - camera.position.y) * 0.03;
    renderer.render(scene, camera);
  }
  animate();

  window.addEventListener("resize", () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
});
"""

with open(os.path.join(BASE_DIR, "shared_ui.js"), "w", encoding="utf-8") as f:
    f.write(shared_js)

print("Generated shared_ui.js with Three.js engine")

# ==============================================================================
# 3. MASTER FLAGSHIP INDEX.HTML
# ==============================================================================
p_flagship = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Growth Academy — The City Kings</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=JetBrains+Mono:wght@500;600;700&family=Readex+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>
  <canvas id="webgl-bg"></canvas>

  <!-- NAVBAR -->
  <header class="navbar">
    <a href="index.html" class="brand-wrapper">
      <span class="brand-crown">👑</span>
      <div class="brand-text">
        <h1>OTB GROWTH ACADEMY</h1>
        <p>THE CITY KINGS · FULL-STACK GROWTH 2026</p>
      </div>
    </a>
    <ul class="nav-menu">
      <li><a href="#overview" class="nav-link active">نظرة عامة</a></li>
      <li><a href="#mindmap" class="nav-link">الخريطة الذهنية</a></li>
      <li><a href="#courses" class="nav-link">المقررات الـ 19</a></li>
      <li><a href="#sprint" class="nav-link">معسكر الـ 5 أيام</a></li>
      <li><a href="#prompts" class="nav-link">استوديو AI</a></li>
      <li><a href="#cases" class="nav-link">دراسات الحالة</a></li>
      <li><a href="#quiz" class="nav-link">الشهادة</a></li>
      <li><a href="#downloads" class="nav-link">التحميلات</a></li>
    </ul>
    <a href="https://notebooklm.google.com/notebook/76ef5be2-d7d2-4a33-a88d-f88fc0fe1148" target="_blank" class="btn-notebook-badge">
      <span>✨ مشروع NotebookLM</span>
    </a>
  </header>

  <!-- AUDIO PODCAST STRIP -->
  <div class="podcast-bar">
    <div class="podcast-info">
      <span style="font-size: 1.1rem;">🎙️</span>
      <span>التدريب الصوتي الاستراتيجي المعتمد (Gemini Studio Deep Dive Podcast)</span>
    </div>
    <div class="audio-wrap">
      <audio controls>
        <source src="track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" type="audio/mp4">
      </audio>
    </div>
  </div>

  <main class="container">
    
    <!-- 1. HERO SECTION -->
    <section id="overview" class="hero-section">
      <span class="hero-pill">👑 THE OFFICIAL INTERNAL GROWTH ENGINE · 2026</span>
      <h1 class="hero-headline">أكاديمية OTB للتسويق: <span>هندسة نمو ملوك المدينة</span></h1>
      <p class="hero-subtext">
        المنظومة التدريبية والتنفيذية الشاملة المستخلصة من 2,400+ صفحة علمية لتمكين فرق عمل وكالة OTB الـ 16 دوراً وظيفياً عبر 19 مساراً تخصصياً، وأوامر الذكاء الاصطناعي التوليدي، ودراسات حالة العملاء الموثقة.
      </p>
      <div class="hero-ctas">
        <a href="#courses" class="btn btn-primary">استعراض المقررات الـ 19 المفصلة</a>
        <a href="#mindmap" class="btn btn-secondary">🗺️ الخريطة الذهنية التفاعلية</a>
        <a href="#sprint" class="btn btn-secondary">⚡ معسكر الـ 5 أيام السريع</a>
      </div>
    </section>

    <!-- 2. STATS STRIP -->
    <section class="stats-strip">
      <div class="stat-box">
        <div class="stat-num">19 Courses</div>
        <div class="stat-label">مقرراً دراسياً معمقاً</div>
        <div class="stat-sub">مستخلصة من 2,400+ صفحة منهج</div>
      </div>
      <div class="stat-box">
        <div class="stat-num">80+ Sub-Skills</div>
        <div class="stat-label">مهارة تكتيكية في الخريطة</div>
        <div class="stat-sub">تغطي كامل مراحل قمع النمو</div>
      </div>
      <div class="stat-box">
        <div class="stat-num">50+ Prompts</div>
        <div class="stat-label">أمر ذكاء اصطناعي RCIC</div>
        <div class="stat-sub">مجهزة لأدوار OTB الـ 16 دوراً</div>
      </div>
      <div class="stat-box">
        <div class="stat-num">7+ Years</div>
        <div class="stat-label">خبرة واقعية في السوق</div>
        <div class="stat-sub">سجل حافل في مضاعفة أرباح العملاء</div>
      </div>
    </section>

    <!-- CLIENTS TICKER BADGE -->
    <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-md); padding: 1.25rem 2rem; margin-bottom: 5rem; text-align: center;">
      <div style="font-size: 0.78rem; font-weight: 700; color: var(--gold); letter-spacing: 1px; margin-bottom: 0.75rem; text-transform: uppercase;">
        👑 موثق بدراسات حالة وحملات حقيقية لعملاء OTB المعتمدين:
      </div>
      <div style="display: flex; justify-content: center; align-items: center; gap: 1.75rem; flex-wrap: wrap; font-size: 0.92rem; color: var(--text-pure); font-weight: 600;">
        <span>☕ MIX Coffee</span> · <span>🍔 Rancho's EG</span> · <span>💍 Dr. Zaghloul Jewelry</span> · <span>🍰 Rice Patisserie</span> · <span>📦 Sakr Store</span> · <span>🧪 Elag Labs</span> · <span>🌯 Wilson Crepe</span>
      </div>
    </div>

    <!-- 3. MINDMAP SECTION -->
    <section id="mindmap" style="margin-bottom: 6rem;">
      <div class="section-header">
        <span class="section-tag">ARCHITECTURAL ROADMAP</span>
        <h2 class="section-title">🗺️ الخريطة الذهنية والتفكيك الهيكلي للمنهج</h2>
        <p class="section-desc">تفكيك منهجي متكامل للمقررات الـ 19 في 4 مراحل نمو رئيسية و 80+ تخصصاً فرعياً.</p>
      </div>

      <div class="grid-2">
        <div class="card" style="border-right: 4px solid var(--gold);">
          <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">المرحلة 01</span>
          <h3 class="card-title">👑 الأساسات، الاستراتيجية، وبناء الهوية</h3>
          <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-body); line-height: 1.8;">
            <li><b>مبادئ التسويق الحديث:</b> 4Ps إلى 4Cs، سيكولوجية المستهلك والقيمة المدركة.</li>
            <li><b>الاستراتيجية والتخطيط:</b> تحليل STP ونموذج SOSTAC وخطة الـ 90 يوماً.</li>
            <li><b>بناء الهوية والعلامة:</b> نمط The Ruler لـ OTB، كراسة الهوية ونبرة الصوت.</li>
            <li><b>الانضباط التشغيلي:</b> إجراءات CoreLink CRM، قفل التبعيات، واتفاقيات الـ SLA.</li>
          </ul>
        </div>

        <div class="card" style="border-right: 4px solid #38BDF8;">
          <span style="font-size: 0.8rem; color: #38BDF8; font-weight: 700;">المرحلة 02</span>
          <h3 class="card-title">✍️ الكرييتف، المحتوى الفيرال، وسيو محركات البحث</h3>
          <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-body); line-height: 1.8;">
            <li><b>تسويق المحتوى والكوبي رايتنج:</b> صيغة PAS، قاعدة الـ 3 ثوانٍ الأولى، وجداول النشر.</li>
            <li><b>احتراف إنستغرام والريلز:</b> خوارزمية الـ Reels، سلاسل الستوري، وأتمتة الرسائل.</li>
            <li><b>سيو محركات البحث:</b> الكلمات المفتاحية التنافسية، السيو التقني، وسيو نتائج الذكاء الاصطناعي.</li>
            <li><b>يوتيوب وسيو الفيديو:</b> سيكولوجية الصورة المصغرة (CTR > 10%) واستراتيجية Shorts.</li>
          </ul>
        </div>

        <div class="card" style="border-right: 4px solid #10B981;">
          <span style="font-size: 0.8rem; color: #10B981; font-weight: 700;">المرحلة 03</span>
          <h3 class="card-title">📊 ميديا بايينج الأداء والسيطرة الإعلانية</h3>
          <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-body); line-height: 1.8;">
            <li><b>إعلانات Meta للأداء:</b> Advantage+، تتبع السيرفر CAPI، وقواعد السكيلينج الرأسي (+20%).</li>
            <li><b>إعلانات ونمو تيك توك:</b> خوارزمية FYP، إعلانات Spark Ads، وسيو تيك توك للمتاجر.</li>
            <li><b>إعلانات سناب شات والخليج:</b> استهداف السوق السعودي، عدسات الواقع المعزز (AR).</li>
            <li><b>لينكد إن B2B ومنصة إكس:</b> استقطاب صناع القرار، المحتوى القيادي، والثريدات التحليلية.</li>
          </ul>
        </div>

        <div class="card" style="border-right: 4px solid #A855F7;">
          <span style="font-size: 0.8rem; color: #A855F7; font-weight: 700;">المرحلة 04</span>
          <h3 class="card-title">🤖 الذكاء الاصطناعي، الأتمتة، وعقود الريتينر</h3>
          <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-body); line-height: 1.8;">
            <li><b>الذكاء الاصطناعي التوليدي:</b> هندسة أوامر RCIC، أصول 3D Midjourney، وأتمتة WhatsApp API.</li>
            <li><b>الإيميل ماركتنج والجروث:</b> استعادة السلات المتروكة، قمع AARRR، ومصفوفة ICE.</li>
            <li><b>عقود الريتينر الشهرية:</b> إغلاق عقود الـ $2,500/شهر القائمة على القيمة والعائد.</li>
            <li><b>التميز المهني:</b> السيرة الذاتية المبنية على الأرقام واجتياز المقابلات بنموذج STAR.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 4. COURSES CATALOG -->
    <section id="courses" style="margin-bottom: 6rem;">
      <div class="section-header">
        <span class="section-tag">FULL-SPECTRUM ENCYCLOPEDIA</span>
        <h2 class="section-title">📚 موسوعة المقررات الـ 19 المفصلة</h2>
        <p class="section-desc">المناهج الأكاديمية المستخلصة من 2,400+ صفحة. انقر على أي مقرر لقراءة الوحدات والأوامر والتكليف العملي.</p>
      </div>

      <div class="tabs-bar">
        <button class="tab-btn active" onclick="filterCourses('all', this)">الكل (19 مقرر)</button>
        <button class="tab-btn" onclick="filterCourses('strategy', this)">الاستراتيجية والهوية (4)</button>
        <button class="tab-btn" onclick="filterCourses('creative', this)">المحتوى والسيو (4)</button>
        <button class="tab-btn" onclick="filterCourses('media', this)">الميديا بايينج (5)</button>
        <button class="tab-btn" onclick="filterCourses('ai', this)">الذكاء الاصطناعي والجروث (4)</button>
        <button class="tab-btn" onclick="filterCourses('career', this)">عقود الوكالة والمهنة (2)</button>
      </div>

      <div class="grid-3" id="coursesGrid"></div>
    </section>

    <!-- 5. SPRINT SECTION -->
    <section id="sprint" style="margin-bottom: 6rem;">
      <div class="section-header">
        <span class="section-tag">INTENSIVE ONBOARDING</span>
        <h2 class="section-title">⚡ معسكر الـ 5 أيام السريع (Sprint)</h2>
        <p class="section-desc">الكبسولة التدريبية اليومية السريعة لفريق عمل الوكالة مع التكليفات اليومية الفورية.</p>
      </div>

      <div class="tabs-bar">
        <button class="tab-btn active" onclick="loadSprintDay(1, this)">اليوم 01: STP والتموضع</button>
        <button class="tab-btn" onclick="loadSprintDay(2, this)">اليوم 02: الكرييتف وريلز</button>
        <button class="tab-btn" onclick="loadSprintDay(3, this)">اليوم 03: ميديا بايينج ROAS</button>
        <button class="tab-btn" onclick="loadSprintDay(4, this)">اليوم 04: AI وأتمتة الواتساب</button>
        <button class="tab-btn" onclick="loadSprintDay(5, this)">اليوم 05: التشغيل والريتينر</button>
      </div>

      <div id="sprintView" class="card" style="padding: 2rem;"></div>
    </section>

    <!-- 6. AI PROMPTS STUDIO -->
    <section id="prompts" style="margin-bottom: 6rem;">
      <div class="section-header">
        <span class="section-tag">INTERACTIVE PROMPT GENERATOR</span>
        <h2 class="section-title">🤖 استوديو أوامر الذكاء الاصطناعي</h2>
        <p class="section-desc">ولد أوامرك المعتمدة بصيغة RCIC فورياً بنقرة زر واحدة.</p>
      </div>

      <div class="card" style="border: 2px solid var(--border-gold); padding: 2rem; margin-bottom: 2rem;">
        <div class="grid-2" style="margin-bottom: 1.5rem;">
          <div>
            <label style="display: block; font-size: 0.88rem; color: var(--text-pure); margin-bottom: 0.4rem; font-weight: 600;">اختر التكليف والتخصص:</label>
            <select id="promptTask" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-surface-elevated);" onchange="updatePrompt()">
              <option value="copy">كتابة إعلانات تحويلية (PAS Framework)</option>
              <option value="reels">اسكريبت فيديو قصير 15 ثانية (Viral Hook)</option>
              <option value="media">تشخيص حساب إعلاني وسكيلينج (Media Buying)</option>
              <option value="design">لقطات برودكت شوت 3D لـ Midjourney</option>
              <option value="retainer">مقترح عقد ريتينر شهري ($2,500/mo)</option>
            </select>
          </div>
          <div>
            <label style="display: block; font-size: 0.88rem; color: var(--text-pure); margin-bottom: 0.4rem; font-weight: 600;">اسم البراند والقطاع:</label>
            <input type="text" id="promptBrand" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-surface-elevated);" value="MIX Coffee (Specialty Coffee)" oninput="updatePrompt()">
          </div>
        </div>

        <div style="margin-bottom: 1.25rem;">
          <label style="display: block; font-size: 0.88rem; color: var(--text-pure); margin-bottom: 0.4rem; font-weight: 600;">الأمر المولد فورياً (RCIC Output):</label>
          <div id="promptOutput" class="code-box" style="max-height: 250px; overflow-y: auto;"></div>
        </div>

        <button class="btn btn-primary" onclick="copyText(document.getElementById('promptOutput').innerText)">📋 نسخ الأمر للحافظة</button>
      </div>
    </section>

    <!-- 7. CASE STUDIES -->
    <section id="cases" style="margin-bottom: 6rem;">
      <div class="section-header">
        <span class="section-tag">EVIDENCE & DOCUMENTED ROI</span>
        <h2 class="section-title">💼 دراسات حالة عملاء OTB الموثقة</h2>
        <p class="section-desc">تحليل استراتيجي وأرقام حقيقية توضح العائد الاستثماري لحملات الوكالة.</p>
      </div>

      <div class="grid-3">
        <div class="card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Specialty Coffee</span>
            <span style="font-size: 0.78rem; color: #10B981; font-weight: 700;">تفاعل +180%</span>
          </div>
          <h3 class="card-title">☕ MIX Coffee</h3>
          <p style="font-size: 0.88rem; color: var(--text-body); line-height: 1.7;">
            إعادة التموضع كوجهة أولى لرواد الأعمال، هوية داكنة راقية، وفيديوهات ASMR لتحضير القهوة، مما ضاعف مبيعات الفروع.
          </p>
        </div>

        <div class="card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Gourmet Burgers</span>
            <span style="font-size: 0.78rem; color: #10B981; font-weight: 700;">Retention 36.8%</span>
          </div>
          <h3 class="card-title">🍔 Rancho's EG</h3>
          <p style="font-size: 0.88rem; color: var(--text-body); line-height: 1.7;">
            الخروج من فخ الخصومات، تموضع البرجر الملحمي، وإعلانات ريلز PAS حققت 450 ألف مشاهدة وزيادة المبيعات بنسبة 65%.
          </p>
        </div>

        <div class="card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Luxury Jewelry</span>
            <span style="font-size: 0.78rem; color: #10B981; font-weight: 700;">ROAS 7.5x+</span>
          </div>
          <h3 class="card-title">💍 Dr. Zaghloul Jewelry</h3>
          <p style="font-size: 0.88rem; color: var(--text-body); line-height: 1.7;">
            بناء الثقة وسرد قصص التصاميم الحصرية بجودة سينمائية وهيكل حملات TOFU/MOFU/BOFU محققاً عائداً إعلانيا تجاوز 7.5x.
          </p>
        </div>

        <div class="card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Pastry & Sweets</span>
            <span style="font-size: 0.78rem; color: #10B981; font-weight: 700;">100% Sold Out</span>
          </div>
          <h3 class="card-title">🍰 Rice Patisserie</h3>
          <p style="font-size: 0.88rem; color: var(--text-body); line-height: 1.7;">
            حملات حجز مسبق قبل المناسبات مع أتمتة رسائل العروض الحصرية، مما أدى لنفاد كامل الكميات قبل 48 ساعة من كل موسم.
          </p>
        </div>

        <div class="card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">E-Commerce</span>
            <span style="font-size: 0.78rem; color: #10B981; font-weight: 700;">CPA -32%</span>
          </div>
          <h3 class="card-title">📦 Sakr Store</h3>
          <p style="font-size: 0.88rem; color: var(--text-body); line-height: 1.7;">
            إعادة هيكلة إعلانات Advantage+ وتتبع CAPI مع عروض الباقات، مما خفض تكلفة الشراء بنسبة 32% ورفع متوسط السلة بنسبة 50%.
          </p>
        </div>

        <div class="card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Clinics & Labs</span>
            <span style="font-size: 0.78rem; color: #10B981; font-weight: 700;">800+ Leads / mo</span>
          </div>
          <h3 class="card-title">🧪 Elag Labs</h3>
          <p style="font-size: 0.88rem; color: var(--text-body); line-height: 1.7;">
            إعلانات تحويلية سريعة مع مسار واتساب مؤتمت لاستقبال وتأهيل حجوزات التحاليل والزيارات المنزلية بنجاح.
          </p>
        </div>
      </div>
    </section>

    <!-- 8. ASSESSMENT & CERTIFICATION -->
    <section id="quiz" style="margin-bottom: 6rem; max-width: 860px; margin-inline: auto;">
      <div class="section-header" style="text-align: center;">
        <span class="section-tag">OFFICIAL CERTIFICATION</span>
        <h2 class="section-title">📝 تقييم الكفاءة وشهادة ملوك المدينة</h2>
        <p class="section-desc" style="margin-inline: auto;">أدخل اسمك وأجب عن الأسئلة الخمسة لإصدار شهادة الاعتماد الملكية الرسمية.</p>
      </div>

      <div class="card" style="margin-bottom: 1.5rem;">
        <label style="display: block; font-size: 0.88rem; color: var(--text-pure); margin-bottom: 0.4rem; font-weight: 600;">الاسم الرسمي على الشهادة:</label>
        <input type="text" id="certName" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-surface-elevated); font-size: 1rem;" value="أحمد عصام رمضان">
      </div>

      <div id="quizWrap">
        <div class="card">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.6rem;">1. ما هو التموضع والنمط النفسي المعتمد لوكالة OTB؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.88rem;"><input type="radio" name="q0" value="0"> المنافسة على أقل سعر</label>
          <label style="display:block; font-size:0.88rem;"><input type="radio" name="q0" value="1" checked> The Ruler & The Creator (ملوك المدينة: الهيبة والجرأة والتركيز على العائد)</label>
        </div>

        <div class="card">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.6rem;">2. ما هو الهدف الأساسي من أول 3 ثوانٍ في ريلز الإعلانات؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.88rem;"><input type="radio" name="q1" value="1" checked> كسر التمرير (Pattern Interrupt) وجذب انتباه المشاهد (Hook Rate > 35%)</label>
          <label style="display:block; font-size:0.88rem;"><input type="radio" name="q1" value="0"> كتابة أرقام السجل التجاري</label>
        </div>

        <div class="card">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.6rem;">3. إذا كان هامش الربح 25%، فما هو الـ Break-Even ROAS؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.88rem;"><input type="radio" name="q2" value="1" checked> 4.0x (حيث 1 / 0.25 = 4)</label>
          <label style="display:block; font-size:0.88rem;"><input type="radio" name="q2" value="0"> 1.5x</label>
        </div>

        <div class="card">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.6rem;">4. ما هي النسبة الآمنة لزيادة ميزانية الحملات الرابحة (Scaling)؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.88rem;"><input type="radio" name="q3" value="1" checked> زيادة 20% كل 48-72 ساعة لحماية استقرار الحملة</label>
          <label style="display:block; font-size:0.88rem;"><input type="radio" name="q3" value="0"> مضاعفة الميزانية 200% كل ساعة</label>
        </div>

        <div class="card">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.6rem;">5. ما هو السعر القياسي لباقة الـ Dominance Retainer لـ OTB؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.88rem;"><input type="radio" name="q4" value="1" checked> $2,500 / شهر (هوية + 24 محتوى + ميديا بايينج + أتمتة)</label>
          <label style="display:block; font-size:0.88rem;"><input type="radio" name="q4" value="0"> $300 / شهر</label>
        </div>
      </div>

      <div style="text-align: center; margin: 2rem 0;">
        <button class="btn btn-primary" style="padding: 0.85rem 3rem; font-size: 1.05rem;" onclick="generateCert()">👑 إصدار شهادة الاعتماد الملكية</button>
      </div>

      <div id="certOutput" style="display: none;"></div>
    </section>

    <!-- 9. DOWNLOADS SECTION -->
    <section id="downloads" style="margin-bottom: 4rem;">
      <div class="section-header">
        <span class="section-tag">RESOURCE CENTER</span>
        <h2 class="section-title">📥 مركز الموارد والتحميلات المباشرة</h2>
        <p class="section-desc">أصول الاستوديو والملفات الصوتية والمستندات التكتيكية متاحة للتحميل الفوري.</p>
      </div>

      <div class="grid-4">
        <div class="card">
          <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">MP4 Audio · 34 MB</span>
          <h4 class="card-title" style="margin-top: 0.3rem;">🎙️ بودكاست التدريب</h4>
          <p style="font-size: 0.85rem; color: var(--text-body); margin-bottom: 1rem;">حلقة صوتية معمقة من Gemini Studio.</p>
          <a href="track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" download class="btn btn-primary" style="width: 100%; font-size: 0.82rem; padding: 0.45rem;">📥 تحميل الصوت</a>
        </div>

        <div class="card">
          <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Markdown Doc</span>
          <h4 class="card-title" style="margin-top: 0.3rem;">📑 التقرير الاستراتيجي</h4>
          <p style="font-size: 0.85rem; color: var(--text-body); margin-bottom: 1rem;">وثيقة التوجيه التنفيذي الشاملة.</p>
          <a href="track_b_4week_masterclass/studio_artifacts/OTB_Executive_Strategic_Briefing.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.82rem; padding: 0.45rem;">📥 تحميل المستند</a>
        </div>

        <div class="card">
          <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">50+ Prompts</span>
          <h4 class="card-title" style="margin-top: 0.3rem;">📖 موسوعة الأوامر</h4>
          <p style="font-size: 0.85rem; color: var(--text-body); margin-bottom: 1rem;">موسوعة أوامر الذكاء الاصطناعي المعتمدة.</p>
          <a href="track_a_fast_track_sprint/cheatsheets/OTB_Prompt_Engineering_Bible.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.82rem; padding: 0.45rem;">📥 تحميل الموسوعة</a>
        </div>

        <div class="card">
          <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">Checklist</span>
          <h4 class="card-title" style="margin-top: 0.3rem;">✈️ فحص الميديا بايينج</h4>
          <p style="font-size: 0.85rem; color: var(--text-body); margin-bottom: 1rem;">قائمة فحص الحملات وقواعد السكيلينج.</p>
          <a href="track_a_fast_track_sprint/cheatsheets/OTB_Media_Buying_Checklist.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.82rem; padding: 0.45rem;">📥 تحميل الفحص</a>
        </div>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-content">
      <div style="display: flex; align-items: center; gap: 0.75rem;">
        <span style="font-size: 2rem;">👑</span>
        <div>
          <h3 style="color: var(--text-pure); font-size: 1.1rem; font-weight: 800;">OTB Agency — We Are The City Kings</h3>
          <p style="color: var(--text-dim); font-size: 0.82rem;">استراتيجيات جريئة.. نتائج حقيقية | Bold Strategies. Real Results</p>
        </div>
      </div>
      <div class="footer-links">
        <div>📍 القاهرة، مصر</div>
        <div>📞 <bdi dir="ltr"><a href="tel:+201008080295" class="phone-link">&lrm;+20 100 808 0295</a></bdi></div>
        <div>✉️ <a href="mailto:otbagency5@gmail.com">otbagency5@gmail.com</a></div>
      </div>
    </div>
    <div style="text-align: center; margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--border); font-size: 0.78rem; color: var(--text-dim);">
      © 2026 OTB Agency Growth Engineering Academy. All Rights Reserved. Engineered for Unmatched Market Dominance.
    </div>
  </footer>

  <!-- MODAL FOR COURSES -->
  <div id="courseModal" class="modal-overlay">
    <div class="modal-box">
      <button class="modal-close" onclick="closeCourseModal()">✕</button>
      <div id="modalBody"></div>
    </div>
  </div>

  <script src="shared_ui.js"></script>
  <script>
    const coursesData = {courses_json};

    function renderCoursesGrid(list) {{
      const grid = document.getElementById("coursesGrid");
      let html = "";
      list.forEach(c => {{
        html += `
          <div class="card" onclick="openCourseModal('${{c.id}}')" style="cursor: pointer;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.6rem;">
              <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">${{c.badge}}</span>
              <span style="font-size: 0.76rem; color: var(--text-dim); font-family: var(--font-mono);">${{c.pages}} P.</span>
            </div>
            <h3 class="card-title">
              <span>${{c.icon}}</span>
              <span>${{c.title}}</span>
            </h3>
            <p style="font-size: 0.88rem; color: var(--text-body); line-height: 1.7; margin-bottom: 1.25rem;">
              ${{c.desc}}
            </p>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border); padding-top: 0.75rem;">
              <span style="color: var(--gold); font-weight: 700; font-size: 0.85rem;">استعراض المنهج والتكليف ←</span>
              <span style="font-size: 0.8rem; color: var(--text-dim);">المرحلة 0${{c.phase}}</span>
            </div>
          </div>
        `;
      }});
      grid.innerHTML = html;
    }}

    function openCourseModal(courseId) {{
      const c = coursesData.find(item => item.id === courseId);
      if (!c) return;

      let unitsHtml = "";
      c.units.forEach((u, i) => {{
        unitsHtml += `<li style="margin-bottom: 0.4rem;"><b>الوحدة ${{i + 1}}:</b> ${{u}}</li>`;
      }});

      document.getElementById("modalBody").innerHTML = `
        <span class="hero-pill" style="margin-bottom: 0.75rem;">المرحلة 0${{c.phase}} · ${{c.badge}} · ${{c.pages}} صفحة منهج</span>
        <h2 style="font-size: 1.7rem; color: var(--text-pure); margin-bottom: 0.75rem;">${{c.icon}} ${{c.title}}</h2>
        <p style="color: var(--text-body); font-size: 0.95rem; margin-bottom: 1.5rem;">${{c.desc}}</p>

        <div class="card" style="margin-bottom: 1.25rem;">
          <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.5rem;">📖 الوحدات الأكاديمية للمنهج:</h4>
          <ul style="padding-right: 1.25rem; font-size: 0.9rem; color: var(--text-body); line-height: 1.8;">
            ${{unitsHtml}}
          </ul>
        </div>

        <div class="card" style="margin-bottom: 1.25rem; border-color: rgba(56, 189, 248, 0.3);">
          <h4 style="font-size: 1rem; color: #38BDF8; margin-bottom: 0.4rem;">🤖 أمر الذكاء الاصطناعي المعتمد (RCIC Prompt):</h4>
          <div class="code-box">${{c.prompt}}</div>
          <button class="btn btn-secondary" style="font-size: 0.82rem; padding: 0.4rem 0.9rem;" onclick="copyText(this.previousElementSibling.innerText)">📋 نسخ الأمر</button>
        </div>

        <div class="card" style="margin-bottom: 1.25rem; border-color: rgba(16, 185, 129, 0.3);">
          <h4 style="font-size: 1rem; color: #10B981; margin-bottom: 0.3rem;">💼 دراسة الحالة التطبيقية لعملاء OTB:</h4>
          <p style="font-size: 0.9rem; color: var(--text-body); line-height: 1.7;">${{c.case_study}}</p>
        </div>

        <div class="card" style="border-color: rgba(168, 85, 247, 0.3);">
          <h4 style="font-size: 1rem; color: #A855F7; margin-bottom: 0.3rem;">🧪 التكليف العملي الإلزامي:</h4>
          <p style="font-size: 0.9rem; color: var(--gold-light); line-height: 1.7;"><b>المطلوب تسليمه:</b> ${{c.lab}}</p>
        </div>
      `;

      document.getElementById("courseModal").classList.add("active");
    }}

    function closeCourseModal() {{
      document.getElementById("courseModal").classList.remove("active");
    }}

    function filterCourses(cat, btn) {{
      document.querySelectorAll(".tabs-bar .tab-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      if (cat === "all") renderCoursesGrid(coursesData);
      else renderCoursesGrid(coursesData.filter(c => c.cat === cat));
    }}

    // SPRINT ENGINE
    const sprintLessons = [
      {{
        day: 1,
        title: "اليوم الأول: تحليل السوق والتموضع وبناء الهوية (STP & Positioning)",
        audience: "الاستراتيجيون ومدراء الحسابات",
        concepts: "• <b>Segmentation:</b> تقسيم السوق سلوكياً ونفسياً.<br>• <b>Targeting:</b> اختيار الشريحة ذات أعلى قيمة عمرية (LTV).<br>• <b>Positioning:</b> حفر تموضع ملكي لا يُنسى في ذهن العميل.",
        caseStudy: "تحويل MIX Coffee من كافيه تقليدي إلى وجهة أولى لرواد الأعمال، محققاً +180% نمواً في التفاعل.",
        prompt: "معادلة التموضع (Positioning Statement):\\n[Target Audience] + [Category] + [Differentiating Benefit] + [Reason to Believe]",
        lab: "اختيار عميل وتعبئة وثيقة البريف واستخراج 3 زوايا تسويقية تستغل فجوات المنافسين."
      }},
      {{
        day: 2,
        title: "اليوم الثاني: الكوبي رايتنج الإعلاني وسيكولوجية الفيديو القصير",
        audience: "صناع المحتوى والمصممون والمونتيرون",
        concepts: "• <b>قاعدة الـ 3 ثوانٍ (Hook Rate > 35%):</b> كسر التمرير بصرياً وصوتياً.<br>• <b>صيغة PAS:</b> Problem (المشكلة) + Agitation (التهويل) + Solution (الحل الفوري).<br>• <b>صوتيات الـ ASMR:</b> رفع الإشباع البصري والصوتي في فيديوهات المنتجات.",
        caseStudy: "فيديو ريلز لـ Rancho's EG يبرز تفاصيل تقطيع البرجر الملحمي حقق 450 ألف مشاهدة ورفع مبيعات الواتساب بنسبة 65%.",
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
        document.querySelectorAll("#sprint .tab-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
      }}
      const d = sprintLessons.find(item => item.day === dNum);
      document.getElementById("sprintView").innerHTML = `
        <div style="font-size: 0.8rem; color: var(--gold); font-weight: 700; margin-bottom: 0.4rem;">المستهدفون: ${{d.audience}}</div>
        <h3 style="font-size: 1.35rem; color: var(--text-pure); margin-bottom: 1.25rem;">${{d.title}}</h3>

        <div style="margin-bottom: 1.25rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.35rem;">📖 المفاهيم والنماذج:</h4>
          <p style="font-size: 0.9rem; color: var(--text-body); line-height: 1.8;">${{d.concepts}}</p>
        </div>

        <div style="margin-bottom: 1.25rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.35rem;">💼 دراسة الحالة التطبيقية:</h4>
          <p style="font-size: 0.9rem; color: var(--text-body); line-height: 1.7;">${{d.caseStudy}}</p>
        </div>

        <div style="margin-bottom: 1.25rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.35rem;">📐 القالب التكتيكي:</h4>
          <div class="code-box">${{d.prompt}}</div>
        </div>

        <div>
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.35rem;">🧪 التكليف اليومي:</h4>
          <p style="font-size: 0.9rem; color: var(--gold-light); line-height: 1.7;"><b>المطلوب تسليمه:</b> ${{d.lab}}</p>
        </div>
      `;
    }}

    // PROMPTS STUDIO ENGINE
    function updatePrompt() {{
      const task = document.getElementById("promptTask").value;
      const brand = document.getElementById("promptBrand").value || "البراند";
      const out = document.getElementById("promptOutput");

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

    // CERTIFICATE ENGINE
    function generateCert() {{
      const name = document.getElementById("certName").value || "خريج الأكاديمية";
      const certId = "OTB-" + Math.floor(100000 + Math.random() * 900000);
      const date = new Date().toLocaleDateString('ar-EG', {{ year: 'numeric', month: 'long', day: 'numeric' }});
      const wrap = document.getElementById("certOutput");

      wrap.style.display = "block";
      wrap.innerHTML = `
        <div style="background: #040507; border: 4px solid var(--gold); border-radius: 20px; padding: 3rem 2rem; text-align: center; margin-top: 2rem; box-shadow: 0 0 60px rgba(212, 168, 83, 0.3);">
          <div style="font-size: 3rem; margin-bottom: 0.5rem;">👑</div>
          <div style="font-size: 0.85rem; letter-spacing: 3px; color: var(--gold); text-transform: uppercase; font-family: var(--font-royal); font-weight: 700;">OTB Marketing Studio · City Kings</div>
          <div style="font-family: var(--font-royal); font-size: 2rem; color: var(--text-pure); margin: 0.85rem 0; font-weight: 900; letter-spacing: 1px;">CERTIFICATE OF GROWTH MASTERY</div>
          <p style="color: var(--text-dim); font-size: 1rem;">تشهد أكاديمية وكالة OTB للتسويق وهندسة النمو بأن</p>
          <h2 style="font-size: 2.2rem; color: var(--gold); margin: 0.85rem 0; font-weight: 900;">${{name}}</h2>
          <p style="color: var(--text-accent); max-width: 580px; margin: 0 auto 2rem auto; font-size: 0.95rem; line-height: 1.8;">
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

    // INITIALIZE
    renderCoursesGrid(coursesData);
    loadSprintDay(1);
    updatePrompt();
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(p_flagship)

print("Generated flagship index.html")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
