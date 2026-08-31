import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from generate_master_academy import COURSES_DATA
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

# ==============================================================================
# 1. AWARD-WINNING LUXURY STYLESHEET (style.css)
# ==============================================================================
award_winning_css = """
/* ==========================================================================
   OTB TEAM AI HUB — AWWWARDS SITE-OF-THE-YEAR DESIGN SYSTEM
   Art Direction: Obsidian Noir, Champagne Gold, Micro-Noise, Fluid Spring Physics
   Typography: Felfel (Bespoke Arabic Display), KOOkies, Cinzel, Readex Pro
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
  --bg-deep: #030406;
  --bg-surface: #07090E;
  --bg-card: rgba(12, 16, 25, 0.65);
  --bg-card-hover: rgba(20, 27, 42, 0.9);
  --bg-input: #020305;
  --bg-code: #010204;

  --border-subtle: rgba(255, 255, 255, 0.06);
  --border-glass: rgba(212, 168, 83, 0.22);
  --border-gold-glow: rgba(212, 168, 83, 0.6);

  --gold: #D4A853;
  --gold-metallic: #C5A059;
  --gold-champagne: #F4E7CE;
  --gold-dark: #8B651B;
  --gold-gradient: linear-gradient(135deg, #FFF6E5 0%, #D4A853 45%, #8B651B 100%);
  --gold-radial: radial-gradient(circle at 50% 0%, rgba(212, 168, 83, 0.15) 0%, transparent 70%);
  --gold-glow: 0 0 45px rgba(212, 168, 83, 0.2);

  --cyan: #38BDF8;
  --emerald: #10B981;
  --crimson: #F43F5E;

  --text-pure: #FFFFFF;
  --text-main: #E2E8F0;
  --text-muted: #94A3B8;
  --text-dim: #64748B;

  --font-felfel: 'Felfel', 'Readex Pro', -apple-system, sans-serif;
  --font-kookies: 'KOOkies', 'Plus Jakarta Sans', sans-serif;
  --font-ar: 'Readex Pro', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --font-royal: 'Cinzel', serif;

  --radius-xs: 8px;
  --radius-sm: 14px;
  --radius-md: 22px;
  --radius-lg: 36px;
  --radius-full: 9999px;

  --transition-fast: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-smooth: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-spring: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: var(--font-ar);
}

html, body {
  background-color: var(--bg-deep);
  color: var(--text-main);
  direction: rtl;
  min-height: 100vh;
  line-height: 1.85;
  font-size: 0.98rem;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  position: relative;
}

/* SUBTLE EDITORIAL FILM GRAIN OVERLAY */
body::after {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.025'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 9999;
}

/* THREE.JS PARTICLES CANVAS */
#webglCanvas {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  opacity: 0.55;
}

/* CUSTOM RADIAL CURSOR GLOW EFFECT */
#cursorGlow {
  position: fixed;
  width: 600px;
  height: 600px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(212, 168, 83, 0.06) 0%, transparent 65%);
  pointer-events: none;
  transform: translate(-50%, -50%);
  z-index: 1;
  transition: transform 0.1s ease-out, opacity 0.3s ease;
}

/* SCROLLBAR */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg-deep); }
::-webkit-scrollbar-thumb { background: rgba(212, 168, 83, 0.3); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }

/* AWWWARDS-GRADE GLASS NAVBAR */
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(3, 4, 6, 0.85);
  backdrop-filter: blur(28px);
  -webkit-backdrop-filter: blur(28px);
  border-bottom: 1px solid var(--border-subtle);
  padding: 1rem 2.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: var(--transition-smooth);
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 1rem;
  text-decoration: none;
}

.brand-badge-img {
  position: relative;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  padding: 2px;
  background: var(--gold-gradient);
  box-shadow: 0 0 25px rgba(212, 168, 83, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition-spring);
}

.nav-brand:hover .brand-badge-img {
  transform: rotate(10deg) scale(1.08);
}

.brand-badge-img img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

.brand-text h1 {
  font-family: var(--font-felfel);
  font-size: 1.35rem;
  color: var(--text-pure);
  line-height: 1.1;
  letter-spacing: 0.5px;
}

.brand-text span {
  font-family: var(--font-kookies);
  font-size: 0.72rem;
  color: var(--gold);
  font-weight: 800;
  letter-spacing: 1.2px;
}

/* NAVBAR NAVIGATION PILLS */
.nav-pills {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(255, 255, 255, 0.03);
  padding: 0.35rem 0.5rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
}

.nav-pill-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 0.5rem 1.25rem;
  border-radius: var(--radius-full);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-fast);
  display: flex;
  align-items: center;
  gap: 0.45rem;
  text-decoration: none;
}

.nav-pill-btn:hover {
  color: var(--text-pure);
  background: rgba(255, 255, 255, 0.06);
}

.nav-pill-btn.active {
  color: #000;
  background: var(--gold-gradient);
  font-weight: 800;
  box-shadow: 0 0 25px rgba(212, 168, 83, 0.45);
}

/* APP CONTAINER */
.app-container {
  max-width: 1140px;
  margin: 0 auto;
  padding: 3.5rem 1.5rem 6rem 1.5rem;
  position: relative;
  z-index: 2;
}

/* MONUMENTAL HERO */
.hero-wrapper {
  text-align: center;
  margin-bottom: 4rem;
  animation: fadeIn 0.9s cubic-bezier(0.16, 1, 0.3, 1);
}

.hero-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  background: rgba(212, 168, 83, 0.08);
  border: 1px solid var(--border-glass);
  color: var(--gold);
  padding: 0.45rem 1.35rem;
  border-radius: var(--radius-full);
  font-size: 0.82rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  font-family: var(--font-kookies);
}

.hero-title {
  font-family: var(--font-felfel);
  font-size: 3.2rem;
  color: var(--text-pure);
  line-height: 1.2;
  margin-bottom: 1.1rem;
  font-weight: 900;
  letter-spacing: -0.5px;
}

.hero-title span {
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  color: var(--text-muted);
  font-size: 1.1rem;
  max-width: 720px;
  margin: 0 auto;
  line-height: 1.85;
}

/* ROLE SELECTOR CARDS GRID (9 ROLES) */
.role-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
  margin-bottom: 2.5rem;
}

.role-tab {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.5rem 1.1rem;
  text-align: center;
  cursor: pointer;
  transition: var(--transition-spring);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.6rem;
  backdrop-filter: blur(16px);
  position: relative;
  overflow: hidden;
}

.role-tab::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 0%, rgba(212, 168, 83, 0.15), transparent 70%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.role-tab:hover::before {
  opacity: 1;
}

.role-tab:hover {
  border-color: var(--border-gold-glow);
  background: var(--bg-card-hover);
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), var(--gold-glow);
}

.role-tab.active {
  border-color: var(--gold);
  background: rgba(212, 168, 83, 0.1);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8), var(--gold-glow);
  transform: translateY(-3px);
}

.role-icon-box {
  font-size: 2.2rem;
  transition: var(--transition-spring);
}

.role-tab:hover .role-icon-box {
  transform: scale(1.18);
}

.role-name {
  font-family: var(--font-felfel);
  font-size: 1.05rem;
  color: var(--text-pure);
  line-height: 1.25;
  font-weight: 700;
}

.role-eng {
  font-family: var(--font-kookies);
  font-size: 0.7rem;
  color: var(--gold);
  font-weight: 800;
  letter-spacing: 0.5px;
}

/* ROLE DISPLAY STAGE */
.role-stage {
  background: var(--bg-surface);
  border: 1px solid var(--border-glass);
  border-radius: var(--radius-lg);
  padding: 3rem;
  box-shadow: 0 25px 70px rgba(0, 0, 0, 0.8), var(--gold-glow);
  animation: slideUp 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  backdrop-filter: blur(24px);
}

.role-header-strip {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 1.5rem;
  margin-bottom: 2.25rem;
  flex-wrap: wrap;
  gap: 1.25rem;
}

.role-heading {
  font-family: var(--font-felfel);
  font-size: 2rem;
  color: var(--text-pure);
  font-weight: 800;
}

/* LUXURY CARDS */
.glass-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  transition: var(--transition-smooth);
  backdrop-filter: blur(16px);
  position: relative;
  overflow: hidden;
}

.glass-card:hover {
  border-color: var(--border-glass);
  background: var(--bg-card-hover);
  transform: translateY(-2px);
}

/* TOOL BADGES */
.tool-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  background: rgba(56, 189, 248, 0.08);
  color: var(--cyan);
  border: 1px solid rgba(56, 189, 248, 0.25);
  padding: 0.45rem 1rem;
  border-radius: var(--radius-full);
  font-size: 0.85rem;
  font-weight: 700;
  transition: var(--transition-fast);
}

.tool-pill:hover {
  background: rgba(56, 189, 248, 0.18);
  transform: translateY(-2px);
  border-color: var(--cyan);
}

/* CODE / PROMPT BOX (Strict LTR) */
.code-box {
  background: var(--bg-code);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-sm);
  padding: 1.35rem;
  font-family: var(--font-mono);
  font-size: 0.9rem;
  color: #38BDF8;
  direction: ltr !important;
  text-align: left;
  white-space: pre-wrap;
  margin: 1.1rem 0;
  line-height: 1.75;
  box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.8);
}

/* LUXURY BUTTONS */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.65rem;
  border-radius: var(--radius-full);
  font-size: 0.92rem;
  font-weight: 700;
  text-decoration: none;
  cursor: pointer;
  transition: var(--transition-fast);
  border: none;
}

.btn-primary {
  background: var(--gold-gradient);
  color: #000;
  font-weight: 800;
  box-shadow: 0 4px 25px rgba(212, 168, 83, 0.35);
}

.btn-primary:hover {
  filter: brightness(1.12);
  transform: translateY(-2px);
  box-shadow: 0 8px 35px rgba(212, 168, 83, 0.5);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.04);
  color: var(--text-pure);
  border: 1px solid var(--border-subtle);
}

.btn-secondary:hover {
  border-color: var(--border-glass);
  background: rgba(212, 168, 83, 0.08);
  color: var(--gold-champagne);
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
  gap: 4px;
  color: var(--gold-champagne);
  text-decoration: none;
  font-weight: 600;
}

.phone-wrapper .phone-code {
  font-weight: 800;
  color: var(--gold);
}

.phone-wrapper .phone-num {
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
  color: var(--gold-champagne);
  padding: 0.9rem 2rem;
  border-radius: var(--radius-full);
  font-size: 0.95rem;
  font-weight: 700;
  opacity: 0;
  transition: var(--transition-smooth);
  z-index: 99999;
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.9), var(--gold-glow);
}

.toast.show {
  transform: translateX(-50%) translateY(0);
  opacity: 1;
}

/* ANIMATIONS */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-12px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(25px); }
  to { opacity: 1; transform: translateY(0); }
}

/* RESPONSIVE */
@media (max-width: 900px) {
  .navbar { flex-direction: column; gap: 1rem; padding: 1.25rem 1rem; }
  .nav-pills { flex-wrap: wrap; justify-content: center; }
  .hero-title { font-size: 2.2rem; }
  .role-stage { padding: 1.75rem 1.25rem; }
}
"""

