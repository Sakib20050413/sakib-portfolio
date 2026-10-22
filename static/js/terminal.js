/**
 * terminal.js
 * Interactive macOS Terminal Emulator (sakib@baiust:~$)
 * Md Najmus Sakib Rahatul (ID: 1119003) - BAIUST
 */

document.addEventListener("DOMContentLoaded", () => {
  const terminalWindow = document.getElementById("terminal-window");
  const terminalBody = document.getElementById("terminal-body");
  const terminalInput = document.getElementById("terminal-input");
  const trafficRed = document.getElementById("traffic-red");
  const trafficYellow = document.getElementById("traffic-yellow");
  const trafficGreen = document.getElementById("traffic-green");

  if (!terminalInput || !terminalBody) return;

  const commandHistory = [];
  let historyIndex = -1;

  const validCommands = [
    "help",
    "whoami",
    "about",
    "projects",
    "open",
    "skills",
    "hardware",
    "contact",
    "admin",
    "clear",
    "theme",
    "date",
    "sudo",
  ];

  // Focus input when clicking anywhere inside terminal body
  terminalBody.parentElement.addEventListener("click", () => {
    terminalInput.focus();
  });

  // Traffic Light Controls
  if (trafficRed) {
    trafficRed.addEventListener("click", () => {
      terminalBody.innerHTML = `
        <div class="text-rose-400 mb-2">[Session Reset] Terminal history wiped by user.</div>
      `;
    });
  }

  if (trafficYellow) {
    trafficYellow.addEventListener("click", () => {
      terminalBody.classList.toggle("hidden");
    });
  }

  if (trafficGreen) {
    trafficGreen.addEventListener("click", () => {
      terminalWindow.classList.toggle("fullscreen-mode");
      if (terminalWindow.classList.contains("fullscreen-mode")) {
        trafficGreen.title = "Exit Fullscreen";
      } else {
        trafficGreen.title = "Fullscreen";
      }
    });
  }

  // Handle Command Submission
  terminalInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      const rawInput = terminalInput.value.trim();
      terminalInput.value = "";
      if (rawInput) {
        commandHistory.push(rawInput);
        historyIndex = commandHistory.length;
        executeCommand(rawInput);
      }
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      if (historyIndex > 0) {
        historyIndex--;
        terminalInput.value = commandHistory[historyIndex];
      }
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      if (historyIndex < commandHistory.length - 1) {
        historyIndex++;
        terminalInput.value = commandHistory[historyIndex];
      } else {
        historyIndex = commandHistory.length;
        terminalInput.value = "";
      }
    } else if (e.key === "Tab") {
      e.preventDefault();
      const current = terminalInput.value.trim().toLowerCase();
      const match = validCommands.find((cmd) => cmd.startsWith(current));
      if (match) terminalInput.value = match;
    }
  });

  function executeCommand(input) {
    const parts = input.split(" ");
    const cmd = parts[0].toLowerCase();
    const arg = parts[1] ? parts[1].toUpperCase() : "";

    // Echo command to output
    appendOutput(`
      <div class="flex items-center gap-2 mt-2 font-mono">
        <span class="text-sky-400 font-semibold">sakib@baiust</span>
        <span class="text-slate-500">:</span>
        <span class="text-emerald-400">~</span>
        <span class="text-slate-400">$</span>
        <span class="text-white">${escapeHtml(input)}</span>
      </div>
    `);

    // Sound effect
    if (window.playSynthClick) window.playSynthClick(440);

    switch (cmd) {
      case "help":
        appendOutput(`
          <div class="text-slate-300 space-y-1 my-2 pl-2 border-l-2 border-purple-500/40">
            <div><span class="text-purple-400 font-semibold">help</span> : Show this list of executable terminal commands</div>
            <div><span class="text-purple-400 font-semibold">whoami / about</span> : Sakib's academic profile & BAIUST research summary</div>
            <div><span class="text-purple-400 font-semibold">projects</span> : Index listing of all 8 portfolio projects</div>
            <div><span class="text-purple-400 font-semibold">open &lt;CODE&gt;</span> : Launch Case-Study modal (e.g. <code class="text-amber-300">open A001</code>)</div>
            <div><span class="text-purple-400 font-semibold">skills</span> : Trigger physics impulse in tech ball pit & jump to section</div>
            <div><span class="text-purple-400 font-semibold">hardware</span> : Inspect ESP32-S3 TinyML Pinout Visualizer</div>
            <div><span class="text-purple-400 font-semibold">contact</span> : Jump to Hire Me / Inquiry form</div>
            <div><span class="text-purple-400 font-semibold">admin</span> : Authenticate and enter Custom Admin CMS (/dashboard/)</div>
            <div><span class="text-purple-400 font-semibold">theme</span> : Toggle between Cyber Dark and Editorial Light mode</div>
            <div><span class="text-purple-400 font-semibold">date</span> : Check Cumilla, Bangladesh local server time</div>
            <div><span class="text-purple-400 font-semibold">clear</span> : Clear terminal display history</div>
          </div>
        `);
        break;

      case "whoami":
      case "about":
        appendOutput(`
          <div class="my-2 p-3 bg-slate-900/80 rounded-lg border border-slate-800 text-sm">
            <div class="text-purple-400 font-bold text-base">Md Najmus Sakib Rahatul</div>
            <div class="text-slate-400 text-xs mt-0.5">Student ID: <span class="text-white font-mono">1119003</span> • Dept. of CSE, BAIUST, Cumilla</div>
            <div class="text-slate-300 mt-2 text-xs leading-relaxed">
              Full-Stack Developer (Django 5, Next.js, PostgreSQL) & Embedded AI / TinyML Researcher.
              Team Leader of Team BlackBerry (CSE 301 IDP & CSE 326) and Team 03 in the BAIUST Computer Club Django Internship.
            </div>
            <div class="text-xs text-sky-400 font-mono mt-2">
              Status: Open to Software Engineering Internships & Remote AI Roles
            </div>
          </div>
        `);
        break;

      case "projects":
        appendOutput(`
          <div class="my-2 space-y-1 text-xs font-mono">
            <div class="text-slate-400 font-bold mb-1">AVAILABLE PORTFOLIO PROJECTS:</div>
            <div><span class="text-amber-400 font-bold">[A001]</span> BAIUST Campus Lost & Found System (Django 5, Multi-Zone Matching)</div>
            <div><span class="text-amber-400 font-bold">[A002]</span> IoT Storm & Lightning Early Warning Box (ESP32-S3, AS3935, TinyML)</div>
            <div><span class="text-amber-400 font-bold">[A003]</span> 512-Point FFT Bio-Acoustic Mosquito Vector Trap (ESP32-S3, DSP, I2S)</div>
            <div><span class="text-amber-400 font-bold">[A004]</span> CodeQuest BD: Gamified Multi-Language Coding Platform (CSE 324)</div>
            <div><span class="text-amber-400 font-bold">[A005]</span> aloron-shop: Modern Full-Stack E-Commerce Platform (Next.js)</div>
            <div><span class="text-amber-400 font-bold">[A006]</span> SmartSpend: Personal Expense & Budget Analytics System (Django)</div>
            <div><span class="text-amber-400 font-bold">[A007]</span> Cafe Ordering & Kitchen Queue Management System (Java Swing)</div>
            <div><span class="text-amber-400 font-bold">[A008]</span> Analog & Digital Signal Modulation Suite (MATLAB DSP, CSE 322)</div>
            <div class="text-purple-400 mt-2">Tip: Type <code class="text-white">open A001</code> to view full architectural case study!</div>
          </div>
        `);
        break;

      case "open":
        if (!arg) {
          appendOutput(`<div class="text-rose-400 text-xs">Error: Please provide a project code. Example: <code class="text-white">open A001</code></div>`);
        } else {
          const targetCard = document.querySelector(`[data-project-code="${arg}"]`);
          if (targetCard) {
            appendOutput(`<div class="text-emerald-400 text-xs">Opening Case-Study Modal for project [${arg}]...</div>`);
            const viewBtn = targetCard.querySelector(".btn-view-casestudy");
            if (viewBtn) viewBtn.click();
          } else {
            // Try fetching via API
            fetch(`/api/projects/${arg}/`)
              .then((res) => res.json())
              .then((data) => {
                if (data.status === "success") {
                  if (window.openProjectModal) {
                    window.openProjectModal(data.project);
                    appendOutput(`<div class="text-emerald-400 text-xs">Case-Study Modal [${arg}] opened.</div>`);
                  }
                } else {
                  appendOutput(`<div class="text-rose-400 text-xs">Project code [${arg}] not found. Type <code class="text-white">projects</code> to inspect valid codes.</div>`);
                }
              })
              .catch(() => {
                appendOutput(`<div class="text-rose-400 text-xs">Project code [${arg}] not found.</div>`);
              });
          }
        }
        break;

      case "skills":
        appendOutput(`<div class="text-purple-400 text-xs">Triggering elastic collision impulse in Physics Ball Pit...</div>`);
        if (window.triggerSkillImpulse) window.triggerSkillImpulse();
        const skillSec = document.getElementById("skills-section");
        if (skillSec) skillSec.scrollIntoView({ behavior: "smooth" });
        break;

      case "hardware":
        appendOutput(`<div class="text-cyan-400 text-xs">Navigating to ESP32-S3 Hardware Pinout Visualizer...</div>`);
        const hwSec = document.getElementById("hardware-section");
        if (hwSec) hwSec.scrollIntoView({ behavior: "smooth" });
        break;

      case "contact":
        appendOutput(`<div class="text-emerald-400 text-xs">Focusing contact message input...</div>`);
        const contactSec = document.getElementById("contact-section");
        if (contactSec) {
          contactSec.scrollIntoView({ behavior: "smooth" });
          const nameInput = document.getElementById("sender_name");
          if (nameInput) setTimeout(() => nameInput.focus(), 600);
        }
        break;

      case "admin":
        appendOutput(`<div class="text-amber-400 text-xs">Redirecting to Admin CMS (/dashboard/)...</div>`);
        setTimeout(() => {
          window.location.href = "/dashboard/";
        }, 600);
        break;

      case "theme":
        document.body.classList.toggle("light-mode");
        const currentTheme = document.body.classList.contains("light-mode") ? "Editorial Light" : "Cyber Dark";
        appendOutput(`<div class="text-sky-400 text-xs">Theme toggled to: <strong class="text-white">${currentTheme}</strong></div>`);
        break;

      case "date":
        const now = new Date();
        appendOutput(`<div class="text-slate-300 text-xs font-mono">Cumilla, Bangladesh (DAC): ${now.toUTCString()} (Local: ${now.toLocaleTimeString()})</div>`);
        break;

      case "sudo":
        appendOutput(`<div class="text-rose-400 text-xs font-mono">[ACCESS DENIED] User 'sakib' is in sudoers file, but admin privileges require web authentication at <a href="/dashboard/" class="underline text-white">/dashboard/</a>.</div>`);
        break;

      case "clear":
        terminalBody.innerHTML = "";
        return;

      default:
        appendOutput(`
          <div class="text-rose-400 text-xs font-mono">
            zsh: command not found: ${escapeHtml(input)}. Type <code class="text-purple-300">help</code> for list of commands.
          </div>
        `);
        break;
    }

    // Scroll to bottom
    terminalBody.scrollTop = terminalBody.scrollHeight;
  }

  function appendOutput(html) {
    const div = document.createElement("div");
    div.innerHTML = html;
    terminalBody.appendChild(div);
  }

  function escapeHtml(str) {
    return str
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }
});
