from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home_view, name="index"),
    path("cv/", views.printable_cv_view, name="cv"),
    path("privacy/", views.privacy_policy_view, name="privacy"),
    path("privacy", views.privacy_policy_view),
    path("terms/", views.terms_of_service_view, name="terms"),
    path("terms", views.terms_of_service_view),
    path("api/projects/<int:pk>/upvote/", views.api_upvote_project, name="api_upvote_project"),
    path("api/contact/", views.api_contact_submit, name="api_contact_submit"),
]
