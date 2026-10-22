from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import ProfileSetting, Project, Skill, TimelineEntry, ContactMessage


class PortfolioCoreTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = ProfileSetting.objects.create(
            full_name="Md Najmus Sakib Rahatul",
            student_id="1119003",
            university="BAIUST, Cumilla",
            headline="Full-Stack Web Developer",
            primary_email="mdnajmussakib2003@gmail.com",
        )
        self.project = Project.objects.create(
            code="A001",
            title="BAIUST Campus Lost & Found System",
            category="Full-Stack Web",
            tech_stack="Django 5, Python, PostgreSQL",
            summary="Campus recovery platform",
            stars_count=10,
        )
        self.skill = Skill.objects.create(
            name="Django",
            category="Web & Backend",
            proficiency=90,
            badge_color="#10B981",
        )
        self.timeline = TimelineEntry.objects.create(
            title="Team Leader — Django Internship",
            organization="BAIUST Computer Club",
            period="May 2026 – Present",
            description="Leading software team",
        )

    def test_homepage_loads_successfully(self):
        response = self.client.get(reverse("core:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Md Najmus Sakib Rahatul")
        self.assertContains(response, "1119003")
        self.assertContains(response, "A001")
        self.assertContains(response, "Campus Lost")

    def test_cv_view_loads_successfully(self):
        response = self.client.get(reverse("core:cv"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Curriculum Vitae")
        self.assertContains(response, "1119003")

    def test_api_projects_list(self):
        response = self.client.get(reverse("core:api_projects_list"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertGreaterEqual(len(data["projects"]), 1)
        self.assertEqual(data["projects"][0]["code"], "A001")

    def test_api_project_detail(self):
        response = self.client.get(reverse("core:api_project_detail", kwargs={"code": "A001"}))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["project"]["title"], "BAIUST Campus Lost & Found System")

    def test_api_project_like_post(self):
        initial_stars = self.project.stars_count
        response = self.client.post(reverse("core:api_project_like", kwargs={"pk": self.project.id}))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["stars_count"], initial_stars + 1)

    def test_api_skills_list(self):
        response = self.client.get(reverse("core:api_skills_list"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertGreaterEqual(len(data["skills"]), 1)

    def test_api_contact_submission(self):
        payload = {
            "sender_name": "Arifur Rahaman",
            "sender_email": "arifur.rahaman@baiust.edu.bd",
            "subject": "Research Collaboration",
            "project_type": "Research Collaboration",
            "message": "Excellent work on the ESP32-S3 TinyML system.",
        }
        response = self.client.post(
            reverse("core:api_contact_submit"),
            data=payload,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertTrue(ContactMessage.objects.filter(sender_name="Arifur Rahaman").exists())


class DashboardCRUDTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_user(
            username="sakib_admin",
            password="baiust1119003",
            is_staff=True,
            is_superuser=True
        )
        self.project = Project.objects.create(
            code="A001",
            title="Initial Project",
            category="Full-Stack Web",
            tech_stack="Django",
            summary="Initial summary",
        )

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard:overview"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_login_successful(self):
        login_res = self.client.login(username="sakib_admin", password="baiust1119003")
        self.assertTrue(login_res)
        response = self.client.get(reverse("dashboard:overview"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Portfolio CMS Control Panel")

    def test_project_create_crud(self):
        self.client.login(username="sakib_admin", password="baiust1119003")
        payload = {
            "code": "A009",
            "title": "New Distributed Cache",
            "category": "Full-Stack Web",
            "tech_stack": "Python, Redis",
            "summary": "Distributed cache system",
            "why_built": "High load mitigation",
            "architecture": "Ring hash",
            "hardware_code_highlights": "Sub-millisecond latency",
            "github_url": "https://github.com/Sakib20050413/cache",
            "live_url": "",
            "stars_count": 5,
            "is_featured": "on",
            "order": 9,
        }
        response = self.client.post(reverse("dashboard:projects_manager"), data=payload)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Project.objects.filter(code="A009").exists())

    def test_project_delete_crud(self):
        self.client.login(username="sakib_admin", password="baiust1119003")
        response = self.client.post(reverse("dashboard:project_delete", kwargs={"pk": self.project.id}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Project.objects.filter(id=self.project.id).exists())
