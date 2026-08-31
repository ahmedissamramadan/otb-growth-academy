import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

# ==========================================
# 1. TRACK A: 5-DAY FAST-TRACK SPRINT FILES
# ==========================================

day1_content = """# 👑 OTB Growth Academy — Sprint Day 01
## تحليل السوق الاستراتيجي وبناء الهوية وتموضع البراند (Strategic Market Analysis & Brand Positioning)

> **شعار وكالة OTB:** *"استراتيجيات جريئة.. نتائج حقيقية | Bold Strategies. Real Results"*  
> **الهتاف والتموضع:** *"We Are OTB — The City Kings" 👑*  
> **المستهدفون:** فريق الاستراتيجية (Brand Strategists)، مدراء الحسابات (Account Managers)، كتاب المحتوى (Copywriters)، ورؤساء الأقسام.  
> **المدة المقررة:** 90 دقيقة تدريبية + 45 دقيقة تطبيق عملي.

---

### 🎯 1. أهداف جلسة اليوم الأول (Learning Objectives)
بنهاية جلسة اليوم، سيكون كل عضو في الفريق قادراً على:
1. تطبيق نموذج **STP (Segmentation, Targeting, Positioning)** على أي براند مصري/عربي في قطاعات الأغذية (F&B)، التجارة الإلكترونية (E-Commerce)، أو الخدمات والعيادات الطبية.
2. استخراج وصياغة **شخصية العميل المثالي (Buyer Persona)** الدقيقة القائمة على الألم النفسي (Pain Points) والدافع الشرائي الفعلي وليس مجرد بيانات ديموغرافية سطحية.
3. تفكيك وبناء الهوية المؤسسية بناءً على نموذج **النمط النفسي (The Ruler & The Creator Archetype)** المعتمد في OTB.
4. صياغة نبرة الصوت (Tone of Voice) للبراند وتحويلها إلى ميثاق كتابي يمنع تضارب المحتوى والتصاميم.

---

### 📊 2. الإطار النظري والتكتيكي (Core Frameworks)

#### أ. نموذج STP في السوق الواقعي (Real-World STP Execution)
* **Segmentation (التقسيم):** تقسيم السوق وفق 4 أبعاد حاسمة:
  * *السلوكي (Behavioral):* معدل تكرار الشراء، الحساسية للسعر، الاستجابة للعروض والخصومات.
  * *النفسي (Psychographic):* المكانة الاجتماعية (Social Status)، البحث عن التميز، الرغبة في الراحة وتوفير الوقت.
  * *الديموغرافي والجغرافي (Demographic & Geographic):* القاهرة الكبرى، الإسكندرية، الدلتا، وتحديد مناطق التوصيل والنفوذ.
* **Targeting (الاستهداف):** تحديد الشريحة ذات أعلى قيمة عمرية للعميل (Highest LTV) وأقل تكلفة استحواذ (Lowest CAC).
* **Positioning (التموضع):** صياغة معادلة التموضع التنافسي:
  $$\\text{Positioning Statement} = \\text{[Target Audience]} + \\text{[Category]} + \\text{[Differentiating Benefit]} + \\text{[Reason to Believe]}$$

```mermaid
flowchart TD
    Market[السوق الكلي المتاح TAM] --> Segments[تقسيم الشرائح SAM]
    Segments --> Target[الشريحة الأكثر ربحية SOM]
    Target --> ValueProp[القيمة المقترحة الفريدة UVP]
    ValueProp --> Positioning[التموضع في ذهن المستهلك]
```

#### ب. النمط النفسي لـ OTB: The Ruler & The Creator 👑
في OTB، لا نصنع محتوى عادياً يمر مرور الكرام؛ نحن نبني علامات تجارية تتصدر السوق:
* **The Ruler (الملك/القائد):** فرض الهيبة السوقية، الثقة المطلقة في جودة المنتج، الحديث من موقع الخبير المتمكن.
* **The Creator (المبدع/المبتكر):** تقديم أفكار خارج الصندوق (Out of The Box)، كسر الملل البصري، وصناعة تريندات جديدة بدلاً من اللحاق بها.

---

### 💼 3. دراسات حالة من عملاء OTB الفعليين (Case Studies)

| العميل / البراند | القطاع | التحدي السابق | الاستراتيجية والتموضع المطبق في OTB | النتيجة المحققة |
|---|---|---|---|---|
| **MIX Coffee** | أغذية ومشروبات (F&B / Specialty Coffee) | منافسة شرسة مع البراندات الكبرى وضعف التميز البصري. | تموضع كوجهة أولى لتجربة القهوة الفاخرة للشباب ورواد الأعمال + هوية داكنة راقية. | زيادة تفاعل الحساب بنسبة 180% ومضاعفة المبيعات اليومية للفروع. |
| **Rancho's EG** | مطاعم وبرجر سريع | حرق أسعار وعروض غير مجدية تسببت في انخفاض الهامش الربحي. | إعادة هيكلة القائمة وربط البراند بتجربة الطعم الملحمي الحصري والجودة الفائقة. | رفع معدل إعادة الطلب (Retention Rate) إلى 36.8% وتحقيق أعلى استقرار تشغيلي. |
| **Dr. Zaghloul Jewelry** | مجوهرات وتجارة فاخرة | انعدام الثقة في طلب قطع الذهب والمجوهرات عبر السوشيال ميديا. | التركيز على زاوية الأمان والمصداقية والقصص المرئية الحصرية لكل قطعة. | تحقيق مبيعات مباشرة وتوليد ليدز عالية الجودة بمعدل ROAS يتجاوز 7.5x. |

---

### 🛠️ 4. التكليف التطبيقي الفوري (Day 1 Team Workshop)
* **المطلوب من كل متدرب / قسم:**
  1. اختيار أحد عملاء الوكالة الحاليين أو عميل جديد قيد الاستقبال (Onboarding).
  2. ملء **وثيقة البريف الاستراتيجي (Brand Discovery Sheet)**.
  3. استخراج 3 زوايا تسويقية غير تقليدية (Unconventional Angles) تستغل فجوات المنافسين في السوق.

---
**OTB Agency — We Are The City Kings 👑**  
*القاهرة · +20 100 808 0295 · otbagency5@gmail.com*
"""

