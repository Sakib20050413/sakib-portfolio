import json
from django.conf import settings
from django.core.management import call_command
from django.test import TestCase, Client
from django.urls import reverse
from core.models import (
    SiteSettings,
    About,
    SkillGroup,
    Skill,
    Project,
    Experience,
    Certificate,
    ContactMessage,
)


class PortfolioCoreTests(TestCase):
    def setUp(self):
        self.client = Client()
        call_command("seed_portfolio")

    def test_homepage_loads_successfully(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Md Najmus Sakib Rahatul")
        self.assertContains(response, "BAIUST Campus Lost")
        self.assertContains(response, "Bio-Acoustic Mosquito Vector Trap")

    def test_standard_admin_returns_404(self):
        """Verifies requirement: /admin/ must return 404."""
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 404)

        response_sub = self.client.get("/admin/login/")
        self.assertEqual(response_sub.status_code, 404)

    def test_secret_admin_url_is_accessible(self):
        """Verifies the secret admin slug from environment variable is active."""
        admin_slug = getattr(settings, "ADMIN_URL", "studio-7f3k").strip("/")
        response = self.client.get(f"/{admin_slug}/login/")
        self.assertEqual(response.status_code, 200)

    def test_printable_cv_loads(self):
        response = self.client.get(reverse("printable_cv"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Md Najmus Sakib Rahatul")

    def test_api_profile_json(self):
        response = self.client.get(reverse("api_profile_json"))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(data["name"], "Md Najmus Sakib Rahatul")
        self.assertIn("skill_groups", data)
        self.assertIn("projects", data)
        self.assertGreater(len(data["projects"]), 0)

    def test_contact_form_submission_success(self):
        initial_count = ContactMessage.objects.count()
        payload = {
            "name": "Jane Recruiter",
            "email": "jane@techcorp.com",
            "message": "We would love to discuss an AI/ML engineering opportunity with you.",
        }
        response = self.client.post(
            reverse("api_contact_submit"),
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["ok"])
        self.assertEqual(ContactMessage.objects.count(), initial_count + 1)
        msg = ContactMessage.objects.first()
        self.assertEqual(msg.name, "Jane Recruiter")
        self.assertEqual(msg.email, "jane@techcorp.com")

    def test_contact_form_honeypot_absorbs_bot_without_saving(self):
        initial_count = ContactMessage.objects.count()
        payload = {
            "name": "Spam Bot",
            "email": "bot@spam.com",
            "message": "Buy cheap crypto",
            "company_hp": "Spam Company Inc",  # Honeypot filled
        }
        response = self.client.post(
            reverse("api_contact_submit"),
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["ok"])
        # Message count must NOT increase
        self.assertEqual(ContactMessage.objects.count(), initial_count)

    def test_project_upvote_api(self):
        project = Project.objects.first()
        initial_upvotes = project.upvotes
        response = self.client.post(reverse("api_upvote_project", kwargs={"pk": project.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["upvotes"], initial_upvotes + 1)
        project.refresh_from_db()
        self.assertEqual(project.upvotes, initial_upvotes + 1)
