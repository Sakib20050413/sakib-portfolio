import os
from django.core.management.base import BaseCommand
from core.models import (
    SiteSettings,
    About,
    SkillGroup,
    Skill,
    Project,
    Experience,
    Certificate,
)


def run_canonical_seed():
    """Seeds the database with Sakib's canonical, 100% verified portfolio content."""
    # 1. Site Settings
    settings_obj, _ = SiteSettings.objects.get_or_create(
        id=1,
        defaults={
            "site_name": "Sakib // AI & Systems",
            "full_name": "Md Najmus Sakib Rahatul",
            "role_title": "Aspiring AI Engineer · Full-Stack Developer",
            "tagline": "Building sovereign local AI inference systems and resilient web platforms.",
            "hero_photo_url": "https://avatars.githubusercontent.com/u/166808901?v=4",
            "resume_url": "/cv/",
            "primary_email": "mdnajmussakib2003@gmail.com",
            "secondary_email": "md.najmus.sakib.rahatul.2005@gmail.com",
            "github_url": "https://github.com/Sakib20050413",
            "linkedin_url": "https://www.linkedin.com/in/md-najmus-sakib-rahatul-559a85285/",
            "kaggle_url": "https://www.kaggle.com/sakib20050413",
            "twitter_url": "https://x.com/Rahatul2005",
            "seo_title": "Md Najmus Sakib Rahatul — AI Engineer & Full-Stack Developer",
            "seo_description": "Personal portfolio of Md Najmus Sakib Rahatul: Aspiring AI Engineer, Full-Stack Developer, and Edge TinyML researcher.",
            "theme_toggle_enabled": True,
            "show_exploring_section": True,
            "exploring_title": "Currently Exploring",
            "exploring_text": (
                "Investigating modular local AI inference architectures where a lightweight dispatcher "
                "dynamically coordinates sub-1GB quantized models across CPU and GPU memory pools to handle "
                "specialized coding and retrieval tasks without external cloud dependencies."
            ),
        }
    )

    # 2. About
    about_obj, _ = About.objects.get_or_create(
        id=1,
        defaults={
            "headline": "Engineering Practical Systems Across Web & Edge AI",
            "bio_paragraph_1": (
                "I am a 3rd-year Computer Science & Engineering student at Bangladesh Army International "
                "University of Science and Technology (BAIUST), Cumilla. I build full-stack web applications "
                "with Python/Django and Next.js, and conduct applied research on real-time embedded signal processing and local AI systems."
            ),
            "bio_paragraph_2": (
                "My current focus centers on applied AI engineering: integrating large language models, "
                "multimodal pipelines, and on-device quantization (4-bit NF4/GGUF) into accessible, production-ready platforms."
            ),
            "education": "B.Sc. in CSE, BAIUST, Cumilla (Level 3, Term 2)",
            "location": "Cumilla / Dhaka, Bangladesh (UTC+6)",
            "availability": "Open to AI/ML engineering internships, remote developer contracts & research",
        }
    )

    # 3. Skills (5 Groups, max 6 items each, honest levels)
    Skill.objects.all().delete()
    SkillGroup.objects.all().delete()

    skill_groups_data = [
        (
            "Core Languages",
            1,
            [
                ("Python", "Proficient", 1),
                ("JavaScript (ES6+)", "Proficient", 2),
                ("C / C++", "Used in projects", 3),
                ("HTML5 & Semantic Web", "Proficient", 4),
                ("CSS3 & Tailwind", "Proficient", 5),
                ("SQL", "Used in projects", 6),
            ]
        ),
        (
            "Web Frameworks & Backend",
            2,
            [
                ("Django 5", "Proficient", 1),
                ("FastAPI", "Used in projects", 2),
                ("Next.js", "Used in projects", 3),
                ("RESTful API Design", "Proficient", 4),
                ("Gunicorn & WhiteNoise", "Used in projects", 5),
            ]
        ),
        (
            "Databases & DevOps",
            3,
            [
                ("PostgreSQL", "Proficient", 1),
                ("SQLite", "Proficient", 2),
                ("Git & GitHub", "Proficient", 3),
                ("Linux & Shell", "Used in projects", 4),
                ("Docker", "Used in projects", 5),
            ]
        ),
        (
            "AI/ML & Applied Machine Learning",
            4,
            [
                ("PyTorch", "Used in projects", 1),
                ("Hugging Face Transformers", "Used in projects", 2),
                ("4-Bit Quantization (NF4/GGUF)", "Used in projects", 3),
                ("vLLM & Local Runtimes", "Learning", 4),
                ("Vector Search & RAG", "Used in projects", 5),
            ]
        ),
        (
            "Embedded Systems & TinyML",
            5,
            [
                ("ESP32-S3 Hardware", "Used in projects", 1),
                ("Digital Signal Processing (DSP)", "Used in projects", 2),
                ("Sensor Fusion", "Used in projects", 3),
                ("Edge TinyML", "Used in projects", 4),
            ]
        ),
    ]

    for group_name, group_order, skills_list in skill_groups_data:
        grp = SkillGroup.objects.create(name=group_name, order=group_order, visible=True)
        for skill_name, level_lbl, skill_order in skills_list:
            Skill.objects.create(
                group=grp,
                name=skill_name,
                level_label=level_lbl,
                order=skill_order,
                visible=True
            )

    # 4. Projects (8 real projects from GitHub)
    Project.objects.all().delete()
    projects_data = [
        {
            "title": "BAIUST Campus Lost & Found",
            "slug": "campus-lost-and-found",
            "category": "WEB",
            "summary": "Disorganized social media groups cause lost campus items to go unclaimed across 14 university zones.",
            "description": (
                "Engineered a centralized recovery platform with student ID authentication and a custom 4-factor "
                "weighted matching algorithm (location, category, date proximity, and keyword similarity) that automatically "
                "matches lost items with found claims."
            ),
            "tech_stack_csv": "Python, Django 5, Bootstrap 5, PostgreSQL, WhiteNoise, JavaScript",
            "repo_url": "https://github.com/Sakib20050413/campus_lostfound",
            "live_url": "https://baiust-campus-lost-and-found.vercel.app/",
            "status": "Completed",
            "order": 1,
            "featured": True,
            "upvotes": 68,
        },
        {
            "title": "Bio-Acoustic Mosquito Vector Trap",
            "slug": "bio-acoustic-mosquito-trap",
            "category": "EMBEDDED",
            "summary": "Chemical insecticides harm non-target pollinator species and foster environmental toxicity.",
            "description": (
                "Designed an eco-friendly acoustic vector trap running a 512-point Hann-windowed Radix-2 FFT on "
                "ESP32-S3 hardware to isolate female mosquito wingbeats (350–600 Hz) in 32 ms and selectively activate "
                "a PWM suction fan while sparing non-biting insects."
            ),
            "tech_stack_csv": "ESP32-S3, C++, I2S Digital Mic, Radix-2 FFT, PWM Control, TinyML",
            "repo_url": "https://github.com/Sakib20050413/Bio-Acoustic-Mosquito-Vector-Trap",
            "live_url": "",
            "status": "Research",
            "order": 2,
            "featured": True,
            "upvotes": 54,
        },
        {
            "title": "IoT Rural Lightning Early Warning System",
            "slug": "iot-rural-lightning-early-warning",
            "category": "EMBEDDED",
            "summary": "Sudden lightning strikes cause high agricultural casualties in rural Bangladesh due to lack of localized alerts.",
            "description": (
                "Constructed a solar-powered telemetry station fusing AS3935 RF electromagnetic waveform sensing (1–40 km), "
                "optical drop, barometric pressure shifts, and offline SIM800L GSM SMS broadcasts to deliver real-time warnings to farmers."
            ),
            "tech_stack_csv": "ESP32-S3, AS3935 RF, SIM800L GSM, Web GIS, C++, Sensors",
            "repo_url": "https://github.com/Sakib20050413/IoT-Rural-Lightning-Early-Warning-System",
            "live_url": "",
            "status": "Completed",
            "order": 3,
            "featured": True,
            "upvotes": 49,
        },
        {
            "title": "Aloron Shop — E-Commerce Platform",
            "slug": "aloron-shop",
            "category": "WEB",
            "summary": "Traditional storefronts suffer from sluggish client navigation and poor mobile checkout UX.",
            "description": (
                "Developed a responsive full-stack e-commerce storefront featuring instant multi-category filtering, "
                "persistent cart state management, and optimized mobile-first checkout flows."
            ),
            "tech_stack_csv": "Next.js, TypeScript, Tailwind CSS, React Hooks, REST API",
            "repo_url": "https://github.com/Sakib20050413/aloron-shop",
            "live_url": "https://aloron-shop.vercel.app/",
            "status": "Completed",
            "order": 4,
            "featured": True,
            "upvotes": 43,
        },
        {
            "title": "CodeQuest BD / Polyglot 3D Learning Platform",
            "slug": "codequest-bd",
            "category": "WEB",
            "summary": "Beginners struggle with abstract programming concepts when learning through text documentation alone.",
            "description": (
                "Built an interactive gamified coding environment where students execute C, Python, and JavaScript snippets "
                "in a cloud compiler sandbox and visualize code execution flow through interactive canvas and 3D visual rovers."
            ),
            "tech_stack_csv": "Django 5, Vanilla JS DOM, Three.js, Tailwind CSS, Piston API",
            "repo_url": "https://github.com/Sakib20050413/codequest-bd",
            "live_url": "https://codequest-bd.vercel.app/",
            "status": "Completed",
            "order": 5,
            "featured": True,
            "upvotes": 61,
        },
        {
            "title": "CoWork API — Multi-Tenant Booking Backend",
            "slug": "cowork-api",
            "category": "WEB",
            "summary": "Shared office spaces suffer from double-booking conflicts and cross-tenant data leaks.",
            "description": (
                "Authored a containerized FastAPI service featuring strict multi-tenant organization isolation, "
                "role-based access control, JWT HS256 access/refresh token rotation, and automated booking collision checks."
            ),
            "tech_stack_csv": "Python 3.11, FastAPI, SQLAlchemy, PostgreSQL, Docker, Pytest",
            "repo_url": "https://github.com/Sakib20050413/ICT_Fest_Hackathon_Preliminary",
            "live_url": "",
            "status": "Completed",
            "order": 6,
            "featured": False,
            "upvotes": 38,
        },
        {
            "title": "SmartSpend — Personal Expense & Budget Analytics",
            "slug": "smartspend",
            "category": "WEB",
            "summary": "Personal finance management across fragmented channels lacks actionable spending insights.",
            "description": (
                "Implemented a full-stack financial tracker allowing users to log daily expenses, define monthly category "
                "spending limits, and analyze financial habits through interactive Chart.js visualizations."
            ),
            "tech_stack_csv": "Python, Django, SQLite, PostgreSQL, Chart.js, Bootstrap 5",
            "repo_url": "https://github.com/Sakib20050413/smartspend_core",
            "live_url": "",
            "status": "Completed",
            "order": 7,
            "featured": False,
            "upvotes": 35,
        },
        {
            "title": "Library Management System",
            "slug": "library-management-system",
            "category": "WEB",
            "summary": "Manual book ledgers lead to record loss, late returns, and slow catalog search.",
            "description": (
                "Created a relational database-backed library management platform with book inventory catalogs, "
                "borrower tracking, automated overdue fine calculators, and fast search indexing."
            ),
            "tech_stack_csv": "Python, Django, Relational DB, HTML5, CSS3, Git",
            "repo_url": "https://github.com/Sakib20050413/library_management_system",
            "live_url": "",
            "status": "Completed",
            "order": 8,
            "featured": False,
            "upvotes": 31,
        },
    ]

    for p in projects_data:
        Project.objects.create(
            title=p["title"],
            slug=p["slug"],
            category=p["category"],
            summary=p["summary"],
            description=p["description"],
            tech_stack_csv=p["tech_stack_csv"],
            repo_url=p["repo_url"],
            live_url=p["live_url"],
            status=p["status"],
            order=p["order"],
            featured=p["featured"],
            visible=True,
            upvotes=p["upvotes"],
        )

    # 5. Experience Timeline
    Experience.objects.all().delete()
    exp_data = [
        (
            "Team Leader (Team 03) — Django Internship Program",
            "BAIUST Computer Club (10th Panel)",
            "May 2026 – Present",
            "Leading a 3-member engineering team developing production-grade Django web applications with custom auth, relational modeling, and cloud deployments.",
            "Lead Developer",
            1
        ),
        (
            "Team Leader — Team BlackBerry (IoT & TinyML Group)",
            "Dept. of CSE, BAIUST",
            "2026 – Present",
            "Directing undergraduate hardware-software research in CSE 301 and CSE 326 focused on 512-point FFT acoustic insect identification and RF lightning warning nodes.",
            "Hardware Lead",
            2
        ),
        (
            "Internshala Student Partner (ISP) & Shortlisted Remote AI Candidate",
            "Internshala & Handshake",
            "2026 – Present",
            "Selected for campus outreach leadership and shortlisted for remote freelance technical data and video annotation specialist opportunities.",
            "Campus Partner",
            3
        ),
        (
            "B.Sc. in Computer Science & Engineering (CSE)",
            "BAIUST, Cumilla (Level 3, Term 2)",
            "Class of 2027",
            "Core coursework in Web Technologies (CSE 323/324), Microprocessors & Embedded Systems (CSE 326), Database Management Systems, Data Structures & Algorithms.",
            "ID: 1119003",
            4
        ),
    ]
    for role, org, period, desc, badge, ord_num in exp_data:
        Experience.objects.create(
            role_title=role,
            organization=org,
            period=period,
            description=desc,
            badge_metric=badge,
            order=ord_num,
            visible=True
        )

    # 6. Certificates
    Certificate.objects.all().delete()
    certs_data = [
        (
            "Cisco Networking Academy — Python Programming",
            "Cisco NetAcad",
            "2025",
            "https://www.credly.com/",
            1
        ),
        (
            "Kaggle — Intro to Machine Learning & Python",
            "Kaggle",
            "2025",
            "https://www.kaggle.com/sakib20050413",
            2
        ),
        (
            "Internshala Student Partner Leadership Certificate",
            "Internshala",
            "2026",
            "https://internshala.com/",
            3
        ),
    ]
    for t, iss, dt, url, ord_num in certs_data:
        Certificate.objects.create(
            title=t,
            issuer=iss,
            issue_date=dt,
            credential_url=url,
            order=ord_num,
            visible=True
        )


class Command(BaseCommand):
    help = "Seeds canonical verified portfolio content from CONTENT.md"

    def handle(self, *args, **options):
        run_canonical_seed()
        self.stdout.write(self.style.SUCCESS("Canonical portfolio content seeded successfully!"))
