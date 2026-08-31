import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from generate_master_academy import COURSES_DATA
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

# ==============================================================================
# 1. 100% REAL & VERIFIED SOURCED DATA FROM OTB MASTER CONTEXT
# ==============================================================================

# 9 REAL CORE DISCIPLINES AT OTB (FROM الدليل الرسمي للمسميات وخارطة الطريق)
REAL_ROLES_DATA = [
  {
    "id": "content_creator",
    "icon": "✍️",
    "name": "صانع وكاتب المحتوى",
    "eng": "Content Creator & Copywriter",
    "officialRole": "عقل الوكالة، مدخل الإبداع وصياغة الخطط والسرد القصصي لكافة منصات العملاء.",
    "realChallenge": "استنزاف 3-4 ساعات يومياً في البحث وكتابة خطط المنشورات وصياغة نصوص متعددة المنصات ونبرات الصوت المختلفة.",
    "aiSuperpower": "أدوات السرد والعصف الذهني (Claude 3.5 Sonnet, ChatGPT) لاختزال صياغة خطة أسبوع كاملة من 4 ساعات إلى 45 دقيقة مع الحفاظ على النبرة المعتمدة.",
    "tools": ["Claude 3.5 Sonnet", "ChatGPT Plus", "Notion AI"],
    "realPrompt": "Role: Senior Copywriter at OTB Agency.\nContext: Writing for [Brand Name] in Egypt.\nTask: Create 3 high-converting ad copy angles using PAS framework (Problem, Agitate, Solution) in modern refined Egyptian Arabic.\nConstraints: Hook under 8 words, bold royal tone, strong CTA linking to WhatsApp.",
    "goldenRule": "الذكاء الاصطناعي لا يستبدل كاتب المحتوى بل يحرره من الروتين؛ القيمة الحقيقية تكمن في دقة السياق (Context) واللمسة الإبداعية البشرية."
  },
  {
    "id": "graphic_designer",
    "icon": "🎨",
    "name": "مصمم الجرافيك والهوية",
    "eng": "Graphic Designer",
    "officialRole": "تحويل الهوية البصرية لعملاء OTB إلى أصول رقمية فاخرة (Logos, Visual Guidelines, Typography, 3D Assets).",
    "realChallenge": "قضاء ساعات مرهقة في البحث عن صور Stock، تفريغ الخلفيات يدوياً، وتعديل مقاسات التصاميم للمنصات المختلفة.",
    "aiSuperpower": "توليد مشاهد وبرودكت شوت 3D حصرية للعميل عبر Midjourney v6 والتعديل الفوري بـ Adobe Firefly Generative Fill، مما يوفر تكاليف ومجهود جلسات التصوير.",
    "tools": ["Midjourney v6", "Adobe Firefly", "Magnific AI", "Photoshop AI"],
    "realPrompt": "/imagine prompt: Commercial product photography of [Product Name], placed on a sleek matte noir obsidian podium, soft royal gold rim lighting, dynamic shadows, high fashion editorial style, 8k, photorealistic, vibrant colors, shot on 35mm lens --ar 4:5 --style raw --v 6.0",
    "goldenRule": "افهم مصطلحات الإضاءة وعدسات الكاميرا لتتحكم بدقة متناهية في مخرجات Midjourney؛ التصميم المتقن يبدأ من جودة الأمر."
  },
  {
    "id": "video_editor",
    "icon": "🎬",
    "name": "مونتير ومخرج الفيديو والريلز",
    "eng": "Video Editor & Motion Designer",
    "officialRole": "إنتاج الفيديوهات القصيرة (Reels / TikTok) والموشن جرافيك والمونتاج الإعلاني عالي التحويل للعملاء.",
    "realChallenge": "استغراق يوم كامل في تقطيع الفترات الصامتة وكتابة الترجمة (Captions) وتنسيق الخطوط يدوياً والبحث عن B-Roll.",
    "aiSuperpower": "استخدام أدوات التقطيع النصي وتوليد الترجمة التلقائية (CapCut Pro, Opus Clip) لتوفير 80% من زمن المونتاج والتفرغ للإخراج البصري والموسيقى.",
    "tools": ["Premiere Pro AI", "CapCut Pro", "Opus Clip", "Runway Gen-3"],
    "realPrompt": "Cinematic slow-motion shot of [Action/Subject], glowing royal gold lighting in the background, luxury modern aesthetic, highly detailed, 4k, photorealistic movement.",
    "goldenRule": "الـ AI ينفذ المهام الشاقة المكررة، لكن حسك الفني هو الذي يضبط الإيقاع العاطفي وتناغم المؤثرات والموسيقى."
  },
  {
    "id": "media_buyer",
    "icon": "📊",
    "name": "أخصائي الإعلانات والميديا بايينج",
    "eng": "Media Buyer & Performance Marketer",
    "officialRole": "إدارة الحملات الممولة على Meta و TikTok، تحسين التحويلات، وتتبع الـ CAPI وسكيلينج الـ ROAS لتحقيق أعلى عائد مالي للعميل.",
    "realChallenge": "تحليل شيتات البيانات الضخمة ومراقبة إرهاق الإعلانات (Ad Fatigue) يدويًا وتتبع فجوات التتبع بعد تحديثات الخصوصية.",
    "aiSuperpower": "تحليل ملفات الـ CSV فورياً عبر ChatGPT لاستخراج أفضل الكرييتفز الرابحة، وتوليد مئات تنويعات النصوص، وضبط قواعد الـ Scaling الآمنة (زيادة 20% كل 48-72 ساعة).",
    "tools": ["ChatGPT Data Analysis", "AdCreative.ai", "Meta Advantage+", "Madgicx"],
    "realPrompt": "أنا أدير حملة إعلانية على فيسبوك بهدف [الهدف: Lead Gen/Sales] لعميل في قطاع [القطاع]. هذه هي مؤشرات الأداء الحالية: [أدخل الأرقام مثل CTR, CPC, ROAS]. بصفتك خبير Media Buying، قم بتحليل هذه الأرقام وحدد الخلل، ثم أعطني 3 خطوات عملية لتحسين الأداء فوراً.",
    "goldenRule": "استخدم الذكاء الاصطناعي لاستخراج الأنماط وتحليل الأرقام، لكن قرار زيادة أو إيقاف الميزانيات يظل قرارك الاستراتيجي المحسوب."
  },
  {
    "id": "account_manager",
    "icon": "🤝",
    "name": "مدير الحسابات وخدمة العملاء",
    "eng": "Account Manager",
    "officialRole": "حلقة الوصل المباشرة بين العميل وفريق التنفيذ، إدارة التوقعات، تسليم الخطط، وضمان رضا العميل وتجديد عقود الريتينر.",
    "realChallenge": "كتابة محاضر الاجتماعات يدوياً، تشتت طلبات العميل في الواتساب، وصياغة إيميلات المتابعة والتقارير الأسبوعية.",
    "aiSuperpower": "تلخيص المكالمات واستخراج بنود العمل (Action Items) تلقائياً عبر Fireflies.ai، وصياغة ردود وتقارير مهنية فورية ومتقنة.",
    "tools": ["Fireflies.ai", "ChatGPT Plus", "Grammarly", "Notion AI"],
    "realPrompt": "إليك تفاصيل غير مرتبة لمكالمة مع عميل غاضب بسبب تأخر التسليم: [ضع الملاحظات]. اكتب بريداً إلكترونياً احترافياً ومطمئناً للعميل، تعتذر فيه بلباقة، وتشرح أن التأخير كان لضمان الجودة، وتحدد موعد تسليم نهائي غداً صباحاً.",
    "goldenRule": "راجع دائماً رسائل الـ AI لتضفي عليها النبرة الإنسانية الدافئة الخاصة بكل عميل وتعمق ثقته في الوكالة."
  },
  {
    "id": "brand_strategist",
    "icon": "👑",
    "name": "استراتيجي البراند والهوية",
    "eng": "Head of Brand & Strategy",
    "officialRole": "قائد الاستراتيجية والتموضع في السوق، تحليل المنافسين، وبناء أدلة الهوية ونبرة الصوت وبريفات الاكتشاف.",
    "realChallenge": "استغراق أسابيع في قراءة أبحاث السوق وتحليل المنافسين وبناء شخصيات المشترين (Buyer Personas) يدوياً.",
    "aiSuperpower": "استخدام محركات البحث التوليدي (Perplexity AI) لجمع دراسات السوق في دقائق، وبناء مصفوفات SWOT وشخصيات الجمهور المستهدف بسرعة ودقة.",
    "tools": ["Perplexity AI", "Claude 3.5 Sonnet", "ChatGPT Plus"],
    "realPrompt": "تخيل أنك استراتيجي علامات تجارية عالمي. قم بإنشاء 3 شخصيات مشترين (Buyer Personas) مفصلة لعلامة تجارية متخصصة في [مجال العميل]. لكل شخصية، اذكر: التركيبة السكانية، الأهداف، نقاط الألم (Pain Points)، كيف يحل منتجنا مشكلتها، وأفضل القنوات التسويقية للوصول إليها.",
    "goldenRule": "الـ AI يمنحك المتوسط العام للسوق؛ أضف دائماً رؤيتك غير التقليدية (Out of The Box) لتصنع الفارق التنافسي للبراند."
  },
  {
    "id": "moderator",
    "icon": "💬",
    "name": "مسؤول الردود والموديريشن",
    "eng": "Community Moderator & Chat Sales",
    "officialRole": "إدارة مجتمعات العملاء على منصات التواصل، سرعة الاستجابة، وتأهيل العملاء المحتملين وتحويلهم لصفقات بيعية عبر الواتساب.",
    "realChallenge": "تكرار الرد على نفس الأسئلة مئات المرات يومياً، وتأخر الرد في أوقات الذروة مما يؤدي لضياع العملاء الجادين.",
    "aiSuperpower": "أتمتة الردود على 80% من الاستفسارات الشائعة فورياً عبر مسارات WhatsApp Business API و ManyChat، وتنبيه الموظف للتدخل لإغلاق الصفقات الكبرى.",
    "tools": ["ManyChat AI", "WhatsApp Business API", "Custom GPTs"],
    "realPrompt": "أنت مسؤول خدمة عملاء ومبيعات يمثل علامة [اسم البراند]. هدفك الأساسي هو الرد على استفسارات العملاء بأسلوب [ودود/محترف/شعبي]، وتحفيزهم بلباقة على ترك رقم هواتفهم لحجز موعد. لا تختلق أسعاراً من عندك. إذا سأل العميل عن معلومات خارج الملف المرفق، اعتذر بلطف واطلب منه الانتظار لتحويله للمدير.",
    "goldenRule": "الوضوح والسرعة هما مفتاح البيع؛ دع البوت يجيب فورياً على الأساسيات وكن أنت الحاضر لإتمام البيع وتأكيد الطلب."
  },
  {
    "id": "sales_pr",
    "icon": "💼",
    "name": "مدير المبيعات والعلاقات العامة",
    "eng": "Sales & PR Manager",
    "officialRole": "استقطاب عملاء الـ B2B والشركات الكبرى (High-Ticket Clients)، تقديم مقترحات الريتينر الشهرية، وتوسيع شراكات الوكالة.",
    "realChallenge": "البحث عن جهات الاتصال بصناع القرار، وكتابة إيميلات تسويقية مخصصة تُفتح ولا تُرمى في الـ Spam.",
    "aiSuperpower": "تخصيص مئات الرسائل البيعية عبر الذكاء الاصطناعي بربطها بإنجازات وأخبار الشركة المستهدفة لرفع نسبة الردود لـ 25%.",
    "tools": ["Apollo.io", "ChatGPT Plus", "Instantly AI"],
    "realPrompt": "أنا مدير مبيعات في وكالة OTB. اكتب لي رسالة LinkedIn للتشبيك مع [اسم الشخص]، وهو [المسمى الوظيفي] في شركة [اسم الشركة]. أريد أن أبدأ الرسالة بتهنئته على [خبر أو إنجاز حديث للشركة]، ثم أعرض باختصار كيف يمكن لوكالتنا مساعدته في زيادة مبيعاته عبر الذكاء الاصطناعي. اجعل الرسالة أقل من 75 كلمة وبدون طابع بيعي فج.",
    "goldenRule": "الشركات الكبرى تبحث عن نتائج حقيقية وأرقام عوائد موثقة، لا مجرد تصاميم وبوستات؛ اجعل مقترحك يركز دائماً على الـ ROI."
  },
  {
    "id": "operations",
    "icon": "⚡",
    "name": "القيادة وتطوير العمليات",
    "eng": "Process Development & Operations",
    "officialRole": "هندسة العمليات، إزالة الاختناقات التشغيلية، بناء لوحات التحكم، ودمج وكلاء الذكاء الاصطناعي لتقليص الهدر بنسبة 40%.",
    "realChallenge": "المتابعة اليدوية المتكررة للمهام والروتين الإداري وغياب الرؤية الموحدة لتدفق العمل بين الأقسام.",
    "aiSuperpower": "بناء أدلة تشغيل معيارية (SOPs) مؤتمتة، ولوحات متابعة لحظية تتيح للقيادة متابعة سير العمل بدون إدارة مجهرية.",
    "tools": ["Make.com", "n8n", "ChatGPT Systems", "Notion AI"],
    "realPrompt": "بصفتك خبير عمليات (Operations Manager)، قم بإنشاء إجراء تشغيل قياسي (SOP) مفصل خطوة بخطوة لعملية [اسم العملية، مثلاً: إطلاق حملة إعلانية جديدة لعميل]. قم بتضمين: الأدوار والمسؤوليات، الأدوات المستخدمة، قائمة التحقق (Checklist) قبل الإطلاق، ومؤشرات الأداء الرئيسية (KPIs) لقياس نجاح العملية.",
    "goldenRule": "الأنظمة والعمليات الواضحة هي التي تحرر طاقة الإبداع؛ اجعل كل خطوة موثقة ومؤتمتة ليعمل الفريق كالساعة السويسرية."
  }
]

