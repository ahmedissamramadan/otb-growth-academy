
// OTB Academy — Interactive WebGL & UI Engine
function showToast(msg) {
  let toast = document.getElementById("otbToast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "otbToast";
    toast.className = "toast";
    document.body.appendChild(toast);
  }
  toast.innerText = msg;
  toast.classList.add("show");
  setTimeout(() => { toast.classList.remove("show"); }, 2500);
}

function copyText(txt, successMsg = "تم النسخ للحافظة بنجاح! 👑") {
  if (!txt) return;
  navigator.clipboard.writeText(txt).then(() => {
    showToast(successMsg);
  }).catch(err => {
    console.error("Copy failed", err);
  });
}

// THREE.JS AMBIENT PARTICLES
window.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("webgl-bg");
  if (!canvas || typeof THREE === "undefined") return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 80;

  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Gold star particles
  const count = 350;
  const geometry = new THREE.BufferGeometry();
  const positions = new Float32Array(count * 3);

  for (let i = 0; i < count * 3; i += 3) {
    positions[i] = (Math.random() - 0.5) * 160;
    positions[i + 1] = (Math.random() - 0.5) * 160;
    positions[i + 2] = (Math.random() - 0.5) * 80;
  }
  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

  const material = new THREE.PointsMaterial({
    size: 1.4,
    color: 0xD4A853,
    transparent: true,
    opacity: 0.45
  });

  const particles = new THREE.Points(geometry, material);
  scene.add(particles);

  let mouseX = 0, mouseY = 0;
  window.addEventListener("mousemove", (e) => {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 4;
    mouseY = (e.clientY / window.innerHeight - 0.5) * 4;
  });

  function animate() {
    requestAnimationFrame(animate);
    particles.rotation.y += 0.0005;
    particles.rotation.x += 0.0003;
    camera.position.x += (mouseX - camera.position.x) * 0.03;
    camera.position.y += (-mouseY - camera.position.y) * 0.03;
    renderer.render(scene, camera);
  }
  animate();

  window.addEventListener("resize", () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
});
