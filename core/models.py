from django.db import models


class ProfileConfig(models.Model):
    site_name = models.CharField(max_length=120, default="Sakib // AI Systems")
    full_name = models.CharField(max_length=120, default="Md Najmus Sakib Rahatul")
    role_title = models.CharField(
        max_length=200,
        default="AI/ML Engineer & Full-Stack AI Systems Architect"
    )
    hero_headline = models.CharField(
        max_length=280,
        default="Architecting Sovereign Local Multi-Model AI Systems, Self-Evolving Neural Nodes & Scalable Web Platforms."
    )
    bio_summary = models.TextField(
        default=(
            "AI/ML Engineer and Full-Stack Developer specializing in Large Language Models, "
            "Multimodal AI orchestration, Edge TinyML, and high-throughput web architectures. "
            "My core engineering thesis focuses on building a locally executable Master AI Router "
            "that coordinates compact ~1 GB specialist sub-models (Code, Image, Video, and Reasoning) "
            "across unified CPU RAM, GPU VRAM, and NPU memory while performing in-place single-node continual self-training."
        )
    )
    photo_url = models.CharField(
        max_length=500,
        default="https://avatars.githubusercontent.com/u/166808901?v=4",
        help_text="Direct URL or uploaded path to Sakib's portrait photo"
    )
    location = models.CharField(max_length=120, default="Cumilla / Dhaka, Bangladesh (UTC+6)")
    availability_text = models.CharField(
        max_length=160,
        default="Available for AI/ML Engineering Roles, Research & Full-Stack Contracts"
    )
    primary_email = models.EmailField(default="mdnajmussakib2003@gmail.com")
    secondary_email = models.EmailField(default="md.najmus.sakib.rahatul.2005@gmail.com")
    github_url = models.URLField(default="https://github.com/Sakib20050413")
    linkedin_url = models.URLField(default="https://www.linkedin.com/in/md-najmus-sakib-rahatul-559a85285/")
    kaggle_url = models.URLField(default="https://www.kaggle.com/sakib20050413")
    twitter_url = models.URLField(default="https://x.com/Rahatul2005")
    facebook_url = models.URLField(default="https://www.facebook.com/Sakib200513")
    instagram_url = models.URLField(default="https://www.instagram.com/sakib200513/")
    accent_color = models.CharField(max_length=30, default="#4f46e5")
    default_theme = models.CharField(max_length=20, default="dark")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class AIArchitectureNode(models.Model):
    node_id = models.CharField(max_length=30, default="NODE-01")
    title = models.CharField(max_length=180)
    memory_budget = models.CharField(max_length=80, default="~1.0 GB Quantized (4-Bit NF4 / GGUF)")
    hardware_pool = models.CharField(max_length=120, default="CPU System RAM + GPU VRAM + NPU")
    summary = models.TextField(default="")
    mechanism_detail = models.TextField(default="")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.node_id}: {self.title}"


class Skill(models.Model):
    DOMAIN_CHOICES = [
        ("LLM_CORE", "01 // Large Language Models, Fine-Tuning & Alignment"),
        ("LOCAL_RUNTIME", "02 // Local AI Inference, Quantization & RAM/VRAM/NPU Routing"),
        ("MULTIMODAL_AGENTS", "03 // Multimodal Synthesis (Image/Video), Agents & Hybrid RAG"),
        ("EDGE_TINYML", "04 // Edge AI, TinyML & Bio-Acoustic / RF Signal Processing"),
        ("FULLSTACK_WEB", "05 // Full-Stack AI Integration (Django, FastAPI, Next.js, DOM, PHP)"),
        ("CLOUD_DATA", "06 // Vector Databases, PostgreSQL, Docker & Cloud CI/CD"),
    ]
    name = models.CharField(max_length=120)
    domain = models.CharField(max_length=40, choices=DOMAIN_CHOICES, default="LLM_CORE")
    proficiency = models.PositiveIntegerField(default=94)
    highlight_tag = models.CharField(max_length=80, default="Core Production")
    sync_to_linkedin_github = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["domain", "order", "id"]

    def __str__(self):
        return self.name


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("AI_LLM", "AI/ML & LLM Systems"),
        ("EDGE_TINYML", "Edge AI & TinyML Hardware"),
        ("FULLSTACK", "Full-Stack Web Platforms"),
        ("API_SYSTEMS", "FastAPI & Core Systems"),
    ]
    code = models.CharField(max_length=20, default="01")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, default="")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="AI_LLM")
    status_label = models.CharField(max_length=80, default="Live Production")
    tagline = models.CharField(max_length=260, default="")
    description = models.TextField(default="")
    architecture_breakdown = models.TextField(default="", blank=True)
    tech_stack_csv = models.CharField(max_length=400, default="")
    preview_image_url = models.CharField(max_length=500, blank=True, default="")
    live_server_url = models.URLField(blank=True, default="")
    github_repo_url = models.URLField(blank=True, default="")
    bento_col_span = models.PositiveIntegerField(default=6)
    upvotes = models.PositiveIntegerField(default=32)
    is_ongoing = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def tech_tags(self):
        return [t.strip() for t in self.tech_stack_csv.split(",") if t.strip()]

    def __str__(self):
        return f"{self.code} - {self.title}"


class CourseCertification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=150)
    completion_date = models.CharField(max_length=60, default="2026")
    credential_url = models.URLField(blank=True, default="")
    screenshot_url = models.CharField(max_length=500, blank=True, default="")
    key_takeaways = models.TextField(default="")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.title} ({self.issuer})"


class TimelineEntry(models.Model):
    role = models.CharField(max_length=180, default="")
    organization = models.CharField(max_length=180)
    period = models.CharField(max_length=80)
    impact_summary = models.TextField(default="")
    badge_metric = models.CharField(max_length=100, blank=True, default="")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.role} — {self.organization}"


class ContactMessage(models.Model):
    sender_name = models.CharField(max_length=120)
    sender_email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender_name}: {self.subject}"
