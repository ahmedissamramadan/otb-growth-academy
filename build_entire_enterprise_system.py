import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

# Load COURSES_DATA
from generate_master_academy import COURSES_DATA

def get_header(active_page):
    pages = [
        ("index.html", "🏠 الرئيسية"),
        ("mindmap.html", "🗺️ الخريطة الذهنية"),
        ("courses.html", "📚 المقررات الـ 19"),
        ("sprint.html", "⚡ المعسكر السريع"),
        ("masterclass.html", "🎓 الأكاديمية (4 أسابيع)"),
        ("prompts.html", "🤖 استوديو الأوامر"),
        ("case-studies.html", "💼 دراسات الحالة"),
        ("quiz.html", "📝 الاختبار والشهادة"),
        ("sops.html", "📋 الـ SOPs"),
        ("downloads.html", "📥 التحميلات")
    ]
    
    nav_links = ""
    for url, title in pages:
        active_cls = ' class="active"' if url == active_page else ""
        nav_links += f'<li class="nav-link-item"><a href="{url}"{active_cls}>{title}</a></li>\n'
        
    return f"""
  <header class="navbar">
    <a href="index.html" class="brand-wrapper">
      <span class="brand-crown">👑</span>
      <div class="brand-text">
        <h1>OTB GROWTH ACADEMY</h1>
        <p>THE CITY KINGS · FULL-SPECTRUM ENTERPRISE LMS 2026</p>
      </div>
    </a>
    <ul class="nav-menu">
      {nav_links}
    </ul>
    <a href="https://notebooklm.google.com/notebook/76ef5be2-d7d2-4a33-a88d-f88fc0fe1148" target="_blank" class="btn-notebook-badge">
      <span>✨ مشروع NotebookLM الرسمي</span>
    </a>
  </header>

  <div class="podcast-strip">
    <div class="podcast-info">
      <div class="live-badge">
        <div class="pulse-dot"></div>
        <span>استوديو التدريب الصوتي المعتمد</span>
      </div>
      <span style="color: var(--gold-200); font-size: 0.86rem; font-weight: 700;">🎙️ OTB Growth Engineering & AI Masterclass (Deep Dive Podcast)</span>
    </div>
    <div class="audio-controls-wrap">
      <audio controls>
        <source src="track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" type="audio/mp4">
        متصفحك لا يدعم مشغل الصوت المباشر.
      </audio>
    </div>
  </div>
"""

def get_footer():
    return """
  <footer class="footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <span style="font-size: 2.2rem;">👑</span>
        <div>
          <h3 style="color: var(--gold-100); font-size: 1.15rem; font-weight: 900;">OTB Agency — We Are The City Kings</h3>
          <p style="color: var(--text-muted); font-size: 0.85rem;">استراتيجيات جريئة.. نتائج حقيقية | Bold Strategies. Real Results</p>
        </div>
      </div>
      <div class="footer-contact">
        <div>📍 القاهرة، مصر</div>
        <div>📞 <a href="tel:+201008080295">+20 100 808 0295</a></div>
        <div>✉️ <a href="mailto:otbagency5@gmail.com">otbagency5@gmail.com</a></div>
      </div>
    </div>
    <div class="footer-bottom">
      © 2026 OTB Agency Growth Engineering Academy. All Rights Reserved. Engineered for Unmatched Market Dominance.
    </div>
  </footer>
  <script src="shared_ui.js"></script>
"""

