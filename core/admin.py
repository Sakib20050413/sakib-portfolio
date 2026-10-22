from django.contrib import admin
from .models import ProfileSetting, Project, Skill, TimelineEntry, ContactMessage


@admin.register(ProfileSetting)
class ProfileSettingAdmin(admin.ModelAdmin):
    list_display = ("full_name", "student_id", "university", "primary_email", "updated_at")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "category", "stars_count", "is_featured", "order")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "code", "tech_stack", "summary")
    list_editable = ("is_featured", "order")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "badge_color", "order")
    list_filter = ("category",)
    search_fields = ("name",)
    list_editable = ("proficiency", "order")


@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "category", "period", "order")
    list_filter = ("category",)
    search_fields = ("title", "organization")
    list_editable = ("order",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("sender_name", "sender_email", "subject", "is_read", "is_replied", "created_at")
    list_filter = ("is_read", "is_replied")
    search_fields = ("sender_name", "sender_email", "subject", "message")
