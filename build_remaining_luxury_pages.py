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
# 2. PROMPTS.HTML
# ==============================================================================
p_prompts = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🤖 استوديو أوامر الذكاء الاصطناعي — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
    .filter-pills {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-bottom: 2rem;
    }}
    .pill-btn {{
      background: var(--bg-card);
      border: 1px solid var(--gold-border);
      color: var(--text-muted);
      padding: 0.5rem 1.15rem;
      border-radius: var(--radius-full);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      transition: var(--transition-fast);
    }}
    .pill-btn:hover {{
      color: var(--gold-100);
      border-color: var(--gold-500);
      background: rgba(245, 158, 11, 0.1);
    }}
    .pill-btn.active {{
      background: var(--gold-gradient);
      color: #000;
      border-color: var(--gold-500);
      font-weight: 800;
    }}
  </style>
</head>
<body>
  {get_header("prompts.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>استوديو أوامر الذكاء الاصطناعي</span>
  </div>

  <main class="container">
    
    <div class="page-header">
      <span class="page-pill">AI STUDIO · RCIC PROMPT ENGINE</span>
      <h1 class="page-title">استوديو أوامر الذكاء الاصطناعي: <span>المولد التفاعلي لفرق OTB</span></h1>
      <p class="page-subtitle">اختر دورك الوظيفي، وخصص بيانات العميل والميزانية، وانسخ البرومبت الاحترافي المعتمد بنقرة واحدة لتحقيق نتائج فائقة الدقة والتحويل.</p>
    </div>

    <!-- INTERACTIVE BUILDER CARD -->
    <div class="card" style="margin-bottom: 3rem; border: 2px solid var(--gold-500);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
        <h2 style="color: var(--gold-100); font-size: 1.4rem; font-weight: 900; margin: 0;">⚡ المولد التفاعلي للأوامر الذكية</h2>
        <span class="live-badge">RCIC Engine Active</span>
      </div>

      <div class="grid-3" style="margin-bottom: 1.5rem;">
        <div>
          <label style="display: block; font-size: 0.88rem; font-weight: 700; color: var(--gold-200); margin-bottom: 0.5rem;">الدور والتكليف:</label>
          <select id="builderRole" class="btn-secondary" style="width: 100%; padding: 0.75rem 1rem; border-radius: var(--radius-sm); color: #FFF; background: var(--bg-surface); text-align: right;" onchange="updatePrompt()">
            <option value="copy">كتابة إعلانات تحويلية (Direct-Response Copy)</option>
            <option value="reels">اسكريبت ريلز 15 ثانية (Viral Hook Script)</option>
            <option value="media">تشخيص حساب إعلاني وسكيلينج (Media Buying)</option>
            <option value="design">لقطات برودكت شوت 3D لـ Midjourney</option>
            <option value="account">مقترح عقد ريتينر شهري ($2,500/mo)</option>
            <option value="whatsapp">أتمتة ردود ومبيعات WhatsApp API</option>
          </select>
        </div>

        <div>
          <label style="display: block; font-size: 0.88rem; font-weight: 700; color: var(--gold-200); margin-bottom: 0.5rem;">اسم البراند / العميل:</label>
          <input type="text" id="builderBrand" class="btn-secondary" style="width: 100%; padding: 0.75rem 1rem; border-radius: var(--radius-sm); color: #FFF; background: var(--bg-surface); text-align: right;" value="MIX Coffee" oninput="updatePrompt()">
        </div>

        <div>
          <label style="display: block; font-size: 0.88rem; font-weight: 700; color: var(--gold-200); margin-bottom: 0.5rem;">القطاع / الفئة السوقية:</label>
          <input type="text" id="builderNiche" class="btn-secondary" style="width: 100%; padding: 0.75rem 1rem; border-radius: var(--radius-sm); color: #FFF; background: var(--bg-surface); text-align: right;" value="Specialty Coffee & F&B" oninput="updatePrompt()">
        </div>
      </div>

      <div style="margin-bottom: 1.5rem;">
        <label style="display: block; font-size: 0.88rem; font-weight: 700; color: var(--gold-200); margin-bottom: 0.5rem;">الأمر التكتيكي المولد فورياً (جاهز للإرسال للـ AI):</label>
        <div id="livePromptBox" class="prompt-box"></div>
      </div>

      <button class="btn-primary" style="padding: 0.85rem 2rem;" onclick="copyLivePrompt()">📋 نسخ الأمر المخصص للحافظة</button>
    </div>

    <!-- FILTER PILLS & SEARCH -->
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
      <h2 style="font-size: 1.5rem; font-weight: 900; color: var(--gold-100); border-right: 4px solid var(--gold-500); padding-right: 0.85rem; margin: 0;">
        📖 موسوعة الأوامر المعتمدة للأقسام
      </h2>
      <div class="filter-pills" style="margin: 0;">
        <button class="pill-btn active" onclick="filterPrompts('all', this)">الكل</button>
        <button class="pill-btn" onclick="filterPrompts('copy', this)">الكوبي رايتنج</button>
        <button class="pill-btn" onclick="filterPrompts('media', this)">الميديا بايينج</button>
        <button class="pill-btn" onclick="filterPrompts('design', this)">التصميم و 3D</button>
        <button class="pill-btn" onclick="filterPrompts('account', this)">إدارة الحسابات</button>
      </div>
    </div>

    <!-- STATIC PROMPTS GRID -->
    <div class="grid-2" id="promptsGrid">
      <div class="card" data-cat="copy">
        <span class="item-badge">Copywriting</span>
        <h3 class="card-title">إعلان PAS تحويلي للمطاعم والـ F&B</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1rem;">صياغة 3 إعلانات تحويلية تركز على إثارة الرغبة والطلب المباشر.</p>
        <div class="prompt-box">Role: Senior Direct-Response Copywriter at OTB Agency.
Context: Client is [Brand Name] in Egypt. Target: Foodies aged 18-35.
Task: Write 3 ad copies using PAS (Problem-Agitation-Solution) in modern Egyptian Arabic.
Constraints: Bold tone, no clichés, high-urgency CTA for WhatsApp ordering.</div>
        <button class="btn-secondary" style="width: 100%;" onclick="copyTextFromElement(this)">📋 نسخ الأمر</button>
      </div>

      <div class="card" data-cat="copy">
        <span class="item-badge">Short-Form Video</span>
        <h3 class="card-title">اسكريبت ريلز 15 ثانية بسرد قصصي خاطف</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1rem;">تصميم اسكريبت بمؤثرات صوتية ولقطات ASMR سريعة.</p>
        <div class="prompt-box">Role: Viral Video Director at OTB Agency.
Context: Creating an Instagram Reel for [Brand Name] in [Industry].
Task: Write a shot-by-shot 15-second script with a 3-second hook, fast ASMR cuts, and direct promotional offer.
Format: Table [Time (Sec) | Visual Scene | Audio Effect | On-Screen Text / Voiceover].</div>
        <button class="btn-secondary" style="width: 100%;" onclick="copyTextFromElement(this)">📋 نسخ الأمر</button>
      </div>

      <div class="card" data-cat="media">
        <span class="item-badge">Media Buying</span>
        <h3 class="card-title">تشخيص الحملات الإعلانية وقرار السكيلينج</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1rem;">تحليل أرقام الحملة واستخراج اختناقات التحويل وتحديد اتجاه السكيلينج.</p>
        <div class="prompt-box">Role: Principal Growth Marketer & Media Buyer at OTB Agency.
Context: Analyzing 7-day data for [Client Name]: Spend, CTR, Purchases, ROAS, CPA.
Task: Full funnel diagnosis (Hook Rate, Hold Rate, Drop-off) + Scaling direction.
Format: 48-hour clear action plan to scale ROAS > 4.0x.</div>
        <button class="btn-secondary" style="width: 100%;" onclick="copyTextFromElement(this)">📋 نسخ الأمر</button>
      </div>

      <div class="card" data-cat="design">
        <span class="item-badge">3D Design</span>
        <h3 class="card-title">برومبت تصوير تجاري 3D لـ Midjourney</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1rem;">توليد لقطات منتجات فخمة بإضاءة استوديو وسينمائية داكنة.</p>
        <div class="prompt-box">/imagine prompt: Ultra-realistic 3D commercial product shot of [Product Name], obsidian black podium, royal gold accents and droplets, dramatic rim lighting, cinematic 8k studio render --ar 9:16 --style raw --v 6.0</div>
        <button class="btn-secondary" style="width: 100%;" onclick="copyTextFromElement(this)">📋 نسخ الأمر</button>
      </div>

      <div class="card" data-cat="account">
        <span class="item-badge">Account Management</span>
        <h3 class="card-title">صياغة مقترح عقد ريتينر شهري ($2,500/mo)</h3>
        <p style="color: var(--text-muted); font-size: 0.88rem; margin-bottom: 1rem;">خطاب تنفيذي مقنع يوضح العائد وخطة النمو لـ 90 يوماً.</p>
        <div class="prompt-box">Role: Commercial Director at OTB Marketing Studio (The City Kings).
Context: Executive Retainer proposal for [Client] to scale from $20k to $100k GMV.
Task: 1-page executive summary: Market gaps, 90-day growth roadmap, $2,500/mo deliverables, and ROAS governance.</div>
        <button class="btn-secondary" style="width: 100%;" onclick="copyTextFromElement(this)">📋 نسخ الأمر</button>
      </div>
    </div>

  </main>
  {get_footer()}

  <script>
    function updatePrompt() {{
      const role = document.getElementById("builderRole").value;
      const brand = document.getElementById("builderBrand").value || "البراند";
      const niche = document.getElementById("builderNiche").value || "القطاع";
      const box = document.getElementById("livePromptBox");

      if (role === "copy") {{
        box.innerText = "Role: Senior Direct-Response Copywriter at OTB Agency.\\n" +
          "Context: We are running high-performance Meta and TikTok campaigns for " + brand + " (" + niche + ") in Egypt.\\n" +
          "Task: Write 3 ad variations using the PAS (Problem-Agitation-Solution) framework in refined modern Egyptian Arabic.\\n" +
          "Constraints: Hook under 8 words, bold royal tone, strong urgency CTA linking to WhatsApp ordering menu.";
      }} else if (role === "reels") {{
        box.innerText = "Role: Master Viral Short-Form Video Director for OTB Agency.\\n" +
          "Context: Instagram Reel / TikTok for " + brand + " in the " + niche + " sector.\\n" +
          "Task: Write a shot-by-shot 15-second script with seconds 0-3 scroll-stopping hook, fast ASMR cuts, and direct promotional offer.\\n" +
          "Format: Table [Time (Sec) | Visual Scene | Audio Effect | On-Screen Text / Voiceover].";
      }} else if (role === "media") {{
        box.innerText = "Role: Principal Media Buyer and Growth Architect at OTB Agency.\\n" +
          "Context: Analyzing performance campaigns for " + brand + " (" + niche + "). Target ROAS is 4.0x, current CPA is $[Amount].\\n" +
          "Task: Diagnose Hook Rate and Click-to-Purchase conversion drop-offs, recommend Vertical or Horizontal scaling, and provide a 48-hour tactical action plan.";
      }} else if (role === "design") {{
        box.innerText = "/imagine prompt: Ultra-realistic commercial 3D product photography of " + brand + " (" + niche + "), obsidian noir stone podium, royal gold accents and droplets, dramatic rim lighting, cinematic 8k resolution studio render --ar 9:16 --style raw --v 6.0";
      }} else if (role === "account") {{
        box.innerText = "Role: Commercial Growth Director at OTB Agency.\\n" +
          "Context: Drafting a $2,500/month Dominance Retainer Proposal for " + brand + " in " + niche + ".\\n" +
          "Task: Draft an executive 1-page proposal covering market positioning, 90-day growth roadmap, content & media deliverables, and expected ROAS targets.";
      }} else if (role === "whatsapp") {{
        box.innerText = "Role: Lead Generation & CRM Automation Specialist at OTB Agency.\\n" +
          "Context: Designing a WhatsApp Business API chatbot sequence for " + brand + " (" + niche + ").\\n" +
          "Task: Create a 3-step conversation flow (Welcome & Name qualification, Catalog/Offer presentation, and instant Order confirmation) with quick-reply buttons.";
      }}
    }}

    function copyLivePrompt() {{
      const text = document.getElementById("livePromptBox").innerText;
      copyText(text, "👑 تم نسخ البرومبت المخصص بنجاح!");
    }}

    function copyTextFromElement(btn) {{
      const text = btn.previousElementSibling.innerText;
      copyText(text);
    }}

    function filterPrompts(cat, btn) {{
      document.querySelectorAll(".pill-btn").forEach(p => p.classList.remove("active"));
      btn.classList.add("active");

      document.querySelectorAll("#promptsGrid .card").forEach(c => {{
        if (cat === "all" || c.getAttribute("data-cat") === cat) {{
          c.style.display = "block";
        }} else {{
          c.style.display = "none";
        }}
      }});
    }}

    updatePrompt();
  </script>
</body>
</html>
"""

# ==============================================================================
# 3. QUIZ.HTML (EXAM & CERTIFICATE ENGINE)
# ==============================================================================
p_quiz = f"""<!DOCTYPE html>
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
    .quiz-option {{
      display: block;
      padding: 1.1rem 1.35rem;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-sm);
      margin-bottom: 0.85rem;
      cursor: pointer;
      font-size: 0.96rem;
      transition: var(--transition-fast);
    }}
    .quiz-option:hover {{
      background: rgba(245, 158, 11, 0.08);
      border-color: var(--gold-500);
      transform: translateX(-3px);
    }}
    .quiz-option.selected {{
      background: rgba(245, 158, 11, 0.22);
      border-color: var(--gold-500);
      color: var(--gold-100);
      font-weight: 800;
    }}
    .quiz-option.correct {{
      background: rgba(16, 185, 129, 0.28) !important;
      border-color: var(--emerald) !important;
      color: #FFF !important;
    }}
    .quiz-option.wrong {{
      background: rgba(225, 29, 72, 0.28) !important;
      border-color: var(--crimson) !important;
    }}
    .certificate-box {{
      background: #020305;
      border: 6px solid var(--gold-500);
      border-radius: 24px;
      padding: 3.5rem 2.5rem;
      text-align: center;
      position: relative;
      box-shadow: 0 0 60px rgba(245, 158, 11, 0.35);
      margin-top: 2.5rem;
    }}
    .cert-title {{
      font-family: 'Cinzel', serif;
      font-size: 2.3rem;
      font-weight: 900;
      color: var(--gold-400);
      letter-spacing: 2px;
      margin: 1rem 0;
    }}
  </style>
</head>
<body>
  {get_header("quiz.html")}

  <div class="breadcrumb-bar">
    <a href="index.html">الرئيسية</a> / <span>اختبار الكفاءة والشهادة</span>
  </div>

  <main class="container" style="max-width: 960px;">
    
    <div class="page-header" style="text-align: center;">
      <span class="page-pill">EXAMINATION & OFFICIAL CERTIFICATION</span>
      <h1 class="page-title">اختبار الكفاءة التسويقية: <span>شهادة ملوك المدينة</span></h1>
      <p class="page-subtitle" style="margin: 0 auto;">أجب عن الأسئلة الـ 10 المعيارية التالية لإثبات استيعابك لمنظومة النمو وإصدار شهادة الاعتماد الملكية الرسمية باسمك.</p>
    </div>

    <div class="card" style="margin-bottom: 2rem;">
      <label style="display: block; font-size: 0.95rem; font-weight: 800; color: var(--gold-200); margin-bottom: 0.6rem;">
        👑 الاسم بالكامل (ليظهر بشكل رسمي على الشهادة المعتمدة):
      </label>
      <input type="text" id="traineeName" class="btn-secondary" style="width: 100%; padding: 0.9rem 1.25rem; font-size: 1.05rem; font-weight: 700; color: #FFF; background: var(--bg-surface); text-align: right;" placeholder="اكتب اسمك الثلاثي هنا..." value="أحمد عصام رمضان">
    </div>

    <div id="quizContainer"></div>

    <div style="text-align: center; margin-top: 3rem;">
      <button class="btn-primary" style="padding: 1.1rem 3.5rem; font-size: 1.2rem;" onclick="submitExam()">
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
          <div class="card" style="margin-bottom: 1.75rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
              <span class="page-pill" style="font-size: 0.75rem; margin: 0;">سؤال ${{qIdx + 1}} من 10</span>
            </div>
            <h3 style="color: var(--gold-100); font-size: 1.2rem; font-weight: 800; margin-bottom: 1.25rem;">${{q.q}}</h3>
            <div>${{optsHtml}}</div>
            <div id="expl_${{qIdx}}" style="display:none; margin-top:1rem; padding:1rem; background:rgba(245,158,11,0.1); border-radius:var(--radius-sm); font-size:0.9rem; border-right:4px solid var(--gold-500); color:#FFF;"></div>
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
          <div style="font-size: 3.5rem;">👑</div>
          <div style="font-size: 0.95rem; letter-spacing: 3px; color: var(--gold-200); text-transform: uppercase; font-weight: 800;">OTB Marketing Studio · City Kings</div>
          <div class="cert-title">CERTIFICATE OF GROWTH MASTERY</div>
          <p style="color: var(--text-muted); font-size: 1.05rem;">تشهد أكاديمية وكالة OTB للتسويق وهندسة النمو بأن</p>
          <h2 style="font-size: 2.4rem; color: #FFF; margin: 1.25rem 0; font-weight: 900; background: var(--gold-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">${{name}}</h2>
          <p style="color: #E2E8F0; max-width: 680px; margin: 0 auto; line-height: 1.85; font-size: 1.05rem;">
            قد اجتاز بنجاح كافة متطلبات معسكر وأكاديمية <b>النمو والتسويق الرقمي المتقدم والذكاء الاصطناعي (Full-Stack Growth Engineering)</b> بدرجة <b>${{percentage}}%</b>، وأصبح مؤهلاً لتطبيق استراتيجيات وإعلانات ملوك المدينة.
          </p>
          <div style="display: flex; justify-content: space-around; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(245, 158, 11, 0.3);">
            <div>
              <div style="font-size: 0.78rem; color: var(--text-muted);">رقم الاعتماد الرقمي</div>
              <div style="font-family: 'JetBrains Mono'; font-weight: 800; color: var(--gold-400); font-size: 1.1rem;">${{certId}}</div>
            </div>
            <div>
              <div style="font-size: 0.78rem; color: var(--text-muted);">تاريخ المنح</div>
              <div style="font-weight: 800; color: #FFF;">${{dateStr}}</div>
            </div>
            <div>
              <div style="font-size: 0.78rem; color: var(--text-muted);">الاعتماد الرسمي</div>
              <div style="font-weight: 900; color: var(--gold-200); font-size: 1.1rem;">OTB Agency 👑</div>
            </div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 2rem;">
          <button class="btn-primary" style="padding: 0.9rem 2.5rem;" onclick="window.print()">🖨️ طباعة أو حفظ الشهادة كـ PDF</button>
        </div>
      `;

      showToast("👑 تهانينا! تم إصدار شهادة الاعتماد بنجاح!");
      resContainer.scrollIntoView({{ behavior: "smooth" }});
    }}

    renderQuiz();
  </script>
</body>
</html>
"""

# WRITE FILES
pages_to_write = {
    "prompts.html": p_prompts,
    "quiz.html": p_quiz
}

for name, content in pages_to_write.items():
    with open(os.path.join(BASE_DIR, name), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {name}")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
