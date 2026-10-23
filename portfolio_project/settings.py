import os
import shutil
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-sakib-ai-portfolio-v1-render-canonical-secret-key"
)

DEBUG = os.environ.get("DEBUG", "True").lower() in ("true", "1", "yes")

# Secret admin URL slug from environment variable (defaults to studio-7f3k)
ADMIN_URL = os.environ.get("ADMIN_URL", "studio-7f3k").strip("/")

ALLOWED_HOSTS = [
    h.strip()
    for h in os.environ.get(
        "ALLOWED_HOSTS",
        "127.0.0.1,localhost,.onrender.com,.vercel.app"
    ).split(",")
    if h.strip()
]
if "*" in ALLOWED_HOSTS or DEBUG:
    ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
    "https://*.vercel.app",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
]

# Resilient Cloudinary integration for remote media on ephemeral hosts
if os.environ.get("CLOUDINARY_URL"):
    try:
        import cloudinary_storage
        INSTALLED_APPS.insert(0, "cloudinary_storage")
        INSTALLED_APPS.append("cloudinary")
        DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
    except ImportError:
        pass

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Resilient django-axes integration for brute-force login protection
try:
    import axes
    INSTALLED_APPS.append("axes")
    AUTHENTICATION_BACKENDS = [
        "axes.backends.AxesStandaloneBackend",
        "django.contrib.auth.backends.ModelBackend",
    ]
    MIDDLEWARE.append("axes.middleware.AxesMiddleware")
    AXES_FAILURE_LIMIT = 5
    AXES_COOLOFF_TIME = 1
    AXES_RESET_ON_SUCCESS = True
except ImportError:
    pass

ROOT_URLCONF = "portfolio_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portfolio_project.wsgi.application"

# Database Configuration (Neon/Supabase PostgreSQL vs SQLite fallback)
if os.environ.get("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.config(
            conn_max_age=600,
            ssl_require="sslmode=require" in os.environ.get("DATABASE_URL", "")
        )
    }
elif "VERCEL" in os.environ:
    tmp_db = Path("/tmp/db.sqlite3")
    bundled_db = BASE_DIR / "db.sqlite3"
    if not tmp_db.exists() and bundled_db.exists():
        shutil.copy2(bundled_db, tmp_db)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": str(tmp_db),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Dhaka"
USE_I18N = True
USE_TZ = True

# Static files (WhiteNoise)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = Path("/tmp/media") if "VERCEL" in os.environ else (BASE_DIR / "media")

# Email Backend (Console in local debug, SMTP in production)
EMAIL_BACKEND = os.environ.get(
    "EMAIL_BACKEND",
    "django.core.mail.backends.console.EmailBackend" if DEBUG else "django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", "True").lower() in ("true", "1")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "sakib@sakib.dev")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = f"/{ADMIN_URL}/login/"
LOGIN_REDIRECT_URL = f"/{ADMIN_URL}/"

# Production security headers
if not DEBUG and "RENDER" in os.environ:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
