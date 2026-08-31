import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from build_factual_otb_portal import COURSES_DATA

# REAL ROLES WITH LUCIDE ICONS MAPPING
REAL_ROLES_DATA = [
  {
    "id": "content",
    "name": "صانع وكاتب المحتوى",
    "eng": "Content Creator & Copywriter",
    "lucide": "pen-tool",
    "officialRole": "المسؤول عن إنتاج النصوص الإعلانية (Copywriting)، خطط المحتوى الشهرية، اسكريبتات الفيديو القصير، وسرد قصة البراند.",
    "realChallenge": "استنزاف 3 إلى 5 ساعات يومياً في التفكير في أفكار جديدة (Writer's Block)، وصياغة هوكات (Hooks) مختلفة لكل منصة وإعادة تعديل النصوص بناء على طلب العميل.",
    "aiSuperpower": "توليد 10 زوايا إعلانية مختلفة (Angle Generation) وصياغة اسكريبتات 15 ثانية بهيكل PAS/AIDA وتكييف اللهجة المصرية الدقيقة في 90 ثانية بدلاً من 4 ساعات.",
    "tools": ["Claude 3.5 Sonnet (Copywriting)", "ChatGPT Plus (Hooks Ideation)", "Notion AI (Content Calendar)", "Grammarly Business"],
    "realPrompt": "Role: Senior Direct-Response Copywriter at OTB Agency.\\nContext: Client is MIX Coffee & Mart (Specialty coffee in Zagazig & Sharkia).\\nTask: Write 3 high-converting Meta Ad Copy variations using the PAS (Problem-Agitation-Solution) framework in refined modern Egyptian Arabic.\\nConstraints: Hook under 8 words, focus on premium atmosphere & specialty beans, bold royal tone, strong urgency CTA linking to WhatsApp menu.",
    "goldenRule": "الـ AI شريك عصف ذهني وسرعة؛ دورك كصانع محتوى في OTB هو وضع 'الروح المصرية والذكاء التنافسي' ومراجعة الكلمات لتليق بملوك المدينة."
  },
  {
    "id": "graphic",
    "name": "مصمم الجرافيك والهوية",
    "eng": "Graphic Designer & Visual Artist",
    "lucide": "palette",
    "officialRole": "المسؤول عن الهوية البصرية، تصاميم السوشيال ميديا، بنرات الإعلانات الممولة (Ad Creatives)، والمطبوعات الرسمية للعملاء.",
    "realChallenge": "تضييع ساعات في تفريغ الصور اليدوي (Masking)، البحث عن عناصر وملحقات وتعديل المقاسات يدوياً للستوري والبوست والبانر.",
    "aiSuperpower": "توليد خلفيات فائقة الواقعية لمنتجات العملاء (AI Product Staging)، إزالة الخلفيات وتوسيع أبعاد التصميم (Generative Fill) بنقرة واحدة وتوليد أفكار مودبورد فورية.",
    "tools": ["Midjourney v6.1 (Concept Art)", "Adobe Photoshop Firefly (Generative Fill)", "Figma + AI Plugins", "Photoroom API (E-Commerce Assets)"],
    "realPrompt": "Role: Senior Art Director at OTB Agency.\\nContext: Designing social media visual campaign for Dr. Zaghloul Jewelry (Luxury Gold).\\nTask: Generate prompt guidelines and lighting setup for high-end gold rings on black velvet with cinematic golden rim lighting and luxury reflections.\\nOutput: Exact visual direction, color hex tokens, font pairing suggestions (Felfel / Cormorant).",
    "goldenRule": "لا تصمم مجرد 'صورة حلوة'؛ صمم 'سلاحاً بصرياً' يوقف إصبع العميل وهو يسحب الشاشة (Thumb-Stopping Ad Creative)."
  },
  {
    "id": "video",
    "name": "مونتير ومخرج الفيديو والريلز",
    "eng": "Video Editor & Motion Designer",
    "lucide": "video",
    "officialRole": "المسؤول عن مونتاج فيديوهات الريلز والتيك توك، المؤثرات الصوتية والبصرية، إيقاع التقطيع، وإخراج الإعلانات المرئية.",
    "realChallenge": "البحث المرهق عن مقاطع الصوت والتريندات، تفريغ النصوص والكتابة التلقائية (Subtitles)، وتقطيع المقابلات الطويلة واختيار اللقطات الممتازة يدوياً.",
    "aiSuperpower": "توليد كابشن عربي تلقائي متحرك، إزالة الصمت وإعادة تأطير الفيديو للعمودي التلقائي (Auto-Reframe)، وتحسين جودة الصوت وعزل الضوضاء في ثوانٍ.",
    "tools": ["CapCut Pro (Auto-Captions & AI Effects)", "Adobe Premiere Pro (Text-Based Editing & Enhance Speech)", "Topaz Video AI (Upscaling & 4K Quality)", "ElevenLabs (Arabic Voice Synthesis)"],
    "realPrompt": "Role: Short-Form Video Strategist at OTB Agency.\\nContext: 15-second viral reel for Rancho's EG (Gourmet Burgers).\\nTask: Write shot-by-shot editing storyboard with 0-3s sensory ASMR hook, fast sync-cut sound design, and text-on-screen layout optimized for TikTok/Instagram Reels algorithm.",
    "goldenRule": "أول 3 ثوانٍ في الفيديو تحدد مصير الحملة؛ استخدم الصوت والمشهد المفاجئ لضمان تجاوز الـ Hook Rate حاجز الـ 35%."
  },
  {
    "id": "media_buyer",
    "name": "أخصائي الإعلانات وميديا بايينج",
    "eng": "Media Buyer & Growth Architect",
    "lucide": "trending-up",
    "officialRole": "المسؤول عن إدارة الميزانيات الإعلانية على Meta و TikTok و Google، تحسين الـ ROAS، واختبار وتوسيع الحملات الرابحة (Scaling).",
    "realChallenge": "استنزاف الوقت في استخراج الأرقام وتحليل التقارير يدوياً وتتبع الإعلانات وتخمين سبب انخفاض التحويل أو ارتفاع تكلفة الشراء (CPA).",
    "aiSuperpower": "تشخيص فوري للأداء واكتشاف الإرهاق الإعلاني (Ad Fatigue) مبكراً، تحليل بيانات CAPI ومعدلات التحويل واقتراح ميزانيات السكيلينج بدقة رياضية.",
    "tools": ["Meta Ads Manager AI Advantage+", "Triple Whale / AI Attribution", "ChatGPT Advanced Data Analysis (Python Cohort Analysis)", "Google Looker Studio AI"],
    "realPrompt": "Role: Principal Media Buyer and Growth Architect at OTB Agency.\\nContext: Running Meta Ads for E-commerce Client with target CPA $8 and target ROAS 4.0x.\\nTask: Analyze campaign metrics [Spend: $1200, Revenue: $5100, CTR: 1.8%, Hook Rate: 28%, Conversion Rate: 2.1%] and provide actionable 48-hour optimization & budget scaling plan.",
    "goldenRule": "الأرقام لا تكذب؛ كل قرار زيادة ميزانية يجب أن يكون مبنياً على معادلة واضحة وليس على الإحساس."
  },
  {
    "id": "account_mgr",
    "name": "مدير الحسابات وخدمة العملاء",
    "eng": "Senior Account Manager",
    "lucide": "briefcase",
    "officialRole": "حلقة الوصل بين عملاء الوكالة وفريق التنفيذ، إدارة المواعيد النهائية، ضبط التوقعات، وبناء علاقات استراتيجية طويلة الأمد.",
    "realChallenge": "كتابة تقارير دورية تستهلك ساعات طويلة، التعامل مع طلبات التعديل غير المنظمة، ومتابعة تسليمات الفريق عبر الشات.",
    "aiSuperpower": "تحويل رسائل العميل وملاحظاته الصوتية إلى مهام عمل واضحة وتوليد ملخصات تنفيذية للتقارير الأسبوعية والشهرية بأسلوب احترافي.",
    "tools": ["Notion AI (Task Synthesis & Client Hub)", "Otter.ai / Fireflies (Meeting Summarization)", "Claude 3.5 Sonnet (Executive Client Reporting)", "Slack AI"],
    "realPrompt": "Role: Senior Account Director at OTB Agency.\\nContext: Monthly performance review email for CEO of Franks EG (B2B Industrial Client).\\nTask: Write an executive, highly professional Arabic briefing summarizing achievements [Sales doubled from 10M to 30M, market rank up to #2], next month strategic goals, and budget recommendations.",
    "goldenRule": "العميل لا يشتري إعلانات فقط؛ يشتري راحة البال وشريكاً يثق في قدرته على قيادة النمو."
  },
  {
    "id": "brand_strategist",
    "name": "استراتيجي البراند والتموضع",
    "eng": "Brand & Strategy Specialist",
    "lucide": "compass",
    "officialRole": "المسؤول عن أبحاث السوق والمنافسين، تحديد التموضع الاستراتيجي، ونبرة الصوت وصياغة عروض القيمة الاستثنائية للبراندات.",
    "realChallenge": "استغراق أسابيع في قراءة تقارير السوق والمنافسين وتحليل آراء العملاء ونقاط الضعف في السوق يدوياً.",
    "aiSuperpower": "استخراج رؤى السوق ونقاط ألم الجمهور من مئات المراجعات والتعليقات في دقائق وتوليد مصفوفات التموضع التنافسي بدقة متناهية.",
    "tools": ["Perplexity Pro (Live Market Research)", "Claude 3.5 Sonnet (Strategic Synthesis & SWOT)", "NotebookLM (Deep Document Synthesis)", "Semrush AI"],
    "realPrompt": "Role: Chief Strategy Officer at OTB Agency.\\nContext: Developing market positioning strategy for a new specialty café chain in Egypt.\\nTask: Conduct a comprehensive competitive positioning matrix against Costa and local cafés, identify the whitespace opportunity, define the Archetype (The Ruler/Creator), and draft the unique value proposition.",
    "goldenRule": "التموضع الصحيح يوفر نصف ميزانية الإعلانات؛ اجعل البراند الخيار البديهي الوحيد في ذهن العميل."
  },
  {
    "id": "moderator",
    "name": "مسؤول مجتمع الموديريشن والمبيعات",
    "eng": "Community Moderator & Sales Chat",
    "lucide": "message-square",
    "officialRole": "إدارة الرسائل والتعليقات على صفحات السوشيال ميديا، الرد الفوري وتوجيه العملاء المحتملين وإتمام المبيعات عبر الشات.",
    "realChallenge": "تراكم مئات الاستفسارات المتكررة حول الأسعار والمواعيد وفقدان عملاء بسبب بطء الرد في ساعات الذروة وخارج أوقات العمل.",
    "aiSuperpower": "أتمتة الردود على الأسئلة الشائعة بنسبة 80% وتأهيل العملاء الجادين بذكاء عبر روبوتات دردشة تتحدث باللهجة المصرية الطبيعية.",
    "tools": ["ManyChat AI (Meta/Instagram Direct Automation)", "WhatsApp Business API Automation", "OpenAI Assistant API (Smart FAQ Auto-Response)", "Zendesk AI"],
    "realPrompt": "Role: Lead Sales & Community Specialist at OTB Agency.\\nContext: Handling WhatsApp Business inquiries for Elag Labs (Medical Lab bookings).\\nTask: Write an automated conversational qualification flow in warm Egyptian Arabic that asks for patient location, required test type, and books home-visit appointment seamlessly.",
    "goldenRule": "الرد السريع خلال 5 دقائق يضاعف نسبة إتمام البيع 400%؛ اجمع بين سرعة الأتمتة وحميمية التواصل الإنساني."
  },
  {
    "id": "sales_pr",
    "name": "مدير المبيعات والعلاقات العامة",
    "eng": "Sales & PR Specialist",
    "lucide": "phone-call",
    "officialRole": "جلب عملاء جدد للوكالة، تقديم عروض الخدمات (Pitches)، إبرام عقود الرتينر، وبناء شراكات استراتيجية مع كبار الشركات.",
    "realChallenge": "البحث عن العملاء المحتملين وتجهيز عروض الأسعار والمقترحات المخصصة من الصفر لكل عميل وتتبع الردود.",
    "aiSuperpower": "توليد مقترحات أعمال وعروض أسعار مخصصة بدقة عالية وتجهيز عروض تقديمية (Pitch Decks) كاملة بالبيانات في أقل من ساعة.",
    "tools": ["Apollo.io (B2B Lead Intelligence)", "Claude 3.5 Sonnet (Custom Proposal Generation)", "Gamma / Beautiful.ai (AI Pitch Deck Presentation)", "HubSpot Sales Hub AI"],
    "realPrompt": "Role: VP of Business Development at OTB Agency.\\nContext: Pitching a $2,500/month Dominance Retainer to a major factory in 10th of Ramadan city.\\nTask: Write a persuasive 1-page B2B executive proposal demonstrating our proven industrial track record (Franks EG case study) and a clear 90-day ROI roadmap.",
    "goldenRule": "نحن لا نبيع 'بوستات وتصاميم'؛ نحن نبيع 'ماكينة نمو وإيرادات موثوقة' تجعل الاستثمار معنا القرار الأكثر ربحية للعميل."
  },
  {
    "id": "leadership",
    "name": "القيادة والإدارة التشغيلية",
    "eng": "Leadership & Operations",
    "lucide": "crown",
    "officialRole": "إدارة وتوجيه الفريق، ضبط مؤشرات الأداء، تطوير العمليات (SOPs)، واتخاذ القرارات الاستراتيجية لترسيخ ريادة OTB.",
    "realChallenge": "متابعة الإنتاجية وجودة المخرجات، تفادي الاختناقات التشغيلية وحل النزاعات وإهدار الوقت في الاجتماعات التنسيقية الطويلة.",
    "aiSuperpower": "لوحات تحكم ذكية ترصد سير العمل ومؤشرات الأداء اللحظية، وتوليد إجراءات تشغيل قياسية (SOPs) لأي عملية جديدة بنقرة واحدة.",
    "tools": ["Notion AI (SOPs & Enterprise Knowledge Engine)", "ClickUp AI / Asana Intelligence", "Claude 3.5 Sonnet (Strategic Decision Support)", "Loom AI"],
    "realPrompt": "Role: Managing Director at OTB Agency.\\nContext: Establishing agency standard operating procedures (SOP) for onboarding new clients via Manus 9-Stage pipeline.\\nTask: Create a detailed operational workflow assigning roles, timelines, review gates, and deliverables for each stage.",
    "goldenRule": "القيادة الحقيقية تمكّن الفريق وتوفر لهم أفضل الأدوات والأنظمة ليبدعوا؛ ملوك المدينة يبنون أنظمة تعمل بكفاءة حتى أثناء غيابهم."
  }
]

