import os
import shutil
import json

BASE_DIR = "/Users/ahmedissamramadan/.gemini/antigravity/scratch/otb-growth-academy"
DOWNLOADS_DIR = "/Users/ahmedissamramadan/Downloads/Materials/OTB_GROWTH_ACADEMY"

# ==============================================================================
# 19 COMPREHENSIVE COURSE CURRICULA
# ==============================================================================
COURSES_DATA = [
    {
        "id": "ai-marketing",
        "cat": "ai",
        "phase": 4,
        "title": "الذكاء الاصطناعي في التسويق الرقمي (AI in Marketing)",
        "pages": 294,
        "icon": "🤖",
        "badge": "GenAI & Prompt Engineering",
        "desc": "توظيف نماذج الذكاء الاصطناعي التوليدي (ChatGPT, Claude, Midjourney) وهندسة الأوامر المتقدمة (RCIC) في صناعة المحتوى، تحليل البيانات الإعلانية، وأتمتة مسارات البيع.",
        "units": [
            "مقدمة في الثورة التوليدية (Generative AI) وتطبيقاتها في صناعة الإعلانات",
            "إطار هندسة الأوامر التسويقية المتقدمة: Role - Context - Instruction - Constraints (RCIC)",
            "توليد الأفكار الإعلانية وسيناريوهات الفيديو الفيرال في ثوانٍ",
            "التصوير التجاري وتوليد أصول الجرافيك و 3D عبر Midjourney & Stable Diffusion",
            "أتمتة خدمة العملاء وتأهيل الليدز عبر WhatsApp Business API و Chatbots",
            "التحليل التنبؤي للبيانات وسلوك العملاء والتنبؤ بالقيمة العمرية (LTV)"
        ],
        "prompt": "Role: Principal AI Growth Engineer at OTB Agency.\nContext: Designing an autonomous multi-modal marketing workflow for [Brand Name] in [Industry].\nTask: Generate a 30-day content and high-converting ad schedule utilizing PAS and AIDA frameworks.\nConstraints: High-converting hooks, Egyptian colloquial luxury tone, direct CTA to WhatsApp.",
        "case_study": "تم بناء مسار ردود ذكي لعميل مختبرات علاج (Elag Labs) يستقبل استفسارات التحاليل، يصنف الحالة، ويحجز موعد الزيارة المنزلية تلقائياً، محققاً أكثر من 800 حجز مؤهل شهرياً.",
        "lab": "بناء برومبت مخصص من 4 أبعاد (RCIC) لإنتاج 5 إعلانات ممولة مختلفة لبراند من اختيارك."
    },
    {
        "id": "content-marketing",
        "cat": "creative",
        "phase": 2,
        "title": "تسويق المحتوى والسرد القصصي الفيرال (Content Marketing)",
        "pages": 476,
        "icon": "✍️",
        "badge": "Viral Storytelling & Copywriting",
        "desc": "أسرار صناعة المحتوى الجذاب، صياغة النصوص الإعلانية المباشرة (Direct-Response Copywriting)، وسيكولوجية الفيديو القصير (Reels & TikTok).",
        "units": [
            "سيكولوجية الانتباه وقاعدة الـ 3 ثوانٍ الأولى (Scroll-Stopping Hooks)",
            "أطر الكتابة الإعلانية المعتمدة عالمياً: AIDA, PAS, BAB, FAB",
            "بناء الركائز الإعلانية وجدول المحتوى الشهري (Content Pillars & Editorial Calendar)",
            "هندسة الفيديوهات القصيرة (Short-Form Video Anatomy): الصوت، الإيقاع، والنص على الشاشة",
            "سرد القصص العاطفي (Brand Storytelling) وتحويل المتابع العادي إلى مدافع عن البراند",
            "إعادة تدوير المحتوى (Content Repurposing) عبر منصات التواصل المتعددة"
        ],
        "prompt": "Role: Senior Direct-Response Copywriter at OTB Agency.\nContext: Launching a viral short-form video campaign for [Brand Name].\nTask: Write 3 contrasting 15-second Reel scripts (Angle 1: Humor & Relatability, Angle 2: FOMO & Urgency, Angle 3: Pure Luxury Aesthetic).\nFormat: Shot-by-shot table with Scene, Visual Action, Audio SFX, and Voiceover.",
        "case_study": "حملة فيديو ريلز لـ Rancho's EG تبرز تفاصيل تقطيع البرجر الملحمي مع صوص الجبنة، محققة أكثر من 450 ألف مشاهدة أورجانيك ورفع المبيعات بنسبة 65%.",
        "lab": "كتابة اسكريبت فيديو قصير مدته 15 ثانية يعتمد على صيغة PAS مع تفصيل لقطات الـ ASMR الصوتية."
    },
    {
        "id": "facebook-ads",
        "cat": "media",
        "phase": 3,
        "title": "إعلانات فيسبوك وميتا للأداء وسكيلينج الـ ROAS (Meta Ads)",
        "pages": 239,
        "icon": "📊",
        "badge": "Performance Media Buying",
        "desc": "الهندسة المتقدمة لإعلانات Meta، ضبط خوارزميات Advantage+، إعداد Conversions API، واستراتيجيات التوسع الرأسي والأفقي لتحقيق عائد استثمار مضاعف.",
        "units": [
            "بنية الحملات المعيارية: TOFU (الوعي الواسع) / MOFU (التفاعل) / BOFU (إعادة الاستهداف)",
            "استراتيجيات الاستهداف الحديثة: Broad Targeting vs Lookalike vs Retargeting",
            "ضبط تتبع السيرفر المتقدم: Conversions API (CAPI) وتجاوز قيود iOS 14.5+",
            "مصفوفة اختبار الكرييتف الإعلاني (Creative Testing Framework)",
            "قواعد السكيلينج الآمنة: Vertical Scaling (+20% كل 48 ساعة) و Horizontal Scaling",
            "تحليل المؤشرات المالية: CAC, CPA, MER, Break-Even ROAS, LTV"
        ],
        "prompt": "Role: Principal Media Buyer and Growth Architect at OTB Agency.\nContext: Client [Brand] with 25% profit margin running Meta Ads in Egypt.\nTask: Formulate a 48-hour scaling protocol when a creative hits 5.2x ROAS.\nFormat: Step-by-step checklist covering budget adjustments, audience duplication, and stop-loss criteria.",
        "case_study": "إعادة هيكلة حساب إعلانات مجوهرات د. زغلول (Dr. Zaghloul) بحملات Advantage+ وتتبع CAPI دقيق، مما حقق ROAS تجاوز 7.5x واستقراراً تاماً في التكلفة.",
        "lab": "حساب الـ Break-Even ROAS لمنتج بهامش ربح 30%، وتصميم خطة ميزانية أسبوعية لاختبار 6 كرييتفز جديدة."
    },
    {
        "id": "instagram-mastery",
        "cat": "creative",
        "phase": 2,
        "title": "احتراف إنستغرام وهندسة التفاعل (Instagram & Reels)",
        "pages": 199,
        "icon": "📸",
        "badge": "Visual Branding & Community",
        "desc": "تحويل الحساب إلى واجهة عرض ملكية (Visual Storefront)، إتقان خوارزمية الريلز، أتمتة الرسائل المباشرة (ManyChat & IG DM)، وبناء مجتمع مخلص.",
        "units": [
            "تحسين البروفايل الاحترافي (Bio, Highlights, Grid Aesthetic)",
            "أسرار خوارزمية الـ Reels وعوامل رفع نسبة الإكمال (Retention Rate)",
            "سيكولوجية الستوري اليومية (Story Sequences) لتحقيق مبيعات فورية",
            "أتمتة الرسائل الخاصة (Instagram DM Automation) لتحويل التعليقات لطلبات شراء",
            "التسويق عبر المؤثرين والمايكرو إنفلونسرز (Micro-Influencer Collaborations)",
            "تحليلات إنستغرام واستخراج أوقات الذروة والمحتوى الأكثر حفظاً ومشاركة"
        ],
        "prompt": "Role: Instagram Growth Strategist at OTB Agency.\nContext: Managing luxury account for [Brand Name].\nTask: Design a 7-day Instagram Story sales funnel (Days 1-2: Tease, Days 3-4: Social Proof, Day 5: Grand Offer, Days 6-7: Last Chance Urgency).",
        "case_study": "تحويل حساب MIX Coffee على إنستغرام إلى وجهة بصرية داكنة فاخرة، مما رفع تفاعل الحساب بنسبة 180% ومعدل الحفظ والمشاركة بنسبة 240%.",
        "lab": "تصميم تسلسل ستوري من 5 شرائح مع دعوة تفاعلية لإرسال رسالة خاصة للحصول على كود خصم حصري."
    },
    {
        "id": "tiktok-growth",
        "cat": "media",
        "phase": 3,
        "title": "إعلانات ونمو تيك توك وسيكولوجية الفيرال (TikTok Ads)",
        "pages": 80,
        "icon": "🎵",
        "badge": "Trends Hijacking & Spark Ads",
        "desc": "استغلال سرعة انتشار تيك توك، استهداف الجيل Z والشباب، إطلاق حملات Spark Ads، وتصميم إعلانات لا تبدو كإعلانات تقليدية (Don't Make Ads, Make TikToks).",
        "units": [
            "فهم صفحة For You Page (FYP) ومعايير انتشار الفيديو التلقائي",
            "صناعة محتوى UGC (User-Generated Content) عالي المصداقية",
            "منصة إعلانات تيك توك (TikTok Ads Manager) وإعداد البيكسل",
            "إعلانات Spark Ads واستغلال الفيديوهات الأورجانيك الرابحة",
            "سيو تيك توك (TikTok SEO) واستهداف الكلمات المفتاحية في شريط البحث",
            "تتبع التحويلات ومبيعات المتاجر الإلكترونية على تيك توك"
        ],
        "prompt": "Role: Creative TikTok Director at OTB Agency.\nContext: Creating native TikTok ads for [Product Name].\nTask: Draft 3 viral UGC concept scripts featuring unboxing, unexpected problem-solving, and funny meme twists.",
        "case_study": "حملة تيك توك لـ Wilson Crepe تعتمد على تصوير تحضير الكريب الساخن مع ترند موسيقي شائع، حققت أكثر من 600 ألف مشاهدة ومئات الطلبات في عطلة نهاية الأسبوع.",
        "lab": "صياغة فكرة إعلان تيك توك على نمط UGC مع كتابة الهوك البصري والصوتي لأول ثانيتين."
    },
    {
        "id": "linkedin-b2b",
        "cat": "strategy",
        "phase": 3,
        "title": "لينكد إن واكتساب عملاء الشركات B2B (LinkedIn Mastery)",
        "pages": 147,
        "icon": "💼",
        "badge": "B2B Lead Generation & Authority",
        "desc": "بناء العلامة التجارية الشخصية للقيادات التنفيذية، استراتيجيات الاستقطاب البارد (Cold Outreach)، ونشر المقالات والدراسات التي تجذب عقود الشركات والريتينر.",
        "units": [
            "تحسين الصفحة الشخصية التنفيذية (All-Star Profile Optimization)",
            "استراتيجية المحتوى القيادي وبناء السلطة المعرفية (Thought Leadership)",
            "استخدام LinkedIn Sales Navigator في استهداف صناع القرار",
            "رسائل الاستقطاب غير المزعجة وسرد القيمة (InMail & Direct Messaging)",
            "إعلانات لينكد إن الممولة (LinkedIn Sponsored Content & Lead Gen Forms)",
            "بناء شبكة علاقات مهنية واستقطاب شراكات وعقود وكالة طويلة الأجل"
        ],
        "prompt": "Role: B2B Growth Strategist at OTB Agency.\nContext: Reaching out to CEOs and CMOs of retail chains in Egypt & Gulf.\nTask: Write a 3-stage cold LinkedIn outreach sequence focusing on high-ROI marketing infrastructure and waste elimination.",
        "case_study": "استقطاب 4 عقود ريتينر كبرى لـ OTB Agency عبر منشورات دراسات الحالة التحليلية لنتائج العملاء على لينكد إن.",
        "lab": "صياغة رسالة تواصل احترافية على لينكد إن موجهة لمدير تسويق شركة تجارة إلكترونية تقترح تدقيقاً مجانياً لحسابهم الإعلاني."
    },
    {
        "id": "strategy-planning",
        "cat": "strategy",
        "phase": 1,
        "title": "الاستراتيجية والتخطيط التسويقي الشامل (Marketing Strategy)",
        "pages": 124,
        "icon": "🎯",
        "badge": "STP, SOSTAC & 90-Day Blueprints",
        "desc": "المنهجية المعتمدة لبناء خطط التسويق المتكاملة، دراسة السوق والمنافسين، نموذج SOSTAC، وتحويل الأهداف العامة إلى مؤشرات أداء رقمية قابلة للقياس.",
        "units": [
            "تحليل الوضع الراهن وتدقيق العلامة التجارية (SWOT & PESTLE Analysis)",
            "نموذج STP العملي: Segmentation, Targeting, Positioning",
            "إطار التخطيط الاستراتيجي SOSTAC (من الوضع الحالي حتى التحكم والقياس)",
            "صياغة الأهداف الذكية (SMART Goals) ومؤشرات الأداء الرئيسية (KPIs)",
            "تحديد مصفوفة الميزانيات وتوزيع الإنفاق على القنوات التسويقية",
            "بناء خارطة طريق التنفيذ لـ 90 يوماً (90-Day Execution Roadmap)"
        ],
        "prompt": "Role: Chief Strategy Officer at OTB Agency.\nContext: Designing a comprehensive 90-day growth strategy for a mid-market brand entering the Egyptian market.\nTask: Provide full SOSTAC framework breakdown with actionable milestones and risk mitigation.",
        "case_study": "بناء الاستراتيجية الشاملة لإطلاق سلسلة فروع حلويات Rice Patisserie وتحديد الشرائح المستهدفة وتوقيتات الحملات الموسمية.",
        "lab": "تطبيق نموذج SOSTAC على بيزنس تجاري حقيقي وتحديد 3 مؤشرات أداء رئيسية للنمو."
    },
    {
        "id": "branding-identity",
        "cat": "strategy",
        "phase": 1,
        "title": "بناء الهوية والعلامة التجارية (Branding & Identity)",
        "pages": 78,
        "icon": "👑",
        "badge": "Brand Archetypes & Equity",
        "desc": "صناعة الشخصية النفسية للعلامة التجارية، اختيار النمط الأصيل (The Ruler & The Creator)، توحيد الصوت البصري والنصي، وبناء قيمة البراند (Brand Equity).",
        "units": [
            "الفرق الجوهري بين الهوية البصرية (Visual Identity) وبناء البراند (Branding)",
            "الأنماط النفسية الـ 12 للعلامات التجارية (Brand Archetypes)",
            "صياغة نبرة الصوت والمفردات اللغوية (Tone of Voice & Messaging)",
            "كتابة كراسة معايير الهوية (Brand Guidelines Bible)",
            "تموضع السعر والهيبة (Premium Positioning & Pricing Power)",
            "حماية سمعة العلامة التجارية وإدارة الأزمات (Brand Crisis Management)"
        ],
        "prompt": "Role: Brand Architecture Director at OTB Agency.\nContext: Developing a luxury brand identity manual for [Client Name].\nTask: Define the Brand Archetype (The Ruler), Core Values, Mission/Vision, and Tone of Voice dos & don'ts.",
        "case_study": "صياغة هوية وكالة OTB نفسها ('The City Kings' 👑) والاعتماد على مزيج الأسود والذهب لفرض تموضع القيادة والهيبة في السوق.",
        "lab": "تحديد النمط النفسي (Archetype) المناسب لبراند فاخر وصياغة 3 جمل تعبر عن نبرة صوته الملكية."
    },
    {
        "id": "seo-mastery",
        "cat": "creative",
        "phase": 2,
        "title": "سيو محركات البحث ومحرك الزيارات العضوية (Search Engine Optimization)",
        "pages": 173,
        "icon": "🔍",
        "badge": "3-Day Technical & On-Page Engine",
        "desc": "تصدر نتائج بحث جوجل العضوية، السيو التقني وتهيئة الموقع، استراتيجيات الكلمات المفتاحية، وبناء الروابط الخلفية القوية (Backlinks) والظهور في نتائج الذكاء الاصطناعي (SGE/AIO).",
        "units": [
            "أساسيات محركات البحث وخوارزميات الترتيب والزحف والفهرسة (Crawling & Indexing)",
            "البحث عن الكلمات المفتاحية التنافسية وتجميعها (Keyword Research & Clustering)",
            "السيو الداخلي (On-Page SEO): العناوين، الأوصاف، الروابط الداخلية، والوسوم الدلالية",
            "السيو التقني (Technical SEO): سرعة الموقع، Core Web Vitals، وهيكل البيانات Schema",
            "بناء الروابط الخلفية والسلطة (Off-Page SEO & High-Authority Backlinks)",
            "سيو التجارة الإلكترونية ومحركات بحث الذكاء الاصطناعي (Search Generative Experience)"
        ],
        "prompt": "Role: Lead SEO Specialist at OTB Agency.\nContext: Optimizing e-commerce website [Website Domain] selling fashion items in Egypt.\nTask: Perform On-Page SEO audit, identify keyword gaps, and write optimized meta titles and H1/H2 structures.",
        "case_study": "تحسين موقع متجر صقر (Sakr Store) وتصدر الكلمات المفتاحية لمنتجات الأدوات المنزلية، محققاً نمواً في الزيارات العضوية بنسبة 320% دون إنفاق إعلاني إضافي.",
        "lab": "إجراء بحث كلمات مفتاحية لمنتج تجاري وتحديد 5 كلمات ذات نية شراء عالية (Commercial Intent)."
    },
    {
        "id": "youtube-strategy",
        "cat": "creative",
        "phase": 2,
        "title": "يوتيوب وسيو الفيديو وزيادة المشاهدات (YouTube & Video SEO)",
        "pages": 82,
        "icon": "🎥",
        "badge": "CTR, Retention & Monetization",
        "desc": "صناعة القنوات المؤثرة، تصميم الصور المصغرة ذات معدل النقر المرتفع (CTR)، رفع متوسط وقت المشاهدة (Audience Retention)، وتوظيف YouTube Shorts.",
        "units": [
            "سيكولوجية الصورة المصغرة (Thumbnails) والعنوان لرفع معدل النقر (CTR > 10%)",
            "هندسة محتوى الفيديو الطويل للحفاظ على المشاهدين حتى النهاية (Retention Graph)",
            "سيو الفيديو وتصدر نتائج بحث يوتيوب ومقاطع الفيديو المقترحة (Suggested Videos)",
            "استراتيجية YouTube Shorts لجذب آلاف المشتركين الجدد يومياً",
            "تحليلات استوديو يوتيوب وفهم مصادر الزيارات ونقاط هبوط المشاهدين",
            "تحويل مشاهدات يوتيوب إلى مبيعات وعملاء لقمع البيع المباشر"
        ],
        "prompt": "Role: YouTube Growth Producer at OTB Agency.\nContext: Planning a high-production brand series for [Company Name].\nTask: Design 3 high-CTR thumbnail & title concepts, outline a 10-minute video retention structure with B-roll cues.",
        "case_study": "إطلاق سلسلة بودكاست وفيديوهات خلف الكواليس لأحد عملاء OTB محققة أكثر من 200 ألف مشاهدة ومئات العملاء المهتمين بخدماتهم.",
        "lab": "تصميم خطة فيديو يوتيوب مدته 8 دقائق مع تحديد اللقطات الافتتاحية والصور المصغرة المقترحة."
    },
    {
        "id": "email-marketing",
        "cat": "ai",
        "phase": 4,
        "title": "التسويق بالبريد الإلكتروني وتدفقات الأتمتة (Email Marketing & Retention)",
        "pages": 52,
        "icon": "📧",
        "badge": "Klaviyo Flows & Lifecycle LTV",
        "desc": "بناء الأصول التسويقية المملوكة (Owned Media)، تدفقات استعادة السلات المتروكة، الرسائل الترحيبية المؤتمتة، ورفع القيمة العمرية للعميل (LTV).",
        "units": [
            "أهمية القوائم البريدية وحماية البيزنس من تقلبات خوارزميات المنصات الإعلانية",
            "سلاسل التدفقات المؤتمتة الإلزامية (Welcome Series, Abandoned Cart, Post-Purchase)",
            "تقسيم القوائم البريدية (Advanced Segmentation) بناءً على سلوك الشراء",
            "كتابة عناوين البريد التي تضمن معدلات فتح قياسية (Open Rates > 35%)",
            "تصميم إيميلات متوافقة مع الموبايل وموجهة للتحويل الفوري (Responsive Design)",
            "ضمان تسليم الإيميل في صندوق الوارد وتجنب مجلد الرسائل غير المرغوبة (Spam)"
        ],
        "prompt": "Role: Lifecycle & Retention Email Architect at OTB Agency.\nContext: Designing an Abandoned Cart email sequence for [E-Commerce Store].\nTask: Write a 3-email recovery sequence (Email 1 at 1hr: Helpful reminder, Email 2 at 12hrs: Social proof & reviews, Email 3 at 24hrs: 10% limited-time incentive).",
        "case_study": "تطبيق تدفقات Klaviyo المؤتمتة لمتجر إلكتروني رفعت إيرادات المتجر الإجمالية بنسبة 28% دون دفع دولار واحد إضافي في الإعلانات.",
        "lab": "كتابة إيميل استعادة سلة متروكة يتضمن عنواناً جذاباً ودعوة واضحة لإتمام الطلب."
    },
    {
        "id": "growth-hacking",
        "cat": "ai",
        "phase": 4,
        "title": "الجروث هاكينج وحلقات الانتشار الفيرال (Growth Hacking)",
        "pages": 58,
        "icon": "🚀",
        "badge": "AARRR Funnel & Viral Loops",
        "desc": "أساليب النمو غير التقليدية للشركات الناشئة، قمع القرصنة AARRR، هندسة برامج الإحالة الفيرال، ومصفوفة أولويات التجارب السريعة (ICE Framework).",
        "units": [
            "عقلية الجروث هاكر والفرق بينه وبين المسوق التقليدي",
            "قمع النمو AARRR: Acquisition, Activation, Retention, Referral, Revenue",
            "هندسة حلقات الانتشار الفيرال (Viral Loops & Referral Mechanisms)",
            "مصفوفة تقييم واختبار الأفكار التجريبية السريعة (ICE Prioritization Framework)",
            "تقنيات استخراج البيانات والمنافسين (Scraping & Growth Tools)",
            "تحسين معدلات التحويل داخل الموقع والتطبيق (CRO & UX Optimization)"
        ],
        "prompt": "Role: Lead Growth Hacker at OTB Agency.\nContext: Rapidly scaling a local delivery app user base in Cairo.\nTask: Brainstorm 5 low-cost, high-impact growth experiments using the ICE scoring framework.",
        "case_study": "تطبيق حلقة إحالة 'ادعُ صديقك واحصل على وجبة مجانية' لـ Rancho's EG، مما جلب أكثر من 3,500 عميل جديد خلال 3 أسابيع بأقل تكلفة استحواذ.",
        "lab": "تقييم 3 أفكار نمو تجريبية باستخدام مصفوفة ICE وترتيبها حسب الأولوية."
    },
    {
        "id": "twitter-x",
        "cat": "media",
        "phase": 3,
        "title": "منصة إكس والتموضع المؤسسي (Twitter / X Authority)",
        "pages": 136,
        "icon": "🐦",
        "badge": "Viral Threads & Newsjacking",
        "desc": "بناء التواجد الرسمي القوي، كتابة الثريدات التحليلية الفيرال، استغلال الترندات والأخبار العاجلة (Newsjacking)، والتواصل المباشر مع النخب والمستثمرين.",
        "units": [
            "خوارزمية منصة إكس وكيفية تحقيق وصول واسع للتغريدات والثريدات",
            "صناعة الثريدات المعرفية العميقة التي تجذب آلاف المتابعين والمشاركات",
            "استراتيجيات ركوب الترند الذكي (Newsjacking) دون الإضرار بسمعة البراند",
            "إدارة الأزمات والرد السريع على استفسارات وشكاوى العملاء العامة",
            "إعلانات منصة إكس الموجهة لرواد الأعمال والجمهور الخليجي",
            "بناء الحضور الرسمي والمؤسسي الموثق للشركات الكبرى"
        ],
        "prompt": "Role: Corporate Communications Strategist at OTB Agency.\nContext: Managing an executive X account in the tech and venture capital space.\nTask: Write an engaging 7-tweet viral thread dissecting a major industry trend with deep market insights.",
        "case_study": "نشر ثريد تحليلي حول أخطاء إعلانات المطاعم في مصر حقق أكثر من 120 ألف تفاعل وجلب عملاء تجاريين جدد لوكالة OTB.",
        "lab": "كتابة تغريدة افتتاحية (Hook Tweet) لثريد تسويقي جذاب يناقش سيكولوجية المستهلك."
    },
    {
        "id": "snapchat-ads",
        "cat": "media",
        "phase": 3,
        "title": "إعلانات سناب شات والتوسع في الخليج (Snapchat Ads & GCC)",
        "pages": 45,
        "icon": "👻",
        "badge": "AR Lenses & GCC Scaling",
        "desc": "استهداف الأسواق الخليجية (السعودية والإمارات والكويت)، تصميم عدسات الواقع المعزز (AR Lenses)، وإطلاق حملات الشراء المباشر والزيارات للمتاجر.",
        "units": [
            "طبيعة مستخدمي سناب شات وسيطرته المطلقة في الأسواق الخليجية",
            "منصة إعلانات سناب شات (Snap Ads Manager) وتركيب Snap Pixel",
            "أنواع الإعلانات: Single Image, Story Ads, Collection Ads, Commercials",
            "تصميم عدسات الواقع المعزز (Snap AR Lenses) التفاعلية لزيادة تفاعل البراند",
            "استراتيجيات مبيعات المتاجر الإلكترونية والتطبيقات في السوق السعودي",
            "تحسين الميزانيات وتجنب إهدار الإنفاق الإعلاني على سناب شات"
        ],
        "prompt": "Role: GCC Media Buying Specialist at OTB Agency.\nContext: Launching a luxury fragrance line on Snapchat targeting Riyadh & Jeddah.\nTask: Design a high-converting Snap Ads funnel utilizing Collection Ads and Story Ads with clear ROI benchmarks.",
        "case_study": "حملة إعلانية على سناب شات لعلامة تجارية سعودية حققت عائداً إعلانيا 6.8x وتصدرت مبيعات العطور في موسم التخفيضات.",
        "lab": "تصميم فكرة إعلان سناب شات عمودي (9:16) مدته 6 ثوانٍ يستهدف الجمهور الخليجي."
    },
    {
        "id": "affiliate-marketing",
        "cat": "ai",
        "phase": 4,
        "title": "التسويق بالعمولة والشراكات الاستراتيجية (Affiliate Marketing)",
        "pages": 44,
        "icon": "🤝",
        "badge": "Partner Networks & Commissions",
        "desc": "بناء شبكات المسوقين بالعمولة لبراندك، اختيار شبكات الأفلييت الموثوقة، تصميم عروض العمولات الجذابة، وتتبع المبيعات بنزاهة وشفافية.",
        "units": [
            "مفهوم التسويق بالعمولة وكيف تبني جيشاً من المسوقين يبيعون لمنتجاتك",
            "أشهر شبكات الأفلييت العربية والعالمية ونماذج التتبع (Cookie Windows & Attribution)",
            "تصميم هيكل العمولات المربحة (CPA, CPL, RevShare) دون الإضرار بهامش الربح",
            "توفير المواد التسويقية الجاهزة للأفلييتس (Creatives, Copy, Landing Pages)",
            "حماية البرنامج من التلاعب والاحتيال التسويقي (Fraud Prevention)",
            "استقطاب كبار صناع المحتوى والمواقع المتخصصة لترويج منتجاتك"
        ],
        "prompt": "Role: Affiliate Program Director at OTB Agency.\nContext: Building an affiliate partner network for an established Egyptian e-commerce brand.\nTask: Create a partner recruitment landing page outline and commission structure guide.",
        "case_study": "بناء برنامج أفلييت لمتجر إلكتروني جلب أكثر من 150 صانع محتوى وسوقوا لمنتجات المتجر محققين 22% من إجمالي المبيعات السنوية.",
        "lab": "تصميم هيكل عمولات عادل لمنتج سعر بيعه 1000 جنيه وهامش ربحه 40%."
    },
    {
        "id": "marketing-principles",
        "cat": "strategy",
        "phase": 1,
        "title": "مبادئ وأسس التسويق الحديث (Modern Marketing Principles)",
        "pages": 20,
        "icon": "💡",
        "badge": "4Ps to 4Cs & Consumer Psychology",
        "desc": "الأسس الأكاديمية الراسخة التي تحكم عالم التسويق، الانتقال من المزيج التسويقي التقليدي (4Ps) إلى المزيج الموجه للعميل (4Cs)، وسيكولوجية اتخاذ القرار.",
        "units": [
            "المفهوم الحقيقي للتسويق: خلق القيمة وتلبية الاحتياجات وتحقيق الربحية",
            "المزيج التسويقي الكلاسيكي (4Ps: Product, Price, Place, Promotion)",
            "المزيج التسويقي الحديث المرتكز على العميل (4Cs: Customer, Cost, Convenience, Communication)",
            "مراحل رحلة العميل (Customer Journey & Buyer Persona)",
            "سيكولوجية التسعير وإدراك القيمة (Perceived Value vs Real Cost)",
            "أخلاقيات التسويق وبناء الثقة طويلة الأجل مع الجمهور"
        ],
        "prompt": "Role: Senior Marketing Consultant at OTB Agency.\nContext: Training newly hired marketing associates.\nTask: Explain the practical shift from 4Ps to 4Cs using real Egyptian market examples.",
        "case_study": "تطبيق مبادئ إدراك القيمة على قائمة أسعار MIX Coffee لجعل خيار الحجم الكبير الأكثر جاذبية وطلباً من العملاء.",
        "lab": "تحويل عناصر الـ 4Ps لمنتج خدمي إلى نموذج الـ 4Cs المقابل له."
    },
    {
        "id": "freelancing-retainers",
        "cat": "career",
        "phase": 4,
        "title": "العمل الحر وإغلاق عقود الريتينر الشهرية (Agency Retainers)",
        "pages": 52,
        "icon": "💼",
        "badge": "$2,500/mo Retainer Pitching",
        "desc": "كيفية تسعير الخدمات التسويقية، بناء البورتفوليو المقنع، تقديم عروض الأسعار التي لا تقاوم، وإغلاق عقود الريتينر الشهرية بقيمة $2,500+ بثقة تامة.",
        "units": [
            "الانتقال من العمل بالساعة إلى التسعير القائم على القيمة والعائد (Value-Based Pricing)",
            "بناء العرض الذي لا يقاوم (Grand Slam Offer) لخدمات التسويق",
            "هيكل باقات الريتينر الشهرية لـ OTB: Starter, Dominance ($2,500), Scale",
            "مهارات إدارة اجتماعات الاكتشاف والمبيعات (Discovery Calls & Closing)",
            "كتابة مقترحات العمل والعقود القانونية وحماية مستحقات الوكالة",
            "الحفاظ على العملاء وتجديد العقود (Client Retention & Upselling)"
        ],
        "prompt": "Role: Commercial Director at OTB Agency.\nContext: Closing a high-ticket $2,500/month Dominance Retainer with a multi-branch business owner.\nTask: Write an executive pitch email outlining the strategic roadmap, team deliverables, and projected ROI.",
        "case_study": "إغلاق عقود ريتينر شهرية مستمرة مع عملاء OTB الرئيسيين بالاعتماد على توضيح عوائد الاستثمار بدلاً من مجرد سرد عدد البوستات.",
        "lab": "صياغة مقترح باقة تسويقية شهرية بقيمة $2,500 تتضمن المحتوى والإعلانات والأتمتة."
    },
    {
        "id": "career-interview",
        "cat": "career",
        "phase": 4,
        "title": "التميز المهني ومهارات المقابلات الشخصية (Career & Interview)",
        "pages": 43,
        "icon": "🎯",
        "badge": "STAR Method & Executive Presence",
        "desc": "بناء السيرة الذاتية المبنية على الأرقام والإنجازات (ATS-Friendly CV)، استعراض سابقة الأعمال باحترافية، وإتقان الإجابة على أصعب أسئلة المقابلات بنموذج STAR.",
        "units": [
            "هندسة السيرة الذاتية القائمة على النتائج والأرقام (Metric-Driven Resume)",
            "تصميم معرض الأعمال التفاعلي (Interactive Case Study Portfolio)",
            "استخدام نموذج STAR للإجابة على الأسئلة السلوكية: Situation, Task, Action, Result",
            "مهارات التفاوض على الراتب والحوافز والمكافآت المرتبطة بالأداء",
            "الحضور التنفيذي والتواصل الواثق مع الإدارة العليا والعملاء",
            "بناء مسار الترقي المهني المستمر والتطوير الذاتي في مجال التسويق"
        ],
        "prompt": "Role: Executive Talent & Career Mentor at OTB Agency.\nContext: Preparing a senior candidate for a Head of Growth interview.\nTask: Provide 5 tough behavioral interview scenarios and structure high-impact answers using the STAR method.",
        "case_study": "تأهيل كوادر OTB Agency الداخلية للتعامل المباشر مع المستثمرين ومدراء الشركات بثقة واحترافية عالية.",
        "lab": "صياغة إنجاز تسويقي حقيقي باستخدام نموذج STAR المعتمد."
    },
    {
        "id": "corelink-sops",
        "cat": "strategy",
        "phase": 1,
        "title": "نظام التشغيل CoreLink CRM والانضباط الإجرائي (SOPs)",
        "pages": 65,
        "icon": "🛡️",
        "badge": "Zero Waste & SLA Management",
        "desc": "الإجراءات التشغيلية الموحدة لمنع الهدر، القضاء على التوجيه الفارغ، ربط الأقسام بنظام قفل التبعيات (Sequential Locking)، والالتزام باتفاقيات الخدمة (SLA).",
        "units": [
            "معايير الجودة الشاملة داخل منظومة OTB التشغيلية",
            "إلزامية نماذج البريف القياسي ومنع التعليمات الشفهية",
            "قفل المراحل التسلسلي: اكتمال النصوص 100% قبل فتح مهام التصميم",
            "قواعد المراجعات وتسليم الأصول عبر السحابة (Cloudflare R2)",
            "اتفاقية مستوى الخدمة (SLA Rule): مراجعة خلال 24 ساعة والتصعيد بعد 48 ساعة",
            "تتبع التكلفة الحقيقية وساعات العمل لحساب ربحية كل حساب بدقة"
        ],
        "prompt": "Role: Operations & CRM Director at OTB Agency.\nContext: Implementing zero-waste SOPs in CoreLink CRM.\nTask: Draft an internal policy document detailing the sequential locking process and SLA escalation ladder.",
        "case_study": "تطبيق إجراءات SOPs الموحدة داخل وكالة OTB مما خفض نسبة إعادة العمل والتعديلات بنسبة 42% وسرع إطلاق الحملات.",
        "lab": "تعبئة نموذج بريف تشغيلي كامل لمهمة إعلانية تتضمن فريق المحتوى والتصميم والميديا بايينج."
    }
]

print(f"Loaded {len(COURSES_DATA)} full course modules!")
