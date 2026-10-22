/**
 * physics_ballpit.js
 * 2D Canvas Physics Engine for Tech-Stack Ball Pit
 * Md Najmus Sakib Rahatul (ID: 1119003) - BAIUST
 */

class PhysicsBall {
  constructor(x, y, radius, name, color, proficiency) {
    this.x = x;
    this.y = y;
    this.vx = (Math.random() - 0.5) * 4;
    this.vy = Math.random() * -3;
    this.radius = radius || 30;
    this.name = name;
    this.color = color || "#a855f7";
    this.proficiency = proficiency || 85;
    this.mass = this.radius * 0.1;
    this.restitution = 0.72; // bounce coefficient
  }

  update(width, height, gravity, mouse) {
    // Apply gravity
    this.vy += gravity;

    // Apply friction
    this.vx *= 0.992;
    this.vy *= 0.992;

    // Mouse collision impulse
    if (mouse && mouse.x !== null) {
      const dx = this.x - mouse.x;
      const dy = this.y - mouse.y;
      const dist = Math.hypot(dx, dy);
      const pushRadius = 90;

      if (dist < pushRadius && dist > 0) {
        const force = (pushRadius - dist) / pushRadius;
        const angle = Math.atan2(dy, dx);
        this.vx += Math.cos(angle) * force * 4.5;
        this.vy += Math.sin(angle) * force * 4.5;
      }
    }

    // Update position
    this.x += this.vx;
    this.y += this.vy;

    // Boundary Collisions (Walls & Floor)
    if (this.x - this.radius < 0) {
      this.x = this.radius;
      this.vx = -this.vx * this.restitution;
    } else if (this.x + this.radius > width) {
      this.x = width - this.radius;
      this.vx = -this.vx * this.restitution;
    }

    if (this.y - this.radius < 0) {
      this.y = this.radius;
      this.vy = -this.vy * this.restitution;
    } else if (this.y + this.radius > height) {
      this.y = height - this.radius;
      this.vy = -this.vy * this.restitution;
      // Ground friction
      this.vx *= 0.96;
    }
  }

  draw(ctx) {
    ctx.save();

    // Subtle drop shadow
    ctx.shadowColor = "rgba(0, 0, 0, 0.4)";
    ctx.shadowBlur = 8;
    ctx.shadowOffsetY = 4;

    // Ball Base Gradient (Glossy sphere)
    const grad = ctx.createRadialGradient(
      this.x - this.radius * 0.3,
      this.y - this.radius * 0.35,
      this.radius * 0.1,
      this.x,
      this.y,
      this.radius
    );
    grad.addColorStop(0, "#ffffff");
    grad.addColorStop(0.25, this.color);
    grad.addColorStop(1, "#090d16");

    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fill();

    // Reset shadow
    ctx.shadowColor = "transparent";

    // Sphere Border
    ctx.strokeStyle = "rgba(255, 255, 255, 0.25)";
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Label
    ctx.fillStyle = "#ffffff";
    ctx.font = `bold ${Math.max(10, Math.floor(this.radius * 0.42))}px 'Plus Jakarta Sans', sans-serif`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(this.name, this.x, this.y);

    ctx.restore();
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("physics-canvas");
  if (!canvas) return;

  const ctx = canvas.getContext("2d");
  const container = canvas.parentElement;

  let width = (canvas.width = container.clientWidth || 700);
  let height = (canvas.height = 380);

  let gravity = 0.24;
  let balls = [];

  const mouse = { x: null, y: null };

  window.addEventListener("resize", () => {
    width = canvas.width = container.clientWidth || 700;
    height = canvas.height = 380;
  });

  canvas.addEventListener("mousemove", (e) => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  });

  canvas.addEventListener("mouseleave", () => {
    mouse.x = null;
    mouse.y = null;
  });

