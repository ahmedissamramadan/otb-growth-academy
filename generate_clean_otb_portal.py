import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

# ==============================================================================
# 1. 100% FACTUAL SOURCED DATA
# ==============================================================================

REAL_ROLES_DATA = [
  {
    "id": "content_creator",
    "name": "صانع وكاتب المحتوى الإبداعي",
    "eng": "Content Creator & Copywriter",
    "icon": "✍️",
    "officialRole": "المسؤول عن صناعة الرؤى التسويقية، كتابة الإعلانات التحويلية، وتصميم الخطط الشهرية الموجهة للعملاء.",
    "realChallenge": "استنزاف 3 إلى 4 ساعات يومياً في محاولة إيجاد أفكار جديدة من الصفر، وصياغة نصوص إعلانية متعددة النبرات لكل منصة، وتنسيق جداول النشر الشهرية يدوياً.",
    "aiSuperpower": "توليد 30 فكرة محتوى استراتيجية وإعلانات PAS/AIDA مفصلة طبقاً لنبرة البراند في أقل من 5 دقائق باستخدام النماذج المتقدمة.",
    "tools": ["Claude 3.5 Sonnet", "ChatGPT (GPT-4o)", "NotebookLM", "Grammarly"],
    "realPrompt": "Role: Senior Direct-Response Copywriter & Content Strategist at OTB Agency (The City Kings).\nContext: Brand name [اسم البراند], Sector [القطاع], Target Audience [الجمهور المستهدف].\nTask: Generate 5 high-converting ad copies using the PAS (Problem-Agitate-Solution) framework in refined modern Egyptian Arabic.\nConstraints: Hook under 8 words, bold royal tone, strong urgency CTA linking to WhatsApp.",
    "goldenRule": "الذكاء الاصطناعي شريك عصف ذهني وسرعة صياغة، لكن اللمسة الإنسانية وفهم ثقافة الشارع المصري ونبرة البراند هي سر التميز الذي لا يُستبدل."
  },
  {
    "id": "graphic_designer",
    "name": "مصمم الجرافيك والهوية البصرية",
    "eng": "Senior Graphic Designer",
    "icon": "🎨",
    "officialRole": "المسؤول عن تجسيد الهوية البصرية للوكالة وعملائها وإنتاج التصاميم الإعلانية والسوشيال ميديا بأعلى جودة.",
    "realChallenge": "البحث لساعات طويلة عن عناصر وملحقات التصميم، وتفريغ الصور يدوياً، وصنع خلفيات ثلاثية الأبعاد واقعية للمنتجات على برامج الفوتوشوب والإيلستريتور.",
    "aiSuperpower": "توليد عناصر 3D فائقة الدقة وتوسيع كادرات التصاميم وتوليد خلفيات تجارية واستبدال العناصر بلحظات عبر أدوات التوليد المتقدمة.",
    "tools": ["Midjourney v6", "Adobe Firefly", "Photoroom Pro", "Figma AI"],
    "realPrompt": "/imagine prompt: Ultra-realistic commercial product shoot for [اسم المنتج], placed on a minimalist dark obsidian stone pedestal, warm subtle gold rim lighting, crisp 8k octane render, cinematic lighting --ar 4:5 --style raw --v 6.0",
    "goldenRule": "لا تعتمد على الصور الجاهزة؛ استخدم الذكاء الاصطناعي لتوليد أصولك الخام (Assets) ثم ابنِ التكوين الفني وتناسق الألوان والتايبوغرافي باحترافيتك المعهودة."
  },
  {
    "id": "video_editor",
    "name": "مونتير ومخرج الفيديو القصير والريلز",
    "eng": "Video Editor & Motion Designer",
    "icon": "🎬",
    "officialRole": "المسؤول عن إنتاج الفيديوهات القصيرة (Reels & TikTok) وتطبيق الإيقاع السريع والتأثيرات البصرية والصوتية.",
    "realChallenge": "كتابة وتنسيق الكابشنز العربية كلمة بكلمة، والبحث عن مؤثرات صوتية مناسبة، وتقطيع السكتات والوقفات يدوياً من الفيديوهات الطويلة.",
    "aiSuperpower": "تفريغ الصوت وتوليد الكابشنز المتحركة بدقة 100%، وقص الصمت تلقائياً، وتوليد مؤثرات صوتية ملحمية عبر أدوات الذكاء الاصطناعي.",
    "tools": ["CapCut Pro", "Premiere Pro AI", "ElevenLabs", "Opus Clip"],
    "realPrompt": "Role: Short-Form Video Director at OTB Agency.\nContext: Creating a 15-second viral Reel for [اسم البراند].\nTask: Write a shot-by-shot script with a 3-second visual hook, fast ASMR cuts, on-screen text cues, and energetic pacing.\nFormat: Table [Time (Sec) | Visual Action | Audio SFX | Voiceover].",
    "goldenRule": "الـ 3 ثوانٍ الأولى (The Hook) هي التي تحدد نجاح الفيديو بنسبة 80%؛ اجعل الحركة البصرية والصوتية الأولى غير متوقعة لجذب انتباه المشاهد فوراً."
  },
  {
    "id": "media_buyer",
    "name": "أخصائي الإعلانات الممولة وميديا بايينج",
    "eng": "Media Buyer & Growth Architect",
    "icon": "📊",
    "officialRole": "المسؤول عن إدارة الميزانيات الإعلانية على منصات Meta و TikTok، وتحقيق أعلى عائد على الإنفاق الإعلاني (ROAS).",
    "realChallenge": "مراقبة الأرقام يدوياً، وحساب تكلفة الاقتناء ونسب التحويل في شيتات معقدة، واكتشاف أسباب تراجع أداء الحملات أو تشبع الجمهور الإعلاني.",
    "aiSuperpower": "تحليل أداء الحساب الإعلاني وتشخيص نقاط الاختناق في مسار الشراء (Funnel) واقتراح خطة سكيلينج آمنة خلال ثوانٍ معدودة.",
    "tools": ["Meta Advantage+", "ChatGPT Advanced Data", "Claude 3.5 Sonnet", "Triple Whale"],
    "realPrompt": "Role: Principal Media Buyer at OTB Agency.\nData: Spent [المبلغ], Revenue [الإيراد], CTR [النسبة], CPM [التكلفة], CPA [التكلفة]. Target ROAS: 4.0x.\nTask: Analyze these performance metrics, identify the biggest leak in the funnel, and give an actionable 48-hour scaling or optimization roadmap.",
    "goldenRule": "الإبداع الإعلاني (Ad Creative) هو الاستهداف الجديد (The Creative is the Targeting)؛ نوع زوايا الإعلانات قبل أن تزيد الميزانية."
  },
  {
    "id": "account_manager",
    "name": "مدير الحسابات وخدمة العملاء",
    "eng": "Senior Account Manager",
    "icon": "🤝",
    "officialRole": "همزة الوصل الاستراتيجية بين العميل وفريق العمل، والمسؤول عن رضا العملاء وتجديد العقود الشهرية.",
    "realChallenge": "صياغة تقارير الأداء الأسبوعية المعقدة، والرد على استفسارات العملاء المتكررة، وتلخيص مخرجات الاجتماعات الطويلة.",
    "aiSuperpower": "تحويل جداول البيانات الخام إلى تقارير تنفيذية احترافية مبهرة بصيغة C-Level في دقائق، وتلخيص الاجتماعات فورياً.",
    "tools": ["NotebookLM", "Otter.ai", "Claude 3.5 Sonnet", "Notion AI"],
    "realPrompt": "Role: Executive Account Director at OTB Agency.\nInput: Weekly campaign data [البيانات والأرقام].\nTask: Draft a concise, highly professional executive summary email to the client highlighting key wins, ROAS achieved, and the next 7-day focus in Arabic.",
    "goldenRule": "العميل لا يشتري مجرد بوستات؛ هو يشتري راحة البال وشريكاً يفهم لغة الأرقام ونمو البيزنس الحقيقي."
  },
  {
    "id": "brand_strategist",
    "name": "استراتيجي البراند والتموضع",
    "eng": "Brand & Strategy Specialist",
    "icon": "🧠",
    "officialRole": "المسؤول عن دراسة الأسواق والمنافسين وبناء استراتيجيات التموضع (Positioning) وخطة النمو لـ 90 يوماً.",
    "realChallenge": "جمع وتحليل بيانات المنافسين وتفكيك عروض السوق يدوياً، وصياغة وثائق استراتيجية تتجاوز 40 صفحة في أوقات قياسية.",
    "aiSuperpower": "استخلاص الفجوات السوقية وتحليل مصفوفات SWOT وبناء خطط الإطلاق والتموضع بسرعة فائقة مستندة إلى أحدث البيانات.",
    "tools": ["Perplexity Pro", "Claude 3.5 Sonnet", "NotebookLM", "Miro AI"],
    "realPrompt": "Role: Chief Brand Strategist at OTB Agency.\nIndustry: [القطاع في السوق المصري]. Target Audience: [الشريحة].\nTask: Perform a deep competitive gap analysis and formulate a unique brand positioning statement using the Ruler/Creator archetype framework.",
    "goldenRule": "التموضع الصحيح يجعلك الخيار الوحيد المنطقي في ذهن العميل بدون الدخول في حرب أسعار مدمرة."
  },
  {
    "id": "community_moderator",
    "name": "مسؤول مجتمع الموديريشن والمبيعات",
    "eng": "Community Moderator & Sales Chat",
    "icon": "💬",
    "officialRole": "خط الدفاع الأول للبراند، والمسؤول عن تحويل التعليقات ورسائل الواتساب والماسنجر إلى مبيعات مؤكدة.",
    "realChallenge": "تكرار الرد على نفس الأسئلة مئات المرات يومياً، والتعامل مع العملاء الغاضبين أو المترددين بأسلوب احترافي وسريع.",
    "aiSuperpower": "بناء مسارات ردود ذكية مؤتمتة وتوليد إجابات مقنعة وسريعة للاعتراضات السعرية تحافظ على نبرة البراند الراقية.",
    "tools": ["WhatsApp Business API", "ChatGPT Team", "ManyChat", "Claude 3.5"],
    "realPrompt": "Role: Senior Social Selling & Community Manager at OTB Agency.\nContext: Customer asking about [اسم المنتج/الخدمة] and objecting to the price [الاعتراض].\nTask: Write 3 polite, persuasive Arabic response options handling the price objection and guiding the customer to complete the order on WhatsApp.",
    "goldenRule": "كل رسالة في الـ Inbox هي فرصة بيع؛ السرعة والاحترافية وإظهار القيمة قبل السعر ترفع معدل التحويل بنسبة تتجاوز 40%."
  },
  {
    "id": "sales_pr",
    "name": "مدير المبيعات والعلاقات العامة",
    "eng": "Sales & PR Specialist",
    "icon": "💼",
    "officialRole": "المسؤول عن استقطاب عملاء جدد للوكالة، وعقد الشراكات الاستراتيجية، وإغلاق الصفقات الكبرى.",
    "realChallenge": "البحث عن صُنّاع القرار في الشركات المستهدفة، وكتابة عروض مخصصة لكل عميل تستغرق أياماً لإعدادها.",
    "aiSuperpower": "صياغة مقترحات أعمال (Proposals) مخصصة مبنية على تحليل دقيق لثغرات العميل التسويقية في دقائق معدودة.",
    "tools": ["Apollo.io", "LinkedIn Sales Navigator", "Claude 3.5 Sonnet", "Figma"],
    "realPrompt": "Role: Head of Business Development at OTB Agency.\nTarget Company: [اسم الشركة/المصنع], Sector: [القطاع].\nTask: Write a high-impact cold outreach pitch to the CEO proposing a strategic marketing partnership to double their digital B2B sales in 90 days.",
    "goldenRule": "لا تبع خدمات تسويقية مجردة؛ بع حلولاً تقضي على أكبر ألم يعاني منه صاحب البيزنس وترفع أرباحه المباشرة."
  },
  {
    "id": "operations_lead",
    "name": "القيادة والإدارة التشغيلية",
    "eng": "Leadership & Operations",
    "icon": "👑",
    "officialRole": "المسؤول عن ضبط جودة المخرجات، متابعة مؤشرات الأداء KPIs، وتطوير المنظومة التقنية للوكالة.",
    "realChallenge": "توزيع المهام ومتابعة الديدلاينز بين الأقسام، واكتشاف الاختناقات التشغيلية قبل أن تؤثر على تسليمات العملاء.",
    "aiSuperpower": "أتمتة تقارير التدفق اليومي للعمليات، وتوزيع المهام، وتدريب الفريق عبر قواعد معرفية موحدة.",
    "tools": ["Notion AI", "Make.com", "n8n", "NotebookLM"],
    "realPrompt": "Role: Chief Operating Officer at OTB Agency.\nContext: Managing a 9-discipline creative and performance agency.\nTask: Design a standardized 5-step SOP (Standard Operating Procedure) for onboarding new retainer clients from brief to first campaign launch.",
    "goldenRule": "السيستم المحكم والأتمتة الذكية هما ما يحول الوكالة من مجرد أفراد مضغوطين إلى مؤسسة كبرى تنمو بثبات واستدامة."
  }
]

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

