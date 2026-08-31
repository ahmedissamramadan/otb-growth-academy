import os
import json

PORTAL_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy/track_c_interactive_portal"

# 1. DATA.JS
data_js = """
window.OTB_DATA = {
  agency: {
    name: "OTB Agency",
    tagline: "Bold Strategies · Real Results",
    motto: "We Are OTB — The City Kings 👑",
    phone: "+20 100 808 0295",
    email: "otbagency5@gmail.com",
    notebookUrl: "https://notebooklm.google.com/notebook/76ef5be2-d7d2-4a33-a88d-f88fc0fe1148",
    clients: ["MIX Coffee", "Rancho's EG", "Dr. Zaghloul Jewelry", "Rice Patisserie", "Sakr Store", "Elag Labs", "Wilson Crepe", "Ninety Six 96"]
  },
  sprint: [
    {
      id: "day1",
      day: "Day 01",
      title: "تحليل السوق الاستراتيجي وبناء الهوية والتموضع (STP & Positioning)",
      role: "Brand Strategists & Account Managers",
      duration: "90 دقيقة",
      summary: "تطبيق نموذج STP في السوق المصري، وتحديد شخصية العميل (Buyer Persona) الدقيقة، وفلسفة الهوية لملوك المدينة.",
      sections: [
        {
          title: "🎯 أهداف اليوم الأول",
          content: "1. إتقان نموذج STP (التقسيم، الاستهداف، التموضع) في السوق المصري.<br>2. تحديد شخصية العميل الدقيقة بناءً على الدوافع النفسية وليس الديموغرافيا فقط.<br>3. تطبيق نموذج The Ruler & The Creator في بناء هيبة العلامات التجارية."
        },
        {
          title: "📊 معادلة التموضع التنافسي (Positioning Statement)",
          content: "<b>Positioning Statement</b> = [الجمهور المستهدف] + [الفئة السوقية] + [الميزة التنافسية الجوهرية] + [سبب التصديق والبرهان الإثباتي].<br><br><i>مثال لـ MIX Coffee:</i> 'لرواد الأعمال والشباب الباحثين عن تجربة قهوة استثنائية، MIX Coffee هي وجهتك اليومية الأولى التي تقدم قهوة مختصة بأعلى معايير الجودة العالمية لأننا نستورد ونحمص حبوبنا الإثيوبية طازجة أسبوعياً.'"
        },
        {
          title: "💼 دراسة حالة عملية: Rancho's EG",
          content: "تحويل البراند من مجرد مطعم برجر تقليدي يحرق الأسعار إلى علامة تجارية فاخرة ذات طابع ملحمي، مما رفع معدل إعادة الطلب (Retention Rate) إلى 36.8% وزيادة متوسط الفاتورة بنسبة 45%."
        }
      ]
    },
    {
      id: "day2",
      day: "Day 02",
      title: "محرك الكرييتف الإعلاني والكوبي رايتنج وسيكولوجية الفيديو القصير",
      role: "Copywriters, Content Creators & Designers",
      duration: "90 دقيقة",
      summary: "إتقان نماذج AIDA و PAS و BAB، وتطبيق قاعدة الـ 3 ثوانٍ الأولى في ريلز وتيك توك، وهندسة العروض التي لا تقاوم.",
      sections: [
        {
          title: "🎯 أهداف اليوم الثاني",
          content: "1. إتقان صياغة الإعلانات المباشرة المحفزة للشراء الفوري.<br>2. تطبيق قاعدة الثواني الـ 3 الأولى لكسر التمرير (Pattern Interrupt).<br>3. رفع معدلات المشاهدة والـ Hook Rate فوق 35%."
        },
        {
          title: "✍️ نموذج PAS الإعلاني لقطاع المطاعم",
          content: "<b>Problem:</b> تعبت من البرجر اللي كله عيش واللحمة ملهاش طعم؟<br><b>Agitation:</b> بتدفع مبلغ محترم وفي الآخر بيجيلك بارد وتندم على الخروجة.<br><b>Solution:</b> في Rancho's مش بنعمل برجر عادي.. قطمة واحدة من الـ Smoked Double Beef بالصوص السري وهتعرف يعني إيه برجر ملوك حقيقي!"
        },
        {
          title: "🎬 تشريح الفيديو الفيرال الناجح",
          content: "<b>0-3 ثواني:</b> Hook بصري وصوتي خاطف.<br><b>3-15 ثانية:</b> القيمة وتفاصيل القصة وحل المشكلة.<br><b>15-25 ثانية:</b> العرض الحصري وغير القابل للمقاومة.<br><b>25-30 ثانية:</b> نداء واضح ومباشر للفعل (CTA)."
        }
      ]
    },
    {
      id: "day3",
      day: "Day 03",
      title: "ميديا بايينج الأداء على ميتا وتيك توك وسكيلينج الـ ROAS",
      role: "Media Buyers & Growth Marketers",
      duration: "90 دقيقة",
      summary: "هيكلة الحسابات الإعلانية، ضبط Conversions API (CAPI)، قراءة مؤشرات الأداء ROAS/CPA، وتطبيق التوسع الرأسي والأفقي.",
      sections: [
        {
          title: "🎯 أهداف اليوم الثالث",
          content: "1. بناء الهياكل الإعلانية المتقدمة (CBO vs ABO & Advantage+).<br>2. تتبع الأحداث الرقمية وتخطي قيود iOS 14.5+ بجودة مطابقة عالية.<br>3. سكيلينج الميزانيات من 1,000$ إلى 10,000$+ شهرياً بأمان."
        },
        {
          title: "🧮 معادلات الميديا باير المالية الحيوية",
          content: "<b>Break-Even ROAS</b> = 1 / Gross Profit Margin %<br><i>إذا كان هامش الربح 25%، فإن نقطة التعادل = 4.0x</i><br><br><b>CAC</b> = إجمالي الإنفاق الإعلاني والتسويقي / عدد العملاء الجدد المكتسبين."
        },
        {
          title: "⚡ قواعد السكيلينج الصارمة",
          content: "• زيادة ميزانية الحملة الرابحة بـ 20% فقط كل 48-72 ساعة.<br>• عدم الحكم على أي إعلان قبل اكتمال 50 حدث تحويل.<br>• إيقاف أي Ad Set ينفق ضعف الـ Target CPA دون تحقيق مبيعات."
        }
      ]
    },
    {
      id: "day4",
      day: "Day 04",
      title: "الذكاء الاصطناعي التسويقي وهندسة الأوامر وأتمتة الليدز",
      role: "All Team Members & Tech Leads",
      duration: "90 دقيقة",
      summary: "إتقان إطار RCIC للأوامر الذكية، وتوليد المحتوى الإعلاني بالـ AI، وأتمتة WhatsApp Business API لاسترجاع المبيعات.",
      sections: [
        {
          title: "🎯 أهداف اليوم الرابع",
          content: "1. إتقان إطار RCIC (الدور، السياق، المهمة، القيود) لأوامر تسويقية خالية من الأخطاء.<br>2. استخدام أدوات التوليد المرئي والنصي لمضاعفة سرعة الإنتاج 5 أضعاف.<br>3. بناء مسار أتمتة الواتساب للرد التلقائي وإتمام الصفقات في ثوانٍ."
        },
        {
          title: "🤖 إطار RCIC لهندسة الأوامر",
          content: "• <b>Role:</b> أنت Senior Copywriter & Growth Marketer بخبرة 10 سنوات.<br>• <b>Context:</b> العميل هو براند مجوهرات فاخر (Dr. Zaghloul) يستهدف السيدات والمقبلين على الزواج.<br>• <b>Instruction:</b> اكتب 3 نصوص إعلانية تركز على الأمان، القيمة الاستثمارية، والقصة الحصرية.<br>• <b>Constraint:</b> ممنوع العبارات المستهلكة، النبرة ملكية وواثقة بالعامية المصرية الراقية."
        },
        {
          title: "💬 أتمتة الـ WhatsApp Business API",
          content: "ربط إعلانات Click-to-WhatsApp بـ Bot يقوم بالترحيب، تصنيف رغبة العميل، إرسال الكتالوج والعرض، وتسجيل الطلب فوراً في CoreLink CRM."
        }
      ]
    },
    {
      id: "day5",
      day: "Day 05",
      title: "الانضباط التشغيلي وإدارة المشاريع وعقود الريتينر الشهرية",
      role: "Management, Account Managers & Team Leads",
      duration: "90 دقيقة",
      summary: "القضاء على متلازمة التوجيه الفارغ، تشغيل CoreLink CRM و ClickUp، وإغلاق عقود الريتينر الشهرية (1,500$ - 3,000$).",
      sections: [
        {
          title: "🎯 أهداف اليوم الخامس",
          content: "1. خفض نسبة إعادة العمل (Rework Rate) بأكثر من 40% عبر نماذج البريف الإلزامية.<br>2. تفعيل اتفاقيات مستوى الخدمة (SLA) وتصعيد المهام المتأخرة بعد 48 ساعة.<br>3. إتقان بيع وإغلاق عقود الريتينر الشهرية المربحة."
        },
        {
          title: "📋 دورة التشغيل القياسية داخل OTB",
          content: "1. <b>Briefing & Delegation:</b> بريف إلزامي كامل + تبعيات مقفولة.<br>2. <b>Execution & Tracking:</b> عمل فعلي مع تايمر + رفع التسليمات إلى Cloudflare R2.<br>3. <b>Review & QA:</b> مراجعة معتمدة خلال 24 ساعة.<br>4. <b>Delivery & Retainer:</b> تسليم وتقارير أداء دورية للعميل."
        },
        {
          title: "💼 باقات الريتينر الشهرية المعتمدة",
          content: "• <b>Growth Starter:</b> 1,200$/شهر للمشاريع الناشئة.<br>• <b>Dominance Retainer 👑:</b> 2,500$/شهر للبراندات وسلاسل المطاعم.<br>• <b>Enterprise Scale:</b> 4,500$+/شهر للشركات الكبرى والمتاجر الضخمة."
        }
      ]
    }
  ],
  prompts: [
    {
      role: "Copywriting",
      name: "إعلان PAS تحويلي للمطاعم والأغذية",
      template: "Role: You are a senior direct-response copywriter for OTB Agency.\\nContext: Client is [Brand Name], a premium [Food/Beverage] brand in Egypt known for [Unique Feature].\\nTask: Write 3 high-converting ad copies using the PAS (Problem-Agitation-Solution) framework in refined modern Egyptian Arabic.\\nConstraints: Bold and confident tone, no cliches, strong Call-to-Action for direct WhatsApp ordering."
    },
    {
      role: "Copywriting",
      name: "اسكريبت فيديو ريلز 15 ثانية بصيغة Storytelling",
      template: "Role: Viral short-form video director for OTB Agency.\\nContext: Creating an Instagram Reel for [Brand Name] in [Industry].\\nTask: Write a shot-by-shot 15-second script with a 3-second visual/audio scroll-stopping hook, dynamic ASMR cuts, and direct promotional offer.\\nFormat: Time (Sec) | Visual Scene | Audio Effect | On-Screen Text / Voiceover."
    },
    {
      role: "Media Buying",
      name: "تشخيص الحملات الإعلانية وقرار السكيلينج",
      template: "Role: Principal Media Buyer and Growth Architect at OTB Agency.\\nContext: Analyzing campaign data for [Client Name]: Spend: $[Spend], CTR: [CTR]%, Purchases: [Purchases], ROAS: [ROAS]x, CPA: $[CPA].\\nTask: Diagnose funnel bottlenecks (Hook Rate, Drop-off), recommend scaling direction (Vertical vs Horizontal), and provide a 48-hour action plan."
    },
    {
      role: "Account Management",
      name: "صياغة مقترح عقد ريتينر شهري (Retainer Proposal)",
      template: "Role: Commercial Director at OTB Marketing Studio (The City Kings).\\nContext: Executive growth proposal for [Potential Client] in [Industry].\\nTask: Write a 1-page executive summary covering competitive market gaps, OTB's 90-day growth roadmap, $2,500/month Retainer deliverables, and expected ROAS targets."
    },
    {
      role: "Design & Creative",
      name: "برومبت توليد برودكت شوت ثلاثي الأبعاد (Midjourney)",
      template: "/imagine prompt: Ultra-realistic 3D commercial product photography of [Product Name, e.g., premium dark iced coffee bottle in frosted glass], elegant royal gold droplets, obsidian black podium, dramatic rim lighting, cinematic 8k resolution, photorealistic studio render --ar 9:16 --style raw --v 6.0"
    }
  ],
  quiz: [
    {
      question: "ما هو التموضع والنمط النفسي المعتمد لوكالة OTB في السوق؟",
      options: [
        "التركيز على خفض التكاليف والمنافسة السعرية",
        "The Ruler & The Creator (ملوك المدينة: الهيبة والجرأة والتركيز على العائد المالي)",
        "تقديم تصاميم عادية دون استراتيجية أو أرقام",
        "الاعتماد الكامل على الإعلانات الممولة فقط"
      ],
      correct: 1,
      explanation: "تموضع OTB يجمع بين هيبة الملك والجرأة الإبداعية لصناعة نتائج حقيقية وأرقام مبيعات ملموسة."
    },
    {
      question: "ما هو الهدف الحاسم من أول 3 ثوانٍ في أي فيديو إعلاني قصير (Reels/TikTok)؟",
      options: [
        "عرض عناوين الفروع وأرقام التواصل",
        "كسر التمرير (Pattern Interrupt) وجذب انتباه المشاهد الفوري (Hook Rate > 35%)",
        "شرح تاريخ تأسيس الشركة",
        "وضع حقوق الملكية الفكرية"
      ],
      correct: 1,
      explanation: "أول 3 ثوانٍ تحدد نجاح أو فشل الإعلان بالكامل من خلال إيقاف التمرير والاحتفاظ بالمشاهد."
    },
    {
      question: "إذا كان هامش الربح الإجمالي لمنتج هو 25%، فما هو الـ Break-Even ROAS المطلوب لتحقيق التعادل؟",
      options: [
        "1.5x",
        "2.0x",
        "4.0x (حيث 1 مقسومة على 0.25 = 4)",
        "8.0x"
      ],
      correct: 2,
      explanation: "معادلة نقطة التعادل = 1 / هامش الربح (1 / 0.25 = 4.0x)."
    },
    {
      question: "ما هي القاعدة الآمنة للتوسع الرأسي (Vertical Scaling) في ميزانية الحملات الرابحة؟",
      options: [
        "مضاعفة الميزانية 200% كل يوم",
        "زيادة الميزانية بنسبة 20% كل 48-72 ساعة لمنع إعادة دخول مرحلة التعلم",
        "تغيير الاستهداف الإعلاني يومياً",
        "إغلاق الحملة وإعادة تشغيلها"
      ],
      correct: 1,
      explanation: "زيادة 20% كل يومين إلى 3 أيام تضمن الحفاظ على استقرار أداء الخوارزمية وتكلفة الاكتساب."
    },
    {
      question: "ما الذي يرمز له حرف (C) الأخير في إطار هندسة الأوامر التسويقية RCIC؟",
      options: [
        "Creativity (الإبداع)",
        "Constraints (القيود والشروط والممنوعات)",
        "Category (الفئة)",
        "Customer (العميل)"
      ],
      correct: 1,
      explanation: "Constraints هي المحددات التي تمنع النموذج من استخدام عبارات مستهلكة وتحدد النبرة والصيغة بدقة."
    },
    {
      question: "كيف يتم القضاء على 'متلازمة التوجيه الفارغ' (Empty Brief) داخل CoreLink CRM؟",
      options: [
        "التواصل عبر رسائل واتساب شفهية",
        "إلزامية تعبئة نموذج البريف الكامل والاعتماد النصي قبل بدء مرحلة التصميم",
        "البدء في التصميم فوراً دون أي نصوص",
        "إلغاء المراجعات بالكامل"
      ],
      correct: 1,
      explanation: "نماذج البريف الإلزامية و Sequential Locking تخفض نسبة إعادة العمل بأكثر من 40%."
    }
  ]
};
"""

