from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from core.models import ProfileSetting, Project, Skill, TimelineEntry, ContactMessage


def login_view(request):
    """Custom aesthetic authentication page for the portfolio admin CMS."""
    if request.user.is_authenticated:
        return redirect("dashboard:overview")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, Sakib! Terminal authentication cleared.")
            next_url = request.GET.get("next") or reverse("dashboard:overview")
            return redirect(next_url)
        else:
            messages.error(request, "Invalid Credentials. Access Denied by Security Protocol.")

    return render(request, "dashboard/login.html")


def logout_view(request):
    """Log out admin session."""
    logout(request)
    messages.info(request, "Session terminated safely.")
    return redirect("dashboard:login")


@login_required
def overview(request):
    """Admin Dashboard overview with live telemetry and system counts."""
    profile = ProfileSetting.load()
    projects = Project.objects.all().order_by("order", "code")
    skills = Skill.objects.all().order_by("order", "name")
    timeline = TimelineEntry.objects.all().order_by("order", "-id")
    messages_qs = ContactMessage.objects.all()

    total_projects = projects.count()
    total_skills = skills.count()
    total_stars = sum(p.stars_count for p in projects)
    unread_messages = messages_qs.filter(is_read=False).count()
    recent_messages = messages_qs.order_by("-created_at")[:5]

    context = {
        "profile": profile,
        "total_projects": total_projects,
        "total_skills": total_skills,
        "total_stars": total_stars,
        "unread_messages": unread_messages,
        "recent_messages": recent_messages,
        "recent_projects": projects[:4],
        "active_tab": "overview",
    }
    return render(request, "dashboard/overview.html", context)


@login_required
def profile_manager(request):
    """Edit Profile Settings and all social/dev URLs."""
    profile = ProfileSetting.load()

    if request.method == "POST":
        profile.full_name = request.POST.get("full_name", profile.full_name)
        profile.display_handle = request.POST.get("display_handle", profile.display_handle)
        profile.student_id = request.POST.get("student_id", profile.student_id)
        profile.university = request.POST.get("university", profile.university)
        profile.department_batch = request.POST.get("department_batch", profile.department_batch)
        profile.headline = request.POST.get("headline", profile.headline)
        profile.bio = request.POST.get("bio", profile.bio)
        profile.primary_email = request.POST.get("primary_email", profile.primary_email)
        profile.academic_email = request.POST.get("academic_email", profile.academic_email)
        profile.location = request.POST.get("location", profile.location)
        profile.availability_status = request.POST.get("availability_status", profile.availability_status)
        profile.cv_url = request.POST.get("cv_url", profile.cv_url)

        # Socials
        profile.github_url = request.POST.get("github_url", profile.github_url)
        profile.linkedin_url = request.POST.get("linkedin_url", profile.linkedin_url)
        profile.x_twitter_url = request.POST.get("x_twitter_url", profile.x_twitter_url)
        profile.facebook_url = request.POST.get("facebook_url", profile.facebook_url)
        profile.instagram_url = request.POST.get("instagram_url", profile.instagram_url)
        profile.leetcode_url = request.POST.get("leetcode_url", profile.leetcode_url)
        profile.kaggle_url = request.POST.get("kaggle_url", profile.kaggle_url)
        profile.scholar_url = request.POST.get("scholar_url", profile.scholar_url)
        profile.blog_url = request.POST.get("blog_url", profile.blog_url)

        profile.save()
        messages.success(request, "Profile settings and social links updated successfully!")
        return redirect("dashboard:profile_manager")

    context = {
        "profile": profile,
        "active_tab": "profile",
    }
    return render(request, "dashboard/profile.html", context)


