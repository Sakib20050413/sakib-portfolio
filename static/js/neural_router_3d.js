(function () {
  "use strict";

  let scene, camera, renderer, masterCore, subModelNodes = [], pulseParticles = [];
  let activeRouteIndex = -1;
  let selfTrainingMode = false;

  function initMasterAI3D() {
    const container = document.getElementById("masterAi3dViewport");
    if (!container || typeof THREE === "undefined") return;

    const w = container.clientWidth || 520;
    const h = container.clientHeight || 320;

    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x07080d);

    camera = new THREE.PerspectiveCamera(42, w / h, 0.1, 100);
    camera.position.set(0, 2.6, 6.4);
    camera.lookAt(0, 0, 0);

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(w, h);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    scene.add(new THREE.AmbientLight(0xffffff, 0.8));
    const pointLight = new THREE.PointLight(0x6366f1, 2.2, 20);
    pointLight.position.set(2, 4, 4);
    scene.add(pointLight);

    // 1. Central Always-Resident Master AI Router Core (CPU RAM + GPU VRAM + NPU)
    masterCore = new THREE.Group();
    const coreGeo = new THREE.IcosahedronGeometry(0.68, 1);
    const coreMat = new THREE.MeshStandardMaterial({
      color: 0x4f46e5,
      emissive: 0x312e81,
      emissiveIntensity: 0.7,
      wireframe: false,
      metalness: 0.7,
      roughness: 0.2,
    });
    masterCore.add(new THREE.Mesh(coreGeo, coreMat));

    const wireRing = new THREE.Mesh(
      new THREE.TorusGeometry(0.95, 0.025, 12, 48),
      new THREE.MeshBasicMaterial({ color: 0x10b981 })
    );
    wireRing.rotation.x = Math.PI / 2.4;
    masterCore.add(wireRing);
    scene.add(masterCore);

    // 2. Four Orbiting ~1.0 GB Specialized Sub-Model Nodes (Code-1G, Photo-1G, Video-1G, Reason-1G)
    const experts = [
      { name: "CODE-1G (0.95 GB)", color: 0x38bdf8, angle: 0 },
      { name: "PHOTO-1G (1.05 GB)", color: 0x10b981, angle: Math.PI / 2 },
      { name: "VIDEO-1G (1.15 GB)", color: 0xf59e0b, angle: Math.PI },
      { name: "REASON-1G (0.90 GB)", color: 0xa855f7, angle: (3 * Math.PI) / 2 },
    ];

    experts.forEach(function (exp, idx) {
      const g = new THREE.Group();
      const mesh = new THREE.Mesh(
        new THREE.OctahedronGeometry(0.32, 0),
        new THREE.MeshStandardMaterial({
          color: exp.color,
          emissive: exp.color,
          emissiveIntensity: 0.35,
          metalness: 0.5,
          roughness: 0.25,
        })
      );
      const orbitRing = new THREE.Mesh(
        new THREE.TorusGeometry(0.44, 0.015, 8, 24),
        new THREE.MeshBasicMaterial({ color: exp.color })
      );
      g.add(mesh);
      g.add(orbitRing);
      g.userData = { baseAngle: exp.angle, label: exp.name, color: exp.color, idx: idx };
      scene.add(g);
      subModelNodes.push(g);
    });

    function animate() {
      requestAnimationFrame(animate);
      const t = Date.now() * 0.0012;

      if (masterCore) {
        masterCore.rotation.y += selfTrainingMode ? 0.045 : 0.012;
        masterCore.rotation.x = Math.sin(t) * 0.18;
        const scalePulse = selfTrainingMode ? 1 + Math.sin(Date.now() * 0.012) * 0.14 : 1;
        masterCore.scale.set(scalePulse, scalePulse, scalePulse);
      }

      subModelNodes.forEach(function (node, i) {
        const angle = node.userData.baseAngle + t * 0.55;
        const radius = activeRouteIndex === i ? 1.65 : 2.35;
        node.position.set(Math.cos(angle) * radius, Math.sin(t * 2 + i) * 0.22, Math.sin(angle) * radius);
        node.rotation.y += 0.03;
        const s = activeRouteIndex === i ? 1.38 : 1.0;
        node.scale.set(s, s, s);
      });

      renderer.render(scene, camera);
    }
    animate();

    window.addEventListener("resize", function () {
      const nw = container.clientWidth || 520;
      const nh = container.clientHeight || 320;
      camera.aspect = nw / nh;
      camera.updateProjectionMatrix();
      renderer.setSize(nw, nh);
    });
  }

  window.triggerMasterAIRoute = function (expertIdx, statusLabel) {
    activeRouteIndex = expertIdx;
    selfTrainingMode = expertIdx === 99;
    const tel = document.getElementById("masterAiTelemetryStatus");
    if (tel) {
      tel.textContent = statusLabel;
    }
  };

  window.addEventListener("DOMContentLoaded", initMasterAI3D);
})();