day2_content = """# 👑 OTB Growth Academy — Sprint Day 02
## محرك الكرييتف الإعلاني والكوبي رايتنج وسيكولوجية الفيديو القصير (Creative Engine & Viral Copywriting)

> **شعار وكالة OTB:** *"استراتيجيات جريئة.. نتائج حقيقية | Bold Strategies. Real Results"*  
> **الهتاف والتموضع:** *"We Are OTB — The City Kings" 👑*  
> **المستهدفون:** صناع المحتوى (Content Creators)، كتاب الإعلانات (Copywriters)، مصممو الجرافيك والموشن (Designers & Video Editors).  
> **المدة المقررة:** 90 دقيقة تدريبية + 45 دقيقة ورشة كتابة وإنتاج.

---

### 🎯 1. أهداف جلسة اليوم الثاني (Learning Objectives)
1. إتقان صياغة الإعلانات التحويلية باستخدام معادلات **AIDA**, **PAS**, و **BAB**.
2. تطبيق **قاعدة الثواني الـ 3 الأولى (The 3-Second Hook Rule)** في الفيديوهات القصيرة (Reels, TikTok, Shorts).
3. بناء **مصفوفة المحتوى الرباعية (The 4-Quadrant Content Matrix)** للجمع بين التفاعل الفيروسي والمبيعات المباشرة.
4. كتابة اسكريبتات إعلانية مخصصة لقطاعات المطاعم والتجارة الإلكترونية ترفع معدل المشاهدة للاكتمال (Retention & Hold Rate).

---

### ✍️ 2. نماذج الكوبي رايتنج الإعلاني المعتمدة في OTB

#### أ. نموذج PAS (Problem - Agitation - Solution)
*مثال تطبيقي لقطاع المطاعم / البرجر:*
* **Problem (المشكلة):** "تعبت من ساندوتشات البرجر اللي كلها عيش واللحمة ملهاش طعم؟"
* **Agitation (تهويل المشكلة):** "بتدفع مبلغ محترم وفي الآخر بيجيلك بارد والجبنة مجلدة وتندم على فلوس الخروجة."
* **Solution (الحل الحصري):** "في Rancho's مش بنعمل برجر عادي.. قطمة واحدة من الـ Smoked Double Beef بالصوص السري وهتعرف يعني إيه برجر ملوك حقيقي. اطلب دلوقتي العرض الملكي من اللينك ويوصلك سخن نار!"

#### ب. نموذج AIDA (Attention - Interest - Desire - Action)
* **Attention (الهوك الخاطف):** "سر ما بيقولهوش غير رواد الأعمال الكبار في شرب القهوة!"
* **Interest (بناء الفضول):** "الفرق بين يوم عادي ويوم بتنتج فيه بتركيز 100% هو جودة حبة البن وتحميصتها."
* **Desire (خلق الرغبة):** "في MIX Coffee وفرنالك حبوب البن المختص الإثيوبي المحمصة طازة في نفس الأسبوع عشان تاخد جرعة طاقتك صح."
* **Action (التحفيز على الفعل):** "زور أقرب فرع ليك النهارده أو اطلب الباكت الأونلاين وخد شحن مجاني لأول طلب!"

---

### 🎬 3. تشريح الفيديو الفيرال الناجح (Viral Reel Anatomy)

```mermaid
flowchart LR
    Hook["0-3 ثواني<br>Visual & Audio Hook"] --> Story["3-15 ثانية<br>The Core Value & Drama"]
    Story --> Offer["15-25 ثانية<br>The Irresistible Offer"]
    Offer --> CTA["25-30 ثانية<br>Clear Direct Call-to-Action"]
```

#### مؤشرات أداء الفيديو الإعلاني التي نقيسها:
1. **Hook Rate (3s Views / Impressions):** الهدف أكثر من **35%**.
2. **Hold Rate (ThruPlays / Impressions):** الهدف أكثر من **15%**.
3. **Outbound CTR:** الهدف أكثر من **2.5%** للإعلانات الممولة.

---

### 🛠️ 4. التكليف التطبيقي الفوري (Day 2 Team Workshop)
* **المطلوب من الفريق:**
  1. كتابة 3 نصوص إعلانية بـ 3 زوايا مختلفة (زاوية فكاهية، زاوية خوف من الفوات FOMO، زاوية فخامة اجتماعية).
  2. تصميم اسكريبت ستوري بورد (Storyboard Script) لريل مدته 20 ثانية جاهز للتصوير والمونتاج.

---
**OTB Agency — We Are The City Kings 👑**
"""

