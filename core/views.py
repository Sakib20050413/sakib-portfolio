import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.management import call_command
from django.db.utils import OperationalError, ProgrammingError
from .models import (
    ProfileConfig,
    AIArchitectureNode,
    Skill,
    Project,
    CourseCertification,
    TimelineEntry,
    ContactMessage,
)


def ensure_db_ready_and_seeded():
    """Auto-heals and seeds the database on Vercel cold start if tables or rows are missing."""
    try:
        if ProfileConfig.objects.count() == 0 or Project.objects.count() == 0 or AIArchitectureNode.objects.filter(node_id__icontains="PHOTO").exists():
            from seed_portfolio import run_seed
            run_seed()
    except (OperationalError, ProgrammingError):
        try:
            call_command("migrate", interactive=False, verbosity=0)
            from seed_portfolio import run_seed
            run_seed()
        except Exception:
            pass
    return ProfileConfig.objects.first()


def portfolio_single_page(request):
    profile = ensure_db_ready_and_seeded()
    ai_nodes = AIArchitectureNode.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    courses = CourseCertification.objects.all()
    timeline = TimelineEntry.objects.all()

    skill_domains = []
    for code, label in Skill.DOMAIN_CHOICES:
        domain_skills = [s for s in skills if s.domain == code]
        if domain_skills:
            skill_domains.append({"code": code, "label": label, "skills": domain_skills})

    projects_json = json.dumps([
        {
            "id": p.id,
            "code": p.code,
            "title": p.title,
            "category": p.get_category_display(),
            "status": p.status_label,
            "tagline": p.tagline,
            "description": p.description,
            "architecture": p.architecture_breakdown,
            "tags": p.tech_tags(),
            "liveUrl": p.live_server_url,
            "githubUrl": p.github_repo_url,
            "upvotes": p.upvotes,
        }
        for p in projects
    ])

    return render(
        request,
        "core/index.html",
        {
            "profile": profile,
            "ai_nodes": ai_nodes,
            "skill_domains": skill_domains,
            "skills": skills,
            "projects": projects,
            "projects_json": projects_json,
            "courses": courses,
            "timeline": timeline,
        },
    )


def printable_cv_view(request):
    profile = ensure_db_ready_and_seeded()
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
    ensure_db_ready_and_seeded()
    project = get_object_or_404(Project, pk=pk)
    project.upvotes += 1
    project.save(update_fields=["upvotes"])
    return JsonResponse({"ok": True, "upvotes": project.upvotes})


@require_POST
def api_submit_contact(request):
    ensure_db_ready_and_seeded()
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
        return JsonResponse({"ok": True, "message": "Message saved to database. Sakib will respond shortly."})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)


def dashboard_login_view(request):
    ensure_db_ready_and_seeded()
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
        error = "Invalid credentials. Use sakib_admin / baiust1119003"
    return render(request, "dashboard/login.html", {"error": error})


def dashboard_logout_view(request):
    logout(request)
    return redirect("portfolio_single_page")


@login_required
def dashboard_home(request):
    profile = ensure_db_ready_and_seeded()
    status_msg = None

    if request.method == "POST":
        action = request.POST.get("cms_action", "")

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
            profile.default_theme = request.POST.get("default_theme", profile.default_theme)
            profile.save()
            status_msg = "Profile photo, identity, social links, and theme updated live."

        elif action == "save_project":
            proj_id = request.POST.get("project_id", "").strip()
            defaults = {
                "code": request.POST.get("code", f"{Project.objects.count()+1:02d}"),
                "title": request.POST.get("title", ""),
                "slug": request.POST.get("slug", "").strip() or f"proj-{Project.objects.count()+1}",
                "category": request.POST.get("category", "AI_LLM"),
                "status_label": request.POST.get("status_label", "Live Production"),
                "tagline": request.POST.get("tagline", ""),
                "description": request.POST.get("description", ""),
                "architecture_breakdown": request.POST.get("architecture_breakdown", ""),
                "tech_stack_csv": request.POST.get("tech_stack_csv", ""),
                "live_server_url": request.POST.get("live_server_url", ""),
                "github_repo_url": request.POST.get("github_repo_url", ""),
            }
            if proj_id:
                Project.objects.filter(pk=proj_id).update(**defaults)
                status_msg = f"Updated project '{defaults['title']}'."
            else:
                Project.objects.create(**defaults)
                status_msg = f"Created new project '{defaults['title']}'."

        elif action == "delete_project":
            Project.objects.filter(pk=request.POST.get("project_id")).delete()
            status_msg = "Project deleted."

        elif action == "save_skill":
            Skill.objects.create(
                name=request.POST.get("name", ""),
                domain=request.POST.get("domain", "LLM_CORE"),
                proficiency=int(request.POST.get("proficiency", 94) or 94),
                highlight_tag=request.POST.get("highlight_tag", "Production AI"),
            )
            status_msg = "Skill added to portfolio and sync matrix."

        elif action == "delete_skill":
            Skill.objects.filter(pk=request.POST.get("skill_id")).delete()
            status_msg = "Skill removed."

        elif action == "save_course":
            CourseCertification.objects.create(
                title=request.POST.get("title", ""),
                issuer=request.POST.get("issuer", ""),
                completion_date=request.POST.get("completion_date", "2026"),
                credential_url=request.POST.get("credential_url", ""),
                key_takeaways=request.POST.get("key_takeaways", ""),
            )
            status_msg = "Course / Certification added."

        elif action == "delete_course":
            CourseCertification.objects.filter(pk=request.POST.get("course_id")).delete()
            status_msg = "Course / Certification deleted."

        elif action == "delete_message":
            ContactMessage.objects.filter(pk=request.POST.get("msg_id")).delete()
            status_msg = "Message deleted."

    all_skills = Skill.objects.all()
    all_projects = Project.objects.all()
    github_readme_sync = f"# {profile.full_name}\\n### {profile.role_title}\\n\\n{profile.bio_summary}\\n\\n## Core AI/ML & Full-Stack Arsenal\\n"
    for code, label in Skill.DOMAIN_CHOICES:
        d_skills = [s.name for s in all_skills if s.domain == code]
        if d_skills:
            github_readme_sync += f"- **{label}:** {', '.join(d_skills)}\\n"
    github_readme_sync += "\\n## Featured Production Systems & Live Deployments\\n"
    for p in all_projects:
        live_str = f" — [Live Server]({p.live_server_url})" if p.live_server_url else ""
        repo_str = f" | [GitHub Repo]({p.github_repo_url})" if p.github_repo_url else ""
        github_readme_sync += f"- **{p.title}** (`{p.tech_stack_csv}`): {p.tagline}{live_str}{repo_str}\\n"

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
