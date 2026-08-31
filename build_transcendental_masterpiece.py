import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from generate_master_academy import COURSES_DATA
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

# ==============================================================================
# 1. TRANSCENDENTAL LUXURY STYLESHEET (style.css)
# ==============================================================================
transcendental_css = """
/* ==========================================================================
   OTB TEAM AI HUB — TRANSCENDENTAL LUXURY DESIGN SYSTEM
   Art Direction: Haute Couture Obsidian, Liquid Gold Ribbons, 3D WebGL Mesh, Bento Architecture
   Typography: Felfel (Arabic Display), KOOkies, Cinzel Decorative, Readex Pro
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
  --bg-deep: #020305;
  --bg-surface: #06080D;
  --bg-card: rgba(10, 14, 22, 0.7);
  --bg-card-hover: rgba(18, 24, 38, 0.92);
  --bg-input: #010203;
  --bg-code: #010102;

  --border-subtle: rgba(255, 255, 255, 0.07);
  --border-gold: rgba(212, 168, 83, 0.28);
  --border-gold-glow: rgba(212, 168, 83, 0.75);

  --gold: #D4A853;
  --gold-metallic: #C5A059;
  --gold-champagne: #F5E8D0;
  --gold-dark: #7A540E;
  --gold-gradient: linear-gradient(135deg, #FFF8EC 0%, #D4A853 40%, #A67C2E 70%, #68480E 100%);
  --gold-shimmer: linear-gradient(90deg, #D4A853 0%, #FFF8EC 50%, #D4A853 100%);
  --gold-glow: 0 0 50px rgba(212, 168, 83, 0.25);
  --gold-glow-intense: 0 0 80px rgba(212, 168, 83, 0.45);

  --cyan: #38BDF8;
  --emerald: #10B981;
  --crimson: #F43F5E;
  --purple: #C084FC;

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
  --radius-md: 24px;
  --radius-lg: 40px;
  --radius-full: 9999px;

  --transition-fast: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-smooth: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-spring: all 0.65s cubic-bezier(0.34, 1.56, 0.64, 1);
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

/* HAUTE COUTURE FILM GRAIN OVERLAY */
body::after {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.028'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 9999;
}

/* THREE.JS WEBGL CANVAS (Background Scene) */
#webglCanvas {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  opacity: 0.65;
}

/* RADIAL GLOW FOLLOWING CURSOR */
#cursorGlow {
  position: fixed;
  width: 650px;
  height: 650px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(212, 168, 83, 0.07) 0%, rgba(212, 168, 83, 0.02) 40%, transparent 70%);
  pointer-events: none;
  transform: translate(-50%, -50%);
  z-index: 1;
  transition: transform 0.08s ease-out;
}

/* SCROLLBAR */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg-deep); }
::-webkit-scrollbar-thumb { background: rgba(212, 168, 83, 0.35); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }

/* ULTRA-LUXURY GLASS NAVBAR */
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(2, 3, 5, 0.88);
  backdrop-filter: blur(32px);
  -webkit-backdrop-filter: blur(32px);
  border-bottom: 1px solid var(--border-subtle);
  padding: 1rem 2.75rem;
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
  width: 48px;
  height: 48px;
  border-radius: 50%;
  padding: 2px;
  background: var(--gold-gradient);
  box-shadow: 0 0 30px rgba(212, 168, 83, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition-spring);
}

.nav-brand:hover .brand-badge-img {
  transform: rotate(12deg) scale(1.1);
}

.brand-badge-img img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

.brand-text h1 {
  font-family: var(--font-felfel);
  font-size: 1.4rem;
  color: var(--text-pure);
  line-height: 1.1;
  letter-spacing: 0.5px;
}

.brand-text span {
  font-family: var(--font-kookies);
  font-size: 0.72rem;
  color: var(--gold);
  font-weight: 800;
  letter-spacing: 1.5px;
}

/* NAVBAR NAVIGATION PILLS */
.nav-pills {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(255, 255, 255, 0.025);
  padding: 0.35rem 0.5rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
}

.nav-pill-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 0.55rem 1.35rem;
  border-radius: var(--radius-full);
  font-size: 0.88rem;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition-fast);
  display: flex;
  align-items: center;
  gap: 0.5rem;
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
  box-shadow: 0 0 30px rgba(212, 168, 83, 0.5);
}

/* MAIN CONTAINER */
.app-container {
  max-width: 1160px;
  margin: 0 auto;
  padding: 3.5rem 1.5rem 6rem 1.5rem;
  position: relative;
  z-index: 2;
}

/* MONUMENTAL HERO SECTION */
.hero-wrapper {
  text-align: center;
  margin-bottom: 4.5rem;
  animation: fadeIn 1s cubic-bezier(0.16, 1, 0.3, 1);
}

.hero-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  background: rgba(212, 168, 83, 0.08);
  border: 1px solid var(--border-gold);
  color: var(--gold);
  padding: 0.45rem 1.45rem;
  border-radius: var(--radius-full);
  font-size: 0.82rem;
  font-weight: 800;
  margin-bottom: 1.75rem;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  font-family: var(--font-kookies);
  box-shadow: 0 0 25px rgba(212, 168, 83, 0.15);
}

.hero-title {
  font-family: var(--font-felfel);
  font-size: 3.5rem;
  color: var(--text-pure);
  line-height: 1.2;
  margin-bottom: 1.25rem;
  font-weight: 900;
  letter-spacing: -0.5px;
}

.hero-title span {
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
  animation: goldShimmer 6s infinite linear;
}

.hero-subtitle {
  color: var(--text-muted);
  font-size: 1.15rem;
  max-width: 760px;
  margin: 0 auto;
  line-height: 1.85;
}

/* ROLE SELECTOR GRID (9 BESPOKE CARDS) */
.role-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1.1rem;
  margin-bottom: 3rem;
}

.role-tab {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.6rem 1.1rem;
  text-align: center;
  cursor: pointer;
  transition: var(--transition-spring);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.65rem;
  backdrop-filter: blur(20px);
  position: relative;
  overflow: hidden;
  transform-style: preserve-3d;
  perspective: 800px;
}

.role-tab::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 0%, rgba(212, 168, 83, 0.2), transparent 70%);
  opacity: 0;
  transition: opacity 0.35s ease;
}

.role-tab:hover::before {
  opacity: 1;
}

.role-tab:hover {
  border-color: var(--border-gold-glow);
  background: var(--bg-card-hover);
  transform: translateY(-6px) scale(1.02);
  box-shadow: 0 20px 45px rgba(0, 0, 0, 0.7), var(--gold-glow);
}

.role-tab.active {
  border-color: var(--gold);
  background: rgba(212, 168, 83, 0.12);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.85), var(--gold-glow-intense);
  transform: translateY(-4px);
}

.role-icon-box {
  font-size: 2.35rem;
  transition: var(--transition-spring);
}

.role-tab:hover .role-icon-box {
  transform: scale(1.2) rotate(4deg);
}

.role-name {
  font-family: var(--font-felfel);
  font-size: 1.1rem;
  color: var(--text-pure);
  line-height: 1.25;
  font-weight: 700;
}

.role-eng {
  font-family: var(--font-kookies);
  font-size: 0.72rem;
  color: var(--gold);
  font-weight: 800;
  letter-spacing: 0.5px;
}

/* BENTO GRID ROLE DISPLAY STAGE */
.role-stage {
  background: var(--bg-surface);
  border: 1px solid var(--border-gold);
  border-radius: var(--radius-lg);
  padding: 3.25rem;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.85), var(--gold-glow);
  animation: slideUp 0.55s cubic-bezier(0.16, 1, 0.3, 1);
  backdrop-filter: blur(28px);
}

.bento-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1.25rem;
}

.bento-col-12 { grid-column: span 12; }
.bento-col-8 { grid-column: span 8; }
.bento-col-6 { grid-column: span 6; }
.bento-col-4 { grid-column: span 4; }

/* LUXURY GLASS CARD */
.glass-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.85rem;
  transition: var(--transition-smooth);
  backdrop-filter: blur(20px);
  position: relative;
  overflow: hidden;
}

.glass-card:hover {
  border-color: var(--border-gold);
  background: var(--bg-card-hover);
  transform: translateY(-2px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

/* TOOL BADGES */
.tool-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(56, 189, 248, 0.08);
  color: var(--cyan);
  border: 1px solid rgba(56, 189, 248, 0.28);
  padding: 0.5rem 1.15rem;
  border-radius: var(--radius-full);
  font-size: 0.88rem;
  font-weight: 700;
  transition: var(--transition-fast);
}

.tool-pill:hover {
  background: rgba(56, 189, 248, 0.2);
  transform: translateY(-2px);
  border-color: var(--cyan);
  box-shadow: 0 0 20px rgba(56, 189, 248, 0.3);
}

/* CODE / PROMPT BOX (Strict LTR) */
.code-box {
  background: var(--bg-code);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-sm);
  padding: 1.45rem;
  font-family: var(--font-mono);
  font-size: 0.92rem;
  color: #38BDF8;
  direction: ltr !important;
  text-align: left;
  white-space: pre-wrap;
  margin: 1.15rem 0;
  line-height: 1.75;
  box-shadow: inset 0 2px 12px rgba(0, 0, 0, 0.85);
}

/* BUTTONS */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.55rem;
  padding: 0.8rem 1.85rem;
  border-radius: var(--radius-full);
  font-size: 0.94rem;
  font-weight: 800;
  text-decoration: none;
  cursor: pointer;
  transition: var(--transition-fast);
  border: none;
}

.btn-primary {
  background: var(--gold-gradient);
  color: #000;
  font-weight: 800;
  box-shadow: 0 4px 25px rgba(212, 168, 83, 0.38);
}

.btn-primary:hover {
  filter: brightness(1.14);
  transform: translateY(-2px);
  box-shadow: 0 8px 40px rgba(212, 168, 83, 0.55);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.04);
  color: var(--text-pure);
  border: 1px solid var(--border-subtle);
}

.btn-secondary:hover {
  border-color: var(--border-gold);
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
  font-weight: 700;
}

.phone-wrapper .phone-code {
  font-weight: 900;
  color: var(--gold);
}

.phone-wrapper .phone-num {
  letter-spacing: 0.5px;
}

/* TOAST NOTIFICATION */
.toast {
  position: fixed;
  bottom: 2.75rem;
  left: 50%;
  transform: translateX(-50%) translateY(100px);
  background: #06080D;
  border: 1px solid var(--gold);
  color: var(--gold-champagne);
  padding: 1rem 2.25rem;
  border-radius: var(--radius-full);
  font-size: 0.98rem;
  font-weight: 800;
  opacity: 0;
  transition: var(--transition-smooth);
  z-index: 99999;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.95), var(--gold-glow);
}

.toast.show {
  transform: translateX(-50%) translateY(0);
  opacity: 1;
}

/* ANIMATIONS */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-14px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes goldShimmer {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* RESPONSIVE */
@media (max-width: 900px) {
  .navbar { flex-direction: column; gap: 1rem; padding: 1.25rem 1rem; }
  .nav-pills { flex-wrap: wrap; justify-content: center; }
  .hero-title { font-size: 2.3rem; }
  .role-stage { padding: 1.75rem 1.25rem; }
  .bento-col-8, .bento-col-6, .bento-col-4 { grid-column: span 12; }
}
"""

