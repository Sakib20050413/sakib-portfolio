/**
 * main.js
 * Primary Frontend Controller & DOM Orchestrator
 * Md Najmus Sakib Rahatul (ID: 1119003) - BAIUST
 */

// CSRF Token Helper
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

// Web Audio API Synthesizer Sound FX
let audioCtx = null;
let soundEnabled = true;

function initAudio() {
  if (!audioCtx) {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (AudioContext) audioCtx = new AudioContext();
  }
}

window.playSynthClick = function (freq = 440, duration = 0.04) {
  if (!soundEnabled) return;
  try {
    initAudio();
    if (!audioCtx) return;
    if (audioCtx.state === "suspended") audioCtx.resume();

    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();

    osc.type = "sine";
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

    gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);

    osc.connect(gain);
    gain.connect(audioCtx.destination);

    osc.start();
    osc.stop(audioCtx.currentTime + duration);
  } catch (e) {
    // Audio context may be restricted before user gesture
  }
};

document.addEventListener("DOMContentLoaded", () => {
  // 1. Terminal Boot Preloader (0% -> 100%)
  const preloader = document.getElementById("boot-preloader");
  const preloaderBar = document.getElementById("preloader-progress-bar");
  const preloaderPercent = document.getElementById("preloader-percent");

  if (preloader) {
    let progress = 0;
    const interval = setInterval(() => {
      progress += Math.floor(Math.random() * 15) + 8;
      if (progress > 100) progress = 100;

      if (preloaderBar) preloaderBar.style.width = `${progress}%`;
      if (preloaderPercent) preloaderPercent.textContent = `${progress}%`;

      if (progress >= 100) {
        clearInterval(interval);
        setTimeout(() => {
          preloader.classList.add("fade-out");
          setTimeout(() => preloader.remove(), 600);
        }, 300);
      }
    }, 45);
  }

  // 2. Sound Toggle Button
  const soundToggleBtn = document.getElementById("btn-sound-toggle");
  if (soundToggleBtn) {
    soundToggleBtn.addEventListener("click", () => {
      soundEnabled = !soundEnabled;
      soundToggleBtn.textContent = soundEnabled ? "🔊 SOUND: ON" : "🔇 SOUND: OFF";
      soundToggleBtn.classList.toggle("text-purple-400", soundEnabled);
      soundToggleBtn.classList.toggle("text-slate-500", !soundEnabled);
      if (soundEnabled) window.playSynthClick(520);
    });
  }

  // 3. Live Cumilla / Dhaka (DAC • UTC+6) Clock
  const clockEl = document.getElementById("live-clock");
  if (clockEl) {
    function updateClock() {
      const now = new Date();
      // Format as 12-hour with seconds
      const options = {
        timeZone: "Asia/Dhaka",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: true,
      };
      clockEl.textContent = `DAC (UTC+6) • ${now.toLocaleTimeString("en-US", options)}`;
    }
    updateClock();
    setInterval(updateClock, 1000);
  }

  // 4. Live FPS Telemetry Badge
  const fpsBadge = document.getElementById("fps-badge");
  if (fpsBadge) {
    let lastTime = performance.now();
    let frameCount = 0;
    function calcFps(now) {
      frameCount++;
      if (now - lastTime >= 1000) {
        const fps = Math.round((frameCount * 1000) / (now - lastTime));
        fpsBadge.textContent = `${fps} FPS`;
        frameCount = 0;
        lastTime = now;
      }
      requestAnimationFrame(calcFps);
    }
    requestAnimationFrame(calcFps);
  }

  // 5. Theme Switcher (Dark Cyber vs Editorial Light)
  const themeToggle = document.getElementById("theme-toggle");
  const savedTheme = localStorage.getItem("sakib_theme");
  if (savedTheme === "light") {
    document.body.classList.add("light-mode");
    if (themeToggle) themeToggle.textContent = "☀️ LIGHT";
  }

  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      document.body.classList.toggle("light-mode");
      const isLight = document.body.classList.contains("light-mode");
      themeToggle.textContent = isLight ? "☀️ LIGHT" : "🌙 CYBER";
      localStorage.setItem("sakib_theme", isLight ? "light" : "dark");
      window.playSynthClick(440);
    });
  }

  // 6. Mode Switcher (Bento UI vs Full Terminal View)
  const modeToggle = document.getElementById("mode-toggle");
  const terminalWindow = document.getElementById("terminal-window");
  if (modeToggle && terminalWindow) {
    modeToggle.addEventListener("click", () => {
      terminalWindow.classList.toggle("fullscreen-mode");
      const isFull = terminalWindow.classList.contains("fullscreen-mode");
      modeToggle.textContent = isFull ? "🪟 BENTO MODE" : "💻 TERMINAL MODE";
      modeToggle.classList.toggle("bg-purple-600", isFull);
      window.playSynthClick(580);
    });
  }

  // 7. Mouse Cursor Spotlight Effect
  document.addEventListener("mousemove", (e) => {
    document.documentElement.style.setProperty("--mouse-x", `${e.clientX}px`);
    document.documentElement.style.setProperty("--mouse-y", `${e.clientY}px`);
  });

  // 8. Typewriter Effect for Hero Badge
  const typewriterEl = document.getElementById("typewriter-text");
  if (typewriterEl) {
    const roles = [
      "Full-Stack Web Developer (Django • Next.js)",
      "Embedded AI & TinyML Researcher (ESP32-S3)",
      "512-Point Radix-2 FFT DSP Engineer",
      "Lead @ BAIUST Computer Club Django Internship",
    ];
    let roleIdx = 0;
    let charIdx = 0;
    let isDeleting = false;

    function typeLoop() {
      const currentRole = roles[roleIdx];
      if (isDeleting) {
        charIdx--;
        typewriterEl.textContent = currentRole.substring(0, charIdx);
      } else {
        charIdx++;
        typewriterEl.textContent = currentRole.substring(0, charIdx);
      }

      let speed = isDeleting ? 30 : 60;

      if (!isDeleting && charIdx === currentRole.length) {
        speed = 1800; // pause at end
        isDeleting = true;
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        roleIdx = (roleIdx + 1) % roles.length;
        speed = 400;
      }

      setTimeout(typeLoop, speed);
    }
    typeLoop();
  }

  // 9. Bento Grid Projects Filtering & Search
  const filterBtns = document.querySelectorAll(".project-filter-btn");
  const projectSearchInput = document.getElementById("project-search-input");
  const projectCards = document.querySelectorAll(".project-card");

  let currentCategory = "All";
  let currentSearch = "";

  function applyProjectFilters() {
    let visibleCount = 0;
    projectCards.forEach((card) => {
      const cardCategory = card.getAttribute("data-category");
      const cardTitle = (card.getAttribute("data-title") || "").toLowerCase();
      const cardStack = (card.getAttribute("data-stack") || "").toLowerCase();
      const cardCode = (card.getAttribute("data-project-code") || "").toLowerCase();

      const matchesCat = currentCategory === "All" || cardCategory === currentCategory;
      const matchesSearch =
        !currentSearch ||
        cardTitle.includes(currentSearch) ||
        cardStack.includes(currentSearch) ||
        cardCode.includes(currentSearch);

      if (matchesCat && matchesSearch) {
        card.style.display = "flex";
        visibleCount++;
      } else {
        card.style.display = "none";
      }
    });

    const noResults = document.getElementById("projects-empty-state");
    if (noResults) {
      noResults.style.display = visibleCount === 0 ? "block" : "none";
    }
  }

  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterBtns.forEach((b) => {
        b.classList.remove("bg-purple-600", "text-white");
        b.classList.add("bg-slate-900/60", "text-slate-400");
      });
      btn.classList.add("bg-purple-600", "text-white");
      btn.classList.remove("bg-slate-900/60", "text-slate-400");

      currentCategory = btn.getAttribute("data-category");
      applyProjectFilters();
      window.playSynthClick(360);
    });
  });

  if (projectSearchInput) {
    projectSearchInput.addEventListener("input", (e) => {
      currentSearch = e.target.value.trim().toLowerCase();
      applyProjectFilters();
    });
  }

  // 10. AJAX Project Upvote / Star Counter
  document.querySelectorAll(".btn-project-star").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const projectId = btn.getAttribute("data-project-id");
      const starCountSpan = btn.querySelector(".star-count");

      btn.classList.add("scale-125");
      setTimeout(() => btn.classList.remove("scale-125"), 200);

      fetch(`/api/projects/${projectId}/like/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.status === "success" && starCountSpan) {
            starCountSpan.textContent = data.stars_count;
            btn.classList.add("text-amber-400");
            window.playSynthClick(640);
          }
        })
        .catch(() => {});
    });
  });

  // 11. macOS Case-Study Modal Dialog Handler
  const modal = document.getElementById("casestudy-modal");
  const modalCloseBtn = document.getElementById("modal-close-btn");
  const modalTabs = document.querySelectorAll(".modal-tab-btn");
  const modalPanels = document.querySelectorAll(".modal-tab-panel");

  window.openProjectModal = function (p) {
    if (!modal) return;

    document.getElementById("modal-project-code").textContent = p.code;
    document.getElementById("modal-project-title").textContent = p.title;
    document.getElementById("modal-project-category").textContent = p.category;
    document.getElementById("modal-project-summary").textContent = p.summary;
    document.getElementById("modal-project-why").textContent = p.why_built || "Documented during engineering sprint.";
    document.getElementById("modal-project-arch").textContent = p.architecture || "Modular layered architecture.";
    document.getElementById("modal-project-highlights").textContent = p.hardware_code_highlights || "Full stack verification passed.";

    // Tech stack badges
    const techBox = document.getElementById("modal-project-tech");
    if (techBox) {
      techBox.innerHTML = "";
      (p.tech_list || p.tech_stack.split(",")).forEach((tech) => {
        const span = document.createElement("span");
        span.className = "px-2.5 py-1 text-xs rounded-md bg-purple-500/20 text-purple-300 border border-purple-500/30 mono";
        span.textContent = tech.trim();
        techBox.appendChild(span);
      });
    }

    // Links
    const githubLink = document.getElementById("modal-github-link");
    if (githubLink) {
      if (p.github_url) {
        githubLink.href = p.github_url;
        githubLink.style.display = "inline-flex";
      } else {
        githubLink.style.display = "none";
      }
    }

    const liveLink = document.getElementById("modal-live-link");
    if (liveLink) {
      if (p.live_url) {
        liveLink.href = p.live_url;
        liveLink.style.display = "inline-flex";
      } else {
        liveLink.style.display = "none";
      }
    }

    // Reset to Tab 1
    modalTabs.forEach((t) => t.classList.remove("active", "bg-purple-600", "text-white"));
    modalPanels.forEach((pan) => pan.classList.add("hidden"));
    if (modalTabs[0]) {
      modalTabs[0].classList.add("active", "bg-purple-600", "text-white");
    }
    if (modalPanels[0]) {
      modalPanels[0].classList.remove("hidden");
    }

    modal.showModal();
    window.playSynthClick(500);
  };

  // Attach click listener on each card's "View Case Study" button
  document.querySelectorAll(".btn-view-casestudy").forEach((btn) => {
    btn.addEventListener("click", () => {
      const card = btn.closest(".project-card");
      const code = card.getAttribute("data-project-code");

      fetch(`/api/projects/${code}/`)
        .then((res) => res.json())
        .then((data) => {
          if (data.status === "success") {
            window.openProjectModal(data.project);
          }
        });
    });
  });

  if (modalCloseBtn && modal) {
    modalCloseBtn.addEventListener("click", () => {
      modal.close();
      window.playSynthClick(320);
    });
  }

  // Close modal when clicking on the backdrop
  if (modal) {
    modal.addEventListener("click", (e) => {
      const rect = modal.getBoundingClientRect();
      const isInDialog =
        rect.top <= e.clientY &&
        e.clientY <= rect.top + rect.height &&
        rect.left <= e.clientX &&
        e.clientX <= rect.left + rect.width;
      if (!isInDialog) modal.close();
    });
  }

  // Modal Tab Switching
  modalTabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      const targetPanelId = tab.getAttribute("data-target-panel");
      modalTabs.forEach((t) => {
        t.classList.remove("bg-purple-600", "text-white");
        t.classList.add("bg-slate-900/60", "text-slate-400");
      });
      tab.classList.add("bg-purple-600", "text-white");
      tab.classList.remove("bg-slate-900/60", "text-slate-400");

      modalPanels.forEach((pan) => {
        pan.classList.toggle("hidden", pan.id !== targetPanelId);
      });
      window.playSynthClick(460);
    });
  });

  // 12. AJAX Contact Form Submission
  const contactForm = document.getElementById("contact-form");
  const contactFeedback = document.getElementById("contact-feedback");
  const contactSubmitBtn = document.getElementById("contact-submit-btn");

  if (contactForm) {
    contactForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const senderName = document.getElementById("sender_name").value.trim();
      const senderEmail = document.getElementById("sender_email").value.trim();
      const subject = document.getElementById("subject").value.trim();
      const projectType = document.getElementById("project_type").value;
      const message = document.getElementById("message").value.trim();

      if (!senderName || !senderEmail || !message) {
        showToast("Please fill in Name, Email, and Message.", "error");
        return;
      }

      if (contactSubmitBtn) {
        contactSubmitBtn.disabled = true;
        contactSubmitBtn.textContent = "Transmitting to Inbox...";
      }

      const payload = {
        sender_name: senderName,
        sender_email: senderEmail,
        subject: subject,
        project_type: projectType,
        message: message,
      };

      fetch("/api/contact/", {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.status === "success") {
            showToast(data.message, "success");
            contactForm.reset();
            window.playSynthClick(720);
          } else {
            showToast(data.message || "Failed to send message.", "error");
          }
        })
        .catch(() => {
          showToast("Network error occurred while transmitting message.", "error");
        })
        .finally(() => {
          if (contactSubmitBtn) {
            contactSubmitBtn.disabled = false;
            contactSubmitBtn.textContent = "Send Encrypted Message";
          }
        });
    });
  }

  function showToast(msg, type = "success") {
    if (!contactFeedback) return;
    contactFeedback.className = `p-4 rounded-xl text-sm font-medium transition ${
      type === "success"
        ? "bg-emerald-500/10 border border-emerald-500/30 text-emerald-300"
        : "bg-rose-500/10 border border-rose-500/30 text-rose-300"
    }`;
    contactFeedback.textContent = msg;
    contactFeedback.classList.remove("hidden");
    setTimeout(() => {
      contactFeedback.classList.add("hidden");
    }, 6000);
  }
});