# ==============================================================================
# 1. MINDMAP.HTML
# ==============================================================================
p_mindmap = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🗺️ الخريطة الذهنية الشاملة — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
    .mindmap-tree {{
      display: flex;
      flex-direction: column;
      gap: 2.5rem;
      position: relative;
    }}
    .phase-block {{
      background: var(--bg-card);
      border: 1px solid var(--gold-border);
      border-radius: var(--radius-md);
      padding: 2rem;
      box-shadow: var(--shadow-card);
      transition: var(--transition-smooth);
    }}
    .phase-block:hover {{
      border-color: var(--gold-500);
      box-shadow: var(--shadow-elevated), var(--gold-glow);
    }}
    .phase-header-title {{
      font-size: 1.4rem;
      font-weight: 900;
      color: var(--gold-100);
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
      padding-bottom: 0.85rem;
      border-bottom: 1px solid rgba(245, 158, 11, 0.2);
    }}
    .node-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
    }}
    .node-card {{
      background: var(--bg-sub);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-sm);
      padding: 1.25rem;
      border-right: 4px solid var(--gold-500);
      transition: var(--transition-fast);
    }}
    .node-card:hover {{
      border-color: var(--gold-500);
      background: var(--bg-surface);
      transform: translateY(-3px);
    }}
    .node-card h4 {{
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--gold-200);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .node-card ul {{
      padding-right: 1.25rem;
      font-size: 0.84rem;
      color: var(--text-muted);
      line-height: 1.7;
    }}
  </style>
</head>
<body>
  {get_header("mindmap.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>الخريطة الذهنية والتفكيك الهيكلي</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-pill">ARCHITECTURAL CURRICULUM BREAKDOWN</span>
      <h1 class="page-title">الخريطة الذهنية الشاملة: <span>تفكيك الـ 19 مساراً تدريبياً</span></h1>
      <p class="page-subtitle">خريطة مفاهيمية تفاعلية تفكك كامل محتوى الـ 2,400 صفحة في 4 مراحل نمو رئيسية و 80+ تخصصاً فرعياً مصممة خصيصاً لأدوار وكالة OTB الـ 16 دوراً.</p>
    </div>

    <div class="mindmap-tree">
      
      <!-- PHASE 1 -->
      <div class="phase-block">
        <div class="phase-header-title">
          <span class="page-pill" style="margin: 0; font-size: 0.8rem;">المرحلة 01</span>
          <span>👑 الأساسات، الاستراتيجية، وبناء الهوية الملكية (Foundations & Brand Architecture)</span>
        </div>
        <div class="node-grid">
          <div class="node-card" style="border-right-color: var(--gold-500);">
            <h4>💡 مبادئ وأسس التسويق الحديث</h4>
            <ul>
              <li>المزيج التسويقي الكلاسيكي (4Ps) إلى (4Cs)</li>
              <li>سيكولوجية اتخاذ القرار والقيمة المدركة</li>
              <li>رحلة العميل وبناء الـ Persona</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--gold-500);">
            <h4>🎯 الاستراتيجية والتخطيط SOSTAC</h4>
            <ul>
              <li>نموذج STP العملي (Segmentation, Targeting, Positioning)</li>
              <li>إطار SOSTAC للخطط السنوية و 90 يوماً</li>
              <li>تحديد مؤشرات الأداء والأهداف الذكية (SMART KPIs)</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--gold-500);">
            <h4>👑 بناء الهوية والعلامة التجارية</h4>
            <ul>
              <li>النمط النفسي The Ruler & The Creator لـ OTB</li>
              <li>صياغة كراسة الهوية ونبرة الصوت (Tone of Voice)</li>
              <li>تموضع السعر والهيبة وحماية السمعة</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--gold-500);">
            <h4>🛡️ الانضباط التشغيلي CoreLink CRM</h4>
            <ul>
              <li>نماذج البريف الإلزامي ومنع التعليمات الشفهية</li>
              <li>قفل التبعيات التسلسلي (Sequential Locking)</li>
              <li>اتفاقيات مستوى الخدمة (SLA 24h Review)</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- PHASE 2 -->
      <div class="phase-block">
        <div class="phase-header-title">
          <span class="page-pill" style="margin: 0; font-size: 0.8rem; color: var(--cyan); border-color: var(--cyan);">المرحلة 02</span>
          <span>✍️ محرك الكرييتف، المحتوى الفيرال، وسيو محركات البحث (Viral Creative & Organic Engine)</span>
        </div>
        <div class="node-grid">
          <div class="node-card" style="border-right-color: var(--cyan);">
            <h4>✍️ تسويق المحتوى والكوبي رايتنج</h4>
            <ul>
              <li>قاعدة الـ 3 ثوانٍ الأولى وهندسة الهوك (Hook Rate > 35%)</li>
              <li>أطر الكتابة التحويلية: PAS, AIDA, BAB</li>
              <li>الركائز الإعلانية وجدول النشر التحريري</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--cyan);">
            <h4>📸 احتراف إنستغرام والريلز</h4>
            <ul>
              <li>خوارزمية الـ Reels وهندسة معدل الإكمال</li>
              <li>تسلسل الستوري اليومي لتحقيق مبيعات مباشرة</li>
              <li>أتمتة الرسائل الخاصة (IG DM Automation)</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--cyan);">
            <h4>🔍 سيو محركات البحث (SEO 3-Day)</h4>
            <ul>
              <li>البحث عن الكلمات المفتاحية التنافسية وتجميعها</li>
              <li>السيو الداخلي والتقني (Core Web Vitals & Schema)</li>
              <li>بناء الروابط الخلفية وسيو نتائج الذكاء الاصطناعي (SGE)</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--cyan);">
            <h4>🎥 يوتيوب وسيو الفيديو الطويل</h4>
            <ul>
              <li>سيكولوجية الصورة المصغرة (CTR > 10%)</li>
              <li>هندسة الحفاظ على المشاهدين (Audience Retention)</li>
              <li>استراتيجية Shorts وتحويل المشاهدين لعملاء</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- PHASE 3 -->
      <div class="phase-block">
        <div class="phase-header-title">
          <span class="page-pill" style="margin: 0; font-size: 0.8rem; color: var(--emerald); border-color: var(--emerald);">المرحلة 03</span>
          <span>📊 ميديا بايينج الأداء والسيطرة الإعلانية المدفوعة (Paid Media Dominance & ROAS)</span>
        </div>
        <div class="node-grid">
          <div class="node-card" style="border-right-color: var(--emerald);">
            <h4>📊 إعلانات فيسبوك وميتا للأداء</h4>
            <ul>
              <li>هيكل TOFU / MOFU / BOFU وحملات Advantage+</li>
              <li>تتبع السيرفر CAPI وتجاوز قيود iOS 14.5+</li>
              <li>قواعد السكيلينج الرأسي (+20% / 48h) والأفقي</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--emerald);">
            <h4>🎵 إعلانات ونمو تيك توك</h4>
            <ul>
              <li>صفحة FYP وسيكولوجية محتوى الـ UGC</li>
              <li>إعلانات Spark Ads واستغلال الفيديوهات الرابحة</li>
              <li>سيو تيك توك وتتبع مبيعات المتاجر الإلكترونية</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--emerald);">
            <h4>👻 إعلانات سناب شات والخليج</h4>
            <ul>
              <li>طبيعة المستهلك الخليجي في السعودية والإمارات</li>
              <li>تصميم عدسات الواقع المعزز (AR Lenses)</li>
              <li>إعلانات المجموعات (Collection Ads) للمتاجر</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--emerald);">
            <h4>💼 لينكد إن واكتساب عملاء B2B</h4>
            <ul>
              <li>استقطاب كبار صناع القرار عبر Sales Navigator</li>
              <li>بناء المحتوى القيادي (Thought Leadership)</li>
              <li>إعلانات Lead Gen Forms لصفقات الشركات</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--emerald);">
            <h4>🐦 منصة إكس والتموضع المؤسسي</h4>
            <ul>
              <li>كتابة الثريدات التحليلية الفيرال وركوب الترندات</li>
              <li>إدارة الأزمات والرد السريع على الجمهور</li>
              <li>بناء الحضور الرسمي الموثق لكبار التنفيذيين</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- PHASE 4 -->
      <div class="phase-block">
        <div class="phase-header-title">
          <span class="page-pill" style="margin: 0; font-size: 0.8rem; color: var(--purple); border-color: var(--purple);">المرحلة 04</span>
          <span>🤖 أتمتة الذكاء الاصطناعي، الجروث هاكينج، وعقود الريتينر (AI, Growth Hacking & Retainers)</span>
        </div>
        <div class="node-grid">
          <div class="node-card" style="border-right-color: var(--purple);">
            <h4>🤖 الذكاء الاصطناعي وهندسة الأوامر</h4>
            <ul>
              <li>إطار RCIC المتقدم لصناعة الإعلانات والاسكريبتات</li>
              <li>التصوير التجاري وتوليد أصول 3D عبر Midjourney</li>
              <li>أتمتة خدمة العملاء عبر WhatsApp Business API</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--purple);">
            <h4>📧 الإيميل ماركتنج وتدفقات الأتمتة</h4>
            <ul>
              <li>تدفقات استعادة السلات المتروكة (Abandoned Cart)</li>
              <li>سلاسل الترحيب ورفع القيمة العمرية للعميل (LTV)</li>
              <li>تقسيم القوائم البريدية وضمان تسليم الوارد</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--purple);">
            <h4>🚀 الجروث هاكينج وقمع AARRR</h4>
            <ul>
              <li>هندسة حلقات الانتشار الفيرال وبرامج الإحالة</li>
              <li>مصفوفة تقييم التجارب السريعة (ICE Framework)</li>
              <li>تحسين معدلات التحويل (CRO & UX Optimization)</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--purple);">
            <h4>🤝 التسويق بالعمولة والشراكات</h4>
            <ul>
              <li>بناء وإدارة شبكات المسوقين بالعمولة لبراندك</li>
              <li>تصميم هياكل العمولات دون الإضرار بهامش الربح</li>
              <li>استقطاب المؤثرين وحماية البرنامج من الاحتيال</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--purple);">
            <h4>💼 عقود الريتينر الشهرية ($2,500/mo)</h4>
            <ul>
              <li>الانتقال للتسعير القائم على القيمة والعائد (Value-Based)</li>
              <li>صياغة عروض الأسعار التي لا تقاوم (Grand Slam Offer)</li>
              <li>إدارة اجتماعات الإغلاق والحفاظ على العملاء</li>
            </ul>
          </div>
          <div class="node-card" style="border-right-color: var(--purple);">
            <h4>🎯 التميز المهني والمقابلات STAR</h4>
            <ul>
              <li>السيرة الذاتية المبنية على الأرقام والإنجازات</li>
              <li>استخدام نموذج STAR للإجابة على الأسئلة الصعبة</li>
              <li>التفاوض على الراتب والحوافز والترقي المستمر</li>
            </ul>
          </div>
        </div>
      </div>

    </div>

  </main>
  {get_footer()}