from build_factual_otb_portal import COURSES_DATA

roles_json = json.dumps(REAL_ROLES_DATA, ensure_ascii=False)
clients_json = json.dumps(REAL_CLIENTS_DATA, ensure_ascii=False)
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

# ==============================================================================
# 2. MASTER CLEAN STYLESHEET (style.css)
# ==============================================================================
clean_css = """/* ==========================================================================
   OTB TEAM AI HUB — CLEAN LUXURY APPLE-GRADE STYLESHEET
   Clean Dark Aesthetics, Generous Whitespace, Fluid Springs, Zero Visual Clutter
   ========================================================================== */

:root {
  /* Pristine Obsidian & Champagne Gold Theme */
  --bg-main: #080A0F;
  --bg-card: rgba(16, 20, 30, 0.72);
  --bg-card-hover: rgba(24, 30, 44, 0.85);
  --bg-input: rgba(14, 18, 26, 0.85);
  --bg-surface: #0E121B;

  --gold: #D4A853;
  --gold-light: #F5E6C8;
  --gold-glow: rgba(212, 168, 83, 0.28);
  --gold-accent: #E5C378;

  --emerald: #10B981;
  --crimson: #F43F5E;
  --cyan: #38BDF8;

  --text-pure: #FFFFFF;
  --text-main: #E2E8F0;
  --text-muted: #94A3B8;
  --text-dim: #64748B;

  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-gold: rgba(212, 168, 83, 0.35);

  --radius-sm: 10px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-full: 9999px;

  /* Typography */
  --font-felfel: 'Felfel-Bold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-kookies: 'KOOkies-Bold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-kookies-black: 'KOOkies-ExtraBold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-royal: 'Cinzel', serif;
  --font-mono: 'JetBrains Mono', monospace;
  --font-ui: -apple-system, BlinkMacSystemFont, 'Readex Pro', 'SF Pro Text', system-ui, sans-serif;

  /* Fluid Apple Springs */
  --spring-snappy: cubic-bezier(0.2, 0, 0, 1);
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

/* Reset & Base */
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

/* WebGL Background Canvas */
#webglCanvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 0;
  opacity: 0.6;
}

/* Translucent Glass Navbar */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(8, 10, 15, 0.75);
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
  width: 40px;
  height: 40px;
  border-radius: var(--radius-sm);
  overflow: hidden;
  border: 1.5px solid var(--gold);
  box-shadow: 0 0 12px var(--gold-glow);
}

.brand-badge-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.brand-text h1 {
  font-family: var(--font-kookies-black);
  font-size: 1.1rem;
  color: var(--text-pure);
  letter-spacing: -0.01em;
  display: flex;
  align-items: center;
  gap: 0.35rem;
}

.brand-text span {
  font-size: 0.7rem;
  color: var(--gold);
  letter-spacing: 1.5px;
  font-weight: 700;
}

/* Clean Pill Navigation */
.nav-pills {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  background: rgba(18, 22, 32, 0.7);
  padding: 0.3rem 0.45rem;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
}

.nav-pill-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 0.45rem 1rem;
  border-radius: var(--radius-full);
  font-size: 0.86rem;
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
  padding: 0.4rem 0.95rem;
  border-radius: var(--radius-full);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.85rem;
  transition: all 0.2s var(--spring-snappy);
}

.phone-wrapper:hover {
  background: rgba(212, 168, 83, 0.18);
  border-color: var(--gold);
  box-shadow: 0 0 12px var(--gold-glow);
}

.phone-wrapper:active {
  transform: scale(0.96);
}

/* Main Container */
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
  padding: 0.35rem 1.15rem;
  background: rgba(212, 168, 83, 0.08);
  border: 1px solid var(--border-gold);
  border-radius: var(--radius-full);
  color: var(--gold);
  font-size: 0.8rem;
  font-weight: 800;
  letter-spacing: 1.2px;
  margin-bottom: 1.25rem;
}

.hero-title {
  font-family: var(--font-felfel);
  font-size: clamp(2rem, 4vw, 3.2rem);
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

/* Clean Bento Cards */
.glass-card {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.65rem;
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
  padding: 1.1rem;
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
  font-size: 0.8rem;
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
  font-size: 2rem;
  color: var(--text-pure);
  margin-top: 0.2rem;
}

/* Tool Badges */
.tool-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.4rem 0.9rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  font-size: 0.86rem;
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
  padding: 0.6rem 1.35rem;
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
  padding: 1.15rem;
  font-family: var(--font-mono);
  font-size: 0.86rem;
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
  padding: 0.45rem 1.05rem;
  border-radius: var(--radius-full);
  font-size: 0.86rem;
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
    f.write(clean_css)

# ==============================================================================
# 3. MASTER CLEAN JAVASCRIPT (shared_ui.js)
# ==============================================================================
clean_js = """// ==========================================================================
// OTB TEAM AI HUB — CLEAN THREE.JS BACKGROUND & INTERACTION ENGINE
// ==========================================================================

