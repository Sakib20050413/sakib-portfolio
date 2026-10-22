/**
 * imessage_faq.js
 * Interactive iMessage Chat-Bubble FAQ Component
 * Md Najmus Sakib Rahatul (ID: 1119003) - BAIUST
 */

document.addEventListener("DOMContentLoaded", () => {
  const faqData = {
    stack: {
      question: "What is your strongest tech stack?",
      answer: "My core production stack is **Python (Django 5)**, **Next.js (TypeScript)**, and **PostgreSQL** on the web side. For embedded systems and Edge AI, I work heavily with **C++ on ESP32-S3**, using hardware FPU Radix-2 FFT DSP and TinyML classifiers. I build full end-to-end architectures from database schema to hardware telemetry."
    },
    deploy: {
      question: "Can you build & deploy full-stack Django/Next.js apps?",
      answer: "Yes, absolutely! Every project I engineer is built for production: configured with **WhiteNoise** for static assets, **dj-database-url** for automated PostgreSQL cloud connection (Neon / Supabase), **Gunicorn/Procfile** for containerized hosting, and CI/CD pipelines on Render or Vercel."
    },
    research: {
      question: "Tell me about your BAIUST research projects",
      answer: "I lead **Team BlackBerry** at BAIUST under Assistant Professor Arifur Rahaman and Lecturer Md. Fahim Kabir Chowdhury. We've built: 1) An IoT Storm & Lightning Warning Box combining 500 kHz RF detection with atmospheric sensor fusion and a Bangla Voice Siren; 2) A 512-Point FFT Bio-Acoustic Mosquito Trap capturing female vectors in 32ms without hurting bees. Both are targeting IEEE publications!"
    },
    internships: {
      question: "Are you available for internships or remote work?",
      answer: "Yes! I am actively looking for **Software Engineering Internships**, **Remote Full-Stack AI Roles**, and **Academic Research Collaborations**. You can reach me directly via the Contact Form below or at `mdnajmussakib2003@gmail.com`."
    }
  };

  const chatContainer = document.getElementById("faq-chat-container");
  const pills = document.querySelectorAll(".faq-pill");

  if (!chatContainer || pills.length === 0) return;

  pills.forEach((pill) => {
    pill.addEventListener("click", () => {
      const key = pill.getAttribute("data-faq-key");
      const item = faqData[key];
      if (!item) return;

      // Disable pill temporarily
      pill.classList.add("opacity-50", "pointer-events-none");

      // 1. Append User Question Bubble
      appendUserBubble(item.question);

      // 2. Append Typing Indicator
      const typingIndicator = appendTypingIndicator();
      chatContainer.scrollTop = chatContainer.scrollHeight;

      if (window.playSynthClick) window.playSynthClick(480);

      // 3. After 800ms, replace indicator with Sakib's reply
      setTimeout(() => {
        typingIndicator.remove();
        appendSakibBubble(item.answer);
        chatContainer.scrollTop = chatContainer.scrollHeight;
        pill.classList.remove("opacity-50", "pointer-events-none");
        if (window.playSynthClick) window.playSynthClick(580);
      }, 900);
    });
  });

  function appendUserBubble(text) {
    const bubble = document.createElement("div");
    bubble.className = "flex justify-end mb-3 animate-fade-in";
    bubble.innerHTML = `
      <div class="max-w-xs sm:max-w-md bg-purple-600 text-white px-4 py-2.5 rounded-2xl rounded-tr-sm text-sm shadow-md">
        ${escapeHtml(text)}
      </div>
    `;
    chatContainer.appendChild(bubble);
  }

  function appendTypingIndicator() {
    const indicator = document.createElement("div");
    indicator.className = "flex justify-start mb-3";
    indicator.innerHTML = `
      <div class="flex items-center gap-1.5 bg-slate-800 text-slate-300 px-4 py-3 rounded-2xl rounded-tl-sm border border-slate-700/80">
        <span class="w-2 h-2 rounded-full bg-slate-400 animate-bounce"></span>
        <span class="w-2 h-2 rounded-full bg-slate-400 animate-bounce [animation-delay:0.2s]"></span>
        <span class="w-2 h-2 rounded-full bg-slate-400 animate-bounce [animation-delay:0.4s]"></span>
      </div>
    `;
    chatContainer.appendChild(indicator);
    return indicator;
  }

  function appendSakibBubble(markdownText) {
    const bubble = document.createElement("div");
    bubble.className = "flex justify-start mb-4 animate-fade-in";
    
    // Simple markdown bold formatting
    let formattedText = escapeHtml(markdownText)
      .replace(/\*\*(.*?)\*\*/g, '<strong class="text-purple-300 font-semibold">$1</strong>')
      .replace(/`(.*?)`/g, '<code class="px-1.5 py-0.5 rounded bg-slate-900 text-cyan-300 font-mono text-xs">$1</code>');

    bubble.innerHTML = `
      <div class="flex gap-2.5 max-w-sm sm:max-w-lg">
        <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-purple-600 to-cyan-500 flex items-center justify-center text-xs font-bold text-white shrink-0 shadow-md">
          NS
        </div>
        <div>
          <div class="text-[11px] text-slate-400 mb-1 mono">Sakib • Level 3 Term 2, BAIUST</div>
          <div class="bg-slate-900 border border-slate-800 text-slate-200 px-4 py-3 rounded-2xl rounded-tl-sm text-sm leading-relaxed shadow-lg">
            ${formattedText}
          </div>
        </div>
      </div>
    `;
    chatContainer.appendChild(bubble);
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
