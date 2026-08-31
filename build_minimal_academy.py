import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

# ==============================================================================
# 1. ULTRA-MINIMAL LUXURY CSS (style.css)
# ==============================================================================
minimal_css = """
:root {
  --bg: #090A0D;
  --bg-sub: #101218;
  --bg-card: #13161F;
  --bg-card-hover: #181C27;
  --bg-input: #0D0F14;
  
  --border: rgba(255, 255, 255, 0.08);
  --border-gold: rgba(212, 168, 83, 0.25);
  --border-hover: rgba(212, 168, 83, 0.6);
  
  --gold: #D4A853;
  --gold-light: #F3E5C8;
  --gold-dim: rgba(212, 168, 83, 0.12);
  
  --text: #FFFFFF;
  --text-body: #9CA3AF;
  --text-dim: #6B7280;
  
  --radius: 12px;
  --radius-sm: 8px;
  --radius-full: 9999px;
  
  --font-ar: 'Readex Pro', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: var(--font-ar);
}

body {
  background: var(--bg);
  color: var(--text-body);
  direction: rtl;
  min-height: 100vh;
  line-height: 1.8;
  font-size: 0.95rem;
  overflow-x: hidden;
}

/* NAVBAR */
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(9, 10, 13, 0.9);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
  color: var(--text);
  font-weight: 700;
  font-size: 1.1rem;
}

.brand-crown {
  font-size: 1.5rem;
}

.nav-links {
  display: flex;
  gap: 0.4rem;
  list-style: none;
}

.nav-links a {
  color: var(--text-dim);
  text-decoration: none;
  padding: 0.5rem 0.9rem;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 500;
  transition: all 0.2s ease;
}

.nav-links a:hover {
  color: var(--text);
  background: rgba(255, 255, 255, 0.04);
}

.nav-links a.active {
  color: var(--gold);
  background: var(--gold-dim);
  font-weight: 600;
}

/* CONTAINER */
.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 3rem 1.5rem 6rem 1.5rem;
}

/* HERO / HEADER */
.hero {
  text-align: center;
  margin-bottom: 3.5rem;
}

.hero-tag {
  display: inline-block;
  font-size: 0.75rem;
  color: var(--gold);
  background: var(--gold-dim);
  border: 1px solid var(--border-gold);
  padding: 0.25rem 0.8rem;
  border-radius: var(--radius-full);
  margin-bottom: 1rem;
  font-weight: 600;
}

.hero-title {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--text);
  line-height: 1.35;
  margin-bottom: 0.85rem;
  letter-spacing: -0.5px;
}

.hero-desc {
  font-size: 1.05rem;
  color: var(--text-body);
  max-width: 620px;
  margin: 0 auto 1.75rem auto;
  line-height: 1.7;
}

/* AUDIO STRIP MINIMAL */
.audio-bar {
  background: var(--bg-sub);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 0.75rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 3rem;
}

.audio-bar-info {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 0.88rem;
  color: var(--text);
  font-weight: 600;
}

.audio-bar audio {
  height: 32px;
  max-width: 320px;
  outline: none;
}

/* BUTTONS */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.65rem 1.4rem;
  border-radius: var(--radius-sm);
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.btn-primary {
  background: var(--gold);
  color: #000;
}

.btn-primary:hover {
  background: #E5BA69;
  transform: translateY(-1px);
}

.btn-secondary {
  background: transparent;
  color: var(--text);
  border: 1px solid var(--border);
}

.btn-secondary:hover {
  border-color: var(--border-gold);
  color: var(--gold);
  background: var(--gold-dim);
}

/* CARDS */
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
  margin-bottom: 1.25rem;
  transition: all 0.2s ease;
}

.card:hover {
  border-color: var(--border-gold);
  background: var(--bg-card-hover);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.6rem;
}

.card-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text);
}

/* TABS / PILLS */
.tabs {
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
  margin-bottom: 2rem;
  border-bottom: 1px solid var(--border);
  padding-bottom: 0.75rem;
}

.tab-btn {
  background: transparent;
  border: none;
  color: var(--text-dim);
  padding: 0.45rem 1rem;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tab-btn:hover {
  color: var(--text);
}

.tab-btn.active {
  color: var(--gold);
  background: var(--gold-dim);
}

/* CODE / PROMPT BOX */
.code-box {
  background: var(--bg-input);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 1rem 1.25rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: #67E8F9;
  direction: ltr;
  text-align: left;
  white-space: pre-wrap;
  margin: 1rem 0;
  line-height: 1.6;
}

/* TOAST */
.toast {
  position: fixed;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%) translateY(100px);
  background: #111;
  border: 1px solid var(--gold);
  color: var(--gold-light);
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 600;
  opacity: 0;
  transition: all 0.3s ease;
  z-index: 1000;
}

.toast.show {
  transform: translateX(-50%) translateY(0);
  opacity: 1;
}

/* FOOTER */
.footer {
  border-top: 1px solid var(--border);
  padding: 2.5rem 1.5rem;
  text-align: center;
  font-size: 0.82rem;
  color: var(--text-dim);
}

.footer a {
  color: var(--gold);
  text-decoration: none;
}

@media (max-width: 768px) {
  .navbar { flex-direction: column; gap: 0.75rem; padding: 1rem; }
  .nav-links { flex-wrap: wrap; justify-content: center; }
  .hero-title { font-size: 1.7rem; }
  .audio-bar { flex-direction: column; text-align: center; }
}
"""

with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(minimal_css)

print("Generated minimal style.css")