with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(award_winning_css)

print("Generated Award-Winning style.css")

# ==============================================================================
# 2. INTERACTIVE THREE.JS & CURSOR ENGINE (shared_ui.js)
# ==============================================================================
award_winning_js = """
// THREE.JS PARTICLES & SMOOTH MOUSE GLOW ENGINE
document.addEventListener('DOMContentLoaded', () => {
  initWebGLParticles();
  initCursorTracker();
});

function initWebGLParticles() {
  const canvas = document.getElementById('webglCanvas');
  if (!canvas || !window.THREE) return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 80;

  const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // 450 GOLD DUST PARTICLES
  const particleCount = 450;
  const geometry = new THREE.BufferGeometry();
  const positions = new Float32Array(particleCount * 3);
  const colors = new Float32Array(particleCount * 3);

  const goldColors = [
    new THREE.Color('#D4A853'),
    new THREE.Color('#C5A059'),
    new THREE.Color('#F4E7CE'),
    new THREE.Color('#9E7D3B')
  ];

  for (let i = 0; i < particleCount; i++) {
    positions[i * 3] = (Math.random() - 0.5) * 160;
    positions[i * 3 + 1] = (Math.random() - 0.5) * 160;
    positions[i * 3 + 2] = (Math.random() - 0.5) * 160;

    const col = goldColors[Math.floor(Math.random() * goldColors.length)];
    colors[i * 3] = col.r;
    colors[i * 3 + 1] = col.g;
    colors[i * 3 + 2] = col.b;
  }

  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

  const material = new THREE.PointsMaterial({
    size: 1.4,
    vertexColors: true,
    transparent: true,
    opacity: 0.75,
    blending: THREE.AdditiveBlending
  });

  const particleSystem = new THREE.Points(geometry, material);
  scene.add(particleSystem);

  let mouseX = 0;
  let mouseY = 0;
  let targetX = 0;
  let targetY = 0;

  window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX - window.innerWidth / 2) * 0.03;
    mouseY = (e.clientY - window.innerHeight / 2) * 0.03;
  });

  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

  function animate() {
    requestAnimationFrame(animate);

    targetX += (mouseX - targetX) * 0.05;
    targetY += (mouseY - targetY) * 0.05;

    particleSystem.rotation.y += 0.0008;
    particleSystem.rotation.x += 0.0004;

    particleSystem.position.x = -targetX;
    particleSystem.position.y = targetY;

    renderer.render(scene, camera);
  }
  animate();
}

function initCursorTracker() {
  const glow = document.createElement('div');
  glow.id = 'cursorGlow';
  document.body.appendChild(glow);

  window.addEventListener('mousemove', (e) => {
    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';
  });
}

function copyText(text) {
  if (!text) return;
  navigator.clipboard.writeText(text).then(() => {
    showToast('👑 تم نسخ الأمر للحافظة بنجاح!');
  }).catch(() => {
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('👑 تم نسخ الأمر للحافظة بنجاح!');
  });
}

function showToast(msg) {
  let t = document.querySelector('.toast');
  if (!t) {
    t = document.createElement('div');
    t.className = 'toast';
    document.body.appendChild(t);
  }
  t.innerText = msg;
  t.classList.add('show');
  setTimeout(() => {
    t.classList.remove('show');
  }, 2800);
}
"""

with open(os.path.join(BASE_DIR, "shared_ui.js"), "w", encoding="utf-8") as f:
    f.write(award_winning_js)

print("Generated shared_ui.js with WebGL & Cursor Glow")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
