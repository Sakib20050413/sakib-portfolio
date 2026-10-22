from django.db import models


class ProfileSetting(models.Model):
    full_name = models.CharField(max_length=150, default="Md Najmus Sakib Rahatul")
    display_handle = models.CharField(max_length=60, default="sakib@baiust")
    student_id = models.CharField(max_length=30, default="1119003")
    university = models.CharField(
        max_length=255,
        default="Bangladesh Army International University of Science and Technology (BAIUST), Cumilla"
    )
    department_batch = models.CharField(
        max_length=255,
        default="B.Sc. in Computer Science & Engineering (CSE), Level 3, Term 2, Section A, Group G1"
    )
    headline = models.CharField(
        max_length=300,
        default="Full-Stack Web Platforms & Embedded TinyML Hardware Systems"
    )
    bio = models.TextField(
        default="Computer Science & Engineering undergraduate at BAIUST, Cumilla (ID: 1119003). Team Leader at the BAIUST Computer Club Django Internship and Team BlackBerry IoT Research Group—building production Django/Next.js web applications and real-time ESP32-S3 signal processing hardware."
    )
    primary_email = models.EmailField(default="mdnajmussakib2003@gmail.com")
    academic_email = models.EmailField(default="md.najmus.sakib.rahatul.2005@gmail.com")
    location = models.CharField(max_length=120, default="Cumilla, Bangladesh (DAC • UTC+6)")
    availability_status = models.CharField(
        max_length=255,
        default="Available for Internships & Remote Roles"
    )
    cv_url = models.CharField(max_length=255, blank=True, default="/cv/")
    
    # Social links
    github_url = models.URLField(max_length=255, blank=True, default="https://github.com/Sakib20050413")
    linkedin_url = models.URLField(max_length=255, blank=True, default="https://www.linkedin.com/in/md-najmus-sakib-rahatul-559a85285/")
    x_twitter_url = models.URLField(max_length=255, blank=True, default="https://x.com/Rahatul2005")
    facebook_url = models.URLField(max_length=255, blank=True, default="https://www.facebook.com/Sakib200513")
    instagram_url = models.URLField(max_length=255, blank=True, default="https://www.instagram.com/sakib200513/")
    leetcode_url = models.URLField(max_length=255, blank=True, default="https://leetcode.com/u/Sakib20050413/")
    kaggle_url = models.URLField(max_length=255, blank=True, default="https://www.kaggle.com/sakib20050413")
    scholar_url = models.URLField(max_length=255, blank=True, default="")
    blog_url = models.URLField(max_length=255, blank=True, default="")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile Setting"
        verbose_name_plural = "Profile Settings"

    def __str__(self):
        return f"{self.full_name} ({self.student_id})"

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("Full-Stack Web", "Full-Stack Web"),
        ("Embedded IoT & TinyML", "Embedded IoT & TinyML"),
        ("Desktop & DSP", "Desktop & DSP"),
    ]

    code = models.CharField(max_length=15, unique=True, help_text="e.g. A001")
    title = models.CharField(max_length=220)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Full-Stack Web")
    tech_stack = models.CharField(max_length=350, help_text="Comma-separated tech badges")
    summary = models.TextField()
    why_built = models.TextField(blank=True)
    architecture = models.TextField(blank=True)
    hardware_code_highlights = models.TextField(blank=True)
    github_url = models.URLField(max_length=300, blank=True)
    live_url = models.URLField(max_length=300, blank=True)
    stars_count = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "code"]

    def __str__(self):
        return f"[{self.code}] {self.title}"

    @property
    def tech_list(self):
        return [tag.strip() for tag in self.tech_stack.split(",") if tag.strip()]


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("Backend & Full-Stack Web", "Backend & Full-Stack Web"),
        ("Frontend & Interactive UI", "Frontend & Interactive UI"),
        ("Embedded AI, IoT & DSP", "Embedded AI, IoT & DSP"),
        ("Databases, Tools & Cloud", "Databases, Tools & Cloud"),
    ]

    name = models.CharField(max_length=80)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Backend & Full-Stack Web")
    proficiency = models.PositiveIntegerField(default=85, help_text="Percentage 0-100")
    badge_color = models.CharField(max_length=30, default="#4f46e5", blank=True)
    icon_svg = models.TextField(blank=True, help_text="Optional inline SVG path or icon name")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} ({self.category})"


class TimelineEntry(models.Model):
    CATEGORY_CHOICES = [
        ("Leadership", "Leadership"),
        ("Experience", "Experience"),
        ("Education", "Education"),
        ("Award", "Award"),
    ]

    title = models.CharField(max_length=220)
    organization = models.CharField(max_length=220)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Experience")
    period = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]
        verbose_name = "Timeline Entry"
        verbose_name_plural = "Timeline Entries"

    def __str__(self):
        return f"{self.title} @ {self.organization}"


class ContactMessage(models.Model):
    sender_name = models.CharField(max_length=150)
    sender_email = models.EmailField()
    subject = models.CharField(max_length=220)
    project_type = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Msg from {self.sender_name} - {self.subject}"
