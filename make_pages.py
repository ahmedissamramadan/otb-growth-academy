import os
import shutil

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

def get_nav(active_page):
    pages = [
        ("index.html", "🏠 الرئيسية"),
        ("sprint.html", "⚡ معسكر الـ 5 أيام"),
        ("masterclass.html", "📚 الأكاديمية (4 أسابيع)"),
        ("prompts.html", "🤖 استوديو الأوامر"),
        ("case-studies.html", "💼 دراسات الحالة"),
        ("quiz.html", "📝 الاختبار والشهادة"),
        ("sops.html", "📋 الـ SOPs والبريفات"),
        ("downloads.html", "📥 التحميلات والموارد")
    ]
    
    links_html = ""
    for url, title in pages:
        active_cls = ' class="active"' if url == active_page else ""
        links_html += f'<li class="nav-item"><a href="{url}"{active_cls}>{title}</a></li>\n'
        
    return f"""
  <header class="navbar">
    <a href="index.html" class="brand-link">
      <span class="crown-logo">👑</span>
      <div class="brand-info">
        <h1>OTB GROWTH ACADEMY</h1>
        <p>THE CITY KINGS · INTERNAL MASTERY PORTAL 2026</p>
      </div>
    </a>
    <ul class="nav-links">
      {links_html}
    </ul>
    <a href="https://notebooklm.google.com/notebook/76ef5be2-d7d2-4a33-a88d-f88fc0fe1148" target="_blank" class="btn-notebook">
      <span>✨ مشروع NotebookLM</span>
    </a>
  </header>

  <div class="audio-banner">
    <div class="audio-title-group">
      <div class="live-indicator">
        <div class="pulse-dot"></div>
        <span>استوديو التدريب الصوتي المعتمد</span>
      </div>
      <span style="color: var(--gold-light); font-size: 0.85rem; font-weight: 600;">🎙️ OTB Growth Engineering & AI Podcast (Deep Dive Overview)</span>
    </div>
    <audio controls class="custom-audio-player">
      <source src="track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" type="audio/mp4">
      متصفحك لا يدعم مشغل الصوت المباشر.
    </audio>
  </div>
"""

def get_footer():
    return """
  <footer class="footer">
    <div class="footer-content">
      <div class="footer-brand">
        <span style="font-size: 2rem;">👑</span>
        <div>
          <h3 style="color: var(--gold-light); font-size: 1.1rem; font-weight: 800;">OTB Agency — We Are The City Kings</h3>
          <p style="color: var(--text-muted); font-size: 0.82rem;">استراتيجيات جريئة.. نتائج حقيقية | Bold Strategies. Real Results</p>
        </div>
      </div>
      <div class="footer-contact">
        <div>📍 القاهرة، مصر</div>
        <div>📞 <a href="tel:+201008080295">+20 100 808 0295</a></div>
        <div>✉️ <a href="mailto:otbagency5@gmail.com">otbagency5@gmail.com</a></div>
      </div>
    </div>
    <div class="footer-bottom">
      © 2026 OTB Agency Growth Engineering Academy. All Rights Reserved. Designed & Architected for Elite Performance.
    </div>
  </footer>
"""

