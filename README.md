# Md Najmus Sakib Rahatul — AI Engineer & Full-Stack Portfolio

A production-grade, single-page personal portfolio and secret CMS built with **Django 5**, **PostgreSQL**, **Vanilla JavaScript (ES6+)**, and **WhiteNoise**, deployed on **Render** with **Neon Postgres** and **Cloudinary** media storage.

---

## 1. Architecture Overview
- **Backend:** Python 3.12 / Django 5 with server-rendered templates.
- **Database:** PostgreSQL (Neon.tech pooled connection in production) / SQLite locally.
- **Frontend:** Semantic HTML5, CSS custom properties (8px spacing grid, WCAG AA contrast), Vanilla JS DOM manipulation.
- **Static & Media:** WhiteNoise compression for static assets; Cloudinary for user-uploaded media files.
- **Admin CMS:** Headless-capable Django admin mounted at a secret environment variable slug (`ADMIN_URL=studio-7f3k/`). The default `/admin/` path returns an explicit 404.
- **Security:** CSRF protection, secure cookies, brute-force lockout (`django-axes`), honeypot and rate-limiting on contact submissions.

---

## 2. Local Development Setup

### Prerequisites
- Python 3.11+
- Git

### Step-by-Step Installation
1. Clone the repository and enter the workspace:
   ```bash
   git clone https://github.com/Sakib20050413/sakib-portfolio.git
   cd sakib-portfolio
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```bash
   cp .env.example .env
   ```
   Fill in `.env` with your values:
   ```ini
   SECRET_KEY=your-secure-random-secret-key
   DEBUG=True
   ADMIN_URL=studio-7f3k/
   # Leave DATABASE_URL empty to use local db.sqlite3, or paste Neon PostgreSQL URL:
   DATABASE_URL=
   CLOUDINARY_URL=
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Seed canonical content (from `CONTENT.md`):
   ```bash
   python manage.py seed_portfolio
   ```

7. Create superuser for the hidden CMS:
   ```bash
   python manage.py createsuperuser
   ```

8. Start the local server:
   ```bash
   python manage.py runserver 127.0.0.1:8000
   ```
   - Public Portfolio: `http://127.0.0.1:8000/`
   - Secret Admin CMS: `http://127.0.0.1:8000/studio-7f3k/` (or your configured `ADMIN_URL`)

---

## 3. Managing Projects & Content from the Dashboard

1. Navigate to the secret CMS URL (e.g., `http://127.0.0.1:8000/studio-7f3k/`) and log in.
2. **Projects:** Click **Projects** → **Add Project**. Fill in:
   - Title, Slug, Category (AI-ML / Web / Embedded), Summary (one-line problem), Description (what was built).
   - Tech stack tags (comma-separated).
   - GitHub Repository URL, Live Demo URL.
   - Cover image (auto-compressed to WebP) and featured flag.
3. **Skills:** Organize skills into up to 5 clear groups with honest proficiency tags.
4. **Site Settings:** Update hero headline, bio summary, resume PDF, and contact availability toggle in one click.

---

## 4. Production Deployment (Render + Neon + Cloudinary)

1. **Database (Neon):** Create a project in `AWS Singapore (ap-southeast-1)` and copy the pooled connection string into `DATABASE_URL`.
2. **Media (Cloudinary):** Create a free Cloudinary account and copy the `CLOUDINARY_URL`.
3. **Web Service (Render):**
   - Connect repository `Sakib20050413/sakib-portfolio`.
   - Region: `Singapore`.
   - Build Command: `./build.sh`
   - Start Command: `gunicorn portfolio_project.wsgi:application`
   - Set environment variables: `SECRET_KEY`, `DEBUG=False`, `DATABASE_URL`, `CLOUDINARY_URL`, `ADMIN_URL`, `ALLOWED_HOSTS`.
