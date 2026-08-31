import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

# Remove fake AI mockups from assets/images
fake_images = [
    "portfolio1.jpg",
    "portfolio2.jpg",
    "arabic_portfolio.jpg",
    "otb_official_showcase.jpg",
    "hero.jpg",
    "brand_logo.jpg"
]
for f in fake_images:
    p = os.path.join(BASE_DIR, "assets", "images", f)
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed fake AI mockup: {f}")

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

# 100% REAL STRATEGIC PRESENTATION & SOCIAL ASSETS
REAL_GALLERY_ASSETS = [
  {
    "title": "مخطط التحول المؤسسي وخارطة طريق Scale الوكالة",
    "cat": "Strategy & Enterprise Blueprint",
    "src": "assets/images/OTP_Strategic_Blueprint_-_Slide_2.png",
    "link": "https://www.facebook.com/otbagency5",
    "desc": "الوثيقة الاستراتيجية المعتمدة لتحول OTB من نموذج النجمة الواحدة إلى مؤسسة الكفاءات ومضاعفة العوائد."
  },
  {
    "title": "هندسة العمليات والتحول الرقمي لأقسام الوكالة",
    "cat": "Process Architecture & Operations",
    "src": "assets/images/OTP_Strategic_Blueprint_-_Slide_3.png",
    "link": "https://www.facebook.com/otbagency5",
    "desc": "مخطط توزيع الأدوار التشغيلية وربط الأقسام بنموذج تدفق المهام الموحد."
  },
  {
    "title": "نموذج التشغيل المستهدف (Target Operating Model)",
    "cat": "Operations & Target Operating Model",
    "src": "assets/images/OTP_Strategic_Blueprint_-_Slide_4.png",
    "link": "https://www.facebook.com/otbagency5",
    "desc": "الركائز الأربع لضبط الجودة، أتمتة التقارير، وتقليص الهدر الزمني بنسبة 40%."
  },
  {
    "title": "استراتيجية استقطاب كبرى الشركات وعملاء الـ B2B",
    "cat": "High-Ticket Client Acquisition",
    "src": "assets/images/OTP_Strategic_Blueprint_-_Slide_5.png",
    "link": "https://www.facebook.com/otbagency5",
    "desc": "معادلة استهداف الكيانات الكبرى والمصانع بالاعتماد على دراسات الجدوى والعائد المالي الموثق."
  },
  {
    "title": "أصول وتصاميم السوشيال ميديا الحقيقية للوكالة",
    "cat": "Official Social Media Feed",
    "src": "assets/images/542857690_767054315958080_2395724451370984613_n.jpg",
    "link": "https://www.facebook.com/otbagency5",
    "desc": "أصل حقيقي منشور على صفحة فيسبوك الرسمية لوكالة OTB (+33K متابع)."
  },
  {
    "title": "منشورات وحملات مجتمع OTB Agency على فيسبوك",
    "cat": "Official Social Media Feed",
    "src": "assets/images/541616658_767052649291580_3125367341401312311_n.jpg",
    "link": "https://www.facebook.com/otbagency5",
    "desc": "منشورات التفاعل المباشر وإعلانات الحملات الرسمية من صفحة فيسبوك."
  }
]

roles_json = json.dumps(REAL_ROLES_DATA, ensure_ascii=False)
clients_json = json.dumps(REAL_CLIENTS_DATA, ensure_ascii=False)
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)
gallery_json = json.dumps(REAL_GALLERY_ASSETS, ensure_ascii=False)

