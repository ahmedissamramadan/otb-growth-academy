import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from generate_master_academy import COURSES_DATA

def get_nav(active):
    items = [
        ("index.html", "الرئيسية"),
        ("mindmap.html", "الخريطة الذهنية"),
        ("courses.html", "المقررات"),
        ("sprint.html", "المعسكر (5 أيام)"),
        ("prompts.html", "الأوامر (AI)"),
        ("quiz.html", "الشهادة"),
        ("downloads.html", "الموارد")
    ]
    links = ""
    for url, title in items:
        cls = ' class="active"' if url == active else ""
        links += f'<li><a href="{url}"{cls}>{title}</a></li>\n'
        
    return f"""
  <nav class="navbar">
    <a href="index.html" class="brand">
      <span class="brand-crown">👑</span>
      <span>OTB Academy</span>
    </a>
    <ul class="nav-links">
      {links}
    </ul>
  </nav>
"""

def get_footer():
    return """
  <footer class="footer">
    <div style="margin-bottom: 0.5rem; color: var(--text);">OTB Agency — We Are The City Kings 👑</div>
    <div>القاهرة · <a href="tel:+201008080295">+20 100 808 0295</a> · <a href="mailto:otbagency5@gmail.com">otbagency5@gmail.com</a></div>
  </footer>
  <script src="shared_ui.js"></script>
"""

# ==============================================================================
# 1. INDEX.HTML (MINIMAL DASHBOARD)
# ==============================================================================
p_index = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_nav("index.html")}

  <main class="container">
    
    <!-- MINIMAL HERO -->
    <div class="hero">
      <span class="hero-tag">OTB INTERNAL ACADEMY 2026</span>
      <h1 class="hero-title">منظومة النمو والتسويق الرقمي</h1>
      <p class="hero-desc">
        المرجع التدريبي والتنفيذي الموحد لفريق وكالة OTB. يضم 19 مقرراً تدريبياً، وأوامر الذكاء الاصطناعي، ودراسات حالة العملاء، وإجراءات العمل اليومية.
      </p>
      <div style="display: flex; justify-content: center; gap: 0.75rem; flex-wrap: wrap;">
        <a href="courses.html" class="btn btn-primary">استعراض المقررات الـ 19</a>
        <a href="mindmap.html" class="btn btn-secondary">الخريطة الذهنية</a>
        <a href="sprint.html" class="btn btn-secondary">معسكر الـ 5 أيام</a>
      </div>
    </div>

    <!-- MINIMAL AUDIO STRIP -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <span>🎙️</span>
        <span>البودكاست الاستراتيجي المعتمد (Gemini Studio)</span>
      </div>
      <audio controls>
        <source src="track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" type="audio/mp4">
      </audio>
    </div>

    <!-- 4 PHASES SUMMARY -->
    <h2 style="font-size: 1.25rem; color: var(--text); margin-bottom: 1.25rem; font-weight: 700;">المسارات الرئيسية للمنهج</h2>

    <div class="card">
      <div class="card-header">
        <h3 class="card-title">المرحلة 01: الاستراتيجية وبناء الهوية الملكية</h3>
        <span style="font-size: 0.8rem; color: var(--gold);">4 مقررات</span>
      </div>
      <p style="font-size: 0.9rem; color: var(--text-body); margin-bottom: 0.75rem;">
        مبادئ التسويق الحديث، نموذج التموضع STP، كراسة الهوية ونبرة الصوت The Ruler، وإجراءات العمل داخل CoreLink CRM.
      </p>
      <a href="courses.html" style="font-size: 0.85rem; color: var(--gold); text-decoration: none; font-weight: 600;">استعراض المرحلة ←</a>
    </div>

    <div class="card">
      <div class="card-header">
        <h3 class="card-title">المرحلة 02: الكرييتف، المحتوى الفيرال، وسيو محركات البحث</h3>
        <span style="font-size: 0.8rem; color: var(--gold);">4 مقررات</span>
      </div>
      <p style="font-size: 0.9rem; color: var(--text-body); margin-bottom: 0.75rem;">
        الكوبي رايتنج ونموذج PAS، سيكولوجية الفيديو القصير وريلز 3-Sec Hooks، سيو محركات البحث، وسيو يوتيوب.
      </p>
      <a href="courses.html" style="font-size: 0.85rem; color: var(--gold); text-decoration: none; font-weight: 600;">استعراض المرحلة ←</a>
    </div>

    <div class="card">
      <div class="card-header">
        <h3 class="card-title">المرحلة 03: ميديا بايينج الأداء وسكيلينج الـ ROAS</h3>
        <span style="font-size: 0.8rem; color: var(--gold);">5 مقررات</span>
      </div>
      <p style="font-size: 0.9rem; color: var(--text-body); margin-bottom: 0.75rem;">
        إعلانات Meta و Advantage+ وتتبع CAPI، إعلانات تيك توك، إعلانات سناب شات للخليج، لينكد إن B2B، ومنصة إكس.
      </p>
      <a href="courses.html" style="font-size: 0.85rem; color: var(--gold); text-decoration: none; font-weight: 600;">استعراض المرحلة ←</a>
    </div>

    <div class="card">
      <div class="card-header">
        <h3 class="card-title">المرحلة 04: الذكاء الاصطناعي، الجروث هاكينج، وعقود الريتينر</h3>
        <span style="font-size: 0.8rem; color: var(--gold);">6 مقررات</span>
      </div>
      <p style="font-size: 0.9rem; color: var(--text-body); margin-bottom: 0.75rem;">
        أوامر RCIC الذكية، أتمتة WhatsApp API، الإيميل ماركتنج، الجروث هاكينج، إغلاق عقود الريتينر ($2,500/شهر)، والتميز المهني.
      </p>
      <a href="courses.html" style="font-size: 0.85rem; color: var(--gold); text-decoration: none; font-weight: 600;">استعراض المرحلة ←</a>
    </div>

    <!-- CLIENTS SIMPLE BADGE -->
    <div style="text-align: center; margin-top: 3.5rem; padding-top: 2rem; border-top: 1px solid var(--border);">
      <div style="font-size: 0.8rem; color: var(--text-dim); margin-bottom: 0.75rem;">دراسات حالة معتمدة لعملاء OTB:</div>
      <div style="display: flex; justify-content: center; gap: 1.25rem; flex-wrap: wrap; font-size: 0.88rem; color: var(--text);">
        <span>MIX Coffee</span> · <span>Rancho's EG</span> · <span>Dr. Zaghloul Jewelry</span> · <span>Rice Patisserie</span> · <span>Sakr Store</span> · <span>Elag Labs</span>
      </div>
    </div>

  </main>
  {get_footer()}