day3_content = """# 👑 OTB Growth Academy — Sprint Day 03
## ميديا بايينج الأداء على ميتا وتيك توك وسكيلينج الـ ROAS (Performance Media Buying & Scaling)

> **شعار وكالة OTB:** *"استراتيجيات جريئة.. نتائج حقيقية | Bold Strategies. Real Results"*  
> **الهتاف والتموضع:** *"We Are OTB — The City Kings" 👑*  
> **المستهدفون:** ميديا بايرز (Media Buyers)، مسؤولو الحملات الممولة، ومدراء الحسابات.  
> **المدة المقررة:** 90 دقيقة تدريبية + 45 دقيقة تحليل حسابات إعلانية مباشرة.

---

### 🎯 1. أهداف جلسة اليوم الثالث (Learning Objectives)
1. بناء الهيكل الحسابي الإعلاني المتقدم **(Account Architecture: CBO vs ABO & Advantage+)**.
2. ضبط التتبع الرقمي المتقدم عبر **Conversions API (CAPI) & Pixel Setup** وحل أزمة تتبع iOS 14.5+.
3. حساب وإدارة معادلات الجدوى المالية: **ROAS, CPA, CAC, AOV, LTV, Contribution Margin**.
4. تطبيق استراتيجيات الـ Scaling بنوعيها: **التوسع الرأسي (Vertical Scaling)** و**التوسع الأفقي (Horizontal Scaling)** للوصول إلى ميزانيات تفوق \$10,000 شهرياً بأمان.

---

### 📈 2. هيكل الحملات الإعلانية المعتمد في OTB (Full-Funnel Media Buying)

```mermaid
graph TD
    subgraph TOFU ["Top of Funnel: البارد (Cold Traffic) - 60% الميزانية"]
        A1[Advantage+ Shopping / Broad Targeting]
        A2[Interest Stacks: High-Intent Niches]
        A3[Lookalikes: 1%-3% Top Buyers]
    end
    subgraph MOFU ["Middle of Funnel: الدافئ (Engaged Audience) - 25% الميزانية"]
        B1[Social Engagers 90 Days Meta/TikTok]
        B2[Video Viewers 50%+ Retention]
    end
    subgraph BOFU ["Bottom of Funnel: الحار (High Intent) - 15% الميزانية"]
        C1[Website Visitors 30 Days]
        C2[View Content & Add to Cart Abandoners]
    end
```

---

### 🧮 3. الرياضيات المالية للميديا باير المحترف (Media Buying Financial Formulas)

1. **العائد على الإنفاق الإعلاني (ROAS):**
   $$\\text{ROAS} = \\frac{\\text{Total Revenue Generated from Ads}}{\\text{Total Ad Spend}}$$
2. **نقطة التعادل الإعلانية (Break-Even ROAS):**
   $$\\text{BE ROAS} = \\frac{1}{\\text{Gross Profit Margin %}}$$
3. **تكلفة الاستحواذ على العميل (CAC):**
   $$\\text{CAC} = \\frac{\\text{Total Ad Spend} + \\text{Direct Acquisition Costs}}{\\text{Total New Customers Acquired}}$$

---

### ⚡ 4. شجرة قرارات سكيلينج الحملات (Scaling Decision Tree)

* **متى نقوم بالـ Scaling؟**
  * إذا كان الـ ROAS أعلى من الـ Target بنسبة **25%+** لمدة **3 أيام متتالية**.
  * إذا كان معدل الـ Frequency أقل من **2.2** في حملات الـ TOFU.
* **كيف نقوم بالـ Scaling؟**
  * **Vertical:** زيادة الميزانية بمقدار **20% كل 48-72 ساعة** لمنع إعادة دخول الحملة في مرحلة التعلم (Learning Phase).
  * **Horizontal:** مضاعفة الحملة الرابحة وفتح الاستهداف الواسع (Broad) مع اختبار 3 زوايا إبداعية جديدة (New Creatives).

---

### 🛠️ 5. التكليف التطبيقي الفوري (Day 3 Team Workshop)
* **المطلوب من كل ميديا باير:**
  1. مراجعة حساب إعلاني نشط لأحد عملاء OTB وتدقيق جودة مطابقة الأحداث (Event Match Quality) للـ CAPI.
  2. إعداد مصفوفة الميزانية الأسبوعية وجدول الـ Testing & Scaling لعميل مستهدف.

---
**OTB Agency — We Are The City Kings 👑**
"""

day4_content = """# 👑 OTB Growth Academy — Sprint Day 04
## الذكاء الاصطناعي التسويقي وهندسة الأوامر وأتمتة الليدز (AI Marketing & Growth Automation)

> **شعار وكالة OTB:** *"استراتيجيات جريئة.. نتائج حقيقية | Bold Strategies. Real Results"*  
> **الهتاف والتموضع:** *"We Are OTB — The City Kings" 👑*  
> **المستهدفون:** جميع أعضاء الفريق ورؤساء الأقسام (Cross-Functional).  
> **المدة المقررة:** 90 دقيقة تدريبية + 45 دقيقة تطبيق أوامر AI وبناء مسار أتمتة.

---

### 🎯 1. أهداف جلسة اليوم الرابع (Learning Objectives)
1. إتقان إطار هندسة الأوامر المتقدم **(RCIC Framework: Role, Context, Instruction, Constraint)**.
2. أتمتة دورة إنتاج المحتوى المرئي والإعلاني باستخدام أدوات الـ AI الحديثة (Midjourney, Gemini, Claude).
3. ربط وتفعيل قنوات المراسلة المباشرة عبر **WhatsApp Business API & Chatbots** لتحويل المحادثات إلى مبيعات فورية.
4. إعداد مسارات استعادة السلات المتروكة (Abandoned Cart Automation) بالبريد والواتساب لتحقيق 20%+ مبيعات إضافية مسترجعة.

---

### 🤖 2. إطار هندسة الأوامر المعتمد في OTB (RCIC Prompting Architecture)

| العنصر | الغرض والتعريف | مثال تطبيقي لكتابة إعلان لـ OTB |
|---|---|---|
| **Role (الدور)** | تحديد هوية الذكاء الاصطناعي وخبرته | "أنت Head of Copywriting و Growth Marketer خبير بخبرة 10 سنوات في السوق المصري." |
| **Context (السياق)** | تزويد النموذج بخلفية البيزنس والجمهور | "العميل هو مطعم برجر فاخر (Rancho's) يستهدف الشباب في القاهرة بمتوسط دخل مرتفع." |
| **Instruction (التعليمات)** | المهمة المطلوب تنفيذها بدقة | "اكتب 3 اسكريبتات لريلز قصيرة مدتها 15 ثانية تركز على الطعم الملحمي والصوصات الخاصة." |
| **Constraint (القيود)** | المحددات والشروط والممنوعات | "ممنوع استخدام عبارات مبتذلة مثل (أشهى المأكولات)؛ النبرة يجب أن تكون جريئة وثقة ملكية بالعامية المصرية الراقية." |

---

### 💬 3. مسار أتمتة الـ WhatsApp Business API لعملاء OTB

```mermaid
flowchart TD
    AdClick[الضغط على إعلان Click-to-WhatsApp] --> Welcome[رسالة ترحيب مخصصة باسم البراند]
    Welcome --> Qualifying[سؤال تأهيلي: تصنيف العميل / القائمة المفضلة]
    Qualifying --> Catalog[إرسال رابط الكتالوج أو العرض الملكي]
    Catalog --> Order[إتمام الطلب وتسجيل البيانات]
    Order --> SyncCRM[مزامنة الليد فوراً مع CoreLink CRM / Google Sheets]
    Order --> Followup[إشعار تقييم الخدمة بعد ساعتين]
```

---

### 🛠️ 4. التكليف التطبيقي الفوري (Day 4 Team Workshop)
* **المطلوب من كل قسم:**
  1. تجربة 3 أوامر RCIC من دليل **OTB Prompt Engineering Bible** لإنتاج محتوى وإعلانات عميل حقيقي.
  2. رسم مخطط مسار أتمتة رسائل ترحيبية وعروض ترويجية عبر WhatsApp API لأحد عملاء الوكالة.

---
**OTB Agency — We Are The City Kings 👑**
"""

