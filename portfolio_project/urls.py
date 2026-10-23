import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import Http404
from django.urls import path
from django.views.generic import RedirectView
from core import views

admin_slug = getattr(settings, "ADMIN_URL", "studio-7f3k").strip("/")


def blocked_admin_view(request, *args, **kwargs):
    """Explicitly returns 404 for /admin/ as required by specification."""
    raise Http404("Standard admin path disabled. Access via configured secret CMS slug.")


urlpatterns = [
    # Explicit 404 for standard admin URLs
    path("admin/", blocked_admin_view),
    path("admin/<path:subpath>", blocked_admin_view),

    # Secret Admin CMS mounted at dynamic environment variable slug
    path(f"{admin_slug}/", admin.site.urls),

    # Public Single-Page Portfolio & ATS CV
    path("", views.home_view, name="home"),
    path("cv/", views.printable_cv_view, name="printable_cv"),

    # Direct Section Redirects for smooth UX
    path("about/", RedirectView.as_view(url="/#about", permanent=False)),
    path("projects/", RedirectView.as_view(url="/#projects", permanent=False)),
    path("skills/", RedirectView.as_view(url="/#skills", permanent=False)),
    path("hardware/", RedirectView.as_view(url="/#hardware", permanent=False)),
    path("experience/", RedirectView.as_view(url="/#timeline", permanent=False)),
    path("timeline/", RedirectView.as_view(url="/#timeline", permanent=False)),
    path("faq/", RedirectView.as_view(url="/#faq", permanent=False)),
    path("contact/", RedirectView.as_view(url="/#contact", permanent=False)),

    # REST APIs & Integration Hooks
    path("api/profile.json", views.api_profile_json, name="api_profile_json"),
    path("api/contact/", views.api_contact_submit, name="api_contact_submit"),
    path("api/projects/<int:pk>/upvote/", views.api_upvote_project, name="api_upvote_project"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