</body>
</html>
"""

# ==============================================================================
# 2. MINDMAP.HTML (MINIMAL CLEAN TREE)
# ==============================================================================
p_mindmap = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🗺️ الخريطة الذهنية — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
    .phase-section {{
      margin-bottom: 2.5rem;
    }}
    .phase-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .item-row {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 1rem 1.25rem;
      margin-bottom: 0.6rem;
    }}
    .item-row h4 {{
      font-size: 0.95rem;
      color: var(--gold);
      margin-bottom: 0.35rem;
    }}
    .item-row p {{
      font-size: 0.86rem;
      color: var(--text-body);
      line-height: 1.6;
    }}
  </style>
</head>
<body>
  {get_nav("mindmap.html")}

  <main class="container">
    
    <div class="hero" style="margin-bottom: 2.5rem;">
      <span class="hero-tag">MIND MAP & BREAKDOWN</span>
      <h1 class="hero-title">الخريطة الذهنية للمنهج</h1>
      <p class="hero-desc">خريطة هيكلية مبسطة تقسم المنهج إلى 4 مراحل و 19 تخصصاً رئيسياً.</p>
    </div>

    <div class="phase-section">
      <div class="phase-title"><span>👑</span> المرحلة 01: الأساسات، الاستراتيجية، وبناء الهوية</div>
      <div class="item-row">
        <h4>1. مبادئ وأسس التسويق الحديث (Modern Marketing Principles)</h4>
        <p>الانتقال من 4Ps إلى 4Cs · سيكولوجية اتخاذ القرار · رحلة العميل وبناء الـ Persona</p>
      </div>
      <div class="item-row">
        <h4>2. الاستراتيجية والتخطيط التسويقي (Marketing Strategy & SOSTAC)</h4>
        <p>نموذج STP العملي · إطار التخطيط SOSTAC · مؤشرات الأداء الذكية (SMART KPIs)</p>
      </div>
      <div class="item-row">
        <h4>3. بناء الهوية والعلامة التجارية (Branding & Identity)</h4>
        <p>النمط النفسي The Ruler لـ OTB · كراسة معايير الهوية ونبرة الصوت · تموضع الهيبة والسعر</p>
      </div>
      <div class="item-row">
        <h4>4. الانضباط التشغيلي ونظام CoreLink CRM (SOPs)</h4>
        <p>نماذج البريف الإلزامي ومنع الهدر · قفل التبعيات التسلسلي · اتفاقيات مستوى الخدمة (SLA)</p>
      </div>
    </div>

    <div class="phase-section">
      <div class="phase-title"><span>✍️</span> المرحلة 02: الكرييتف، المحتوى الفيرال، وسيو محركات البحث</div>
      <div class="item-row">
        <h4>5. تسويق المحتوى والكوبي رايتنج (Content Marketing)</h4>
        <p>هندسة الهوك وأول 3 ثوانٍ · أطر الكتابة الإعلانية: PAS, AIDA, BAB · ركائز المحتوى الشهري</p>
      </div>
      <div class="item-row">
        <h4>6. احتراف إنستغرام والريلز (Instagram & Reels)</h4>
        <p>خوارزمية الريلز ومعدل الإكمال · تسلسل الستوري اليومي للبيع · أتمتة الرسائل الخاصة (IG DM)</p>
      </div>
      <div class="item-row">
        <h4>7. سيو محركات البحث الشامل (Search Engine Optimization)</h4>
        <p>البحث عن الكلمات المفتاحية التنافسية · السيو الداخلي والتقني · بناء الروابط وسيو نتائج الذكاء الاصطناعي</p>
      </div>
      <div class="item-row">
        <h4>8. يوتيوب وسيو الفيديو الطويل (YouTube Strategy)</h4>
        <p>سيكولوجية الصورة المصغرة (CTR > 10%) · هندسة وقت المشاهدة · استراتيجية YouTube Shorts</p>
      </div>
    </div>

    <div class="phase-section">
      <div class="phase-title"><span>📊</span> المرحلة 03: ميديا بايينج الأداء والسيطرة الإعلانية</div>
      <div class="item-row">
        <h4>9. إعلانات فيسبوك وميتا للأداء (Meta Performance Ads)</h4>
        <p>هيكل TOFU / MOFU / BOFU · تتبع السيرفر CAPI · قواعد السكيلينج الرأسي (+20% كل 48 ساعة)</p>
      </div>
      <div class="item-row">
        <h4>10. إعلانات ونمو تيك توك (TikTok Growth & Spark Ads)</h4>
        <p>صفحة FYP ومحتوى الـ UGC · إعلانات Spark Ads · سيو تيك توك وتتبع مبيعات المتاجر</p>
      </div>
      <div class="item-row">
        <h4>11. إعلانات سناب شات والخليج (Snapchat Ads & GCC)</h4>
        <p>استهداف السوق السعودي والخليجي · تصميم عدسات الواقع المعزز (AR) · إعلانات المجموعات للمتاجر</p>
      </div>
      <div class="item-row">
        <h4>12. لينكد إن واكتساب عملاء الشركات B2B (LinkedIn Mastery)</h4>
        <p>استقطاب صناع القرار عبر Sales Navigator · المحتوى القيادي · إعلانات استمارات الليدز</p>
      </div>
      <div class="item-row">
        <h4>13. منصة إكس والتموضع المؤسسي (Twitter / X Authority)</h4>
        <p>صناعة الثريدات الفيرال · ركوب الترندات الذكي · إدارة الأزمات وبناء الحضور الرسمي</p>
      </div>
    </div>

    <div class="phase-section">
      <div class="phase-title"><span>🤖</span> المرحلة 04: الذكاء الاصطناعي، الأتمتة، وعقود الريتينر</div>
      <div class="item-row">
        <h4>14. الذكاء الاصطناعي في التسويق (AI & RCIC Prompts)</h4>
        <p>إطار هندسة الأوامر RCIC · التصوير التجاري و 3D عبر Midjourney · أتمتة WhatsApp API</p>
      </div>
      <div class="item-row">
        <h4>15. الإيميل ماركتنج وتدفقات الأتمتة (Email Marketing)</h4>
        <p>تدفقات استعادة السلات المتروكة · سلاسل الترحيب المؤتمتة · رفع القيمة العمرية للعميل (LTV)</p>
      </div>
      <div class="item-row">
        <h4>16. الجروث هاكينج وقمع AARRR (Growth Hacking)</h4>
        <p>حلقات الانتشار الفيرال وبرامج الإحالة · مصفوفة أولويات التجارب ICE · تحسين معدلات التحويل</p>
      </div>
      <div class="item-row">
        <h4>17. التسويق بالعمولة والشراكات (Affiliate Marketing)</h4>
        <p>بناء شبكات المسوقين بالعمولة لبراندك · تصميم هياكل العمولات دون الإضرار بهامش الربح</p>
      </div>
      <div class="item-row">
        <h4>18. العمل الحر وإغلاق عقود الريتينر (Agency Retainers)</h4>
        <p>التسعير القائم على القيمة · باقة Dominance Retainer ($2,500/شهر) · إغلاق الصفقات والحفاظ على العملاء</p>
      </div>
      <div class="item-row">
        <h4>19. التميز المهني والمقابلات (Career & STAR Method)</h4>
        <p>السيرة الذاتية القائمة على الأرقام · الإجابة بنموذج STAR · التفاوض على الراتب والترقي المستمر</p>
      </div>
    </div>

  </main>
  {get_footer()}
</body>
</html>
"""

