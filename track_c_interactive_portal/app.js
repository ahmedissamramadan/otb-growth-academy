
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
