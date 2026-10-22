from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.overview, name="overview"),
    path("profile/", views.profile_manager, name="profile_manager"),
    path("projects/", views.projects_manager, name="projects_manager"),
    path("projects/<int:pk>/edit/", views.project_edit, name="project_edit"),
    path("projects/<int:pk>/delete/", views.project_delete, name="project_delete"),
    path("skills/", views.skills_manager, name="skills_manager"),
    path("skills/<int:pk>/edit/", views.skill_edit, name="skill_edit"),
    path("skills/<int:pk>/delete/", views.skill_delete, name="skill_delete"),
    path("timeline/", views.timeline_manager, name="timeline_manager"),
    path("timeline/<int:pk>/edit/", views.timeline_edit, name="timeline_edit"),
    path("timeline/<int:pk>/delete/", views.timeline_delete, name="timeline_delete"),
    path("messages/", views.messages_inbox, name="messages_inbox"),
    path("messages/<int:pk>/toggle-read/", views.message_toggle_read, name="message_toggle_read"),
    path("messages/<int:pk>/toggle-replied/", views.message_toggle_replied, name="message_toggle_replied"),
    path("messages/<int:pk>/delete/", views.message_delete, name="message_delete"),
]