day5_content = """# 👑 OTB Growth Academy — Sprint Day 05
## الانضباط التشغيلي وإدارة المشاريع وعقود الريتينر الشهرية (Operations, CRM SOPs & Retainers)

> **شعار وكالة OTB:** *"استراتيجيات جريئة.. نتائج حقيقية | Bold Strategies. Real Results"*  
> **الهتاف والتموضع:** *"We Are OTB — The City Kings" 👑*  
> **المستهدفون:** الإدارة العليا، مدراء الحسابات (Account Managers)، وقادة الفرق (Team Leads).  
> **المدة المقررة:** 90 دقيقة تدريبية + 45 دقيقة ورشة محاكاة إغلاق الصفقات وإسناد المهام.

---

### 🎯 1. أهداف جلسة اليوم الخامس (Learning Objectives)
1. القضاء التام على **متلازمة التوجيه الفارغ (Empty Brief Syndrome)** وخفض نسبة إعادة العمل (Rework Rate) بأكثر من 40%.
2. تطبيق إجراءات العمل القياسية (SOPs) داخل **CoreLink CRM** ونظام **ClickUp** لإدارة المشاريع بسلاسة تامة.
3. تفعيل قواعد الـ **SLA (اتفاقيات مستوى الخدمة)** ونظام تصعيد المهام المتأخرة لمنع تراكم المهام.
4. إتقان استراتيجيات بيع وإغلاق **عقود الريتينر الشهرية (\$1,500 - \$3,000)** وضمان استمرارية العميل لأكثر من 12 شهراً.

---

### 📋 2. دورة التشغيل القياسية داخل OTB (The 4-Stage Operational Cycle)

```mermaid
flowchart LR
    Stage1["1. Briefing & Delegation<br>بريف كامل إلزامي + تبعيات مقفولة"] --> Stage2["2. Execution & Tracking<br>تنفيذ بتايمر حقيقي + رفع لـ Cloudflare R2"]
    Stage2 --> Stage3["3. Review & QA<br>مراجعة خلال 24 ساعة كحد أقصى"]
    Stage3 --> Stage4["4. Delivery & Retainer<br>تسليم للعميل وتقرير أداء شهري"]
```

#### ركائز منع الهدر التشغيلي:
1. **لا مهمة بدون بريف إلزامي:** يُمنع بدء أي تصميم أو كتابة أو ميديا بايينج بناءً على رسائل واتساب شفهية.
2. **Sequential Locking:** لا تبدأ مرحلة التصميم إلا بعد اعتماد نص الكوبي رايتنج بنسبة 100%.
3. **قاعدة الـ 24 ساعة:** كل مراجعة يجب أن تتم خلال 24 ساعة، وإذا تجاوزت 48 ساعة تُصعد تلقائياً للإدارة.

---

### 💼 3. باقات وعقود الريتينر الشهرية في OTB (Retainer Tiers)

| الباقة (Package) | السعر المقترح | الخدمات المشمولة | الجمهور المستهدف |
|---|---|---|---|
| **Growth Starter** | \$1,200 / شهر | إدارة صفحتين + 12 بوست/ريل + إدارة ميزانية إعلانية حتى \$2,000 | المشاريع الناشئة والمطاعم الفردية |
| **Dominance Retainer 👑** | \$2,500 / شهر | هوية كاملة + 24 بوست/ريل بجودة عالية + ميديا بايينج متقدم + أتمتة واتساب + تقرير أسبوعي | البراندات المتوسطة وسلاسل المطاعم |
| **Enterprise Scale** | \$4,500+ / شهر | Full-Stack Growth Engine + إنتاج مرئي 3D + استشارات استراتيجية أسبوعية + دعم مخصص 24/7 | الشركات الكبرى ومتاجر التجارة الإلكترونية الضخمة |

---

### 🏆 4. مشروع ختام المعسكر (Sprint Capstone Action)
* **تسليم كل عضو بالفريق:**
  1. ملف تدقيق شامل لمهامه في CoreLink CRM وتحديث كافة الـ SOPs الخاصة بدوره.
  2. تقديم خطة نمو شهرية مصغرة متكاملة لعميل حقيقي تتضمن (الاستراتيجية، عينة المحتوى، خطة الإعلانات، ومسار الأتمتة).

---
**OTB Agency — We Are The City Kings 👑**
"""

# ==========================================
# 2. CHEATSHEETS & SOP TEMPLATES
# ==========================================