# REAL CLIENTS
REAL_CLIENTS_DATA = [
  {
    "name": "Franks EG (فرانكس)",
    "sector": "Industrial & B2B / قطاع التصنيع والشركات الكبرى",
    "metric": "من المركز 25 ➔ المركز الثاني | 10M ➔ 30M EGP",
    "desc": "قصة نجاح OTB الأكبر؛ إعادة هيكلة المنظومة التسويقية والبيعية ومضاعفة المبيعات الرقمية من 10 إلى 30 مليون جنيه شهرياً عبر استراتيجيات تسويق موجهة للشركات (B2B).",
    "socialLink": "https://www.facebook.com/otbagency5",
    "badge": "B2B Leader",
    "lucide": "factory"
  },
  {
    "name": "MIX Coffee & Mart (ميكس كوفي)",
    "sector": "Specialty Coffee / قطاع الضيافة والكافيهات",
    "metric": "تفاعل +180% | مضاعفة مبيعات الفروع",
    "desc": "إعادة التموضع من كافيه تقليدي إلى وجهة أولى لرواد الأعمال بهوية داكنة فاخرة، وفيديوهات ASMR لصناعة القهوة حققت انتشاراً واسعاً على السوشيال ميديا.",
    "socialLink": "https://www.facebook.com/people/MIX-Coffee-Mart/100063935293290/",
    "badge": "Specialty Coffee",
    "lucide": "coffee"
  },
  {
    "name": "Rancho's EG (رانشوز برجر)",
    "sector": "Gourmet Burgers / قطاع المطاعم والأغذية",
    "metric": "معدل احتفاظ 36.8% | 450K مشاهدة ريلز",
    "desc": "الخروج من فخ الخصومات إلى تموضع 'البرجر الملحمي'، وإعلانات فيديو ريلز مباشرة رفعت مبيعات الواتساب والطلبات بنسبة 65% عبر الخط الساخن 19484.",
    "socialLink": "https://www.facebook.com/ranchos.eg",
    "badge": "Gourmet Burger",
    "lucide": "utensils"
  },
  {
    "name": "مجوهرات دكتور زغلول (Dr. Zaghloul)",
    "sector": "Luxury Gold & Jewelry / ذهب ومجوهرات",
    "metric": "ROAS 7.5x+ | إعلانات تحويلية",
    "desc": "بناء الثقة وسرد قصص التصاميم الحصرية بجودة سينمائية وهيكل حملات TOFU/MOFU/BOFU محققاً عائداً إعلانيا استثنائياً.",
    "socialLink": "https://www.facebook.com/otbagency5",
    "badge": "Luxury Gold",
    "lucide": "gem"
  },
  {
    "name": "معامل علاج (Elag Labs)",
    "sector": "Clinics & Medical / معامل وتحاليل طبية",
    "metric": "800+ حجز مؤهل شهرياً",
    "desc": "إعلانات تحويلية مع مسار WhatsApp Business API مؤتمت لتأهيل واستقبال طلبات الزيارات المنزلية وحجوزات التحاليل بدقة.",
    "socialLink": "https://www.facebook.com/elaglabs",
    "badge": "Medical Labs",
    "lucide": "activity"
  },
  {
    "name": "صقر ستور (Sakr Store)",
    "sector": "E-Commerce & Retail / تجارة وتجزئة الملابس",
    "metric": "تكلفة الشراء (CPA) -32%",
    "desc": "إعادة هيكلة حملات Meta وإعلانات Advantage+ مع ربط تتبع CAPI وعروض الباقات المجمعة لرفع متوسط قيمة السلة.",
    "socialLink": "https://www.facebook.com/otbagency5",
    "badge": "E-Commerce",
    "lucide": "shopping-bag"
  }
]