# 2. STYLE.CSS
style_css = """
:root {
  --bg-primary: #070A10;
  --bg-secondary: #0D131F;
  --bg-card: rgba(13, 19, 31, 0.75);
  --gold-primary: #F59E0B;
  --gold-light: #FEF3C7;
  --gold-dark: #B45309;
  --gold-gradient: linear-gradient(135deg, #DFBA73 0%, #C5A059 50%, #9A7B38 100%);
  --crimson: #E11D48;
  --emerald: #10B981;
  --text-main: #F8FAFC;
  --text-muted: #94A3B8;
  --border-color: rgba(245, 158, 11, 0.2);
  --border-highlight: rgba(245, 158, 11, 0.5);
  --glass-blur: blur(16px);
  --shadow-gold: 0 10px 30px -10px rgba(245, 158, 11, 0.25);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Readex Pro', 'Cairo', sans-serif;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-main);
  direction: rtl;
  min-height: 100vh;
  overflow-x: hidden;
  background-image: 
    radial-gradient(circle at 15% 15%, rgba(245, 158, 11, 0.08) 0%, transparent 40%),
    radial-gradient(circle at 85% 85%, rgba(225, 29, 72, 0.05) 0%, transparent 40%);
  background-attachment: fixed;
}

/* NAVBAR & HEADER */
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(7, 10, 16, 0.85);
  backdrop-filter: var(--glass-blur);
  border-bottom: 1px solid var(--border-color);
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-badge {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.crown-icon {
  font-size: 1.8rem;
  filter: drop-shadow(0 0 8px rgba(245, 158, 11, 0.6));
}

.brand-title h1 {
  font-size: 1.25rem;
  font-weight: 800;
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: -0.5px;
}

.brand-title p {
  font-size: 0.75rem;
  color: var(--text-muted);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.btn-notebook {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(245, 158, 11, 0.1);
  border: 1px solid var(--gold-primary);
  color: var(--gold-light);
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-notebook:hover {
  background: var(--gold-primary);
  color: #000;
  box-shadow: var(--shadow-gold);
  transform: translateY(-2px);
}

/* AUDIO BAR EMBED */
.audio-strip {
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
  padding: 0.75rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.audio-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.85rem;
}

.pulse-dot {
  width: 10px;
  height: 10px;
  background-color: var(--emerald);
  border-radius: 50%;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
  70% { transform: scale(1.1); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

audio {
  height: 36px;
  max-width: 400px;
  outline: none;
}

/* MAIN LAYOUT */
.main-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

/* NAVIGATION TABS */
.nav-tabs {
  display: flex;
  gap: 0.5rem;
  border-bottom: 1px solid var(--border-color);
  margin-bottom: 2rem;
  overflow-x: auto;
  padding-bottom: 0.5rem;
}

.tab-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 0.75rem 1.25rem;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  border-radius: 8px 8px 0 0;
  transition: all 0.3s ease;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.tab-btn:hover {
  color: var(--gold-light);
  background: rgba(245, 158, 11, 0.05);
}

.tab-btn.active {
  color: var(--gold-primary);
  border-bottom: 3px solid var(--gold-primary);
  background: rgba(245, 158, 11, 0.1);
}

/* TAB CONTENT PANELS */
.tab-panel {
  display: none;
  animation: fadeIn 0.4s ease;
}

.tab-panel.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

/* GRID & CARDS */
.grid-2col {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 2rem;
}

@media (max-width: 992px) {
  .grid-2col { grid-template-columns: 1fr; }
}

.card {
  background: var(--bg-card);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
  transition: border-color 0.3s ease;
}

.card:hover {
  border-color: var(--border-highlight);
}

/* DAY / LESSON SELECTOR */
.lesson-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.lesson-item {
  padding: 1rem;
  background: var(--bg-secondary);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.lesson-item:hover {
  border-color: var(--gold-primary);
  transform: translateX(-4px);
}

.lesson-item.active {
  background: rgba(245, 158, 11, 0.12);
  border-color: var(--gold-primary);
  box-shadow: 0 0 15px rgba(245, 158, 11, 0.15);
}

.lesson-badge {
  display: inline-block;
  padding: 0.2rem 0.6rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 700;
  background: var(--gold-primary);
  color: #000;
  margin-bottom: 0.5rem;
}

.lesson-title {
  font-size: 0.95rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.lesson-meta {
  font-size: 0.8rem;
  color: var(--text-muted);
}

/* LESSON DETAIL VIEW */
.lesson-header {
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 1.5rem;
  margin-bottom: 1.5rem;
}

.lesson-header h2 {
  font-size: 1.5rem;
  color: var(--gold-light);
  margin-bottom: 0.5rem;
}

.lesson-section {
  background: var(--bg-secondary);
  border-radius: 12px;
  padding: 1.25rem;
  margin-bottom: 1.25rem;
  border-right: 4px solid var(--gold-primary);
}

.lesson-section h3 {
  font-size: 1.1rem;
  color: var(--gold-primary);
  margin-bottom: 0.75rem;
}

.lesson-section p, .lesson-section div {
  font-size: 0.95rem;
  line-height: 1.7;
  color: #E2E8F0;
}

/* PROMPT STUDIO */
.prompt-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
}

.prompt-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.prompt-role {
  font-size: 0.75rem;
  text-transform: uppercase;
  color: var(--gold-primary);
  font-weight: 700;
  letter-spacing: 1px;
}

.prompt-name {
  font-size: 1.1rem;
  font-weight: 700;
  margin: 0.5rem 0 1rem 0;
}

.prompt-code {
  background: #000;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 1rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  color: #38BDF8;
  direction: ltr;
  text-align: left;
  white-space: pre-wrap;
  margin-bottom: 1rem;
  max-height: 200px;
  overflow-y: auto;
}

.btn-copy {
  background: var(--gold-primary);
  color: #000;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.btn-copy:hover {
  background: var(--gold-light);
  box-shadow: var(--shadow-gold);
}

/* QUIZ STYLES */
.quiz-box {
  max-width: 800px;
  margin: 0 auto;
}

.question-card {
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: var(--bg-secondary);
  border-radius: 12px;
  border: 1px solid var(--border-color);
}

.question-title {
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.quiz-option {
  display: block;
  padding: 0.85rem 1.25rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  margin-bottom: 0.75rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.quiz-option:hover {
  background: rgba(245, 158, 11, 0.08);
  border-color: var(--gold-primary);
}

.quiz-option.selected {
  background: rgba(245, 158, 11, 0.2);
  border-color: var(--gold-primary);
  color: var(--gold-light);
}

.quiz-option.correct {
  background: rgba(16, 185, 129, 0.25) !important;
  border-color: var(--emerald) !important;
}

.quiz-option.wrong {
  background: rgba(225, 29, 72, 0.25) !important;
  border-color: var(--crimson) !important;
}

.quiz-result {
  text-align: center;
  padding: 2rem;
  background: var(--bg-secondary);
  border-radius: 16px;
  border: 2px solid var(--gold-primary);
}

/* SOP GENERATOR */
.form-group {
  margin-bottom: 1.25rem;
}

.form-group label {
  display: block;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--gold-light);
}

.form-control {
  width: 100%;
  background: var(--bg-secondary);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 0.75rem 1rem;
  color: #FFF;
  outline: none;
  font-size: 0.95rem;
}

.form-control:focus {
  border-color: var(--gold-primary);
}
"""