prompt_bible = """# 👑 OTB Prompt Engineering Bible
## موسوعة الأوامر التكتيكية المتقدمة لفرق عمل وكالة OTB

> **شعار الوكالة:** *"Bold Strategies. Real Results"* | *"We Are OTB — The City Kings"* 👑  
> **الإصدار:** 2026.1 M-Core

---

### 1. أوامر فريق كتابة المحتوى والإعلانات (Copywriters & Content Creators)

#### 📝 أمر 1: كتابة إعلان تحويلي بصيغة PAS لمطاعم F&B
```text
Role: You are a senior direct-response copywriter for OTB Agency, specializing in high-converting food & beverage marketing in Egypt.
Context: We are running Meta & TikTok ads for [Brand Name], a premium burger brand known for [Unique Feature, e.g., smoked brisket patties and secret melted cheese sauce]. Target audience: Young adults (18-34) in Cairo who love foodie experiences.
Task: Write 3 ad variations using the PAS (Problem-Agitation-Solution) framework in engaging, modern Egyptian Arabic (عامية راقية وجريئة).
Constraints:
- Hook must be under 8 words.
- Do not use clichéd words like 'أشهى المأكولات' or 'طعم لا يقاوم'.
- Include a strong scarcity/urgency Call To Action linking to our WhatsApp ordering menu.
- Provide a clear headline and Primary Text format.
```

#### 📝 أمر 2: اسكريبت فيديو ريلز 15 ثانية بأسلوب Storytelling
```text
Role: Master viral short-form video director and scriptwriter for OTB Agency.
Context: Creating an Instagram Reel / TikTok for [Brand Name, e.g., Specialty Coffee Shop].
Task: Write a shot-by-shot 15-second script with:
1. Seconds 0-3: A visual and auditory scroll-stopping hook.
2. Seconds 3-10: Quick-cut B-roll actions showing product craftsmanship and ASMR sound design.
3. Seconds 10-15: Direct, irresistible offer and CTA.
Format: Table with columns [Time (Sec), Visual Scene, Sound / Audio Effect, On-Screen Text / Voiceover].
```

---

### 2. أوامر فريق الميديا بايينج وهندسة النمو (Media Buyers & Growth Engineers)

#### 📊 أمر 3: تحليل نتائج الحملات واستخراج فرص السكيلينج
```text
Role: Principal Media Buyer and Growth Architect at OTB Agency.
Context: Here are our last 7 days of campaign performance data for [Client Name]:
- Ad Spend: $[Amount]
- Impressions: [Number]
- Link Clicks: [Number] (CTR: [Percentage]%)
- Purchases: [Number]
- Revenue: $[Amount] (ROAS: [Number]x)
- CPM: $[Amount], CPC: $[Amount], CPA: $[Amount]
Task:
1. Conduct a full funnel diagnostic (diagnose Hook Rate, Click-to-Purchase conversion drop-offs, and Audience Saturation).
2. Give me a clear decision: Scale Vertically, Scale Horizontally, or Kill/Iterate Creatives.
3. Outline specific action steps for the next 48 hours to maintain ROAS > 4.0x.
```

---

### 3. أوامر فريق مدراء الحسابات واستقبال العملاء (Account Managers)

#### 💼 أمر 4: صياغة مقترح تسويقي وتنفيذي لعقد ريتينر شهري (Retainer Proposal)
```text
Role: Commercial Director at OTB Marketing Studio (The City Kings).
Context: Writing an executive marketing proposal for [Potential Client], a mid-tier [Industry] business looking to scale from $20k to $100k monthly GMV.
Task: Draft a 1-page executive summary outlining:
1. The Core Market Challenge & Competitor Blind Spots.
2. OTB's 90-Day Full-Stack Growth Roadmap (Branding -> Content Engine -> Performance Media -> WhatsApp Automation).
3. Deliverables breakdown for a $2,500/month Retainer.
4. Expected KPIs and Governance Model (Weekly dashboard + CoreLink CRM tracking).
Tone: Authoritative, elite, bold, and purely ROI-focused.
```
"""

sop_templates = """# 👑 OTB Standard Operating Procedures (SOPs) & Briefing Templates
## نماذج التوجيه الإلزامي لفرق العمل لمنع الهدر التشغيلي

---

### 📋 قالب 1: بريف صناعة المحتوى والكوبي رايتنج (Content Brief)
* **اسم العميل / المشروع:** `[Client Name]`
* **الهدف التسويقي:** `[Awareness / Engagement / Direct Conversion / Retargeting]`
* **الجمهور المستهدف (Persona):** `[Demographics & Psychographics]`
* **الزاوية الإعلانية (Angle):** `[e.g., Quality Guarantee / Price-Value / Social Proof]`
* **الصيغة المطلوبة:** `[Reel Script / Carousel 5 Slides / Single Image Ad / WhatsApp Drip]`
* **الـ Hook الإلزامي:** `[Must be specified by Account Manager / Strategist]`
* **الـ CTA ورابط التحويل:** `[Direct Link / Phone / WhatsApp URL]`
* **الديدلاين وتاريخ النشر:** `[Date & Time]`

---

### 🎨 قالب 2: بريف التصميم والموشن جرافيك (Design & Motion Brief)
* **اسم العميل والمشروع:** `[Client Name]`
* **المقاسات المطلوبة:** `[1080x1920 (9:16) / 1080x1080 (1:1) / 1200x628]`
* **النص المعتمد 100% (Approved Copy):** `[Insert finalized Arabic/English copy here - No design starts without approved copy]`
* **المرجع البصري (Moodboard / Reference Links):** `[Attach 2-3 visual references]`
* **الأصول المطلوبة من العميل (Assets):** `[Raw Photos / 3D Packshots / Brand Fonts]`
* **ملاحظات الحركة والمؤثرات الصوتية (For Video):** `[Fast pacing, dynamic typography, sound effects on cuts]`
* **موقع التسليم:** `[Cloudflare R2 Link inside CoreLink CRM]`

---

### 🎯 قالب 3: بريف إطلاق الحملات الممولة (Media Buying Brief)
* **اسم الحساب الإعلاني:** `[Meta / TikTok / Google]`
* **نوع الحملة:** `[Sales / Leads / App Installs / Engagement]`
* **الميزانية اليومية / الشهرية:** `[$ Amount / EGP Amount]`
* **استراتيجية الشراء:** `[CBO / ABO / Advantage+ Shopping]`
* **الاستهداف (Targeting):** `[Broad / Stacked Interests / Lookalikes %]`
* **الأحداث والتتبع (Tracking):** `[Pixel ID + CAPI Verified - Deduplication active]`
* **معايير النجاح (Target KPIs):** `[Target CPA: $X | Target ROAS: X.X]`
"""

