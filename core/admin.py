from django.contrib import admin
from .models import (
    ProfileConfig,
    AIArchitectureNode,
    Skill,
    Project,
    CourseCertification,
    TimelineEntry,
    ContactMessage,
)


@admin.register(ProfileConfig)
class ProfileConfigAdmin(admin.ModelAdmin):
    list_display = ("full_name", "role_title", "location", "primary_email", "updated_at")


@admin.register(AIArchitectureNode)
class AIArchitectureNodeAdmin(admin.ModelAdmin):
    list_display = ("node_id", "title", "memory_budget", "hardware_pool", "order")
    list_editable = ("order",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "domain", "proficiency", "highlight_tag", "order")
    list_filter = ("domain",)
    search_fields = ("name", "highlight_tag")
    list_editable = ("proficiency", "order")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "category", "status_label", "upvotes", "order")
    list_filter = ("category", "is_ongoing")
    search_fields = ("title", "code", "tech_stack_csv", "description")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("order",)


@admin.register(CourseCertification)
class CourseCertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "completion_date", "order")
    list_filter = ("issuer",)
    search_fields = ("title", "issuer", "key_takeaways")
    list_editable = ("order",)


@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):
    list_display = ("role", "organization", "period", "badge_metric", "order")
    search_fields = ("role", "organization", "impact_summary")
    list_editable = ("order",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("sender_name", "sender_email", "subject", "is_read", "created_at")
    list_filter = ("is_read",)
    search_fields = ("sender_name", "sender_email", "subject", "message")
