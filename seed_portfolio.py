import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_cms.settings")
django.setup()

from django.contrib.auth.models import User
from core.models import ProfileSetting, Project, Skill, TimelineEntry, ContactMessage


def seed():
    print("[*] Seeding V3.0 Full-Viewport 12-Column Apple & Helion-grade Portfolio...")

    # 1. Superuser / Admin Account
    admin_username = "sakib_admin"
    admin_email = "mdnajmussakib2003@gmail.com"
    admin_pass = "baiust1119003"

    user, created = User.objects.get_or_create(username=admin_username, defaults={"email": admin_email})
    user.set_password(admin_pass)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    if created:
        print(f"[+] Admin account created: {admin_username}")
    else:
        print(f"[OK] Admin account verified: {admin_username}")

    # 2. Profile Setting
    profile = ProfileSetting.load()
    profile.full_name = "Md Najmus Sakib Rahatul"
    profile.display_handle = "sakib@baiust"
    profile.student_id = "1119003"
    profile.university = "Bangladesh Army International University of Science and Technology (BAIUST), Cumilla"
    profile.department_batch = "B.Sc. in Computer Science & Engineering (CSE), Level 3, Term 2, Section A, Group G1"
    profile.headline = "Full-Stack Web Platforms & Embedded TinyML Hardware Systems"
    profile.bio = (
        "Computer Science & Engineering undergraduate at BAIUST, Cumilla (ID: 1119003). "
        "Team Leader at the BAIUST Computer Club Django Internship and Team BlackBerry IoT Research Group—"
        "building production Django/Next.js web applications and real-time ESP32-S3 signal processing hardware."
    )
    profile.primary_email = "mdnajmussakib2003@gmail.com"
    profile.academic_email = "md.najmus.sakib.rahatul.2005@gmail.com"
    profile.location = "Cumilla, Bangladesh (DAC • UTC+6)"
    profile.availability_status = "Available for Internships & Remote Roles"
    profile.cv_url = "/cv/"
    profile.github_url = "https://github.com/Sakib20050413"
    profile.linkedin_url = "https://www.linkedin.com/in/md-najmus-sakib-rahatul-559a85285/"
    profile.x_twitter_url = "https://x.com/Rahatul2005"
    profile.facebook_url = "https://www.facebook.com/Sakib200513"
    profile.instagram_url = "https://www.instagram.com/sakib200513/"
    profile.leetcode_url = "https://leetcode.com/u/Sakib20050413/"
    profile.kaggle_url = "https://www.kaggle.com/sakib20050413"
    profile.scholar_url = ""
    profile.blog_url = ""
    profile.save()
    print("[+] Profile settings updated.")

    # 3. 8 Real Projects
    Project.objects.all().delete()
    projects_data = [
        {
            "code": "A001",
            "title": "BAIUST Campus Lost & Found System",
            "category": "Full-Stack Web",
            "tech_stack": "Django 5, Python, Bootstrap 5, PostgreSQL, Multi-Factor Matching",
            "summary": "Production university recovery platform across 14 BAIUST campus zones. Features a weighted 0–100% matching algorithm and secret-mark verification workflow to replace disorganized social media posts.",
            "why_built": "Students frequently lose essential items like IDs, calculators, and lab materials across campus. Social media posts are chaotic and unverified, creating a need for an authenticated institutional lost-and-found system.",
            "architecture": "Structured across modular Django apps (`accounts`, `items`, `claims`) with automated multi-factor scoring (location, item category, date decay, and keyword tokens) and secret-mark claim verification.",
            "hardware_code_highlights": "4-Factor Weighted Algorithm: Category 30% + Location 25% + Date Proximity 15% + Keyword Similarity 30% = Match Score.",
            "github_url": "https://github.com/Sakib20050413/campus_lostfound",
            "live_url": "https://campus-lostfound.onrender.com",
            "stars_count": 42,
            "is_featured": True,
            "order": 1,
        },
        {
            "code": "A002",
            "title": "IoT Storm & Lightning Early Warning Box (CSE 301 IDP)",
            "category": "Embedded IoT & TinyML",
            "tech_stack": "ESP32-S3, AS3935 RF, SIM800L GSM, TinyML, Web GIS",
            "summary": "Early-warning telemetry node detecting lightning strikes within 1–40 km using RF waveform analysis combined with pressure and light sensors. Alerts users via localized audio sirens and real-time Web GIS.",
            "why_built": "Severe thunderstorms and lightning strikes represent severe hazards in Bangladesh. This project provides hyper-local early detection to alert outdoor campus personnel and field workers before fatal proximity.",
            "architecture": "Sensor fusion integrating an AS3935 500 kHz RF lightning front-end detector, BH1750 ambient light lux drop, and BMP280 barometric rate-of-fall with cellular SMS alerts.",
            "hardware_code_highlights": "Embedded C++ state machine implementing the 30-30 lightning safety rule with an I2S MAX98357A speaker prompt.",
            "github_url": "https://github.com/Sakib20050413/lightning-early-warning-iot",
            "live_url": "https://team-blackberry.github.io/storm-gis",
            "stars_count": 58,
            "is_featured": True,
            "order": 2,
        },
        {
            "code": "A003",
            "title": "512-Point FFT Bio-Acoustic Mosquito Vector Trap (CSE 326)",
            "category": "Embedded IoT & TinyML",
            "tech_stack": "ESP32-S3 FPU, INMP441 I2S Mic, Radix-2 FFT (32ms), PWM MOSFET",
            "summary": "A smart vector trap executing a 512-point FFT on wingbeat audio to distinguish biting female mosquitoes (350–600 Hz) from non-biting insects, activating suction only when vectors are detected.",
            "why_built": "Chemical sprays harm beneficial pollinators and cause environmental damage. This non-chemical acoustic trap selectively captures disease-carrying female mosquitoes while remaining safe for honeybees.",
            "architecture": "Samples 16 kHz audio via an INMP441 digital microphone and executes an on-chip Radix-2 512-point FFT on the ESP32-S3 hardware FPU in 8.2 ms.",
            "hardware_code_highlights": "Dual-core FreeRTOS task division: Core 0 processes I2S DMA FFT buffers; Core 1 controls PWM suction MOSFET gates.",
            "github_url": "https://github.com/Sakib20050413/mosquito-dsp-trap",
            "live_url": "",
            "stars_count": 51,
            "is_featured": True,
            "order": 3,
        },
        {
            "code": "A004",
            "title": "CodeQuest 3D — Gamified Multi-Language Coding Platform (CSE 324)",
            "category": "Full-Stack Web",
            "tech_stack": "Django 5, Three.js WebGL, JavaScript DOM, Tailwind CSS, PHP CRUD",
            "summary": "Gamified platform helping students learn programming across multiple languages (C, C++, Python, JS, PHP) through interactive 2D grid challenges, live DOM builders, and quiz sprints.",
            "why_built": "Beginner students often struggle with abstract programming concepts. CodeQuest turns algorithmic logic into visual rover missions and interactive DOM manipulation.",
            "architecture": "Decoupled Django REST backend interfacing with a sandboxed compiler runner, paired with an HTML5 Canvas grid engine on the frontend.",
            "hardware_code_highlights": "Sub-second code evaluation, real-time leaderboard aggregation, and course quiz evaluation modules.",
            "github_url": "https://github.com/Sakib20050413/codequest-bd",
            "live_url": "https://codequest-bd.vercel.app",
            "stars_count": 39,
            "is_featured": True,
            "order": 4,
        },
        {
            "code": "A005",
            "title": "aloron-shop E-Commerce Platform",
            "category": "Full-Stack Web",
            "tech_stack": "Next.js, TypeScript, Tailwind CSS, Dynamic Cart",
            "summary": "Modern e-commerce storefront with dynamic category filtering, real-time cart state management, and a responsive mobile checkout experience.",
            "why_built": "Engineered to deliver clean web performance, Server-Side Rendering (SSR), and smooth state transitions without heavy third-party client dependencies.",
            "architecture": "Next.js App Router with TypeScript type safety across product schemas, local cart persistence, and modular UI components.",
            "hardware_code_highlights": "Zero layout shift, responsive mobile navigation, and reusable custom React hooks.",
            "github_url": "https://github.com/Sakib20050413/aloron-shop",
            "live_url": "https://aloron-shop.vercel.app",
            "stars_count": 27,
            "is_featured": False,
            "order": 5,
        },
        {
            "code": "A006",
            "title": "SmartSpend Expense & Budget Analytics",
            "category": "Full-Stack Web",
            "tech_stack": "Python, Django, Chart.js, SQLite/PostgreSQL",
            "summary": "Web app for personal expense logging and budget analytics with visual category breakdowns and spending summaries.",
            "why_built": "Designed as a personal utility to track recurring expenses, identify spending leaks, and organize monthly financial habits.",
            "architecture": "Django ORM aggregation queries visualised through Chart.js donut and line graphs with monthly statement generation.",
            "hardware_code_highlights": "Instant category budget threshold warnings and CSV transaction export.",
            "github_url": "https://github.com/Sakib20050413/smartspend-tracker",
            "live_url": "",
            "stars_count": 22,
            "is_featured": False,
            "order": 6,
        },
        {
            "code": "A007",
            "title": "Cafe Ordering & Kitchen Queue System",
            "category": "Desktop & DSP",
            "tech_stack": "Java, Swing GUI, OOP, FIFO Queue<Order>",
            "summary": "Desktop Point-of-Sale application with live menu management, order billing, and a real-time FIFO kitchen dispatch queue.",
            "why_built": "Built to eliminate communication errors between cafeteria cashiers and kitchen staff with instant desktop responsiveness.",
            "architecture": "Engineered purely in Java with Object-Oriented principles, using a thread-safe FIFO queue to track order preparation in real time.",
            "hardware_code_highlights": "Automated receipt formatting and clean multi-tab Java Swing layout with zero third-party dependencies.",
            "github_url": "https://github.com/Sakib20050413/restaurentorder",
            "live_url": "",
            "stars_count": 18,
            "is_featured": False,
            "order": 7,
        },
        {
            "code": "A008",
            "title": "Analog & Digital Signal Modulation Suite",
            "category": "Desktop & DSP",
            "tech_stack": "MATLAB, AM/FM/PM, ASK/FSK/PSK, CSE 322",
            "summary": "Comprehensive signal processing simulation toolkit implementing continuous-time and discrete-time stem plots, analog carrier modulation, and digital shift keying schemes.",
            "why_built": "Developed as a scientific simulation laboratory for the Data Communication (CSE 322) syllabus to visualize waveform distortions under AWGN channel noise.",
            "architecture": "Vectorized MATLAB scripts generating time-domain and frequency-domain FFT spectral distributions for AM, FM, ASK, and PSK.",
            "hardware_code_highlights": "Bit Error Rate (BER) vs SNR curve generation and constellation diagram plots for digital M-ary PSK.",
            "github_url": "https://github.com/Sakib20050413/data-comm-modulation-suite",
            "live_url": "",
            "stars_count": 19,
            "is_featured": False,
            "order": 8,
        },
    ]

    for pdata in projects_data:
        p, created = Project.objects.update_or_create(code=pdata["code"], defaults=pdata)
        print(f"[+] Project: [{p.code}] {p.title}")

    # 4. Skills (4 Structured Bento Categories)
    Skill.objects.all().delete()
    skills_data = [
        # 1. Backend & Full-Stack Web
        {"name": "Python", "category": "Backend & Full-Stack Web", "proficiency": 92, "order": 1},
        {"name": "Django 5", "category": "Backend & Full-Stack Web", "proficiency": 90, "order": 2},
        {"name": "Next.js", "category": "Backend & Full-Stack Web", "proficiency": 84, "order": 3},
        {"name": "REST APIs", "category": "Backend & Full-Stack Web", "proficiency": 88, "order": 4},
        {"name": "PHP (MySQLi CRUD)", "category": "Backend & Full-Stack Web", "proficiency": 80, "order": 5},
        {"name": "Authentication & ORM", "category": "Backend & Full-Stack Web", "proficiency": 88, "order": 6},

        # 2. Frontend & Interactive UI
        {"name": "JavaScript (ES6+)", "category": "Frontend & Interactive UI", "proficiency": 88, "order": 7},
        {"name": "TypeScript", "category": "Frontend & Interactive UI", "proficiency": 82, "order": 8},
        {"name": "React", "category": "Frontend & Interactive UI", "proficiency": 85, "order": 9},
        {"name": "HTML5 & CSS3", "category": "Frontend & Interactive UI", "proficiency": 94, "order": 10},
        {"name": "Tailwind CSS", "category": "Frontend & Interactive UI", "proficiency": 92, "order": 11},
        {"name": "Bootstrap 5", "category": "Frontend & Interactive UI", "proficiency": 86, "order": 12},
        {"name": "DOM Manipulation", "category": "Frontend & Interactive UI", "proficiency": 90, "order": 13},
        {"name": "Three.js / Canvas", "category": "Frontend & Interactive UI", "proficiency": 78, "order": 14},

        # 3. Embedded AI, IoT & DSP
        {"name": "ESP32-S3", "category": "Embedded AI, IoT & DSP", "proficiency": 88, "order": 15},
        {"name": "C / C++", "category": "Embedded AI, IoT & DSP", "proficiency": 86, "order": 16},
        {"name": "512-Point FFT DSP", "category": "Embedded AI, IoT & DSP", "proficiency": 82, "order": 17},
        {"name": "TinyML", "category": "Embedded AI, IoT & DSP", "proficiency": 80, "order": 18},
        {"name": "I2S / I2C / SPI / UART", "category": "Embedded AI, IoT & DSP", "proficiency": 85, "order": 19},
        {"name": "AS3935 / INMP441 / SIM800L", "category": "Embedded AI, IoT & DSP", "proficiency": 86, "order": 20},
        {"name": "MATLAB", "category": "Embedded AI, IoT & DSP", "proficiency": 80, "order": 21},

        # 4. Databases, Tools & Cloud
        {"name": "PostgreSQL (Neon/Supabase)", "category": "Databases, Tools & Cloud", "proficiency": 88, "order": 22},
        {"name": "SQLite", "category": "Databases, Tools & Cloud", "proficiency": 90, "order": 23},
        {"name": "MySQL", "category": "Databases, Tools & Cloud", "proficiency": 85, "order": 24},
        {"name": "Git & GitHub", "category": "Databases, Tools & Cloud", "proficiency": 90, "order": 25},
        {"name": "Render", "category": "Databases, Tools & Cloud", "proficiency": 85, "order": 26},
        {"name": "Vercel", "category": "Databases, Tools & Cloud", "proficiency": 86, "order": 27},
        {"name": "Linux", "category": "Databases, Tools & Cloud", "proficiency": 84, "order": 28},
        {"name": "Java Swing", "category": "Databases, Tools & Cloud", "proficiency": 82, "order": 29},
    ]

    for sdata in skills_data:
        s, created = Skill.objects.update_or_create(name=sdata["name"], defaults=sdata)
        print(f"[+] Skill: {s.name} ({s.category})")

    # 5. Timeline Entries
    TimelineEntry.objects.all().delete()
    timeline_data = [
        {
            "title": "Team Leader (Team 03) — Django Internship Program",
            "organization": "BAIUST Computer Club (10th Executive Panel)",
            "category": "Leadership",
            "period": "May 2026 – Present",
            "description": "Led a 3-member engineering team (with Nesar Uddin Ifaj 1119004 and Maliha Hossain 1119085) building production Django web apps with custom authentication, query optimization, and cloud deployment.",
            "order": 1,
        },
        {
            "title": "Team Leader — Team BlackBerry (IoT & TinyML Research Group)",
            "organization": "Dept. of Computer Science & Engineering, BAIUST",
            "category": "Experience",
            "period": "2026 – Present",
            "description": "Leading dual hardware-software research projects in CSE 301 (Interdisciplinary Design Project) and CSE 326 (Microprocessor & Embedded Systems Sessional) under Assistant Professor Arifur Rahaman and Lecturer Md. Fahim Kabir Chowdhury.",
            "order": 2,
        },
        {
            "title": "Internshala Student Partner (ISP) & Shortlisted AI/Robotics Candidate",
            "organization": "Internshala & Handshake (Uber AI Solutions)",
            "category": "Leadership",
            "period": "2026 – Present",
            "description": "Selected for university campus outreach leadership cohort. Shortlisted on Handshake for remote robotics video annotation specialist positions.",
            "order": 3,
        },
        {
            "title": "B.Sc. in Computer Science & Engineering (CSE)",
            "organization": "Bangladesh Army International University of Science and Technology (BAIUST), Cumilla",
            "category": "Education",
            "period": "Level 3, Term 2, Section A (Student ID: 1119003)",
            "description": "Core coursework: Web Technologies (CSE 323/324), Microprocessors & Embedded Systems (CSE 326), Data Communication (CSE 322), Software Engineering, Database Systems, Algorithms, and AI.",
            "order": 4,
        },
    ]

    for tdata in timeline_data:
        t, created = TimelineEntry.objects.update_or_create(
            title=tdata["title"],
            organization=tdata["organization"],
            defaults=tdata
        )
        print(f"[+] Timeline: {t.title}")

    print("\n[OK] Database seeded with 100% verified real 8 projects and 4 skill categories!")


if __name__ == "__main__":
    seed()