# 3. APP.JS
app_js = """
document.addEventListener("DOMContentLoaded", () => {
  const { agency, sprint, prompts, quiz } = window.OTB_DATA;
  
  // 1. TAB NAVIGATION
  const tabBtns = document.querySelectorAll(".tab-btn");
  const tabPanels = document.querySelectorAll(".tab-panel");
  
  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      tabBtns.forEach(b => b.classList.remove("active"));
      tabPanels.forEach(p => p.classList.remove("active"));
      
      btn.classList.add("active");
      const target = btn.getAttribute("data-target");
      document.getElementById(target).classList.add("active");
    });
  });
  
  // 2. RENDER SPRINT LESSONS
  const sprintListEl = document.getElementById("sprintList");
  const sprintDetailEl = document.getElementById("sprintDetail");
  
  function renderSprint(selectedId) {
    sprintListEl.innerHTML = "";
    sprint.forEach(item => {
      const el = document.createElement("div");
      el.className = `lesson-item ${item.id === selectedId ? "active" : ""}`;
      el.innerHTML = `
        <span class="lesson-badge">${item.day}</span>
        <div class="lesson-title">${item.title}</div>
        <div class="lesson-meta">⏱️ ${item.duration} · 👥 ${item.role}</div>
      `;
      el.addEventListener("click", () => renderSprint(item.id));
      sprintListEl.appendChild(el);
    });
    
    const activeItem = sprint.find(s => s.id === selectedId) || sprint[0];
    let sectionsHtml = "";
    activeItem.sections.forEach(sec => {
      sectionsHtml += `
        <div class="lesson-section">
          <h3>${sec.title}</h3>
          <div>${sec.content}</div>
        </div>
      `;
    });
    
    sprintDetailEl.innerHTML = `
      <div class="lesson-header">
        <span class="lesson-badge">${activeItem.day}</span>
        <h2>${activeItem.title}</h2>
        <p style="color: var(--text-muted);">${activeItem.summary}</p>
      </div>
      ${sectionsHtml}
    `;
  }
  renderSprint("day1");
  
  // 3. RENDER PROMPTS STUDIO
  const promptGridEl = document.getElementById("promptGrid");
  prompts.forEach((p, idx) => {
    const card = document.createElement("div");
    card.className = "card prompt-card";
    card.innerHTML = `
      <div>
        <span class="prompt-role">${p.role}</span>
        <h3 class="prompt-name">${p.name}</h3>
        <pre class="prompt-code" id="promptText_${idx}">${p.template}</pre>
      </div>
      <button class="btn-copy" onclick="copyPrompt(${idx})">
        📋 نسخ الأمر المعتمد
      </button>
    `;
    promptGridEl.appendChild(card);
  });
  
  window.copyPrompt = (idx) => {
    const text = document.getElementById(`promptText_${idx}`).innerText;
    navigator.clipboard.writeText(text).then(() => {
      alert("تم نسخ الأمر بنجاح إلى الحافظة!");
    });
  };
  
  // 4. RENDER QUIZ
  const quizBoxEl = document.getElementById("quizBox");
  let userAnswers = {};
  
  function renderQuiz() {
    quizBoxEl.innerHTML = "";
    quiz.forEach((q, qIdx) => {
      const qCard = document.createElement("div");
      qCard.className = "question-card";
      let optionsHtml = "";
      q.options.forEach((opt, oIdx) => {
        optionsHtml += `
          <div class="quiz-option" data-q="${qIdx}" data-o="${oIdx}" onclick="selectOption(${qIdx}, ${oIdx})">
            ${opt}
          </div>
        `;
      });
      qCard.innerHTML = `
        <div class="question-title">سؤال ${qIdx + 1}: ${q.question}</div>
        <div class="options-group">${optionsHtml}</div>
        <div id="explanation_${qIdx}" style="display:none; margin-top:1rem; padding:0.75rem; background:rgba(245,158,11,0.1); border-radius:8px; font-size:0.85rem;"></div>
      `;
      quizBoxEl.appendChild(qCard);
    });
  }
  
  window.selectOption = (qIdx, oIdx) => {
    userAnswers[qIdx] = oIdx;
    const options = document.querySelectorAll(`[data-q="${qIdx}"]`);
    options.forEach(opt => opt.classList.remove("selected"));
    document.querySelector(`[data-q="${qIdx}"][data-o="${oIdx}"]`).classList.add("selected");
  };
  
  window.submitQuiz = () => {
    let score = 0;
    quiz.forEach((q, qIdx) => {
      const selected = userAnswers[qIdx];
      const options = document.querySelectorAll(`[data-q="${qIdx}"]`);
      const explEl = document.getElementById(`explanation_${qIdx}`);
      explEl.style.display = "block";
      explEl.innerHTML = `<b>توضيح الإجابة:</b> ${q.explanation}`;
      
      options.forEach((opt, oIdx) => {
        if (oIdx === q.correct) opt.classList.add("correct");
        if (selected !== undefined && selected === oIdx && selected !== q.correct) {
          opt.classList.add("wrong");
        }
      });
      if (selected === q.correct) score++;
    });
    
    const percentage = Math.round((score / quiz.length) * 100);
    const resultEl = document.getElementById("quizResult");
    resultEl.style.display = "block";
    resultEl.innerHTML = `
      <h2>النتيجة النهائية: ${score} من ${quiz.length} (${percentage}%)</h2>
      <p style="margin: 1rem 0; font-size: 1.1rem;">
        ${percentage >= 80 ? "👑 مبروك! لقد اجتزت اختبار أكاديمية OTB بدرجة امتياز وحصلت على اعتماد النمو الملكي." : "⚠️ تحتاج لمراجعة بعض الدروس في المعسكر للوصول لمستوى التميز."}
      </p>
    `;
    window.scrollTo({ top: resultEl.offsetTop - 100, behavior: "smooth" });
  };
  
  renderQuiz();
  
  // 5. SOP BRIEF BUILDER
  window.generateBrief = () => {
    const client = document.getElementById("sopClient").value || "العميل";
    const type = document.getElementById("sopType").value;
    const goal = document.getElementById("sopGoal").value || "تحقيق مبيعات مباشرة";
    const angle = document.getElementById("sopAngle").value || "العرض الحصري والضمان الملكي";
    const notes = document.getElementById("sopNotes").value || "الالتزام بهوية OTB الصارمة وتفادي الكليشيهات.";
    
    const output = `### 👑 OTB OFFICIAL BRIEF: ${client}
* **النوع والقسم:** ${type}
* **الهدف التسويقي:** ${goal}
* **الزاوية الإعلانية:** ${angle}
* **المحددات ونبرة الصوت:** ${notes}
* **تاريخ التسليم والاعتماد:** ${new Date().toLocaleDateString('ar-EG')}
* **نظام التتبع:** CoreLink CRM / Cloudflare R2`;
    
    document.getElementById("sopOutput").value = output;
  };
});
"""

