/**
 * ==============================================================================
 * GOOGLE ANTIGRAVITY IDE — MASTER PROMPT 1 (V3.0)
 * INTERACTIVE CONTROLLER: 12-COLUMN STUDIO, 3D ISOMETRIC CORE, TELEMETRY & CLI
 * Md Najmus Sakib Rahatul (Student ID: 1119003) — Dept. of CSE, BAIUST
 * ==============================================================================
 */

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function showToast(message, type = "success") {
  const container = document.getElementById("toast-container");
  if (!container) return;

  const toast = document.createElement("div");
  toast.className = `px-4 py-3 rounded-xl text-xs font-mono border backdrop-blur-md transition-all duration-300 transform translate-y-2 pointer-events-auto flex items-center gap-2.5 shadow-xl ${
    type === "success"
      ? "bg-[#11131c]/95 border-emerald-500/40 text-emerald-300"
      : "bg-[#11131c]/95 border-rose-500/40 text-rose-300"
  }`;

  const icon = document.createElement("i");
  icon.className = type === "success" ? "fa-solid fa-circle-check text-emerald-400" : "fa-solid fa-circle-exclamation text-rose-400";
  toast.appendChild(icon);

  const text = document.createElement("span");
  text.textContent = message;
  toast.appendChild(text);

  container.appendChild(toast);

  requestAnimationFrame(() => {
    toast.classList.remove("translate-y-2");
    toast.classList.add("translate-y-0");
  });

  setTimeout(() => {
    toast.classList.add("opacity-0", "translate-y-2");
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

document.addEventListener("DOMContentLoaded", () => {
  // ----------------------------------------------------------------------------
  // 1. LIVE CUMILLA TIME (Asia/Dhaka UTC+6)
  // ----------------------------------------------------------------------------
  const clockEl = document.getElementById("dac-clock");
  if (clockEl) {
    function updateClock() {
      const now = new Date();
      const options = {
        timeZone: "Asia/Dhaka",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: false,
      };
      clockEl.textContent = `CUMILLA • ${now.toLocaleTimeString("en-US", options)} UTC+6`;
    }
    updateClock();
    setInterval(updateClock, 1000);
  }

  // ----------------------------------------------------------------------------
  // 2. THEME SWITCHER (Obsidian Dark vs Warm Editorial Paper Light)
  // ----------------------------------------------------------------------------
  const themeToggle = document.getElementById("theme-toggle");
  const savedTheme = localStorage.getItem("sakib_v3_theme");

  if (savedTheme === "light") {
    document.body.classList.add("light-mode");
    document.documentElement.classList.remove("dark");
    if (themeToggle) themeToggle.innerHTML = '<i class="fa-solid fa-sun mr-1 text-[11px]"></i> Light';
  }

  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      document.body.classList.toggle("light-mode");
      const isLight = document.body.classList.contains("light-mode");
      if (isLight) {
        document.documentElement.classList.remove("dark");
        themeToggle.innerHTML = '<i class="fa-solid fa-sun mr-1 text-[11px]"></i> Light';
      } else {
        document.documentElement.classList.add("dark");
        themeToggle.innerHTML = '<i class="fa-solid fa-moon mr-1 text-[11px]"></i> Dark';
      }
      localStorage.setItem("sakib_v3_theme", isLight ? "light" : "dark");
    });
  }

  // ----------------------------------------------------------------------------
  // 3. HERO 3-TAB SWITCHER (3D Core, Telemetry, Mini-CLI)
  // ----------------------------------------------------------------------------
  const tabBtn3D = document.getElementById("tab-btn-3d");
  const tabBtnTelemetry = document.getElementById("tab-btn-telemetry");
  const tabBtnQuickCli = document.getElementById("tab-btn-quickcli");

  const view3D = document.getElementById("hero-view-3d");
  const viewTelemetry = document.getElementById("hero-view-telemetry");
  const viewQuickCli = document.getElementById("hero-view-quickcli");

  function switchHeroTab(activeBtn, activeView) {
    [tabBtn3D, tabBtnTelemetry, tabBtnQuickCli].forEach((b) => {
      if (!b) return;
      b.classList.remove("bg-indigo-600", "text-white");
      b.classList.add("text-neutral-400");
    });
    [view3D, viewTelemetry, viewQuickCli].forEach((v) => {
      if (!v) return;
      v.classList.add("hidden");
    });

    if (activeBtn) {
      activeBtn.classList.add("bg-indigo-600", "text-white");
      activeBtn.classList.remove("text-neutral-400");
    }
    if (activeView) {
      activeView.classList.remove("hidden");
    }
  }

  if (tabBtn3D) tabBtn3D.addEventListener("click", () => switchHeroTab(tabBtn3D, view3D));
  if (tabBtnTelemetry) tabBtnTelemetry.addEventListener("click", () => switchHeroTab(tabBtnTelemetry, viewTelemetry));
  if (tabBtnQuickCli) tabBtnQuickCli.addEventListener("click", () => switchHeroTab(tabBtnQuickCli, viewQuickCli));

  const heroOpenTerminalBtn = document.getElementById("hero-open-terminal-btn");
  if (heroOpenTerminalBtn) {
    heroOpenTerminalBtn.addEventListener("click", () => {
      switchHeroTab(tabBtnQuickCli, viewQuickCli);
      const input = document.getElementById("quickcli-input");
      if (input) input.focus();
    });
  }

  // ----------------------------------------------------------------------------
  // 4. HERO TAB 1: 3D ISOMETRIC DEVELOPER & EMBEDDED HARDWARE CORE
  // ----------------------------------------------------------------------------
  const isoCanvas = document.getElementById("isometric-canvas");
  if (isoCanvas) {
    const ctx = isoCanvas.getContext("2d");
    let animationFrameId;
    let width, height;
    let mouseX = 0, mouseY = 0;
    let targetAngleX = 0, targetAngleY = 0;
    let angleX = 0, angleY = 0;

    function resizeCanvas() {
      const rect = isoCanvas.parentElement.getBoundingClientRect();
      width = rect.width;
      height = rect.height;
      isoCanvas.width = width * window.devicePixelRatio;
      isoCanvas.height = height * window.devicePixelRatio;
      ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
    }
    resizeCanvas();
    window.addEventListener("resize", resizeCanvas);

    isoCanvas.parentElement.addEventListener("mousemove", (e) => {
      const rect = isoCanvas.getBoundingClientRect();
      const x = e.clientX - rect.left - width / 2;
      const y = e.clientY - rect.top - height / 2;
      targetAngleY = (x / width) * 0.4;
      targetAngleX = (y / height) * -0.3;
    });

    isoCanvas.parentElement.addEventListener("mouseleave", () => {
      targetAngleX = 0;
      targetAngleY = 0;
    });

    let pulseStep = 0;
    function renderIsoCore() {
      ctx.clearRect(0, 0, width, height);

      // Smooth camera interpolation
      angleX += (targetAngleX - angleX) * 0.08;
      angleY += (targetAngleY - angleY) * 0.08;
      pulseStep += 0.03;

      const cx = width / 2;
      const cy = height / 2 + 10;
      const size = Math.min(width, height) * 0.22;

      // Isometric projection helper
      function isoProject(x, y, z) {
        // Rotate around Y
        const cosY = Math.cos(angleY + 0.6);
        const sinY = Math.sin(angleY + 0.6);
        const rx = x * cosY - z * sinY;
        const rz = x * sinY + z * cosY;

        // Rotate around X
        const cosX = Math.cos(angleX + 0.5);
        const sinX = Math.sin(angleX + 0.5);
        const ry = y * cosX - rz * sinX;

        return {
          px: cx + rx,
          py: cy + ry,
        };
      }

      // Draw Base Grid / Circuit lines
      ctx.strokeStyle = "rgba(79, 70, 229, 0.15)";
      ctx.lineWidth = 1;
      const gridSize = 3;
      const step = size * 0.8;
      for (let i = -gridSize; i <= gridSize; i++) {
        const p1 = isoProject(i * step, size * 0.8, -gridSize * step);
        const p2 = isoProject(i * step, size * 0.8, gridSize * step);
        ctx.beginPath();
        ctx.moveTo(p1.px, p1.py);
        ctx.lineTo(p2.px, p2.py);
        ctx.stroke();

        const p3 = isoProject(-gridSize * step, size * 0.8, i * step);
        const p4 = isoProject(gridSize * step, size * 0.8, i * step);
        ctx.beginPath();
        ctx.moveTo(p3.px, p3.py);
        ctx.lineTo(p4.px, p4.py);
        ctx.stroke();
      }

      // 3D Isometric Cube / Silicon Chip Block
      const h = size * 0.7;
      const s = size * 0.9;
      const vertices = [
        isoProject(-s, -h, -s), // 0: Top Front Left
        isoProject(s, -h, -s),  // 1: Top Front Right
        isoProject(s, -h, s),   // 2: Top Back Right
        isoProject(-s, -h, s),  // 3: Top Back Left
        isoProject(-s, h, -s),  // 4: Bottom Front Left
        isoProject(s, h, -s),   // 5: Bottom Front Right
        isoProject(s, h, s),    // 6: Bottom Back Right
        isoProject(-s, h, s),   // 7: Bottom Back Left
      ];

      // Draw Top Face (Chip Silicon)
      ctx.fillStyle = "rgba(19, 23, 38, 0.95)";
      ctx.beginPath();
      ctx.moveTo(vertices[0].px, vertices[0].py);
      ctx.lineTo(vertices[1].px, vertices[1].py);
      ctx.lineTo(vertices[2].px, vertices[2].py);
      ctx.lineTo(vertices[3].px, vertices[3].py);
      ctx.closePath();
      ctx.fill();
      ctx.strokeStyle = "rgba(99, 102, 241, 0.6)";
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Top Face Micro-Circuit Traces
      const centerP = isoProject(0, -h, 0);
      const glow = Math.sin(pulseStep) * 0.3 + 0.7;
      ctx.fillStyle = `rgba(16, 185, 129, ${glow})`;
      ctx.beginPath();
      ctx.arc(centerP.px, centerP.py, 3, 0, Math.PI * 2);
      ctx.fill();

      // Draw Left Face
      ctx.fillStyle = "rgba(14, 17, 28, 0.95)";
      ctx.beginPath();
      ctx.moveTo(vertices[0].px, vertices[0].py);
      ctx.lineTo(vertices[3].px, vertices[3].py);
      ctx.lineTo(vertices[7].px, vertices[7].py);
      ctx.lineTo(vertices[4].px, vertices[4].py);
      ctx.closePath();
      ctx.fill();
      ctx.strokeStyle = "rgba(255, 255, 255, 0.08)";
      ctx.stroke();

      // Draw Right Face
      ctx.fillStyle = "rgba(22, 27, 44, 0.95)";
      ctx.beginPath();
      ctx.moveTo(vertices[0].px, vertices[0].py);
      ctx.lineTo(vertices[1].px, vertices[1].py);
      ctx.lineTo(vertices[5].px, vertices[5].py);
      ctx.lineTo(vertices[4].px, vertices[4].py);
      ctx.closePath();
      ctx.fill();
      ctx.strokeStyle = "rgba(255, 255, 255, 0.08)";
      ctx.stroke();

      animationFrameId = requestAnimationFrame(renderIsoCore);
    }
    renderIsoCore();
  }

  // ----------------------------------------------------------------------------
  // 5. HERO TAB 2: HARDWARE TELEMETRY OSCILLOSCOPE (512-Pt FFT & AS3935 RF)
  // ----------------------------------------------------------------------------
  const osc1 = document.getElementById("oscilloscope-canvas-1");
  const osc2 = document.getElementById("oscilloscope-canvas-2");

  function initOscilloscopes() {
    if (!osc1 || !osc2) return;
    const ctx1 = osc1.getContext("2d");
    const ctx2 = osc2.getContext("2d");

    let step = 0;
    function drawWaves() {
      step += 0.05;
      [osc1, osc2].forEach((c) => {
        c.width = c.parentElement.clientWidth;
        c.height = 96;
      });

      // Canvas 1: 350-600 Hz Bio-Acoustic Waveform
      ctx1.clearRect(0, 0, osc1.width, osc1.height);
      ctx1.strokeStyle = "#10b981";
      ctx1.lineWidth = 1.5;
      ctx1.beginPath();
      for (let x = 0; x < osc1.width; x++) {
        const y =
          osc1.height / 2 +
          Math.sin(x * 0.05 + step * 3) * 18 * Math.sin(x * 0.01) +
          Math.sin(x * 0.12 - step * 2) * 8;
        if (x === 0) ctx1.moveTo(x, y);
        else ctx1.lineTo(x, y);
      }
      ctx1.stroke();

      // Canvas 2: AS3935 RF Lightning Signal
      ctx2.clearRect(0, 0, osc2.width, osc2.height);
      ctx2.strokeStyle = "#f59e0b";
      ctx2.lineWidth = 1.5;
      ctx2.beginPath();
      for (let x = 0; x < osc2.width; x++) {
        const spike = Math.sin(step) > 0.8 && x > osc2.width * 0.6 && x < osc2.width * 0.7 ? 35 : 0;
        const y =
          osc2.height / 2 +
          Math.sin(x * 0.03 + step) * 12 +
          (Math.random() - 0.5) * 4 -
          spike;
        if (x === 0) ctx2.moveTo(x, y);
        else ctx2.lineTo(x, y);
      }
      ctx2.stroke();

      requestAnimationFrame(drawWaves);
    }
    drawWaves();
  }
  initOscilloscopes();

  // ----------------------------------------------------------------------------
  // 6. HERO TAB 3 & MAIN TERMINAL: INTERACTIVE SHELL ENGINE
  // ----------------------------------------------------------------------------
  const commands = {
    help: () =>
      "Available commands:\n• whoami: Profile and BAIUST credentials\n• projects: List 8 production projects\n• skills: 4-category tech matrix\n• hardware: ESP32-S3 TinyML & DSP specs\n• contact: Email and outreach details\n• clear: Clear terminal buffer",
    whoami: () =>
      "Md Najmus Sakib Rahatul (Student ID: 1119003)\nUndergraduate in CSE (Level 3 Term 2) at BAIUST, Cumilla.\nTeam Leader at BAIUST Computer Club Django Internship & Team BlackBerry IoT Group.",
    projects: () =>
      "[A001] BAIUST Campus Lost & Found (Django 5/PostgreSQL)\n[A002] IoT Storm Warning Box (ESP32-S3/AS3935/SIM800L)\n[A003] 512-Pt FFT Mosquito Vector Trap (ESP32-S3/INMP441)\n[A004] CodeQuest 3D Gamified Platform (Django/Three.js)\n[A005] aloron-shop E-Commerce (Next.js/TypeScript)\n[A006] SmartSpend Expense Analytics (Django/Chart.js)\n[A007] Cafe Ordering & Kitchen Queue (Java Swing)\n[A008] Signal Modulation Suite (MATLAB DSP)",
    skills: () =>
      "Backend: Python, Django 5, Next.js, REST APIs, PHP CRUD\nFrontend: TypeScript, JavaScript, React, Tailwind, Three.js\nHardware: ESP32-S3, C/C++, 512-Pt FFT, TinyML, AS3935, INMP441\nDatabases: PostgreSQL, SQLite, MySQL, Git, Linux",
    hardware: () =>
      "• Storm Early Warning: AS3935 RF lightning distance (1-40km), BMP280, BH1750, SIM800L.\n• Mosquito Trap: 16kHz I2S mic, 512-pt Radix-2 FFT (350-600Hz female vector detection, 32ms latency).",
    contact: () =>
      "Primary: mdnajmussakib2003@gmail.com\nAcademic: md.najmus.sakib.rahatul.2005@gmail.com\nLocation: Cumilla, Bangladesh (DAC UTC+6)",
  };

  // Mini-CLI Handler
  const quickInput = document.getElementById("quickcli-input");
  const quickOutput = document.getElementById("quickcli-output");
  if (quickInput && quickOutput) {
    quickInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        const cmd = quickInput.value.trim().toLowerCase();
        quickInput.value = "";
        if (!cmd) return;

        const line = document.createElement("div");
        line.className = "text-white font-bold";
        line.textContent = `$ ${cmd}`;
        quickOutput.appendChild(line);

        if (cmd === "clear") {
          quickOutput.innerHTML = "";
          return;
        }

        const resp = commands[cmd] ? commands[cmd]() : `Command not found: '${cmd}'. Type 'help' for available commands.`;
        const respLine = document.createElement("div");
        respLine.className = "text-neutral-400 whitespace-pre-line";
        respLine.textContent = resp;
        quickOutput.appendChild(respLine);

        quickOutput.scrollTop = quickOutput.scrollHeight;
      }
    });
  }

  // Section 05 Main Terminal Handler
  const mainTermInput = document.getElementById("main-terminal-input");
  const mainTermHistory = document.getElementById("main-terminal-history");
  if (mainTermInput && mainTermHistory) {
    mainTermInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        const cmd = mainTermInput.value.trim().toLowerCase();
        mainTermInput.value = "";
        if (!cmd) return;

        const line = document.createElement("div");
        line.className = "text-indigo-400 font-bold";
        line.textContent = `sakib@baiust:~$ ${cmd}`;
        mainTermHistory.appendChild(line);

        if (cmd === "clear") {
          mainTermHistory.innerHTML = '<div class="text-emerald-400">Sakib Terminal Shell [Version 3.0]</div>';
          return;
        }

        const resp = commands[cmd] ? commands[cmd]() : `zsh: command not found: ${cmd}. Type 'help'.`;
        const respLine = document.createElement("div");
        respLine.className = "text-neutral-300 whitespace-pre-line pl-2 border-l-2 border-indigo-500/30";
        respLine.textContent = resp;
        mainTermHistory.appendChild(respLine);

        mainTermHistory.scrollTop = mainTermHistory.scrollHeight;
      }
    });
  }

  // Dual Inspector Tab Switcher (Shell vs FAQ)
  const dualTabCli = document.getElementById("dual-tab-cli");
  const dualTabFaq = document.getElementById("dual-tab-faq");
  const dualPanelCli = document.getElementById("dual-panel-cli");
  const dualPanelFaq = document.getElementById("dual-panel-faq");

  if (dualTabCli && dualTabFaq && dualPanelCli && dualPanelFaq) {
    dualTabCli.addEventListener("click", () => {
      dualTabCli.classList.add("bg-indigo-600", "text-white");
      dualTabCli.classList.remove("text-neutral-400");
      dualTabFaq.classList.remove("bg-indigo-600", "text-white");
      dualTabFaq.classList.add("text-neutral-400");

      dualPanelCli.classList.remove("hidden");
      dualPanelFaq.classList.add("hidden");
    });

    dualTabFaq.addEventListener("click", () => {
      dualTabFaq.classList.add("bg-indigo-600", "text-white");
      dualTabFaq.classList.remove("text-neutral-400");
      dualTabCli.classList.remove("bg-indigo-600", "text-white");
      dualTabCli.classList.add("text-neutral-400");

      dualPanelFaq.classList.remove("hidden");
      dualPanelCli.classList.add("hidden");
    });
  }

  // Interactive FAQ Accordion
  document.querySelectorAll(".faq-item").forEach((item) => {
    item.addEventListener("click", () => {
      const ans = item.querySelector(".faq-answer");
      const chevron = item.querySelector("i");
      if (ans) {
        const isClosed = ans.classList.contains("hidden");
        ans.classList.toggle("hidden");
        if (chevron) {
          chevron.className = isClosed
            ? "fa-solid fa-chevron-up text-indigo-400 text-[10px]"
            : "fa-solid fa-chevron-down text-neutral-500 text-[10px]";
        }
      }
    });
  });

  // ----------------------------------------------------------------------------
  // 7. SELECTED WORKS: CATEGORY FILTERS & INSTANT SEARCH
  // ----------------------------------------------------------------------------
  const filterBtns = document.querySelectorAll(".project-filter-btn");
  const projectCards = document.querySelectorAll(".project-card");
  const searchInput = document.getElementById("project-search-input");

  let activeCategory = "All";
  let activeSearch = "";

  function applyProjectFilters() {
    projectCards.forEach((card) => {
      const cat = card.getAttribute("data-category") || "";
      const title = (card.getAttribute("data-title") || "").toLowerCase();
      const stack = (card.getAttribute("data-stack") || "").toLowerCase();

      const matchCat = activeCategory === "All" || cat === activeCategory;
      const matchSearch = !activeSearch || title.includes(activeSearch) || stack.includes(activeSearch);

      if (matchCat && matchSearch) {
        card.style.display = "";
      } else {
        card.style.display = "none";
      }
    });
  }

  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterBtns.forEach((b) => {
        b.classList.remove("bg-white", "text-black");
        b.classList.add("text-neutral-400");
      });
      btn.classList.add("bg-white", "text-black");
      btn.classList.remove("text-neutral-400");

      activeCategory = btn.getAttribute("data-category");
      applyProjectFilters();
    });
  });

  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      activeSearch = e.target.value.trim().toLowerCase();
      applyProjectFilters();
    });
  }

  // ----------------------------------------------------------------------------
  // 8. PROJECT STAR UPVOTE VIA AJAX
  // ----------------------------------------------------------------------------
  document.querySelectorAll(".btn-project-star").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const projectId = btn.getAttribute("data-id");
      const countEl = btn.querySelector(".star-count");

      fetch(`/api/projects/${projectId}/like/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.status === "success" && countEl) {
            countEl.textContent = data.stars_count;
            btn.classList.add("text-rose-400");
            btn.querySelector("i").className = "fa-solid fa-heart";
            showToast("Liked project!");
          }
        })
        .catch(() => {});
    });
  });

  // ----------------------------------------------------------------------------
  // 9. CASE STUDY / README MODAL DRAWER
  // ----------------------------------------------------------------------------
  const modal = document.getElementById("project-detail-modal");
  const modalCloseBtn = document.getElementById("modal-close-btn");

  function openProjectModal(p) {
    if (!modal) return;
    document.getElementById("modal-code").textContent = `${p.code} // README.md`;
    document.getElementById("modal-category").textContent = p.category;
    document.getElementById("modal-title").textContent = p.title;
    document.getElementById("modal-summary").textContent = p.summary;
    document.getElementById("modal-why").textContent = p.why_built || "Built to solve university and real-world domain requirements.";
    document.getElementById("modal-arch").textContent = p.architecture || "Modular layered MVC/MVT architecture.";
    document.getElementById("modal-highlights").textContent = p.hardware_code_highlights || "Rigorous hardware and test suite verification.";

    const techBox = document.getElementById("modal-tech-list");
    if (techBox) {
      techBox.innerHTML = "";
      (p.tech_list || p.tech_stack.split(",")).forEach((tech) => {
        const badge = document.createElement("span");
        badge.className = "px-2.5 py-1 rounded text-xs font-mono bg-white/[0.04] text-neutral-300 border border-white/[0.08]";
        badge.textContent = tech.trim();
        techBox.appendChild(badge);
      });
    }

    const githubA = document.getElementById("modal-github");
    if (githubA) {
      if (p.github_url) {
        githubA.href = p.github_url;
        githubA.style.display = "inline-flex";
      } else {
        githubA.style.display = "none";
      }
    }

    const liveA = document.getElementById("modal-live");
    if (liveA) {
      if (p.live_url) {
        liveA.href = p.live_url;
        liveA.style.display = "inline-flex";
      } else {
        liveA.style.display = "none";
      }
    }

    modal.showModal();
  }

  document.querySelectorAll(".btn-inspect-readme").forEach((btn) => {
    btn.addEventListener("click", () => {
      const code = btn.getAttribute("data-code");
      fetch(`/api/projects/${code}/`)
        .then((res) => res.json())
        .then((data) => {
          if (data.status === "success") {
            openProjectModal(data.project);
          }
        })
        .catch(() => showToast("Failed to load project details.", "error"));
    });
  });

  if (modalCloseBtn && modal) {
    modalCloseBtn.addEventListener("click", () => modal.close());
    modal.addEventListener("click", (e) => {
      const rect = modal.getBoundingClientRect();
      const inDialog =
        rect.top <= e.clientY &&
        e.clientY <= rect.top + rect.height &&
        rect.left <= e.clientX &&
        e.clientX <= rect.left + rect.width;
      if (!inDialog) modal.close();
    });
  }

  // ----------------------------------------------------------------------------
  // 10. SYSTEM ARCHITECTURE SCHEMATIC SELECTOR & LIVE NODE INSPECTOR
  // ----------------------------------------------------------------------------
  const schTab1 = document.getElementById("schematic-tab-1");
  const schTab2 = document.getElementById("schematic-tab-2");
  const schTab3 = document.getElementById("schematic-tab-3");

  const schView1 = document.getElementById("schematic-view-1");
  const schView2 = document.getElementById("schematic-view-2");
  const schView3 = document.getElementById("schematic-view-3");

  function switchSchematic(tab, view) {
    [schTab1, schTab2, schTab3].forEach((t) => {
      if (!t) return;
      t.classList.remove("bg-indigo-600", "text-white");
      t.classList.add("text-neutral-400");
    });
    [schView1, schView2, schView3].forEach((v) => {
      if (!v) return;
      v.classList.add("hidden");
    });

    if (tab) {
      tab.classList.add("bg-indigo-600", "text-white");
      tab.classList.remove("text-neutral-400");
    }
    if (view) {
      view.classList.remove("hidden");
    }
  }

  if (schTab1) schTab1.addEventListener("click", () => switchSchematic(schTab1, schView1));
  if (schTab2) schTab2.addEventListener("click", () => switchSchematic(schTab2, schView2));
  if (schTab3) schTab3.addEventListener("click", () => switchSchematic(schTab3, schView3));

  // Schematic Node Click Inspector
  document.querySelectorAll(".schematic-node").forEach((node) => {
    node.addEventListener("click", () => {
      document.querySelectorAll(".schematic-node").forEach((n) => n.classList.remove("active"));
      node.classList.add("active");

      const title = node.getAttribute("data-title") || "Component";
      const spec = node.getAttribute("data-spec") || "--";
      const latency = node.getAttribute("data-latency") || "--";
      const status = node.getAttribute("data-status") || "OK";

      const inspectorTitle = document.getElementById("inspector-title");
      const inspectorSpec = document.getElementById("inspector-spec");
      const inspectorLatency = document.getElementById("inspector-latency");
      const inspectorBus = document.getElementById("inspector-bus");
      const inspectorStatus = document.getElementById("inspector-status");

      if (inspectorTitle) inspectorTitle.textContent = title;
      if (inspectorSpec) inspectorSpec.textContent = spec;
      if (inspectorLatency) inspectorLatency.textContent = latency;
      if (inspectorBus) inspectorBus.textContent = latency.includes("us") || latency.includes("ms") ? "Hardware DMA" : "HTTP/JSON";
      if (inspectorStatus) inspectorStatus.textContent = `STATUS: ${status}`;
    });
  });

  // ----------------------------------------------------------------------------
  // 11. TECHNICAL ARSENAL: CLICK SKILL TO HIGHLIGHT RELEVANT PROJECTS
  // ----------------------------------------------------------------------------
  document.querySelectorAll(".skill-item").forEach((item) => {
    item.addEventListener("click", () => {
      const skillName = (item.getAttribute("data-skill-name") || "").toLowerCase();
      let matchedCount = 0;

      projectCards.forEach((card) => {
        const stack = (card.getAttribute("data-stack") || "").toLowerCase();
        if (stack.includes(skillName)) {
          card.classList.add("ring-2", "ring-indigo-500", "scale-[1.01]");
          matchedCount++;
          setTimeout(() => {
            card.classList.remove("ring-2", "ring-indigo-500", "scale-[1.01]");
          }, 3000);
        }
      });

      if (matchedCount > 0) {
        showToast(`Highlighted ${matchedCount} projects using ${item.getAttribute("data-skill-name")}`);
      }
    });
  });

  // ----------------------------------------------------------------------------
  // 12. 1-CLICK COPY EMAIL
  // ----------------------------------------------------------------------------
  const copyEmailBtn = document.getElementById("copy-email-btn");
  if (copyEmailBtn) {
    copyEmailBtn.addEventListener("click", () => {
      navigator.clipboard.writeText("mdnajmussakib2003@gmail.com").then(() => {
        showToast("Email address copied to clipboard!");
        copyEmailBtn.textContent = "Copied!";
        setTimeout(() => (copyEmailBtn.textContent = "Copy"), 2000);
      });
    });
  }

  // ----------------------------------------------------------------------------
  // 13. AJAX CONTACT FORM SUBMISSION
  // ----------------------------------------------------------------------------
  const contactForm = document.getElementById("contact-form");
  const contactSubmitBtn = document.getElementById("contact-submit-btn");

  if (contactForm) {
    contactForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const name = document.getElementById("sender_name").value.trim();
      const email = document.getElementById("sender_email").value.trim();
      const subject = document.getElementById("subject").value.trim();
      const message = document.getElementById("message").value.trim();

      if (!name || !email || !message) {
        showToast("Please fill in Name, Email, and Message.", "error");
        return;
      }

      if (contactSubmitBtn) {
        contactSubmitBtn.disabled = true;
        contactSubmitBtn.innerHTML = '<span>Sending...</span> <i class="fa-solid fa-spinner fa-spin text-xs"></i>';
      }

      fetch("/api/contact/", {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          sender_name: name,
          sender_email: email,
          subject: subject,
          message: message,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.status === "success") {
            showToast(data.message || "Message delivered successfully!", "success");
            contactForm.reset();
          } else {
            showToast(data.message || "Could not deliver message.", "error");
          }
        })
        .catch(() => {
          showToast("Network error. Please reach out directly via email.", "error");
        })
        .finally(() => {
          if (contactSubmitBtn) {
            contactSubmitBtn.disabled = false;
            contactSubmitBtn.innerHTML = '<span>Send Message</span> <i class="fa-solid fa-paper-plane text-xs"></i>';
          }
        });
    });
  }

  // ----------------------------------------------------------------------------
  // 14. CMD+K COMMAND PALETTE MODAL
  // ----------------------------------------------------------------------------
  const cmdkModal = document.getElementById("cmdk-modal");
  const cmdkTriggerBtn = document.getElementById("cmdk-trigger-btn");
  const cmdkInput = document.getElementById("cmdk-input");

  if (cmdkModal) {
    function toggleCmdk() {
      if (cmdkModal.open) {
        cmdkModal.close();
      } else {
        cmdkModal.showModal();
        if (cmdkInput) {
          cmdkInput.value = "";
          cmdkInput.focus();
        }
      }
    }

    if (cmdkTriggerBtn) cmdkTriggerBtn.addEventListener("click", toggleCmdk);

    window.addEventListener("keydown", (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        toggleCmdk();
      }
    });

    document.querySelectorAll(".cmdk-item").forEach((item) => {
      item.addEventListener("click", () => cmdkModal.close());
    });

    cmdkModal.addEventListener("click", (e) => {
      const rect = cmdkModal.getBoundingClientRect();
      const inDialog =
        rect.top <= e.clientY &&
        e.clientY <= rect.top + rect.height &&
        rect.left <= e.clientX &&
        e.clientX <= rect.left + rect.width;
      if (!inDialog) cmdkModal.close();
    });
  }
});