# ==============================================================================
# 3. COURSES.HTML (MINIMAL CLEAN ACCORDION / GRID)
# ==============================================================================
courses_json = json.dumps(COURSES_DATA, ensure_ascii=False)

p_courses = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📚 المقررات — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
    .course-item {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.25rem 1.5rem;
      margin-bottom: 1rem;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .course-item:hover {{
      border-color: var(--border-gold);
      background: var(--bg-card-hover);
    }}
    .course-item.active {{
      border-color: var(--gold);
    }}
    .course-details {{
      display: none;
      margin-top: 1.25rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--border);
    }}
    .course-item.active .course-details {{
      display: block;
    }}
  </style>
</head>
<body>
  {get_nav("courses.html")}

  <main class="container">
    
    <div class="hero" style="margin-bottom: 2rem;">
      <span class="hero-tag">19 COURSES CURRICULUM</span>
      <h1 class="hero-title">موسوعة المقررات الـ 19</h1>
      <p class="hero-desc">انقر على أي مقرر لاستعراض وحداته الدراسية، وأمر الـ AI المعتمد، ودراسة الحالة التطبيقية.</p>
    </div>

    <!-- TABS -->
    <div class="tabs">
      <button class="tab-btn active" onclick="filterCourses('all', this)">الكل (19)</button>
      <button class="tab-btn" onclick="filterCourses('strategy', this)">الاستراتيجية والهوية (4)</button>
      <button class="tab-btn" onclick="filterCourses('creative', this)">المحتوى والسيو (4)</button>
      <button class="tab-btn" onclick="filterCourses('media', this)">الميديا بايينج (5)</button>
      <button class="tab-btn" onclick="filterCourses('ai', this)">الذكاء الاصطناعي والأتمتة (4)</button>
      <button class="tab-btn" onclick="filterCourses('career', this)">عقود الوكالة والمهنة (2)</button>
    </div>

    <!-- COURSES LIST -->
    <div id="coursesList"></div>

  </main>
  {get_footer()}

  <script>
    const coursesData = {courses_json};

    function renderList(list) {{
      const container = document.getElementById("coursesList");
      let html = "";
      list.forEach(c => {{
        let unitsHtml = "";
        c.units.forEach((u, i) => {{
          unitsHtml += `<li style="margin-bottom: 0.35rem;"><b>الوحدة ${{i + 1}}:</b> ${{u}}</li>`;
        }});

        html += `
          <div class="course-item" onclick="toggleCourse(this)">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div>
                <span style="font-size: 0.8rem; color: var(--gold); font-weight: 600;">${{c.badge}}</span>
                <h3 style="font-size: 1.1rem; color: var(--text); margin-top: 0.2rem;">${{c.icon}} ${{c.title}}</h3>
              </div>
              <span style="font-size: 0.82rem; color: var(--text-dim);">${{c.pages}} صفحة ▾</span>
            </div>

            <div class="course-details" onclick="event.stopPropagation()">
              <p style="font-size: 0.9rem; color: var(--text-body); margin-bottom: 1rem;">${{c.desc}}</p>
              
              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.5rem;">📖 الوحدات التدريبية:</h4>
                <ul style="padding-right: 1.25rem; font-size: 0.88rem; color: var(--text-body); line-height: 1.7;">
                  ${{unitsHtml}}
                </ul>
              </div>

              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.4rem;">🤖 أمر الذكاء الاصطناعي (RCIC Prompt):</h4>
                <div class="code-box">${{c.prompt}}</div>
                <button class="btn btn-secondary" style="font-size: 0.82rem; padding: 0.4rem 0.9rem;" onclick="copyText(this.previousElementSibling.innerText)">📋 نسخ البرومبت</button>
              </div>

              <div style="margin-bottom: 1.25rem;">
                <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.3rem;">💼 دراسة الحالة التطبيقية:</h4>
                <p style="font-size: 0.88rem; color: var(--text-body); line-height: 1.6;">${{c.case_study}}</p>
              </div>

              <div>
                <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.3rem;">🧪 التكليف العملي:</h4>
                <p style="font-size: 0.88rem; color: var(--gold-light); line-height: 1.6;">${{c.lab}}</p>
              </div>
            </div>
          </div>
        `;
      }});
      container.innerHTML = html;
    }}

    function toggleCourse(el) {{
      const wasActive = el.classList.contains("active");
      document.querySelectorAll(".course-item").forEach(item => item.classList.remove("active"));
      if (!wasActive) el.classList.add("active");
    }}

    function filterCourses(cat, btn) {{
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      if (cat === "all") renderList(coursesData);
      else renderList(coursesData.filter(c => c.cat === cat));
    }}

    renderList(coursesData);
  </script>
