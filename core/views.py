import json
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.conf import settings
from .models import (
    SiteSettings,
    About,
    SkillGroup,
    Skill,
    Project,
    Experience,
    Certificate,
    ContactMessage,
)
from .management.commands.seed_portfolio import run_canonical_seed


def get_or_seed_canonical_data():
    """Ensures database has canonical content if empty."""
    if not SiteSettings.objects.exists() or not Project.objects.exists():
        run_canonical_seed()
    return SiteSettings.objects.first(), About.objects.first()


def home_view(request):
    """Renders the main single-page portfolio."""
    site_settings, about = get_or_seed_canonical_data()

    skill_groups = SkillGroup.objects.filter(visible=True).prefetch_related(
        "skills"
    ).order_by("order")

    projects = Project.objects.filter(visible=True).order_by("order")
    experiences = Experience.objects.filter(visible=True).order_by("order")
    certificates = Certificate.objects.filter(visible=True).order_by("order")

    context = {
        "settings": site_settings,
        "about": about,
        "skill_groups": skill_groups,
        "projects": projects,
        "experiences": experiences,
        "certificates": certificates,
    }
    return render(request, "core/index.html", context)


def printable_cv_view(request):
    """Renders a clean, ATS-compliant, printable CV."""
    site_settings, about = get_or_seed_canonical_data()
    skill_groups = SkillGroup.objects.filter(visible=True).prefetch_related("skills").order_by("order")
    projects = Project.objects.filter(visible=True).order_by("order")
    experiences = Experience.objects.filter(visible=True).order_by("order")
    certificates = Certificate.objects.filter(visible=True).order_by("order")

    context = {
        "settings": site_settings,
        "about": about,
        "skill_groups": skill_groups,
        "projects": projects,
        "experiences": experiences,
        "certificates": certificates,
    }
    return render(request, "core/cv.html", context)


def api_profile_json(request):
    """Read-only JSON endpoint exposing profile, skills, and projects for external sync."""
    site_settings, about = get_or_seed_canonical_data()

    skill_groups = []
    for g in SkillGroup.objects.filter(visible=True).order_by("order"):
        skill_groups.append({
            "group": g.name,
            "skills": [
                {"name": s.name, "level": s.level_label}
                for s in g.skills.filter(visible=True).order_by("order")
            ]
        })

    projects = []
    for p in Project.objects.filter(visible=True).order_by("order"):
        projects.append({
            "title": p.title,
            "category": p.category,
            "summary": p.summary,
            "description": p.description,
            "tech_stack": p.tech_tags(),
            "repo_url": p.repo_url,
            "live_url": p.live_url,
            "status": p.status,
            "upvotes": p.upvotes,
        })

    data = {
        "name": site_settings.full_name if site_settings else "Md Najmus Sakib Rahatul",
        "role": site_settings.role_title if site_settings else "Aspiring AI Engineer",
        "location": about.location if about else "Cumilla / Dhaka, Bangladesh",
        "bio": about.bio_paragraph_1 if about else "",
        "contact": {
            "email": site_settings.primary_email if site_settings else "",
            "github": site_settings.github_url if site_settings else "",
            "linkedin": site_settings.linkedin_url if site_settings else "",
            "kaggle": site_settings.kaggle_url if site_settings else "",
        },
        "skill_groups": skill_groups,
        "projects": projects,
        "synced_at": timezone.now().isoformat(),
    }
    return JsonResponse(data, safe=False, json_dumps_params={"indent": 2})


@require_POST
def api_contact_submit(request):
    """Handles contact form submissions with honeypot spam protection and rate limiting."""
    # 1. Parse payload (JSON or Form-data)
    if request.content_type == "application/json":
        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception:
            return JsonResponse({"ok": False, "error": "Invalid JSON payload."}, status=400)
    else:
        data = request.POST

    # 2. Honeypot check (hidden field)
    honeypot = data.get("company_hp", "").strip() or data.get("website_hp", "").strip()
    if honeypot:
        # Silently absorb bot submissions
        return JsonResponse({"ok": True, "message": "Thank you! Your message has been received."})

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not name or not email or not message:
        return JsonResponse({"ok": False, "error": "Please provide your name, email, and message."}, status=400)

    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({"ok": False, "error": "Please enter a valid email address."}, status=400)

    # 3. Rate limiting check (session-based)
    last_sent = request.session.get("last_contact_sent")
    now_ts = timezone.now().timestamp()
    if last_sent and (now_ts - last_sent) < 30:
        return JsonResponse({"ok": False, "error": "Please wait a moment before sending another message."}, status=429)

    # 4. Save to Database
    msg = ContactMessage.objects.create(name=name, email=email, message=message)
    request.session["last_contact_sent"] = now_ts

    # 5. Email notification dispatch (best-effort)
    site_settings = SiteSettings.objects.first()
    recipient_email = site_settings.primary_email if site_settings else settings.DEFAULT_FROM_EMAIL
    try:
        send_mail(
            subject=f"[Portfolio Contact] Message from {name}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            fail_silently=True,
        )
    except Exception:
        pass

    return JsonResponse({"ok": True, "message": "Thank you! Your message has been received."})


@require_POST
def api_upvote_project(request, pk):
    """Increments a project's upvotes count."""
    project = get_object_or_404(Project, pk=pk)
    project.upvotes += 1
    project.save(update_fields=["upvotes"])
    return JsonResponse({"ok": True, "upvotes": project.upvotes})