media_buying_checklist = """# 👑 OTB Media Buying Pre-Flight Checklist & Scaling Guide
## الدليل التنفيذي قبل إطلاق ومتابعة وسكيلينج الإعلانات الممولة

---

### ✈️ المرحلة 1: التدقيق الفني قبل الإطلاق (Pre-Launch Checklist)
- [ ] التأكد من عمل **Meta Pixel** و **Conversions API (CAPI)** ومطابقة الأحداث بجودة > 8.0/10.
- [ ] تفعيل التحقق من النطاق (Domain Verification) وضبط 8 أحداث قياسية في Aggregated Event Measurement.
- [ ] التأكد من سلامة روابط الهبوط وسرعة تحميل الصفحة على الموبايل (< 2.5 ثانية).
- [ ] فحص نصوص الإعلانات والتأكد من خلوها من أي كلمات محظورة في سياسات Meta/TikTok.
- [ ] مطابقة رسالة الترحيب في إعلانات Click-to-WhatsApp مع العرض الترويجي.

---

### 🔍 المرحلة 2: التدقيق اليومي أثناء التشغيل (Daily Optimization)
1. فحص مقياس **Hook Rate (3-sec views / Impressions)**: إذا كان < 25%، يجب تغيير الثواني الثلاث الأولى فوراً.
2. فحص مقياس **Hold Rate (ThruPlays / Impressions)**: إذا كان < 10%، يجب تسريع إيقاع المونتاج وتغيير النص في المنتصف.
3. فحص **Cost Per Link Click (CPC)** و **Outbound CTR**: إذا كان CTR < 1.5%، الإعلان لا يولد رغبة حقيقية في الشراء.
4. مراجعة تكرار الإعلان (**Frequency**): إذا تجاوز 3.0 في الجماهير الباردة، يجب إدخال كرييتفز جديدة.

---

### 🚀 المرحلة 3: قواعد السكيلينج الصارمة (Scaling Rules)
* **قاعدة الـ 20%:** لا ترفع ميزانية الحملة الرابحة بأكثر من 20% في المرة الواحدة كل 48 ساعة.
* **قاعدة الـ 3 أيام:** لا تحكم على نجاح أو فشل إعلان من أول 24 ساعة؛ انتظر اكتمال 50 حدث تحويل (Optimization Window).
* **إغلاق الإعلانات الخاسرة:** أي Ad Set يتجاوز إنفاقه 2x Target CPA بدون أي تحويل يتم إيقافه فوراً.
"""

# ==========================================
# 3. TRACK B: 4-WEEK FULL-SPECTRUM MASTERCLASS
# ==========================================

week1_masterclass = """# 👑 OTB Masterclass — Week 01
## المرحلة 1: التموضع الاستراتيجي وأبحاث السوق وبناء العلامات التجارية الكبرى

> **البرنامج الأكاديمي:** *OTB Full-Spectrum Growth Masterclass*  
> **المدة:** الأسبوع الأول (4 محاضرات تخصصية + ورشة تحليل أسواق).  
> **المصادر المرجعية المعتمدة:** `[SRC-0003, SRC-0004, SRC-0038, SRC-0043]`

---

### 📚 الوحدات الدراسية للأسبوع الأول:
* **الوحدة 01: مبادئ التسويق الاستراتيجي وبحوث السوق (Market Research & Consumer Psychology)**
  * تحليل البيئة الكلية PESTEL والبيئة التنافسية بمصفوفة Porter's Five Forces.
  * هيكلة أبحاث السوق الميدانية والرقمية واستخراج الـ Consumer Insights.
* **الوحدة 02: استراتيجيات البراندنج وبناء الهوية ونبرة الصوت (Brand Identity & Archetypes)**
  * الفلسفة الملكية لهوية OTB (The Ruler & Creator Framework).
  * بناء Brand Book متكامل يشمل لوحة الألوان، الخطوط، الرسائل، والمحددات البصرية.

---

### 🧪 ورشة العمل الأسبوعية (Weekly Applied Lab):
بناء ملف استراتيجي شامل (Market Positioning Bible) لأحد عملاء قطاع الأغذية أو المتاجر الإلكترونية مع تحليل 5 منافسين وتحديد الفجوات السعرية والتسويقية.
"""

week2_masterclass = """# 👑 OTB Masterclass — Week 02
## المرحلة 2: محرك الكرييتف، الكوبي رايتنج الفيرال، والسيو التنافسي

> **البرنامج الأكاديمي:** *OTB Full-Spectrum Growth Masterclass*  
> **المدة:** الأسبوع الثاني (4 محاضرات تخصصية + ستوديو إنتاج مرئي).  
> **المصادر المرجعية المعتمدة:** `[SRC-0005, SRC-0039, SRC-0040, SRC-0041]`

---

### 📚 الوحدات الدراسية للأسبوع الثاني:
* **الوحدة 03: استراتيجيات صناعة المحتوى والكوبي رايتنج الإعلاني (Copywriting Mastery)**
  * صياغة العروض التي لا تقاوم (Irresistible Offers & Grand Slam Offers).
  * هندسة جداول النشر وتوزيع المحتوى على مدار 90 يوماً.
* **الوحدة 04 & 05: تحسين محركات البحث الأساسي والتقني (SEO Foundations & Technical SEO)**
  * تحليل نية البحث (Search Intent) وبحث الكلمات المفتاحية للمواقع المحلية.
  * السيو الداخلي (On-Page) وتنسيق بنية المقالات وبناء الروابط الخلفية القوية (Backlinks).

---

### 🧪 ورشة العمل الأسبوعية (Weekly Applied Lab):
إنتاج حقيبة إعلانية مرئية كاملة (10 بوستات + 4 ريلز + مقال سيو متوافق مع خوارزميات جوجل 2026).
"""