@login_required
def projects_manager(request):
    """List all projects and create new project."""
    if request.method == "POST":
        code = request.POST.get("code", "").strip().upper()
        title = request.POST.get("title", "").strip()
        category = request.POST.get("category", "Full-Stack Web")
        tech_stack = request.POST.get("tech_stack", "").strip()
        summary = request.POST.get("summary", "").strip()
        why_built = request.POST.get("why_built", "").strip()
        architecture = request.POST.get("architecture", "").strip()
        hardware_code_highlights = request.POST.get("hardware_code_highlights", "").strip()
        github_url = request.POST.get("github_url", "").strip()
        live_url = request.POST.get("live_url", "").strip()
        stars_count = int(request.POST.get("stars_count", 0) or 0)
        is_featured = request.POST.get("is_featured") == "on"
        order = int(request.POST.get("order", 0) or 0)

        if not code or not title or not summary:
            messages.error(request, "Code, Title, and Summary are required fields.")
        else:
            Project.objects.create(
                code=code,
                title=title,
                category=category,
                tech_stack=tech_stack,
                summary=summary,
                why_built=why_built,
                architecture=architecture,
                hardware_code_highlights=hardware_code_highlights,
                github_url=github_url,
                live_url=live_url,
                stars_count=stars_count,
                is_featured=is_featured,
                order=order,
            )
            messages.success(request, f"Project [{code}] '{title}' created successfully!")
            return redirect("dashboard:projects_manager")

    projects = Project.objects.all().order_by("order", "code")
    context = {
        "projects": projects,
        "active_tab": "projects",
    }
    return render(request, "dashboard/projects.html", context)


@login_required
def project_edit(request, pk):
    """Edit an existing project."""
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.code = request.POST.get("code", project.code).strip().upper()
        project.title = request.POST.get("title", project.title).strip()
        project.category = request.POST.get("category", project.category)
        project.tech_stack = request.POST.get("tech_stack", project.tech_stack).strip()
        project.summary = request.POST.get("summary", project.summary).strip()
        project.why_built = request.POST.get("why_built", project.why_built).strip()
        project.architecture = request.POST.get("architecture", project.architecture).strip()
        project.hardware_code_highlights = request.POST.get("hardware_code_highlights", project.hardware_code_highlights).strip()
        project.github_url = request.POST.get("github_url", project.github_url).strip()
        project.live_url = request.POST.get("live_url", project.live_url).strip()
        project.stars_count = int(request.POST.get("stars_count", project.stars_count) or 0)
        project.is_featured = request.POST.get("is_featured") == "on"
        project.order = int(request.POST.get("order", project.order) or 0)

        project.save()
        messages.success(request, f"Project [{project.code}] updated successfully!")
        return redirect("dashboard:projects_manager")

    projects = Project.objects.all().order_by("order", "code")
    context = {
        "project": project,
        "projects": projects,
        "editing": True,
        "active_tab": "projects",
    }
    return render(request, "dashboard/projects.html", context)


@login_required
def project_delete(request, pk):
    """Delete a project."""
    if request.method == "POST":
        project = get_object_or_404(Project, pk=pk)
        code = project.code
        project.delete()
        messages.success(request, f"Project [{code}] was deleted permanently.")
    return redirect("dashboard:projects_manager")


@login_required
def skills_manager(request):
    """List skills, configure physics ball colors, add new skills."""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        category = request.POST.get("category", "Web & Backend")
        proficiency = int(request.POST.get("proficiency", 85) or 85)
        badge_color = request.POST.get("badge_color", "#8B5CF6").strip()
        radius = int(request.POST.get("radius", 28) or 28)
        order = int(request.POST.get("order", 0) or 0)

        if not name:
            messages.error(request, "Skill name cannot be empty.")
        else:
            Skill.objects.create(
                name=name,
                category=category,
                proficiency=proficiency,
                badge_color=badge_color,
                radius=radius,
                order=order,
            )
            messages.success(request, f"Skill '{name}' added to tech-stack and physics pit!")
            return redirect("dashboard:skills_manager")

    skills = Skill.objects.all().order_by("order", "name")
    context = {
        "skills": skills,
        "active_tab": "skills",
    }
    return render(request, "dashboard/skills.html", context)


@login_required
def skill_edit(request, pk):
    """Edit skill parameters."""
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        skill.name = request.POST.get("name", skill.name).strip()
        skill.category = request.POST.get("category", skill.category)
        skill.proficiency = int(request.POST.get("proficiency", skill.proficiency) or 85)
        skill.badge_color = request.POST.get("badge_color", skill.badge_color).strip()
        skill.radius = int(request.POST.get("radius", skill.radius) or 28)
        skill.order = int(request.POST.get("order", skill.order) or 0)

        skill.save()
        messages.success(request, f"Skill '{skill.name}' updated successfully!")
        return redirect("dashboard:skills_manager")

    skills = Skill.objects.all().order_by("order", "name")
    context = {
        "skill": skill,
        "skills": skills,
        "editing": True,
        "active_tab": "skills",
    }
    return render(request, "dashboard/skills.html", context)


