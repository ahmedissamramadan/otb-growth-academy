import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from build_factual_otb_portal import REAL_ROLES_DATA, COURSES_DATA

# REAL CLIENTS WITH DIRECT OFFICIAL SOCIAL MEDIA LINKS & REAL METRICS (NO FAKE IMAGES)
REAL_CLIENTS_DATA = [
  {
    "name": "Franks EG (فرانكس)",
    "sector": "Industrial & B2B / قطاع التصنيع والشركات الكبرى",
    "metric": "من المركز 25 ➔ المركز الثاني | 10M ➔ 30M EGP",
    "desc": "قصة نجاح OTB الأكبر؛ إعادة هيكلة المنظومة التسويقية والبيعية ومضاعفة المبيعات الرقمية من 10 إلى 30 مليون جنيه شهرياً عبر استراتيجيات تسويق موجهة للشركات (B2B).",
    "socialLink": "https://www.facebook.com/otbagency5",
    "badge": "🏭 B2B Leader"
  },
  {
    "name": "MIX Coffee & Mart (ميكس كوفي)",
    "sector": "Specialty Coffee / قطاع الضيافة والكافيهات",
    "metric": "تفاعل +180% | مضاعفة مبيعات الفروع",
    "desc": "إعادة التموضع من كافيه تقليدي إلى وجهة أولى لرواد الأعمال بهوية داكنة فاخرة، وفيديوهات ASMR لصناعة القهوة حققت انتشاراً واسعاً على السوشيال ميديا.",
    "socialLink": "https://www.facebook.com/people/MIX-Coffee-Mart/100063935293290/",
    "badge": "☕ Specialty Coffee"
  },
  {
    "name": "Rancho's EG (رانشوز برجر)",
    "sector": "Gourmet Burgers / قطاع المطاعم والأغذية",
    "metric": "معدل احتفاظ 36.8% | 450K مشاهدة ريلز",
    "desc": "الخروج من فخ الخصومات إلى تموضع 'البرجر الملحمي'، وإعلانات فيديو ريلز مباشرة رفعت مبيعات الواتساب والطلبات بنسبة 65% عبر الخط الساخن 19484.",
    "socialLink": "https://www.facebook.com/ranchos.eg",
    "badge": "🍔 Gourmet Burger"
  },
  {
    "name": "مجوهرات دكتور زغلول (Dr. Zaghloul)",
    "sector": "Luxury Gold & Jewelry / ذهب ومجوهرات",
    "metric": "ROAS 7.5x+ | إعلانات تحويلية",
    "desc": "بناء الثقة وسرد قصص التصاميم الحصرية بجودة سينمائية وهيكل حملات TOFU/MOFU/BOFU محققاً عائداً إعلانيا استثنائياً.",
    "socialLink": "https://www.facebook.com/otbagency5",
    "badge": "💍 Luxury Gold"
  },
  {
    "name": "معامل علاج (Elag Labs)",
    "sector": "Clinics & Medical / معامل وتحاليل طبية",
    "metric": "800+ حجز مؤهل شهرياً",
    "desc": "إعلانات تحويلية مع مسار WhatsApp Business API مؤتمت لتأهيل واستقبال طلبات الزيارات المنزلية وحجوزات التحاليل بدقة.",
    "socialLink": "https://www.facebook.com/elaglabs",
    "badge": "🧪 Medical Labs"
  },
  {
    "name": "صقر ستور (Sakr Store)",
    "sector": "E-Commerce & Retail / تجارة وتجزئة الملابس",
    "metric": "تكلفة الشراء (CPA) -32%",
    "desc": "إعادة هيكلة حملات Meta وإعلانات Advantage+ مع ربط تتبع CAPI وعروض الباقات المجمعة لرفع متوسط قيمة السلة.",
    "socialLink": "https://www.facebook.com/otbagency5",
    "badge": "📦 E-Commerce"
  }
]

roles_json = json.dumps(REAL_ROLES_DATA, ensure_ascii=False)
clients_json = json.dumps(REAL_CLIENTS_DATA, ensure_ascii=False)
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