</body>
</html>
"""

# ==============================================================================
# 2. COURSES.HTML (19-COURSE ENCYCLOPEDIA & READER)
# ==============================================================================
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

p_courses = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📚 موسوعة المقررات الـ 19 — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
    .courses-filter {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-bottom: 2rem;
    }}
    .course-card-link {{
      text-decoration: none;
      color: inherit;
      display: block;
      cursor: pointer;
    }}
    .reader-modal {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(4, 6, 10, 0.92);
      backdrop-filter: var(--blur-glass);
      z-index: 99999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }}
    .reader-modal.open {{
      display: flex;
    }}
    .reader-content {{
      background: var(--bg-main);
      border: 2px solid var(--gold-500);
      border-radius: var(--radius-md);
      width: 100%;
      max-width: 960px;
      max-height: 90vh;
      overflow-y: auto;
      padding: 2.5rem;
      position: relative;
      box-shadow: 0 0 60px rgba(0,0,0,0.9), var(--gold-glow);
    }}
    .close-modal-btn {{
      position: absolute;
      top: 1.25rem;
      left: 1.25rem;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #FFF;
      font-size: 1.2rem;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition-fast);
    }}
    .close-modal-btn:hover {{
      background: var(--crimson);
      border-color: var(--crimson);
    }}
  </style>
</head>
<body>
  {get_header("courses.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>موسوعة المقررات الـ 19 الشاملة</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-pill">THE FULL 19-COURSE ENCYCLOPEDIA</span>
      <h1 class="page-title">موسوعة المقررات الـ 19: <span>المنهج الأكاديمي الشامل لـ OTB</span></h1>
      <p class="page-subtitle">استكشف المقررات الـ 19 المفصلة المستخلصة من 2,400+ صفحة علمية مع أوامر الذكاء الاصطناعي ودراسات الحالة والتكليفات العملية لكل تخصص.</p>
    </div>

    <!-- SEARCH & FILTER -->
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 2rem;">
      <div class="courses-filter" style="margin: 0;">
        <button class="pill-btn active" onclick="filterCourses('all', this)">الكل (19 مقرر)</button>
        <button class="pill-btn" onclick="filterCourses('strategy', this)">🎯 الاستراتيجية والهوية (4)</button>
        <button class="pill-btn" onclick="filterCourses('creative', this)">✍️ الكرييتف والمحتوى والسيو (4)</button>
        <button class="pill-btn" onclick="filterCourses('media', this)">📊 الميديا بايينج والإعلانات (5)</button>
        <button class="pill-btn" onclick="filterCourses('ai', this)">🤖 الـ AI والجروث والأتمتة (4)</button>
        <button class="pill-btn" onclick="filterCourses('career', this)">💼 عقود الريتينر والمسار المهني (2)</button>
      </div>

      <input type="text" id="courseSearch" class="btn-secondary" placeholder="🔍 بحث في المقررات..." style="padding: 0.6rem 1.25rem; border-radius: var(--radius-full); text-align: right; width: 260px;" oninput="searchCourses()">
    </div>

    <!-- COURSES GRID -->
    <div class="grid-3" id="coursesGrid"></div>

    <!-- READER MODAL -->
    <div id="readerModal" class="reader-modal">
      <div class="reader-content">
        <button class="close-modal-btn" onclick="closeReader()">✕</button>
        <div id="readerBody"></div>
      </div>
    </div>

  </main>
  {get_footer()}

  <script>
    const coursesData = {courses_json};

    function renderCourses(list) {{
      const grid = document.getElementById("coursesGrid");
      let html = "";
      list.forEach(c => {{
        const isDone = localStorage.getItem("otb_course_" + c.id) === "true";
        html += `
          <div class="card course-card-link" onclick="openReader('${{c.id}}')">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
              <span class="item-badge">${{c.badge}}</span>
              <span style="font-size: 0.76rem; color: var(--gold-400); font-weight: 700;">📄 ${{c.pages}} صفحة منهج</span>
            </div>
            <h3 class="card-title">
              <span>${{c.icon}}</span>
              <span>${{c.title}}</span>
            </h3>
            <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.7; margin-bottom: 1.25rem;">
              ${{c.desc}}
            </p>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 0.85rem; margin-top: 0.85rem;">
              <span style="color: var(--gold-400); font-weight: 800; font-size: 0.85rem;">فتح المنهج والتطبيق ←</span>
              <span style="font-size: 0.8rem; color: ${{isDone ? 'var(--emerald)' : 'var(--text-dim)'}};">${{isDone ? '✅ تم دراسته' : '○ قيد الانتظار'}}</span>
            </div>
          </div>
        `;
      }});
      grid.innerHTML = html;
    }}

    function openReader(courseId) {{
      const c = coursesData.find(item => item.id === courseId);
      if (!c) return;

      const isDone = localStorage.getItem("otb_course_" + c.id) === "true";
      const body = document.getElementById("readerBody");

      let unitsHtml = "";
      c.units.forEach((u, i) => {{
        unitsHtml += `<li><b>الوحدة ${{i + 1}}:</b> ${{u}}</li>`;
      }});

      body.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem; border-bottom: 1px solid var(--gold-border); padding-bottom: 1.5rem; margin-bottom: 1.5rem;">
          <div>
            <span class="page-pill">المرحلة 0${{c.phase}} · ${{c.badge}} · ${{c.pages}} صفحة</span>
            <h2 style="font-size: 1.85rem; color: var(--gold-100); margin: 0.5rem 0;">${{c.icon}} ${{c.title}}</h2>
            <p style="color: var(--text-muted); font-size: 0.95rem;">${{c.desc}}</p>
          </div>
          <button class="${{isDone ? 'btn-secondary' : 'btn-primary'}}" onclick="toggleCourseDone('${{c.id}}')">
            ${{isDone ? '✅ تم إكمال هذا المقرر' : '🎯 تحديد كـ مكتمل'}}
          </button>
        </div>

        <div class="lesson-box">
          <h3>📖 الوحدات التفصيلية للمنهج الأكاديمي (Deep-Dive Units)</h3>
          <ul style="padding-right: 1.5rem; font-size: 0.95rem; line-height: 2;">
            ${{unitsHtml}}
          </ul>
        </div>

        <div class="lesson-box" style="border-right-color: var(--cyan);">
          <h3>🤖 أمر الذكاء الاصطناعي المعتمد (RCIC Prompt)</h3>
          <div class="prompt-box">${{c.prompt}}</div>
          <button class="btn-secondary" style="width: 100%; margin-top: 0.5rem;" onclick="copyText(this.previousElementSibling.innerText)">📋 نسخ الأمر المعتمد</button>
        </div>

        <div class="lesson-box" style="border-right-color: var(--emerald);">
          <h3>💼 دراسة الحالة التطبيقية لعملاء OTB</h3>
          <p style="font-size: 0.95rem; line-height: 1.8;">${{c.case_study}}</p>
        </div>

        <div class="lesson-box" style="border-right-color: var(--purple);">
          <h3>🧪 التكليف العملي الإلزامي للقسم</h3>
          <p style="font-size: 0.95rem; line-height: 1.8;"><b>المطلوب تسليمه:</b> ${{c.lab}}</p>
        </div>
      `;

      document.getElementById("readerModal").classList.add("open");
    }}

    function closeReader() {{
      document.getElementById("readerModal").classList.remove("open");
      renderCourses(coursesData);
    }}

    function toggleCourseDone(courseId) {{
      const key = "otb_course_" + courseId;
      const cur = localStorage.getItem(key) === "true";
      localStorage.setItem(key, !cur);
      showToast(!cur ? "👑 تم تسجيل إكمال المقرر بنجاح!" : "تم إلغاء التحديد");
      openReader(courseId);
    }}

    function filterCourses(cat, btn) {{
      document.querySelectorAll(".pill-btn").forEach(p => p.classList.remove("active"));
      btn.classList.add("active");

      if (cat === "all") {{
        renderCourses(coursesData);
      }} else {{
        const filtered = coursesData.filter(c => c.cat === cat);
        renderCourses(filtered);
      }}
    }}

    function searchCourses() {{
      const q = document.getElementById("courseSearch").value.toLowerCase();
      const filtered = coursesData.filter(c => 
        c.title.toLowerCase().includes(q) || 
        c.desc.toLowerCase().includes(q) ||
        c.badge.toLowerCase().includes(q)
      );
      renderCourses(filtered);
    }}

    renderCourses(coursesData);
  </script>
</body>
</html>
"""

# WRITE FILES
with open(os.path.join(BASE_DIR, "mindmap.html"), "w", encoding="utf-8") as f:
    f.write(p_mindmap)
print("Generated mindmap.html")

with open(os.path.join(BASE_DIR, "courses.html"), "w", encoding="utf-8") as f:
    f.write(p_courses)
print("Generated courses.html")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized all files to Downloads!")