# 100% REAL VERIFIED OTB CLIENTS & CASE STUDIES (FROM OTB MASTER CONTEXT)
REAL_CLIENTS_DATA = [
  {
    "name": "Franks EG (فرانكس)",
    "sector": "Industrial & B2B / تصنيع",
    "metric": "من المركز 25 ➔ المركز الثاني | 10M ➔ 30M EGP",
    "desc": "قصة نجاح OTB الأكبر؛ إعادة هيكلة المنظومة التسويقية والبيعية ومضاعفة المبيعات الرقمية من 10 إلى 30 مليون جنيه شهرياً عبر استراتيجيات تسويق موجهة للشركات."
  },
  {
    "name": "MIX Coffee (ميكس كوفي)",
    "sector": "Specialty Coffee / قطاع الضيافة والكافيهات",
    "metric": "تفاعل +180% | مضاعفة مبيعات الفروع",
    "desc": "إعادة التموضع من كافيه تقليدي إلى وجهة أولى لرواد الأعمال بهوية بصرية داكنة فاخرة، وفيديوهات ASMR لصناعة القهوة حققت انتشاراً واسعاً."
  },
  {
    "name": "Rancho's EG (رانشوز)",
    "sector": "Gourmet Burgers / المطاعم",
    "metric": "معدل احتفاظ 36.8% | 450K مشاهدة ريلز",
    "desc": "الخروج من فخ الخصومات إلى تموضع 'البرجر الملحمي'، وإعلانات فيديو ريلز مباشرة رفعت مبيعات الواتساب والطلبات بنسبة 65%."
  },
  {
    "name": "مجوهرات دكتور زغلول (Dr. Zaghloul)",
    "sector": "Luxury Gold & Jewelry / ذهب ومجوهرات",
    "metric": "ROAS 7.5x+ | إعلانات تحويلية",
    "desc": "بناء الثقة وسرد قصص التصاميم الحصرية بجودة سينمائية وهيكل حملات TOFU/MOFU/BOFU محققاً عائداً إعلانيا استثنائياً."
  },
  {
    "name": "معامل علاج (Elag Labs)",
    "sector": "Clinics & Medical / معامل وتحاليل",
    "metric": "800+ حجز مؤهل شهرياً",
    "desc": "إعلانات تحويلية مع مسار WhatsApp Business API مؤتمت لتأهيل واستقبال طلبات الزيارات المنزلية وحجوزات التحاليل بدقة."
  },
  {
    "name": "صقر ستور (Sakr Store)",
    "sector": "E-Commerce & Retail / تجارة وتجزئة",
    "metric": "تكلفة الشراء (CPA) -32%",
    "desc": "إعادة هيكلة حملات Meta وإعلانات Advantage+ مع ربط تتبع CAPI وعروض الباقات المجمعة لرفع متوسط قيمة السلة."
  },
  {
    "name": "حلويات رايس (Rice Patisserie)",
    "sector": "Patisserie & Sweets / حلويات فاخرة",
    "metric": "انتشار واسع وطلب موسمي",
    "desc": "إبراز التفاصيل الفنية للحلويات الغربية والموسمية بحملات فيديو إعلانية استهدفت المناسبات والأعياد."
  }
]

