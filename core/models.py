import os
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.db import models


def optimize_image_to_webp(image_field, max_width=1600, quality=85):
    """Auto-resizes uploaded images and converts them to high-efficiency WebP."""
    if not image_field:
        return
    try:
        img = Image.open(image_field)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        if img.width > max_width:
            ratio = max_width / float(img.width)
            new_height = int(float(img.height) * float(ratio))
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        buffer = BytesIO()
        img.save(buffer, format="WEBP", quality=quality, optimize=True)
        buffer.seek(0)

        base_name = os.path.splitext(image_field.name)[0]
        image_field.save(f"{base_name}.webp", ContentFile(buffer.read()), save=False)
    except Exception:
        # Fallback gracefully if image cannot be transformed
        pass


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=120, default="Sakib // AI & Systems")
    full_name = models.CharField(max_length=120, default="Md Najmus Sakib Rahatul")
    role_title = models.CharField(
        max_length=200,
        default="Aspiring AI Engineer · Full-Stack Developer"
    )
    tagline = models.CharField(
        max_length=280,
        default="Building sovereign local AI inference systems and resilient web platforms."
    )
    hero_photo = models.ImageField(upload_to="profile/", blank=True, null=True)
    hero_photo_url = models.CharField(
        max_length=500,
        blank=True,
        default="https://avatars.githubusercontent.com/u/166808901?v=4"
    )
    resume_file = models.FileField(upload_to="resume/", blank=True, null=True)
    resume_url = models.CharField(max_length=500, blank=True, default="/cv/")
    primary_email = models.EmailField(default="mdnajmussakib2003@gmail.com")
    secondary_email = models.EmailField(default="md.najmus.sakib.rahatul.2005@gmail.com")
    github_url = models.URLField(default="https://github.com/Sakib20050413")
    linkedin_url = models.URLField(default="https://www.linkedin.com/in/md-najmus-sakib-rahatul-559a85285/")
    kaggle_url = models.URLField(default="https://www.kaggle.com/sakib20050413")
    twitter_url = models.URLField(default="https://x.com/Rahatul2005")
    seo_title = models.CharField(
        max_length=200,
        default="Md Najmus Sakib Rahatul — AI Engineer & Full-Stack Developer"
    )
    seo_description = models.TextField(
        default="Personal portfolio of Md Najmus Sakib Rahatul: Aspiring AI Engineer, Full-Stack Developer, and Edge TinyML researcher."
    )
    theme_toggle_enabled = models.BooleanField(default=True)
    show_exploring_section = models.BooleanField(default=True)
    exploring_title = models.CharField(max_length=160, default="Currently Exploring")
    exploring_text = models.TextField(
        default=(
            "Investigating modular local AI inference architectures where a persistent dispatcher "
            "hot-swaps sub-1GB quantized specialist models into host memory pools to eliminate "
            "external cloud dependencies for software engineering and retrieval tasks."
        )
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def save(self, *args, **kwargs):
        if self.hero_photo and hasattr(self.hero_photo, "file") and not self.hero_photo.name.endswith(".webp"):
            optimize_image_to_webp(self.hero_photo, max_width=800)
        super().save(*args, **kwargs)

    @property
    def photo_display_url(self):
        if self.hero_photo:
            try:
                return self.hero_photo.url
            except Exception:
                pass
        return self.hero_photo_url

    def __str__(self):
        return f"{self.full_name} ({self.site_name})"


class About(models.Model):
    headline = models.CharField(max_length=220, default="Engineering Practical Systems Across Web & Edge AI")
    bio_paragraph_1 = models.TextField(
        default=(
            "I am a 3rd-year Computer Science & Engineering student at Bangladesh Army International "
            "University of Science and Technology (BAIUST), Cumilla. I build full-stack web applications "
            "with Python/Django and Next.js, and work on embedded IoT and real-time signal processing hardware."
        )
    )
    bio_paragraph_2 = models.TextField(
        blank=True,
        default=(
            "My current focus centers on applied AI engineering: integrating large language models, "
            "multimodal pipelines, and on-device quantization (4-bit NF4/GGUF) into accessible, production-ready platforms."
        )
    )
    education = models.CharField(
        max_length=200,
        default="B.Sc. in CSE, BAIUST, Cumilla (Level 3, Term 2)"
    )
    location = models.CharField(max_length=120, default="Cumilla / Dhaka, Bangladesh (UTC+6)")
    availability = models.CharField(
        max_length=160,
        default="Open to AI/ML engineering internships, remote developer contracts & research"
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.headline


class SkillGroup(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class Skill(models.Model):
    LEVEL_CHOICES = [
        ("Proficient", "Proficient"),
        ("Used in projects", "Used in projects"),
        ("Learning", "Learning"),
    ]
    group = models.ForeignKey(SkillGroup, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level_label = models.CharField(max_length=40, choices=LEVEL_CHOICES, default="Proficient")
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.name} ({self.level_label})"


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("AI_ML", "AI-ML"),
        ("WEB", "Web"),
        ("EMBEDDED", "Embedded"),
    ]
    STATUS_CHOICES = [
        ("Completed", "Completed"),
        ("In progress", "In progress"),
        ("Research", "Research"),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="WEB")
    summary = models.CharField(max_length=300, help_text="One-line problem statement")
    description = models.TextField(help_text="2-3 lines of what was built and engineering decisions")
    tech_stack_csv = models.CharField(max_length=400, help_text="Comma-separated stack tags")
    repo_url = models.URLField(blank=True, default="")
    live_url = models.URLField(blank=True, default="")
    cover_image = models.ImageField(upload_to="projects/", blank=True, null=True)
    cover_image_url = models.CharField(max_length=500, blank=True, default="")
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default="Completed")
    order = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    upvotes = models.PositiveIntegerField(default=24)

    class Meta:
        ordering = ["order", "id"]

    def save(self, *args, **kwargs):
        if self.cover_image and hasattr(self.cover_image, "file") and not self.cover_image.name.endswith(".webp"):
            optimize_image_to_webp(self.cover_image, max_width=1200)
        super().save(*args, **kwargs)

    @property
    def cover_display_url(self):
        if self.cover_image:
            try:
                return self.cover_image.url
            except Exception:
                pass
        return self.cover_image_url

    def tech_tags(self):
        return [t.strip() for t in self.tech_stack_csv.split(",") if t.strip()]

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects/gallery/", blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, default="")
    caption = models.CharField(max_length=200, blank=True, default="")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def save(self, *args, **kwargs):
        if self.image and hasattr(self.image, "file") and not self.image.name.endswith(".webp"):
            optimize_image_to_webp(self.image, max_width=1600)
        super().save(*args, **kwargs)

    @property
    def display_url(self):
        if self.image:
            try:
                return self.image.url
            except Exception:
                pass
        return self.image_url

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"


class Experience(models.Model):
    role_title = models.CharField(max_length=180)
    organization = models.CharField(max_length=180)
    period = models.CharField(max_length=80)
    description = models.TextField()
    badge_metric = models.CharField(max_length=100, blank=True, default="")
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.role_title} — {self.organization}"


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=150)
    issue_date = models.CharField(max_length=60, default="2026")
    credential_url = models.URLField(blank=True, default="")
    image = models.ImageField(upload_to="certificates/", blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, default="")
    order = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def save(self, *args, **kwargs):
        if self.image and hasattr(self.image, "file") and not self.image.name.endswith(".webp"):
            optimize_image_to_webp(self.image, max_width=1200)
        super().save(*args, **kwargs)

    @property
    def display_image_url(self):
        if self.image:
            try:
                return self.image.url
            except Exception:
                pass
        return self.image_url

    def __str__(self):
        return f"{self.title} ({self.issuer})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages (Inbox)"

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.created_at.strftime('%Y-%m-%d')}"
