/**
 * hardware_scrolly.js
 * Interactive ESP32-S3 Hardware Pinout & TinyML Signal Flow Visualizer
 * Md Najmus Sakib Rahatul (ID: 1119003) - BAIUST
 */

document.addEventListener("DOMContentLoaded", () => {
  const hardwareData = {
    lightning: {
      title: "System 01: IoT Storm & Lightning Early Warning Box (CSE 301 IDP)",
      subtitle: "3-Stream AI/ML Cross-Verified Distance Estimation & Bangla Voice Siren",
      mcu: "ESP32-S3-WROOM-1 (240MHz Dual-Core Xtensa LX7, 512KB SRAM, 8MB Octal PSRAM)",
      pins: [
        {
          pin: "GPIO 4 (SDA) & GPIO 5 (SCL)",
          label: "AS3935 RF & BH1750 Optical I2C Bus",
          type: "I2C Sensor Bus (400 kHz Fast-Mode)",
          summary: "Tunes AS3935 lightning sensor to 500 kHz resonance to detect cloud-to-ground electromagnetic discharge front-ends (1–40 km). Simultaneously reads BH1750 ambient light lux drop.",
          codeSnippet: "// I2C Init & AS3935 Resonance Calibration\nWire.begin(4, 5, 400000);\nlightningSensor.calibrateResonance();\nlightningSensor.setIndoorOutdoor(OUTDOOR);",
        },
        {
          pin: "GPIO 16 (TX) & GPIO 17 (RX)",
          label: "SIM800L GSM/GPRS Telemetry & SMS",
          type: "Hardware UART2 (115200 Baud)",
          summary: "Provides offline cellular fallback. When a strike within 10 km is detected, immediately broadcasts automated warning SMS to campus patrol and field farmers.",
          codeSnippet: "// SIM800L Emergency Dispatch\nSerial2.begin(115200, SERIAL_8N1, 16, 17);\nsendEmergencySMS(\"+8801XXXXXXXXX\", \"WARNING: Lightning detected within 6km\");",
        },
        {
          pin: "GPIO 25 (BCLK) & GPIO 26 (LRCLK) & GPIO 27 (DIN)",
          label: "MAX98357A 3W Bangla Voice Siren",
          type: "I2S Digital Audio Stream",
          summary: "Direct digital-to-analog amplification driving an 8-ohm 3W speaker. Plays pre-rendered Bengali voice announcements: 'সতর্কতা: বজ্রপাত ১০ কিলোমিটারের মধ্যে!'",
          codeSnippet: "// I2S DMA Audio Playback\ni2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL);\nplayAudioPrompt(BANGLA_VOICE_STORM_ALERT);",
        },
        {
          pin: "GPIO 1 (ADC1_CH0)",
          label: "Solar Battery Telemetry Voltage Divider",
          type: "12-Bit SAR ADC (0–3.3V)",
          summary: "Measures 3.7V 18650 Li-ion pack voltage through a 100k/100k voltage divider to manage deep-sleep power states during overcast rainy conditions.",
          codeSnippet: "float vBat = (analogRead(1) / 4095.0) * 3.3 * 2.0;\nif (vBat < 3.4) esp_deep_sleep_start();",
        },
      ],
    },
    mosquito: {
      title: "System 02: 512-Point FFT Bio-Acoustic Mosquito Vector Trap (CSE 326)",
      subtitle: "32-Millisecond Dual-Stage Acoustic & Optical Insect Classification",
      mcu: "ESP32-S3 Hardware FPU (Vector Math DSP Accelerators)",
      pins: [
        {
          pin: "GPIO 18 (SCK) & GPIO 8 (WS) & GPIO 3 (SD)",
          label: "INMP441 Digital MEMS Microphone",
          type: "I2S DMA Audio Stream (16 kHz @ 24-Bit)",
          summary: "Samples insect wingbeat vibrations directly into DMA buffers without CPU overhead. Feeds 512 raw PCM samples into Hann window accumulator.",
          codeSnippet: "// INMP441 DMA Config\ni2s_config_t i2s_mic = {\n  .sample_rate = 16000,\n  .bits_per_sample = I2S_BITS_PER_SAMPLE_32BIT,\n  .channel_format = I2S_CHANNEL_FMT_ONLY_LEFT\n};",
        },
        {
          pin: "ESP32-S3 Hardware FPU",
          label: "512-Point Radix-2 FFT Execution",
          type: "DSP Kernel (8.2 ms Processing Time)",
          summary: "Executes 512-point Radix-2 Real FFT yielding 31.25 Hz bin resolution. Isolates Band C (350–600 Hz female vector fundamental) vs Band A (100–250 Hz bees/pollinators).",
          codeSnippet: "dsps_fft2r_fc32(fft_buffer, 512);\ndsps_bit_rev_fc32(fft_buffer, 512);\ndsps_cplx2reM_fc32(fft_buffer, magnitude, 256);",
        },
        {
          pin: "GPIO 10",
          label: "IRLZ44N PWM Suction Gate",
          type: "LEDC PWM Output (25 kHz, 8-Bit)",
          summary: "Drives high-RPM 12V suction fan. Activates 100% PWM only when female mosquito spectral signature is validated; remains 0% for honeybees and harmless insects.",
          codeSnippet: "if (classifiedCategory == FEMALE_AEDES_VECTOR) {\n  ledcWrite(0, 255); // 100% PWM Fan Trap ON\n} else {\n  ledcWrite(0, 0);   // Pollinator Safety Guard\n}",
        },
        {
          pin: "GPIO 14 & GPIO 15",
          label: "LM393 Dual IR Gate Detectors",
          type: "GPIO External Interrupt (Falling Edge)",
          summary: "Optical beam break detector at funnel entrance. Wakes audio DSP subsystem only when an insect enters the chamber, conserving battery energy.",
          codeSnippet: "attachInterrupt(digitalPinToInterrupt(14), onInsectEnter, FALLING);",
        },
      ],
    },
  };

  let currentSystem = "lightning";

  const btnLightning = document.getElementById("btn-hw-lightning");
  const btnMosquito = document.getElementById("btn-hw-mosquito");
  const titleEl = document.getElementById("hw-title");
  const subtitleEl = document.getElementById("hw-subtitle");
  const mcuEl = document.getElementById("hw-mcu");
  const pinListEl = document.getElementById("hw-pin-list");
  const detailBox = document.getElementById("hw-detail-box");

  if (!pinListEl || !detailBox) return;

  function renderSystem(sysKey) {
    currentSystem = sysKey;
    const data = hardwareData[sysKey];

    if (btnLightning && btnMosquito) {
      if (sysKey === "lightning") {
        btnLightning.classList.add("bg-purple-600", "text-white");
        btnLightning.classList.remove("bg-slate-800", "text-slate-300");
        btnMosquito.classList.remove("bg-purple-600", "text-white");
        btnMosquito.classList.add("bg-slate-800", "text-slate-300");
      } else {
        btnMosquito.classList.add("bg-purple-600", "text-white");
        btnMosquito.classList.remove("bg-slate-800", "text-slate-300");
        btnLightning.classList.remove("bg-purple-600", "text-white");
        btnLightning.classList.add("bg-slate-800", "text-slate-300");
      }
    }

    if (titleEl) titleEl.textContent = data.title;
    if (subtitleEl) subtitleEl.textContent = data.subtitle;
    if (mcuEl) mcuEl.textContent = `MCU CORE: ${data.mcu}`;

    // Render Pin Buttons
    pinListEl.innerHTML = "";
    data.pins.forEach((pinItem, idx) => {
      const pinBtn = document.createElement("button");
      pinBtn.className = `w-full text-left p-3.5 rounded-xl border transition flex items-center justify-between ${
        idx === 0
          ? "bg-purple-500/10 border-purple-500/40 text-purple-300 shadow-sm"
          : "bg-slate-900/50 border-slate-800 text-slate-300 hover:bg-slate-800/60"
      }`;
      pinBtn.innerHTML = `
        <div>
          <div class="font-mono text-xs font-bold text-amber-300">${pinItem.pin}</div>
          <div class="text-sm font-semibold text-slate-100 mt-0.5">${pinItem.label}</div>
        </div>
        <span class="text-xs text-slate-400 mono">&rarr;</span>
      `;

      pinBtn.addEventListener("click", () => {
        // Toggle active UI
        Array.from(pinListEl.children).forEach((child) => {
          child.className = "w-full text-left p-3.5 rounded-xl border border-slate-800 bg-slate-900/50 text-slate-300 hover:bg-slate-800/60 transition flex items-center justify-between";
        });
        pinBtn.className = "w-full text-left p-3.5 rounded-xl border border-purple-500/40 bg-purple-500/10 text-purple-300 shadow-sm transition flex items-center justify-between";
        renderDetail(pinItem);
        if (window.playSynthClick) window.playSynthClick(520);
      });

      pinListEl.appendChild(pinBtn);
    });

    // Default to first pin detail
    renderDetail(data.pins[0]);
  }

  function renderDetail(pinItem) {
    detailBox.innerHTML = `
      <div class="space-y-4">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800">
          <span class="px-3 py-1 rounded-md bg-purple-500/20 text-purple-300 font-mono text-xs font-bold border border-purple-500/30">
            ${pinItem.pin}
          </span>
          <span class="text-xs text-cyan-400 mono font-semibold">${pinItem.type}</span>
        </div>
        <div>
          <h4 class="text-lg font-bold text-white">${pinItem.label}</h4>
          <p class="text-slate-300 text-sm mt-2 leading-relaxed">${pinItem.summary}</p>
        </div>
        <div class="pt-2">
          <div class="text-xs text-slate-400 mono mb-1.5 flex items-center justify-between">
            <span>EMBEDDED C++ / FIRMWARE SNIPPET</span>
            <span class="text-emerald-400">Verified ESP-IDF / Arduino</span>
          </div>
          <pre class="p-3.5 bg-slate-950 rounded-xl border border-slate-800/80 text-xs font-mono text-emerald-300 overflow-x-auto leading-relaxed"><code>${pinItem.codeSnippet}</code></pre>
        </div>
      </div>
    `;
  }

  if (btnLightning) {
    btnLightning.addEventListener("click", () => renderSystem("lightning"));
  }
  if (btnMosquito) {
    btnMosquito.addEventListener("click", () => renderSystem("mosquito"));
  }

  // Initial load
  renderSystem("lightning");
});
