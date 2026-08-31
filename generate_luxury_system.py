import os
import shutil

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

# ==========================================
# 1. LUXURY CSS (style.css)
# ==========================================
luxury_css = """
:root {
  --bg-main: #06080D;
  --bg-sub: #0B0F19;
  --bg-card: rgba(14, 20, 33, 0.85);
  --bg-card-hover: rgba(20, 28, 46, 0.95);
  --bg-surface: #111827;
  --bg-elevated: #162032;

  --gold-50: #FFFBEB;
  --gold-100: #FEF3C7;
  --gold-200: #FDE68A;
  --gold-300: #FCD34D;
  --gold-400: #FBBF24;
  --gold-500: #F59E0B;
  --gold-600: #D97706;
  --gold-700: #B45309;
  --gold-gradient: linear-gradient(135deg, #FFFBEB 0%, #F59E0B 50%, #B45309 100%);
  --gold-glow: 0 0 30px rgba(245, 158, 11, 0.22);
  --gold-border: rgba(245, 158, 11, 0.2);
  --gold-border-hover: rgba(245, 158, 11, 0.6);

  --crimson: #E11D48;
  --emerald: #10B981;
  --cyan: #06B6D4;
  --purple: #8B5CF6;
  
  --text-pure: #FFFFFF;
  --text-main: #F1F5F9;
  --text-muted: #94A3B8;
  --text-dim: #64748B;
  
  --radius-xs: 6px;
  --radius-sm: 10px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-full: 9999px;
  
  --blur-glass: blur(18px);
  --shadow-card: 0 12px 40px -10px rgba(0, 0, 0, 0.6);
  --shadow-elevated: 0 20px 50px -15px rgba(0, 0, 0, 0.8);
  --transition-fast: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-smooth: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Readex Pro', 'Cairo', -apple-system, sans-serif;
  -webkit-font-smoothing: antialiased;
}

body {
  background-color: var(--bg-main);
  color: var(--text-main);
  direction: rtl;
  min-height: 100vh;
  overflow-x: hidden;
  line-height: 1.7;
  background-image: 
    radial-gradient(circle at 12% 12%, rgba(245, 158, 11, 0.08) 0%, transparent 45%),
    radial-gradient(circle at 88% 88%, rgba(225, 29, 72, 0.05) 0%, transparent 45%),
    radial-gradient(circle at 50% 50%, rgba(11, 15, 25, 0.7) 0%, transparent 100%);
  background-attachment: fixed;
}

/* CUSTOM SCROLLBAR */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: var(--bg-main); }
::-webkit-scrollbar-thumb { background: rgba(245, 158, 11, 0.25); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold-500); }

/* NAVBAR */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(6, 8, 13, 0.92);
  backdrop-filter: var(--blur-glass);
  border-bottom: 1px solid var(--gold-border);
  padding: 0.85rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: var(--transition-smooth);
}

.brand-wrapper {
  display: flex;
  align-items: center;
  gap: 0.9rem;
  text-decoration: none;
}

.brand-crown {
  font-size: 2.2rem;
  filter: drop-shadow(0 0 12px rgba(245, 158, 11, 0.7));
  animation: crownHover 3s ease-in-out infinite alternate;
}

@keyframes crownHover {
  0% { transform: translateY(0) rotate(0deg); }
  100% { transform: translateY(-4px) rotate(-3deg); }
}

.brand-text h1 {
  font-size: 1.22rem;
  font-weight: 900;
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: -0.5px;
  line-height: 1.2;
}

.brand-text p {
  font-size: 0.72rem;
  color: var(--gold-200);
  opacity: 0.75;
  font-weight: 500;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  list-style: none;
}

.nav-link-item a {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.55rem 0.95rem;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 600;
  border-radius: var(--radius-sm);
  transition: var(--transition-fast);
}

.nav-link-item a:hover {
  color: var(--gold-100);
  background: rgba(245, 158, 11, 0.1);
  transform: translateY(-1px);
}

.nav-link-item a.active {
  color: #000;
  background: var(--gold-gradient);
  font-weight: 800;
  box-shadow: var(--gold-glow);
}

.btn-notebook-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(245, 158, 11, 0.12);
  border: 1px solid var(--gold-500);
  color: var(--gold-100);
  padding: 0.55rem 1.15rem;
  border-radius: var(--radius-full);
  text-decoration: none;
  font-size: 0.82rem;
  font-weight: 800;
  transition: var(--transition-smooth);
}

.btn-notebook-badge:hover {
  background: var(--gold-500);
  color: #000;
  box-shadow: var(--gold-glow);
  transform: translateY(-2px);
}

/* PODCAST AUDIO STRIP */
.podcast-strip {
  background: linear-gradient(90deg, #0B0F19 0%, #111827 50%, #0B0F19 100%);
  border-bottom: 1px solid var(--gold-border);
  padding: 0.75rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.podcast-info {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.live-badge {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(16, 185, 129, 0.15);
  color: var(--emerald);
  padding: 0.25rem 0.7rem;
  border-radius: var(--radius-full);
  font-size: 0.74rem;
  font-weight: 800;
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.pulse-dot {
  width: 8px;
  height: 8px;
  background-color: var(--emerald);
  border-radius: 50%;
  box-shadow: 0 0 10px var(--emerald);
  animation: pulseAnim 1.5s infinite;
}

@keyframes pulseAnim {
  0% { transform: scale(0.95); opacity: 0.8; }
  50% { transform: scale(1.2); opacity: 1; }
  100% { transform: scale(0.95); opacity: 0.8; }
}

.audio-controls-wrap audio {
  height: 36px;
  max-width: 380px;
  outline: none;
  border-radius: var(--radius-full);
}

/* BREADCRUMB */
.breadcrumb-bar {
  background: rgba(11, 15, 25, 0.6);
  border-bottom: 1px solid rgba(245, 158, 11, 0.08);
  padding: 0.65rem 2rem;
  font-size: 0.82rem;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.breadcrumb-bar a {
  color: var(--gold-400);
  text-decoration: none;
  transition: var(--transition-fast);
}

.breadcrumb-bar a:hover {
  text-decoration: underline;
  color: var(--gold-200);
}

/* CONTAINER */
.container {
  max-width: 1440px;
  margin: 0 auto;
  padding: 2.5rem 2rem 5rem 2rem;
}

/* PAGE HEADER */
.page-header {
  margin-bottom: 3rem;
  position: relative;
}

.page-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(245, 158, 11, 0.12);
  color: var(--gold-400);
  border: 1px solid var(--gold-border);
  padding: 0.3rem 0.95rem;
  border-radius: var(--radius-full);
  font-size: 0.78rem;
  font-weight: 800;
  margin-bottom: 0.85rem;
  letter-spacing: 0.5px;
}

.page-title {
  font-size: 2.35rem;
  font-weight: 900;
  color: var(--text-pure);
  line-height: 1.25;
  margin-bottom: 0.65rem;
}

.page-title span {
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.page-subtitle {
  font-size: 1.05rem;
  color: var(--text-muted);
  max-width: 840px;
  line-height: 1.8;
}

/* CARDS & GLASSMORPHISM */
.card {
  background: var(--bg-card);
  backdrop-filter: var(--blur-glass);
  border: 1px solid var(--gold-border);
  border-radius: var(--radius-md);
  padding: 1.85rem;
  box-shadow: var(--shadow-card);
  transition: var(--transition-smooth);
  position: relative;
  overflow: hidden;
}

.card::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 100%;
  height: 3px;
  background: transparent;
  transition: var(--transition-fast);
}

.card:hover {
  background: var(--bg-card-hover);
  border-color: var(--gold-border-hover);
  transform: translateY(-4px);
  box-shadow: var(--shadow-elevated), var(--gold-glow);
}

.card:hover::before {
  background: var(--gold-gradient);
}

.card-title {
  font-size: 1.28rem;
  font-weight: 800;
  color: var(--gold-100);
  margin-bottom: 0.85rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

/* BUTTONS */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.55rem;
  background: var(--gold-gradient);
  color: #000;
  border: none;
  padding: 0.8rem 1.6rem;
  border-radius: var(--radius-sm);
  font-size: 0.95rem;
  font-weight: 800;
  cursor: pointer;
  text-decoration: none;
  transition: var(--transition-smooth);
}

.btn-primary:hover {
  box-shadow: var(--gold-glow);
  transform: translateY(-2px);
  filter: brightness(1.12);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.55rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--text-main);
  padding: 0.8rem 1.6rem;
  border-radius: var(--radius-sm);
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  text-decoration: none;
  transition: var(--transition-smooth);
}

.btn-secondary:hover {
  background: rgba(245, 158, 11, 0.12);
  border-color: var(--gold-500);
  color: var(--gold-100);
  transform: translateY(-2px);
}

/* GRIDS */
.grid-2 { display: grid; grid-template-columns: 340px 1fr; gap: 2.25rem; }
.grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.85rem; }
.grid-4 { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; }

@media (max-width: 1024px) {
  .grid-2 { grid-template-columns: 1fr; }
  .navbar { flex-direction: column; gap: 1rem; padding: 1rem; }
  .nav-menu { flex-wrap: wrap; justify-content: center; }
}

/* LESSON BOXES & CONTENT */
.lesson-box {
  background: var(--bg-sub);
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: var(--radius-sm);
  padding: 1.6rem;
  margin-bottom: 1.6rem;
  border-right: 4px solid var(--gold-500);
  transition: var(--transition-fast);
}

.lesson-box:hover {
  border-color: rgba(245, 158, 11, 0.4);
}

.lesson-box h3 {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--gold-400);
  margin-bottom: 0.85rem;
}

.lesson-box p, .lesson-box ul, .lesson-box ol {
  color: #E2E8F0;
  font-size: 0.96rem;
  line-height: 1.85;
}

.lesson-box ul { padding-right: 1.5rem; }
.lesson-box li { margin-bottom: 0.4rem; }

/* PROMPT CODE BOX */
.prompt-box {
  background: #040508;
  border: 1px solid rgba(245, 158, 11, 0.28);
  border-radius: var(--radius-sm);
  padding: 1.35rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.88rem;
  color: #38BDF8;
  direction: ltr;
  text-align: left;
  white-space: pre-wrap;
  position: relative;
  margin-bottom: 1rem;
  max-height: 280px;
  overflow-y: auto;
  line-height: 1.6;
}

/* TOAST NOTIFICATION */
.toast-msg {
  position: fixed;
  bottom: 2rem;
  left: 2rem;
  z-index: 9999;
  background: #000;
  border: 2px solid var(--gold-500);
  color: var(--gold-100);
  padding: 1rem 1.75rem;
  border-radius: var(--radius-sm);
  font-weight: 800;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8), var(--gold-glow);
  transform: translateY(100px);
  opacity: 0;
  transition: var(--transition-smooth);
}

.toast-msg.show {
  transform: translateY(0);
  opacity: 1;
}

/* FOOTER */
.footer {
  background: var(--bg-sub);
  border-top: 1px solid var(--gold-border);
  padding: 3.5rem 2rem 2.5rem 2rem;
  margin-top: 5rem;
}

.footer-inner {
  max-width: 1440px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 2rem;
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.footer-contact {
  display: flex;
  gap: 2rem;
  font-size: 0.9rem;
  color: var(--text-muted);
}

.footer-contact a {
  color: var(--gold-200);
  text-decoration: none;
}

.footer-bottom {
  max-width: 1440px;
  margin: 2.5rem auto 0 auto;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  text-align: center;
  font-size: 0.8rem;
  color: var(--text-dim);
}
"""

with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(luxury_css)

print("Luxury style.css generated successfully!")