@login_required
def skill_delete(request, pk):
    """Delete a skill."""
    if request.method == "POST":
        skill = get_object_or_404(Skill, pk=pk)
        name = skill.name
        skill.delete()
        messages.success(request, f"Skill '{name}' deleted.")
    return redirect("dashboard:skills_manager")


@login_required
def timeline_manager(request):
    """List timeline entries and create new timeline milestone."""
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        organization = request.POST.get("organization", "").strip()
        category = request.POST.get("category", "Experience")
        period = request.POST.get("period", "").strip()
        description = request.POST.get("description", "").strip()
        order = int(request.POST.get("order", 0) or 0)

        if not title or not organization:
            messages.error(request, "Title and Organization are required.")
        else:
            TimelineEntry.objects.create(
                title=title,
                organization=organization,
                category=category,
                period=period,
                description=description,
                order=order,
            )
            messages.success(request, f"Timeline milestone '{title}' created!")
            return redirect("dashboard:timeline_manager")

    timeline = TimelineEntry.objects.all().order_by("order", "-id")
    context = {
        "timeline": timeline,
        "active_tab": "timeline",
    }
    return render(request, "dashboard/timeline.html", context)


@login_required
def timeline_edit(request, pk):
    """Edit timeline milestone."""
    entry = get_object_or_404(TimelineEntry, pk=pk)
    if request.method == "POST":
        entry.title = request.POST.get("title", entry.title).strip()
        entry.organization = request.POST.get("organization", entry.organization).strip()
        entry.category = request.POST.get("category", entry.category)
        entry.period = request.POST.get("period", entry.period).strip()
        entry.description = request.POST.get("description", entry.description).strip()
        entry.order = int(request.POST.get("order", entry.order) or 0)

        entry.save()
        messages.success(request, f"Milestone '{entry.title}' updated!")
        return redirect("dashboard:timeline_manager")

    timeline = TimelineEntry.objects.all().order_by("order", "-id")
    context = {
        "entry": entry,
        "timeline": timeline,
        "editing": True,
        "active_tab": "timeline",
    }
    return render(request, "dashboard/timeline.html", context)


@login_required
def timeline_delete(request, pk):
    """Delete a timeline milestone."""
    if request.method == "POST":
        entry = get_object_or_404(TimelineEntry, pk=pk)
        title = entry.title
        entry.delete()
        messages.success(request, f"Milestone '{title}' deleted.")
    return redirect("dashboard:timeline_manager")


@login_required
def messages_inbox(request):
    """View and triage portfolio inquiries."""
    filter_type = request.GET.get("filter", "all")
    messages_qs = ContactMessage.objects.all().order_by("-created_at")

    if filter_type == "unread":
        messages_qs = messages_qs.filter(is_read=False)
    elif filter_type == "replied":
        messages_qs = messages_qs.filter(is_replied=True)

    context = {
        "messages_list": messages_qs,
        "filter_type": filter_type,
        "total_count": ContactMessage.objects.count(),
        "unread_count": ContactMessage.objects.filter(is_read=False).count(),
        "active_tab": "messages",
    }
    return render(request, "dashboard/messages.html", context)


@login_required
def message_toggle_read(request, pk):
    """Toggle read status."""
    if request.method == "POST":
        msg = get_object_or_404(ContactMessage, pk=pk)
        msg.is_read = not msg.is_read
        msg.save(update_fields=["is_read"])
        status_str = "Read" if msg.is_read else "Unread"
        messages.success(request, f"Message marked as {status_str}.")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse("dashboard:messages_inbox")))


@login_required
def message_toggle_replied(request, pk):
    """Toggle replied status."""
    if request.method == "POST":
        msg = get_object_or_404(ContactMessage, pk=pk)
        msg.is_replied = not msg.is_replied
        msg.save(update_fields=["is_replied"])
        status_str = "Replied" if msg.is_replied else "Pending Reply"
        messages.success(request, f"Message marked as {status_str}.")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse("dashboard:messages_inbox")))


@login_required
def message_delete(request, pk):
    """Delete a message."""
    if request.method == "POST":
        msg = get_object_or_404(ContactMessage, pk=pk)
        sender = msg.sender_name
        msg.delete()
        messages.success(request, f"Message from {sender} deleted.")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse("dashboard:messages_inbox")))
