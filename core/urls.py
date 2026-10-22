from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("cv/", views.cv_view, name="cv"),
    # APIs
    path("api/projects/", views.api_projects_list, name="api_projects_list"),
    path("api/projects/<str:code>/", views.api_project_detail, name="api_project_detail"),
    path("api/projects/<int:pk>/like/", views.api_project_like, name="api_project_like"),
    path("api/skills/", views.api_skills_list, name="api_skills_list"),
    path("api/contact/", views.api_contact_submit, name="api_contact_submit"),
]
