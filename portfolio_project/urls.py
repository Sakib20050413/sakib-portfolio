from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path("", views.portfolio_single_page, name="portfolio_single_page"),
    path("cv/", views.printable_cv_view, name="printable_cv"),
    path("api/projects/<int:pk>/upvote/", views.api_upvote_project, name="api_upvote_project"),
    path("api/contact/submit/", views.api_submit_contact, name="api_submit_contact"),
    # Hidden Direct-URL Full-Site Admin CMS (Not linked anywhere on public page!)
    path("dashboard/", views.dashboard_home, name="dashboard_home"),
    path("dashboard/login/", views.dashboard_login_view, name="dashboard_login"),
    path("dashboard/logout/", views.dashboard_logout_view, name="dashboard_logout"),
    path("django-admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
