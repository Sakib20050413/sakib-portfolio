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
            "site_name": "Sakib // Engineering & Systems",
            "full_name": "Md Najmus Sakib Rahatul",
            "role_title": "Aspiring AI Engineer · Full-Stack Developer",
            "tagline": "Building dependable web platforms, applied AI systems, and embedded signal processing hardware.",
            "hero_photo_url": "https://avatars.githubusercontent.com/u/166808901?v=4",
            "resume_url": "/cv/",
            "primary_email": "mdnajmussakib2003@gmail.com",
            "secondary_email": "md.najmus.sakib.rahatul.2005@gmail.com",
            "github_url": "https://github.com/Sakib20050413",
            "linkedin_url": "https://www.linkedin.com/in/md-najmus-sakib-rahatul-559a85285/",
            "kaggle_url": "https://www.kaggle.com/sakib20050413",
            "twitter_url": "https://x.com/Rahatul2005",
            "seo_title": "Md Najmus Sakib Rahatul — Engineering Portfolio & Applied AI",
            "seo_description": "Personal engineering portfolio of Md Najmus Sakib Rahatul: Aspiring AI Engineer, Full-Stack Developer, and Embedded Systems researcher at BAIUST.",
            "theme_toggle_enabled": True,
            "show_exploring_section": True,
            "exploring_title": "Applied Research & Exploration",
            "exploring_text": (
                "Investigating modular local AI inference architectures where a persistent dispatcher "
                "dynamically coordinates sub-1GB quantized models across CPU and GPU memory pools to handle "
                "specialized coding and retrieval tasks without external cloud dependencies."
            ),
        }
    )

    # 2. About Section
    about_obj, _ = About.objects.get_or_create(
        id=1,
        defaults={
            "headline": "Engineering Practical Software, AI Systems & Embedded Hardware",
            "bio_paragraph_1": (
                "I am a 3rd-year Computer Science & Engineering student at Bangladesh Army International "
                "University of Science and Technology (BAIUST), Cumilla. My technical work spans full-stack "
                "web development with Python/Django and Next.js, alongside applied research in embedded systems, "
                "digital signal processing, and real-time sensor telemetry."
            ),
            "bio_paragraph_2": (
                "I focus on solving real operational problems through clean software architecture: "
                "automating campus recovery systems, building high-throughput REST APIs, and designing "
                "edge-AI hardware on ESP32-S3. I believe in writing well-tested, maintainable code backed by evidence."
            ),
            "education": "B.Sc. in Computer Science & Engineering, BAIUST, Cumilla (Level 3, Term 2)",
            "location": "Cumilla / Dhaka, Bangladesh (UTC+6)",
            "availability": "Open to AI/ML engineering internships, full-stack roles & technical collaborations",
        }
    )

    # 3. Technical Skills (6 Clear Categories from Section 6)
    Skill.objects.all().delete()
    SkillGroup.objects.all().delete()

    skill_groups_data = [
        (
            "Programming Languages",
            1,
            [
                ("Python", "Proficient", 1),
                ("JavaScript (ES6+)", "Proficient", 2),
                ("C / C++", "Used in projects", 3),
                ("HTML5 & Semantic Markup", "Proficient", 4),
                ("CSS3 & Tailwind CSS", "Proficient", 5),
                ("SQL", "Used in projects", 6),
            ]
        ),
        (
            "Full-Stack and Backend Development",
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
            "Databases and Infrastructure",
            3,
            [
                ("PostgreSQL", "Proficient", 1),
                ("SQLite", "Proficient", 2),
                ("Git & GitHub", "Proficient", 3),
                ("Linux & Shell Scripting", "Used in projects", 4),
                ("Docker", "Used in projects", 5),
            ]
        ),
        (
            "AI/ML and Applied Research",
            4,
            [
                ("PyTorch", "Used in projects", 1),
                ("Hugging Face Transformers", "Used in projects", 2),
                ("4-Bit Quantization (NF4/GGUF)", "Used in projects", 3),
                ("vLLM & Local Inference", "Learning", 4),
                ("Vector Search & RAG", "Used in projects", 5),
            ]
        ),
        (
            "Embedded Systems and Edge AI",
            5,
            [
                ("ESP32-S3 Architecture", "Used in projects", 1),
                ("Digital Signal Processing (DSP)", "Used in projects", 2),
                ("Sensor Fusion & Telemetry", "Used in projects", 3),
                ("Edge TinyML", "Used in projects", 4),
            ]
        ),
        (
            "Developer Tools",
            6,
            [
                ("VS Code", "Proficient", 1),
                ("Chrome DevTools", "Proficient", 2),
                ("Postman API Testing", "Used in projects", 3),
                ("Figma Interface Design", "Used in projects", 4),
                ("Vite Build Tooling", "Used in projects", 5),
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

    # 4. Featured Projects & Deep Case Studies (8 Real Projects from GitHub)
    Project.objects.all().delete()
    projects_data = [
        {
            "title": "BAIUST Campus Lost & Found",
            "slug": "campus-lost-and-found",
            "category": "WEB",
            "summary": "Disorganized social media posts cause lost campus items to go unclaimed across 14 university zones.",
            "description": (
                "Problem & Motivation:\n"
                "Students and faculty across 14 BAIUST campus zones previously relied on fragmented social media groups to locate lost items, causing high abandonment rates and lack of ownership verification.\n\n"
                "Architecture & Implementation:\n"
                "Engineered a production Django 5 platform with BAIUST student/faculty ID authentication and a custom 0–100% 4-factor matching algorithm: Category (30%), Location (25%), Keyword Similarity (30%), and Date Proximity within 14 days (15%). Implemented secret-mark and photo verification workflows to prevent fraudulent claims.\n\n"
                "Outcomes & Results:\n"
                "Deployed on Vercel with PostgreSQL backend and WhiteNoise static compression. Features zero layout shift (CLS = 0) and responsive mobile layouts."
            ),
            "tech_stack_csv": "Python, Django 5, PostgreSQL, Bootstrap 5, WhiteNoise, JavaScript",
            "repo_url": "https://github.com/Sakib20050413/campus_lostfound",
            "live_url": "https://baiust-campus-lost-and-found.vercel.app/",
            "status": "Completed",
            "order": 1,
            "featured": True,
            "upvotes": 72,
        },
        {
            "title": "Bio-Acoustic Mosquito Vector Trap",
            "slug": "bio-acoustic-mosquito-trap",
            "category": "EMBEDDED",
            "summary": "Broad-spectrum chemical insecticides destroy non-target pollinators and cause environmental toxicity.",
            "description": (
                "Problem & Motivation:\n"
                "Mosquito control in subtropical regions often relies on toxic sprays that destroy beneficial pollinators like honeybees. An acoustic, selective non-chemical trap was needed.\n\n"
                "Architecture & Implementation:\n"
                "Designed an embedded DSP node on the ESP32-S3 dual-core processor. Wingbeat audio is sampled at 16 kHz via I2S DMA and processed through a 512-point Hann-windowed Radix-2 FFT (31.25 Hz bin resolution) executing in 32 ms. Identifies female vector wingbeats (350–600 Hz fundamental) and selectively triggers a PWM suction fan while keeping it off for non-target frequencies.\n\n"
                "Current Status:\n"
                "Under active research in CSE 326 (Microprocessors & Embedded Systems Sessional) under faculty supervision."
            ),
            "tech_stack_csv": "ESP32-S3, C++, I2S Digital Mic, Radix-2 FFT, PWM Control, TinyML",
            "repo_url": "https://github.com/Sakib20050413/Bio-Acoustic-Mosquito-Vector-Trap",
            "live_url": "",
            "status": "Research",
            "order": 2,
            "featured": True,
            "upvotes": 58,
        },
        {
            "title": "IoT Rural Lightning Early Warning System",
            "slug": "iot-rural-lightning-early-warning",
            "category": "EMBEDDED",
            "summary": "Sudden severe lightning strikes cause tragic casualties among agricultural workers in open fields in rural Bangladesh.",
            "description": (
                "Problem & Motivation:\n"
                "Agricultural workers in rural Bangladesh frequently lack localized nowcasting alerts during pre-monsoon thunderstorms, leading to hundreds of fatalities annually.\n\n"
                "Architecture & Implementation:\n"
                "Constructed an autonomous telemetry node combining AS3935 RF electromagnetic waveform sensing (1–40 km detection range), barometric pressure drop monitoring (BMP280), optical darkening sensors (BH1750), and offline SIM800L GSM SMS broadcast to notify community field managers before strikes reach critical proximity.\n\n"
                "Outcomes & Results:\n"
                "Built and verified as an Interdisciplinary Design Project (CSE 301) with Leaflet Web GIS mapping and local Bangla voice siren triggers."
            ),
            "tech_stack_csv": "ESP32-S3, AS3935 RF Sensor, SIM800L GSM, Web GIS, C++, Sensors",
            "repo_url": "https://github.com/Sakib20050413/IoT-Rural-Lightning-Early-Warning-System",
            "live_url": "",
            "status": "Completed",
            "order": 3,
            "featured": True,
            "upvotes": 51,
        },
        {
            "title": "CodeQuest BD / Polyglot 3D Learning Platform",
            "slug": "codequest-bd",
            "category": "WEB",
            "summary": "Novice students struggle with syntax and logic flow when learning programming through abstract console logs alone.",
            "description": (
                "Problem & Motivation:\n"
                "Early computer science students often hit motivational walls when syntax errors lack immediate visual context.\n\n"
                "Architecture & Implementation:\n"
                "Built an interactive gamified coding environment where learners execute C, Python, and JavaScript snippets in a cloud compiler sandbox (Piston API) and visualize program state and data structures through interactive HTML5 canvas rovers and 3D scenes.\n\n"
                "Outcomes & Results:\n"
                "Deployed on Vercel with responsive mobile-friendly UI, interactive DOM quizzes, and progress persistence."
            ),
            "tech_stack_csv": "Django 5, Vanilla JS DOM, Three.js, Tailwind CSS, Piston API",
            "repo_url": "https://github.com/Sakib20050413/codequest-bd",
            "live_url": "https://codequest-bd.vercel.app/",
            "status": "Completed",
            "order": 4,
            "featured": True,
            "upvotes": 65,
        },
        {
            "title": "Aloron Shop — Modern E-Commerce Platform",
            "slug": "aloron-shop",
            "category": "WEB",
            "summary": "Traditional online stores suffer from full-page reloads and sluggish checkout flows on low-bandwidth connections.",
            "description": (
                "Problem & Motivation:\n"
                "Creating a snappy e-commerce shopping experience requires minimizing layout shifts and optimizing mobile network waterfalls.\n\n"
                "Architecture & Implementation:\n"
                "Engineered a responsive storefront with Next.js and TypeScript. Implemented client-side category filtering, instant query search, persistent localStorage cart state, and accessible checkout forms styled with Tailwind CSS.\n\n"
                "Outcomes & Results:\n"
                "Deployed on Vercel with sub-second page transitions and clean mobile navigation."
            ),
            "tech_stack_csv": "Next.js, TypeScript, Tailwind CSS, React Hooks, REST API",
            "repo_url": "https://github.com/Sakib20050413/aloron-shop",
            "live_url": "https://aloron-shop.vercel.app/",
            "status": "Completed",
            "order": 5,
            "featured": False,
            "upvotes": 45,
        },
        {
            "title": "CoWork API — Multi-Tenant Booking Backend",
            "slug": "cowork-api",
            "category": "WEB",
            "summary": "Shared office spaces suffer from double-booking conflicts and cross-tenant data leaks.",
            "description": (
                "Problem & Motivation:\n"
                "Designed for the ICT Fest Hackathon Preliminary. Managing shared meeting rooms across organizations requires strict tenant data isolation and atomic booking verification.\n\n"
                "Architecture & Implementation:\n"
                "Authored a containerized FastAPI service featuring strict multi-tenant organization isolation, role-based access control (Admin, Staff, Member), JWT HS256 access and refresh token rotation, and collision-free slot reservation logic.\n\n"
                "Outcomes & Results:\n"
                "Fully containerized with production Dockerfile and docker-compose.yml with automated Pytest suites."
            ),
            "tech_stack_csv": "Python 3.11, FastAPI, SQLAlchemy, PostgreSQL, Docker, Pytest",
            "repo_url": "https://github.com/Sakib20050413/ICT_Fest_Hackathon_Preliminary",
            "live_url": "",
            "status": "Completed",
            "order": 6,
            "featured": False,
            "upvotes": 40,
        },
        {
            "title": "SmartSpend — Personal Expense & Budget Analytics",
            "slug": "smartspend",
            "category": "WEB",
            "summary": "Tracking personal finances across multiple payment channels lacks actionable spending categorization.",
            "description": (
                "Problem & Motivation:\n"
                "University students struggle to track monthly budgets and recurrent expenses without clear visualization of cash flow.\n\n"
                "Architecture & Implementation:\n"
                "Implemented a full-stack Django financial tracking application allowing users to log expenses, define category spending ceilings, and inspect spending distribution through interactive Chart.js visualizations.\n\n"
                "Outcomes & Results:\n"
                "Relational schema with SQLite and PostgreSQL compatibility, clean Bootstrap UI, and monthly export reports."
            ),
            "tech_stack_csv": "Python, Django, SQLite, PostgreSQL, Chart.js, Bootstrap 5",
            "repo_url": "https://github.com/Sakib20050413/smartspend_core",
            "live_url": "",
            "status": "Completed",
            "order": 7,
            "featured": False,
            "upvotes": 36,
        },
        {
            "title": "Library Management System",
            "slug": "library-management-system",
            "category": "WEB",
            "summary": "Manual book circulation logs result in record loss, overdue book errors, and slow catalog lookups.",
            "description": (
                "Problem & Motivation:\n"
                "Departmental libraries require reliable inventory records, member circulation tracking, and automated fine calculations.\n\n"
                "Architecture & Implementation:\n"
                "Created a database-backed circulation platform with book cataloging, borrower limits, automated fine calculators based on return dates, and quick search indexing.\n\n"
                "Outcomes & Results:\n"
                "Built with Django ORM, role-based checkout workflows, and responsive templates."
            ),
            "tech_stack_csv": "Python, Django, Relational DB, HTML5, CSS3, Git",
            "repo_url": "https://github.com/Sakib20050413/library_management_system",
            "live_url": "",
            "status": "Completed",
            "order": 8,
            "featured": False,
            "upvotes": 33,
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
            "Leading a 3-member developer team building production-grade Django web applications with custom auth, relational modeling, and cloud deployments.",
            "Lead Developer",
            1
        ),
        (
            "Team Leader — Team BlackBerry (IoT & Embedded TinyML Group)",
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

    # 6. Certifications
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
