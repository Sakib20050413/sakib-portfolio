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
    """Seeds the database with Sakib's canonical, 100% verified, comprehensive portfolio content."""
    # 1. Site Settings
    settings_obj, _ = SiteSettings.objects.get_or_create(
        id=1,
        defaults={
            "site_name": "Sakib // Engineering, Systems & AI",
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

    # 3. Technical Skills (Comprehensive Inventory Across 8 Explicit Categories)
    Skill.objects.all().delete()
    SkillGroup.objects.all().delete()

    skill_groups_data = [
        (
            "Programming Languages",
            1,
            [
                ("Python", "Proficient", 1),
                ("JavaScript (ES6+)", "Proficient", 2),
                ("TypeScript", "Used in projects", 3),
                ("C / C++", "Used in projects", 4),
                ("HTML5 & Semantic Web", "Proficient", 5),
                ("CSS3 & Modern Layouts", "Proficient", 6),
                ("SQL", "Used in projects", 7),
                ("PHP", "Used in projects", 8),
            ]
        ),
        (
            "Full-Stack & Backend Frameworks",
            2,
            [
                ("Django 5", "Proficient", 1),
                ("FastAPI", "Used in projects", 2),
                ("Next.js (App Router)", "Used in projects", 3),
                ("React & Hooks", "Used in projects", 4),
                ("Tailwind CSS", "Proficient", 5),
                ("Bootstrap 5", "Proficient", 6),
                ("RESTful API Architecture", "Proficient", 7),
                ("Gunicorn & WhiteNoise", "Used in projects", 8),
            ]
        ),
        (
            "Databases & Cloud Storage",
            3,
            [
                ("PostgreSQL", "Proficient", 1),
                ("SQLite", "Proficient", 2),
                ("MySQL", "Used in projects", 3),
                ("Supabase / Cloud DB", "Used in projects", 4),
                ("Cloudinary Media CDN", "Used in projects", 5),
                ("Database Migrations & Indexing", "Proficient", 6),
            ]
        ),
        (
            "DevOps, Infrastructure & Hosting",
            4,
            [
                ("Git & GitHub Workflow", "Proficient", 1),
                ("Docker & Containers", "Used in projects", 2),
                ("Linux & Bash Scripting", "Used in projects", 3),
                ("Render Web Services", "Proficient", 4),
                ("Vercel Cloud Deployments", "Proficient", 5),
                ("Environment & Secret Security", "Proficient", 6),
            ]
        ),
        (
            "AI, Machine Learning & LLMs",
            5,
            [
                ("PyTorch Fundamentals", "Used in projects", 1),
                ("Hugging Face Transformers", "Used in projects", 2),
                ("4-Bit Quantization (GGUF / NF4)", "Used in projects", 3),
                ("Vector Search & RAG Architecture", "Used in projects", 4),
                ("vLLM & Local Inference", "Learning", 5),
                ("Data Analysis (NumPy, Pandas)", "Used in projects", 6),
            ]
        ),
        (
            "Embedded Systems & Edge AI",
            6,
            [
                ("ESP32-S3 Dual-Core Architecture", "Used in projects", 1),
                ("Digital Signal Processing (Radix-2 FFT)", "Used in projects", 2),
                ("I2S DMA Audio Streaming", "Used in projects", 3),
                ("Sensor Fusion & Filtering", "Used in projects", 4),
                ("Edge TinyML Pipelines", "Used in projects", 5),
                ("PWM Actuator Control", "Used in projects", 6),
            ]
        ),
        (
            "Telemetry & Hardware Protocols",
            7,
            [
                ("AS3935 RF Lightning Detection", "Used in projects", 1),
                ("SIM800L GSM Telemetry", "Used in projects", 2),
                ("I2C, SPI & UART Protocols", "Used in projects", 3),
                ("INMP441 MEMS Microphone", "Used in projects", 4),
                ("BMP280 Barometric Pressure", "Used in projects", 5),
                ("Solar & Battery Power Budgeting", "Used in projects", 6),
            ]
        ),
        (
            "Developer Tools & Quality Engineering",
            8,
            [
                ("VS Code Advanced Setup", "Proficient", 1),
                ("Chrome DevTools Performance", "Proficient", 2),
                ("Postman API Testing", "Used in projects", 3),
                ("Figma UI/UX Prototyping", "Used in projects", 4),
                ("Vite Build Tooling", "Used in projects", 5),
                ("Pytest & Unit Testing", "Used in projects", 6),
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

    # 4. Featured Projects & Deep Case Studies (8 Real Projects from GitHub: Sakib20050413)
    Project.objects.all().delete()
    projects_data = [
        {
            "title": "BAIUST Campus Lost & Found",
            "slug": "campus-lost-and-found",
            "category": "WEB",
            "summary": "Centralized recovery portal with student verification and a 4-factor matching algorithm across 14 campus zones.",
            "description": (
                "Problem & Motivation:\n"
                "Unorganized social media posts across unofficial student groups frequently caused lost belongings "
                "(ID cards, lab notebooks, electronics, calculators) to go unclaimed across 14 university zones.\n\n"
                "Architecture & Implementation:\n"
                "Engineered a centralized Django 5 portal featuring institutional student authentication, structured claim "
                "management, and an automated 4-factor heuristic matching engine (location, item category, date proximity, "
                "and keyword cosine overlap) that calculates a 0–100% similarity score to pair lost posts with found items.\n\n"
                "Verified Capabilities:\n"
                "Role-based moderation, secure photo verification, privacy-preserving claim handoff workflows, "
                "and production deployment with zero downtime."
            ),
            "tech_stack_csv": "Python, Django 5, PostgreSQL, Bootstrap 5, WhiteNoise, JavaScript",
            "repo_url": "https://github.com/Sakib20050413/baiust-campus-lost-and-found",
            "live_url": "https://baiust-campus-lost-and-found.vercel.app/",
            "order": 1,
            "featured": True,
            "status": "Completed",
            "upvotes": 42,
        },
        {
            "title": "Bio-Acoustic Mosquito Vector Trap",
            "slug": "bio-acoustic-mosquito-trap",
            "category": "EMBEDDED",
            "summary": "Autonomous hardware trap executing 512-point Hann-windowed Radix-2 FFT on ESP32-S3 to isolate mosquito wingbeats in 32ms.",
            "description": (
                "Problem & Motivation:\n"
                "Broad-spectrum chemical pesticides destroy critical non-target pollinators, trigger insecticide "
                "resistance, and cause chemical toxicity in agricultural and residential habitats.\n\n"
                "Architecture & Implementation:\n"
                "Architected a target-selective bio-acoustic smart trap utilizing an INMP441 I2S digital microphone connected "
                "via DMA directly into an ESP32-S3 dual-core microcontroller. Implemented a 512-point Hann-windowed Radix-2 "
                "Fast Fourier Transform (FFT) in C++ to isolate fundamental female mosquito wingbeat acoustic frequencies "
                "(350–600 Hz) within a 32ms detection window.\n\n"
                "Engineering Decisions & Hardware Constraints:\n"
                "Employed dual-core task affinity: Core 0 dedicated exclusively to continuous I2S DMA audio capture and FFT "
                "computation, while Core 1 handles optical beam break validation, threshold confirmation, and PWM fan actuation "
                "to minimize overall system power consumption."
            ),
            "tech_stack_csv": "ESP32-S3, C++, I2S DMA, 512-Pt FFT, PWM Control, TinyML, INMP441",
            "repo_url": "https://github.com/Sakib20050413/Bio-Acoustic-Mosquito-AI-Trap",
            "live_url": "",
            "order": 2,
            "featured": True,
            "status": "Research",
            "upvotes": 58,
        },
        {
            "title": "IoT Rural Lightning Early Warning System",
            "slug": "iot-rural-lightning-early-warning",
            "category": "EMBEDDED",
            "summary": "Solar telemetry station fusing AS3935 RF lightning detection with SIM800L GSM SMS broadcasts for rural safety.",
            "description": (
                "Problem & Motivation:\n"
                "Severe lightning strikes in open agricultural fields cause tragic loss of life among Bangladeshi farmers "
                "who lack access to real-time localized storm warnings.\n\n"
                "Architecture & Implementation:\n"
                "Built an off-grid solar-powered telemetry station utilizing an ESP32-S3 paired with an AMS AS3935 Franklin "
                "lightning sensor to detect electromagnetic radiation from cloud-to-ground strikes within a 1–40 km radius. "
                "Fuses RF readings with sudden barometric pressure drops from a BMP280 sensor to filter false positives.\n\n"
                "Communication & Deployment:\n"
                "Integrated a SIM800L GSM modem to broadcast immediate SMS alerts and automated buzzer sirens to agricultural "
                "community leaders before storms arrive overhead."
            ),
            "tech_stack_csv": "ESP32-S3, AS3935 RF, SIM800L GSM, BMP280, C++, Solar Telemetry",
            "repo_url": "https://github.com/Sakib20050413/IoT-Rural-Lightning-Early-Warning-System",
            "live_url": "",
            "order": 3,
            "featured": True,
            "status": "Completed",
            "upvotes": 36,
        },
        {
            "title": "CodeQuest BD / Polyglot 3D Learning Platform",
            "slug": "codequest-bd",
            "category": "WEB",
            "summary": "Interactive programming education platform combining cloud compiler execution with Three.js 3D logic rover visualizers.",
            "description": (
                "Problem & Motivation:\n"
                "Novice computer science students struggle with abstract syntax and control flow when guided solely "
                "by plain command-line console logs.\n\n"
                "Architecture & Implementation:\n"
                "Engineered a gamified educational platform where learners run multi-language code (Python, C, JavaScript) "
                "in a secured sandbox using the Piston Execution API. Visualized code logic and variable changes through "
                "interactive DOM widgets and an integrated Three.js 3D rover that navigates algorithm mazes based on student code."
            ),
            "tech_stack_csv": "Django 5, Vanilla JS, Three.js, Tailwind CSS, Piston API, Canvas",
            "repo_url": "https://github.com/Sakib20050413/codequest-bd",
            "live_url": "https://codequest-bd.vercel.app/",
            "order": 4,
            "featured": True,
            "status": "Completed",
            "upvotes": 29,
        },
        {
            "title": "Aloron Shop — E-Commerce Web Application",
            "slug": "aloron-shop",
            "category": "WEB",
            "summary": "Modern e-commerce storefront with instantaneous client-side category filtering and persistent checkout state.",
            "description": (
                "Problem & Motivation:\n"
                "Traditional online retail experiences in developing markets often suffer from slow full-page reloads and "
                "clunky mobile cart updates on unreliable connections.\n\n"
                "Architecture & Implementation:\n"
                "Constructed a high-speed e-commerce storefront leveraging Next.js, TypeScript, and Tailwind CSS. Features "
                "instantaneous client-side filtering, keyword debouncing, persistent cart synchronization via localStorage, "
                "and an accessible, mobile-first responsive checkout flow."
            ),
            "tech_stack_csv": "Next.js, TypeScript, Tailwind CSS, React, REST API, LocalStorage",
            "repo_url": "https://github.com/Sakib20050413/aloron-shop",
            "live_url": "https://aloron-shop.vercel.app/",
            "order": 5,
            "featured": False,
            "status": "Completed",
            "upvotes": 21,
        },
        {
            "title": "CoWork API — Multi-Tenant Booking Engine",
            "slug": "cowork-api",
            "category": "WEB",
            "summary": "Containerized FastAPI microservice with strict tenant isolation, JWT authentication, and conflict-free room reservations.",
            "description": (
                "Problem & Motivation:\n"
                "Shared office spaces encounter double-booking conflicts and security hazards when customer tenant data is "
                "not rigorously segregated.\n\n"
                "Architecture & Implementation:\n"
                "Designed and containerized a high-performance RESTful API using FastAPI, SQLAlchemy ORM, and PostgreSQL. "
                "Enforces strict multi-tenant database scoping, role-based access control (RBAC), and JWT token refresh rotation "
                "with automated pytest test coverage."
            ),
            "tech_stack_csv": "Python 3.11, FastAPI, SQLAlchemy, PostgreSQL, Docker, Pytest, JWT",
            "repo_url": "https://github.com/Sakib20050413/ICT_Fest_Hackathon_Preliminary",
            "live_url": "",
            "order": 6,
            "featured": False,
            "status": "Completed",
            "upvotes": 19,
        },
        {
            "title": "SmartSpend — Personal Expense & Budget Analytics",
            "slug": "smartspend",
            "category": "WEB",
            "summary": "Financial tracking engine with category budgeting and responsive Chart.js visual distribution analytics.",
            "description": (
                "Problem & Motivation:\n"
                "Personal financial tracking is prone to abandonment when expense categorization requires laborious manual inputs.\n\n"
                "Architecture & Implementation:\n"
                "Developed a Django web utility that enables users to record transactions, set monthly threshold ceilings per category, "
                "and evaluate spending distributions through dynamic Chart.js visualizations and automated balance updates."
            ),
            "tech_stack_csv": "Python, Django, Chart.js, SQLite, Bootstrap 5, Analytics",
            "repo_url": "https://github.com/Sakib20050413/smartspend_core",
            "live_url": "https://smartspendcore.vercel.app",
            "order": 7,
            "featured": False,
            "status": "Completed",
            "upvotes": 17,
        },
        {
            "title": "Library Management System",
            "slug": "library-management-system",
            "category": "WEB",
            "summary": "Comprehensive academic cataloging and circulation system handling member borrowing quotas and automated fines.",
            "description": (
                "Problem & Motivation:\n"
                "Paper and spreadsheet-based inventory logs frequently result in overdue book discrepancies and lost book catalogs.\n\n"
                "Architecture & Implementation:\n"
                "Constructed a structured cataloging system with Django, managing book inventories, member borrowing quotas, "
                "automated overdue fine computation, and responsive search indexing."
            ),
            "tech_stack_csv": "Python, Django, Relational DB, HTML5, CSS3, JavaScript",
            "repo_url": "https://github.com/Sakib20050413/Library-Management-System",
            "live_url": "",
            "order": 8,
            "featured": False,
            "status": "Completed",
            "upvotes": 15,
        },
    ]

    for p_data in projects_data:
        Project.objects.create(**p_data)

    # 5. Experience & Leadership Timeline
    Experience.objects.all().delete()
    experiences_data = [
        (
            "Team Leader (Team 03) — Django Internship Program",
            "BAIUST Computer Club (10th Panel)",
            "May 2026 – Present",
            (
                "Leading a 3-member development team architecting production-grade Django web applications. "
                "Directing relational database schema design, Git feature branch workflows, and deployment to cloud infrastructure."
            ),
            1
        ),
        (
            "Team Leader — Team BlackBerry (IoT & TinyML Research Group)",
            "Dept. of CSE, BAIUST",
            "2026 – Present",
            (
                "Spearheading undergraduate hardware-software research in CSE 301 and CSE 326. "
                "Focused on 512-point FFT acoustic insect vector identification and RF lightning early warning telemetry nodes."
            ),
            2
        ),
        (
            "Internshala Student Partner (ISP) & Shortlisted Remote AI Candidate",
            "Internshala & Handshake",
            "2026 – Present",
            (
                "Selected for university campus leadership outreach and shortlisted for remote freelance technical data and "
                "video annotation specialist opportunities."
            ),
            3
        ),
        (
            "B.Sc. in Computer Science & Engineering (CSE)",
            "BAIUST, Cumilla (Level 3, Term 2)",
            "2023 – 2027 (Expected)",
            (
                "Undergraduate studies with completed coursework in Web Technologies, Microprocessors, Database Management Systems, "
                "Data Structures, Algorithm Analysis, Operating Systems, and Object-Oriented Programming."
            ),
            4
        ),
    ]

    for role, org, period, desc, ord_num in experiences_data:
        Experience.objects.create(
            role_title=role,
            organization=org,
            period=period,
            description=desc,
            order=ord_num
        )

    # 6. Verified Certifications
    Certificate.objects.all().delete()
    certificates_data = [
        (
            "Introduction to Cybersecurity",
            "Cisco Networking Academy",
            "2026",
            "https://www.credly.com/",
            1
        ),
        (
            "Python Essentials & Advanced Scripting",
            "Cisco Networking Academy",
            "2026",
            "https://www.credly.com/",
            2
        ),
        (
            "Intro to Machine Learning",
            "Kaggle",
            "2026",
            "https://www.kaggle.com/sakib20050413",
            3
        ),
        (
            "Web Technology Theory & Project Certification",
            "Dept. of CSE, BAIUST",
            "2026",
            "https://github.com/Sakib20050413",
            4
        ),
    ]

    for title, issuer, issue_date, cred_url, ord_num in certificates_data:
        Certificate.objects.create(
            title=title,
            issuer=issuer,
            issue_date=issue_date,
            credential_url=cred_url,
            order=ord_num
        )


class Command(BaseCommand):
    help = "Seeds the database with Sakib's canonical, comprehensive portfolio content."

    def handle(self, *args, **options):
        run_canonical_seed()
        self.stdout.write(self.style.SUCCESS("Canonical portfolio content seeded successfully!"))