roles_json = json.dumps(REAL_ROLES_DATA, ensure_ascii=False)
clients_json = json.dumps(REAL_CLIENTS_DATA, ensure_ascii=False)
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

# Build Enhanced CSS with Lucide vector support
css_content = """/* ==========================================================================
   OTB TEAM AI HUB — MASTER STYLESHEET (LUCIDE & VERCEL CERTIFIED)
   ========================================================================== */

:root {
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
  --crimson: #F43F5E;
  --cyan: #38BDF8;

  --text-pure: #FFFFFF;
  --text-main: #E2E8F0;
  --text-muted: #94A3B8;
  --text-dim: #64748B;

  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-gold: rgba(212, 168, 83, 0.32);

  --radius-sm: 10px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-full: 9999px;

  --font-felfel: 'Felfel-Bold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-kookies: 'KOOkies-Bold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-kookies-black: 'KOOkies-ExtraBold', 'Readex Pro', system-ui, -apple-system, sans-serif;
  --font-royal: 'Cinzel', serif;
  --font-mono: 'JetBrains Mono', monospace;
  --font-ui: -apple-system, BlinkMacSystemFont, 'Readex Pro', 'SF Pro Text', system-ui, sans-serif;

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

/* Reset */
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

/* Lucide Vector Icons Global Sizing & Alignment */
svg.lucide, i.lucide, [data-lucide] {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  flex-shrink: 0;
}

/* Content Visibility */
.cv-optimize {
  content-visibility: auto;
  contain-intrinsic-size: 1px 400px;
}

/* WebGL Background */
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

/* Navbar */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(6, 8, 12, 0.85);
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

/* Nav Pills */
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
  min-height: 44px;
  border-radius: var(--radius-full);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.18s var(--spring-snappy);
  display: flex;
  align-items: center;
  gap: 0.45rem;
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

.nav-pill-btn.active svg {
  color: #000 !important;
}

/* Phone Button */
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
  gap: 0.45rem;
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

/* App Container */
.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 3rem 1.5rem 6rem 1.5rem;
  position: relative;
  z-index: 1;
}

/* Hero */
.hero-wrapper {
  text-align: center;
  max-width: 820px;
  margin: 0 auto 3.5rem auto;
}

.hero-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
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

/* Glass Card */
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

/* Bento Grid */
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

/* Role Grid */
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
  margin-bottom: 0.35rem;
  display: flex;
  align-items: center;
  justify-content: center;
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

/* Role Stage */
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
  min-height: 44px;
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

.btn-primary svg {
  color: #000 !important;
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

/* Tabs */
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
"""

