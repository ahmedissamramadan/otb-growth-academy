// OTB Growth Academy — Shared Interactive UI Engine
function showToast(message) {
  let toast = document.getElementById("otbToast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "otbToast";
    toast.className = "toast-msg";
    document.body.appendChild(toast);
  }
  toast.innerText = message;
  toast.classList.add("show");
  setTimeout(() => {
    toast.classList.remove("show");
  }, 2500);
}

function copyText(text, successMsg = "تم النسخ بنجاح للحافظة! 👑") {
  if (!text) return;
  navigator.clipboard.writeText(text).then(() => {
    showToast(successMsg);
  }).catch(err => {
    console.error("Copy failed", err);
    showToast("حدث خطأ أثناء النسخ");
  });
}