week3_masterclass = """# 👑 OTB Masterclass — Week 03
## المرحلة 3: ميديا بايينج الأداء، قرصنة النمو، وسكيلينج العوائد (ROAS Mastery)

> **البرنامج الأكاديمي:** *OTB Full-Spectrum Growth Masterclass*  
> **المدة:** الأسبوع الثالث (4 محاضرات تخصصية + محاكاة إدارة ميزانيات ضخمة).  
> **المصادر المرجعية المعتمدة:** `[SRC-0031, SRC-0033, SRC-0037, SRC-0042]`

---

### 📚 الوحدات الدراسية للأسبوع الثالث:
* **الوحدة 06 & 07: إعلانات Meta و TikTok وقنوات B2B (Performance Media Buying)**
  * بناء الحملات، تتبع CAPI، وهندسة الجمهور المشابه (Lookalike Audiences).
  * التسويق الاحترافي عبر لينكد إن وإكس وبناء شبكات العلاقات الاستثمارية.
* **الوحدة 08 & 09: الجروث هاكينج ومنظومة الـ AARRR وسكيلينج الميزانيات**
  * مصفوفة أولويات التجارب (ICE Framework: Impact, Confidence, Ease).
  * التوسع بالميزانيات الإعلانية من \$1,000 إلى \$50,000 بأمان كامل.

---

### 🧪 ورشة العمل الأسبوعية (Weekly Applied Lab):
إعداد خطة إطلاق حملة ممولة بميزانية \$5,000 شهرياً لعميل تجارة إلكترونية مع مصفوفة توقعات العائد والـ ROAS.
"""

week4_masterclass = """# 👑 OTB Masterclass — Week 04
## المرحلة 4: أتمتة الذكاء الاصطناعي، تكامل CRM، ومشروع التخرج الشامل 360°

> **البرنامج الأكاديمي:** *OTB Full-Spectrum Growth Masterclass*  
> **المدة:** الأسبوع الرابع (4 محاضرات تخصصية + تقييم مشروع التخرج).  
> **المصادر المرجعية المعتمدة:** `[SRC-0002, SRC-0006, SRC-0032, SRC-0036]`

---

### 📚 الوحدات الدراسية للأسبوع الرابع:
* **الوحدة 10 & 11: أتمتة الذكاء الاصطناعي والتسويق بالبريد والواتساب (AI & Funnel Automation)**
  * بناء Funnels متكاملة للواتساب والإيميل لاستعادة المبيعات المفقودة وتأهيل العملاء.
* **الوحدة 12 & 13: الانضباط التشغيلي، CRM، وإدارة عقود الوكالة (Agency Mastery & Retainers)**
  * إدارة العمليات عبر CoreLink CRM و ClickUp، وإغلاق عقود الريتينر الشهرية (\$1,500 - \$3,000).

---

### 🎓 مشروع التخرج الشامل (The 360° Capstone Growth Engine):
تسليم خطة نمو وتسويق استراتيجية متكاملة لبراند حقيقي تشمل كافة الجوانب (من أبحاث السوق حتى أرقام الـ ROAS والأتمتة وعرض الـ Pitch Deck التنفيذي).
"""

capstone_brief = """# 👑 OTB 360° Capstone Growth Engine — Final Brief & Rubric
## مواصفات ومعايير تقييم مشروع التخرج الشامل لأكاديمية OTB

---

### 🎯 متطلبات المشروع النهائي:
على كل متدرب / فريق عمل تقديم ملف تنفيذي متكامل (Master Growth Bible) يتضمن:
1. **وثيقة التموضع الاستراتيجي:** تحليل STP، الهوية، ونبرة الصوت للبراند.
2. **محرك المحتوى والكرييتف:** خطة نشر لـ 30 يوماً مع 5 اسكريبتات ريلز مصورة و3 نماذج كوبي رايتنج إعلانية.
3. **هيكلة الحملات الإعلانية:** شجرة استهداف Meta/TikTok وخطة ميزانية بقيمة \$3,000+ متوقعة العائد.
4. **نظام الأتمتة:** مخطط تدفق رسائل الـ WhatsApp Business API والإيميل ماركتنج.
5. **لوحة التحكم التشغيلية:** خطة إدارة المشروع في CoreLink CRM وجدول تسليمات الـ SOPs.

---

### 📊 معايير التقييم والدرجات (Grading Rubric):

| المحور | الوزن النسبي | معيار التميز (Excellence Criteria) |
|---|---|---|
| **العمق الاستراتيجي والتموضع** | 25% | تحديد زوايا غير تقليدية ومبنية على أرقام وأبحاث سوق دقيقة. |
| **جودة الكرييتف والكوبي رايتنج** | 25% | هوكات إعلانية قوية، نصوص خالية من الحشو، وتصاميم توافق هوية البراند. |
| **منطقية الميديا بايينج والأرقام** | 25% | حساب دقيق لـ ROAS, CPA, CAC مع خطة واضحة لإدارة المخاطر والسكيلينج. |
| **الأتمتة والانضباط التشغيلي** | 25% | مسارات أتمتة واقعية، قوالب بريف مكتملة، وعرض تقديمي احترافي (Pitch Deck). |
"""