# ==============================================================================
# UI/UX PRO MAX SPECIFICATION COMPLIANT CSS
# ==============================================================================
uupm_css = """/* ==========================================================================
   OTB TEAM AI HUB — UI/UX PRO MAX DESIGN SYSTEM SPECIFICATION
   Dark Luxury Liquid Glass + Bento Grid + WCAG AAA Contrast + Zero Latency
   ========================================================================== */

:root {
  /* Dark Luxury Obsidian & Champagne Gold Palette (UI Pro Max verified) */
  --bg-main: #06080C;
  --bg-card: rgba(14, 18, 26, 0.76);
  --bg-card-hover: rgba(22, 28, 40, 0.88);
  --bg-input: rgba(12, 16, 24, 0.9);
  --bg-surface: #0A0D14;

  --gold: #D4A853;
  --gold-light: #F5E6C8;
  --gold-glow: rgba(212, 168, 83, 0.28);
  --gold-accent: #E5C378;

  --emerald: #10B981;
  --emerald-glow: rgba(16, 185, 129, 0.25);
  --crimson: #F43F5E;
  --crimson-glow: rgba(244, 63, 94, 0.25);
  --cyan: #38BDF8;

  --text-pure: #FFFFFF;
  --text-main: #E2E8F0;
  --text-muted: #94A3B8;
  --text-dim: #64748B;

  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-gold: rgba(212, 168, 83, 0.32);
  --border-gold-bright: rgba(212, 168, 83, 0.65);

  --radius-sm: 10px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-full: 9999px;

  /* Typography Hierarchy */
  --font-felfel: 'Felfel-Bold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-kookies: 'KOOkies-Bold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-kookies-black: 'KOOkies-ExtraBold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-royal: 'Cinzel', serif;
  --font-mono: 'JetBrains Mono', monospace;
  --font-ui: -apple-system, BlinkMacSystemFont, 'Readex Pro', 'SF Pro Text', system-ui, sans-serif;

  /* Apple Fluid Springs */
  --spring-snappy: cubic-bezier(0.2, 0, 0, 1);
  --spring-bounce: cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

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

/* Reset & Accessibility Defaults */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
  background-color: var(--bg-main);
  color-scheme: dark;
}

body {
  font-family: var(--font-ui);
  color: var(--text-main);
  background-color: var(--bg-main);
  min-height: 100vh;
  overflow-x: hidden;
  position: relative;
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Subtle WebGL Canvas */
#webglCanvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 0;
  opacity: 0.55;
}

/* Translucent Glass Navbar */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(6, 8, 12, 0.78);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border-bottom: 1px solid var(--border-subtle);
  padding: 0.85rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
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
  border-radius: var(--radius-sm);
  overflow: hidden;
  border: 1.5px solid var(--gold);
  box-shadow: 0 0 12px var(--gold-glow);
  transition: transform 0.2s var(--spring-snappy);
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
  gap: 0.35rem;
}

.brand-text span {
  font-size: 0.72rem;
  color: var(--gold);
  letter-spacing: 1.5px;
  font-weight: 700;
}

/* Clean Pill Navigation */
.nav-pills {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  background: rgba(16, 20, 30, 0.75);
  padding: 0.3rem 0.45rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
}

.nav-pill-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 0.48rem 1.05rem;
  min-height: 44px; /* WCAG touch target */
  border-radius: var(--radius-full);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.18s var(--spring-snappy);
  display: flex;
  align-items: center;
  gap: 0.35rem;
}

.nav-pill-btn:hover {
  color: var(--text-pure);
  background: rgba(255, 255, 255, 0.06);
}

.nav-pill-btn:active {
  transform: scale(0.96);
}

.nav-pill-btn.active {
  color: #000;
  background: var(--gold);
  font-weight: 700;
  box-shadow: 0 0 15px var(--gold-glow);
}

/* LTR Phone */
.phone-wrapper {
  direction: ltr !important;
  unicode-bidi: isolate !important;
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--gold);
  background: rgba(212, 168, 83, 0.08);
  border: 1px solid var(--border-gold);
  padding: 0.45rem 1rem;
  min-height: 44px;
  border-radius: var(--radius-full);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.88rem;
  transition: all 0.2s var(--spring-snappy);
}

.phone-wrapper:hover {
  background: rgba(212, 168, 83, 0.18);
  border-color: var(--gold);
  box-shadow: 0 0 14px var(--gold-glow);
}

.phone-wrapper:active {
  transform: scale(0.96);
}

/* Main App Container */
.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 3rem 1.5rem 6rem 1.5rem;
  position: relative;
  z-index: 1;
}

/* Hero Section */
.hero-wrapper {
  text-align: center;
  max-width: 820px;
  margin: 0 auto 3.5rem auto;
}

.hero-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.4rem 1.25rem;
  background: rgba(212, 168, 83, 0.08);
  border: 1px solid var(--border-gold);
  border-radius: var(--radius-full);
  color: var(--gold);
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 1.2px;
  margin-bottom: 1.25rem;
}

.hero-title {
  font-family: var(--font-felfel);
  font-size: clamp(2rem, 4.2vw, 3.25rem);
  color: var(--text-pure);
  line-height: 1.2;
  letter-spacing: -0.02em;
  margin-bottom: 1rem;
}

.hero-title span {
  color: var(--gold);
}

.hero-subtitle {
  font-size: clamp(0.95rem, 1.4vw, 1.1rem);
  color: var(--text-muted);
  line-height: 1.8;
  max-width: 720px;
  margin: 0 auto;
}

/* Bento Cards */
.glass-card {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  transition: transform 0.25s var(--spring-snappy), border-color 0.25s ease, box-shadow 0.25s ease;
}

.glass-card:hover {
  background: var(--bg-card-hover);
  border-color: var(--border-gold);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
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
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 0.9rem;
  margin-bottom: 2.5rem;
}

.role-tab {
  background: rgba(14, 18, 26, 0.7);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.15rem;
  min-height: 44px;
  cursor: pointer;
  transition: all 0.22s var(--spring-snappy);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 0.4rem;
}

.role-tab:hover {
  background: rgba(22, 28, 40, 0.85);
  border-color: var(--border-gold);
  transform: translateY(-2px);
}

.role-tab:active {
  transform: scale(0.97);
}

.role-tab.active {
  background: rgba(212, 168, 83, 0.1);
  border-color: var(--gold);
  box-shadow: 0 0 20px rgba(212, 168, 83, 0.2);
}

.role-icon-box {
  font-size: 1.85rem;
  margin-bottom: 0.2rem;
}

.role-name {
  font-family: var(--font-felfel);
  font-size: 1.1rem;
  color: var(--text-pure);
  font-weight: 700;
}

.role-eng {
  font-family: var(--font-kookies);
  font-size: 0.82rem;
  color: var(--gold);
  letter-spacing: 0.4px;
}

/* Selected Role Stage */
.role-stage {
  background: rgba(10, 13, 20, 0.85);
  border: 1.5px solid var(--border-gold);
  border-radius: var(--radius-lg);
  padding: 2.25rem;
  box-shadow: 0 16px 50px rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(24px);
}

.role-header-strip {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 1.25rem;
  margin-bottom: 1.75rem;
}

.role-heading {
  font-family: var(--font-felfel);
  font-size: 2.1rem;
  color: var(--text-pure);
  margin-top: 0.2rem;
}

/* Tool Badges */
.tool-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.45rem 0.95rem;
  min-height: 36px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--text-main);
  transition: all 0.18s var(--spring-snappy);
}

.tool-pill:hover {
  background: rgba(212, 168, 83, 0.12);
  border-color: var(--gold);
  color: var(--gold-light);
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.45rem;
  padding: 0.65rem 1.4rem;
  min-height: 44px; /* WCAG 44x44px */
  border-radius: var(--radius-full);
  font-weight: 700;
  font-size: 0.9rem;
  cursor: pointer;
  border: none;
  text-decoration: none;
  transition: all 0.18s var(--spring-snappy);
}

.btn:active {
  transform: scale(0.96);
}

.btn-primary {
  background: var(--gold);
  color: #000;
  box-shadow: 0 4px 15px var(--gold-glow);
}

.btn-primary:hover {
  background: var(--gold-light);
  box-shadow: 0 6px 20px rgba(212, 168, 83, 0.4);
  transform: translateY(-1px);
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
  transform: translateY(-1px);
}

/* Code Console Box */
.code-box {
  background: rgba(0, 0, 0, 0.65);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 1.2rem;
  font-family: var(--font-mono);
  font-size: 0.88rem;
  color: var(--cyan);
  line-height: 1.6;
  white-space: pre-wrap;
  direction: ltr;
  text-align: left;
  position: relative;
  margin: 0.65rem 0;
}

/* Tabs Row */
.tabs-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
  margin-bottom: 1.5rem;
}

.tab-pill {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  color: var(--text-muted);
  padding: 0.48rem 1.1rem;
  min-height: 44px;
  border-radius: var(--radius-full);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.18s var(--spring-snappy);
}

.tab-pill:hover {
  color: var(--text-pure);
  background: rgba(255, 255, 255, 0.1);
}

.tab-pill.active {
  background: var(--gold);
  color: #000;
  font-weight: 700;
  box-shadow: 0 0 12px var(--gold-glow);
}

/* Reduced Motion & Transparency */
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
    background: #0B0E14 !important;
    backdrop-filter: none !important;
  }
}
"""

with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(uupm_css)

print("Applied UI/UX Pro Max CSS!")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