</body>
</html>
"""

# ==============================================================================
# 4. SPRINT.HTML (MINIMAL SPRINT)
# ==============================================================================
p_sprint = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>⚡ المعسكر السريع — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_nav("sprint.html")}

  <main class="container">
    
    <div class="hero" style="margin-bottom: 2rem;">
      <span class="hero-tag">5-DAY FAST-TRACK SPRINT</span>
      <h1 class="hero-title">معسكر الـ 5 أيام السريع</h1>
      <p class="hero-desc">خلاصة سريعة ومضغوطة تركز على النماذج التكتيكية الفورية لفريق عمل الوكالة.</p>
    </div>

    <!-- DAY SELECTOR -->
    <div class="tabs">
      <button class="tab-btn active" onclick="loadDay(1, this)">اليوم 01: STP والتموضع</button>
      <button class="tab-btn" onclick="loadDay(2, this)">اليوم 02: الكرييتف وريلز</button>
      <button class="tab-btn" onclick="loadDay(3, this)">اليوم 03: ميديا بايينج ROAS</button>
      <button class="tab-btn" onclick="loadDay(4, this)">اليوم 04: AI وأتمتة الواتساب</button>
      <button class="tab-btn" onclick="loadDay(5, this)">اليوم 05: التشغيل والريتينر</button>
    </div>

    <!-- SPRINT VIEWER -->
    <div id="sprintView"></div>

  </main>
  {get_footer()}

  <script>
    const sprintData = [
      {{
        day: 1,
        title: "اليوم الأول: تحليل السوق والتموضع وبناء الهوية (STP & Positioning)",
        audience: "الاستراتيجيون ومدراء الحسابات",
        concepts: "• <b>Segmentation:</b> تقسيم الجمهور جغرافياً وسلوكياً في السوق المصري.<br>• <b>Targeting:</b> استهداف الشريحة الأعلى ربحية (LTV).<br>• <b>Positioning:</b> حفر مكانة ملكية في ذهن العميل تجعلك تصنع الاتجاهات ولا تتبعها.",
        caseStudy: "تحويل براند MIX Coffee من كافيه تقليدي إلى وجهة شبابية أولى بهوية داكنة فاخرة، مما رفع التفاعل بنسبة 180%.",
        prompt: "معادلة التموضع (Positioning Statement):\\n[Target Audience] + [Category] + [Differentiating Benefit] + [Reason to Believe]",
        lab: "اختيار عميل وتعبئة وثيقة البريف واستخراج 3 زوايا تسويقية تستغل فجوات المنافسين."
      }},
      {{
        day: 2,
        title: "اليوم الثاني: الكوبي رايتنج الإعلاني وسيكولوجية الفيديو القصير",
        audience: "صناع المحتوى والمصممون والمونتيرون",
        concepts: "• <b>قاعدة الـ 3 ثوانٍ (Hook Rate > 35%):</b> كسر التمرير بصرياً وصوتياً.<br>• <b>صيغة PAS:</b> توضيح المشكلة (Problem)، تهويل أثرها (Agitation)، ثم تقديم الحل الفوري (Solution).<br>• <b>صوتيات الـ ASMR:</b> رفع الإشباع البصري والصوتي في فيديوهات المنتجات.",
        caseStudy: "فيديو ريلز لـ Rancho's EG يبرز تفاصيل تقطيع البرجر الملحمي، محققاً 450 ألف مشاهدة ورفع مبيعات الواتساب بنسبة 65%.",
        prompt: "Problem: تعبت من ساندوتشات البرجر اللي كلها عيش؟\\nAgitation: بتدفع مبلغ وفي الآخر بيجيلك بارد وتندم.\\nSolution: في Rancho's قطمة واحدة من الـ Smoked Beef بالصوص السري هتعرف يعني إيه برجر ملوك!",
        lab: "كتابة 3 نصوص إعلانية بـ 3 زوايا مختلفة (فكاهية، FOMO، هيبة اجتماعية) واسكريبت فيديو 15 ثانية."
      }},
      {{
        day: 3,
        title: "اليوم الثالث: ميديا بايينج الأداء وسكيلينج الـ ROAS",
        audience: "الميديا بايرز وهندسة النمو",
        concepts: "• <b>Advantage+ & Broad Targeting:</b> الاستهداف المفتوح مع تغذية الخوارزمية بكرييتفز قوية.<br>• <b>Conversions API (CAPI):</b> ربط التتبع بالسيرفر لتجاوز قيود iOS 14.5+.<br>• <b>قاعدة الـ 20%:</b> رفع الميزانية 20% فقط كل 48-72 ساعة لحماية استقرار الحملة.",
        caseStudy: "إعادة هيكلة إعلانات Dr. Zaghloul Jewelry بحملات TOFU/MOFU/BOFU محققة ROAS تجاوز 7.5x.",
        prompt: "Break-Even ROAS = 1 / Gross Profit Margin %\\n(إذا كان الهامش 25%، التعادل = 4.0x)",
        lab: "تدقيق حساب إعلاني نشط، فحص جودة مطابقة CAPI، وإعداد مصفوفة الميزانية الأسبوعية."
      }},
      {{
        day: 4,
        title: "اليوم الرابع: الذكاء الاصطناعي وهندسة الأوامر وأتمتة الواتساب",
        audience: "جميع أعضاء الفريق",
        concepts: "• <b>إطار RCIC:</b> Role (الدور) + Context (السياق) + Instruction (التعليمات) + Constraints (القيود).<br>• <b>مسار WhatsApp Business API:</b> ترحيب فوري، تصنيف الطلب، إرسال الكتالوج، وتسجيل البيع تلقائياً.",
        caseStudy: "بناء بوت واتساب لمختبرات علاج (Elag Labs) يستقبل ويؤهل أكثر من 800 حجز منزلي شهرياً.",
        prompt: "Role: Senior Direct-Response Copywriter at OTB Agency.\\nContext: Client is [Brand] in Egypt. Target: 20-35.\\nTask: Write 3 ad copies using PAS framework in refined modern Egyptian Arabic.\\nConstraints: Bold tone, high-urgency CTA for WhatsApp ordering.",
        lab: "توليد 5 إعلانات وبرودكت شوت 3D لعميل حقيقي عبر الـ AI، ورسم مخطط لمسار ردود الواتساب."
      }},
      {{
        day: 5,
        title: "اليوم الخامس: الانضباط التشغيلي وعقود الريتينر الشهرية",
        audience: "الإدارة ومدراء الحسابات",
        concepts: "• <b>منع الهدر التشغيلي:</b> لا مهمة بدون بريف إلزامي، وقفل التبعيات (Sequential Locking).<br>• <b>اتفاقية مستوى الخدمة (SLA):</b> مراجعة خلال 24 ساعة والتصعيد بعد 48 ساعة.<br>• <b>باقة Dominance Retainer ($2,500/شهر):</b> هوية كاملة + 24 محتوى + ميديا بايينج + أتمتة.",
        caseStudy: "إغلاق عقود ريتينر طويلة الأجل مع عملاء OTB بالاعتماد على إثبات العائد المالي بدلاً من عدد البوستات.",
        prompt: "نحن في OTB لا نبيع مجرد بوستات وتصاميم، بل نبني لك محرك نمو متكامل يربط الهوية بالإعلانات الممولة لتحقيق أعلى عائد مالي مضمون.",
        lab: "تقديم مقترح خطة نمو شهرية مصغرة لعميل حقيقي تتضمن الاستراتيجية وعينة المحتوى ومسار الأتمتة."
      }}
    ];

    function loadDay(dayNum, btn) {{
      if (btn) {{
        document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
      }}
      const d = sprintData.find(item => item.day === dayNum);
      const container = document.getElementById("sprintView");

      container.innerHTML = `
        <div class="card">
          <div style="font-size: 0.8rem; color: var(--gold); font-weight: 600; margin-bottom: 0.3rem;">المستهدفون: ${{d.audience}}</div>
          <h2 style="font-size: 1.35rem; color: var(--text); margin-bottom: 1.25rem;">${{d.title}}</h2>

          <div style="margin-bottom: 1.5rem;">
            <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.4rem;">📖 المفاهيم والنماذج الأساسية:</h4>
            <p style="font-size: 0.9rem; color: var(--text-body); line-height: 1.8;">${{d.concepts}}</p>
          </div>

          <div style="margin-bottom: 1.5rem;">
            <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.4rem;">💼 دراسة الحالة التطبيقية:</h4>
            <p style="font-size: 0.9rem; color: var(--text-body); line-height: 1.6;">${{d.caseStudy}}</p>
          </div>

          <div style="margin-bottom: 1.5rem;">
            <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.4rem;">📐 القالب / المعادلة:</h4>
            <div class="code-box">${{d.prompt}}</div>
          </div>

          <div>
            <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.4rem;">🧪 التكليف العملي لليوم:</h4>
            <p style="font-size: 0.9rem; color: var(--gold-light); line-height: 1.6;"><b>المطلوب تسليمه:</b> ${{d.lab}}</p>
          </div>
        </div>
      `;
    }}

    loadDay(1);
  </script>
</body>
</html>
"""

