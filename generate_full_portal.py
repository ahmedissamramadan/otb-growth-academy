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
# 1. INDEX.HTML (DASHBOARD)
# ==============================================================================
p_index = f"""<!DOCTYPE html>
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
  {get_header("index.html")}

  <main class="container">
    
    <!-- HERO SECTION -->
    <div class="page-header" style="text-align: center; padding: 2rem 0 3rem 0;">
      <span class="page-pill">👑 OFFICIAL INTERNAL GROWTH ENGINE · 2026</span>
      <h1 class="page-title">أكاديمية OTB للتسويق: <span>ماستركلاس ملوك المدينة وهندسة النمو</span></h1>
      <p class="page-subtitle" style="margin: 0.85rem auto 2rem auto;">
        المنظومة التدريبية والتنفيذية الداخلية الموحدة لتمكين فرق عمل وكالة OTB الـ 16 دوراً وظيفياً بأحدث تقنيات التسويق الرقمي، إعلانات الأداء (Performance Ads)، وأتمتة الذكاء الاصطناعي وهندسة الأوامر.
      </p>
      <div style="display: flex; justify-content: center; gap: 1.25rem; flex-wrap: wrap;">
        <a href="sprint.html" class="btn-primary">⚡ بدء معسكر الـ 5 أيام السريع</a>
        <a href="prompts.html" class="btn-secondary">🤖 استوديو أوامر الذكاء الاصطناعي</a>
        <a href="quiz.html" class="btn-secondary">📝 اختبار الكفاءة وإصدار الشهادة</a>
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
        <div style="font-size: 2.3rem; font-weight: 900; color: var(--gold-500); font-family: 'JetBrains Mono';">16 Modules</div>
        <div style="font-size: 1rem; font-weight: 800; margin-top: 0.25rem;">وحدة تخصصية شاملة</div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">تغطي كامل مسار النمو والـ ROAS</div>
      </div>
      <div class="card" style="text-align: center;">
        <div style="font-size: 2.3rem; font-weight: 900; color: var(--emerald); font-family: 'JetBrains Mono';">5 Days</div>
        <div style="font-size: 1rem; font-weight: 800; margin-top: 0.25rem;">معسكر مكثف ومضغوط</div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">ورش عمل وتكليفات يومية لكل قسم</div>
      </div>
      <div class="card" style="text-align: center;">
        <div style="font-size: 2.3rem; font-weight: 900; color: var(--cyan); font-family: 'JetBrains Mono';">50+ Prompts</div>
        <div style="font-size: 1rem; font-weight: 800; margin-top: 0.25rem;">أمر ذكاء اصطناعي RCIC</div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">مجهزة ومخصصة لأدوار OTB الـ 16</div>
      </div>
      <div class="card" style="text-align: center;">
        <div style="font-size: 2.3rem; font-weight: 900; color: var(--crimson); font-family: 'JetBrains Mono';">7+ Years</div>
        <div style="font-size: 1rem; font-weight: 800; margin-top: 0.25rem;">خبرة سوق حقيقية</div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">سجل حافل في مضاعفة مبيعات البراندات</div>
      </div>
    </div>

    <!-- 4-PHASE ROADMAP PREVIEW -->
    <div class="card" style="margin-bottom: 3.5rem; border: 2px solid var(--gold-border);">
      <h2 style="color: var(--gold-100); font-size: 1.4rem; font-weight: 900; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.6rem;">
        <span>🗺️ خارطة الطريق المعمارية للأكاديمية (The 4-Phase Growth Engine)</span>
      </h2>
      <div class="grid-4">
        <div class="lesson-box" style="margin: 0; border-right-color: var(--gold-500);">
          <span class="page-pill" style="font-size: 0.7rem; padding: 0.15rem 0.6rem;">المرحلة 01</span>
          <h4 style="color: var(--gold-200); font-size: 1.05rem; margin: 0.4rem 0;">التموضع والبراندنج</h4>
          <p style="font-size: 0.84rem; color: var(--text-muted);">تحليل STP، شخصية العميل (Persona)، ونمط The Ruler & Creator.</p>
        </div>
        <div class="lesson-box" style="margin: 0; border-right-color: var(--cyan);">
          <span class="page-pill" style="font-size: 0.7rem; padding: 0.15rem 0.6rem; color: var(--cyan); border-color: var(--cyan);">المرحلة 02</span>
          <h4 style="color: var(--gold-200); font-size: 1.05rem; margin: 0.4rem 0;">الكرييتف والسيو الفيرال</h4>
          <p style="font-size: 0.84rem; color: var(--text-muted);">صيغ PAS/AIDA، سيكولوجية الفيديو القصير وريلز 3-Sec Hooks.</p>
        </div>
        <div class="lesson-box" style="margin: 0; border-right-color: var(--emerald);">
          <span class="page-pill" style="font-size: 0.7rem; padding: 0.15rem 0.6rem; color: var(--emerald); border-color: var(--emerald);">المرحلة 03</span>
          <h4 style="color: var(--gold-200); font-size: 1.05rem; margin: 0.4rem 0;">الميديا بايينج وسكيلينج ROAS</h4>
          <p style="font-size: 0.84rem; color: var(--text-muted);">إعلانات Meta/TikTok، تتبع CAPI، والسكيلينج الرأسي والأفقي.</p>
        </div>
        <div class="lesson-box" style="margin: 0; border-right-color: var(--purple);">
          <span class="page-pill" style="font-size: 0.7rem; padding: 0.15rem 0.6rem; color: var(--purple); border-color: var(--purple);">المرحلة 04</span>
          <h4 style="color: var(--gold-200); font-size: 1.05rem; margin: 0.4rem 0;">الذكاء الاصطناعي والـ Capstone</h4>
          <p style="font-size: 0.84rem; color: var(--text-muted);">أتمتة WhatsApp API، ضبط CoreLink CRM، ومشروع التخرج 360°.</p>
        </div>
      </div>
    </div>

    <!-- QUICK LAUNCHPAD SECTIONS -->
    <h2 style="font-size: 1.5rem; font-weight: 900; color: var(--gold-100); margin-bottom: 1.75rem; border-right: 4px solid var(--gold-500); padding-right: 0.85rem;">
      🚀 بوابات التدريب والتنفيذ السريع
    </h2>
    <div class="grid-3">
      <a href="sprint.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="page-pill">المسار (أ)</span>
        <h3 class="card-title">⚡ معسكر الـ 5 أيام السريع (Sprint)</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7;">
          الكبسولة التدريبية اليومية المركزة لفريق العمل: STP، الكوبي رايتنج، ميديا بايينج ميتا، أتمتة الواتساب، وعقود الريتينر.
        </p>
        <div style="margin-top: 1.25rem; color: var(--gold-400); font-weight: 800; font-size: 0.88rem;">استعراض أيام المعسكر ←</div>
      </a>

      <a href="masterclass.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="page-pill">المسار (ب)</span>
        <h3 class="card-title">📚 الأكاديمية الشاملة (4 أسابيع)</h3>
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

      <a href="case-studies.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="page-pill">قاعدة المعرفة</span>
        <h3 class="card-title">💼 دراسات حالة عملاء OTB</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7;">
          تحليل استراتيجي لعملاء الوكالة الموثقين (MIX Coffee, Rancho's EG, Dr. Zaghloul, Rice Patisserie) وشرح النماذج التكتيكية.
        </p>
        <div style="margin-top: 1.25rem; color: var(--gold-400); font-weight: 800; font-size: 0.88rem;">قراءة دراسات الحالة ←</div>
      </a>

      <a href="quiz.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="page-pill">التقييم والاعتماد</span>
        <h3 class="card-title">📝 محاكي الاختبارات والشهادة</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7;">
          اختبر معلوماتك التسويقية في 10 أسئلة تخصصية واحصل فوراً على شهادة إتمام معتمدة من أكاديمية OTB باسمك ورقم اعتماد رسمي.
        </p>
        <div style="margin-top: 1.25rem; color: var(--gold-400); font-weight: 800; font-size: 0.88rem;">بدء الاختبار الآن ←</div>
      </a>

      <a href="sops.html" class="card" style="text-decoration: none; color: inherit;">
        <span class="page-pill">التشغيل وCRM</span>
        <h3 class="card-title">📋 الـ SOPs ومولد البريفات</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7;">
          إجراءات العمل القياسية داخل CoreLink CRM و ClickUp، ومولد تفاعلي لإنشاء بريفات المهام ومنع الهدر التشغيلي وإعادة العمل.
        </p>
        <div style="margin-top: 1.25rem; color: var(--gold-400); font-weight: 800; font-size: 0.88rem;">توليد بريف فوري ←</div>
      </a>
    </div>

  </main>
  {get_footer()}
</body>
</html>
"""

# ==============================================================================
# WRITE ALL UPGRADED PAGES
# ==============================================================================
print("Writing upgraded HTML pages...")
with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(p_index)

print("Generated upgraded index.html")

# Sync to Downloads
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)
print("Synchronized to Downloads!")
