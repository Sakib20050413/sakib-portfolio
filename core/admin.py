from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSettings,
    About,
    SkillGroup,
    Skill,
    Project,
    ProjectImage,
    Experience,
    Certificate,
    ContactMessage,
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "full_name", "role_title", "primary_email", "updated_at")

    def has_add_permission(self, request):
        # Enforce singleton pattern: only one settings instance allowed
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("headline", "education", "location", "availability", "updated_at")

    def has_add_permission(self, request):
        if About.objects.exists():
            return False
        return super().has_add_permission(request)


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ("name", "level_label", "order", "visible")


@admin.register(SkillGroup)
class SkillGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "visible", "skill_count")
    list_editable = ("order", "visible")
    inlines = [SkillInline]

    def skill_count(self, obj):
        return obj.skills.count()
    skill_count.short_description = "Skills"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "group", "level_label", "order", "visible")
    list_filter = ("group", "level_label", "visible")
    search_fields = ("name",)
    list_editable = ("level_label", "order", "visible")


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ("image", "image_url", "caption", "order")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "order", "featured", "visible", "preview_links")
    list_filter = ("category", "status", "featured", "visible")
    search_fields = ("title", "summary", "description", "tech_stack_csv")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("order", "featured", "visible")
    inlines = [ProjectImageInline]

    def preview_links(self, obj):
        links = []
        if obj.live_url:
            links.append(f'<a href="{obj.live_url}" target="_blank" style="color:#10b981;font-weight:600;">Live</a>')
        if obj.repo_url:
            links.append(f'<a href="{obj.repo_url}" target="_blank" style="color:#6366f1;">Repo</a>')
        return format_html(" | ".join(links) if links else "—")
    preview_links.short_description = "Links"


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role_title", "organization", "period", "order", "visible")
    search_fields = ("role_title", "organization", "description")
    list_editable = ("order", "visible")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "issue_date", "order", "visible")
    list_filter = ("issuer", "visible")
    search_fields = ("title", "issuer")
    list_editable = ("order", "visible")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "message", "created_at")
    list_editable = ("is_read",)

    def has_add_permission(self, request):
        # Contact messages are created via public form, not manually in admin
        return False
