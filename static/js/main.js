/**
 * Apple & Heva-Grade Human Portfolio Controller
 * Md Najmus Sakib Rahatul (Student ID: 1119003) — BAIUST
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

document.addEventListener("DOMContentLoaded", () => {
  // 1. Live Cumilla Time (DAC • UTC+6)
  const clockEl = document.getElementById("dac-clock");
  if (clockEl) {
    function updateClock() {
      const now = new Date();
      const options = {
        timeZone: "Asia/Dhaka",
        hour: "2-digit",
        minute: "2-digit",
        hour12: true,
      };
      clockEl.textContent = `DAC ${now.toLocaleTimeString("en-US", options)}`;
    }
    updateClock();
    setInterval(updateClock, 1000);
  }

  // 2. Minimalist Theme Switcher (Obsidian Dark vs Studio Light)
  const themeToggle = document.getElementById("theme-toggle");
  const savedTheme = localStorage.getItem("sakib_theme_clean");
  if (savedTheme === "light") {
    document.body.classList.add("light-mode");
    if (themeToggle) themeToggle.textContent = "Light";
  }

  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      document.body.classList.toggle("light-mode");
      const isLight = document.body.classList.contains("light-mode");
      themeToggle.textContent = isLight ? "Light" : "Dark";
      localStorage.setItem("sakib_theme_clean", isLight ? "light" : "dark");
    });
  }

  // 3. Category Filter Tabs for Works
  const filterBtns = document.querySelectorAll(".project-filter-btn");
  const projectCards = document.querySelectorAll(".project-card");
  const searchInput = document.getElementById("project-search-input");

  let currentCategory = "All";
  let currentSearch = "";

  function filterProjects() {
    let visibleCount = 0;
    projectCards.forEach((card) => {
      const cardCategory = card.getAttribute("data-category");
      const cardTitle = (card.getAttribute("data-title") || "").toLowerCase();
      const cardStack = (card.getAttribute("data-stack") || "").toLowerCase();

      const matchesCat = currentCategory === "All" || cardCategory === currentCategory;
      const matchesSearch =
        !currentSearch ||
        cardTitle.includes(currentSearch) ||
        cardStack.includes(currentSearch);

      if (matchesCat && matchesSearch) {
        card.style.display = "flex";
        visibleCount++;
      } else {
        card.style.display = "none";
      }
    });

    const emptyState = document.getElementById("projects-empty-state");
    if (emptyState) {
      emptyState.style.display = visibleCount === 0 ? "block" : "none";
    }
  }

  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterBtns.forEach((b) => {
        b.classList.remove("bg-white", "text-black", "dark:bg-white", "dark:text-black", "border-transparent", "shadow-sm");
        b.classList.add("text-neutral-400", "hover:text-neutral-200");
      });
      btn.classList.add("bg-white", "text-black", "dark:bg-white", "dark:text-black", "border-transparent", "shadow-sm");
      btn.classList.remove("text-neutral-400", "hover:text-neutral-200");

      currentCategory = btn.getAttribute("data-category");
      filterProjects();
    });
  });

  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      currentSearch = e.target.value.trim().toLowerCase();
      filterProjects();
    });
  }

  // 4. Case-Study Modal Trigger
  const modal = document.getElementById("project-detail-modal");
  const modalCloseBtn = document.getElementById("modal-close-btn");

  window.openProjectModal = function (p) {
    if (!modal) return;

    document.getElementById("modal-title").textContent = p.title;
    document.getElementById("modal-category").textContent = p.category;
    document.getElementById("modal-summary").textContent = p.summary;
    document.getElementById("modal-why").textContent = p.why_built || "Built to address core engineering constraints.";
    document.getElementById("modal-arch").textContent = p.architecture || "Modular layered design.";
    document.getElementById("modal-highlights").textContent = p.hardware_code_highlights || "Standard test verification passed.";

    const techBox = document.getElementById("modal-tech-list");
    if (techBox) {
      techBox.innerHTML = "";
      (p.tech_list || p.tech_stack.split(",")).forEach((tech) => {
        const span = document.createElement("span");
        span.className = "px-2.5 py-1 rounded-md text-xs font-mono bg-neutral-800 text-neutral-300 border border-neutral-700/60";
        span.textContent = tech.trim();
        techBox.appendChild(span);
      });
    }

    const githubLink = document.getElementById("modal-github");
    if (githubLink) {
      if (p.github_url) {
        githubLink.href = p.github_url;
        githubLink.style.display = "inline-flex";
      } else {
        githubLink.style.display = "none";
      }
    }

    const liveLink = document.getElementById("modal-live");
    if (liveLink) {
      if (p.live_url) {
        liveLink.href = p.live_url;
        liveLink.style.display = "inline-flex";
      } else {
        liveLink.style.display = "none";
      }
    }

    modal.showModal();
  };

  document.querySelectorAll(".btn-view-details").forEach((btn) => {
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
    modalCloseBtn.addEventListener("click", () => modal.close());
  }

  if (modal) {
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

  // 5. Project Star Upvote Counter
  document.querySelectorAll(".btn-project-star").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const projectId = btn.getAttribute("data-project-id");
      const starSpan = btn.querySelector(".star-count");

      fetch(`/api/projects/${projectId}/like/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.status === "success" && starSpan) {
            starSpan.textContent = data.stars_count;
            btn.classList.add("text-indigo-400");
          }
        })
        .catch(() => {});
    });
  });

  // 6. Clean AJAX Contact Form Submission
  const contactForm = document.getElementById("contact-form");
  const contactFeedback = document.getElementById("contact-feedback");
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
        contactSubmitBtn.textContent = "Sending...";
      }

      const payload = {
        sender_name: name,
        sender_email: email,
        subject: subject,
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
          } else {
            showToast(data.message || "Unable to send message.", "error");
          }
        })
        .catch(() => {
          showToast("Network error. Please try again or reach out via email.", "error");
        })
        .finally(() => {
          if (contactSubmitBtn) {
            contactSubmitBtn.disabled = false;
            contactSubmitBtn.textContent = "Send Message";
          }
        });
    });
  }

  function showToast(msg, type = "success") {
    if (!contactFeedback) return;
    contactFeedback.className = `p-4 rounded-xl text-xs font-medium transition ${
      type === "success"
        ? "bg-emerald-500/10 border border-emerald-500/30 text-emerald-300"
        : "bg-rose-500/10 border border-rose-500/30 text-rose-300"
    }`;
    contactFeedback.textContent = msg;
    contactFeedback.classList.remove("hidden");
    setTimeout(() => {
      contactFeedback.classList.add("hidden");
    }, 5000);
  }
});
