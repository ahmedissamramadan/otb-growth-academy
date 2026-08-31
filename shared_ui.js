
// OTB Agency WebGL 3D Particle Starfield & UI Engine
function initWebGLParticles() {
  const canvas = document.getElementById("webglCanvas");
  if (!canvas || typeof THREE === "undefined") return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 80;

  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Golden Geometric Dust Particles
  const particleCount = 450;
  const geometry = new THREE.BufferGeometry();
  const positions = new Float32Array(particleCount * 3);
  const colors = new Float32Array(particleCount * 3);

  const goldColor = new THREE.Color(0xD4A853);
  const lightColor = new THREE.Color(0xF3E5C8);

  for (let i = 0; i < particleCount; i++) {
    positions[i * 3] = (Math.random() - 0.5) * 200;
    positions[i * 3 + 1] = (Math.random() - 0.5) * 200;
    positions[i * 3 + 2] = (Math.random() - 0.5) * 120;

    const mixedColor = goldColor.clone().lerp(lightColor, Math.random());
    colors[i * 3] = mixedColor.r;
    colors[i * 3 + 1] = mixedColor.g;
    colors[i * 3 + 2] = mixedColor.b;
  }

  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

  const material = new THREE.PointsMaterial({
    size: 2.2,
    vertexColors: true,
    transparent: true,
    opacity: 0.65,
    blending: THREE.AdditiveBlending
  });

  const particleSystem = new THREE.Points(geometry, material);
  scene.add(particleSystem);

  let mouseX = 0, mouseY = 0;
  window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX - window.innerWidth / 2) * 0.03;
    mouseY = (e.clientY - window.innerHeight / 2) * 0.03;
  });

  function animate() {
    requestAnimationFrame(animate);
    particleSystem.rotation.y += 0.0008;
    particleSystem.rotation.x += 0.0004;

    camera.position.x += (mouseX - camera.position.x) * 0.03;
    camera.position.y += (-mouseY - camera.position.y) * 0.03;
    camera.lookAt(scene.position);

    renderer.render(scene, camera);
  }
  animate();

  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
}

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

function copyText(txt, successMsg = "تم النسخ بنجاح للحافظة! 👑") {
  if (!txt) return;
  navigator.clipboard.writeText(txt).then(() => {
    showToast(successMsg);
  }).catch(err => {
    console.error("Copy failed", err);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initWebGLParticles();
});