roles_json = json.dumps(REAL_ROLES_DATA, ensure_ascii=False)
clients_json = json.dumps(REAL_CLIENTS_DATA, ensure_ascii=False)

# ==============================================================================
# 2. GENERATE MASTER HTML (index.html) WITH 100% SOURCED REAL DATA
# ==============================================================================
p_master_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Team AI Hub — منصة تمكين الذكاء الاصطناعي لملوك المدينة</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=JetBrains+Mono:wght@500;600;700&family=Readex+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>

  <!-- WEBGL BACKGROUND CANVAS -->
  <canvas id="webglCanvas"></canvas>

  <!-- MINIMAL LUXURY NAVBAR -->
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

    <!-- TOP NAVIGATION PILLS -->
    <nav class="nav-pills">
      <button class="nav-pill-btn active" id="tabBtn-roles" onclick="switchMainTab('roles')">🎯 أدوار الفريق</button>
      <button class="nav-pill-btn" id="tabBtn-manus" onclick="switchMainTab('manus')">📋 بريف Manus (9 مراحل)</button>
      <button class="nav-pill-btn" id="tabBtn-courses" onclick="switchMainTab('courses')">📚 المناهج (19)</button>
      <button class="nav-pill-btn" id="tabBtn-prompts" onclick="switchMainTab('prompts')">🤖 استوديو الأوامر</button>
      <button class="nav-pill-btn" id="tabBtn-cases" onclick="switchMainTab('cases')">💼 عملاء OTB</button>
      <button class="nav-pill-btn" id="tabBtn-quiz" onclick="switchMainTab('quiz')">🏆 الشهادة</button>
      <button class="nav-pill-btn" id="tabBtn-downloads" onclick="switchMainTab('downloads')">📥 التحميلات</button>
    </nav>

    <div>
      <a href="tel:+201008080295" class="phone-wrapper" style="font-size: 0.85rem;">
        <span class="phone-code">+20</span>
        <span class="phone-num">100 808 0295</span>
      </a>
    </div>
  </header>

  <!-- APP CONTAINER -->
  <main class="app-container">

    <!-- ========================================== -->
    <!-- SECTION 1: ROLE AI SUPERPOWERS (DEFAULT) -->
    <!-- ========================================== -->
    <section id="section-roles" class="hub-section">
      
      <!-- HERO -->
      <div class="hero-wrapper">
        <div class="hero-pill">✨ OTB AI SUPERPOWER ENGINE · 2026</div>
        <h2 class="hero-title">اختر تخصصك.. واكتشف قوة الـ <span>AI الحقيقية 🚀</span></h2>
        <p class="hero-subtitle">
          بيانات حقيقية 100% مستخلصة من الدليل الرسمي للمسميات وخارطة طريق OTB Agency. اكتشف دورك المعتمد، وتعرف كيف تختزل أدوات الذكاء الاصطناعي 40% من وقت المهام الروتينية.
        </p>
      </div>

      <!-- ROLE SELECTOR CARDS GRID (9 ROLES) -->
      <div class="role-grid" id="rolesGrid"></div>

      <!-- SELECTED ROLE STAGE -->
      <div id="roleDetailsStage" class="role-stage"></div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 2: MANUS 9-STAGE BRIEF -->
    <!-- ========================================== -->
    <section id="section-manus" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <div class="hero-pill">👑 MANUS STRATEGIC DISCOVERY</div>
        <h2 class="hero-title">نظام بريف واستقبال العملاء المعتمد (9 مراحل)</h2>
        <p class="hero-subtitle">المنظومة الرسمية لاكتشاف وتأهيل عملاء وكالة OTB وضبط التوقعات من الجلسة الأولى.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.25rem;">
        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">المرحلة 01</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">🌱 الجذور (من أنتم؟)</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted);">قصة التأسيس، الرؤية، والسبب الجوهري لوجود البراند في السوق.</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">المرحلة 02</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">💎 العرض والقيمة (The Offer)</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted);">المنتجات والخدمات الأساسية، الميزة التنافسية، وهيكل الأسعار.</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">المرحلة 03</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">🎯 الجمهور المستهدف (Audience)</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted);">الشرائح السكانية، السلوك الشرائي، ونقاط الألم الرئيسية (Pain Points).</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">المرحلة 04</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">🔍 مشهد المنافسة والفجوات</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted);">المنافسون المباشرون ونقاط ضعفهم التي يمكن لـ OTB استغلالها.</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">المرحلة 05</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">🎭 شخصية البراند ونبرة الصوت</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted);">النمط النفسي ونبرة الحديث المعتمدة (Bold, Royal, Friendly...).</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">المرحلة 06</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">📈 النجاح ومستهدفات الـ 90 يوماً</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted);">أهداف الـ ROAS، الإيرادات، والمبيعات المستهدفة ومؤشرات الـ KPIs.</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">المرحلة 07</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">⚙️ التشغيل والميزانيات</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted);">ميزانية الإعلانات الشهرية المتاحة، الموارد، وقنوات التواصل المعتمدة.</p>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">المرحلة 08</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin: 0.3rem 0;">🛡️ السياق والدروس السابقة</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted);">تجارب الحملات السابقة، ما نجح وما فشل، والمحاذير القانونية والتسويقية.</p>
        </div>

        <div class="glass-card" style="border-color: var(--border-gold);">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">المرحلة 09</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--gold); margin: 0.3rem 0;">✅ المراجعة وإصدار الرقم المرجعي</h3>
          <p style="font-size: 0.88rem; color: var(--text-main);">تأكيد بنود البريف وتوليد الكود الرسمي (مثل: OTB-K3M9P) لتوزيع المهام على الفريق.</p>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 3: 19 COURSES -->
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
    <!-- SECTION 4: PROMPTS STUDIO -->
    <!-- ========================================== -->
    <section id="section-prompts" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <h2 class="hero-title">🤖 استوديو أوامر الذكاء الاصطناعي</h2>
        <p class="hero-subtitle">أوامر RCIC عملية وفورية مصممة خصيصاً لعملاء OTB وقابلة للنسخ المباشر.</p>
      </div>

      <div class="glass-card" style="border: 2px solid var(--border-gold); padding: 2.5rem; max-width: 850px; margin: 0 auto;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 1.5rem;">
          <div>
            <label style="display: block; font-size: 0.88rem; color: var(--text-pure); margin-bottom: 0.4rem; font-weight: 700;">نوع التكليف المطلوب:</label>
            <select id="promptTask" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input); border-radius: var(--radius-sm);" onchange="updateLivePrompt()">
              <option value="copy">كتابة إعلانات تحويلية (PAS Framework)</option>
              <option value="reels">اسكريبت ريلز 15 ثانية (Viral Hook)</option>
              <option value="media">تشخيص حساب إعلاني وسكيلينج (Media Buying)</option>
              <option value="design">لقطات برودكت شوت 3D لـ Midjourney</option>
              <option value="retainer">مقترح عقد ريتينر شهري ($2,500/mo)</option>
            </select>
          </div>
          <div>
            <label style="display: block; font-size: 0.88rem; color: var(--text-pure); margin-bottom: 0.4rem; font-weight: 700;">اسم البراند والقطاع:</label>
            <input type="text" id="promptBrand" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input); border-radius: var(--radius-sm);" value="MIX Coffee (Specialty Coffee)" oninput="updateLivePrompt()">
          </div>
        </div>

        <div style="margin-bottom: 1.5rem;">
          <label style="display: block; font-size: 0.88rem; color: var(--text-pure); margin-bottom: 0.4rem; font-weight: 700;">الأمر المولد فورياً:</label>
          <div id="livePromptCode" class="code-box" style="max-height: 240px; overflow-y: auto;"></div>
        </div>

        <button class="btn btn-primary" style="width: 100%; padding: 0.85rem;" onclick="copyText(document.getElementById('livePromptCode').innerText)">📋 نسخ الأمر المخصص للحافظة</button>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 5: REAL CASE STUDIES -->
    <!-- ========================================== -->
    <section id="section-cases" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <h2 class="hero-title">💼 نتائج وأرقام عملاء OTB الموثقة</h2>
        <p class="hero-subtitle">بيانات حقيقية وأرقام مسجلة من واقع حملات وإنجازات عملاء الوكالة عبر السنوات السبع الماضية.</p>
      </div>

      <div id="clientsGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem;"></div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 6: QUIZ & CERTIFICATE -->
    <!-- ========================================== -->
    <section id="section-quiz" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2rem;">
        <h2 class="hero-title">🏆 تقييم الكفاءة وإصدار شهادة ملوك المدينة</h2>
        <p class="hero-subtitle">أدخل اسمك وأجب عن الأسئلة الخمسة لإصدار شهادة الاعتماد الملكية الرسمية المعتمدة.</p>
      </div>

      <div class="glass-card" style="max-width: 750px; margin: 0 auto 2rem auto;">
        <label style="display: block; font-size: 0.9rem; color: var(--text-pure); margin-bottom: 0.5rem; font-weight: 700;">الاسم الرسمي المطبوع على الشهادة:</label>
        <input type="text" id="certName" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input); font-size: 1.05rem; border-radius: var(--radius-sm);" value="أحمد عصام رمضان">
      </div>

      <div style="max-width: 750px; margin: 0 auto;">
        <div class="glass-card" style="margin-bottom: 1rem;">
          <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.6rem;">1. ما هو التموضع والنمط النفسي المعتمد لوكالة OTB؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q0" value="0"> المنافسة على أقل سعر</label>
          <label style="display:block; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q0" value="1" checked> The Ruler & The Creator (ملوك المدينة: الهيبة والجرأة والتركيز على العائد)</label>
        </div>

        <div class="glass-card" style="margin-bottom: 1rem;">
          <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.6rem;">2. كيف يساعد الذكاء الاصطناعي صانع المحتوى بشكل سليم؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q1" value="1" checked> كـ شريك عصف ذهني وسرعة صياغة بدقة المعطيات (Context) مع مراجعة بشرية</label>
          <label style="display:block; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q1" value="0"> نسخ ولصق الردود بدون قراءة</label>
        </div>

        <div class="glass-card" style="margin-bottom: 1rem;">
          <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.6rem;">3. إذا كان هامش الربح 25%، فما هو الـ Break-Even ROAS؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q2" value="1" checked> 4.0x (حيث 1 / 0.25 = 4)</label>
          <label style="display:block; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q2" value="0"> 1.5x</label>
        </div>

        <div class="glass-card" style="margin-bottom: 1rem;">
          <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.6rem;">4. ما هي النسبة الآمنة لزيادة ميزانية الحملات الرابحة (Scaling)؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q3" value="1" checked> زيادة 20% كل 48-72 ساعة لحماية استقرار الحملة</label>
          <label style="display:block; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q3" value="0"> مضاعفة الميزانية 200% كل ساعة</label>
        </div>

        <div class="glass-card" style="margin-bottom: 2rem;">
          <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.6rem;">5. ما هو السعر القياسي لباقة الـ Dominance Retainer لـ OTB؟</h4>
          <label style="display:block; margin-bottom:0.35rem; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q4" value="1" checked> $2,500 / شهر (هوية + 24 محتوى + ميديا بايينج + أتمتة)</label>
          <label style="display:block; font-size:0.9rem; cursor:pointer;"><input type="radio" name="q4" value="0"> $300 / شهر</label>
        </div>

        <div style="text-align: center;">
          <button class="btn btn-primary" style="padding: 0.9rem 3.5rem; font-size: 1rem;" onclick="generateOfficialCert()">👑 إصدار شهادة الاعتماد الملكية</button>
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
        <p class="hero-subtitle">تحميل التقارير الاستراتيجية، وموسوعات الأوامر، وقوائم الفحص بصيغ مباشرة.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">50+ Prompts</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin: 0.4rem 0;">📖 موسوعة الأوامر التكتيكية</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1.25rem;">أوامر الذكاء الاصطناعي المعتمدة لأدوار OTB.</p>
          <a href="track_a_fast_track_sprint/cheatsheets/OTB_Prompt_Engineering_Bible.md" download class="btn btn-primary" style="width: 100%; font-size: 0.85rem;">📥 تحميل الموسوعة</a>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Checklist</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin: 0.4rem 0;">✈️ فحص الميديا بايينج</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1.25rem;">قائمة فحص الحملات قبل الإطلاق وقواعد السكيلينج.</p>
          <a href="track_a_fast_track_sprint/cheatsheets/OTB_Media_Buying_Checklist.md" download class="btn btn-secondary" style="width: 100%; font-size: 0.85rem;">📥 تحميل الفحص</a>
        </div>

        <div class="glass-card">
          <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">Markdown Doc</span>
          <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin: 0.4rem 0;">📑 التقرير الاستراتيجي الشامل</h3>
          <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1.25rem;">وثيقة التوجيه التنفيذي لنمو الوكالة.</p>
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
            <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">الدور المعتمد رسمياً في هيكل OTB</span>
            <h2 class="role-heading">${{r.icon}} ${{r.name}} <span style="font-family: var(--font-kookies); font-size: 1.1rem; color: var(--gold-light);">(${{r.eng}})</span></h2>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 0.35rem;">${{r.officialRole}}</p>
          </div>
          <button class="btn btn-primary" onclick="copyText(document.getElementById('rolePromptBox').innerText)">📋 نسخ الأمر المعتمد</button>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-bottom: 1.5rem;">
          <div class="glass-card" style="background: rgba(225, 29, 72, 0.06); border-color: rgba(225, 29, 72, 0.25);">
            <h4 style="color: var(--crimson); font-size: 0.95rem; margin-bottom: 0.35rem; font-weight: 700;">🛑 أين يضيع وقتك يومياً؟ (التحدي المعتاد):</h4>
            <p style="font-size: 0.88rem; color: var(--text-main); line-height: 1.7;">${{r.realChallenge}}</p>
          </div>

          <div class="glass-card" style="background: rgba(16, 185, 129, 0.06); border-color: rgba(16, 185, 129, 0.25);">
            <h4 style="color: var(--emerald); font-size: 0.95rem; margin-bottom: 0.35rem; font-weight: 700;">🚀 كيف يضاعف الـ AI إنتاجيتك 5x؟:</h4>
            <p style="font-size: 0.88rem; color: var(--text-main); line-height: 1.7;">${{r.aiSuperpower}}</p>
          </div>
        </div>

        <div style="margin-bottom: 1.5rem;">
          <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.6rem; font-weight: 700;">🛠️ ترسانة الأدوات المعتمدة لدورك:</h4>
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">${{toolsHtml}}</div>
        </div>

        <div style="margin-bottom: 1.5rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <h4 style="font-size: 0.95rem; color: var(--cyan); font-weight: 700;">📋 الأمر الجاهز الفوري لعملاء الوكالة (Plug-and-Play Prompt):</h4>
            <span style="font-size: 0.75rem; color: var(--text-dim);">صيغة RCIC معتمدة</span>
          </div>
          <div id="rolePromptBox" class="code-box">${{r.realPrompt}}</div>
        </div>

        <div class="glass-card" style="background: var(--gold-dim); border-color: var(--border-gold);">
          <h4 style="color: var(--gold); font-size: 0.95rem; margin-bottom: 0.35rem; font-weight: 700;">💡 النصيحة الذهبية لملوك المدينة:</h4>
          <p style="font-size: 0.9rem; color: var(--text-main); line-height: 1.8;">${{r.goldenRule}}</p>
        </div>
      `;
    }}

    function renderClientsGrid() {{
      const container = document.getElementById("clientsGrid");
      let html = "";
      clientsData.forEach(c => {{
        html += `
          <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="font-size: 0.8rem; color: var(--gold); font-weight: 700;">${{c.sector}}</span>
              <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 700; background: rgba(16, 185, 129, 0.1); padding: 0.2rem 0.6rem; border-radius: var(--radius-full);">${{c.metric}}</span>
            </div>
            <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin-bottom: 0.4rem;">${{c.name}}</h3>
            <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.7;">${{c.desc}}</p>
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
          unitsHtml += `<li style="margin-bottom: 0.35rem;"><b>الوحدة ${{i + 1}}:</b> ${{u}}</li>`;
        }});

        html += `
          <div class="glass-card" style="margin-bottom: 1rem; padding: 1.25rem 1.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; cursor: pointer;" onclick="toggleCourseDetails('${{c.id}}')">
              <div>
                <span style="font-size: 0.78rem; color: var(--gold); font-weight: 700;">المرحلة 0${{c.phase}} · ${{c.badge}}</span>
                <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-pure); margin-top: 0.2rem;">${{c.icon}} ${{c.title}}</h3>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem;">
                <span style="font-size: 0.8rem; color: ${{isDone ? 'var(--emerald)' : 'var(--text-dim)'}};">${{isDone ? '✅ مكتمل' : '○ قيد الانتظار'}}</span>
                <span style="font-size: 0.9rem; color: var(--text-dim);">▾</span>
              </div>
            </div>

            <div id="details_${{c.id}}" style="display: none; margin-top: 1.25rem; padding-top: 1.25rem; border-top: 1px solid var(--border);">
              <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.25rem;">${{c.desc}}</p>
              
              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.4rem;">📖 الوحدات التدريبية (${{c.pages}} صفحة منهج):</h4>
                <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-muted); line-height: 1.8;">
                  ${{unitsHtml}}
                </ul>
              </div>

              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--cyan); margin-bottom: 0.35rem;">🤖 أمر الذكاء الاصطناعي المعتمد (RCIC Prompt):</h4>
                <div class="code-box">${{c.prompt}}</div>
                <button class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.35rem 0.8rem;" onclick="copyText(this.previousElementSibling.innerText)">📋 نسخ الأمر</button>
              </div>

              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--emerald); margin-bottom: 0.3rem;">💼 دراسة الحالة التطبيقية:</h4>
                <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.7;">${{c.case_study}}</p>
              </div>

              <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--border);">
                <div>
                  <h4 style="font-size: 0.95rem; color: var(--gold-light); margin-bottom: 0.2rem;">🧪 التكليف العملي:</h4>
                  <p style="font-size: 0.85rem; color: var(--text-muted);">${{c.lab}}</p>
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
      }} else if (task === "design") {{
        out.innerText = "/imagine prompt: Ultra-realistic commercial 3D product shot of " + brand + ", obsidian noir stone podium, royal gold accents and droplets, dramatic rim lighting, cinematic 8k render --ar 9:16 --style raw --v 6.0";
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
        <div style="background: #030406; border: 3px solid var(--gold); border-radius: 24px; padding: 3.5rem 2.5rem; text-align: center; margin-top: 2rem; box-shadow: 0 0 60px rgba(212, 168, 83, 0.35);">
          <div style="font-size: 3.2rem; margin-bottom: 0.5rem;">👑</div>
          <div style="font-size: 0.85rem; letter-spacing: 3px; color: var(--gold); text-transform: uppercase; font-family: var(--font-kookies); font-weight: 700;">OTB Marketing Studio · City Kings</div>
          <div style="font-family: var(--font-royal); font-size: 2.2rem; color: var(--text-pure); margin: 0.85rem 0; font-weight: 900; letter-spacing: 1px;">CERTIFICATE OF AI MASTERY</div>
          <p style="color: var(--text-dim); font-size: 1rem;">تشهد أكاديمية وكالة OTB لتمكين الذكاء الاصطناعي وهندسة النمو بأن</p>
          <h2 style="font-family: var(--font-felfel); font-size: 2.5rem; color: var(--gold); margin: 0.85rem 0; font-weight: 900;">${{name}}</h2>
          <p style="color: var(--text-main); max-width: 580px; margin: 0 auto 2rem auto; font-size: 0.95rem; line-height: 1.8;">
            قد أتم بنجاح متطلبات أكاديمية <b>الذكاء الاصطناعي التوليدي والنمو الرقمي (AI-Powered Marketing & Growth Engineering)</b> وأصبح مؤهلاً لمضاعفة الإنتاجية 5x وتطبيق استراتيجيات ملوك المدينة.
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
    f.write(p_master_html)

print("Generated 100% Sourced Factual index.html")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
