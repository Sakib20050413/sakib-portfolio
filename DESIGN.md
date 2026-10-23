# DESIGN SPECIFICATION & DESIGN SYSTEM — SAKIB PORTFOLIO

## 1. Visual Philosophy & Core Aesthetic
- **Philosophy:** Human-crafted, restrained editorial engineering minimalism inspired by Apple, Heva Health, and AVEA Studio.
- **Visitor Mode:** Experience mode for recruiters & engineering hiring managers; Operate mode for the secret `/dashboard/` admin CMS.
- **Anti-Slop Guarantees:** 
  - Zero rainbow cyberpunk neon glows or artificial purple/cyan gradients.
  - Zero emoji icons (use semantic crisp SVG icons only).
  - Zero Matter.js ball pits, zero fake terminal scanlines, zero auto-scrolling marquee tickers, zero fabricated stat-counter counters.
  - Generous whitespace based on an 8px modular spacing grid.

## 2. Typography Hierarchy & Scale
- **Display Typeface:** *Instrument Serif* (Editorial serif italic accents) or *Plus Jakarta Sans* (Weight: 700/800, tight tracking `-0.02em`, `text-wrap: balance`).
- **Body / Interface Typeface:** *Inter* / *Plus Jakarta Sans* (Weight: 400/500/600, line-height `1.6`, maximum reading width `65ch` / `max-w-2xl`).
- **Monospace Typeface:** *JetBrains Mono* (Used strictly for architecture node tags, terminal shell prompts, commit IDs, and technology chips).

### Modular Type Scale
| Level | Font Size | Line Height | Tracking | Usage |
| :--- | :--- | :--- | :--- | :--- |
| Hero Display | `3.25rem` – `4.5rem` (52–72px) | `1.05` | `-0.03em` | Hero Name & Role Headline |
| H2 Section | `2.0rem` – `2.5rem` (32–40px) | `1.15` | `-0.02em` | Section Titles (`#projects`, `#skills`) |
| H3 Card | `1.25rem` – `1.5rem` (20–24px) | `1.3` | `-0.01em` | Project & Architecture Node Titles |
| Body Regular | `1.0rem` (16px) | `1.6` | `0` | Biographies, problem statements, descriptions |
| Small / Meta | `0.875rem` (14px) | `1.5` | `+0.01em` | Timeline dates, filter tabs, form labels |
| Micro Mono | `0.75rem` (12px) | `1.4` | `+0.04em` | Status chips, tech tags, commit pills |

## 3. Calibrated Color Palette & WCAG AA Contrast Ratios
Defined as pure CSS variables in `:root` and `[data-theme="light"]`:

### Dark Mode (Primary Palette)
- `--bg-canvas: #090a0f` (Deep Obsidian / Zinc 950 base)
- `--bg-surface: #12151f` (Card surface background)
- `--bg-surface-elevated: #181c2a` (Hover states & modal overlays)
- `--bg-glass: rgba(9, 10, 15, 0.85)` (`backdrop-filter: blur(16px)`)
- `--border-subtle: rgba(255, 255, 255, 0.08)` (Hairline borders)
- `--border-focus: rgba(99, 102, 241, 0.5)` (Input & interactive focus outlines)
- `--text-primary: #f8fafc` (Contrast ratio vs `#090a0f`: 18.2:1 — WCAG AAA)
- `--text-secondary: #cbd5e1` (Contrast ratio vs `#090a0f`: 12.1:1 — WCAG AAA)
- `--text-muted: #94a3b8` (Contrast ratio vs `#090a0f`: 7.4:1 — WCAG AA)
- `--accent: #4f46e5` (Restrained Electric Indigo / Cobalt)
- `--signal: #10b981` (Live Status / "Available for work" pulse)

### Light Mode (Clean Studio Alabaster)
- `--bg-canvas: #f8f9fa`
- `--bg-surface: #ffffff`
- `--bg-surface-elevated: #f1f5f9`
- `--bg-glass: rgba(248, 249, 250, 0.90)`
- `--border-subtle: rgba(15, 23, 42, 0.08)`
- `--text-primary: #0f172a` (Contrast ratio: 16.5:1 — WCAG AAA)
- `--text-secondary: #334155` (Contrast ratio: 10.8:1 — WCAG AAA)
- `--text-muted: #64748b` (Contrast ratio: 4.8:1 — WCAG AA)
- `--accent: #4338ca`
- `--signal: #059669`

## 4. Spacing System (8px Grid)
- Multiples: `4px` (0.5), `8px` (1), `12px` (1.5), `16px` (2), `24px` (3), `32px` (4), `48px` (6), `64px` (8), `96px` (12).
- Section Padding: `py-20` on desktop, `py-12` on mobile.
- Container: Max width `1280px` (`max-w-7xl`), centered, padding `px-4 sm:px-6 lg:px-8`.

## 5. Motion Rules & Accessibility
- **Motion Principle:** High-craft restraint. GSAP or native `IntersectionObserver` reveal on scroll.
- **Animation Bounds:** Opacity (`0 -> 1`) and subtle Y-translation (`16px -> 0px`), duration `400ms – 600ms`, easing `cubic-bezier(0.23, 1, 0.32, 1)`.
- **Prefe-reduced-motion:** `prefers-reduced-motion: reduce` completely disables all transitions, WebGL cursor tracking, and transforms (`animation: none !important; transition: none !important;`).
- **Interactive States:** Subtle card hover lift (`transform: translateY(-2px)`), button active depression (`transform: scale(0.98)`).
- **Target Sizes:** All clickable buttons, pills, and links have minimum touch target dimensions of `44px x 44px`.

## 6. Target Performance & Audit Budgets
- **Lighthouse Targets:** Performance ≥ 90, Accessibility ≥ 95, Best Practices ≥ 95, SEO ≥ 95.
- **CLS (Cumulative Layout Shift):** `0.00` (Explicit width/height on all images and containers).
- **LCP (Largest Contentful Paint):** `< 1.8s` (Critical CSS inlined, fonts preloaded).