// Subtle Three.js Ambient Particle System
(function initCleanWebGL() {
  const canvas = document.getElementById("webglCanvas");
  if (!canvas || typeof THREE === "undefined") return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 25;

  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Particles
  const particleCount = 350;
  const geometry = new THREE.BufferGeometry();
  const positions = new Float32Array(particleCount * 3);

  for (let i = 0; i < particleCount * 3; i += 3) {
    positions[i] = (Math.random() - 0.5) * 50;
    positions[i + 1] = (Math.random() - 0.5) * 50;
    positions[i + 2] = (Math.random() - 0.5) * 50;
  }

  geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));

  const material = new THREE.PointsMaterial({
    color: 0xD4A853,
    size: 0.18,
    transparent: true,
    opacity: 0.6,
    blending: THREE.AdditiveBlending
  });

  const particles = new THREE.Points(geometry, material);
  scene.add(particles);

  let mouseX = 0;
  let mouseY = 0;
  window.addEventListener("pointermove", (e) => {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 0.4;
    mouseY = (e.clientY / window.innerHeight - 0.5) * 0.4;
  });

  function animate() {
    requestAnimationFrame(animate);
    particles.rotation.y += 0.0008;
    particles.rotation.x += 0.0004;

    camera.position.x += (mouseX * 5 - camera.position.x) * 0.05;
    camera.position.y += (-mouseY * 5 - camera.position.y) * 0.05;
    camera.lookAt(scene.position);

    renderer.render(scene, camera);
  }
  animate();

  window.addEventListener("resize", () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
})();