# ==============================================================================
# 5. PROMPTS.HTML (MINIMAL AI PROMPTS STUDIO)
# ==============================================================================
p_prompts = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🤖 استوديو الأوامر — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_nav("prompts.html")}

  <main class="container">
    
    <div class="hero" style="margin-bottom: 2rem;">
      <span class="hero-tag">AI RCIC PROMPT ENGINE</span>
      <h1 class="hero-title">استوديو أوامر الذكاء الاصطناعي</h1>
      <p class="hero-desc">اختر المهمة التسويقية ليتم توليد الأمر فورياً بصيغة RCIC المعتمدة جاهزاً للنسخ.</p>
    </div>

    <div class="card" style="margin-bottom: 2.5rem;">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.25rem;">
        <div>
          <label style="display: block; font-size: 0.85rem; color: var(--text); margin-bottom: 0.4rem; font-weight: 600;">اختر التكليف:</label>
          <select id="promptTask" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input);" onchange="updatePrompt()">
            <option value="copy">كتابة إعلانات تحويلية (PAS Framework)</option>
            <option value="reels">اسكريبت فيديو قصير 15 ثانية (Viral Hook)</option>
            <option value="media">تشخيص حساب إعلاني وسكيلينج (Media Buying)</option>
            <option value="design">لقطات برودكت شوت 3D لـ Midjourney</option>
            <option value="retainer">مقترح عقد ريتينر شهري ($2,500/mo)</option>
          </select>
        </div>
        <div>
          <label style="display: block; font-size: 0.85rem; color: var(--text); margin-bottom: 0.4rem; font-weight: 600;">اسم البراند والقطاع:</label>
          <input type="text" id="promptBrand" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input);" value="MIX Coffee (Specialty Coffee)" oninput="updatePrompt()">
        </div>
      </div>

      <div style="margin-bottom: 1rem;">
        <label style="display: block; font-size: 0.85rem; color: var(--text); margin-bottom: 0.4rem; font-weight: 600;">الأمر المولد فورياً:</label>
        <div id="promptOutput" class="code-box" style="max-height: 250px; overflow-y: auto;"></div>
      </div>

      <button class="btn btn-primary" onclick="copyText(document.getElementById('promptOutput').innerText)">📋 نسخ الأمر للحافظة</button>
    </div>

    <!-- PRE-MADE PROMPTS -->
    <h3 style="font-size: 1.15rem; color: var(--text); margin-bottom: 1rem; font-weight: 700;">أوامر معتمدة سريعة</h3>

    <div class="card">
      <div class="card-header">
        <h4 class="card-title">كتابة 3 إعلانات PAS سريعة</h4>
        <span style="font-size: 0.8rem; color: var(--gold);">Copywriting</span>
      </div>
      <div class="code-box">Role: Direct-Response Copywriter at OTB Agency.
