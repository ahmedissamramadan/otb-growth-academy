import os
import shutil

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

from build_entire_enterprise_system import get_header, get_footer

# Update index.html hero and quick cards to include Mindmap and 19 Courses
p_index = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Growth Academy — The City Kings Enterprise Portal</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {get_header("index.html")}

  <main class="container">
    
    <!-- HERO SECTION -->
    <div class="page-header" style="text-align: center; padding: 2rem 0 3rem 0;">
      <span class="page-pill">👑 OFFICIAL INTERNAL ACADEMY & GROWTH ENGINE · 2026</span>
      <h1 class="page-title">أكاديمية OTB للتسويق: <span>موسوعة ملوك المدينة وهندسة النمو</span></h1>
      <p class="page-subtitle" style="margin: 0.85rem auto 2rem auto;">
        المنظومة التدريبية والتنفيذية الشاملة المستخلصة من 2,400+ صفحة لتمكين فرق وكالة OTB الـ 16 دوراً وظيفياً عبر 19 مساراً تخصصياً، وأكثر من 50 أمر ذكاء اصطناعي، ودراسات حالة واقعية معتمدة.
      </p>
      <div style="display: flex; justify-content: center; gap: 1.25rem; flex-wrap: wrap;">
        <a href="mindmap.html" class="btn-primary">🗺️ استعراض الخريطة الذهنية الشاملة</a>
        <a href="courses.html" class="btn-primary">📚 موسوعة المقررات الـ 19 المفصلة</a>
        <a href="sprint.html" class="btn-secondary">⚡ معسكر الـ 5 أيام السريع</a>
        <a href="prompts.html" class="btn-secondary">🤖 استوديو أوامر الـ AI</a>
      </div>
    </div>

    <!-- CLIENTS MARQUEE BADGES -->
    <div style="background: rgba(14, 20, 33, 0.6); border: 1px solid var(--gold-border); border-radius: var(--radius-md); padding: 1.25rem 2rem; margin-bottom: 3.5rem; text-align: center;">
      <div style="font-size: 0.78rem; font-weight: 800; color: var(--gold-400); letter-spacing: 1px; margin-bottom: 0.75rem; text-transform: uppercase;">
        👑 موثق بدراسات حالة وحملات حقيقية لعملاء OTB المعتمدين:
      </div>
      <div style="display: flex; justify-content: center; align-items: center; gap: 2rem; flex-wrap: wrap; font-weight: 700; font-size: 0.95rem; color: #FFF;">
        <span>☕ MIX Coffee</span>
        <span style="color: var(--gold-500);">•</span>
        <span>🍔 Rancho's EG</span>
        <span style="color: var(--gold-500);">•</span>
        <span>💍 Dr. Zaghloul Jewelry</span>
        <span style="color: var(--gold-500);">•</span>
        <span>🍰 Rice Patisserie</span>
        <span style="color: var(--gold-500);">•</span>
        <span>📦 Sakr Store</span>
        <span style="color: var(--gold-500);">•</span>
        <span>🧪 Elag Labs</span>
        <span style="color: var(--gold-500);">•</span>
        <span>🌯 Wilson Crepe</span>
      </div>
    </div>

    <!-- STATS METRICS GRID -->
    <div class="grid-4" style="margin-bottom: 3.5rem;">
      <div class="card" style="text-align: center;">
        <div style="font-size: 2.3rem; font-weight: 900; color: var(--gold-500); font-family: 'JetBrains Mono';">19 Courses</div>
        <div style="font-size: 1rem; font-weight: 800; margin-top: 0.25rem;">مقرراً تدريبياً مفصلاً</div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">مستخلصة من 2,400+ صفحة منهج</div>
      </div>
      <div class="card" style="text-align: center;">
        <div style="font-size: 2.3rem; font-weight: 900; color: var(--cyan); font-family: 'JetBrains Mono';">80+ Sub-Skills</div>
        <div style="font-size: 1rem; font-weight: 800; margin-top: 0.25rem;">مهارة تكتيكية في الخريطة</div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">تغطي كامل قمع الـ Full-Funnel</div>
      </div>
      <div class="card" style="text-align: center;">
        <div style="font-size: 2.3rem; font-weight: 900; color: var(--emerald); font-family: 'JetBrains Mono';">50+ Prompts</div>
        <div style="font-size: 1rem; font-weight: 800; margin-top: 0.25rem;">أمر ذكاء اصطناعي RCIC</div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">مجهزة ومخصصة لأدوار OTB الـ 16</div>
      </div>
      <div class="card" style="text-align: center;">
        <div style="font-size: 2.3rem; font-weight: 900; color: var(--crimson); font-family: 'JetBrains Mono';">7+ Years</div>
        <div style="font-size: 1rem; font-weight: 800; margin-top: 0.25rem;">خبرة سوق حقيقية</div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">سجل حافل في مضاعفة مبيعات البراندات</div>
      </div>
    </div>

    <!-- QUICK LAUNCHPAD SECTIONS -->
    <h2 style="font-size: 1.5rem; font-weight: 900; color: var(--gold-100); margin-bottom: 1.75rem; border-right: 4px solid var(--gold-500); padding-right: 0.85rem;">
      🚀 بوابات التدريب والتنفيذ السريع
    </h2>
    <div class="grid-3">
      <a href="mindmap.html" class="card" style="text-decoration: none; color: inherit; border-color: var(--gold-500);">
        <span class="page-pill">الخريطة الشاملة</span>
        <h3 class="card-title">🗺️ الخريطة الذهنية والتفكيك الهيكلي</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7;">
          خريطة مفاهيمية متكاملة تفكك المقررات الـ 19 في 4 مراحل نمو رئيسية و 80+ تخصصاً فرعياً لأقسام الوكالة.
        </p>
        <div style="margin-top: 1.25rem; color: var(--gold-400); font-weight: 800; font-size: 0.88rem;">استعراض الخريطة الذهنية ←</div>
      </a>

      <a href="courses.html" class="card" style="text-decoration: none; color: inherit; border-color: var(--gold-500);">
        <span class="page-pill">الموسوعة الكاملة</span>
        <h3 class="card-title">📚 موسوعة المقررات الـ 19</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7;">
          مستعرض المناهج الكاملة لجميع المقررات (AI, SEO, Copywriting, Ads, Strategy, Branding) مع الأوامر والتكليفات.
        </p>
        <div style="margin-top: 1.25rem; color: var(--gold-400); font-weight: 800; font-size: 0.88rem;">فتح المقررات الـ 19 ←</div>
      </a>

      <a href="sprint.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="page-pill">المسار المكثف</span>
        <h3 class="card-title">⚡ معسكر الـ 5 أيام السريع (Sprint)</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7;">
          الكبسولة التدريبية اليومية المركزة لفريق العمل: STP، الكوبي رايتنج، ميديا بايينج ميتا، أتمتة الواتساب، وعقود الريتينر.
        </p>
        <div style="margin-top: 1.25rem; color: var(--gold-400); font-weight: 800; font-size: 0.88rem;">استعراض أيام المعسكر ←</div>
      </a>

      <a href="masterclass.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="page-pill">الأكاديمية الأكاديمية</span>
        <h3 class="card-title">🎓 الأكاديمية الشاملة والـ Capstone</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7;">
          المنهج الأكاديمي لـ 16 وحدة تخصصية تغطي الـ SEO، الإعلانات الممولة، الجروث هاكينج، ومشروع التخرج الشامل 360°.
        </p>
        <div style="margin-top: 1.25rem; color: var(--gold-400); font-weight: 800; font-size: 0.88rem;">استعراض المنهج الأكاديمي ←</div>
      </a>

      <a href="prompts.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="page-pill">استوديو AI</span>
        <h3 class="card-title">🤖 استوديو أوامر الذكاء الاصطناعي</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7;">
          مولد أوامر تفاعلي حي لصناع المحتوى، الميديا بايرز، والمصممين لتوليد الاسكريبتات والإعلانات والتصاميم بضغطة زر.
        </p>
        <div style="margin-top: 1.25rem; color: var(--gold-400); font-weight: 800; font-size: 0.88rem;">فتح محاكي الأوامر ←</div>
      </a>

      <a href="quiz.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="page-pill">التقييم والاعتماد</span>
        <h3 class="card-title">📝 محاكي الاختبارات والشهادة</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7;">
          اختبر معلوماتك التسويقية في 10 أسئلة تخصصية واحصل فوراً على شهادة إتمام معتمدة من أكاديمية OTB باسمك ورقم اعتماد رسمي.
        </p>
        <div style="margin-top: 1.25rem; color: var(--gold-400); font-weight: 800; font-size: 0.88rem;">بدء الاختبار الآن ←</div>
      </a>
    </div>

  </main>
  {get_footer()}
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(p_index)

print("Updated index.html with 10-page master architecture!")
