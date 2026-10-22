import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_cms.settings")
django.setup()

from django.contrib.auth.models import User
from core.models import ProfileSetting, Project, Skill, TimelineEntry, ContactMessage


def seed():
    print("[*] Seeding Apple/Heva-grade refined portfolio data...")

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

    # 2. Profile Setting (Authentic, human voice)
    profile = ProfileSetting.load()
    profile.full_name = "Md Najmus Sakib Rahatul"
    profile.display_handle = "sakib@baiust"
    profile.student_id = "1119003"
    profile.university = "Bangladesh Army International University of Science and Technology (BAIUST), Cumilla"
    profile.department_batch = "B.Sc. in Computer Science & Engineering (CSE), Level 3, Term 2, Section A, Group G1"
    profile.headline = "Full-Stack Web Developer & Embedded Systems Undergrad"
    profile.bio = (
        "I'm a 3rd-year Computer Science & Engineering student at BAIUST, Cumilla. "
        "I build full-stack web applications with Python/Django and Next.js, and work on embedded IoT and "
        "signal processing systems with ESP32-S3. I enjoy solving practical problems—whether that's automating "
        "campus operations, designing interactive tools, or building real-time environmental monitoring hardware."
    )
    profile.primary_email = "mdnajmussakib2003@gmail.com"
    profile.academic_email = "md.najmus.sakib.rahatul.2005@gmail.com"
    profile.location = "Cumilla, Bangladesh (DAC • UTC+6)"
    profile.availability_status = "Available for Software Engineering Internships & Collaborative Projects"
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
    print("[+] Profile settings updated with human tone.")

    # 3. Clean Projects (7 crisp real systems)
    Project.objects.all().delete()
    projects_data = [
        {
            "code": "A001",
            "title": "BAIUST Campus Lost & Found System",
            "category": "Web Applications",
            "tech_stack": "Django 5, Bootstrap 5, PostgreSQL, Campus Auth",
            "summary": "A dedicated campus platform for BAIUST students to report and recover lost items across 14 campus zones. Features a weighted 0–100% matching algorithm and verification workflow to replace disorganized social media posts.",
            "why_built": "Students frequently lose essential items like IDs, calculators, and lab materials across campus. Social media posts are chaotic and unverified, creating a need for an authenticated institutional lost-and-found system.",
            "architecture": "Structured across modular Django apps (`accounts`, `items`, `claims`) with automated multi-factor scoring (location, item category, date decay, and keyword tokens) and secret-mark claim verification.",
            "hardware_code_highlights": "Clean query optimization, responsive mobile layout, and production-ready dj-database-url integration.",
            "github_url": "https://github.com/Sakib20050413/campus_lostfound",
            "live_url": "https://campus-lostfound.onrender.com",
            "stars_count": 42,
            "is_featured": True,
            "order": 1,
        },
        {
            "code": "A002",
            "title": "IoT Storm & Lightning Early Warning Box (CSE 301 IDP)",
            "category": "Embedded Systems",
            "tech_stack": "ESP32-S3, AS3935 RF, Sensors, Web GIS",
            "summary": "An early-warning telemetry node detecting lightning strikes within 1–40 km using RF waveform analysis combined with pressure and light sensors. Alerts users via localized audio sirens and a real-time web map.",
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
            "category": "Embedded Systems",
            "tech_stack": "ESP32-S3 DSP, INMP441 I2S Mic, Radix-2 FFT, PWM",
            "summary": "A smart mosquito trap that runs a 512-point FFT on wingbeat audio to distinguish biting female mosquitoes (350–600 Hz) from non-biting insects, activating a suction fan only when vectors are detected.",
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
            "title": "CodeQuest BD: Gamified Programming Learning Platform (CSE 324)",
            "category": "Web Applications",
            "tech_stack": "Django 5, JavaScript DOM, Tailwind CSS, Compiler API",
            "summary": "A gamified platform helping students learn programming across multiple languages (C, C++, Python, JS, PHP) through interactive 2D grid challenges, live DOM builders, and quiz sprints.",
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
            "category": "Web Applications",
            "tech_stack": "Next.js, TypeScript, Tailwind CSS, Cart State",
            "summary": "A modern e-commerce storefront with category filtering, real-time cart state management, and a responsive mobile checkout experience.",
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
            "title": "SmartSpend Personal Expense Tracker",
            "category": "Web Applications",
            "tech_stack": "Python, Django, Chart.js, SQLite/PostgreSQL",
            "summary": "A web app for personal expense logging and budget analytics with visual category breakdowns and spending summaries.",
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
            "title": "Cafe Ordering & Kitchen Dispatch System",
            "category": "Desktop Tools",
            "tech_stack": "Java, Swing GUI, OOP, FIFO Queue",
            "summary": "A desktop Point-of-Sale application with live menu management, order billing, and a real-time FIFO kitchen dispatch queue.",
            "why_built": "Built to eliminate communication errors between cafeteria cashiers and kitchen staff with instant desktop responsiveness.",
            "architecture": "Engineered purely in Java with Object-Oriented principles, using a thread-safe FIFO queue to track order preparation in real time.",
            "hardware_code_highlights": "Automated receipt formatting and clean multi-tab Java Swing layout with zero third-party dependencies.",
            "github_url": "https://github.com/Sakib20050413/restaurentorder",
            "live_url": "",
            "stars_count": 18,
            "is_featured": False,
            "order": 7,
        },
    ]

    for pdata in projects_data:
        p, created = Project.objects.update_or_create(code=pdata["code"], defaults=pdata)
        print(f"[+] Project: [{p.code}] {p.title}")

    # 4. Clean Skills (Structured in 4 quiet categories)
    Skill.objects.all().delete()
    skills_data = [
        # Languages
        {"name": "Python", "category": "Languages", "proficiency": 92, "order": 1},
        {"name": "JavaScript", "category": "Languages", "proficiency": 88, "order": 2},
        {"name": "TypeScript", "category": "Languages", "proficiency": 82, "order": 3},
        {"name": "C", "category": "Languages", "proficiency": 85, "order": 4},
        {"name": "C++", "category": "Languages", "proficiency": 86, "order": 5},
        {"name": "PHP", "category": "Languages", "proficiency": 80, "order": 6},
        {"name": "Java", "category": "Languages", "proficiency": 82, "order": 7},
        {"name": "SQL", "category": "Languages", "proficiency": 86, "order": 8},
        {"name": "HTML5 & CSS3", "category": "Languages", "proficiency": 94, "order": 9},

        # Frameworks & Libraries
        {"name": "Django", "category": "Frameworks & Libraries", "proficiency": 90, "order": 10},
        {"name": "Next.js", "category": "Frameworks & Libraries", "proficiency": 84, "order": 11},
        {"name": "React", "category": "Frameworks & Libraries", "proficiency": 85, "order": 12},
        {"name": "Tailwind CSS", "category": "Frameworks & Libraries", "proficiency": 92, "order": 13},
        {"name": "Bootstrap 5", "category": "Frameworks & Libraries", "proficiency": 88, "order": 14},

        # Hardware & Embedded
        {"name": "ESP32-S3", "category": "Hardware & Embedded", "proficiency": 88, "order": 15},
        {"name": "Arduino", "category": "Hardware & Embedded", "proficiency": 86, "order": 16},
        {"name": "I2S / I2C / SPI Buses", "category": "Hardware & Embedded", "proficiency": 85, "order": 17},
        {"name": "Digital Signal Processing (FFT)", "category": "Hardware & Embedded", "proficiency": 82, "order": 18},
        {"name": "Sensors (RF, Pressure, Light)", "category": "Hardware & Embedded", "proficiency": 86, "order": 19},

        # Tools & Platforms
        {"name": "Git & GitHub", "category": "Tools & Platforms", "proficiency": 90, "order": 20},
        {"name": "PostgreSQL", "category": "Tools & Platforms", "proficiency": 88, "order": 21},
        {"name": "Docker", "category": "Tools & Platforms", "proficiency": 75, "order": 22},
        {"name": "Linux", "category": "Tools & Platforms", "proficiency": 85, "order": 23},
        {"name": "Vercel & Render", "category": "Tools & Platforms", "proficiency": 88, "order": 24},
    ]

    for sdata in skills_data:
        s, created = Skill.objects.update_or_create(name=sdata["name"], defaults=sdata)
        print(f"[+] Skill: {s.name} ({s.category})")

    # 5. Timeline Entries (Human, verified)
    TimelineEntry.objects.all().delete()
    timeline_data = [
        {
            "title": "Team Leader — Django Internship Program",
            "organization": "BAIUST Computer Club (10th Executive Panel)",
            "category": "Leadership",
            "period": "May 2026 – Present",
            "description": "Led a 3-member team building full-stack Django web applications, managing authentication, database modeling, and deployment.",
            "order": 1,
        },
        {
            "title": "Team Leader — Team BlackBerry (Hardware & Embedded Systems Group)",
            "organization": "Dept. of Computer Science & Engineering, BAIUST",
            "category": "Experience",
            "period": "2026 – Present",
            "description": "Leading undergraduate research teams on dual hardware-software systems in CSE 301 and CSE 326 under faculty supervision.",
            "order": 2,
        },
        {
            "title": "Internshala Student Partner (ISP) & Remote Candidate",
            "organization": "Internshala & Handshake",
            "category": "Leadership",
            "period": "2026 – Present",
            "description": "Selected for campus outreach and shortlisted for remote technical annotation opportunities.",
            "order": 3,
        },
        {
            "title": "B.Sc. in Computer Science & Engineering",
            "organization": "Bangladesh Army International University of Science and Technology (BAIUST), Cumilla",
            "category": "Education",
            "period": "Class of 2027 (Student ID: 1119003)",
            "description": "Completed coursework in Data Structures, Algorithms, OOP, Database Systems, Web Technologies, and Embedded Systems.",
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

    print("\n[OK] Database successfully seeded with authentic, human-crafted content!")


if __name__ == "__main__":
    seed()