# 4. INDEX.HTML
index_html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 OTB Growth Academy — The City Kings Internal Hub</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=JetBrains+Mono:wght@600;700&family=Readex+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- NAVBAR -->
  <header class="navbar">
    <div class="brand-badge">
      <span class="crown-icon">👑</span>
      <div class="brand-title">
        <h1>OTB GROWTH ACADEMY</h1>
        <p>THE CITY KINGS · INTERNAL MASTERY PORTAL 2026</p>
      </div>
    </div>
    <div class="nav-actions">
      <a href="https://notebooklm.google.com/notebook/76ef5be2-d7d2-4a33-a88d-f88fc0fe1148" target="_blank" class="btn-notebook">
        <span>✨ فتح مشروع NotebookLM الرسمي</span>
      </a>
    </div>
  </header>

  <!-- AUDIO STRIP (PODCAST PLAYER) -->
  <section class="audio-strip">
    <div class="audio-info">
      <div class="pulse-dot"></div>
      <div>
        <strong>🎙️ البودكاست الاستراتيجي المعتمد:</strong>
        <span style="color: var(--gold-light);">OTB Growth Engineering & Full-Stack AI Overview</span>
      </div>
    </div>
    <audio controls>
      <source src="../track_b_4week_masterclass/studio_artifacts/OTB_Growth_Podcast.mp4" type="audio/mp4">
      متصفحك لا يدعم مشغل الصوت المباشر.
    </audio>
  </section>

  <!-- MAIN CONTAINER -->
  <main class="main-container">
    
    <!-- NAVIGATION TABS -->
    <nav class="nav-tabs">
      <button class="tab-btn active" data-target="tabSprint">⚡ معسكر الـ 5 أيام السريع (Sprint)</button>
      <button class="tab-btn" data-target="tabMasterclass">📚 الأكاديمية الشاملة (4 أسابيع)</button>
      <button class="tab-btn" data-target="tabPrompts">🤖 استوديو أوامر الذكاء الاصطناعي</button>
      <button class="tab-btn" data-target="tabQuiz">📝 الاختبار التفاعلي والاعتماد</button>
      <button class="tab-btn" data-target="tabSOP">📋 مولد البريفات القياسية (SOPs)</button>
      <button class="tab-btn" data-target="tabDownloads">📥 مركز الملفات والمستخرجات</button>
    </nav>

    <!-- TAB 1: SPRINT -->
    <section id="tabSprint" class="tab-panel active">
      <div class="grid-2col">
        <div class="card">
          <h3 style="margin-bottom: 1rem; color: var(--gold-primary);">📅 جدول أيام المعسكر</h3>
          <div class="lesson-list" id="sprintList"></div>
        </div>
        <div class="card" id="sprintDetail"></div>
      </div>
    </section>

    <!-- TAB 2: MASTERCLASS -->
    <section id="tabMasterclass" class="tab-panel">
      <div class="card" style="margin-bottom: 1.5rem;">
        <h2 style="color: var(--gold-light); margin-bottom: 0.5rem;">👑 مسار الأكاديمية التخصصية الشاملة (4 أسابيع)</h2>
        <p style="color: var(--text-muted);">تحويل المنهج الأكاديمي لـ 16 وحدة تخصصية مقسمة على 4 مراحل محورية لبناء منظومة التسويق وهندسة النمو 360°.</p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
        <div class="card">
          <span class="lesson-badge">الأسبوع 01</span>
          <h3 style="margin: 0.5rem 0; color: var(--gold-primary);">الاستراتيجية وأبحاث السوق والبراندنج</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">بناء ملف التموضع الاستراتيجي، ونموذج STP، والهوية الملكية لـ OTB (The Ruler & Creator).</p>
        </div>
        <div class="card">
          <span class="lesson-badge">الأسبوع 02</span>
          <h3 style="margin: 0.5rem 0; color: var(--gold-primary);">محرك الكرييتف والسيو الفيرال</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">كتابة الإعلانات التحويلية، سيكولوجية الفيديو القصير وسيو المواقع والمطاعم.</p>
        </div>
        <div class="card">
          <span class="lesson-badge">الأسبوع 03</span>
          <h3 style="margin: 0.5rem 0; color: var(--gold-primary);">ميديا بايينج الأداء وسكيلينج الـ ROAS</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">إعلانات Meta/TikTok، ضبط CAPI، ومضاعفة الميزانيات بأمان من 1K$ إلى 50K$.</p>
        </div>
        <div class="card">
          <span class="lesson-badge">الأسبوع 04</span>
          <h3 style="margin: 0.5rem 0; color: var(--gold-primary);">الذكاء الاصطناعي وعقود الريتينر</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">أتمتة WhatsApp API، إدارة مشاريع CoreLink CRM، ومشروع التخرج الشامل 360°.</p>
        </div>
      </div>
    </section>

    <!-- TAB 3: PROMPTS STUDIO -->
    <section id="tabPrompts" class="tab-panel">
      <div class="card" style="margin-bottom: 1.5rem;">
        <h2 style="color: var(--gold-light); margin-bottom: 0.5rem;">🤖 استوديو أوامر الذكاء الاصطناعي المعتمدة</h2>
        <p style="color: var(--text-muted);">أوامر ذكاء اصطناعي تم اختبارها وصياغتها بإطار RCIC لتوليد المحتوى والإعلانات واستراتيجيات النمو بنقرة واحدة.</p>
      </div>
      <div class="prompt-grid" id="promptGrid"></div>
    </section>

    <!-- TAB 4: QUIZ -->
    <section id="tabQuiz" class="tab-panel">
      <div class="quiz-box">
        <div class="card" style="margin-bottom: 1.5rem; text-align: center;">
          <h2 style="color: var(--gold-light); margin-bottom: 0.5rem;">📝 اختبار تقييم الكفاءة التسويقية لملوك المدينة</h2>
          <p style="color: var(--text-muted);">أجب عن الأسئلة التالية لاختبار استيعابك لمنهج ومفاهيم النمو المعتمدة داخل OTB.</p>
        </div>
        <div id="quizBox"></div>
        <div style="text-align: center; margin-top: 2rem;">
          <button class="btn-copy" style="padding: 1rem 2.5rem; font-size: 1.1rem; margin: 0 auto;" onclick="submitQuiz()">
            👑 تسليم الإجابات وحساب النتيجة
          </button>
        </div>
        <div id="quizResult" class="quiz-result" style="display:none; margin-top: 2rem;"></div>
      </div>
    </section>

    <!-- TAB 5: SOP BUILDER -->
    <section id="tabSOP" class="tab-panel">
      <div class="grid-2col">
        <div class="card">
          <h3 style="color: var(--gold-primary); margin-bottom: 1rem;">⚙️ إعداد بيانات البريف</h3>
          <div class="form-group">
            <label>اسم العميل / البراند:</label>
            <input type="text" id="sopClient" class="form-control" placeholder="مثال: MIX Coffee / Rancho's">
          </div>
          <div class="form-group">
            <label>نوع التكليف والقسم:</label>
            <select id="sopType" class="form-control">
              <option>كتابة محتوى وكوبي رايتنج إعلاني</option>
              <option>تصميم سوشيال ميديا وموشن جرافيك</option>
              <option>إطلاق وإدارة حملات ميديا بايينج ممولة</option>
              <option>أتمتة رسائل واتساب وخدمة عملاء</option>
            </select>
          </div>
          <div class="form-group">
            <label>الهدف التسويقي الأساسي:</label>
            <input type="text" id="sopGoal" class="form-control" placeholder="مثال: مضاعفة المبيعات / إطلاق فرع جديد">
          </div>
          <div class="form-group">
            <label>الزاوية الإعلانية (Angle):</label>
            <input type="text" id="sopAngle" class="form-control" placeholder="مثال: زاوية الفخامة والجودة الاستثنائية">
          </div>
          <div class="form-group">
            <label>ملاحظات وممنوعات (Constraints):</label>
            <textarea id="sopNotes" class="form-control" rows="3" placeholder="ممنوع استخدام عبارات تقليدية.."></textarea>
          </div>
          <button class="btn-copy" style="width: 100%;" onclick="generateBrief()">⚡ توليد البريف القياسي</button>
        </div>
        <div class="card">
          <h3 style="color: var(--gold-primary); margin-bottom: 1rem;">📋 الناتج التنفيذي للإسناد في CoreLink CRM</h3>
          <textarea id="sopOutput" class="form-control" style="height: 350px; font-family: 'JetBrains Mono', monospace;" readonly placeholder="اضغط على زر التوليد لعرض البريف القياسي هنا..."></textarea>
        </div>
      </div>
    </section>

    <!-- TAB 6: DOWNLOADS -->
    <section id="tabDownloads" class="tab-panel">
      <div class="card" style="margin-bottom: 1.5rem;">
        <h2 style="color: var(--gold-light); margin-bottom: 0.5rem;">📥 مركز المستخرجات والأصول التنفيذية</h2>
        <p style="color: var(--text-muted);">جميع الملفات والأدلة المنشأة محفوظة محلياً وجاهزة للمشاركة المباشرة مع الفريق.</p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
        <div class="card">
          <h3 style="color: var(--gold-primary); margin-bottom: 0.5rem;">⚡ حقائب معسكر الـ 5 أيام</h3>
          <ul style="list-style: none; padding: 0; font-size: 0.9rem; line-height: 2;">
            <li>📄 Day 01: Strategic Market Analysis</li>
            <li>📄 Day 02: Creative Engine & Copywriting</li>
            <li>📄 Day 03: Performance Media Buying</li>
            <li>📄 Day 04: AI Marketing & Automation</li>
            <li>📄 Day 05: Operations & Retainers</li>
          </ul>
        </div>
        <div class="card">
          <h3 style="color: var(--gold-primary); margin-bottom: 0.5rem;">📖 الأدلة التكتيكية والكوديكس</h3>
          <ul style="list-style: none; padding: 0; font-size: 0.9rem; line-height: 2;">
            <li>📖 OTB Prompt Engineering Bible (50+ Prompts)</li>
            <li>✈️ OTB Media Buying Pre-Flight Checklist</li>
            <li>📋 OTB Standard SOPs & Briefing Templates</li>
            <li>🎓 OTB 360° Capstone Growth Engine Brief</li>
          </ul>
        </div>
        <div class="card">
          <h3 style="color: var(--gold-primary); margin-bottom: 0.5rem;">🎙️ أصول Gemini Studio الرسمية</h3>
          <ul style="list-style: none; padding: 0; font-size: 0.9rem; line-height: 2;">
            <li>🎙️ OTB Growth Engineering Podcast (MP4 Audio)</li>
            <li>📑 OTB Executive Strategic Briefing (Markdown)</li>
            <li>📝 OTB Marketing Assessment Quiz (JSON)</li>
          </ul>
        </div>
      </div>
    </section>

  </main>

  <script src="data.js"></script>
  <script src="app.js"></script>
</body>
</html>
"""

print("Writing Track C Web Portal files...")
with open(os.path.join(PORTAL_DIR, "data.js"), "w", encoding="utf-8") as f:
    f.write(data_js)
with open(os.path.join(PORTAL_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(style_css)
with open(os.path.join(PORTAL_DIR, "app.js"), "w", encoding="utf-8") as f:
    f.write(app_js)
with open(os.path.join(PORTAL_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# ==========================================
# SYNC ALL FILES TO DOWNLOADS/MATERIALS
# ==========================================
print(f"Syncing all materials to {DOWNLOADS_DIR}...")
if os.path.exists(DOWNLOADS_DIR):
    shutil.rmtree(DOWNLOADS_DIR)
shutil.copytree(BASE_DIR, DOWNLOADS_DIR)

print("ALL ASSETS SUCCESSFULLY GENERATED AND SYNCED TO DOWNLOADS!")