# Page 1: index.html
p1 = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Growth Academy — The City Kings Internal Hub</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_nav("index.html")}

  <main class="container">
    
    <div class="page-header" style="text-align: center; padding: 2rem 0;">
      <span class="page-tag">👑 OFFICIAL INTERNAL ACADEMY · 2026 EDITION</span>
      <h1 class="page-title">أكاديمية OTB للتسويق: <span>ماستركلاس ملوك المدينة وهندسة النمو</span></h1>
      <p class="page-subtitle" style="margin: 0.75rem auto 1.5rem auto;">
        المنظومة التدريبية والتنفيذية الداخلية الموحدة لتمكين فرق عمل وكالة OTB الـ 16 دوراً وظيفياً بأقوى استراتيجيات التسويق الرقمي، إعلانات الأداء (Performance Ads)، وأتمتة الذكاء الاصطناعي.
      </p>
      <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
        <a href="sprint.html" class="btn-primary">⚡ بدء معسكر الـ 5 أيام السريع</a>
        <a href="prompts.html" class="btn-secondary">🤖 فتح استوديو أوامر الـ AI</a>
        <a href="quiz.html" class="btn-secondary">📝 دخول اختبار الكفاءة والشهادة</a>
      </div>
    </div>

    <div class="grid-4" style="margin-bottom: 3rem;">
      <div class="card" style="text-align: center;">
        <div style="font-size: 2.2rem; font-weight: 900; color: var(--gold-primary); font-family: 'JetBrains Mono';">16</div>
        <div style="font-size: 0.95rem; font-weight: 700; margin-top: 0.25rem;">وحدة تخصصية شاملة</div>
        <div style="font-size: 0.78rem; color: var(--text-muted);">تغطي كامل مسارات الـ Full-Stack Growth</div>
      </div>
      <div class="card" style="text-align: center;">
        <div style="font-size: 2.2rem; font-weight: 900; color: var(--emerald); font-family: 'JetBrains Mono';">5 Days</div>
        <div style="font-size: 0.95rem; font-weight: 700; margin-top: 0.25rem;">معسكر مكثف وسريع</div>
        <div style="font-size: 0.78rem; color: var(--text-muted);">تطبيقات وورش عمل يومية لكل قسم</div>
      </div>
      <div class="card" style="text-align: center;">
        <div style="font-size: 2.2rem; font-weight: 900; color: var(--cyan); font-family: 'JetBrains Mono';">50+</div>
        <div style="font-size: 0.95rem; font-weight: 700; margin-top: 0.25rem;">أمر ذكاء اصطناعي معتمد</div>
        <div style="font-size: 0.78rem; color: var(--text-muted);">بإطار RCIC المخصص لفرق OTB</div>
      </div>
      <div class="card" style="text-align: center;">
        <div style="font-size: 2.2rem; font-weight: 900; color: var(--crimson); font-family: 'JetBrains Mono';">7+ Years</div>
        <div style="font-size: 0.95rem; font-weight: 700; margin-top: 0.25rem;">خبرة سوق حقيقية موثقة</div>
        <div style="font-size: 0.78rem; color: var(--text-muted);">مبنية على أرقام وحملات كبرى البراندات</div>
      </div>
    </div>

    <h2 style="font-size: 1.5rem; font-weight: 800; color: var(--gold-light); margin-bottom: 1.5rem; border-right: 4px solid var(--gold-primary); padding-right: 0.75rem;">
      🚀 بوابات التعلم والتنفيذ السريع
    </h2>
    <div class="grid-3" style="margin-bottom: 3rem;">
      <a href="sprint.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="item-badge">المسار (أ)</span>
        <h3 class="card-title">⚡ معسكر الـ 5 أيام السريع (Sprint)</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.6;">
          الكبسولة التدريبية المكثفة لفريق العمل: STP، كتابة الكوبي رايتنج الإعلاني، ميديا بايينج ميتا وتيك توك، أتمتة الواتساب، وعقود الريتينر.
        </p>
        <div style="margin-top: 1rem; color: var(--gold-primary); font-weight: 700; font-size: 0.85rem;">استعراض أيام المعسكر ←</div>
      </a>

      <a href="masterclass.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="item-badge">المسار (ب)</span>
        <h3 class="card-title">📚 الأكاديمية الشاملة (4 أسابيع)</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.6;">
          التدريب التخصصي الأكاديمي لـ 16 وحدة دراسية كاملة تغطي الـ SEO، الإعلانات الممولة، الجروث هاكينج، ومشروع التخرج الشامل 360°.
        </p>
        <div style="margin-top: 1rem; color: var(--gold-primary); font-weight: 700; font-size: 0.85rem;">استعراض المنهج الأكاديمي ←</div>
      </a>

      <a href="prompts.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="item-badge">استوديو AI</span>
        <h3 class="card-title">🤖 استوديو الأوامر المخصصة</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.6;">
          مكتبة أوامر ذكاء اصطناعي تفاعلية لصناع المحتوى، الميديا بايرز، والمصممين لتوليد الاسكريبتات والإعلانات والتصاميم بضغطة زر.
        </p>
        <div style="margin-top: 1rem; color: var(--gold-primary); font-weight: 700; font-size: 0.85rem;">فتح محاكي الأوامر ←</div>
      </a>

      <a href="case-studies.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="item-badge">قاعدة المعرفة</span>
        <h3 class="card-title">💼 دراسات حالة عملاء OTB</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.6;">
          تحليل استراتيجي لعملاء الوكالة الموثقين (MIX Coffee, Rancho's EG, Dr. Zaghloul, Rice Patisserie) وشرح النماذج التكتيكية.
        </p>
        <div style="margin-top: 1rem; color: var(--gold-primary); font-weight: 700; font-size: 0.85rem;">قراءة دراسات الحالة ←</div>
      </a>

      <a href="quiz.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="item-badge">التقييم والاعتماد</span>
        <h3 class="card-title">📝 محاكي الاختبارات والشهادة</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.6;">
          اختبر معلوماتك التسويقية في 10 أسئلة تخصصية واحصل فوراً على شهادة إتمام معتمدة من أكاديمية OTB باسمك ورقم اعتماد رسمي.
        </p>
        <div style="margin-top: 1rem; color: var(--gold-primary); font-weight: 700; font-size: 0.85rem;">بدء الاختبار الآن ←</div>
      </a>

      <a href="sops.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="item-badge">التشغيل وCRM</span>
        <h3 class="card-title">📋 الـ SOPs ومولد البريفات</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.6;">
          إجراءات العمل القياسية داخل CoreLink CRM و ClickUp، ومولد تفاعلي لإنشاء بريفات المهام ومنع الهدر التشغيلي وإعادة العمل.
        </p>
        <div style="margin-top: 1rem; color: var(--gold-primary); font-weight: 700; font-size: 0.85rem;">توليد بريف فوري ←</div>
      </a>
    </div>

  </main>
  {get_footer()}
</body>
</html>
"""

# Page 2: sprint.html
p2 = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>⚡ معسكر الـ 5 أيام السريع — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_nav("sprint.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>معسكر الـ 5 أيام السريع</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-tag">TRACK A · FAST-TRACK SPRINT</span>
      <h1 class="page-title">معسكر الـ 5 أيام المكثف: <span>الزبدة التطبيقية لفرق OTB</span></h1>
      <p class="page-subtitle">دورة تدريبية سريعة ومضغوطة تركز على النماذج التكتيكية الفورية لكل دور وظيفي في الوكالة مع تكليفات عمل حقيقية.</p>
    </div>

    <div class="grid-2">
      <div>
        <div class="card" style="padding: 1.25rem;">
          <h3 style="color: var(--gold-primary); font-size: 1.1rem; margin-bottom: 1rem;">📅 جدول أيام المعسكر</h3>
          <div class="sidebar-list">
            <div class="sidebar-item active" onclick="loadDay(1)">
              <span class="item-badge">Day 01</span>
              <div class="item-title">تحليل السوق والتموضع (STP)</div>
              <div class="item-meta">👥 الاستراتيجيين ومدراء الحسابات</div>
            </div>
            <div class="sidebar-item" onclick="loadDay(2)">
              <span class="item-badge">Day 02</span>
              <div class="item-title">محرك الكرييتف وسيكولوجية الريلز</div>
              <div class="item-meta">✍️ كتاب المحتوى والمصممون</div>
            </div>
            <div class="sidebar-item" onclick="loadDay(3)">
              <span class="item-badge">Day 03</span>
              <div class="item-title">ميديا بايينج الأداء وسكيلينج ROAS</div>
              <div class="item-meta">📊 ميديا بايرز وهندسة النمو</div>
            </div>
            <div class="sidebar-item" onclick="loadDay(4)">
              <span class="item-badge">Day 04</span>
              <div class="item-title">الذكاء الاصطناعي وأتمتة الواتساب</div>
              <div class="item-meta">🤖 جميع أعضاء الفريق</div>
            </div>
            <div class="sidebar-item" onclick="loadDay(5)">
              <span class="item-badge">Day 05</span>
              <div class="item-title">الانضباط التشغيلي وعقود الريتينر</div>
              <div class="item-meta">💼 الإدارة ومدراء المشاريع</div>
            </div>
          </div>
        </div>
      </div>

      <div id="lessonContainer" class="lesson-content"></div>
    </div>

  </main>
  {get_footer()}

  <script>
    const sprintData = [
      {{
        day: 1,
        tag: "اليوم الأول · الاستراتيجية والتموضع",
        title: "تحليل السوق الاستراتيجي وبناء الهوية وتموضع البراند (STP & Positioning)",
        meta: "⏱️ 90 دقيقة تدريبية + 45 دقيقة ورشة تطبيقية · 👥 المستهدفون: الاستراتيجيون ومدراء الحسابات",
        boxes: [
          {{
            title: "🎯 أهداف جلسة اليوم الأول",
            content: "<ul><li>تطبيق نموذج STP (Segmentation, Targeting, Positioning) على قطاعات F&B، التجارة الإلكترونية، والخدمات في السوق المصري.</li><li>استخراج وصياغة شخصية العميل المثالي (Buyer Persona) بناءً على الدوافع النفسية والألم الحقيقي.</li><li>تطبيق نموذج The Ruler & Creator Archetype المعتمد لفرض هيبة العلامات التجارية.</li></ul>"
          }},
          {{
            title: "📊 معادلة التموضع التنافسي لـ OTB",
            content: "<p><b>Positioning Statement</b> = [الجمهور المستهدف] + [الفئة السوقية] + [الميزة التنافسية الجوهرية] + [سبب التصديق والإثبات].</p><p style='margin-top:0.5rem;'><i>دراسة حالة MIX Coffee:</i> 'لرواد الأعمال والشباب الباحثين عن تجربة قهوة فاخرة، MIX Coffee هي وجهتك الأولى التي تقدم بن مختص إثيوبي محمص طازجاً كل أسبوع لنمنحك أعلى طاقة وتركيز.'</p>"
          }},
          {{
            title: "🛠️ التكليف التطبيقي الفوري (Day 1 Assignment)",
            content: "<p>اختر أحد عملاء الوكالة (أو عميل جديد قيد الـ Onboarding) وقم بملء وثيقة البريف الاستراتيجي وتحديد 3 زوايا تسويقية غير تقليدية تستغل فجوات المنافسين.</p>"
          }}
        ]
      }},
      {{
        day: 2,
        tag: "اليوم الثاني · الكرييتف والمحتوى الفيرال",
        title: "محرك الكرييتف الإعلاني والكوبي رايتنج وسيكولوجية الفيديو القصير",
        meta: "⏱️ 90 دقيقة تدريبية + 45 دقيقة كتابة وتصوير · 👥 المستهدفون: صناع المحتوى والمصممون والمونتيرون",
        boxes: [
          {{
            title: "🎯 أهداف جلسة اليوم الثاني",
            content: "<ul><li>إتقان معادلات الكوبي رايتنج الإعلاني المباشر: AIDA و PAS و BAB.</li><li>تطبيق قاعدة الثواني الـ 3 الأولى لكسر التمرير (Pattern Interrupt) في ريلز وتيك توك.</li><li>رفع معدل الـ Hook Rate فوق 35% والـ Hold Rate فوق 15%.</li></ul>"
          }},
          {{
            title: "✍️ نموذج PAS الإعلاني لقطاع المطاعم (Rancho's Example)",
            content: "<p><b>Problem:</b> تعبت من البرجر اللي كله عيش واللحمة ملهاش طعم؟<br><b>Agitation:</b> بتدفع مبلغ محترم وفي الآخر بيجيلك بارد وتندم على الخروجة.<br><b>Solution:</b> في Rancho's مش بنعمل برجر عادي.. قطمة واحدة من الـ Smoked Double Beef وهتعرف يعني إيه برجر ملوك حقيقي!</p>"
          }},
          {{
            title: "🛠️ التكليف التطبيقي الفوري (Day 2 Assignment)",
            content: "<p>كتابة 3 نصوص إعلانية بـ 3 زوايا مختلفة (فكاهية، FOMO، هيبة اجتماعية) وتصميم اسكريبت ستوري بورد لريل 15 ثانية جاهز للتصوير.</p>"
          }}
        ]
      }},
      {{
        day: 3,
        tag: "اليوم الثالث · الميديا بايينج والأرقام",
        title: "ميديا بايينج الأداء على ميتا وتيك توك وسكيلينج الـ ROAS",
        meta: "⏱️ 90 دقيقة تدريبية + 45 دقيقة تحليل حسابات إعلانية · 👥 المستهدفون: الميديا بايرز وهندسة النمو",
        boxes: [
          {{
            title: "🎯 أهداف جلسة اليوم الثالث",
            content: "<ul><li>بناء الهياكل الإعلانية المتقدمة (CBO vs ABO & Advantage+).</li><li>ضبط التتبع الرقمي وحل قيود iOS 14.5+ عبر Conversions API (CAPI).</li><li>إتقان الرياضيات المالية: حساب ROAS, Break-Even ROAS, CPA, CAC, Contribution Margin.</li><li>تطبيق قواعد السكيلينج الرأسي والأفقي للوصول إلى ميزانيات $10,000+ شهرياً.</li></ul>"
          }},
          {{
            title: "🧮 معادلات الميديا باير المحترف",
            content: "<p><b>Break-Even ROAS</b> = 1 / Gross Profit Margin %<br><i>إذا كان هامش الربح 25%، فإن نقطة التعادل الإعلانية المطلوبة = 4.0x.</i></p><p style='margin-top:0.5rem;'><b>قاعدة الـ 20%:</b> زيادة ميزانية الحملة الرابحة بـ 20% فقط كل 48-72 ساعة لتجنب إعادة دخول مرحلة التعلم (Learning Phase).</p>"
          }},
          {{
            title: "🛠️ التكليف التطبيقي الفوري (Day 3 Assignment)",
            content: "<p>تدقيق حساب إعلاني حقيقي لأحد عملاء OTB، مراجعة جودة مطابقة أحداث CAPI، وإعداد مصفوفة الميزانية الأسبوعية وجدول الـ Testing & Scaling.</p>"
          }}
        ]
      }},
      {{
        day: 4,
        tag: "اليوم الرابع · الذكاء الاصطناعي والأتمتة",
        title: "الذكاء الاصطناعي التسويقي وهندسة الأوامر وأتمتة الليدز",
        meta: "⏱️ 90 دقيقة تدريبية + 45 دقيقة بناء مسار أتمتة · 👥 المستهدفون: جميع أعضاء الفريق",
        boxes: [
          {{
            title: "🎯 أهداف جلسة اليوم الرابع",
            content: "<ul><li>إتقان إطار RCIC المتقدم (Role, Context, Instruction, Constraint) لصياغة أوامر تسويقية دقيقة.</li><li>أتمتة إنتاج الأصول المرئية والموشن والاسكريبتات بأدوات AI الحديثة.</li><li>ربط وتفعيل قنوات المراسلة المباشرة عبر WhatsApp Business API لتحويل المحادثات لمبيعات.</li></ul>"
          }},
          {{
            title: "🤖 إطار RCIC لهندسة الأوامر",
            content: "<p>• <b>Role:</b> أنت Senior Copywriter & Growth Marketer خبير.<br>• <b>Context:</b> العميل هو براند مجوهرات فاخر (Dr. Zaghloul) يستهدف المقبلين على الزواج.<br>• <b>Instruction:</b> اكتب 3 إعلانات تركز على الأمان والقيمة الاستثمارية.<br>• <b>Constraint:</b> ممنوع العبارات المستهلكة، النبرة ملكية وواثقة بالعامية المصرية الراقية.</p>"
          }},
          {{
            title: "🛠️ التكليف التطبيقي الفوري (Day 4 Assignment)",
            content: "<p>استخدام أوامر الـ AI من دليل OTB لتوليد 5 نصوص إعلانية وبرودكت شوت 3D لعميل حقيقي، ورسم مسار ردود WhatsApp API لأحد المتاجر.</p>"
          }}
        ]
      }},
      {{
        day: 5,
        tag: "اليوم الخامس · التشغيل وعقود الريتينر",
        title: "الانضباط التشغيلي وإدارة المشاريع وعقود الريتينر الشهرية",
        meta: "⏱️ 90 دقيقة تدريبية + 45 دقيقة محاكاة إغلاق الصفقات · 👥 المستهدفون: الإدارة ومدراء الحسابات",
        boxes: [
          {{
            title: "🎯 أهداف جلسة اليوم الخامس",
            content: "<ul><li>القضاء على متلازمة البريف الفارغ (Empty Brief) وخفض نسبة إعادة العمل بأكثر من 40%.</li><li>تطبيق إجراءات العمل القياسية (SOPs) داخل CoreLink CRM و ClickUp.</li><li>تفعيل اتفاقيات مستوى الخدمة (SLA) وتصعيد المهام المتأخرة بعد 48 ساعة.</li><li>إغلاق وتغليف عقود الريتينر الشهرية ($1,500 - $3,000) للعملاء.</li></ul>"
          }},
          {{
            title: "💼 باقات الريتينر الشهرية المعتمدة في OTB",
            content: "<p>• <b>Growth Starter ($1,200/شهر):</b> للمشاريع الناشئة والمطاعم الفردية.<br>• <b>Dominance Retainer 👑 ($2,500/شهر):</b> للبراندات المتوسطة وسلاسل الفروع.<br>• <b>Enterprise Scale ($4,500+/شهر):</b> للشركات الكبرى ومتاجر التجارة الإلكترونية الضخمة.</p>"
          }},
          {{
            title: "🏆 مشروع ختام المعسكر (Sprint Capstone)",
            content: "<p>تقديم خطة نمو شهرية مصغرة لعميل حقيقي تتضمن (الاستراتيجية، عينة المحتوى، خطة الإعلانات، ومسار الأتمتة) وتحديث ملفات الـ SOPs الخاصة بك.</p>"
          }}
        ]
      }}
    ];

    function loadDay(dayNum) {{
      const data = sprintData.find(d => d.day === dayNum);
      const container = document.getElementById("lessonContainer");
      
      document.querySelectorAll(".sidebar-item").forEach((item, idx) => {{
        if (idx + 1 === dayNum) item.classList.add("active");
        else item.classList.remove("active");
      }});

      let boxesHtml = "";
      data.boxes.forEach(b => {{
        boxesHtml += `
          <div class="lesson-box">
            <h3>${{b.title}}</h3>
            ${{b.content}}
          </div>
        `;
      }});

      container.innerHTML = `
        <div class="lesson-hero">
          <span class="item-badge">${{data.tag}}</span>
          <h2>${{data.title}}</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">${{data.meta}}</p>
        </div>
        ${{boxesHtml}}
        <div style="display: flex; justify-content: space-between; margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--border-color);">
          ${{dayNum > 1 ? `<button class="btn-secondary" onclick="loadDay(${{dayNum - 1}})">← اليوم السابق</button>` : '<div></div>'}}
          ${{dayNum < 5 ? `<button class="btn-primary" onclick="loadDay(${{dayNum + 1}})">اليوم التالي →</button>` : '<a href="quiz.html" class="btn-primary">الانتقال لاختبار الكفاءة 👑</a>'}}
        </div>
      `;
    }}

    loadDay(1);
  </script>
</body>
</html>
"""

# Page 3: masterclass.html
p3 = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📚 الأكاديمية الشاملة لـ 4 أسابيع — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_nav("masterclass.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>الأكاديمية الشاملة (4 أسابيع)</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-tag">TRACK B · FULL-SPECTRUM MASTERCLASS</span>
      <h1 class="page-title">الأكاديمية الأكاديمية الشاملة: <span>16 وحدة تخصصية في 4 مراحل</span></h1>
      <p class="page-subtitle">هندسة كاملة وموسوعية لكافة محاور التسويق الرقمي والميديا بايينج وهندسة النمو مبنية على 46 مصدراً مرجعياً وخبرة 7+ سنوات.</p>
    </div>

    <div class="grid-2">
      <div>
        <div class="card" style="padding: 1.25rem;">
          <h3 style="color: var(--gold-primary); font-size: 1.1rem; margin-bottom: 1rem;">📚 مراحل الأكاديمية الـ 4</h3>
          <div class="sidebar-list">
            <div class="sidebar-item active" onclick="loadWeek(1)">
              <span class="item-badge">المرحلة 01 · الأسبوع 1</span>
              <div class="item-title">التموضع، أبحاث السوق والبراندنج</div>
              <div class="item-meta">الوحدات 01 - 02 · الهوية الملكية لـ OTB</div>
            </div>
            <div class="sidebar-item" onclick="loadWeek(2)">
              <span class="item-badge">المرحلة 02 · الأسبوع 2</span>
              <div class="item-title">محرك الكرييتف، الكوبي رايتنج والسيو</div>
              <div class="item-meta">الوحدات 03 - 05 · السيو والفيديو القصير</div>
            </div>
            <div class="sidebar-item" onclick="loadWeek(3)">
              <span class="item-badge">المرحلة 03 · الأسبوع 3</span>
              <div class="item-title">ميديا بايينج الأداء وقرصنة النمو</div>
              <div class="item-meta">الوحدات 06 - 09 · ميتا، تيك توك و B2B</div>
            </div>
            <div class="sidebar-item" onclick="loadWeek(4)">
              <span class="item-badge">المرحلة 04 · الأسبوع 4</span>
              <div class="item-title">الذكاء الاصطناعي ومشروع التخرج 360°</div>
              <div class="item-meta">الوحدات 10 - 16 · أتمتة ومحرك النمو</div>
            </div>
          </div>
        </div>

        <div class="card" style="margin-top: 1.5rem; text-align: center;">
          <h4 style="color: var(--gold-light); font-size: 1rem; margin-bottom: 0.5rem;">👑 مشروع التخرج النهائي</h4>
          <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 1rem;">تسليم محرك النمو الشامل 360° Capstone Growth Engine لبراند حقيقي.</p>
          <a href="quiz.html" class="btn-primary" style="width: 100%;">دخول الاختبار النهائي</a>
        </div>
      </div>

      <div id="weekContainer" class="lesson-content"></div>
    </div>

  </main>
  {get_footer()}

  <script>
    const weeksData = [
      {{
        week: 1,
        tag: "الأسبوع الأول · التأسيس الاستراتيجي",
        title: "المرحلة 1: التموضع الاستراتيجي، أبحاث السوق، وبناء العلامات التجارية الكبرى",
        modules: [
          {{
            num: "الوحدة 01",
            name: "مبادئ التسويق الاستراتيجي وبحوث السوق (Market Research & STP)",
            desc: "تحليل البيئة الكلية PESTEL، مصفوفة Porter's Five Forces، صياغة شخصية العميل (Persona)، وتحديد القيمة المقترحة الفريدة (UVP)."
          }},
          {{
            num: "الوحدة 02",
            name: "استراتيجيات البراندنج وبناء الهوية ونبرة الصوت (Brand Identity Systems)",
            desc: "فلسفة الهوية لملوك المدينة (The Ruler & Creator Framework)، صياغة ميثاق نبرة الصوت، وبناء الـ Brand Book المتكامل."
          }}
        ],
        lab: "بناء ملف التموضع الاستراتيجي (Market Positioning Bible) لأحد عملاء قطاع الأغذية أو التجارة الإلكترونية مع تحليل 5 منافسين وتحديد فجوات السوق."
      }},
      {{
        week: 2,
        tag: "الأسبوع الثاني · المحتوى والظهور العضوي",
        title: "المرحلة 2: محرك الكرييتف، الكوبي رايتنج الإعلاني، والسيو التنافسي",
        modules: [
          {{
            num: "الوحدة 03",
            name: "استراتيجيات صناعة المحتوى والكوبي رايتنج الإعلاني (Direct-Response Copy)",
            desc: "نماذج AIDA و PAS و BAB، صياغة العروض التي لا تقاوم (Irresistible Offers)، وهندسة جداول النشر لـ 90 يوماً."
          }},
          {{
            num: "الوحدة 04 & 05",
            name: "السيو الأساسي والتقني وبناء الروابط الخلفية (SEO Mastery)",
            desc: "بحث الكلمات المفتاحية وفهم نية البحث (Search Intent)، السيو الداخلي On-Page، السيو التقني للمواقع، وبناء الباك لينكس القوية."
          }}
        ],
        lab: "إنتاج حقيبة إعلانية مرئية متكاملة (10 بوستات + 4 ريلز مصورة + مقال سيو متوافق مع خوارزميات جوجل 2026)."
      }},
      {{
        week: 3,
        tag: "الأسبوع الثالث · إعلانات الأداء والنمو",
        title: "المرحلة 3: ميديا بايينج الأداء، قرصنة النمو، وسكيلينج الـ ROAS",
        modules: [
          {{
            num: "الوحدة 06 & 07",
            name: "إعلانات Meta و TikTok وقنوات B2B (Performance Advertising)",
            desc: "بناء هياكل الحملات (CBO vs ABO)، ضبط Conversions API (CAPI)، هندسة الجماهير المشابهة، وبناء شبكات لينكد إن."
          }},
          {{
            num: "الوحدة 08 & 09",
            name: "الجروث هاكينج ومنظومة الـ AARRR وسكيلينج الميزانيات",
            desc: "مصفوفة أولويات التجارب السريعة (ICE Matrix)، وتوسيع الميزانيات من $1,000 إلى $50,000 بأمان كامل ومضاعفة الـ ROAS."
          }}
        ],
        lab: "إعداد خطة إطلاق حملة ممولة بميزانية $5,000 شهرياً لعميل تجارة إلكترونية مع مصفوفة توقعات العائد والـ ROAS."
      }},
      {{
        week: 4,
        tag: "الأسبوع الرابع · الأتمتة والمحرك الشامل",
        title: "المرحلة 4: أتمتة الذكاء الاصطناعي، تكامل CRM، ومشروع التخرج 360°",
        modules: [
          {{
            num: "الوحدة 10 & 11",
            name: "أتمتة الذكاء الاصطناعي والتسويق بالبريد والواتساب (Funnel Automation)",
            desc: "بناء مسارات WhatsApp Business API والإيميل لاستعادة السلات المتروكة وتأهيل الليدز آلياً."
          }},
          {{
            num: "الوحدة 12 & 13",
            name: "الانضباط التشغيلي، CRM، وإدارة عقود الوكالة (Agency Mastery)",
            desc: "إدارة العمليات عبر CoreLink CRM و ClickUp، وإغلاق عقود الريتينر الشهرية ($1,500 - $3,000)."
          }}
        ],
        lab: "تسليم مشروع التخرج الشامل 360° Capstone Growth Engine مع عرض تقديمي تنفيذي (Pitch Deck) لبراند حقيقي."
      }}
    ];

    function loadWeek(weekNum) {{
      const data = weeksData.find(w => w.week === weekNum);
      const container = document.getElementById("weekContainer");

      document.querySelectorAll(".sidebar-item").forEach((item, idx) => {{
        if (idx + 1 === weekNum) item.classList.add("active");
        else item.classList.remove("active");
      }});

      let modulesHtml = "";
      data.modules.forEach(m => {{
        modulesHtml += `
          <div class="lesson-box">
            <span class="item-badge">${{m.num}}</span>
            <h3>${{m.name}}</h3>
            <p>${{m.desc}}</p>
          </div>
        `;
      }});

      container.innerHTML = `
        <div class="lesson-hero">
          <span class="item-badge">${{data.tag}}</span>
          <h2>${{data.title}}</h2>
        </div>
        ${{modulesHtml}}
        <div class="lesson-box" style="border-right-color: var(--emerald); background: rgba(16, 185, 129, 0.08);">
          <h3 style="color: var(--emerald);">🧪 ورشة العمل الأسبوعية (Applied Lab)</h3>
          <p>${{data.lab}}</p>
        </div>
      `;
    }}

    loadWeek(1);
  </script>
</body>
</html>
"""

# Page 4: prompts.html
p4 = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🤖 استوديو أوامر الذكاء الاصطناعي — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_nav("prompts.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>استوديو أوامر الذكاء الاصطناعي</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-tag">AI STUDIO · RCIC PROMPT ENGINE</span>
      <h1 class="page-title">استوديو أوامر الذكاء الاصطناعي: <span>المولد التفاعلي لفرق OTB</span></h1>
      <p class="page-subtitle">اختر دورك الوظيفي، وخصص بيانات العميل، وانسخ البرومبت الاحترافي المعتمد بنقرة واحدة لتحقيق نتائج فائقة الدقة.</p>
    </div>

    <div class="card" style="margin-bottom: 2.5rem; border: 2px solid var(--gold-primary);">
      <h2 style="color: var(--gold-light); font-size: 1.4rem; margin-bottom: 1.25rem;">⚡ المولد التفاعلي للأوامر الذكية</h2>
      <div class="grid-3">
        <div class="form-group">
          <label class="form-label">القسم / الدور الوظيفي:</label>
          <select id="builderRole" class="form-select" onchange="updateCustomPrompt()">
            <option value="copy">كتابة الإعلانات والكوبي رايتنج (Copywriting)</option>
            <option value="media">الميديا بايينج وسكيلينج الحملات (Media Buying)</option>
            <option value="design">تصوير وتوليد برودكت شوت 3D (Midjourney)</option>
            <option value="account">مقترحات عقود الريتينر (Account Management)</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">اسم البراند / العميل:</label>
          <input type="text" id="builderBrand" class="form-input" value="MIX Coffee" oninput="updateCustomPrompt()">
        </div>
        <div class="form-group">
          <label class="form-label">القطاع / الفئة:</label>
          <input type="text" id="builderNiche" class="form-input" value="Specialty Coffee & F&B" oninput="updateCustomPrompt()">
        </div>
      </div>

      <div class="form-group">
        <label class="form-label">الأمر التكتيكي المولد فورياً (جاهز للإرسال للذكاء الاصطناعي):</label>
        <div id="livePromptBox" class="prompt-box"></div>
      </div>

      <button class="btn-primary" onclick="copyLivePrompt()">📋 نسخ الأمر المخصص للحافظة</button>
    </div>

    <h2 style="font-size: 1.5rem; font-weight: 800; color: var(--gold-light); margin-bottom: 1.5rem; border-right: 4px solid var(--gold-primary); padding-right: 0.75rem;">
      📖 موسوعة الأوامر المعتمدة للأقسام
    </h2>

    <div class="grid-2">
      <div class="card">
        <span class="item-badge">Copywriting</span>
        <h3 class="card-title">إعلان PAS تحويلي للمطاعم والأغذية</h3>
        <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 1rem;">صياغة 3 إعلانات تحويلية تركز على إثارة الرغبة والطلب المباشر.</p>
        <div class="prompt-box">Role: Senior Direct-Response Copywriter at OTB Agency.
Context: Client is [Brand Name] in Egypt. Target: Foodies aged 18-35.
Task: Write 3 ad copies using PAS (Problem-Agitation-Solution) in modern Egyptian Arabic.
Constraints: Bold tone, no clichés, high-urgency CTA for WhatsApp ordering.</div>
        <button class="btn-secondary" style="width: 100%;" onclick="copyStaticPrompt(this)">📋 نسخ الأمر</button>
      </div>

      <div class="card">
        <span class="item-badge">Media Buying</span>
        <h3 class="card-title">تشخيص حساب إعلاني وقرار الـ Scaling</h3>
        <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 1rem;">تحليل أرقام الحملة واستخراج اختناقات التحويل وتحديد اتجاه السكيلينج.</p>
        <div class="prompt-box">Role: Principal Growth Marketer & Media Buyer at OTB Agency.
Context: Analyzing 7-day data for [Client Name]: Spend, CTR, Purchases, ROAS, CPA.
Task: Full funnel diagnosis (Hook Rate, Hold Rate, Drop-off) + Scaling direction.
Format: 48-hour clear action plan to scale ROAS > 4.0x.</div>
        <button class="btn-secondary" style="width: 100%;" onclick="copyStaticPrompt(this)">📋 نسخ الأمر</button>
      </div>

      <div class="card">
        <span class="item-badge">3D Design</span>
        <h3 class="card-title">برومبت تصوير تجاري 3D لـ Midjourney</h3>
        <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 1rem;">توليد لقطات منتجات فخمة بإضاءة استوديو وسينمائية داكنة.</p>
        <div class="prompt-box">/imagine prompt: Ultra-realistic 3D commercial product shot of [Product Name], obsidian black podium, royal gold accents and droplets, dramatic rim lighting, cinematic 8k studio render --ar 9:16 --style raw --v 6.0</div>
        <button class="btn-secondary" style="width: 100%;" onclick="copyStaticPrompt(this)">📋 نسخ الأمر</button>
      </div>

      <div class="card">
        <span class="item-badge">Account Management</span>
        <h3 class="card-title">صياغة مقترح عقد ريتينر شهري ($2,500)</h3>
        <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 1rem;">خطاب تنفيذي مقنع يوضح العائد وخطة النمو لـ 90 يوماً.</p>
        <div class="prompt-box">Role: Commercial Director at OTB Marketing Studio (The City Kings).
Context: Executive Retainer proposal for [Client] to scale from $20k to $100k GMV.
Task: 1-page executive summary: Market gaps, 90-day growth roadmap, $2,500/mo deliverables, and ROAS governance.</div>
        <button class="btn-secondary" style="width: 100%;" onclick="copyStaticPrompt(this)">📋 نسخ الأمر</button>
      </div>
    </div>

  </main>
  {get_footer()}

  <script>
    function updateCustomPrompt() {{
      const role = document.getElementById("builderRole").value;
      const brand = document.getElementById("builderBrand").value || "البراند";
      const niche = document.getElementById("builderNiche").value || "القطاع";
      const box = document.getElementById("livePromptBox");

      if (role === "copy") {{
        box.innerText = "Role: Senior Direct-Response Copywriter & Growth Marketer at OTB Agency.\\n" +
          "Context: We are running high-performance Meta and TikTok campaigns for " + brand + " (" + niche + ") in the Egyptian and Arab market.\\n" +
          "Task: Write 3 ad variations using the PAS (Problem-Agitation-Solution) framework in engaging, refined Egyptian Arabic.\\n" +
          "Constraints:\\n" +
          "- Hook must be under 8 words.\\n" +
          "- Tone: Bold, authoritative, and royal ('The City Kings' style).\\n" +
          "- Include strong scarcity/urgency Call To Action linking to our WhatsApp ordering menu.";
      }} else if (role === "media") {{
        box.innerText = "Role: Principal Media Buyer and Growth Architect at OTB Agency.\\n" +
          "Context: Analyzing performance campaigns for " + brand + " (" + niche + "). Target ROAS is 4.0x, current CPA is $[Amount].\\n" +
          "Task:\\n" +
          "1. Conduct a full funnel diagnostic on Hook Rate, Hold Rate, and Click-to-Purchase conversion drop-offs.\\n" +
          "2. Recommend whether to Scale Vertically (20% budget boost) or Horizontally (Broad targeting + new angles).\\n" +
          "3. Outline a 48-hour tactical action plan.";
      }} else if (role === "design") {{
        box.innerText = "/imagine prompt: Cinematic commercial product photography of " + brand + " (" + niche + "), obsidian noir stone podium, royal gold accents, elegant backlight, 8k resolution studio render, dramatic rim lighting --ar 9:16 --style raw --v 6.0";
      }} else if (role === "account") {{
        box.innerText = "Role: Commercial Growth Director at OTB Agency.\\n" +
          "Context: Drafting a $2,500/month Retainer Proposal for " + brand + " in the " + niche + " sector.\\n" +
          "Task: Draft an executive 1-page proposal covering market positioning, 90-day growth roadmap, content & media deliverables, and expected ROAS targets.";
      }}
    }}

    function copyLivePrompt() {{
      const text = document.getElementById("livePromptBox").innerText;
      navigator.clipboard.writeText(text).then(() => {{
        alert("تم نسخ الأمر بنجاح إلى الحافظة!");
      }});
    }}

    function copyStaticPrompt(btn) {{
      const text = btn.previousElementSibling.innerText;
      navigator.clipboard.writeText(text).then(() => {{
        btn.innerText = "✅ تم النسخ!";
        setTimeout(() => btn.innerText = "📋 نسخ الأمر", 2000);
      }});
    }}

    updateCustomPrompt();
  </script>
</body>
</html>
"""

# Page 5: case-studies.html
p5 = f"""<!DOCTYPE html>
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
  {get_nav("case-studies.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>دراسات الحالة وقاعدة المعرفة</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-tag">CASE STUDIES & KNOWLEDGE BASE</span>
      <h1 class="page-title">دراسات حالة عملاء OTB: <span>أرقام حقيقية ونتائج موثقة</span></h1>
      <p class="page-subtitle">استعراض لأبرز النماذج العملية المطبقة في السوق المصري لعملاء الوكالة، وكيف تحولت التحديات إلى أرباح وعوائد استثنائية.</p>
    </div>

    <div class="grid-3" style="margin-bottom: 3rem;">
      <div class="card">
        <span class="item-badge" style="background: var(--gold-primary);">Specialty Coffee</span>
        <h3 class="card-title">☕ MIX Coffee</h3>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1rem;">
          <b>التحدي:</b> منافسة شرسة في سوق القهوة المختصة وضعف التميز البصري.<br>
          <b>الاستراتيجية:</b> إعادة صياغة الهوية كوجهة أولى لرواد الأعمال مع محتوى داكن فاخر وفيديوهات ASMR لصنع القهوة.<br>
          <b>النتيجة:</b> نمو التفاعل بنسبة <b>+180%</b> ومضاعفة مبيعات الفروع.
        </p>
      </div>

      <div class="card">
        <span class="item-badge" style="background: var(--crimson);">Gourmet Burgers</span>
        <h3 class="card-title">🍔 Rancho's EG</h3>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1rem;">
          <b>التحدي:</b> انخفاض الهامش الربحي بسبب حرق الأسعار والعروض التقليدية.<br>
          <b>الاستراتيجية:</b> التموضع كبرجر فاخر ملحمي ذي جودة لا تضاهى مع حملات Click-to-WhatsApp عالية الاستهداف.<br>
          <b>النتيجة:</b> تحقيق معدل إعادة طلب <b>36.8%</b> ورفع متوسط قيمة الفاتورة 45%.
        </p>
      </div>

      <div class="card">
        <span class="item-badge" style="background: var(--cyan);">Luxury Jewelry</span>
        <h3 class="card-title">💍 Dr. Zaghloul Jewelry</h3>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1rem;">
          <b>التحدي:</b> ضعف الثقة في شراء المجوهرات والذهب عبر السوشيال ميديا.<br>
          <b>الاستراتيجية:</b> التركيز على أمان الاستثمار، وعرض فيديوهات عالية الدقة للقطع مع سرد قصة كل تصميم.<br>
          <b>النتيجة:</b> تحقيق مبيعات مباشرة ومعدل عائد إعلاني <b>ROAS يتجاوز 7.5x</b>.
        </p>
      </div>

      <div class="card">
        <span class="item-badge" style="background: var(--purple);">Pastry & Sweets</span>
        <h3 class="card-title">🍰 Rice Patisserie</h3>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1rem;">
          <b>التحدي:</b> تذبذب الطلب الموسمي ومنافسة محلات الحلويات الكبرى.<br>
          <b>الاستراتيجية:</b> إطلاق حملات أعياد ومناسبات مسبقة الحجز مع أتمتة رسائل العروض للعملاء السابقين.<br>
          <b>النتيجة:</b> نفاد كامل الكميات المحجوزة قبل 48 ساعة من المناسبات.
        </p>
      </div>

      <div class="card">
        <span class="item-badge" style="background: var(--emerald);">E-Commerce & Retail</span>
        <h3 class="card-title">📦 Sakr Store</h3>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1rem;">
          <b>التحدي:</b> ارتفاع تكلفة الاستحواذ على العميل (CAC) في التجارة الإلكترونية.<br>
          <b>الاستراتيجية:</b> إعادة هيكلة إعلانات Advantage+ وتتبع CAPI المتقدم مع عروض الباقات المجمعة (Bundles).<br>
          <b>النتيجة:</b> خفض تكلفة الشراء بنسبة <b>32%</b> ورفع الـ AOV بمقدار 50%.
        </p>
      </div>

      <div class="card">
        <span class="item-badge" style="background: var(--cyan);">Medical & Clinics</span>
        <h3 class="card-title">🧪 Elag Labs</h3>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1rem;">
          <b>التحدي:</b> صعوبة جذب حجوزات التحاليل الطبية والزيارات المنزلية.<br>
          <b>الاستراتيجية:</b> حملات توعوية سريعة تركز على دقة النتائج وراحة الزيارة المنزلية مع بوت حجز فوري.<br>
          <b>النتيجة:</b> استقبال أكثر من <b>800 حجز شهرياً</b> عبر المراسلة المباشرة.
        </p>
      </div>
    </div>

    <h2 style="font-size: 1.5rem; font-weight: 800; color: var(--gold-light); margin-bottom: 1.5rem; border-right: 4px solid var(--gold-primary); padding-right: 0.75rem;">
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

# Page 6: quiz.html
p6 = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📝 اختبار الكفاءة والشهادة — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=Cinzel:wght@700;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
    .quiz-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.75rem;
      margin-bottom: 1.5rem;
      transition: var(--transition-smooth);
    }}
    .quiz-option {{
      display: block;
      padding: 1rem 1.25rem;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-sm);
      margin-bottom: 0.75rem;
      cursor: pointer;
      font-size: 0.95rem;
      transition: var(--transition-smooth);
    }}
    .quiz-option:hover {{
      background: rgba(245, 158, 11, 0.08);
      border-color: var(--gold-primary);
    }}
    .quiz-option.selected {{
      background: rgba(245, 158, 11, 0.2);
      border-color: var(--gold-primary);
      color: var(--gold-light);
      font-weight: 700;
    }}
    .quiz-option.correct {{
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: var(--emerald) !important;
      color: #FFF !important;
    }}
    .quiz-option.wrong {{
      background: rgba(225, 29, 72, 0.25) !important;
      border-color: var(--crimson) !important;
    }}
    .certificate-box {{
      background: #000;
      border: 4px solid var(--gold-primary);
      border-radius: 16px;
      padding: 3rem 2rem;
      text-align: center;
      position: relative;
      box-shadow: 0 0 50px rgba(245, 158, 11, 0.3);
      margin-top: 2rem;
    }}
    .cert-title {{
      font-family: 'Cinzel', serif;
      font-size: 2.2rem;
      font-weight: 900;
      color: var(--gold-primary);
      letter-spacing: 2px;
      margin: 1rem 0;
    }}
  </style>
</head>
<body>
  {get_nav("quiz.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>اختبار الكفاءة والشهادة</span>
  </div>

  <main class="container" style="max-width: 900px;">
    
    <div class="page-header" style="text-align: center;">
      <span class="page-tag">EXAMINATION & CERTIFICATION</span>
      <h1 class="page-title">اختبار الكفاءة التسويقية: <span>شهادة ملوك المدينة</span></h1>
      <p class="page-subtitle" style="margin: 0 auto;">أجب عن الأسئلة الـ 10 المعيارية التالية لإثبات استيعابك للمنهج والحصول على شهادة الاعتماد الرسمية باسمك.</p>
    </div>

    <div class="card" style="margin-bottom: 2rem;">
      <div class="form-group" style="margin: 0;">
        <label class="form-label">الاسم بالكامل (ليظهر على الشهادة المعتمدة):</label>
        <input type="text" id="traineeName" class="form-input" placeholder="اكتب اسمك الثلاثي هنا..." value="أحمد عصام رمضان">
      </div>
    </div>

    <div id="quizContainer"></div>

    <div style="text-align: center; margin-top: 2.5rem;">
      <button class="btn-primary" style="padding: 1rem 3rem; font-size: 1.15rem;" onclick="submitExam()">
        👑 تسليم الإجابات وإصدار الشهادة
      </button>
    </div>

    <div id="resultContainer" style="display: none;"></div>

  </main>
  {get_footer()}

  <script>
    const questions = [
      {{
        q: "ما هو التموضع والنمط النفسي المعتمد لوكالة OTB في السوق؟",
        options: [
          "المنافسة على أقل سعر ممكن وتقليل التكاليف",
          "The Ruler & The Creator (ملوك المدينة: الهيبة والجرأة والتركيز الصارم على النتائج)",
          "الاعتماد على الإعلانات الممولة دون أي هوية",
          "تقديم تصاميم عادية دون قياس العائد المالي"
        ],
        correct: 1,
        expl: "تموضع OTB يجمع بين هيبة القيادة والجرأة الإبداعية لفرض السيطرة السوقية وصناعة عوائد ملموسة."
      }},
      {{
        q: "ما هو الهدف الحاسم من أول 3 ثوانٍ في أي فيديو ريلز إعلاني (Short-Form Video)؟",
        options: [
          "عرض تفاصيل فروع الشركة وأرقام الهواتف",
          "كسر التمرير (Pattern Interrupt) وجذب انتباه المشاهد الفوري (Hook Rate > 35%)",
          "شرح تاريخ تأسيس الشركة منذ 2018",
          "وضع حقوق الملكية الفكرية والشعار"
        ],
        correct: 1,
        expl: "أول 3 ثوانٍ تحسم بقاء المشاهد وتحدد تكلفة الألف ظهور ومعدل تفاعل الإعلان."
      }},
      {{
        q: "إذا كان هامش الربح الإجمالي لمنتج هو 25%، فما هو الـ Break-Even ROAS المطلوب لتحقيق نقطة التعادل؟",
        options: [
          "1.5x",
          "2.0x",
          "4.0x (حيث 1 / 0.25 = 4)",
          "8.0x"
        ],
        correct: 2,
        expl: "نقطة التعادل = 1 مقسومة على هامش الربح (1 / 0.25 = 4.0x)."
      }},
      {{
        q: "ما هي القاعدة الآمنة للتوسع الرأسي (Vertical Scaling) في ميزانية الحملات الإعلانية الرابحة؟",
        options: [
          "مضاعفة الميزانية 200% كل يوم",
          "زيادة الميزانية بنسبة 20% كل 48-72 ساعة لتجنب إعادة دخول مرحلة التعلم",
          "تغيير الاستهداف الإعلاني يومياً",
          "إيقاف الحملة وإعادة تشغيلها بميزانية جديدة"
        ],
        correct: 1,
        expl: "زيادة 20% كل يومين إلى 3 أيام تضمن استقرار أداء الخوارزمية وتكلفة التحويل."
      }},
      {{
        q: "ما الذي يرمز له حرف (C) الأخير في إطار هندسة الأوامر التسويقية RCIC؟",
        options: [
          "Creativity (الإبداع)",
          "Constraints (القيود والشروط والممنوعات)",
          "Category (الفئة)",
          "Customer (العميل)"
        ],
        correct: 1,
        expl: "Constraints هي المحددات التي تمنع الـ AI من استخدام عبارات مستهلكة وتضبط النبرة بدقة."
      }},
      {{
        q: "كيف يتم القضاء على 'متلازمة التوجيه الفارغ' (Empty Brief) داخل CoreLink CRM؟",
        options: [
          "التواصل عبر رسائل واتساب شفهية وسريعة",
          "إلزامية تعبئة نموذج البريف الكامل والاعتماد النصي بنسبة 100% قبل بدء التصميم",
          "البدء في التصميم فوراً دون انتظار المحتوى",
          "إلغاء المراجعات بالكامل"
        ],
        correct: 1,
        expl: "نماذج البريف الإلزامية و Sequential Locking تخفض نسبة إعادة العمل بأكثر من 40%."
      }},
      {{
        q: "في نموذج PAS للكتابة الإعلانية، ماذا يمثل حرف (A)؟",
        options: [
          "Action (الفعل)",
          "Agitation (تهويل المشكلة وتوضيح ألم استمرارها)",
          "Awareness (الوعي)",
          "Attention (الانتباه)"
        ],
        correct: 1,
        expl: "Agitation هو تعميق المشكلة وإشعار العميل بخسارة عدم حلها فوراً."
      }},
      {{
        q: "ما هي الفائدة الأساسية من إعداد Conversions API (CAPI) مع Meta Pixel؟",
        options: [
          "تقليل تكلفة إعلانات جوجل",
          "تجاوز قيود الخصوصية و iOS 14.5+ وتمرير بيانات الشراء مباشرة من السيرفر بجودة مطابقة عالية",
          "زيادة عدد المتابعين الأورجانيك",
          "الحصول على علامة التوثيق الزرقاء"
        ],
        correct: 1,
        expl: "CAPI يرسل الأحداث مباشرة من الخادم لميتا مما يحمي بيانات التتبع والـ ROAS."
      }},
      {{
        q: "ما هو معدل الـ Hook Rate المستهدف في إعلانات الريلز الاحترافية لـ OTB؟",
        options: [
          "أكثر من 5%",
          "أكثر من 15%",
          "أكثر من 35%",
          "100%"
        ],
        correct: 2,
        expl: "الهدف القياسي لفيديوهات OTB هو تخطي 35% في أول 3 ثوانٍ."
      }},
      {{
        q: "ما هو السعر القياسي المعتمد لباقة الـ Dominance Retainer الشهرية لـ OTB؟",
        options: [
          "$300 / شهر",
          "$800 / شهر",
          "$2,500 / شهر",
          "$10,000 / شهر"
        ],
        correct: 2,
        expl: "باقة Dominance Retainer تغطي هوية كاملة و24 محتوى عالي الجودة وميديا بايينج وأتمتة بسعر $2,500 شهرياً."
      }}
    ];

    let userAnswers = {{}};

    function renderQuiz() {{
      const container = document.getElementById("quizContainer");
      let html = "";
      questions.forEach((q, qIdx) => {{
        let optsHtml = "";
        q.options.forEach((opt, oIdx) => {{
          optsHtml += `
            <div class="quiz-option" data-q="${{qIdx}}" data-o="${{oIdx}}" onclick="selectOpt(${{qIdx}}, ${{oIdx}})">
              ${{opt}}
            </div>
          `;
        }});
        html += `
          <div class="quiz-card">
            <h3 style="color: var(--gold-light); font-size: 1.15rem; margin-bottom: 1rem;">سؤال ${{qIdx + 1}}: ${{q.q}}</h3>
            <div>${{optsHtml}}</div>
            <div id="expl_${{qIdx}}" style="display:none; margin-top:1rem; padding:0.75rem; background:rgba(245,158,11,0.1); border-radius:8px; font-size:0.85rem; border-right:3px solid var(--gold-primary);"></div>
          </div>
        `;
      }});
      container.innerHTML = html;
    }}

    function selectOpt(qIdx, oIdx) {{
      userAnswers[qIdx] = oIdx;
      document.querySelectorAll(`[data-q="${{qIdx}}"]`).forEach(el => el.classList.remove("selected"));
      document.querySelector(`[data-q="${{qIdx}}"][data-o="${{oIdx}}"]`).classList.add("selected");
    }}

    function submitExam() {{
      const name = document.getElementById("traineeName").value || "خريج الأكاديمية";
      let score = 0;

      questions.forEach((q, qIdx) => {{
        const selected = userAnswers[qIdx];
        const expl = document.getElementById(`expl_${{qIdx}}`);
        expl.style.display = "block";
        expl.innerHTML = `<b>💡 توضيح الإجابة الصحيحة:</b> ${{q.expl}}`;

        document.querySelectorAll(`[data-q="${{qIdx}}"]`).forEach((el, oIdx) => {{
          if (oIdx === q.correct) el.classList.add("correct");
          if (selected !== undefined && selected === oIdx && selected !== q.correct) {{
            el.classList.add("wrong");
          }}
        }});

        if (selected === q.correct) score++;
      }});

      const percentage = Math.round((score / questions.length) * 100);
      const resContainer = document.getElementById("resultContainer");
      resContainer.style.display = "block";

      const certId = "OTB-" + Math.floor(100000 + Math.random() * 900000);
      const dateStr = new Date().toLocaleDateString('ar-EG', {{ year: 'numeric', month: 'long', day: 'numeric' }});

      resContainer.innerHTML = `
        <div class="certificate-box">
          <div style="font-size: 3rem;">👑</div>
          <div style="font-size: 0.9rem; letter-spacing: 3px; color: var(--gold-light); text-transform: uppercase;">OTB Marketing Studio · City Kings</div>
          <div class="cert-title">CERTIFICATE OF GROWTH MASTERY</div>
          <p style="color: var(--text-muted); font-size: 1rem;">تشهد أكاديمية وكالة OTB للتسويق وهندسة النمو بأن</p>
          <h2 style="font-size: 2.2rem; color: #FFF; margin: 1rem 0; font-weight: 900; background: var(--gold-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">${{name}}</h2>
          <p style="color: #E2E8F0; max-width: 650px; margin: 0 auto; line-height: 1.8;">
            قد اجتاز بنجاح كافة متطلبات معسكر وأكاديمية <b>النمو والتسويق الرقمي المتقدم والذكاء الاصطناعي (Full-Stack Growth Engineering)</b> بدرجة <b>${{percentage}}%</b>، وأصبح مؤهلاً لتطبيق استراتيجيات وإعلانات ملوك المدينة.
          </p>
          <div style="display: flex; justify-content: space-around; margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(245, 158, 11, 0.3);">
            <div>
              <div style="font-size: 0.75rem; color: var(--text-muted);">رقم الاعتماد الرقمي</div>
              <div style="font-family: 'JetBrains Mono'; font-weight: 700; color: var(--gold-primary);">${{certId}}</div>
            </div>
            <div>
              <div style="font-size: 0.75rem; color: var(--text-muted);">تاريخ المنح</div>
              <div style="font-weight: 700; color: #FFF;">${{dateStr}}</div>
            </div>
            <div>
              <div style="font-size: 0.75rem; color: var(--text-muted);">الاعتماد الرسمي</div>
              <div style="font-weight: 800; color: var(--gold-light);">OTB Agency 👑</div>
            </div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 1.5rem;">
          <button class="btn-secondary" onclick="window.print()">🖨️ طباعة أو حفظ الشهادة كـ PDF</button>
        </div>
      `;

      resContainer.scrollIntoView({{ behavior: "smooth" }});
    }}

    renderQuiz();
  </script>
</body>
</html>
"""

# Page 7: sops.html
p7 = f"""<!DOCTYPE html>
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
  {get_nav("sops.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>إجراءات التشغيل القياسية والبريفات</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-tag">OPERATIONAL EXCELLENCE & CRM</span>
      <h1 class="page-title">الانضباط التشغيلي: <span>مولد البريفات القياسية وإجراءات CoreLink</span></h1>
      <p class="page-subtitle">القضاء على متلازمة التوجيه الفارغ، توحيد نماذج الإسناد، وضمان التزام الفرق باتفاقيات مستوى الخدمة (SLA).</p>
    </div>

    <div class="grid-2" style="margin-bottom: 3rem;">
      <div class="card" style="border: 2px solid var(--gold-primary);">
        <h3 style="color: var(--gold-light); font-size: 1.25rem; margin-bottom: 1.25rem;">⚙️ مولد البريف الإلزامي للقسم</h3>
        <div class="form-group">
          <label class="form-label">اسم العميل / البراند:</label>
          <input type="text" id="sopClient" class="form-input" value="Rancho's EG">
        </div>
        <div class="form-group">
          <label class="form-label">القسم والتكليف:</label>
          <select id="sopType" class="form-select">
            <option>كتابة محتوى وكوبي رايتنج إعلاني (Copywriting)</option>
            <option>تصميم سوشيال ميديا وموشن جرافيك (Design/Video)</option>
            <option>إطلاق وإدارة حملات ميديا بايينج ممولة (Media Buying)</option>
            <option>أتمتة رسائل واتساب وخدمة عملاء (WhatsApp CRM)</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">الهدف التسويقي الأساسي:</label>
          <input type="text" id="sopGoal" class="form-input" value="مضاعفة مبيعات فرع التجمع ورفع متوسط الفاتورة">
        </div>
        <div class="form-group">
          <label class="form-label">الزاوية الإعلانية (Angle):</label>
          <input type="text" id="sopAngle" class="form-input" value="زاوية الطعم الملحمي الحصري للـ Smoked Brisket">
        </div>
        <div class="form-group">
          <label class="form-label">المحددات والممنوعات ونبرة الصوت:</label>
          <textarea id="sopNotes" class="form-textarea" rows="3">النبرة ملكية وواثقة بالعامية المصرية الراقية. ممنوع العبارات المبتذلة. الـ CTA يوجه لطلب القائمة عبر واتساب.</textarea>
        </div>
        <button class="btn-primary" style="width: 100%;" onclick="generateSopBrief()">⚡ توليد البريف القياسي الآن</button>
      </div>

      <div class="card">
        <h3 style="color: var(--gold-light); font-size: 1.25rem; margin-bottom: 1.25rem;">📋 النص الجاهز للإسناد في CoreLink CRM</h3>
        <textarea id="sopResult" class="form-textarea" style="height: 380px; font-family: 'JetBrains Mono', monospace; font-size: 0.88rem; line-height: 1.7;" readonly placeholder="اضغط على زر التوليد وسيظهر البريف هنا..."></textarea>
        <button class="btn-secondary" style="width: 100%; margin-top: 1rem;" onclick="copyBriefText()">📋 نسخ البريف للإسناد الفوري</button>
      </div>
    </div>

    <h2 style="font-size: 1.5rem; font-weight: 800; color: var(--gold-light); margin-bottom: 1.5rem; border-right: 4px solid var(--gold-primary); padding-right: 0.75rem;">
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
    function generateSopBrief() {{
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
      if (!txt) return alert("يرجى توليد البريف أولاً!");
      navigator.clipboard.writeText(txt).then(() => {{
        alert("تم نسخ البريف بنجاح! جاهز للصق في CoreLink CRM.");
      }});
    }}

    generateSopBrief();
  </script>
</body>
</html>
"""

# Page 8: downloads.html
p8 = f"""<!DOCTYPE html>
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
  {get_nav("downloads.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>مركز الموارد والتحميلات</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-tag">STUDIO ASSETS & RESOURCE HUB</span>
      <h1 class="page-title">مركز الموارد والتحميلات: <span>أصول الوكالة وملفات التدريب</span></h1>
      <p class="page-subtitle">جميع الأدلة التكتيكية، ملفات المنهج الأكاديمي، مخرجات Gemini Studio، والبودكاست الصوتي المعتمد متاحة للتحميل المباشر.</p>
    </div>

    <div class="grid-3" style="margin-bottom: 3rem;">
      <div class="card">
        <span class="item-badge">Podcast & Audio</span>
        <h3 class="card-title">🎙️ البودكاست الاستراتيجي المعتمد</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1.25rem;">
          حلقة صوتية معمقة تم توليدها عبر Gemini Studio تناقش هندسة النمو ومحرك الذكاء الاصطناعي لوكالة OTB.
        </p>
        <a href="track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" download class="btn-primary" style="width: 100%;">📥 تحميل ملف الصوت (34 MB)</a>
      </div>

      <div class="card">
        <span class="item-badge">Briefing Doc</span>
        <h3 class="card-title">📑 التقرير الاستراتيجي الشامل</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1.25rem;">
          وثيقة التوجيه الاستراتيجي الصادرة من الاستوديو تلخص الهيكل التنظيمي ومؤشرات الأداء لوكالة OTB.
        </p>
        <a href="track_b_4week_masterclass/studio_artifacts/OTB_Executive_Strategic_Briefing.md" download class="btn-secondary" style="width: 100%;">📥 تحميل المستند (Markdown)</a>
      </div>

      <div class="card">
        <span class="item-badge">AI Bible</span>
        <h3 class="card-title">📖 موسوعة الأوامر التكتيكية (Bible)</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1.25rem;">
          أكثر من 50 برومبت معتمد ومفصل لجميع أقسام الوكالة الـ 16 دوراً وظيفياً بصيغة Markdown.
        </p>
        <a href="track_a_fast_track_sprint/cheatsheets/OTB_Prompt_Engineering_Bible.md" download class="btn-secondary" style="width: 100%;">📥 تحميل موسوعة الأوامر</a>
      </div>

      <div class="card">
        <span class="item-badge">Media Buying</span>
        <h3 class="card-title">✈️ دليل تدقيق الإعلانات الممولة</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1.25rem;">
          قائمة الفحص الفني قبل إطلاق الحملات (Pre-Flight Checklist) وقواعد السكيلينج الرأسي والأفقي.
        </p>
        <a href="track_a_fast_track_sprint/cheatsheets/OTB_Media_Buying_Checklist.md" download class="btn-secondary" style="width: 100%;">📥 تحميل قائمة الفحص</a>
      </div>

      <div class="card">
        <span class="item-badge">CRM SOPs</span>
        <h3 class="card-title">📋 نماذج البريفات وإجراءات العمل</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1.25rem;">
          نماذج التوجيه الإلزامي للأقسام وقواعد الـ SLA المعتمدة داخل CoreLink CRM.
        </p>
        <a href="track_a_fast_track_sprint/cheatsheets/OTB_SOP_Briefing_Templates.md" download class="btn-secondary" style="width: 100%;">📥 تحميل نماذج الـ SOPs</a>
      </div>

      <div class="card">
        <span class="item-badge">Capstone Brief</span>
        <h3 class="card-title">🎓 دليل مشروع التخرج الشامل 360°</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1.25rem;">
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

pages = {
    "index.html": p1,
    "sprint.html": p2,
    "masterclass.html": p3,
    "prompts.html": p4,
    "case-studies.html": p5,
    "quiz.html": p6,
    "sops.html": p7,
    "downloads.html": p8
}

for name, content in pages.items():
    with open(os.path.join(BASE_DIR, name), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {name}")

print(f"Syncing to {DOWNLOADS_DIR}...")
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("ALL 8 PAGES SUCCESSFULLY GENERATED AND SYNCED!")