with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(transcendental_css)

print("Generated Transcendental Luxury style.css")

# ==============================================================================
# 2. WEBGL 3D MESH & PARALLAX ENGINE (shared_ui.js)
# ==============================================================================
transcendental_js = """
// 3D FLOATING ISOMETRIC GOLD CUBE + PARTICLE FIELD
document.addEventListener('DOMContentLoaded', () => {
  initTranscendentalWebGL();
  initCursorTracker();
});

function initTranscendentalWebGL() {
  const canvas = document.getElementById('webglCanvas');
  if (!canvas || !window.THREE) return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 75;

  const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // 1. ROTATING METALLIC WIREFRAME CUBE (OTB EMBLEM)
  const cubeGeo = new THREE.BoxGeometry(18, 18, 18);
  const cubeMat = new THREE.MeshBasicMaterial({
    color: 0xD4A853,
    wireframe: true,
    transparent: true,
    opacity: 0.22
  });
  const wireCube = new THREE.Mesh(cubeGeo, cubeMat);
  wireCube.position.set(0, 0, -10);
  scene.add(wireCube);

  // INNER GLOW CUBE
  const innerGeo = new THREE.IcosahedronGeometry(9, 1);
  const innerMat = new THREE.MeshBasicMaterial({
    color: 0xF5E8D0,
    wireframe: true,
    transparent: true,
    opacity: 0.15
  });
  const innerMesh = new THREE.Mesh(innerGeo, innerMat);
  wireCube.add(innerMesh);

  // 2. 500 GOLD DUST PARTICLES
  const particleCount = 500;
  const geometry = new THREE.BufferGeometry();
  const positions = new Float32Array(particleCount * 3);
  const colors = new Float32Array(particleCount * 3);

  const goldColors = [
    new THREE.Color('#D4A853'),
    new THREE.Color('#F5E8D0'),
    new THREE.Color('#C5A059'),
    new THREE.Color('#9E7D3B')
  ];

  for (let i = 0; i < particleCount; i++) {
    positions[i * 3] = (Math.random() - 0.5) * 170;
    positions[i * 3 + 1] = (Math.random() - 0.5) * 170;
    positions[i * 3 + 2] = (Math.random() - 0.5) * 170;

    const col = goldColors[Math.floor(Math.random() * goldColors.length)];
    colors[i * 3] = col.r;
    colors[i * 3 + 1] = col.g;
    colors[i * 3 + 2] = col.b;
  }

  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

  const material = new THREE.PointsMaterial({
    size: 1.5,
    vertexColors: true,
    transparent: true,
    opacity: 0.8,
    blending: THREE.AdditiveBlending
  });

  const particleSystem = new THREE.Points(geometry, material);
  scene.add(particleSystem);

  let mouseX = 0;
  let mouseY = 0;
  let targetX = 0;
  let targetY = 0;

  window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX - window.innerWidth / 2) * 0.035;
    mouseY = (e.clientY - window.innerHeight / 2) * 0.035;
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

    // ROTATE CUBE & PARTICLES
    wireCube.rotation.x += 0.003;
    wireCube.rotation.y += 0.005;
    innerMesh.rotation.y -= 0.008;

    particleSystem.rotation.y += 0.0006;
    particleSystem.rotation.x += 0.0003;

    particleSystem.position.x = -targetX * 0.8;
    particleSystem.position.y = targetY * 0.8;

    wireCube.position.x = targetX * 1.2;
    wireCube.position.y = -targetY * 1.2;

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
    f.write(transcendental_js)

print("Generated Transcendental shared_ui.js")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
