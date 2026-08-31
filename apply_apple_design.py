import os
import shutil

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

# Upgrade style.css with Apple Design principles
apple_css = """/* ==========================================================================
   OTB TEAM AI HUB — APPLE DESIGN SYSTEM TRANSLATION
   Fluid Physics, Translucent Materials, Optical Typography & Zero Latency
   ========================================================================== */

:root {
  /* Obsidian Noir & Champagne Gold Palette */
  --bg-deep: #020305;
  --bg-card: rgba(12, 14, 20, 0.72);
  --bg-card-hover: rgba(22, 26, 36, 0.85);
  --bg-input: rgba(18, 20, 28, 0.8);
  
  --gold: #D4A853;
  --gold-glow: rgba(212, 168, 83, 0.35);
  --gold-champagne: #F5E6C8;
  --gold-accent: #E5C378;

  --cyan: #38BDF8;
  --emerald: #10B981;
  --crimson: #F43F5E;

  --text-pure: #FFFFFF;
  --text-main: #E2E8F0;
  --text-muted: #94A3B8;
  --text-dim: #64748B;

  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-gold: rgba(212, 168, 83, 0.32);
  --border-gold-bright: rgba(212, 168, 83, 0.65);

  --radius-sm: 12px;
  --radius-md: 18px;
  --radius-lg: 26px;
  --radius-full: 9999px;

  /* Typography */
  --font-felfel: 'Felfel-Bold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-kookies: 'KOOkies-Bold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-kookies-black: 'KOOkies-ExtraBold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-royal: 'Cinzel', serif;
  --font-mono: 'JetBrains Mono', monospace;
  --font-ui: -apple-system, BlinkMacSystemFont, 'Readex Pro', 'SF Pro Text', 'SF Pro Icons', system-ui, sans-serif;

  /* Apple Fluid Spring Timings */
  --spring-snappy: cubic-bezier(0.2, 0, 0, 1);
  --spring-bounce: cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

/* @font-face rules */
@font-face {
  font-family: 'Felfel-Bold';
  src: url('assets/fonts/Felfel-Bold.woff2') format('woff2');
  font-weight: bold;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'KOOkies-Bold';
  src: url('assets/fonts/KOOkies-Bold.otf') format('opentype');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'KOOkies-ExtraBold';
  src: url('assets/fonts/KOOkies-ExtraBold.otf') format('opentype');
  font-weight: 900;
  font-style: normal;
  font-display: swap;
}

/* Reset & Optical Typography */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
  background-color: var(--bg-deep);
}

body {
  font-family: var(--font-ui);
  color: var(--text-main);
  background-color: var(--bg-deep);
  min-height: 100vh;
  overflow-x: hidden;
  position: relative;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Apple Translucent Layering & Film Grain */
body::after {
  content: "";
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.035'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 9999;
}

/* WebGL Background Canvas */
#webglCanvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 0;
  opacity: 0.85;
}

/* Apple Translucent Glass Navigation Bar */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(4, 6, 10, 0.65);
  backdrop-filter: blur(28px) saturate(190%);
  -webkit-backdrop-filter: blur(28px) saturate(190%);
  border-bottom: 1px solid var(--border-subtle);
  padding: 0.75rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.4);
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 1rem;
  text-decoration: none;
}

.brand-badge-img {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-sm);
  overflow: hidden;
  border: 1.5px solid var(--gold);
  box-shadow: 0 0 15px var(--gold-glow);
  transition: transform 0.25s var(--spring-snappy);
}

.brand-badge-img:hover {
  transform: scale(1.05);
}

.brand-badge-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.brand-text h1 {
  font-family: var(--font-kookies-black);
  font-size: 1.15rem;
  color: var(--text-pure);
  letter-spacing: -0.01em;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.brand-text span {
  font-size: 0.72rem;
  color: var(--gold);
  letter-spacing: 2px;
  font-weight: 700;
}

/* Apple Pill Navigation */
.nav-pills {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(18, 22, 32, 0.6);
  padding: 0.35rem 0.5rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
  backdrop-filter: blur(16px);
}

.nav-pill-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 0.45rem 1.1rem;
  border-radius: var(--radius-full);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: color 0.15s ease, background 0.15s ease, transform 0.1s var(--spring-snappy);
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

/* Instant Response on Pointer Down */
.nav-pill-btn:active {
  transform: scale(0.96);
}

.nav-pill-btn:hover {
  color: var(--text-pure);
  background: rgba(255, 255, 255, 0.06);
}

.nav-pill-btn.active {
  color: #000;
  background: var(--gold);
  font-weight: 700;
  box-shadow: 0 0 20px var(--gold-glow);
}

/* LTR Phone Button */
.phone-wrapper {
  direction: ltr !important;
  unicode-bidi: isolate !important;
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--gold);
  background: rgba(212, 168, 83, 0.08);
  border: 1px solid var(--border-gold);
  padding: 0.4rem 1rem;
  border-radius: var(--radius-full);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  transition: all 0.2s var(--spring-snappy);
}

.phone-wrapper:hover {
  background: rgba(212, 168, 83, 0.18);
  border-color: var(--gold);
  box-shadow: 0 0 16px var(--gold-glow);
  transform: translateY(-1px);
}

.phone-wrapper:active {
  transform: scale(0.96);
}

/* Container & Optical Layout */
.app-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 3rem 1.75rem 6rem 1.75rem;
  position: relative;
  z-index: 1;
}

/* Hero Typography */
.hero-wrapper {
  text-align: center;
  max-width: 860px;
  margin: 0 auto 3.5rem auto;
}

.hero-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 1.25rem;
  background: rgba(212, 168, 83, 0.1);
  border: 1px solid var(--border-gold);
  border-radius: var(--radius-full);
  color: var(--gold);
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 1.5px;
  margin-bottom: 1.25rem;
}

.hero-title {
  font-family: var(--font-felfel);
  font-size: clamp(2rem, 4.5vw, 3.4rem);
  color: var(--text-pure);
  line-height: 1.15;
  letter-spacing: -0.02em;
  margin-bottom: 1.25rem;
}

.hero-title span {
  color: var(--gold);
  text-shadow: 0 0 25px var(--gold-glow);
}

.hero-subtitle {
  font-size: clamp(1rem, 1.5vw, 1.15rem);
  color: var(--text-muted);
  line-height: 1.8;
  max-width: 760px;
  margin: 0 auto;
}

/* Apple Bento Cards & Interactive Surfaces */
.glass-card {
  background: var(--bg-card);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid var(--border-subtle);
  border-top: 1px solid rgba(255, 255, 255, 0.14); /* bright top edge = light catching */
  border-radius: var(--radius-md);
  padding: 1.75rem;
  transition: transform 0.3s var(--spring-snappy), border-color 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  overflow: hidden;
}

.glass-card:hover {
  background: var(--bg-card-hover);
  border-color: var(--border-gold);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5), 0 0 25px rgba(212, 168, 83, 0.12);
  transform: translateY(-3px);
}

.glass-card:active {
  transform: scale(0.985);
}

/* Bento Grid System */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1.25rem;
}

.bento-col-12 { grid-column: span 12; }
.bento-col-6  { grid-column: span 6; }
.bento-col-4  { grid-column: span 4; }

@media (max-width: 860px) {
  .bento-col-6, .bento-col-4 {
    grid-column: span 12;
  }
  .nav-pills {
    overflow-x: auto;
    max-width: 100%;
  }
}

/* Role Selector Grid */
.role-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
  margin-bottom: 2.5rem;
}

.role-tab {
  background: rgba(14, 17, 24, 0.7);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.15rem;
  cursor: pointer;
  transition: all 0.25s var(--spring-snappy);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 0.5rem;
}

.role-tab:hover {
  background: rgba(24, 30, 44, 0.85);
  border-color: var(--border-gold);
  transform: translateY(-2px);
}

.role-tab:active {
  transform: scale(0.96);
}

.role-tab.active {
  background: rgba(212, 168, 83, 0.1);
  border-color: var(--gold);
  box-shadow: 0 0 30px rgba(212, 168, 83, 0.25);
}

.role-icon-box {
  font-size: 2rem;
  margin-bottom: 0.25rem;
}

.role-name {
  font-family: var(--font-felfel);
  font-size: 1.15rem;
  color: var(--text-pure);
  font-weight: 700;
}

.role-eng {
  font-family: var(--font-kookies);
  font-size: 0.82rem;
  color: var(--gold);
  letter-spacing: 0.5px;
}

/* Selected Role Stage */
.role-stage {
  background: rgba(8, 10, 15, 0.85);
  border: 2px solid var(--border-gold);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7), 0 0 45px rgba(212, 168, 83, 0.15);
  backdrop-filter: blur(30px);
}

.role-header-strip {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 1.5rem;
  margin-bottom: 2rem;
}

.role-heading {
  font-family: var(--font-felfel);
  font-size: 2.2rem;
  color: var(--text-pure);
  margin-top: 0.25rem;
}

/* Tool Pill Badges */
.tool-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 1rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--text-main);
  transition: all 0.2s var(--spring-snappy);
}

.tool-pill:hover {
  background: rgba(212, 168, 83, 0.12);
  border-color: var(--gold);
  color: var(--gold-champagne);
  transform: translateY(-1px);
}

/* Buttons with Instant Press Feedback */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.65rem 1.4rem;
  border-radius: var(--radius-full);
  font-weight: 700;
  font-size: 0.92rem;
  cursor: pointer;
  border: none;
  text-decoration: none;
  transition: all 0.2s var(--spring-snappy);
}

.btn:active {
  transform: scale(0.96);
}

.btn-primary {
  background: var(--gold);
  color: #000;
  box-shadow: 0 4px 18px var(--gold-glow);
}

.btn-primary:hover {
  background: var(--gold-champagne);
  box-shadow: 0 6px 25px rgba(212, 168, 83, 0.5);
  transform: translateY(-2px);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.06);
  color: var(--text-main);
  border: 1px solid var(--border-subtle);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.12);
  border-color: var(--border-gold);
  color: var(--text-pure);
  transform: translateY(-2px);
}

/* Code Console Box */
.code-box {
  background: rgba(0, 0, 0, 0.7);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 1.25rem;
  font-family: var(--font-mono);
  font-size: 0.88rem;
  color: var(--cyan);
  line-height: 1.6;
  white-space: pre-wrap;
  direction: ltr;
  text-align: left;
  position: relative;
  margin: 0.75rem 0;
}

/* Tabs row */
.tabs-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.tab-pill {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  color: var(--text-muted);
  padding: 0.45rem 1.1rem;
  border-radius: var(--radius-full);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s var(--spring-snappy);
}

.tab-pill:hover {
  color: var(--text-pure);
  background: rgba(255, 255, 255, 0.1);
}

.tab-pill.active {
  background: var(--gold);
  color: #000;
  font-weight: 700;
  box-shadow: 0 0 16px var(--gold-glow);
}

/* Apple Accessibility & Reduced Motion Support */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  .glass-card, .btn, .role-tab, .tool-pill {
    transform: none !important;
  }
}

@media (prefers-reduced-transparency: reduce) {
  .navbar, .glass-card, .role-stage, .nav-pills {
    background: #090B10 !important;
    backdrop-filter: none !important;
  }
}
"""

with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(apple_css)

print("Applied Apple Design System to style.css!")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