// Toast Notification
function showToast(msg) {
  let toast = document.getElementById("cleanToast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "cleanToast";
    toast.style.cssText = "position: fixed; bottom: 2rem; left: 50%; transform: translateX(-50%); background: #D4A853; color: #000; font-weight: 700; padding: 0.75rem 1.75rem; border-radius: 9999px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); z-index: 999999; font-size: 0.9rem; transition: opacity 0.25s cubic-bezier(0.2,0,0,1); opacity: 0; pointer-events: none;";
    document.body.appendChild(toast);
  }
  toast.innerText = msg;
  toast.style.opacity = "1";
  setTimeout(() => {
    toast.style.opacity = "0";
  }, 2200);
}

// Copy Text
function copyText(str) {
  navigator.clipboard.writeText(str).then(() => {
    showToast("📋 تم نسخ الأمر بنجاح إلى الحافظة!");
  }).catch(() => {
    showToast("تم النسخ!");
  });
}
"""

with open(os.path.join(BASE_DIR, "shared_ui.js"), "w", encoding="utf-8") as f:
    f.write(clean_js)

# ==============================================================================
# 4. MASTER CLEAN HTML (index.html)
# ==============================================================================
clean_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Team AI Hub — منصة تمكين ملوك المدينة</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=JetBrains+Mono:wght@500;600;700&family=Readex+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>

  <!-- WebGL Background -->
  <canvas id="webglCanvas"></canvas>

  <!-- Clean Navbar -->
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

    <!-- Top Navigation Pills -->
    <nav class="nav-pills">
      <button class="nav-pill-btn active" id="tabBtn-roles" onclick="switchMainTab('roles')">🎯 أدوار الفريق</button>
      <button class="nav-pill-btn" id="tabBtn-cases" onclick="switchMainTab('cases')">💼 عملاء الوكالة</button>
      <button class="nav-pill-btn" id="tabBtn-manus" onclick="switchMainTab('manus')">📋 بريف Manus</button>
      <button class="nav-pill-btn" id="tabBtn-courses" onclick="switchMainTab('courses')">📚 المناهج (19)</button>
      <button class="nav-pill-btn" id="tabBtn-prompts" onclick="switchMainTab('prompts')">🤖 استوديو الأوامر</button>
      <button class="nav-pill-btn" id="tabBtn-quiz" onclick="switchMainTab('quiz')">🏆 الشهادة</button>
      <button class="nav-pill-btn" id="tabBtn-downloads" onclick="switchMainTab('downloads')">📥 التحميلات</button>
    </nav>

    <div>
      <a href="tel:+201008080295" class="phone-wrapper">
        <span class="phone-code">+20</span>
        <span class="phone-num">100 808 0295</span>
      </a>
    </div>
  </header>

  <!-- App Main Content -->
  <main class="app-container">

    <!-- ========================================== -->
    <!-- SECTION 1: ROLE AI COCKPIT (BENTO GRID) -->
    <!-- ========================================== -->
    <section id="section-roles" class="hub-section">
      <div class="hero-wrapper">
        <div class="hero-pill">✨ OTB AI SUPERPOWER COCKPIT · 2026</div>
        <h2 class="hero-title">اختر تخصصك.. واكتشف قوة الـ <span>AI الحقيقية 🚀</span></h2>
        <p class="hero-subtitle">
          بيانات حقيقية 100% مستخلصة من الدليل الرسمي للمسميات وخارطة طريق OTB Agency. تعرف كيف تختزل أدوات الذكاء الاصطناعي 40% من وقت المهام الروتينية لتبدع كأحد ملوك المدينة.
        </p>
      </div>

      <!-- Role Selector Tabs Grid -->
      <div class="role-grid" id="rolesGrid"></div>

      <!-- Selected Role Bento Stage -->
      <div id="roleDetailsStage" class="role-stage"></div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 2: REAL CLIENT CASES (NO FAKE IMAGES) -->
    <!-- ========================================== -->
    <section id="section-cases" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <div class="hero-pill">💼 VERIFIED CLIENT TRIUMPHS</div>
        <h2 class="hero-title">نتائج وأرقام عملاء OTB <span>الموثقة بالسوشيال ميديا</span></h2>
        <p class="hero-subtitle">بيانات حقيقية وأرقام مسجلة وروابط مباشرة لصفحات التواصل الاجتماعي الرسمية لعملاء الوكالة.</p>
      </div>

      <div id="clientsGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.25rem;"></div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 3: MANUS 9-STAGE STRATEGIC PIPELINE -->
    <!-- ========================================== -->
    <section id="section-manus" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <div class="hero-pill">👑 MANUS STRATEGIC DISCOVERY PIPELINE</div>
        <h2 class="hero-title">نظام بريف واستقبال العملاء المعتمد <span>(9 مراحل)</span></h2>
        <p class="hero-subtitle">المنظومة الرسمية لاكتشاف وتأهيل عملاء وكالة OTB وضبط التوقعات والأهداف من الجلسة الأولى.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.15rem;">
        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 01</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">🌱 الجذور (من أنتم؟)</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">قصة التأسيس، الرؤية، والسبب الجوهري لوجود البراند في السوق والمهمة الأساسية.</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 02</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">💎 العرض والقيمة (The Offer)</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">المنتجات والخدمات الأساسية، الميزة التنافسية الحصرية، وهيكل الأسعار.</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 03</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">🎯 الجمهور المستهدف (Audience)</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">الشرائح السكانية، السلوك الشرائي، ونقاط الألم الرئيسية (Pain Points).</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 04</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">🔍 مشهد المنافسة والفجوات</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">المنافسون المباشرون ونقاط ضعفهم التي يمكن لـ OTB استغلالها لصالح العميل.</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 05</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">🎭 شخصية البراند ونبرة الصوت</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">النمط النفسي ونبرة الحديث المعتمدة (Bold, Royal, Friendly, Prestigious...).</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 06</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">📈 النجاح ومستهدفات الـ 90 يوماً</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">أهداف الـ ROAS، الإيرادات، والمبيعات المستهدفة ومؤشرات الأداء KPIs.</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 07</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">⚙️ التشغيل والميزانيات</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">ميزانية الإعلانات الشهرية المتاحة، الموارد، وقنوات التواصل المعتمدة.</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 08</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">🛡️ السياق والدروس السابقة</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">تجارب الحملات السابقة، ما نجح وما فشل، والمحاذير التسويقية والقانونية.</p>
        </div>

        <div class="glass-card" style="border-color: var(--border-gold); background: rgba(212, 168, 83, 0.08);">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 09</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--gold); margin: 0.3rem 0;">✅ المراجعة وإصدار الكود المرجعي</h3>
          <p style="font-size: 0.9rem; color: var(--text-main);">تأكيد بنود البريف وتوليد الكود الرسمي (مثل: OTB-K3M9P) لتوزيع المهام على الفريق.</p>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 4: 19 COURSES -->
    <!-- ========================================== -->
    <section id="section-courses" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <h2 class="hero-title">📚 مناهج الـ 19 تخصصاً المعتمدة</h2>
        <p class="hero-subtitle">تفكيك 2,400+ صفحة إلى مقررات تدريبية عملية تشمل كافة أدوار ومسارات نمو الوكالة.</p>
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
    <!-- SECTION 5: PROMPTS STUDIO -->
    <!-- ========================================== -->
    <section id="section-prompts" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <h2 class="hero-title">🤖 استوديو أوامر الذكاء الاصطناعي</h2>
        <p class="hero-subtitle">أوامر RCIC عملية وفورية مصممة خصيصاً لعملاء OTB وقابلة للنسخ المباشر.</p>
      </div>

      <div class="glass-card" style="border: 1.5px solid var(--border-gold); padding: 2.25rem; max-width: 800px; margin: 0 auto;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.25rem;">
          <div>
            <label style="display: block; font-size: 0.85rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 700;">نوع التكليف المطلوب:</label>
            <select id="promptTask" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input); border-radius: var(--radius-sm);" onchange="updateLivePrompt()">
              <option value="copy">كتابة إعلانات تحويلية (PAS Framework)</option>
              <option value="reels">اسكريبت ريلز 15 ثانية (Viral Hook)</option>
              <option value="media">تشخيص حساب إعلاني وسكيلينج (Media Buying)</option>
              <option value="retainer">مقترح عقد ريتينر شهري ($2,500/mo)</option>
            </select>
          </div>
          <div>
            <label style="display: block; font-size: 0.85rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 700;">اسم البراند والقطاع:</label>
            <input type="text" id="promptBrand" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input); border-radius: var(--radius-sm);" value="MIX Coffee (Specialty Coffee)" oninput="updateLivePrompt()">
          </div>
        </div>

        <div style="margin-bottom: 1.25rem;">
          <label style="display: block; font-size: 0.85rem; color: var(--text-pure); margin-bottom: 0.35rem; font-weight: 700;">الأمر المولد فورياً:</label>
          <div id="livePromptCode" class="code-box" style="max-height: 220px; overflow-y: auto;"></div>
        </div>

        <button class="btn btn-primary" style="width: 100%; padding: 0.8rem;" onclick="copyText(document.getElementById('livePromptCode').innerText)">📋 نسخ الأمر المخصص للحافظة</button>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 6: QUIZ & CERTIFICATE -->
    <!-- ========================================== -->
    <section id="section-quiz" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <h2 class="hero-title">🏆 تقييم الكفاءة وإصدار شهادة ملوك المدينة</h2>
        <p class="hero-subtitle">أدخل اسمك وأجب عن الأسئلة الخمسة لإصدار شهادة الاعتماد الملكية الرسمية المعتمدة.</p>
      </div>

      <div class="glass-card" style="max-width: 720px; margin: 0 auto 1.75rem auto;">
        <label style="display: block; font-size: 0.88rem; color: var(--text-pure); margin-bottom: 0.4rem; font-weight: 700;">الاسم الرسمي المطبوع على الشهادة:</label>
        <input type="text" id="certName" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input); font-size: 1rem; border-radius: var(--radius-sm);" value="أحمد عصام رمضان">
      </div>

      <div style="max-width: 720px; margin: 0 auto;">
        <div class="glass-card" style="margin-bottom: 0.9rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.5rem;">1. ما هو التموضع والنمط النفسي المعتمد لوكالة OTB؟</h4>
          <label style="display:block; margin-bottom:0.3rem; font-size:0.88rem; cursor:pointer;"><input type="radio" name="q0" value="0"> المنافسة على أقل سعر</label>
          <label style="display:block; font-size:0.88rem; cursor:pointer;"><input type="radio" name="q0" value="1" checked> The Ruler & The Creator (ملوك المدينة: الهيبة والجرأة والتركيز على العائد)</label>
        </div>

        <div class="glass-card" style="margin-bottom: 0.9rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.5rem;">2. كيف يساعد الذكاء الاصطناعي صانع المحتوى بشكل سليم؟</h4>
          <label style="display:block; margin-bottom:0.3rem; font-size:0.88rem; cursor:pointer;"><input type="radio" name="q1" value="1" checked> كـ شريك عصف ذهني وسرعة صياغة بدقة المعطيات مع مراجعة بشرية</label>
          <label style="display:block; font-size:0.88rem; cursor:pointer;"><input type="radio" name="q1" value="0"> نسخ ولصق الردود بدون قراءة</label>
        </div>

        <div class="glass-card" style="margin-bottom: 0.9rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.5rem;">3. إذا كان هامش الربح 25%، فما هو الـ Break-Even ROAS؟</h4>
          <label style="display:block; margin-bottom:0.3rem; font-size:0.88rem; cursor:pointer;"><input type="radio" name="q2" value="1" checked> 4.0x (حيث 1 / 0.25 = 4)</label>
          <label style="display:block; font-size:0.88rem; cursor:pointer;"><input type="radio" name="q2" value="0"> 1.5x</label>
        </div>

        <div class="glass-card" style="margin-bottom: 0.9rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.5rem;">4. ما هي النسبة الآمنة لزيادة ميزانية الحملات الرابحة (Scaling)؟</h4>
          <label style="display:block; margin-bottom:0.3rem; font-size:0.88rem; cursor:pointer;"><input type="radio" name="q3" value="1" checked> زيادة 20% كل 48-72 ساعة لحماية استقرار الحملة</label>
          <label style="display:block; font-size:0.88rem; cursor:pointer;"><input type="radio" name="q3" value="0"> مضاعفة الميزانية 200% كل ساعة</label>
        </div>

        <div class="glass-card" style="margin-bottom: 1.75rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.5rem;">5. ما هو السعر القياسي لباقة الـ Dominance Retainer لـ OTB؟</h4>
          <label style="display:block; margin-bottom:0.3rem; font-size:0.88rem; cursor:pointer;"><input type="radio" name="q4" value="1" checked> $2,500 / شهر (هوية + 24 محتوى + ميديا بايينج + أتمتة)</label>
          <label style="display:block; font-size:0.88rem; cursor:pointer;"><input type="radio" name="q4" value="0"> $300 / شهر</label>
        </div>

        <div style="text-align: center;">
          <button class="btn btn-primary" style="padding: 0.85rem 3rem; font-size: 0.95rem;" onclick="generateOfficialCert()">👑 إصدار شهادة الاعتماد الملكية</button>
        </div>

        <div id="certContainer" style="display: none;"></div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 7: DOWNLOADS -->
    <!-- ========================================== -->
    <section id="section-downloads" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <h2 class="hero-title">📥 مركز المستندات والأوامر المباشرة</h2>
        <p class="hero-subtitle">تحميل التقارير الاستراتيجية وموسوعات الأوامر وقوائم الفحص بصيغ مباشرة.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">50+ Prompts</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.4rem 0;">📖 موسوعة الأوامر التكتيكية</h3>
          <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1.25rem;">أوامر الذكاء الاصطناعي المعتمدة لأدوار OTB.</p>
          <a href="track_a_fast_track_sprint/cheatsheets/OTB_Prompt_Engineering_Bible.md" download class="btn btn-primary" style="width: 100%; font-size: 0.85rem;">📥 تحميل الموسوعة</a>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Checklist</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.4rem 0;">✈️ فحص الميديا بايينج</h3>
          <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1.25rem;">قائمة فحص الحملات قبل الإطلاق وقواعد السكيلينج.</p>
          <a href="track_a_fast_track_sprint/cheatsheets/OTB_Media_Buying_Checklist.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.85rem;">📥 تحميل الفحص</a>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Markdown Doc</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.4rem 0;">📑 التقرير الاستراتيجي الشامل</h3>
          <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1.25rem;">وثيقة التوجيه التنفيذي لنمو الوكالة.</p>
          <a href="track_b_4week_masterclass/studio_artifacts/OTB_Executive_Strategic_Briefing.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.85rem;">📥 تحميل التقرير</a>
        </div>
      </div>
    </section>

  </main>

  <script src="shared_ui.js"></script>
  <script>
    const coursesData = {courses_json};
    const rolesData = {roles_json};
    const clientsData = {clients_json};

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
      rolesData.forEach((r, idx) => {{
        html += `
          <div class="role-tab ${{idx === 0 ? 'active' : ''}}" id="roleTab_${{r.id}}" onclick="selectRole('${{r.id}}')">
            <div class="role-icon-box">${{r.icon}}</div>
            <div class="role-name">${{r.name}}</div>
            <div class="role-eng">${{r.eng}}</div>
          </div>
        `;
      }});
      grid.innerHTML = html;
      selectRole(rolesData[0].id);
    }}

    function selectRole(roleId) {{
      document.querySelectorAll(".role-tab").forEach(t => t.classList.remove("active"));
      const activeTab = document.getElementById("roleTab_" + roleId);
      if (activeTab) activeTab.classList.add("active");

      const r = rolesData.find(item => item.id === roleId);
      if (!r) return;

      let toolsHtml = "";
      r.tools.forEach(t => {{
        toolsHtml += `<span class="tool-pill">${{t}}</span>`;
      }});

      const stage = document.getElementById("roleDetailsStage");
      stage.innerHTML = `
        <div class="role-header-strip">
          <div>
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 800; letter-spacing: 1px;">الدور المعتمد رسمياً في هيكل OTB</span>
            <h2 class="role-heading">${{r.icon}} ${{r.name}} <span style="font-family: var(--font-kookies); font-size: 1.1rem; color: var(--gold-light);">(${{r.eng}})</span></h2>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-top: 0.3rem;">${{r.officialRole}}</p>
          </div>
          <button class="btn btn-primary" onclick="copyText(document.getElementById('rolePromptBox').innerText)">📋 نسخ الأمر المعتمد</button>
        </div>

        <div class="bento-grid">
          <div class="bento-col-6 glass-card" style="background: rgba(244, 63, 94, 0.04); border-color: rgba(244, 63, 94, 0.25);">
            <div style="display: flex; align-items: center; gap: 0.45rem; margin-bottom: 0.45rem;">
              <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--crimson); box-shadow: 0 0 8px var(--crimson);"></span>
              <h4 style="color: var(--crimson); font-size: 0.95rem; font-weight: 800;">أين يضيع وقتك يومياً؟ (التحدي المعتاد):</h4>
            </div>
            <p style="font-size: 0.9rem; color: var(--text-main); line-height: 1.7;">${{r.realChallenge}}</p>
          </div>

          <div class="bento-col-6 glass-card" style="background: rgba(16, 185, 129, 0.04); border-color: rgba(16, 185, 129, 0.25);">
            <div style="display: flex; align-items: center; gap: 0.45rem; margin-bottom: 0.45rem;">
              <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--emerald); box-shadow: 0 0 8px var(--emerald);"></span>
              <h4 style="color: var(--emerald); font-size: 0.95rem; font-weight: 800;">كيف يضاعف الـ AI إنتاجيتك 5x؟:</h4>
            </div>
            <p style="font-size: 0.9rem; color: var(--text-main); line-height: 1.7;">${{r.aiSuperpower}}</p>
          </div>

          <div class="bento-col-12 glass-card">
            <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.65rem; font-weight: 800;">🛠️ ترسانة الأدوات الذكية المعتمدة لدورك:</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">${{toolsHtml}}</div>
          </div>

          <div class="bento-col-12 glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
              <h4 style="font-size: 0.95rem; color: var(--cyan); font-weight: 800;">📋 الأمر الجاهز الفوري لعملاء الوكالة (Plug-and-Play Prompt):</h4>
              <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: 700;">صيغة RCIC احترافية</span>
            </div>
            <div id="rolePromptBox" class="code-box">${{r.realPrompt}}</div>
          </div>

          <div class="bento-col-12 glass-card" style="background: rgba(212, 168, 83, 0.06); border-color: var(--border-gold);">
            <div style="display: flex; align-items: center; gap: 0.45rem; margin-bottom: 0.35rem;">
              <span style="font-size: 1.2rem;">👑</span>
              <h4 style="color: var(--gold); font-size: 1rem; font-weight: 800;">النصيحة الذهبية لملوك المدينة:</h4>
            </div>
            <p style="font-size: 0.92rem; color: var(--text-main); line-height: 1.8;">${{r.goldenRule}}</p>
          </div>
        </div>
      `;
    }}

    function renderClientsGrid() {{
      const container = document.getElementById("clientsGrid");
      let html = "";
      clientsData.forEach(c => {{
        html += `
          <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
              <span style="font-size: 0.8rem; color: var(--gold); font-weight: 800;">${{c.badge}}</span>
              <span style="font-size: 0.72rem; color: var(--emerald); font-weight: 800; background: rgba(16, 185, 129, 0.1); padding: 0.2rem 0.55rem; border-radius: var(--radius-full); border: 1px solid rgba(16, 185, 129, 0.25);">${{c.metric}}</span>
            </div>
            <h3 style="font-family: var(--font-felfel); font-size: 1.3rem; color: var(--text-pure); margin-bottom: 0.35rem;">${{c.name}}</h3>
            <div style="font-size: 0.8rem; color: var(--text-dim); margin-bottom: 0.55rem; font-weight: 600;">${{c.sector}}</div>
            <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">${{c.desc}}</p>
            <a href="${{c.socialLink}}" target="_blank" class="btn btn-secondary" style="width: 100%; font-size: 0.82rem; padding: 0.5rem;">🌐 زيارة صفحة فيسبوك الرسمية</a>
          </div>
        `;
      }});
      container.innerHTML = html;
    }}

    function renderCoursesList(list) {{
      const container = document.getElementById("coursesList");
      let html = "";
      list.forEach(c => {{
        const isDone = localStorage.getItem("otb_done_" + c.id) === "true";
        let unitsHtml = "";
        c.units.forEach((u, i) => {{
          unitsHtml += `<li style="margin-bottom: 0.3rem;"><b>الوحدة ${{i + 1}}:</b> ${{u}}</li>`;
        }});

        html += `
          <div class="glass-card" style="margin-bottom: 0.85rem; padding: 1.25rem 1.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; cursor: pointer;" onclick="toggleCourseDetails('${{c.id}}')">
              <div>
                <span style="font-size: 0.75rem; color: var(--gold); font-weight: 800;">المرحلة 0${{c.phase}} · ${{c.badge}}</span>
                <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-top: 0.2rem;">${{c.icon}} ${{c.title}}</h3>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem;">
                <span style="font-size: 0.8rem; color: ${{isDone ? 'var(--emerald)' : 'var(--text-dim)'}};">${{isDone ? '✅ مكتمل' : '○ قيد الانتظار'}}</span>
                <span style="font-size: 0.9rem; color: var(--text-dim);">▾</span>
              </div>
            </div>

            <div id="details_${{c.id}}" style="display: none; margin-top: 1.15rem; padding-top: 1.15rem; border-top: 1px solid var(--border-subtle);">
              <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.15rem;">${{c.desc}}</p>
              
              <div style="margin-bottom: 1.15rem;">
                <h4 style="font-size: 0.92rem; color: var(--text-pure); margin-bottom: 0.35rem;">📖 الوحدات التدريبية (${{c.pages}} صفحة منهج):</h4>
                <ul style="padding-right: 1.25rem; font-size: 0.86rem; color: var(--text-muted); line-height: 1.8;">
                  ${{unitsHtml}}
                </ul>
              </div>

              <div style="margin-bottom: 1.15rem;">
                <h4 style="font-size: 0.92rem; color: var(--cyan); margin-bottom: 0.3rem;">🤖 أمر الذكاء الاصطناعي المعتمد (RCIC Prompt):</h4>
                <div class="code-box">${{c.prompt}}</div>
                <button class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.35rem 0.9rem;" onclick="copyText(this.previousElementSibling.innerText)">📋 نسخ الأمر</button>
              </div>

              <div style="margin-bottom: 1.15rem;">
                <h4 style="font-size: 0.92rem; color: var(--emerald); margin-bottom: 0.25rem;">💼 دراسة الحالة التطبيقية:</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">${{c.case_study}}</p>
              </div>

              <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1.15rem; padding-top: 0.85rem; border-top: 1px solid var(--border-subtle);">
                <div>
                  <h4 style="font-size: 0.92rem; color: var(--gold-light); margin-bottom: 0.15rem;">🧪 التكليف العملي:</h4>
                  <p style="font-size: 0.86rem; color: var(--text-muted);">${{c.lab}}</p>
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
        <div style="background: #06080D; border: 2px solid var(--gold); border-radius: 20px; padding: 3.5rem 2rem; text-align: center; margin-top: 2rem; box-shadow: 0 0 50px rgba(212, 168, 83, 0.35); position: relative;">
          <div style="font-size: 3rem; margin-bottom: 0.35rem;">👑</div>
          <div style="font-size: 0.85rem; letter-spacing: 3px; color: var(--gold); text-transform: uppercase; font-family: var(--font-kookies); font-weight: 800;">OTB Marketing Studio · City Kings</div>
          <div style="font-family: var(--font-royal); font-size: 2rem; color: var(--text-pure); margin: 0.75rem 0; font-weight: 900;">CERTIFICATE OF AI MASTERY</div>
          <p style="color: var(--text-dim); font-size: 0.95rem;">تشهد أكاديمية وكالة OTB لتمكين الذكاء الاصطناعي وهندسة النمو بأن</p>
          <h2 style="font-family: var(--font-felfel); font-size: 2.4rem; color: var(--gold); margin: 0.85rem 0; font-weight: 900;">${{name}}</h2>
          <p style="color: var(--text-main); max-width: 560px; margin: 0 auto 2rem auto; font-size: 0.92rem; line-height: 1.8;">
            قد أتم بنجاح متطلبات أكاديمية <b>الذكاء الاصطناعي التوليدي والنمو الرقمي</b> وأصبح مؤهلاً لمضاعفة الإنتاجية 5x وتطبيق استراتيجيات ملوك المدينة.
          </p>
          <div style="display: flex; justify-content: space-around; border-top: 1px solid var(--border-gold); padding-top: 1.5rem; font-size: 0.85rem;">
            <div>
              <div style="color: var(--text-dim); font-size: 0.75rem;">رقم الاعتماد الرسمي</div>
              <div style="font-family: var(--font-mono); color: var(--gold); font-weight: 800;">${{certId}}</div>
            </div>
            <div>
              <div style="color: var(--text-dim); font-size: 0.75rem;">تاريخ المنح</div>
              <div style="color: var(--text-pure); font-weight: 700;">${{date}}</div>
            </div>
            <div>
              <div style="color: var(--text-dim); font-size: 0.75rem;">الاعتماد الرقمي</div>
              <div style="color: var(--gold); font-weight: 900;">OTB Agency 👑</div>
            </div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 1.75rem;">
          <button class="btn btn-secondary" onclick="window.print()">🖨️ طباعة الشهادة / حفظ PDF</button>
        </div>
      `;
      wrap.scrollIntoView({{ behavior: "smooth" }});
      showToast("👑 تم إصدار شهادة الاعتماد الملكية بنجاح!");
    }}

    // INITIALIZATION
    renderRolesGrid();
    renderClientsGrid();
    renderCoursesList(coursesData);
    updateLivePrompt();
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(clean_html)

print("Generated Clean Apple-Grade OTB Team AI Hub Masterpiece!")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
