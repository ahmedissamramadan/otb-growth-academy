import os
import shutil

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

# ==========================================
# 1. SHARED CSS (LUXURY OBSIDIAN & ROYAL GOLD)
# ==========================================
style_css = """
:root {
  --bg-primary: #070A10;
  --bg-secondary: #0D131F;
  --bg-surface: #111827;
  --bg-card: rgba(13, 19, 31, 0.85);
  --bg-card-hover: rgba(22, 30, 49, 0.95);
  
  --gold-primary: #F59E0B;
  --gold-light: #FEF3C7;
  --gold-dark: #B45309;
  --gold-gradient: linear-gradient(135deg, #FDE68A 0%, #F59E0B 50%, #B45309 100%);
  --gold-glow: 0 0 25px rgba(245, 158, 11, 0.25);
  
  --crimson: #E11D48;
  --emerald: #10B981;
  --cyan: #06B6D4;
  --purple: #8B5CF6;
  
  --text-main: #F8FAFC;
  --text-muted: #94A3B8;
  --text-dim: #64748B;
  
  --border-color: rgba(245, 158, 11, 0.18);
  --border-hover: rgba(245, 158, 11, 0.5);
  --glass-blur: blur(16px);
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --transition-smooth: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Readex Pro', 'Cairo', -apple-system, sans-serif;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-main);
  direction: rtl;
  min-height: 100vh;
  overflow-x: hidden;
  line-height: 1.6;
  background-image: 
    radial-gradient(circle at 10% 10%, rgba(245, 158, 11, 0.07) 0%, transparent 45%),
    radial-gradient(circle at 90% 90%, rgba(225, 29, 72, 0.05) 0%, transparent 45%),
    radial-gradient(circle at 50% 50%, rgba(13, 19, 31, 0.5) 0%, transparent 100%);
  background-attachment: fixed;
}

/* NAVBAR */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(7, 10, 16, 0.9);
  backdrop-filter: var(--glass-blur);
  border-bottom: 1px solid var(--border-color);
  padding: 0.85rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-link {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  text-decoration: none;
}

.crown-logo {
  font-size: 2rem;
  filter: drop-shadow(0 0 10px rgba(245, 158, 11, 0.6));
  animation: crownFloat 3s ease-in-out infinite alternate;
}

@keyframes crownFloat {
  0% { transform: translateY(0); }
  100% { transform: translateY(-3px); }
}

.brand-info h1 {
  font-size: 1.2rem;
  font-weight: 900;
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: -0.5px;
}

.brand-info p {
  font-size: 0.72rem;
  color: var(--text-muted);
  font-weight: 500;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  list-style: none;
}

.nav-item a {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.55rem 0.95rem;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 600;
  border-radius: var(--radius-sm);
  transition: var(--transition-smooth);
}

.nav-item a:hover {
  color: var(--gold-light);
  background: rgba(245, 158, 11, 0.08);
}

.nav-item a.active {
  color: #000;
  background: var(--gold-gradient);
  font-weight: 700;
  box-shadow: var(--gold-glow);
}

.btn-notebook {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(245, 158, 11, 0.12);
  border: 1px solid var(--gold-primary);
  color: var(--gold-light);
  padding: 0.5rem 1.1rem;
  border-radius: 9999px;
  text-decoration: none;
  font-size: 0.82rem;
  font-weight: 700;
  transition: var(--transition-smooth);
}

.btn-notebook:hover {
  background: var(--gold-primary);
  color: #000;
  box-shadow: var(--gold-glow);
  transform: translateY(-2px);
}

/* PODCAST AUDIO BANNER */
.audio-banner {
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
  padding: 0.7rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.audio-title-group {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.live-indicator {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(16, 185, 129, 0.15);
  color: var(--emerald);
  padding: 0.2rem 0.6rem;
  border-radius: 9999px;
  font-size: 0.72rem;
  font-weight: 700;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  background-color: var(--emerald);
  border-radius: 50%;
  box-shadow: 0 0 8px var(--emerald);
}

.custom-audio-player {
  height: 34px;
  max-width: 380px;
  outline: none;
}

/* BREADCRUMBS */
.breadcrumb-bar {
  background: rgba(13, 19, 31, 0.5);
  border-bottom: 1px solid rgba(245, 158, 11, 0.08);
  padding: 0.6rem 2rem;
  font-size: 0.8rem;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.breadcrumb-bar a {
  color: var(--gold-primary);
  text-decoration: none;
  transition: var(--transition-smooth);
}

.breadcrumb-bar a:hover {
  text-decoration: underline;
}

/* MAIN CONTAINER */
.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2.5rem 2rem 4rem 2rem;
}

/* PAGE HEADER */
.page-header {
  margin-bottom: 2.5rem;
  position: relative;
}

.page-tag {
  display: inline-block;
  background: rgba(245, 158, 11, 0.12);
  color: var(--gold-primary);
  border: 1px solid var(--border-color);
  padding: 0.25rem 0.85rem;
  border-radius: 9999px;
  font-size: 0.78rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
  letter-spacing: 0.5px;
}

.page-title {
  font-size: 2.2rem;
  font-weight: 900;
  color: #FFF;
  margin-bottom: 0.5rem;
}

.page-title span {
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.page-subtitle {
  font-size: 1.05rem;
  color: var(--text-muted);
  max-width: 800px;
}

/* CARDS & GLASS */
.card {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
  transition: var(--transition-smooth);
}

.card:hover {
  background: var(--bg-card-hover);
  border-color: var(--border-hover);
  transform: translateY(-3px);
}

.card-title {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--gold-light);
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* GRIDS */
.grid-2 {
  display: grid;
  grid-template-columns: 340px 1fr;
  gap: 2rem;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.75rem;
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

@media (max-width: 992px) {
  .grid-2 { grid-template-columns: 1fr; }
  .navbar { flex-direction: column; gap: 1rem; padding: 1rem; }
  .nav-links { flex-wrap: wrap; justify-content: center; }
}

/* LESSON SIDEBAR & DETAIL */
.sidebar-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.sidebar-item {
  padding: 1rem 1.25rem;
  background: var(--bg-secondary);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: var(--transition-smooth);
  text-decoration: none;
  color: var(--text-main);
  display: block;
}

.sidebar-item:hover {
  border-color: var(--gold-primary);
  transform: translateX(-4px);
  background: rgba(245, 158, 11, 0.06);
}

.sidebar-item.active {
  background: rgba(245, 158, 11, 0.15);
  border-color: var(--gold-primary);
  border-right: 4px solid var(--gold-primary);
  box-shadow: var(--gold-glow);
}

.item-badge {
  display: inline-block;
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
  font-size: 0.7rem;
  font-weight: 800;
  background: var(--gold-primary);
  color: #000;
  margin-bottom: 0.35rem;
}

.item-title {
  font-size: 0.95rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.item-meta {
  font-size: 0.78rem;
  color: var(--text-muted);
}

/* LESSON CONTENT SECTIONS */
.lesson-content {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 2.25rem;
}

.lesson-hero {
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 1.5rem;
  margin-bottom: 2rem;
}

.lesson-hero h2 {
  font-size: 1.75rem;
  font-weight: 900;
  color: var(--gold-light);
  margin: 0.5rem 0;
}

.lesson-box {
  background: var(--bg-secondary);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-sm);
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  border-right: 4px solid var(--gold-primary);
}

.lesson-box h3 {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--gold-primary);
  margin-bottom: 0.85rem;
}

.lesson-box p, .lesson-box ul, .lesson-box ol {
  color: #E2E8F0;
  font-size: 0.96rem;
  line-height: 1.8;
}

.lesson-box ul {
  padding-right: 1.5rem;
}

/* PROMPTS & CODE BLOCKS */
.prompt-box {
  background: #04060A;
  border: 1px solid rgba(245, 158, 11, 0.25);
  border-radius: var(--radius-sm);
  padding: 1.25rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.88rem;
  color: #38BDF8;
  direction: ltr;
  text-align: left;
  white-space: pre-wrap;
  position: relative;
  margin-bottom: 1rem;
  max-height: 260px;
  overflow-y: auto;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: var(--gold-gradient);
  color: #000;
  border: none;
  padding: 0.75rem 1.5rem;
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
  filter: brightness(1.1);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--text-main);
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-sm);
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  text-decoration: none;
  transition: var(--transition-smooth);
}

.btn-secondary:hover {
  background: rgba(245, 158, 11, 0.1);
  border-color: var(--gold-primary);
  color: var(--gold-light);
}

/* FORM CONTROLS */
.form-group {
  margin-bottom: 1.25rem;
}

.form-label {
  display: block;
  font-size: 0.88rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: var(--gold-light);
}

.form-input, .form-select, .form-textarea {
  width: 100%;
  background: var(--bg-surface);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-sm);
  padding: 0.8rem 1rem;
  color: #FFF;
  font-size: 0.95rem;
  outline: none;
  transition: var(--transition-smooth);
}

.form-input:focus, .form-select:focus, .form-textarea:focus {
  border-color: var(--gold-primary);
  box-shadow: 0 0 10px rgba(245, 158, 11, 0.2);
}

/* FOOTER */
.footer {
  background: var(--bg-secondary);
  border-top: 1px solid var(--border-color);
  padding: 3rem 2rem 2rem 2rem;
  margin-top: 4rem;
}

.footer-content {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.footer-contact {
  display: flex;
  gap: 1.5rem;
  font-size: 0.88rem;
  color: var(--text-muted);
}

.footer-contact a {
  color: var(--gold-light);
  text-decoration: none;
}

.footer-bottom {
  max-width: 1400px;
  margin: 2rem auto 0 auto;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  text-align: center;
  font-size: 0.78rem;
  color: var(--text-dim);
}
"""

print("Generating multi-page files...")
with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(style_css)

print("Shared style.css generated!")
