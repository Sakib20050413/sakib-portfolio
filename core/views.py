import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .models import ProfileSetting, Project, Skill, TimelineEntry, ContactMessage


def global_portfolio_context(request):
    """Context processor providing basic profile across all templates."""
    try:
        profile = ProfileSetting.load()
    except Exception:
        profile = None
    return {"profile": profile}


def index(request):
    """Full-Viewport 12-Column Apple & Awwwards-grade portfolio view."""
    profile = ProfileSetting.load()
    projects = Project.objects.all().order_by("order", "code")
    skills = Skill.objects.all().order_by("order", "name")
    timeline = TimelineEntry.objects.all().order_by("order", "-id")

    # Categories for filters
    categories = ["All", "Full-Stack Web", "Embedded IoT & TinyML", "Desktop & DSP"]
    
    # Skill groupings (4 Categories)
    skills_backend = skills.filter(category="Backend & Full-Stack Web")
    skills_frontend = skills.filter(category="Frontend & Interactive UI")
    skills_embedded = skills.filter(category="Embedded AI, IoT & DSP")
    skills_tools = skills.filter(category="Databases, Tools & Cloud")

    # Metrics
    total_projects = projects.count()
    total_stars = sum(p.stars_count for p in projects)
    total_skills = skills.count()

    context = {
        "profile": profile,
        "projects": projects,
        "skills": skills,
        "skills_backend": skills_backend,
        "skills_frontend": skills_frontend,
        "skills_embedded": skills_embedded,
        "skills_tools": skills_tools,
        "timeline": timeline,
        "categories": categories,
        "total_projects": total_projects,
        "total_stars": total_stars,
        "total_skills": total_skills,
    }
    return render(request, "core/index.html", context)


def cv_view(request):
    """Clean, printable, and downloadable CV view for Md Najmus Sakib Rahatul."""
    profile = ProfileSetting.load()
    projects = Project.objects.all().order_by("order", "code")
    skills = Skill.objects.all().order_by("order", "name")
    timeline = TimelineEntry.objects.all().order_by("order", "-id")

    context = {
        "profile": profile,
        "projects": projects,
        "skills": skills,
        "timeline": timeline,
    }
    return render(request, "core/cv.html", context)


# ==========================================
# RESTful / AJAX API Endpoints for Frontend
# ==========================================

@require_GET
def api_projects_list(request):
    """Returns JSON list of all projects for dynamic UI filters."""
    category = request.GET.get("category")
    projects_qs = Project.objects.all().order_by("order", "code")
    if category and category != "All":
        projects_qs = projects_qs.filter(category=category)

    data = []
    for p in projects_qs:
        data.append({
            "id": p.id,
            "code": p.code,
            "title": p.title,
            "category": p.category,
            "tech_stack": p.tech_stack,
            "tech_list": p.tech_list,
            "summary": p.summary,
            "why_built": p.why_built,
            "architecture": p.architecture,
            "hardware_code_highlights": p.hardware_code_highlights,
            "github_url": p.github_url,
            "live_url": p.live_url,
            "stars_count": p.stars_count,
            "is_featured": p.is_featured,
        })
    return JsonResponse({"status": "success", "count": len(data), "projects": data})


@require_GET
def api_project_detail(request, code):
    """Fetch single project data by code (e.g., A001)."""
    p = get_object_or_404(Project, code__iexact=code)
    data = {
        "id": p.id,
        "code": p.code,
        "title": p.title,
        "category": p.category,
        "tech_stack": p.tech_stack,
        "tech_list": p.tech_list,
        "summary": p.summary,
        "why_built": p.why_built,
        "architecture": p.architecture,
        "hardware_code_highlights": p.hardware_code_highlights,
        "github_url": p.github_url,
        "live_url": p.live_url,
        "stars_count": p.stars_count,
    }
    return JsonResponse({"status": "success", "project": data})


@require_POST
def api_project_like(request, pk):
    """Optimistic AJAX star / upvote counter increment."""
    project = get_object_or_404(Project, pk=pk)
    project.stars_count += 1
    project.save(update_fields=["stars_count"])
    return JsonResponse({
        "status": "success",
        "project_id": project.id,
        "code": project.code,
        "stars_count": project.stars_count,
        "message": f"Starred project {project.code} successfully!"
    })


@require_POST
def api_contact_submit(request):
    """Receive and validate AJAX contact message submissions without page reload."""
    try:
        if request.content_type == "application/json":
            payload = json.loads(request.body.decode("utf-8"))
        else:
            payload = request.POST

        name = payload.get("sender_name", "").strip()
        email = payload.get("sender_email", "").strip()
        subject = payload.get("subject", "").strip()
        project_type = payload.get("project_type", "").strip()
        message = payload.get("message", "").strip()

        if not name or not email or not message:
            return JsonResponse({
                "status": "error",
                "message": "Name, email, and message are required."
            }, status=400)

        contact = ContactMessage.objects.create(
            sender_name=name,
            sender_email=email,
            subject=subject or f"Portfolio inquiry from {name}",
            project_type=project_type,
            message=message,
        )

        return JsonResponse({
            "status": "success",
            "message": f"Thank you, {name}. Your message has been received.",
            "contact_id": contact.id,
        })
    except Exception as exc:
        return JsonResponse({
            "status": "error",
            "message": f"Error saving message: {str(exc)}"
        }, status=500)


@require_GET
def api_skills_list(request):
    """Returns JSON payload of skills."""
    skills_qs = Skill.objects.all().order_by("order", "name")
    data = []
    for s in skills_qs:
        data.append({
            "id": s.id,
            "name": s.name,
            "category": s.category,
            "proficiency": s.proficiency,
        })
    return JsonResponse({"status": "success", "skills": data})
