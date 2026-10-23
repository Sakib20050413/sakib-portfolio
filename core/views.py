import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import (
    ProfileConfig,
    AIArchitectureNode,
    Skill,
    Project,
    CourseCertification,
    TimelineEntry,
    ContactMessage,
)


def get_profile():
    profile = ProfileConfig.objects.first()
    if not profile:
        profile = ProfileConfig.objects.create()
    return profile


def portfolio_single_page(request):
    """Renders the 100% Single-Page Public AI/ML Engineer Portfolio."""
    profile = get_profile()
    ai_nodes = AIArchitectureNode.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    courses = CourseCertification.objects.all()
    timeline = TimelineEntry.objects.all()

    # Group skills by domain for the 6-Card AI/ML Arsenal Bento Grid
    skill_domains = []
    for code, label in Skill.DOMAIN_CHOICES:
        domain_skills = [s for s in skills if s.domain == code]
        if domain_skills:
            skill_domains.append({"code": code, "label": label, "skills": domain_skills})

    context = {
        "profile": profile,
        "ai_nodes": ai_nodes,
        "skill_domains": skill_domains,
        "skills": skills,
        "projects": projects,
        "courses": courses,
        "timeline": timeline,
    }
    return render(request, "core/index.html", context)


def printable_cv_view(request):
    profile = get_profile()
    return render(
        request,
        "core/cv.html",
        {
            "profile": profile,
            "skills": Skill.objects.all(),
            "projects": Project.objects.all(),
            "courses": CourseCertification.objects.all(),
            "timeline": TimelineEntry.objects.all(),
        },
    )


@require_POST
def api_upvote_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.upvotes += 1
    project.save(update_fields=["upvotes"])
    return JsonResponse({"ok": True, "upvotes": project.upvotes})


@require_POST
def api_submit_contact(request):
    try:
        data = json.loads(request.body.decode("utf-8")) if request.content_type == "application/json" else request.POST
        name = (data.get("sender_name") or "").strip()
        email = (data.get("sender_email") or "").strip()
        subject = (data.get("subject") or "Portfolio Inquiry").strip()
        message = (data.get("message") or "").strip()
        if not name or not email or not message:
            return JsonResponse({"ok": False, "error": "Please fill in your name, email, and message."}, status=400)
        ContactMessage.objects.create(
            sender_name=name,
            sender_email=email,
            subject=subject,
            message=message,
        )
        return JsonResponse({"ok": True, "message": "Message received. Sakib will respond shortly."})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)


# ==============================================================================
# HIDDEN DIRECT-URL FULL-SITE ADMIN CMS (/dashboard/)
# ==============================================================================
def dashboard_login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard_home")
    error = None
    if request.method == "POST":
        u = request.POST.get("username", "").strip()
        p = request.POST.get("password", "").strip()
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect("dashboard_home")
        error = "Invalid administrator credentials."
    return render(request, "dashboard/login.html", {"error": error})


def dashboard_logout_view(request):
    logout(request)
    return redirect("portfolio_single_page")


