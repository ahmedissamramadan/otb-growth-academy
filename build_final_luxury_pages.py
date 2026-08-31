import os
import shutil

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

def get_header(active_page):
    pages = [
        ("index.html", "🏠 الرئيسية"),
        ("sprint.html", "⚡ معسكر الـ 5 أيام"),
        ("masterclass.html", "📚 الأكاديمية (4 أسابيع)"),
        ("prompts.html", "🤖 استوديو الأوامر"),
        ("case-studies.html", "💼 دراسات الحالة"),
        ("quiz.html", "📝 الاختبار والشهادة"),
        ("sops.html", "📋 الـ SOPs والبريفات"),
        ("downloads.html", "📥 الموارد والتحميلات")
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
        <p>THE CITY KINGS · INTERNAL MASTERY PORTAL 2026</p>
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
# CASE-STUDIES.HTML
# ==============================================================================
p_case = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>💼 دراسات الحالة وقاعدة المعرفة — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_header("case-studies.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>دراسات الحالة وقاعدة المعرفة</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-pill">DOCUMENTED EVIDENCE & ROI CASE STUDIES</span>
      <h1 class="page-title">دراسات حالة عملاء OTB: <span>أرقام حقيقية ونتائج موثقة</span></h1>
      <p class="page-subtitle">تحليل استراتيجي معمق لكيفية تحويل التحديات التسويقية المعقدة إلى عوائد مالية قياسية (ROAS) وأرباح مستدامة لعملاء الوكالة.</p>
    </div>

    <!-- CLIENT CASE STUDIES GRID -->
    <div class="grid-3" style="margin-bottom: 3.5rem;">
      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge" style="background: var(--gold-500);">Specialty Coffee</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0; color: var(--emerald); border-color: var(--emerald);">تفاعل +180%</span>
        </div>
        <h3 class="card-title">☕ MIX Coffee</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          <b>التحدي السابق:</b> منافسة شرسة في سوق القهوة المختصة وتراجع مبيعات الفروع.<br>
          <b>استراتيجية OTB:</b> إعادة التموضع كوجهة أولى لرواد الأعمال، هوية داكنة راقية، وفيديوهات ASMR لصنع القهوة.<br>
          <b>النتيجة المحققة:</b> مضاعفة مبيعات الفروع اليومية ونمو التفاعل بنسبة 180%.
        </p>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge" style="background: var(--crimson);">Gourmet Burgers</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0; color: var(--emerald); border-color: var(--emerald);">Retention 36.8%</span>
        </div>
        <h3 class="card-title">🍔 Rancho's EG</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          <b>التحدي السابق:</b> حرق الأسعار وتآكل هوامش الربح بسبب الخصومات المستمرة.<br>
          <b>استراتيجية OTB:</b> تموضع البرجر الملحمي الفاخر مع حملات Click-to-WhatsApp عالية الدقة.<br>
          <b>النتيجة المحققة:</b> رفع معدل إعادة الشراء إلى 36.8% وزيادة متوسط الفاتورة بنسبة 45%.
        </p>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge" style="background: var(--cyan);">Luxury Jewelry</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0; color: var(--emerald); border-color: var(--emerald);">ROAS 7.5x+</span>
        </div>
        <h3 class="card-title">💍 Dr. Zaghloul Jewelry</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          <b>التحدي السابق:</b> ضعف ثقة العملاء في طلب قطع الذهب والمجوهرات عبر السوشيال ميديا.<br>
          <b>استراتيجية OTB:</b> التركيز على الأمان والاستثمار وسرد قصص التصاميم الحصرية بجودة سينمائية.<br>
          <b>النتيجة المحققة:</b> تحقيق مبيعات مباشرة وعائد إعلاني ROAS تجاوز 7.5x.
        </p>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge" style="background: var(--purple);">Pastry & Sweets</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0; color: var(--emerald); border-color: var(--emerald);">100% Sold Out</span>
        </div>
        <h3 class="card-title">🍰 Rice Patisserie</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          <b>التحدي السابق:</b> تذبذب الطلب الموسمي ومنافسة محلات الحلويات الكبرى.<br>
          <b>استراتيجية OTB:</b> حملات حجز مسبق قبل المناسبات مع أتمتة رسائل العروض الحصرية.<br>
          <b>النتيجة المحققة:</b> نفاد كامل الكميات المحجوزة قبل 48 ساعة من كل موسم.
        </p>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge" style="background: var(--emerald);">E-Commerce & Retail</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0; color: var(--emerald); border-color: var(--emerald);">CPA -32%</span>
        </div>
        <h3 class="card-title">📦 Sakr Store</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          <b>التحدي السابق:</b> ارتفاع تكلفة الاستحواذ (CAC) وضعف استقرار الحملات.<br>
          <b>استراتيجية OTB:</b> إعادة هيكلة إعلانات Advantage+ وتتبع CAPI مع عروض الباقات المجمعة.<br>
          <b>النتيجة المحققة:</b> خفض تكلفة الشراء بنسبة 32% ورفع متوسط السلة بنسبة 50%.
        </p>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge" style="background: var(--cyan);">Medical & Clinics</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0; color: var(--emerald); border-color: var(--emerald);">800+ Leads / mo</span>
        </div>
        <h3 class="card-title">🧪 Elag Labs</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.7; margin-bottom: 1.25rem;">
          <b>التحدي السابق:</b> صعوبة جذب حجوزات التحاليل والزيارات المنزلية الطبية.<br>
          <b>استراتيجية OTB:</b> إعلانات سريعة ومقنعة تركز على دقة النتائج وسرعة الزيارة المنزلية.<br>
          <b>النتيجة المحققة:</b> استقبال وتأهيل أكثر من 800 حجز شهرياً عبر الواتساب.
        </p>
      </div>
    </div>

    <!-- FRAMEWORKS SECTION -->
    <h2 style="font-size: 1.5rem; font-weight: 900; color: var(--gold-100); margin-bottom: 1.75rem; border-right: 4px solid var(--gold-500); padding-right: 0.85rem;">
      📐 الأطر والنماذج التسويقية المعتمدة في OTB
    </h2>

    <div class="grid-2">
      <div class="lesson-box">
        <h3>1. نموذج التموضع (STP Framework)</h3>
        <p>• <b>Segmentation:</b> تقسيم الجمهور جغرافياً وسلوكياً ونفسياً.<br>• <b>Targeting:</b> اختيار الشريحة الأعلى ربحية والأكثر ولاءً.<br>• <b>Positioning:</b> حفر مكانة مميزة في ذهن العميل تجعل المنافسين غير ذي صلة.</p>
      </div>

      <div class="lesson-box">
        <h3>2. معادلة العائد على الإنفاق الإعلاني (ROAS Math)</h3>
        <p>• <b>ROAS = إجمالي الإيرادات / إجمالي الإنفاق الإعلاني</b><br>• <b>Break-Even ROAS = 1 / هامش الربح %</b><br>• <b>CAC = إجمالي تكاليف التسويق / عدد العملاء الجدد</b></p>
      </div>

      <div class="lesson-box">
        <h3>3. مصفوفة أولويات التجارب (ICE Framework)</h3>
        <p>تقييم أي فكرة إعلانية أو حملة نمو من 1 إلى 10 في:<br>• <b>Impact (التأثير المالي المتوقع)</b><br>• <b>Confidence (الثقة في نجاح التجربة)</b><br>• <b>Ease (سهولة وسرعة التنفيذ)</b></p>
      </div>

      <div class="lesson-box">
        <h3>4. إطار هندسة الأوامر الذكية (RCIC Architecture)</h3>
        <p>• <b>Role:</b> تحديد خبرة وهامش تفكير الذكاء الاصطناعي.<br>• <b>Context:</b> تفاصيل البيزنس والجمهور المستهدف.<br>• <b>Instruction:</b> المهمة الواضحة المطلوب إنجازها.<br>• <b>Constraints:</b> القيود والشروط والممنوعات ونبرة الصوت.</p>
      </div>
    </div>

  </main>
  {get_footer()}
</body>
</html>
"""

# ==============================================================================
# SOPS.HTML
# ==============================================================================
p_sops = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📋 الـ SOPs ومولد البريفات — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_header("sops.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>إجراءات التشغيل القياسية والبريفات</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-pill">OPERATIONAL DISCIPLINE & CRM</span>
      <h1 class="page-title">الانضباط التشغيلي: <span>مولد البريفات القياسية وإجراءات CoreLink</span></h1>
      <p class="page-subtitle">القضاء على متلازمة التوجيه الفارغ (Empty Brief)، توحيد نماذج الإسناد للأقسام، وضمان التزام الفرق باتفاقيات مستوى الخدمة (SLA).</p>
    </div>

    <!-- INTERACTIVE BRIEF BUILDER WIZARD -->
    <div class="grid-2" style="margin-bottom: 3.5rem;">
      <div class="card" style="border: 2px solid var(--gold-500);">
        <h3 style="color: var(--gold-100); font-size: 1.3rem; font-weight: 800; margin-bottom: 1.25rem;">⚙️ مولد البريف الإلزامي للقسم</h3>
        
        <div class="form-group">
          <label style="display: block; font-size: 0.88rem; font-weight: 700; color: var(--gold-200); margin-bottom: 0.4rem;">اسم العميل / البراند:</label>
          <input type="text" id="sopClient" class="btn-secondary" style="width: 100%; padding: 0.75rem 1rem; border-radius: var(--radius-sm); color: #FFF; background: var(--bg-surface); text-align: right;" value="Rancho's EG" oninput="buildBrief()">
        </div>

        <div class="form-group">
          <label style="display: block; font-size: 0.88rem; font-weight: 700; color: var(--gold-200); margin-bottom: 0.4rem;">القسم والتكليف:</label>
          <select id="sopType" class="btn-secondary" style="width: 100%; padding: 0.75rem 1rem; border-radius: var(--radius-sm); color: #FFF; background: var(--bg-surface); text-align: right;" onchange="buildBrief()">
            <option>كتابة محتوى وكوبي رايتنج إعلاني (Copywriting)</option>
            <option>تصميم سوشيال ميديا وموشن جرافيك (Design/Video)</option>
            <option>إطلاق وإدارة حملات ميديا بايينج ممولة (Media Buying)</option>
            <option>أتمتة رسائل واتساب وخدمة عملاء (WhatsApp CRM)</option>
          </select>
        </div>

        <div class="form-group">
          <label style="display: block; font-size: 0.88rem; font-weight: 700; color: var(--gold-200); margin-bottom: 0.4rem;">الهدف التسويقي الأساسي:</label>
          <input type="text" id="sopGoal" class="btn-secondary" style="width: 100%; padding: 0.75rem 1rem; border-radius: var(--radius-sm); color: #FFF; background: var(--bg-surface); text-align: right;" value="مضاعفة مبيعات فرع التجمع ورفع متوسط الفاتورة" oninput="buildBrief()">
        </div>

        <div class="form-group">
          <label style="display: block; font-size: 0.88rem; font-weight: 700; color: var(--gold-200); margin-bottom: 0.4rem;">الزاوية الإعلانية (Angle):</label>
          <input type="text" id="sopAngle" class="btn-secondary" style="width: 100%; padding: 0.75rem 1rem; border-radius: var(--radius-sm); color: #FFF; background: var(--bg-surface); text-align: right;" value="زاوية الطعم الملحمي الحصري للـ Smoked Brisket" oninput="buildBrief()">
        </div>

        <div class="form-group">
          <label style="display: block; font-size: 0.88rem; font-weight: 700; color: var(--gold-200); margin-bottom: 0.4rem;">المحددات ونبرة الصوت والممنوعات:</label>
          <textarea id="sopNotes" class="btn-secondary" style="width: 100%; height: 90px; padding: 0.75rem 1rem; border-radius: var(--radius-sm); color: #FFF; background: var(--bg-surface); text-align: right; resize: vertical;" oninput="buildBrief()">النبرة ملكية وواثقة بالعامية المصرية الراقية. ممنوع العبارات المبتذلة. الـ CTA يوجه لطلب القائمة عبر واتساب.</textarea>
        </div>
      </div>

      <div class="card">
        <h3 style="color: var(--gold-100); font-size: 1.3rem; font-weight: 800; margin-bottom: 1.25rem;">📋 النص الجاهز للإسناد في CoreLink CRM</h3>
        <textarea id="sopResult" class="prompt-box" style="height: 380px; width: 100%; max-height: none;" readonly></textarea>
        <button class="btn-primary" style="width: 100%; margin-top: 1rem;" onclick="copyBriefText()">📋 نسخ البريف للإسناد الفوري في CoreLink</button>
      </div>
    </div>

    <!-- SOPS RULES -->
    <h2 style="font-size: 1.5rem; font-weight: 900; color: var(--gold-100); margin-bottom: 1.75rem; border-right: 4px solid var(--gold-500); padding-right: 0.85rem;">
      🛡️ القواعد الأربع لمنع الهدر التشغيلي في OTB
    </h2>

    <div class="grid-2">
      <div class="lesson-box">
        <h3>1. لا مهمة بدون بريف إلزامي كامل</h3>
        <p>يُحظر بدء أي تصميم أو تصوير أو ميديا بايينج بناءً على رسائل شفهية أو محادثات واتساب مبعثرة. كل مهمة يجب أن تحتوي على زاوية إعلانية، نص معتمد، وهدف رقمي واضح.</p>
      </div>

      <div class="lesson-box">
        <h3>2. قفل التبعيات التسلسلي (Sequential Locking)</h3>
        <p>مرحلة التصميم الجرافيكي والمونتاج لا تفتح للمصمم إلا بعد اعتماد مدير المحتوى لكامل النصوص بنسبة 100%، مما يقضي تماماً على تضارب النصوص بعد انتهاء التصميم.</p>
      </div>

      <div class="lesson-box">
        <h3>3. قاعدة الـ 24 ساعة للمراجعات (SLA Rule)</h3>
        <p>كل تسليم يتم رفعه عبر Cloudflare R2 داخل النظام يجب مراجعته واعتماده أو إرجاعه بملاحظات معيارية خلال 24 ساعة. إذا تجاوزت المهمة 48 ساعة يتم تصعيدها فوراً للإدارة العليا.</p>
      </div>

      <div class="lesson-box">
        <h3>4. الشفافية التامة في تتبع الساعات (True Cost Tracking)</h3>
        <p>استخدام المؤقت الفعلي للعمل مع الإيقاف التلقائي عند الخمول لكشف التكلفة الحقيقية لكل عميل وحساب ربحية عقود الريتينر بدقة متناهية.</p>
      </div>
    </div>

  </main>
  {get_footer()}

  <script>
    function buildBrief() {{
      const client = document.getElementById("sopClient").value || "العميل";
      const type = document.getElementById("sopType").value;
      const goal = document.getElementById("sopGoal").value || "تحقيق مبيعات";
      const angle = document.getElementById("sopAngle").value || "الجودة العالية";
      const notes = document.getElementById("sopNotes").value || "الالتزام بالهوية.";
      const date = new Date().toLocaleDateString('ar-EG');

      const brief = "### 👑 OTB OFFICIAL TASK BRIEF\\n" +
        "==================================================\\n" +
        "* العميل / المشروع: " + client + "\\n" +
        "* القسم والتكليف: " + type + "\\n" +
        "* تاريخ الإسناد: " + date + "\\n" +
        "* نظام التتبع: CoreLink CRM (Live System)\\n" +
        "==================================================\\n" +
        "🎯 الهدف التسويقي (Marketing Objective):\\n" +
        goal + "\\n\\n" +
        "💡 الزاوية الإعلانية (Angle & Positioning):\\n" +
        angle + "\\n\\n" +
        "⚠️ المحددات ونبرة الصوت والممنوعات (Constraints & Tone):\\n" +
        notes + "\\n\\n" +
        "📦 التسليم والمراجعة (Delivery & SLA):\\n" +
        "- مكان التسليم: Cloudflare R2 Storage inside CoreLink CRM\\n" +
        "- مهلة المراجعة القصوى: 24 ساعة من تاريخ الرفع.\\n" +
        "==================================================\\n" +
        "👑 OTB Agency — We Are The City Kings";

      document.getElementById("sopResult").value = brief;
    }}

    function copyBriefText() {{
      const txt = document.getElementById("sopResult").value;
      copyText(txt, "👑 تم نسخ البريف بنجاح! جاهز للإسناد في CoreLink CRM.");
    }}

    buildBrief();
  </script>
</body>
</html>
"""

# ==============================================================================
# DOWNLOADS.HTML
# ==============================================================================
p_downloads = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📥 الموارد والتحميلات — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_header("downloads.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>مركز الموارد والتحميلات</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-pill">STUDIO ASSETS & RESOURCE HUB</span>
      <h1 class="page-title">مركز الموارد والتحميلات: <span>أصول الوكالة وملفات التدريب</span></h1>
      <p class="page-subtitle">جميع الأدلة التكتيكية، ملفات المنهج الأكاديمي، مخرجات Gemini Studio، والبودكاست الصوتي المعتمد متاحة للتحميل المباشر.</p>
    </div>

    <div class="grid-3">
      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge">Podcast & Audio</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0;">34 MB MP4</span>
        </div>
        <h3 class="card-title">🎙️ البودكاست الاستراتيجي المعتمد</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.7; margin-bottom: 1.5rem;">
          حلقة صوتية معمقة تم توليدها عبر Gemini Studio تناقش هندسة النمو ومحرك الذكاء الاصطناعي لوكالة OTB.
        </p>
        <a href="track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" download class="btn-primary" style="width: 100%;">📥 تحميل ملف الصوت المعتمد</a>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge">Briefing Doc</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0;">Markdown</span>
        </div>
        <h3 class="card-title">📑 التقرير الاستراتيجي الشامل</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.7; margin-bottom: 1.5rem;">
          وثيقة التوجيه الاستراتيجي الصادرة من الاستوديو تلخص الهيكل التنظيمي ومؤشرات الأداء لوكالة OTB.
        </p>
        <a href="track_b_4week_masterclass/studio_artifacts/OTB_Executive_Strategic_Briefing.md" download class="btn-secondary" style="width: 100%;">📥 تحميل المستند التنفيذي</a>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge">AI Bible</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0;">50+ Prompts</span>
        </div>
        <h3 class="card-title">📖 موسوعة الأوامر التكتيكية (Bible)</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.7; margin-bottom: 1.5rem;">
          أكثر من 50 برومبت معتمد ومفصل لجميع أقسام الوكالة الـ 16 دوراً وظيفياً بصيغة Markdown.
        </p>
        <a href="track_a_fast_track_sprint/cheatsheets/OTB_Prompt_Engineering_Bible.md" download class="btn-secondary" style="width: 100%;">📥 تحميل موسوعة الأوامر</a>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge">Media Buying</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0;">Checklist</span>
        </div>
        <h3 class="card-title">✈️ دليل تدقيق الإعلانات الممولة</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.7; margin-bottom: 1.5rem;">
          قائمة الفحص الفني قبل إطلاق الحملات (Pre-Flight Checklist) وقواعد السكيلينج الرأسي والأفقي.
        </p>
        <a href="track_a_fast_track_sprint/cheatsheets/OTB_Media_Buying_Checklist.md" download class="btn-secondary" style="width: 100%;">📥 تحميل قائمة الفحص</a>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge">CRM SOPs</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0;">Templates</span>
        </div>
        <h3 class="card-title">📋 نماذج البريفات وإجراءات العمل</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.7; margin-bottom: 1.5rem;">
          نماذج التوجيه الإلزامي للأقسام وقواعد الـ SLA المعتمدة داخل CoreLink CRM.
        </p>
        <a href="track_a_fast_track_sprint/cheatsheets/OTB_SOP_Briefing_Templates.md" download class="btn-secondary" style="width: 100%;">📥 تحميل نماذج الـ SOPs</a>
      </div>

      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
          <span class="item-badge">Capstone Brief</span>
          <span class="page-pill" style="font-size: 0.72rem; margin: 0;">Evaluation</span>
        </div>
        <h3 class="card-title">🎓 دليل مشروع التخرج الشامل 360°</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.7; margin-bottom: 1.5rem;">
          المواصفات والمعايير التفصيلية لتسليم مشروع تخرج الأكاديمية (360° Capstone Growth Engine).
        </p>
        <a href="track_b_4week_masterclass/assessments/OTB_360_Capstone_Brief_&_Evaluation.md" download class="btn-secondary" style="width: 100%;">📥 تحميل دليل المشروع</a>
      </div>
    </div>

  </main>
  {get_footer()}
</body>
</html>
"""

# WRITE FILES
pages_to_write = {
    "case-studies.html": p_case,
    "sops.html": p_sops,
    "downloads.html": p_downloads
}

for name, content in pages_to_write.items():
    with open(os.path.join(BASE_DIR, name), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {name}")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads successfully!")
