from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import (
    ProfileConfig,
    AIArchitectureNode,
    Skill,
    Project,
    CourseCertification,
    TimelineEntry,
    ContactMessage,
)


class PortfolioV5Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = ProfileConfig.objects.create(
            full_name="Md Najmus Sakib Rahatul",
            role_title="AI/ML Engineer & Full-Stack AI Systems Architect",
            primary_email="mdnajmussakib2003@gmail.com",
            hero_headline="Architecting Sovereign Local Multi-Model AI Systems",
        )
        self.node = AIArchitectureNode.objects.create(
            node_id="MASTER-00",
            title="Always-Resident Master AI Router",
            memory_budget="~420 MB RAM",
            summary="Prompt router",
            mechanism_detail="Unified memory paging",
        )
        self.project = Project.objects.create(
            code="01",
            title="NexusLocal Master AI",
            slug="nexuslocal-master-ai",
            category="AI_LLM",
            tagline="Sovereign local AI",
            description="Runs locally",
            architecture_breakdown="Unified memory",
            tech_stack_csv="PyTorch, FastAPI",
            upvotes=10,
        )
        self.skill = Skill.objects.create(
            name="PyTorch",
            domain="LLM_CORE",
            proficiency=95,
            highlight_tag="Core AI Stack",
        )
        self.course = CourseCertification.objects.create(
            title="Full-Stack Python & Django Internship",
            issuer="BAIUST Computer Club",
            completion_date="2026",
            key_takeaways="Team Leader",
        )
        self.timeline = TimelineEntry.objects.create(
            role="AI/ML Systems Architect",
            organization="Independent Research",
            period="2026 – Present",
            impact_summary="Master AI research",
        )
        self.admin_user = User.objects.create_superuser(
            username="sakib_admin",
            email="mdnajmussakib2003@gmail.com",
            password="baiust1119003"
        )

    def test_homepage_loads_successfully(self):
        response = self.client.get(reverse("portfolio_single_page"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Md Najmus Sakib Rahatul")
        self.assertContains(response, "NexusLocal Master AI")
        self.assertContains(response, "PyTorch")
        # Ensure NO visible admin button in public navbar
        self.assertNotContains(response, ">/admin<")
        self.assertNotContains(response, ">Admin CMS<")

    def test_cv_view_loads_successfully(self):
        response = self.client.get(reverse("printable_cv"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CV")
        self.assertContains(response, "Md Najmus Sakib Rahatul")

    def test_api_upvote_project(self):
        initial_upvotes = self.project.upvotes
        response = self.client.post(reverse("api_upvote_project", kwargs={"pk": self.project.id}))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["ok"])
        self.assertEqual(data["upvotes"], initial_upvotes + 1)

    def test_api_contact_submission(self):
        payload = {
            "sender_name": "Recruiter Team",
            "sender_email": "recruiting@ai-startup.com",
            "subject": "AI/ML Role Interview",
            "message": "We reviewed your Sovereign Local Master AI architecture and would love to interview you.",
        }
        response = self.client.post(
            reverse("api_submit_contact"),
            data=payload,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["ok"])
        self.assertTrue(ContactMessage.objects.filter(sender_name="Recruiter Team").exists())

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard_home"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/dashboard/login/", response.url)

    def test_dashboard_authenticated_access(self):
        self.client.login(username="sakib_admin", password="baiust1119003")
        response = self.client.get(reverse("dashboard_home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "HIDDEN ADMIN CMS")
        self.assertContains(response, "Full-Site Dynamic Controller")
