/**
 * avatar_tracker.js
 * Interactive Cursor-Tracking 3D/2D Vector Avatar Canvas
 * Md Najmus Sakib Rahatul (ID: 1119003) - BAIUST
 */

document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("avatar-canvas");
  if (!canvas) return;

  const ctx = canvas.getContext("2d");
  let width = (canvas.width = canvas.parentElement.clientWidth || 360);
  let height = (canvas.height = 360);

  let mouseX = width / 2;
  let mouseY = height / 2;
  let targetAngleX = 0;
  let targetAngleY = 0;
  let currentAngleX = 0;
  let currentAngleY = 0;

  window.addEventListener("resize", () => {
    width = canvas.width = canvas.parentElement.clientWidth || 360;
    height = canvas.height = 360;
  });

  window.addEventListener("mousemove", (e) => {
    const rect = canvas.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    const dx = e.clientX - centerX;
    const dy = e.clientY - centerY;

    targetAngleX = Math.max(-18, Math.min(18, (dx / window.innerWidth) * 40));
    targetAngleY = Math.max(-14, Math.min(14, (dy / window.innerHeight) * 30));
  });

  function render() {
    // Smooth lerp
    currentAngleX += (targetAngleX - currentAngleX) * 0.08;
    currentAngleY += (targetAngleY - currentAngleY) * 0.08;

    ctx.clearRect(0, 0, width, height);

    const centerX = width / 2 + currentAngleX * 1.5;
    const centerY = height / 2 + currentAngleY * 1.2;

    // Outer Ambient Glow
    const glowGrad = ctx.createRadialGradient(centerX, centerY, 40, centerX, centerY, 140);
    glowGrad.addColorStop(0, "rgba(168, 85, 247, 0.35)");
    glowGrad.addColorStop(0.6, "rgba(6, 182, 212, 0.15)");
    glowGrad.addColorStop(1, "rgba(0, 0, 0, 0)");
    ctx.fillStyle = glowGrad;
    ctx.beginPath();
    ctx.arc(centerX, centerY, 140, 0, Math.PI * 2);
    ctx.fill();

    // Cyber Headset Ring (Background)
    ctx.strokeStyle = "rgba(168, 85, 247, 0.5)";
    ctx.lineWidth = 6;
    ctx.beginPath();
    ctx.arc(centerX, centerY - 15, 82, Math.PI * 0.8, Math.PI * 2.2);
    ctx.stroke();

    // Stylized Face Oval
    ctx.fillStyle = "#1e293b";
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.ellipse(centerX, centerY, 65, 78, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // Modern Hair / Cap
    ctx.fillStyle = "#0f172a";
    ctx.beginPath();
    ctx.arc(centerX, centerY - 28, 66, Math.PI, Math.PI * 2);
    ctx.fill();

    // Hair bang accent
    ctx.strokeStyle = "#a855f7";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(centerX - 35, centerY - 32);
    ctx.quadraticCurveTo(centerX, centerY - 15, centerX + 40, centerY - 30);
    ctx.stroke();

    // Cyber Visor / Glasses Frame
    const eyeOffsetX = currentAngleX * 0.8;
    const eyeOffsetY = currentAngleY * 0.6;

    ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
    ctx.strokeStyle = "#a855f7";
    ctx.lineWidth = 2.5;

    // Left Lens
    ctx.beginPath();
    ctx.roundRect(centerX - 46 + eyeOffsetX, centerY - 12 + eyeOffsetY, 38, 24, 6);
    ctx.fill();
    ctx.stroke();

    // Right Lens
    ctx.beginPath();
    ctx.roundRect(centerX + 8 + eyeOffsetX, centerY - 12 + eyeOffsetY, 38, 24, 6);
    ctx.fill();
    ctx.stroke();

    // Visor Bridge
    ctx.beginPath();
    ctx.moveTo(centerX - 8 + eyeOffsetX, centerY + eyeOffsetY);
    ctx.lineTo(centerX + 8 + eyeOffsetX, centerY + eyeOffsetY);
    ctx.stroke();

    // Glowing Cyan Pupils (Looking at cursor)
    const pupilX = (currentAngleX / 18) * 6;
    const pupilY = (currentAngleY / 14) * 4;

    ctx.fillStyle = "#38bdf8";
    ctx.shadowColor = "#38bdf8";
    ctx.shadowBlur = 10;

    // Left Pupil
    ctx.beginPath();
    ctx.arc(centerX - 27 + eyeOffsetX + pupilX, centerY + eyeOffsetY + pupilY, 4.5, 0, Math.PI * 2);
    ctx.fill();

    // Right Pupil
    ctx.beginPath();
    ctx.arc(centerX + 27 + eyeOffsetX + pupilX, centerY + eyeOffsetY + pupilY, 4.5, 0, Math.PI * 2);
    ctx.fill();

    ctx.shadowBlur = 0; // reset shadow

    // Smile / Tech Collar
    ctx.strokeStyle = "rgba(148, 163, 184, 0.8)";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.arc(centerX, centerY + 30, 20, 0.2 * Math.PI, 0.8 * Math.PI);
    ctx.stroke();

    // Glowing Headset Ear Cups
    ctx.fillStyle = "#a855f7";
    ctx.shadowColor = "#c084fc";
    ctx.shadowBlur = 8;

    // Left ear cup
    ctx.beginPath();
    ctx.ellipse(centerX - 68, centerY, 8, 20, 0, 0, Math.PI * 2);
    ctx.fill();

    // Right ear cup
    ctx.beginPath();
    ctx.ellipse(centerX + 68, centerY, 8, 20, 0, 0, Math.PI * 2);
    ctx.fill();

    ctx.shadowBlur = 0;

    // Subtle Live Telemetry Label below Avatar
    ctx.font = "10px 'JetBrains Mono', monospace";
    ctx.fillStyle = "rgba(148, 163, 184, 0.7)";
    ctx.textAlign = "center";
    ctx.fillText(`HEAD_TILT [ X: ${currentAngleX.toFixed(1)}° | Y: ${currentAngleY.toFixed(1)}° ]`, width / 2, height - 16);

    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
});