@login_required
def dashboard_home(request):
    profile = get_profile()
    status_msg = None

    if request.method == "POST":
        action = request.POST.get("cms_action", "")

        # 1. UPDATE PROFILE PHOTO, NAME, BIO, LINKS & THEME
        if action == "update_profile":
            profile.site_name = request.POST.get("site_name", profile.site_name)
            profile.full_name = request.POST.get("full_name", profile.full_name)
            profile.role_title = request.POST.get("role_title", profile.role_title)
            profile.hero_headline = request.POST.get("hero_headline", profile.hero_headline)
            profile.bio_summary = request.POST.get("bio_summary", profile.bio_summary)
            profile.photo_url = request.POST.get("photo_url", profile.photo_url)
            profile.location = request.POST.get("location", profile.location)
            profile.availability_text = request.POST.get("availability_text", profile.availability_text)
            profile.primary_email = request.POST.get("primary_email", profile.primary_email)
            profile.github_url = request.POST.get("github_url", profile.github_url)
            profile.linkedin_url = request.POST.get("linkedin_url", profile.linkedin_url)
            profile.kaggle_url = request.POST.get("kaggle_url", profile.kaggle_url)
            profile.twitter_url = request.POST.get("twitter_url", profile.twitter_url)
            profile.facebook_url = request.POST.get("facebook_url", profile.facebook_url)
            profile.instagram_url = request.POST.get("instagram_url", profile.instagram_url)
            profile.accent_color = request.POST.get("accent_color", profile.accent_color)
            profile.default_theme = request.POST.get("default_theme", profile.default_theme)
            profile.save()
            status_msg = "Profile photo, identity, links, and theme updated live."

        # 2. CREATE OR UPDATE PROJECT (INCLUDING LIVE SERVER URL & SCREENSHOT)
        elif action == "save_project":
            proj_id = request.POST.get("project_id", "").strip()
            defaults = {
                "code": request.POST.get("code", "09"),
                "title": request.POST.get("title", ""),
                "slug": request.POST.get("slug", "").strip() or f"proj-{Project.objects.count()+1}",
                "category": request.POST.get("category", "AI_LLM"),
                "status_label": request.POST.get("status_label", "Live Production"),
                "tagline": request.POST.get("tagline", ""),
                "description": request.POST.get("description", ""),
                "architecture_breakdown": request.POST.get("architecture_breakdown", ""),
                "tech_stack_csv": request.POST.get("tech_stack_csv", ""),
                "preview_image_url": request.POST.get("preview_image_url", ""),
                "live_server_url": request.POST.get("live_server_url", ""),
                "github_repo_url": request.POST.get("github_repo_url", ""),
                "bento_col_span": int(request.POST.get("bento_col_span", 6) or 6),
                "is_ongoing": request.POST.get("is_ongoing") == "on",
                "order": int(request.POST.get("order", 0) or 0),
            }
            if proj_id:
                Project.objects.filter(pk=proj_id).update(**defaults)
                status_msg = f"Updated project '{defaults['title']}'."
            else:
                Project.objects.create(**defaults)
                status_msg = f"Added new project '{defaults['title']}'."

        elif action == "delete_project":
            Project.objects.filter(pk=request.POST.get("project_id")).delete()
            status_msg = "Project removed."

        # 3. CREATE OR DELETE SKILL
        elif action == "save_skill":
            Skill.objects.create(
                name=request.POST.get("name", ""),
                domain=request.POST.get("domain", "LLM_CORE"),
                proficiency=int(request.POST.get("proficiency", 92) or 92),
                highlight_tag=request.POST.get("highlight_tag", "Core Production"),
            )
            status_msg = "New skill added to portfolio and sync matrix."

        elif action == "delete_skill":
            Skill.objects.filter(pk=request.POST.get("skill_id")).delete()
            status_msg = "Skill deleted."

        # 4. CREATE OR DELETE COURSE / CERTIFICATION
        elif action == "save_course":
            CourseCertification.objects.create(
                title=request.POST.get("title", ""),
                issuer=request.POST.get("issuer", ""),
                completion_date=request.POST.get("completion_date", "2026"),
                credential_url=request.POST.get("credential_url", ""),
                screenshot_url=request.POST.get("screenshot_url", ""),
                key_takeaways=request.POST.get("key_takeaways", ""),
            )
            status_msg = "Course / Certification added."

        elif action == "delete_course":
            CourseCertification.objects.filter(pk=request.POST.get("course_id")).delete()
            status_msg = "Course / Certification deleted."

        # 5. CREATE OR DELETE LOCAL MASTER AI NODE
        elif action == "save_ai_node":
            AIArchitectureNode.objects.create(
                node_id=request.POST.get("node_id", "NODE-X"),
                title=request.POST.get("title", ""),
                memory_budget=request.POST.get("memory_budget", "~1.0 GB RAM/VRAM"),
                hardware_pool=request.POST.get("hardware_pool", "CPU RAM + GPU VRAM + NPU"),
                summary=request.POST.get("summary", ""),
                mechanism_detail=request.POST.get("mechanism_detail", ""),
            )
            status_msg = "Master AI Architecture Node added."

        elif action == "delete_ai_node":
            AIArchitectureNode.objects.filter(pk=request.POST.get("node_id_pk")).delete()
            status_msg = "AI Architecture Node removed."

        # 6. DELETE CONTACT MESSAGE
        elif action == "delete_message":
            ContactMessage.objects.filter(pk=request.POST.get("msg_id")).delete()
            status_msg = "Message deleted."

    # Generate LinkedIn & GitHub Profile README Sync Markdown automatically from live DB
    all_skills = Skill.objects.all()
    all_projects = Project.objects.all()
    github_readme_sync = f"# {profile.full_name}\n### {profile.role_title}\n\n{profile.bio_summary}\n\n## Core AI/ML & Full-Stack Arsenal\n"
    for code, label in Skill.DOMAIN_CHOICES:
        d_skills = [s.name for s in all_skills if s.domain == code]
        if d_skills:
            github_readme_sync += f"- **{label}:** {', '.join(d_skills)}\n"
    github_readme_sync += "\n## Featured Production Systems & Live Deployments\n"
    for p in all_projects:
        live_str = f" — [Live Server]({p.live_server_url})" if p.live_server_url else ""
        repo_str = f" | [GitHub Repo]({p.github_repo_url})" if p.github_repo_url else ""
        github_readme_sync += f"- **{p.title}** (`{p.tech_stack_csv}`): {p.tagline}{live_str}{repo_str}\n"

    return render(
        request,
        "dashboard/index.html",
        {
            "profile": profile,
            "projects": all_projects,
            "skills": all_skills,
            "skill_choices": Skill.DOMAIN_CHOICES,
            "project_categories": Project.CATEGORY_CHOICES,
            "courses": CourseCertification.objects.all(),
            "ai_nodes": AIArchitectureNode.objects.all(),
            "messages_inbox": ContactMessage.objects.all(),
            "github_readme_sync": github_readme_sync,
            "status_msg": status_msg,
        },
    )