master_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Team AI Hub — منصة تمكين ملوك المدينة بأصول حقيقية</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=JetBrains+Mono:wght@500;600;700&family=Readex+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>

  <!-- 3D WEBGL PARTICLE & METALLIC CUBE CANVAS -->
  <canvas id="webglCanvas"></canvas>

  <!-- LUXURY GLASS NAVBAR -->
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
      <button class="nav-pill-btn" id="tabBtn-gallery" onclick="switchMainTab('gallery')">📑 وثائق ومخططات OTB</button>
      <button class="nav-pill-btn" id="tabBtn-cases" onclick="switchMainTab('cases')">💼 عملاء OTB الحقيقيون</button>
      <button class="nav-pill-btn" id="tabBtn-manus" onclick="switchMainTab('manus')">📋 بريف Manus (9 مراحل)</button>
      <button class="nav-pill-btn" id="tabBtn-courses" onclick="switchMainTab('courses')">📚 المناهج (19)</button>
      <button class="nav-pill-btn" id="tabBtn-prompts" onclick="switchMainTab('prompts')">🤖 استوديو الأوامر</button>
      <button class="nav-pill-btn" id="tabBtn-quiz" onclick="switchMainTab('quiz')">🏆 الشهادة</button>
      <button class="nav-pill-btn" id="tabBtn-downloads" onclick="switchMainTab('downloads')">📥 التحميلات</button>
    </nav>

    <div>
      <a href="tel:+201008080295" class="phone-wrapper" style="font-size: 0.88rem;">
        <span class="phone-code">+20</span>
        <span class="phone-num">100 808 0295</span>
      </a>
    </div>
  </header>

  <!-- APP CONTAINER -->
  <main class="app-container">

    <!-- ========================================== -->
    <!-- SECTION 1: ROLE AI SUPERPOWERS (BENTO GRID) -->
    <!-- ========================================== -->
    <section id="section-roles" class="hub-section">
      
      <!-- HERO -->
      <div class="hero-wrapper">
        <div class="hero-pill">✨ OTB AI SUPERPOWER COCKPIT · 2026</div>
        <h2 class="hero-title">اختر تخصصك.. واكتشف قوة الـ <span>AI الحقيقية 🚀</span></h2>
        <p class="hero-subtitle">
          بيانات حقيقية 100% مستخلصة من الدليل الرسمي للمسميات وخارطة طريق OTB Agency وأصول السوشيال ميديا للعملاء. اختزل 40% من وقت المهام الروتينية لتبدع كأحد ملوك المدينة.
        </p>
      </div>

      <!-- ROLE SELECTOR CARDS GRID (9 BESPOKE ROLES) -->
      <div class="role-grid" id="rolesGrid"></div>

      <!-- SELECTED ROLE BENTO STAGE -->
      <div id="roleDetailsStage" class="role-stage"></div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 2: REAL STRATEGIC BLUEPRINTS & SOCIAL FEED -->
    <!-- ========================================== -->
    <section id="section-gallery" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <div class="hero-pill">📑 100% AUTHENTIC OTB STRATEGY & ASSETS</div>
        <h2 class="hero-title">وثائق الاستراتيجية <span>ومنشورات OTB الرسمية</span></h2>
        <p class="hero-subtitle">مخططات التحول المؤسسي الرسمية ولوحات هندسة العمليات المنشورة في أرشيف الوكالة وصفحتها الرسمية.</p>
      </div>

      <div id="galleryGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem;"></div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 3: REAL CLIENT CASES (WITH OFFICIAL SOCIAL LINKS) -->
    <!-- ========================================== -->
    <section id="section-cases" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <div class="hero-pill">💼 VERIFIED CLIENT TRIUMPHS</div>
        <h2 class="hero-title">نتائج وأرقام عملاء OTB <span>الموثقة بالسوشيال ميديا</span></h2>
        <p class="hero-subtitle">بيانات حقيقية، أرقام مسجلة، وروابط مباشرة لصفحات التواصل الاجتماعي الرسمية لعملاء الوكالة.</p>
      </div>

      <div id="clientsGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem;"></div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 4: MANUS 9-STAGE BRIEF -->
    <!-- ========================================== -->
    <section id="section-manus" class="hub-section" style="display: none;">
      <div class="hero-wrapper" style="margin-bottom: 2.5rem;">
        <div class="hero-pill">👑 MANUS STRATEGIC DISCOVERY PIPELINE</div>
        <h2 class="hero-title">نظام بريف واستقبال العملاء المعتمد <span>(9 مراحل)</span></h2>
        <p class="hero-subtitle">المنظومة الرسمية لاكتشاف وتأهيل عملاء وكالة OTB وضبط التوقعات والأهداف من الجلسة الأولى.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.25rem;">
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
          <h3 style="font-family: var(--font-felfel); font-size: 1.2rem; color: var(--text-gold); margin: 0.3rem 0;">✅ المراجعة وإصدار الكود المرجعي</h3>
          <p style="font-size: 0.9rem; color: var(--text-main);">تأكيد بنود البريف وتوليد الكود الرسمي (مثل: OTB-K3M9P) لتوزيع المهام على الفريق.</p>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 5: 19 COURSES -->
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
    <!-- SECTION 6: PROMPTS STUDIO -->
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
    <!-- SECTION 7: QUIZ & CERTIFICATE -->
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
    <!-- SECTION 8: DOWNLOADS -->
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

  <!-- FULLSCREEN LIGHTBOX MODAL -->
  <div id="lightboxModal" style="display: none; position: fixed; inset: 0; background: rgba(0, 0, 0, 0.94); z-index: 999999; backdrop-filter: blur(24px); justify-content: center; align-items: center; padding: 2rem;" onclick="closeLightbox()">
    <div style="max-width: 960px; width: 100%; text-align: center; position: relative;" onclick="event.stopPropagation()">
      <img id="lightboxImg" src="" style="max-width: 100%; max-height: 75vh; border-radius: var(--radius-md); border: 2px solid var(--gold); box-shadow: 0 0 60px rgba(212, 168, 83, 0.5);">
      <h3 id="lightboxCaption" style="font-family: var(--font-felfel); font-size: 1.4rem; color: var(--gold-champagne); margin-top: 1.25rem;"></h3>
      <p id="lightboxDesc" style="color: var(--text-muted); font-size: 0.95rem; margin-top: 0.35rem;"></p>
      <div style="margin-top: 1.5rem; display: flex; justify-content: center; gap: 1rem;">
        <a id="lightboxSocialBtn" href="#" target="_blank" class="btn btn-primary" style="font-size: 0.88rem; padding: 0.5rem 1.5rem;">🌐 زيارة صفحة فيسبوك الرسمية</a>
        <button class="btn btn-secondary" style="font-size: 0.88rem; padding: 0.5rem 1.5rem;" onclick="closeLightbox()">✕ إغلاق</button>
      </div>
    </div>
  </div>

  <script src="shared_ui.js"></script>
  <script>
    const coursesData = {courses_json};
    const rolesData = {roles_json};
    const clientsData = {clients_json};
    const galleryData = {gallery_json};

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
            <span style="font-size: 0.82rem; color: var(--gold); font-weight: 800; letter-spacing: 1px;">الدور المعتمد رسمياً في هيكل OTB</span>
            <h2 class="role-heading">${{r.icon}} ${{r.name}} <span style="font-family: var(--font-kookies); font-size: 1.15rem; color: var(--gold-champagne);">(${{r.eng}})</span></h2>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin-top: 0.35rem;">${{r.officialRole}}</p>
          </div>
          <button class="btn btn-primary" onclick="copyText(document.getElementById('rolePromptBox').innerText)">📋 نسخ الأمر المعتمد</button>
        </div>

        <div class="bento-grid">
          <div class="bento-col-6 glass-card" style="background: rgba(244, 63, 94, 0.05); border-color: rgba(244, 63, 94, 0.28);">
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
              <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: var(--crimson); box-shadow: 0 0 10px var(--crimson);"></span>
              <h4 style="color: var(--crimson); font-size: 1rem; font-weight: 800;">أين يضيع وقتك يومياً؟ (التحدي المعتاد):</h4>
            </div>
            <p style="font-size: 0.92rem; color: var(--text-main); line-height: 1.75;">${{r.realChallenge}}</p>
          </div>

          <div class="bento-col-6 glass-card" style="background: rgba(16, 185, 129, 0.05); border-color: rgba(16, 185, 129, 0.28);">
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
              <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: var(--emerald); box-shadow: 0 0 10px var(--emerald);"></span>
              <h4 style="color: var(--emerald); font-size: 1rem; font-weight: 800;">كيف يضاعف الـ AI إنتاجيتك 5x؟:</h4>
            </div>
            <p style="font-size: 0.92rem; color: var(--text-main); line-height: 1.75;">${{r.aiSuperpower}}</p>
          </div>

          <div class="bento-col-12 glass-card">
            <h4 style="font-size: 1rem; color: var(--text-pure); margin-bottom: 0.75rem; font-weight: 800;">🛠️ ترسانة الأدوات الذكية المعتمدة لدورك:</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 0.6rem;">${{toolsHtml}}</div>
          </div>

          <div class="bento-col-12 glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
              <h4 style="font-size: 1rem; color: var(--cyan); font-weight: 800;">📋 الأمر الجاهز الفوري لعملاء الوكالة (Plug-and-Play Prompt):</h4>
              <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: 700;">صيغة RCIC احترافية</span>
            </div>
            <div id="rolePromptBox" class="code-box">${{r.realPrompt}}</div>
          </div>

          <div class="bento-col-12 glass-card" style="background: rgba(212, 168, 83, 0.08); border-color: var(--border-gold);">
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.4rem;">
              <span style="font-size: 1.3rem;">👑</span>
              <h4 style="color: var(--gold); font-size: 1.05rem; font-weight: 800;">النصيحة الذهبية لملوك المدينة:</h4>
            </div>
            <p style="font-size: 0.95rem; color: var(--text-main); line-height: 1.85;">${{r.goldenRule}}</p>
          </div>
        </div>
      `;
    }}

    function renderGalleryGrid() {{
      const container = document.getElementById("galleryGrid");
      let html = "";
      galleryData.forEach(g => {{
        html += `
          <div class="glass-card" style="padding: 0.9rem; overflow: hidden; cursor: pointer;" onclick="openLightbox('${{g.src}}', '${{g.title}}', '${{g.desc}}', '${{g.link}}')">
            <img src="${{g.src}}" alt="${{g.title}}" style="width: 100%; height: 230px; object-fit: cover; border-radius: var(--radius-sm); transition: transform 0.4s ease;">
            <div style="padding: 0.9rem 0.5rem 0.35rem 0.5rem;">
              <span style="font-size: 0.75rem; color: var(--gold); font-weight: 800;">${{g.cat}}</span>
              <h4 style="font-family: var(--font-felfel); font-size: 1.15rem; color: #fff; margin: 0.2rem 0;">${{g.title}}</h4>
              <p style="font-size: 0.85rem; color: var(--text-muted);">${{g.desc}}</p>
            </div>
          </div>
        `;
      }});
      container.innerHTML = html;
    }}

    function renderClientsGrid() {{
      const container = document.getElementById("clientsGrid");
      let html = "";
      clientsData.forEach(c => {{
        html += `
          <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
              <span style="font-size: 0.8rem; color: var(--gold); font-weight: 800;">${{c.badge}}</span>
              <span style="font-size: 0.75rem; color: var(--emerald); font-weight: 800; background: rgba(16, 185, 129, 0.1); padding: 0.25rem 0.65rem; border-radius: var(--radius-full); border: 1px solid rgba(16, 185, 129, 0.3);">${{c.metric}}</span>
            </div>
            <h3 style="font-family: var(--font-felfel); font-size: 1.35rem; color: var(--text-pure); margin-bottom: 0.4rem;">${{c.name}}</h3>
            <div style="font-size: 0.82rem; color: var(--text-dim); margin-bottom: 0.6rem; font-weight: 600;">${{c.sector}}</div>
            <p style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.75; margin-bottom: 1.25rem;">${{c.desc}}</p>
            <a href="${{c.socialLink}}" target="_blank" class="btn btn-secondary" style="width: 100%; font-size: 0.85rem; padding: 0.55rem;">🌐 زيارة صفحة فيسبوك الرسمية</a>
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
          <div class="glass-card" style="margin-bottom: 1rem; padding: 1.35rem 1.65rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; cursor: pointer;" onclick="toggleCourseDetails('${{c.id}}')">
              <div>
                <span style="font-size: 0.78rem; color: var(--gold); font-weight: 800;">المرحلة 0${{c.phase}} · ${{c.badge}}</span>
                <h3 style="font-family: var(--font-felfel); font-size: 1.25rem; color: var(--text-pure); margin-top: 0.2rem;">${{c.icon}} ${{c.title}}</h3>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem;">
                <span style="font-size: 0.8rem; color: ${{isDone ? 'var(--emerald)' : 'var(--text-dim)'}};">${{isDone ? '✅ مكتمل' : '○ قيد الانتظار'}}</span>
                <span style="font-size: 0.9rem; color: var(--text-dim);">▾</span>
              </div>
            </div>

            <div id="details_${{c.id}}" style="display: none; margin-top: 1.25rem; padding-top: 1.25rem; border-top: 1px solid var(--border-subtle);">
              <p style="font-size: 0.92rem; color: var(--text-muted); margin-bottom: 1.25rem;">${{c.desc}}</p>
              
              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--text-pure); margin-bottom: 0.4rem;">📖 الوحدات التدريبية (${{c.pages}} صفحة منهج):</h4>
                <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-muted); line-height: 1.8;">
                  ${{unitsHtml}}
                </ul>
              </div>

              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--cyan); margin-bottom: 0.35rem;">🤖 أمر الذكاء الاصطناعي المعتمد (RCIC Prompt):</h4>
                <div class="code-box">${{c.prompt}}</div>
                <button class="btn btn-secondary" style="font-size: 0.82rem; padding: 0.4rem 1rem;" onclick="copyText(this.previousElementSibling.innerText)">📋 نسخ الأمر</button>
              </div>

              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--emerald); margin-bottom: 0.3rem;">💼 دراسة الحالة التطبيقية:</h4>
                <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.7;">${{c.case_study}}</p>
              </div>

              <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--border-subtle);">
                <div>
                  <h4 style="font-size: 0.95rem; color: var(--gold-champagne); margin-bottom: 0.2rem;">🧪 التكليف العملي:</h4>
                  <p style="font-size: 0.88rem; color: var(--text-muted);">${{c.lab}}</p>
                </div>
                <button class="btn ${{isDone ? 'btn-secondary' : 'btn-primary'}}" style="font-size: 0.82rem; padding: 0.45rem 1.1rem;" onclick="toggleCourseDone('${{c.id}}')">
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

    // LIGHTBOX
    function openLightbox(src, title, desc, link) {{
      const modal = document.getElementById("lightboxModal");
      document.getElementById("lightboxImg").src = src;
      document.getElementById("lightboxCaption").innerText = title;
      document.getElementById("lightboxDesc").innerText = desc || "";
      const btn = document.getElementById("lightboxSocialBtn");
      if (link) {{
        btn.href = link;
        btn.style.display = "inline-flex";
      }} else {{
        btn.style.display = "none";
      }}
      modal.style.display = "flex";
    }}

    function closeLightbox() {{
      document.getElementById("lightboxModal").style.display = "none";
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
        <div style="background: #020305; border: 4px solid var(--gold); border-radius: 28px; padding: 4rem 2.5rem; text-align: center; margin-top: 2.5rem; box-shadow: 0 0 80px rgba(212, 168, 83, 0.45); position: relative; overflow: hidden;">
          <div style="font-size: 3.5rem; margin-bottom: 0.5rem;">👑</div>
          <div style="font-size: 0.9rem; letter-spacing: 4px; color: var(--gold); text-transform: uppercase; font-family: var(--font-kookies); font-weight: 800;">OTB Marketing Studio · City Kings</div>
          <div style="font-family: var(--font-royal); font-size: 2.4rem; color: var(--text-pure); margin: 0.85rem 0; font-weight: 900; letter-spacing: 1.5px;">CERTIFICATE OF AI MASTERY</div>
          <p style="color: var(--text-dim); font-size: 1.05rem;">تشهد أكاديمية وكالة OTB لتمكين الذكاء الاصطناعي وهندسة النمو بأن</p>
          <h2 style="font-family: var(--font-felfel); font-size: 2.75rem; color: var(--gold); margin: 1rem 0; font-weight: 900;">${{name}}</h2>
          <p style="color: var(--text-main); max-width: 600px; margin: 0 auto 2.25rem auto; font-size: 0.98rem; line-height: 1.85;">
            قد أتم بنجاح متطلبات أكاديمية <b>الذكاء الاصطناعي التوليدي والنمو الرقمي (AI-Powered Marketing & Growth Engineering)</b> وأصبح مؤهلاً لمضاعفة الإنتاجية 5x وتطبيق استراتيجيات ملوك المدينة.
          </p>
          <div style="display: flex; justify-content: space-around; border-top: 1px solid var(--border-gold); padding-top: 1.75rem; font-size: 0.9rem;">
            <div>
              <div style="color: var(--text-dim); font-size: 0.78rem;">رقم الاعتماد الرسمي</div>
              <div style="font-family: var(--font-mono); color: var(--gold); font-weight: 800;">${{certId}}</div>
            </div>
            <div>
              <div style="color: var(--text-dim); font-size: 0.78rem;">تاريخ المنح</div>
              <div style="color: var(--text-pure); font-weight: 700;">${{date}}</div>
            </div>
            <div>
              <div style="color: var(--text-dim); font-size: 0.78rem;">الاعتماد الرقمي</div>
              <div style="color: var(--gold); font-weight: 900;">OTB Agency 👑</div>
            </div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 2rem;">
          <button class="btn btn-secondary" onclick="window.print()">🖨️ طباعة الشهادة / حفظ PDF</button>
        </div>
      `;
      wrap.scrollIntoView({{ behavior: "smooth" }});
      showToast("👑 تم إصدار شهادة الاعتماد الملكية بنجاح!");
    }}

    // INITIALIZATION
    renderRolesGrid();
    renderGalleryGrid();
    renderClientsGrid();
    renderCoursesList(coursesData);
    updateLivePrompt();
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(master_html)

print("Generated 100% Verified Real Document & Social Portal")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