weekly_quizzes = """# 👑 OTB Weekly Quizzes & Formative Assessments
## بنك الاختبارات الأسبوعية التفاعلية لتقييم استيعاب الفريق

---

### 📝 اختبار الأسبوع الأول: الاستراتيجية والبراندنج
1. **سؤال:** ما هو الفرق الجوهري بين استراتيجيات التسويق التقليدية وتموضع OTB كـ "ملوك المدينة"؟
   * أ) التركيز فقط على التصميم الجميل.
   * ب) الجمع بين الهيبة البصرية والجرأة في كسر الملل والتركيز الصارم على النتائج المالية. ✅
   * ج) الاكتفاء بالإعلانات الممولة دون بناء هوية.
2. **سؤال:** عند صياغة الـ Buyer Persona لمطعم فاخر، ما هو العنصر الأكثر أهمية؟
   * أ) السن والوظيفة فقط.
   * ب) الألم النفسي والمكانة الاجتماعية والدافع وراء تجربة الطعام. ✅
   * ج) نوع الهاتف المحمول فقط.

---

### 📝 اختبار الأسبوع الثاني: الكوبي رايتنج والكرييتف
1. **سؤال:** ما هو الهدف الأساسي من أول 3 ثوانٍ في أي فيديو ريلز إعلاني؟
   * أ) ذكر اسم الشركة وتفاصيل فروعها.
   * ب) كسر التمرير (Pattern Interrupt) وجذب انتباه المشاهد الفوري (Hook). ✅
   * ج) عرض الشعار واللوجو في المنتصف.
2. **سؤال:** في نموذج PAS للكتابة الإعلانية، ماذا يمثل حرف (A)؟
   * أ) Action (الفعل).
   * ب) Agitation (تهويل وتوضيح عواقب استمرار المشكلة). ✅
   * ج) Awareness (الوعي).

---

### 📝 اختبار الأسبوع الثالث: الميديا بايينج والأرقام
1. **سؤال:** إذا كان هامش الربح الإجمالي لمنتج هو 25%، فما هو الـ Break-Even ROAS المطلوب؟
   * أ) 2.0x
   * ب) 4.0x (1 / 0.25 = 4) ✅
   * ج) 1.25x
2. **سؤال:** ما هو الحد الأقصى الآمن لزيادة ميزانية الحملة الإعلانية الرابحة (Vertical Scaling)؟
   * أ) مضاعفتها 100% يومياً.
   * ب) زيادة 20% كل 48-72 ساعة لمنع اضطراب الخوارزمية. ✅
   * ج) لا توجد أي حدود.

---

### 📝 اختبار الأسبوع الرابع: الذكاء الاصطناعي والأتمتة
1. **سؤال:** في إطار RCIC لهندسة الأوامر، ما الذي يضمن عدم استخدام الذكاء الاصطناعي لعبارات مبتذلة؟
   * أ) Role
   * ب) Context
   * ج) Constraints (القيود والشروط الواضحة). ✅
2. **سؤال:** ما هي الفائدة المباشرة لربط الـ WhatsApp Business API بإعلانات Click-to-WhatsApp؟
   * أ) تقليل تكلفة إعلانات جوجل.
   * ب) فتح محادثة فورية مخصصة وتحويل الليد إلى طلب شراء مسجل في ثوانٍ. ✅
   * ج) زيادة عدد المتابعين فقط.
"""

# ==========================================
# WRITE TRACK A & B FILES
# ==========================================

print("Writing Track A files...")
with open(os.path.join(BASE_DIR, "track_a_fast_track_sprint", "Day_01_Strategic_Market_Analysis_&_Brand_Positioning.md"), "w", encoding="utf-8") as f:
    f.write(day1_content)
with open(os.path.join(BASE_DIR, "track_a_fast_track_sprint", "Day_02_Creative_Engine_Copywriting_&_Short_Form_Video.md"), "w", encoding="utf-8") as f:
    f.write(day2_content)
with open(os.path.join(BASE_DIR, "track_a_fast_track_sprint", "Day_03_Performance_Media_Buying_Meta_Ads_&_Pixel_CAPI.md"), "w", encoding="utf-8") as f:
    f.write(day3_content)
with open(os.path.join(BASE_DIR, "track_a_fast_track_sprint", "Day_04_AI_Marketing_Tactical_Prompts_&_Lead_Gen_Automation.md"), "w", encoding="utf-8") as f:
    f.write(day4_content)
with open(os.path.join(BASE_DIR, "track_a_fast_track_sprint", "Day_05_Operational_Discipline_CoreLink_SOPs_&_Client_Retainers.md"), "w", encoding="utf-8") as f:
    f.write(day5_content)

with open(os.path.join(BASE_DIR, "track_a_fast_track_sprint", "cheatsheets", "OTB_Prompt_Engineering_Bible.md"), "w", encoding="utf-8") as f:
    f.write(prompt_bible)
with open(os.path.join(BASE_DIR, "track_a_fast_track_sprint", "cheatsheets", "OTB_Media_Buying_Checklist.md"), "w", encoding="utf-8") as f:
    f.write(media_buying_checklist)
with open(os.path.join(BASE_DIR, "track_a_fast_track_sprint", "cheatsheets", "OTB_SOP_Briefing_Templates.md"), "w", encoding="utf-8") as f:
    f.write(sop_templates)

print("Writing Track B files...")
with open(os.path.join(BASE_DIR, "track_b_4week_masterclass", "Week_01_Foundations_STP_&_Brand_Identity.md"), "w", encoding="utf-8") as f:
    f.write(week1_masterclass)
with open(os.path.join(BASE_DIR, "track_b_4week_masterclass", "Week_02_Content_Virality_SEO_&_Creative_Production.md"), "w", encoding="utf-8") as f:
    f.write(week2_masterclass)
with open(os.path.join(BASE_DIR, "track_b_4week_masterclass", "Week_03_Paid_Acquisition_Scaling_&_Growth_Experimentation.md"), "w", encoding="utf-8") as f:
    f.write(week3_masterclass)
with open(os.path.join(BASE_DIR, "track_b_4week_masterclass", "Week_04_AI_Automation_CRM_Integration_&_Capstone_Engine.md"), "w", encoding="utf-8") as f:
    f.write(week4_masterclass)

with open(os.path.join(BASE_DIR, "track_b_4week_masterclass", "assessments", "OTB_Weekly_Quizzes_&_Rubrics.md"), "w", encoding="utf-8") as f:
    f.write(weekly_quizzes)
with open(os.path.join(BASE_DIR, "track_b_4week_masterclass", "assessments", "OTB_360_Capstone_Brief_&_Evaluation.md"), "w", encoding="utf-8") as f:
    f.write(capstone_brief)

print("Track A & B files created successfully!")