with open(os.path.join(BASE_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

# Build Master HTML with Local Script Paths & Fallbacks
html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Aggressive Cache Prevention Meta -->
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  
  <title>👑 OTB Team AI Hub — منصة تمكين ملوك المدينة</title>
  
  <!-- Resource Hints -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=JetBrains+Mono:wght@500;600;700&family=Readex+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css?v=2.6.0">
  
  <!-- Standalone Bundled Libraries (Local + CDN fallback) -->
  <script src="assets/js/lucide.min.js"></script>
  <script src="assets/js/three.min.js"></script>
</head>
<body>

  <!-- WebGL Background -->
  <canvas id="webglCanvas"></canvas>

  <!-- Navbar -->
  <header class="navbar">
    <a href="#" class="nav-brand" onclick="switchMainTab('roles')">
      <div class="brand-badge-img">
        <img src="assets/images/otb_official_logo.jpg" alt="OTB Logo" width="42" height="42">
      </div>
      <div class="brand-text">
        <h1>OTB TEAM AI HUB <i data-lucide="crown" style="width: 18px; height: 18px; color: var(--gold);"></i></h1>
        <span>WE ARE OTB · THE CITY KINGS</span>
      </div>
    </a>

    <!-- Nav Pills -->
    <nav class="nav-pills">
      <button class="nav-pill-btn active" id="tabBtn-roles" onclick="switchMainTab('roles')">
        <i data-lucide="users" style="width: 16px; height: 16px;"></i> أدوار الفريق
      </button>
      <button class="nav-pill-btn" id="tabBtn-cases" onclick="switchMainTab('cases')">
        <i data-lucide="briefcase" style="width: 16px; height: 16px;"></i> عملاء الوكالة
      </button>
      <button class="nav-pill-btn" id="tabBtn-manus" onclick="switchMainTab('manus')">
        <i data-lucide="compass" style="width: 16px; height: 16px;"></i> بريف Manus
      </button>
      <button class="nav-pill-btn" id="tabBtn-courses" onclick="switchMainTab('courses')">
        <i data-lucide="book-open" style="width: 16px; height: 16px;"></i> المناهج (19)
      </button>
      <button class="nav-pill-btn" id="tabBtn-prompts" onclick="switchMainTab('prompts')">
        <i data-lucide="bot" style="width: 16px; height: 16px;"></i> استوديو الأوامر
      </button>
      <button class="nav-pill-btn" id="tabBtn-quiz" onclick="switchMainTab('quiz')">
        <i data-lucide="award" style="width: 16px; height: 16px;"></i> الشهادة
      </button>
      <button class="nav-pill-btn" id="tabBtn-downloads" onclick="switchMainTab('downloads')">
        <i data-lucide="download" style="width: 16px; height: 16px;"></i> التحميلات
      </button>
    </nav>

    <div>
      <a href="tel:+201008080295" class="phone-wrapper">
        <i data-lucide="phone" style="width: 16px; height: 16px;"></i>
        <span class="phone-code">+20</span>
        <span class="phone-num">100 808 0295</span>
      </a>
    </div>
  </header>

  <!-- App Container -->
  <main class="app-container">

    <!-- SECTION 1: ROLES -->
    <section id="section-roles" class="hub-section">
      <div class="hero-wrapper">
        <div class="hero-pill"><i data-lucide="sparkles" style="width: 14px; height: 14px;"></i> OTB AI SUPERPOWER COCKPIT · 2026</div>
        <h2 class="hero-title">اختر تخصصك.. واكتشف قوة الـ <span>AI الحقيقية</span> <i data-lucide="zap" style="width: 32px; height: 32px; color: var(--gold); display: inline-block; vertical-align: middle;"></i></h2>
        <p class="hero-subtitle">
          بيانات حقيقية 100% مستخلصة من الدليل الرسمي للمسميات وخارطة طريق OTB Agency. تعرف كيف تختزل أدوات الذكاء الاصطناعي 40% من وقت المهام الروتينية لتبدع كأحد ملوك المدينة.
        </p>
      </div>

      <!-- Roles Grid -->
      <div class="role-grid" id="rolesGrid"></div>

      <!-- Selected Role Stage -->
      <div id="roleDetailsStage" class="role-stage"></div>
    </section>

    <!-- SECTION 2: CLIENT CASES -->
    <section id="section-cases" class="hub-section cv-optimize" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <div class="hero-pill"><i data-lucide="shield-check" style="width: 14px; height: 14px;"></i> VERIFIED CLIENT TRIUMPHS</div>
        <h2 class="hero-title">نتائج وأرقام عملاء OTB <span>الموثقة بالسوشيال ميديا</span></h2>
        <p class="hero-subtitle">بيانات حقيقية وأرقام مسجلة وروابط مباشرة لصفحات التواصل الاجتماعي الرسمية لعملاء الوكالة.</p>
      </div>

      <div id="clientsGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.25rem;"></div>
    </section>

    <!-- SECTION 3: MANUS PIPELINE -->
    <section id="section-manus" class="hub-section cv-optimize" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <div class="hero-pill"><i data-lucide="crown" style="width: 14px; height: 14px;"></i> MANUS STRATEGIC DISCOVERY PIPELINE</div>
        <h2 class="hero-title">نظام بريف واستقبال العملاء المعتمد <span>(9 مراحل)</span></h2>
        <p class="hero-subtitle">المنظومة الرسمية لاكتشاف وتأهيل عملاء وكالة OTB وضبط التوقعات والأهداف من الجلسة الأولى.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.15rem;">
        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 01</span>
            <i data-lucide="sprout" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-bottom: 0.3rem;">الجذور (من أنتم؟)</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">قصة التأسيس، الرؤية، والسبب الجوهري لوجود البراند في السوق والمهمة الأساسية.</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 02</span>
            <i data-lucide="gem" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-bottom: 0.3rem;">العرض والقيمة (The Offer)</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">المنتجات والخدمات الأساسية، الميزة التنافسية الحصرية، وهيكل الأسعار.</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 03</span>
            <i data-lucide="target" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-bottom: 0.3rem;">الجمهور المستهدف (Audience)</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">الشرائح السكانية، السلوك الشرائي، ونقاط الألم الرئيسية (Pain Points).</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 04</span>
            <i data-lucide="crosshair" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-bottom: 0.3rem;">مشهد المنافسة والفجوات</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">المنافسون المباشرون ونقاط ضعفهم التي يمكن لـ OTB استغلالها لصالح العميل.</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 05</span>
            <i data-lucide="sparkles" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-bottom: 0.3rem;">شخصية البراند ونبرة الصوت</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">النمط النفسي ونبرة الحديث المعتمدة (Bold, Royal, Friendly, Prestigious...).</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 06</span>
            <i data-lucide="bar-chart-3" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-bottom: 0.3rem;">النجاح ومستهدفات الـ 90 يوماً</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">أهداف الـ ROAS، الإيرادات، والمبيعات المستهدفة ومؤشرات الأداء KPIs.</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 07</span>
            <i data-lucide="settings" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-bottom: 0.3rem;">التشغيل والميزانيات</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">ميزانية الإعلانات الشهرية المتاحة، الموارد، وقنوات التواصل المعتمدة.</p>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 08</span>
            <i data-lucide="shield-check" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-bottom: 0.3rem;">السياق والدروس السابقة</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted);">تجارب الحملات السابقة، ما نجح وما فشل، والمحاذير التسويقية والقانونية.</p>
        </div>

        <div class="glass-card" style="border-color: var(--border-gold); background: rgba(212, 168, 83, 0.08);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 09</span>
            <i data-lucide="check-circle-2" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--gold); margin-bottom: 0.3rem;">المراجعة وإصدار الكود المرجعي</h3>
          <p style="font-size: 0.9rem; color: var(--text-main);">تأكيد بنود البريف وتوليد الكود الرسمي (مثل: OTB-K3M9P) لتوزيع المهام على الفريق.</p>
        </div>
      </div>
    </section>

    <!-- SECTION 4: COURSES -->
    <section id="section-courses" class="hub-section cv-optimize" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <h2 class="hero-title"><i data-lucide="book-open" style="width: 28px; height: 28px; color: var(--gold); display: inline-block; vertical-align: middle;"></i> مناهج الـ 19 تخصصاً المعتمدة</h2>
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

    <!-- SECTION 5: PROMPTS STUDIO -->
    <section id="section-prompts" class="hub-section cv-optimize" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <h2 class="hero-title"><i data-lucide="bot" style="width: 28px; height: 28px; color: var(--gold); display: inline-block; vertical-align: middle;"></i> استوديو أوامر الذكاء الاصطناعي</h2>
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

        <button class="btn btn-primary" style="width: 100%; padding: 0.8rem;" onclick="copyText(document.getElementById('livePromptCode').innerText)">
          <i data-lucide="copy" style="width: 16px; height: 16px;"></i> نسخ الأمر المخصص للحافظة
        </button>
      </div>
    </section>

    <!-- SECTION 6: QUIZ & CERTIFICATE -->
    <section id="section-quiz" class="hub-section cv-optimize" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <h2 class="hero-title"><i data-lucide="award" style="width: 28px; height: 28px; color: var(--gold); display: inline-block; vertical-align: middle;"></i> تقييم الكفاءة وإصدار شهادة ملوك المدينة</h2>
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
          <button class="btn btn-primary" style="padding: 0.85rem 3rem; font-size: 0.95rem;" onclick="generateOfficialCert()">
            <i data-lucide="crown" style="width: 18px; height: 18px;"></i> إصدار شهادة الاعتماد الملكية
          </button>
        </div>

        <div id="certContainer" style="display: none;"></div>
      </div>
    </section>

    <!-- SECTION 7: DOWNLOADS -->
    <section id="section-downloads" class="hub-section cv-optimize" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <h2 class="hero-title"><i data-lucide="download" style="width: 28px; height: 28px; color: var(--gold); display: inline-block; vertical-align: middle;"></i> مركز المستندات والأوامر المباشرة</h2>
        <p class="hero-subtitle">تحميل التقارير الاستراتيجية وموسوعات الأوامر وقوائم الفحص بصيغ مباشرة.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">50+ Prompts</span>
            <i data-lucide="terminal" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.4rem 0;">موسوعة الأوامر التكتيكية</h3>
          <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1.25rem;">أوامر الذكاء الاصطناعي المعتمدة لأدوار OTB.</p>
          <a href="track_a_fast_track_sprint/cheatsheets/OTB_Prompt_Engineering_Bible.md" download class="btn btn-primary" style="width: 100%; font-size: 0.85rem;">
            <i data-lucide="download" style="width: 16px; height: 16px;"></i> تحميل الموسوعة
          </a>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Checklist</span>
            <i data-lucide="check-square" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.4rem 0;">فحص الميديا بايينج</h3>
          <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1.25rem;">قائمة فحص الحملات قبل الإطلاق وقواعد السكيلينج.</p>
          <a href="track_a_fast_track_sprint/cheatsheets/OTB_Media_Buying_Checklist.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.85rem;">
            <i data-lucide="download" style="width: 16px; height: 16px;"></i> تحميل الفحص
          </a>
        </div>

        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Strategic Doc</span>
            <i data-lucide="file-text" style="width: 18px; height: 18px; color: var(--gold);"></i>
          </div>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.4rem 0;">التقرير الاستراتيجي الشامل</h3>
          <p style="font-size: 0.86rem; color: var(--text-muted); margin-bottom: 1.25rem;">وثيقة التوجيه التنفيذي لنمو الوكالة.</p>
          <a href="track_b_4week_masterclass/studio_artifacts/OTB_Executive_Strategic_Briefing.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.85rem;">
            <i data-lucide="download" style="width: 16px; height: 16px;"></i> تحميل التقرير
          </a>
        </div>
      </div>
    </section>

  </main>

  <script src="shared_ui.js?v=2.6.0"></script>
  <script>
    const coursesData = {courses_json};
    const rolesData = {roles_json};
    const clientsData = {clients_json};

    const rolesMap = new Map(rolesData.map(r => [r.id, r]));
    const coursesMap = new Map(coursesData.map(c => [c.id, c]));

    const doneCoursesSet = new Set();
    coursesData.forEach(c => {{
      if (localStorage.getItem("otb_done_" + c.id) === "true") {{
        doneCoursesSet.add(c.id);
      }}
    }});

    function refreshLucide() {{
      try {{
        if (window.lucide && typeof lucide.createIcons === 'function') {{
          lucide.createIcons();
        }}
      }} catch (e) {{
        console.warn("Lucide render error:", e);
      }}
    }}

    function switchMainTab(tabName) {{
      if (!tabName) return;
      document.querySelectorAll(".hub-section").forEach(s => s.style.display = "none");
      const target = document.getElementById("section-" + tabName);
      if (target) target.style.display = "block";

      document.querySelectorAll(".nav-pill-btn").forEach(b => b.classList.remove("active"));
      const btn = document.getElementById("tabBtn-" + tabName);
      if (btn) btn.classList.add("active");

      window.scrollTo({{ top: 0, behavior: "smooth" }});
      setTimeout(refreshLucide, 20);
    }}

    function renderRolesGrid() {{
      const grid = document.getElementById("rolesGrid");
      let html = "";
      rolesData.forEach((r, idx) => {{
        html += `
          <div class="role-tab ${{idx === 0 ? 'active' : ''}}" id="roleTab_${{r.id}}" onclick="selectRole('${{r.id}}')">
            <div class="role-icon-box">
              <i data-lucide="${{r.lucide}}" style="width: 28px; height: 28px; color: var(--gold);"></i>
            </div>
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

      const r = rolesMap.get(roleId);
      if (!r) return;

      let toolsHtml = "";
      r.tools.forEach(t => {{
        toolsHtml += `<span class="tool-pill"><i data-lucide="wrench" style="width: 13px; height: 13px; color: var(--gold);"></i> ${{t}}</span>`;
      }});

      const stage = document.getElementById("roleDetailsStage");
      stage.innerHTML = `
        <div class="role-header-strip">
          <div>
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 800; letter-spacing: 1px;">الدور المعتمد رسمياً في هيكل OTB</span>
            <h2 class="role-heading">
              <i data-lucide="${{r.lucide}}" style="width: 32px; height: 32px; color: var(--gold); display: inline-block; vertical-align: middle;"></i>
              ${{r.name}} <span style="font-family: var(--font-kookies); font-size: 1.1rem; color: var(--gold-light);">(${{r.eng}})</span>
            </h2>
            <p style="color: var(--text-muted); font-size: 0.92rem; margin-top: 0.3rem;">${{r.officialRole}}</p>
          </div>
          <button class="btn btn-primary" onclick="copyText(document.getElementById('rolePromptBox').innerText)">
            <i data-lucide="copy" style="width: 16px; height: 16px;"></i> نسخ الأمر المعتمد
          </button>
        </div>

        <div class="bento-grid">
          <div class="bento-col-6 glass-card" style="background: rgba(244, 63, 94, 0.04); border-color: rgba(244, 63, 94, 0.25);">
            <div style="display: flex; align-items: center; gap: 0.45rem; margin-bottom: 0.45rem;">
              <i data-lucide="alert-triangle" style="width: 18px; height: 18px; color: var(--crimson);"></i>
              <h4 style="color: var(--crimson); font-size: 0.95rem; font-weight: 800;">أين يضيع وقتك يومياً؟ (التحدي المعتاد):</h4>
            </div>
            <p style="font-size: 0.9rem; color: var(--text-main); line-height: 1.7;">${{r.realChallenge}}</p>
          </div>

          <div class="bento-col-6 glass-card" style="background: rgba(16, 185, 129, 0.04); border-color: rgba(16, 185, 129, 0.25);">
            <div style="display: flex; align-items: center; gap: 0.45rem; margin-bottom: 0.45rem;">
              <i data-lucide="zap" style="width: 18px; height: 18px; color: var(--emerald);"></i>
              <h4 style="color: var(--emerald); font-size: 0.95rem; font-weight: 800;">كيف يضاعف الـ AI إنتاجيتك 5x؟:</h4>
            </div>
            <p style="font-size: 0.9rem; color: var(--text-main); line-height: 1.7;">${{r.aiSuperpower}}</p>
          </div>

          <div class="bento-col-12 glass-card">
            <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.65rem; font-weight: 800; display: flex; align-items: center; gap: 0.35rem;">
              <i data-lucide="wrench" style="width: 18px; height: 18px; color: var(--gold);"></i> ترسانة الأدوات الذكية المعتمدة لدورك:
            </h4>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">${{toolsHtml}}</div>
          </div>

          <div class="bento-col-12 glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
              <h4 style="font-size: 0.95rem; color: var(--cyan); font-weight: 800; display: flex; align-items: center; gap: 0.35rem;">
                <i data-lucide="terminal" style="width: 18px; height: 18px; color: var(--cyan);"></i> الأمر الجاهز الفوري لعملاء الوكالة (Plug-and-Play Prompt):
              </h4>
              <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: 700;">صيغة RCIC احترافية</span>
            </div>
            <div id="rolePromptBox" class="code-box">${{r.realPrompt}}</div>
          </div>

          <div class="bento-col-12 glass-card" style="background: rgba(212, 168, 83, 0.06); border-color: var(--border-gold);">
            <div style="display: flex; align-items: center; gap: 0.45rem; margin-bottom: 0.35rem;">
              <i data-lucide="crown" style="width: 20px; height: 20px; color: var(--gold);"></i>
              <h4 style="color: var(--gold); font-size: 1rem; font-weight: 800;">النصيحة الذهبية لملوك المدينة:</h4>
            </div>
            <p style="font-size: 0.92rem; color: var(--text-main); line-height: 1.8;">${{r.goldenRule}}</p>
          </div>
        </div>
      `;
      setTimeout(refreshLucide, 20);
    }}

    function renderClientsGrid() {{
      const container = document.getElementById("clientsGrid");
      let html = "";
      clientsData.forEach(c => {{
        html += `
          <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
              <span style="font-size: 0.8rem; color: var(--gold); font-weight: 800; display: flex; align-items: center; gap: 0.3rem;">
                <i data-lucide="${{c.lucide}}" style="width: 16px; height: 16px;"></i> ${{c.badge}}
              </span>
              <span style="font-size: 0.72rem; color: var(--emerald); font-weight: 800; background: rgba(16, 185, 129, 0.1); padding: 0.2rem 0.55rem; border-radius: var(--radius-full); border: 1px solid rgba(16, 185, 129, 0.25);">${{c.metric}}</span>
            </div>
            <h3 style="font-family: var(--font-felfel); font-size: 1.3rem; color: var(--text-pure); margin-bottom: 0.35rem;">${{c.name}}</h3>
            <div style="font-size: 0.8rem; color: var(--text-dim); margin-bottom: 0.55rem; font-weight: 600;">${{c.sector}}</div>
            <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">${{c.desc}}</p>
            <a href="${{c.socialLink}}" target="_blank" class="btn btn-secondary" style="width: 100%; font-size: 0.82rem; padding: 0.5rem;">
              <i data-lucide="external-link" style="width: 14px; height: 14px;"></i> زيارة صفحة فيسبوك الرسمية
            </a>
          </div>
        `;
      }});
      container.innerHTML = html;
      setTimeout(refreshLucide, 20);
    }}

    function renderCoursesList(list) {{
      const container = document.getElementById("coursesList");
      let html = "";
      list.forEach(c => {{
        const isDone = doneCoursesSet.has(c.id);
        let unitsHtml = "";
        c.units.forEach((u, i) => {{
          unitsHtml += `<li style="margin-bottom: 0.3rem;"><b>الوحدة ${{i + 1}}:</b> ${{u}}</li>`;
        }});

        html += `
          <div class="glass-card" style="margin-bottom: 0.85rem; padding: 1.25rem 1.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; cursor: pointer;" onclick="toggleCourseDetails('${{c.id}}')">
              <div>
                <span style="font-size: 0.75rem; color: var(--gold); font-weight: 800;">المرحلة 0${{c.phase}} · ${{c.badge}}</span>
                <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-top: 0.2rem;">${{c.title}}</h3>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem;">
                <span style="font-size: 0.8rem; color: ${{isDone ? 'var(--emerald)' : 'var(--text-dim)'}};">${{isDone ? '✅ مكتمل' : '○ قيد الانتظار'}}</span>
                <i data-lucide="chevron-down" style="width: 18px; height: 18px; color: var(--text-dim);"></i>
              </div>
            </div>

            <div id="details_${{c.id}}" style="display: none; margin-top: 1.15rem; padding-top: 1.15rem; border-top: 1px solid var(--border-subtle);">
              <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.15rem;">${{c.desc}}</p>
              
              <div style="margin-bottom: 1.15rem;">
                <h4 style="font-size: 0.92rem; color: var(--text-pure); margin-bottom: 0.35rem; display: flex; align-items: center; gap: 0.35rem;">
                  <i data-lucide="book-open" style="width: 16px; height: 16px; color: var(--gold);"></i> الوحدات التدريبية (${{c.pages}} صفحة منهج):
                </h4>
                <ul style="padding-right: 1.25rem; font-size: 0.86rem; color: var(--text-muted); line-height: 1.8;">
                  ${{unitsHtml}}
                </ul>
              </div>

              <div style="margin-bottom: 1.15rem;">
                <h4 style="font-size: 0.92rem; color: var(--cyan); margin-bottom: 0.3rem; display: flex; align-items: center; gap: 0.35rem;">
                  <i data-lucide="bot" style="width: 16px; height: 16px; color: var(--cyan);"></i> أمر الذكاء الاصطناعي المعتمد (RCIC Prompt):
                </h4>
                <div class="code-box">${{c.prompt}}</div>
                <button class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.35rem 0.9rem;" onclick="copyText(this.previousElementSibling.innerText)">
                  <i data-lucide="copy" style="width: 14px; height: 14px;"></i> نسخ الأمر
                </button>
              </div>

              <div style="margin-bottom: 1.15rem;">
                <h4 style="font-size: 0.92rem; color: var(--emerald); margin-bottom: 0.25rem; display: flex; align-items: center; gap: 0.35rem;">
                  <i data-lucide="briefcase" style="width: 16px; height: 16px; color: var(--emerald);"></i> دراسة الحالة التطبيقية:
                </h4>
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
      setTimeout(refreshLucide, 20);
    }}

    function toggleCourseDetails(id) {{
      const d = document.getElementById("details_" + id);
      if (d) d.style.display = (d.style.display === "none") ? "block" : "none";
      setTimeout(refreshLucide, 20);
    }}

    function toggleCourseDone(id) {{
      const isDone = doneCoursesSet.has(id);
      if (isDone) {{
        doneCoursesSet.delete(id);
        localStorage.setItem("otb_done_" + id, "false");
        showToast("تم إلغاء التحديد");
      }} else {{
        doneCoursesSet.add(id);
        localStorage.setItem("otb_done_" + id, "true");
        showToast("👑 تم تسجيل إكمال المقرر بنجاح!");
      }}
      renderCoursesList(coursesData);
    }}

    function filterCourses(cat, btn) {{
      document.querySelectorAll("#section-courses .tab-pill").forEach(p => p.classList.remove("active"));
      btn.classList.add("active");

      if (cat === "all") {{
        renderCoursesList(coursesData);
      }} else {{
        renderCoursesList(coursesData.filter(c => c.cat === cat));
      }}
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
          <div style="margin-bottom: 0.35rem;">
            <i data-lucide="crown" style="width: 48px; height: 48px; color: var(--gold);"></i>
          </div>
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
          <button class="btn btn-secondary" onclick="window.print()">
            <i data-lucide="printer" style="width: 16px; height: 16px;"></i> طباعة الشهادة / حفظ PDF
          </button>
        </div>
      `;
      wrap.scrollIntoView({{ behavior: "smooth" }});
      setTimeout(refreshLucide, 20);
      showToast("👑 تم إصدار شهادة الاعتماد الملكية بنجاح!");
    }}

    // Initial Execution
    document.addEventListener("DOMContentLoaded", () => {{
      renderRolesGrid();
      renderClientsGrid();
      renderCoursesList(coursesData);
      updateLivePrompt();
      refreshLucide();
    }});

    // Instant Execution
    renderRolesGrid();
    renderClientsGrid();
    renderCoursesList(coursesData);
    updateLivePrompt();
    refreshLucide();
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("Applied Bundled Lucide & Three.js to index.html!")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