  // Ball-to-ball elastic collision resolution
  function resolveCollisions() {
    for (let i = 0; i < balls.length; i++) {
      for (let j = i + 1; j < balls.length; j++) {
        const b1 = balls[i];
        const b2 = balls[j];

        const dx = b2.x - b1.x;
        const dy = b2.y - b1.y;
        const dist = Math.hypot(dx, dy);
        const minDist = b1.radius + b2.radius;

        if (dist < minDist && dist > 0) {
          // Normal vector
          const nx = dx / dist;
          const ny = dy / dist;

          // Positional correction to prevent sticking
          const overlap = minDist - dist;
          b1.x -= nx * overlap * 0.5;
          b1.y -= ny * overlap * 0.5;
          b2.x += nx * overlap * 0.5;
          b2.y += ny * overlap * 0.5;

          // Relative velocity
          const kx = b1.vx - b2.vx;
          const ky = b1.vy - b2.vy;

          // Velocity along normal
          const p = 2 * (nx * kx + ny * ky) / (b1.mass + b2.mass);

          b1.vx -= p * b2.mass * nx * 0.85;
          b1.vy -= p * b2.mass * ny * 0.85;
          b2.vx += p * b1.mass * nx * 0.85;
          b2.vy += p * b1.mass * ny * 0.85;
        }
      }
    }
  }

  // Load skills via API or fallback
  fetch("/api/skills/")
    .then((res) => res.json())
    .then((data) => {
      const skillsData = (data.status === "success" && data.skills) ? data.skills : [];
      initBalls(skillsData);
    })
    .catch(() => {
      // Fallback skills if offline or API unavailable
      const defaultSkills = [
        { name: "Python", badge_color: "#3B82F6", radius: 32 },
        { name: "Django", badge_color: "#10B981", radius: 30 },
        { name: "JavaScript", badge_color: "#F59E0B", radius: 30 },
        { name: "Next.js", badge_color: "#6366F1", radius: 28 },
        { name: "ESP32-S3", badge_color: "#EAB308", radius: 30 },
        { name: "TinyML", badge_color: "#A855F7", radius: 29 },
        { name: "FFT DSP", badge_color: "#D946EF", radius: 28 },
        { name: "PostgreSQL", badge_color: "#06B6D4", radius: 29 },
        { name: "PHP", badge_color: "#8B5CF6", radius: 28 },
        { name: "C++", badge_color: "#0284C7", radius: 29 },
        { name: "Tailwind", badge_color: "#14B8A6", radius: 29 },
        { name: "HTML5", badge_color: "#EF4444", radius: 31 },
      ];
      initBalls(defaultSkills);
    });

  function initBalls(skills) {
    balls = skills.map((s, index) => {
      const startX = 60 + ((index * 55) % (width - 120));
      const startY = 30 + Math.floor(index / 8) * 60;
      return new PhysicsBall(
        startX,
        startY,
        s.radius || 29,
        s.name,
        s.badge_color,
        s.proficiency
      );
    });
  }

  // Shake / Invert Gravity Button
  const shakeBtn = document.getElementById("btn-shake-gravity");
  if (shakeBtn) {
    shakeBtn.addEventListener("click", () => {
      balls.forEach((ball) => {
        ball.vx += (Math.random() - 0.5) * 16;
        ball.vy -= Math.random() * 12 + 6;
      });
      // Sound effect if enabled
      if (window.playSynthClick) window.playSynthClick(380);
    });
  }

  // Animation Loop
  function animate() {
    ctx.clearRect(0, 0, width, height);

    // Subtle Grid Background
    ctx.strokeStyle = "rgba(148, 163, 184, 0.05)";
    ctx.lineWidth = 1;
    const gridSize = 40;
    for (let x = 0; x < width; x += gridSize) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
    for (let y = 0; y < height; y += gridSize) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }

    // Update and draw balls
    balls.forEach((ball) => ball.update(width, height, gravity, mouse));
    resolveCollisions();
    balls.forEach((ball) => ball.draw(ctx));

    requestAnimationFrame(animate);
  }

  requestAnimationFrame(animate);

  // Expose global trigger for terminal commands
  window.triggerSkillImpulse = function () {
    balls.forEach((ball) => {
      ball.vx += (Math.random() - 0.5) * 14;
      ball.vy -= Math.random() * 10 + 5;
    });
  };
});