Context: Client is [Brand Name] in Egypt. Target: 18-35.
Task: Write 3 ad variations using PAS (Problem-Agitation-Solution) in modern Egyptian Arabic.
Constraints: Bold tone, no clichés, high-urgency CTA for WhatsApp ordering.</div>
      <button class="btn btn-secondary" style="font-size: 0.82rem; padding: 0.4rem 0.9rem;" onclick="copyText(this.previousElementSibling.innerText)">📋 نسخ</button>
    </div>

    <div class="card">
      <div class="card-header">
        <h4 class="card-title">برومبت تصوير تجاري 3D لـ Midjourney</h4>
        <span style="font-size: 0.8rem; color: var(--gold);">3D Design</span>
      </div>
      <div class="code-box">/imagine prompt: Ultra-realistic 3D commercial product photography of [Product Name], obsidian noir stone podium, royal gold accents and droplets, dramatic rim lighting, cinematic 8k studio render --ar 9:16 --style raw --v 6.0</div>
      <button class="btn btn-secondary" style="font-size: 0.82rem; padding: 0.4rem 0.9rem;" onclick="copyText(this.previousElementSibling.innerText)">📋 نسخ</button>
    </div>

  </main>
  {get_footer()}

  <script>
    function updatePrompt() {{
      const task = document.getElementById("promptTask").value;
      const brand = document.getElementById("promptBrand").value || "البراند";
      const out = document.getElementById("promptOutput");

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

    updatePrompt();
  </script>
</body>
</html>
"""

# ==============================================================================
# 6. QUIZ.HTML (MINIMAL CERTIFICATE & QUIZ)
# ==============================================================================
p_quiz = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📝 الشهادة والاختبار — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;500;600;700&family=Cinzel:wght@700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
    .cert-frame {{
      background: #060709;
      border: 3px solid var(--gold);
      border-radius: 16px;
      padding: 3rem 2rem;
      text-align: center;
      margin-top: 2rem;
      box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    }}
  </style>
</head>
<body>
  {get_nav("quiz.html")}

  <main class="container" style="max-width: 800px;">
    
    <div class="hero" style="margin-bottom: 2rem;">
      <span class="hero-tag">ASSESSMENT & CERTIFICATION</span>
      <h1 class="hero-title">شهادة إتمام الأكاديمية</h1>
      <p class="hero-desc">أدخل اسمك وأجب عن الأسئلة الخمسة الأساسية لإصدار شهادتك الرسمية المعتمدة.</p>
    </div>

    <div class="card" style="margin-bottom: 1.5rem;">
      <label style="display: block; font-size: 0.88rem; color: var(--text); margin-bottom: 0.4rem; font-weight: 600;">الاسم الرسمي على الشهادة:</label>
      <input type="text" id="certName" class="btn btn-secondary" style="width: 100%; text-align: right; background: var(--bg-input); font-size: 1rem;" value="أحمد عصام رمضان">
    </div>

    <div id="questionsWrap">
      <div class="card">
        <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.75rem;">1. ما هو التموضع والنمط النفسي المعتمد لوكالة OTB؟</h4>
        <label style="display:block; margin-bottom:0.4rem; font-size:0.88rem;"><input type="radio" name="q0" value="0"> المنافسة على أقل سعر</label>
        <label style="display:block; font-size:0.88rem;"><input type="radio" name="q0" value="1" checked> The Ruler & The Creator (ملوك المدينة: الهيبة والجرأة والتركيز على العائد)</label>
      </div>

      <div class="card">
        <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.75rem;">2. ما هو الهدف الأساسي من أول 3 ثوانٍ في ريلز الإعلانات؟</h4>
        <label style="display:block; margin-bottom:0.4rem; font-size:0.88rem;"><input type="radio" name="q1" value="1" checked> كسر التمرير (Pattern Interrupt) وجذب انتباه المشاهد (Hook Rate > 35%)</label>
        <label style="display:block; font-size:0.88rem;"><input type="radio" name="q1" value="0"> كتابة أرقام السجل التجاري</label>
      </div>

      <div class="card">
        <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.75rem;">3. إذا كان هامش الربح 25%، فما هو الـ Break-Even ROAS؟</h4>
        <label style="display:block; margin-bottom:0.4rem; font-size:0.88rem;"><input type="radio" name="q2" value="1" checked> 4.0x (حيث 1 / 0.25 = 4)</label>
        <label style="display:block; font-size:0.88rem;"><input type="radio" name="q2" value="0"> 1.5x</label>
      </div>

      <div class="card">
        <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.75rem;">4. ما هي النسبة الآمنة لزيادة ميزانية الحملات الرابحة (Scaling)؟</h4>
        <label style="display:block; margin-bottom:0.4rem; font-size:0.88rem;"><input type="radio" name="q3" value="1" checked> زيادة 20% كل 48-72 ساعة لحماية استقرار الحملة</label>
        <label style="display:block; font-size:0.88rem;"><input type="radio" name="q3" value="0"> مضاعفة الميزانية 200% كل ساعة</label>
      </div>

      <div class="card">
        <h4 style="font-size: 0.95rem; color: var(--text); margin-bottom: 0.75rem;">5. ما هو السعر القياسي لباقة الـ Dominance Retainer لـ OTB؟</h4>
        <label style="display:block; margin-bottom:0.4rem; font-size:0.88rem;"><input type="radio" name="q4" value="1" checked> $2,500 / شهر (هوية + 24 محتوى + ميديا بايينج + أتمتة)</label>
        <label style="display:block; font-size:0.88rem;"><input type="radio" name="q4" value="0"> $300 / شهر</label>
      </div>
    </div>

    <div style="text-align: center; margin: 2rem 0;">
      <button class="btn btn-primary" style="padding: 0.8rem 2.5rem; font-size: 1rem;" onclick="generateCert()">👑 إصدار شهادة الاعتماد</button>
    </div>

    <div id="certResult" style="display: none;"></div>

  </main>
  {get_footer()}

  <script>
    function generateCert() {{
      const name = document.getElementById("certName").value || "خريج الأكاديمية";
      const certId = "OTB-" + Math.floor(100000 + Math.random() * 900000);
      const date = new Date().toLocaleDateString('ar-EG', {{ year: 'numeric', month: 'long', day: 'numeric' }});
      const wrap = document.getElementById("certResult");

      wrap.style.display = "block";
      wrap.innerHTML = `
        <div class="cert-frame">
          <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">👑</div>
          <div style="font-size: 0.8rem; letter-spacing: 2px; color: var(--gold); text-transform: uppercase;">OTB Marketing Studio · City Kings</div>
          <div style="font-family: 'Cinzel', serif; font-size: 1.8rem; color: var(--text); margin: 0.75rem 0; font-weight: 700;">CERTIFICATE OF GROWTH MASTERY</div>
          <p style="color: var(--text-dim); font-size: 0.95rem;">تشهد أكاديمية وكالة OTB للتسويق وهندسة النمو بأن</p>
          <h2 style="font-size: 2rem; color: var(--gold); margin: 0.85rem 0; font-weight: 800;">${{name}}</h2>
          <p style="color: var(--text-body); max-width: 540px; margin: 0 auto 2rem auto; font-size: 0.92rem; line-height: 1.7;">
            قد أتم بنجاح متطلبات أكاديمية <b>النمو والتسويق الرقمي والذكاء الاصطناعي (Full-Stack Growth Engineering)</b> وأصبح مؤهلاً لتطبيق استراتيجيات وإعلانات ملوك المدينة.
          </p>
          <div style="display: flex; justify-content: space-around; border-top: 1px solid var(--border); padding-top: 1.5rem; font-size: 0.85rem;">
            <div>
              <div style="color: var(--text-dim); font-size: 0.75rem;">رقم الاعتماد</div>
              <div style="font-family: 'JetBrains Mono'; color: var(--gold); font-weight: 600;">${{certId}}</div>
            </div>
            <div>
              <div style="color: var(--text-dim); font-size: 0.75rem;">تاريخ المنح</div>
              <div style="color: var(--text);">${{date}}</div>
            </div>
            <div>
              <div style="color: var(--text-dim); font-size: 0.75rem;">الاعتماد الرسمي</div>
              <div style="color: var(--gold); font-weight: 700;">OTB Agency 👑</div>
            </div>
          </div>
        </div>
        <div style="text-align: center; margin-top: 1.5rem;">
          <button class="btn btn-secondary" onclick="window.print()">🖨️ طباعة الشهادة / حفظ PDF</button>
        </div>
      `;
      wrap.scrollIntoView({{ behavior: "smooth" }});
      showToast("👑 تم إصدار الشهادة بنجاح!");
    }}
  </script>
</body>
</html>
"""

# ==============================================================================
# 7. DOWNLOADS.HTML (MINIMAL DOWNLOADS)
# ==============================================================================
p_downloads = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📥 الموارد والتحميلات — OTB Growth Academy</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Readex+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_nav("downloads.html")}

  <main class="container">
    
    <div class="hero" style="margin-bottom: 2rem;">
      <span class="hero-tag">RESOURCES & STUDIO ASSETS</span>
      <h1 class="hero-title">الموارد وملفات التحميل</h1>
      <p class="hero-desc">تحميل الملفات الصوتية، الأدلة التكتيكية، ومستندات التوجيه الاستراتيجي بصيغ مباشرة.</p>
    </div>

    <div class="card">
      <div class="card-header">
        <h3 class="card-title">🎙️ البودكاست التدريبي الاستراتيجي (MP4)</h3>
        <span style="font-size: 0.8rem; color: var(--gold);">34 MB</span>
      </div>
      <p style="font-size: 0.88rem; color: var(--text-body); margin-bottom: 1rem;">حلقة صوتية معمقة تم إنتاجها عبر Gemini Studio تناقش منظومة وهندسة نمو وكالة OTB.</p>
      <a href="track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" download class="btn btn-primary" style="font-size: 0.85rem; padding: 0.45rem 1rem;">📥 تحميل ملف الصوت</a>
    </div>

    <div class="card">
      <div class="card-header">
        <h3 class="card-title">📑 التقرير الاستراتيجي الشامل (Markdown)</h3>
        <span style="font-size: 0.8rem; color: var(--gold);">Doc</span>
      </div>
      <p style="font-size: 0.88rem; color: var(--text-body); margin-bottom: 1rem;">وثيقة التوجيه الاستراتيجي الصادرة من استوديو Gemini تلخص الهيكل التنظيمي ومؤشرات الأداء.</p>
      <a href="track_b_4week_masterclass/studio_artifacts/OTB_Executive_Strategic_Briefing.md" download class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 1rem;">📥 تحميل التقرير</a>
    </div>

    <div class="card">
      <div class="card-header">
        <h3 class="card-title">📖 موسوعة الأوامر التكتيكية (Prompt Bible)</h3>
        <span style="font-size: 0.8rem; color: var(--gold);">50+ Prompts</span>
      </div>
      <p style="font-size: 0.88rem; color: var(--text-body); margin-bottom: 1rem;">موسوعة الأوامر الذكية המعتمدة لأقسام الوكالة الـ 16 دوراً وظيفياً.</p>
      <a href="track_a_fast_track_sprint/cheatsheets/OTB_Prompt_Engineering_Bible.md" download class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 1rem;">📥 تحميل الموسوعة</a>
    </div>

    <div class="card">
      <div class="card-header">
        <h3 class="card-title">✈️ دليل تدقيق الإعلانات الممولة (Checklist)</h3>
        <span style="font-size: 0.8rem; color: var(--gold);">Checklist</span>
      </div>
      <p style="font-size: 0.88rem; color: var(--text-body); margin-bottom: 1rem;">قائمة الفحص الفني قبل إطلاق الحملات وقواعد السكيلينج الرأسي والأفقي.</p>
      <a href="track_a_fast_track_sprint/cheatsheets/OTB_Media_Buying_Checklist.md" download class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 1rem;">📥 تحميل الدليل</a>
    </div>

  </main>
  {get_footer()}
</body>
</html>
"""

# WRITE MINIMAL PAGES
pages = {
    "index.html": p_index,
    "mindmap.html": p_mindmap,
    "courses.html": p_courses,
    "sprint.html": p_sprint,
    "prompts.html": p_prompts,
    "quiz.html": p_quiz,
    "downloads.html": p_downloads
}

for fname, content in pages.items():
    with open(os.path.join(BASE_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated minimal {fname}")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized all minimal files to Downloads!")
