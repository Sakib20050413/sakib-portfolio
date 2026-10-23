from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.portfolio_single_page, name="index"),
    path("cv/", views.printable_cv_view, name="cv"),
    path("api/projects/<int:pk>/upvote/", views.api_upvote_project, name="api_upvote_project"),
    path("api/contact/submit/", views.api_submit_contact, name="api_submit_contact"),
]
