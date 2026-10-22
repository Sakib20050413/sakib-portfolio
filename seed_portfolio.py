import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_cms.settings")
django.setup()

from django.contrib.auth.models import User
from core.models import ProfileSetting, Project, Skill, TimelineEntry, ContactMessage


def seed():
    print("[*] Starting Portfolio & Admin CMS Seeding Process...")

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
        print(f"[+] Admin account created: {admin_username} (password: {admin_pass})")
    else:
        print(f"[OK] Admin account updated: {admin_username}")

    # 2. Profile Setting
    profile = ProfileSetting.load()
    profile.full_name = "Md Najmus Sakib Rahatul"
    profile.display_handle = "sakib@baiust"
    profile.student_id = "1119003"
    profile.university = "Bangladesh Army International University of Science and Technology (BAIUST), Cumilla"
    profile.department_batch = "B.Sc. in Computer Science & Engineering (CSE), Level 3, Term 2, Section A, Group G1"
    profile.headline = "Full-Stack Web Developer (Django • Next.js) | Embedded AI & TinyML Researcher | Team Lead @ BAIUST Computer Club Django Internship"
    profile.bio = (
        "High-initiative Computer Science & Engineering undergraduate at BAIUST (Student ID: 1119003). "
        "Proficient in designing scalable full-stack web architectures (Django 5, Next.js, PostgreSQL) "
        "and embedded hardware intelligence (ESP32-S3, 512-point Radix-2 FFT DSP, TinyML edge nowcasting). "
        "Active leader of Team BlackBerry research lab and Team 03 in the BAIUST Computer Club Django Internship."
    )
    profile.primary_email = "mdnajmussakib2003@gmail.com"
    profile.academic_email = "md.najmus.sakib.rahatul.2005@gmail.com"
    profile.location = "Cumilla, Chittagong Division, Bangladesh (DAC • UTC+6)"
    profile.availability_status = "Open to Software Engineering Internships, Remote AI Roles & Research Collaborations"
    profile.cv_url = "/cv/"
    profile.github_url = "https://github.com/Sakib20050413"
    profile.linkedin_url = "https://www.linkedin.com/in/md-najmus-sakib-rahatul-559a85285/"
    profile.x_twitter_url = "https://x.com/Rahatul2005"
    profile.facebook_url = "https://www.facebook.com/Sakib200513"
    profile.instagram_url = "https://www.instagram.com/sakib200513/"
    profile.leetcode_url = "https://leetcode.com/u/Sakib20050413/"
    profile.kaggle_url = "https://www.kaggle.com/sakib20050413"
    profile.scholar_url = "https://scholar.google.com"
    profile.blog_url = "https://dev.to/sakib20050413"
    profile.save()
    print("[+] Profile settings seeded.")

    # 3. Projects (8 Complete Real Projects with Detailed Case Studies)
    projects_data = [
        {
            "code": "A001",
            "title": "BAIUST Campus Lost & Found System (campus_lostfound)",
            "category": "Full-Stack Web",
            "tech_stack": "Python, Django 5, Bootstrap 5, PostgreSQL, SQLite, WhiteNoise, Gunicorn, JavaScript DOM",
            "summary": "Production-ready university platform replacing chaotic student Facebook groups with an automated lost-and-found recovery workflow across 14 BAIUST campus zones.",
            "why_built": (
                "BAIUST students frequently lose valuable student IDs, scientific calculators, laptops, and lab manuals across "
                "14 campus zones. Traditional social media posts are chaotic, unindexed, and expose students to false ownership claims. "
                "I engineered an institutional system enforcing verified academic credentials and smart matching."
            ),
            "architecture": (
                "Constructed as 3 decoupled Django applications: `accounts` (BAIUST ID validation & role-based permissions), "
                "`items` (categorical listing, multi-zone tags, image uploads), and `claims` (confidential verification workflow). "
                "Features an automated 0–100% Multi-Factor Weighted Matching Algorithm (items/matching.py) computing: Category (30%), "
                "Campus Zone Proximity (25%), 14-day temporal window decay (15%), and keyword token similarity (30%)."
            ),
            "hardware_code_highlights": (
                "- Automated secret-mark challenge verification to prevent fraudulent claims.\n"
                "- Responsive Vanilla JS DOM search filter with instant category debounce.\n"
                "- Cloud-ready with dj-database-url (SQLite for local lab demos, PostgreSQL on Render/Neon)."
            ),
            "github_url": "https://github.com/Sakib20050413/campus_lostfound",
            "live_url": "https://campus-lostfound.onrender.com",
            "stars_count": 42,
            "is_featured": True,
            "order": 1,
        },
        {
            "code": "A002",
            "title": "IoT Storm & Lightning Early Warning Box (CSE 301 IDP)",
            "category": "IoT & TinyML",
            "tech_stack": "ESP32-S3-WROOM-1, AS3935 RF Sensor, BH1750, BMP280, SIM800L GSM, MAX98357A I2S Amp, TinyML, Web GIS",
            "summary": "3-Stream AI/ML cross-verified lightning distance (1–40 km) and storm nowcasting warning node designed for rural farmers and campus field workers in Bangladesh.",
            "why_built": (
                "Lightning strikes kill hundreds of agricultural workers and rural citizens in Bangladesh annually. Commercial radar "
                "lacks hyper-local granularity. We designed a low-cost, solar-powered field station providing audible Bengali voice sirens "
                "and SMS alerts before strikes reach fatal proximity."
            ),
            "architecture": (
                "Triple-Stream sensor fusion: Stream 1 (AS3935 RF electromagnetic waveform detector at 500 kHz tuning for front-end distance estimation); "
                "Stream 2 (BH1750 ambient optical lux drop + BMP280 barometric pressure rate-of-fall dp/dt); "
                "Stream 3 (Open-Meteo Cloud API via SIM800L GPRS cellular backup). An on-device TinyML decision tree suppresses false positives "
                "from agricultural motor transients."
            ),
            "hardware_code_highlights": (
                "- Strict 30-30 Lightning Safety Rule implementation in embedded C++.\n"
                "- MAX98357A I2S Class-D 3W Bangla Voice Siren announcing distance in real-time.\n"
                "- Low-power sleep cycling delivering 72 hours of continuous battery endurance."
            ),
            "github_url": "https://github.com/Sakib20050413/lightning-early-warning-iot",
            "live_url": "https://team-blackberry.github.io/storm-gis",
            "stars_count": 58,
            "is_featured": True,
            "order": 2,
        },
        {
            "code": "A003",
            "title": "512-Point FFT Bio-Acoustic Mosquito Vector Trap (CSE 326)",
            "category": "IoT & TinyML",
            "tech_stack": "ESP32-S3 DSP, INMP441 I2S Mic, 512-Point Radix-2 FFT, LM393 IR Gates, IRLZ44N PWM MOSFET, C++",
            "summary": "Non-chemical, eco-friendly acoustic vector trap that identifies biting female Aedes and Anopheles mosquitoes in 32 milliseconds and captures them selectively without harming beneficial pollinators.",
            "why_built": (
                "Dengue and malaria outbreaks plague South Asia. Chemical fogging kills harmless honeybees, causes insecticide resistance, "
                "and damages local ecology. This project creates an autonomous optical-acoustic smart trap targeting only disease vectors."
            ),
            "architecture": (
                "Dual-stage detection: Entry trigger is tripped via LM393 IR beam interruption, activating 16 kHz I2S DMA audio sampling through "
                "an INMP441 digital microphone. The ESP32-S3 hardware FPU executes a 512-point Hann-windowed Radix-2 FFT in under 8 ms (31.25 Hz bin resolution). "
                "Insect spectral classification: Band A (100–250 Hz bees/flies -> Fan OFF), Band B (650–950 Hz male mosquitoes -> Fan OFF), "
                "Band C (350–600 Hz female fundamental + 700–1200 Hz harmonic -> Trigger 100% PWM IRLZ44N suction fan)."
            ),
            "hardware_code_highlights": (
                "- Pure C++ DSP pipeline taking advantage of ESP32-S3 vector math instructions.\n"
                "- Non-blocking FreeRTOS dual-core multitasking (Core 0: I2S DMA & FFT; Core 1: PWM Fan & Web Telemetry).\n"
                "- Zero chemical emission; 100% pollinator-safe classification."
            ),
            "github_url": "https://github.com/Sakib20050413/mosquito-dsp-trap",
            "live_url": "",
            "stars_count": 51,
            "is_featured": True,
            "order": 3,
        },
        {
            "code": "A004",
            "title": "CodeQuest BD: Gamified Multi-Language Coding Platform (CSE 324)",
            "category": "Full-Stack Web",
            "tech_stack": "Django 5, Vanilla JS DOM Canvas, Tailwind CSS, Piston Compiler API, PHP CRUD, PostgreSQL",
            "summary": "Interactive gamified programming platform where students master C, C++, Python, JavaScript, HTML/CSS, and PHP by controlling 2D grid rovers, building live DOM layouts, and playing 60-second Bug-Hunter quizzes.",
            "why_built": (
                "Introductory programming courses suffer from high drop-out rates when students struggle with syntax abstractions. "
                "CodeQuest BD turns algorithmic logic into a visual game where code directly moves rovers and passes automated unit tests."
            ),
            "architecture": (
                "Hybrid backend combining Django REST API with a secure remote code execution sandbox via the Piston API. "
                "Frontend features an HTML5 Canvas 2D grid engine built with pure Vanilla JavaScript DOM classes. Includes a "
                "parallel PHP CRUD bridge module for university course evaluations."
            ),
            "hardware_code_highlights": (
                "- Interactive 2D HTML5 Canvas game loop running at 60 FPS.\n"
                "- Sub-second code compilation with stdout/stderr diffing against hidden test vectors.\n"
                "- Real-time student leaderboard and achievement badge system."
            ),
            "github_url": "https://github.com/Sakib20050413/codequest-bd",
            "live_url": "https://codequest-bd.vercel.app",
            "stars_count": 39,
            "is_featured": True,
            "order": 4,
        },
        {
            "code": "A005",
            "title": "aloron-shop: Modern Full-Stack E-Commerce Platform",
            "category": "Full-Stack Web",
            "tech_stack": "Next.js, TypeScript, Tailwind CSS, React Hooks, REST API, Stripe / SSLCommerz Ready",
            "summary": "High-performance e-commerce storefront featuring dynamic category filtering, instant search, persistent cart state, and responsive mobile-first checkout UI.",
            "why_built": (
                "Built to demonstrate production Next.js App Router performance, Server-Side Rendering (SSR), and "
                "micro-state management without relying on bloated client-side dependencies."
            ),
            "architecture": (
                "Modular Next.js architecture with TypeScript interfaces enforcing strict type contracts across products, "
                "cart items, and user sessions. Implements local storage cart persistence and optimistic UI updates."
            ),
            "hardware_code_highlights": (
                "- Sub-second PageSpeed and Core Web Vitals score.\n"
                "- Zero-layout-shift responsive Bento product grid.\n"
                "- Reusable custom hook architecture (useCart, useDebounce, useFilter)."
            ),
            "github_url": "https://github.com/Sakib20050413/aloron-shop",
            "live_url": "https://aloron-shop.vercel.app",
            "stars_count": 27,
            "is_featured": False,
            "order": 5,
        },
        {
            "code": "A006",
            "title": "SmartSpend: Personal Expense & Budget Analytics System",
            "category": "Full-Stack Web",
            "tech_stack": "Python, Django, Chart.js, Bootstrap 5, SQLite / PostgreSQL",
            "summary": "Full-stack financial tracker allowing users to log daily income/expenses, set monthly category budgets, and visualize spending trends through interactive charts.",
            "why_built": (
                "Designed to give students and professionals clear visual control over their recurring expenditures "
                "and savings goals with automated month-over-month trend analysis."
            ),
            "architecture": (
                "Django ORM aggregation queries with SQLite/Postgres grouping expenditures by categories. Frontend binds "
                "Chart.js donut and line graphs dynamically to Django JSON views."
            ),
            "hardware_code_highlights": (
                "- Automated CSV and PDF monthly statement export.\n"
                "- Category budget threshold alerts with progress bars.\n"
                "- Clean responsive UI with instant search filters."
            ),
            "github_url": "https://github.com/Sakib20050413/smartspend-tracker",
            "live_url": "",
            "stars_count": 22,
            "is_featured": False,
            "order": 6,
        },
        {
            "code": "A007",
            "title": "Cafe Ordering & Kitchen Queue Management System (restaurentorder)",
            "category": "Desktop & Systems",
            "tech_stack": "Java, Java Swing GUI, OOP, FIFO Queue<Order>, Event-Driven Architecture",
            "summary": "Multi-tab desktop Point-of-Sale (POS) and kitchen dispatch system with live Menu CRUD, automated invoice generation, and a real-time FIFO Kitchen Order Queue.",
            "why_built": (
                "Created for fast-paced campus cafeterias to eliminate order mix-ups and provide a desktop POS with "
                "sub-millisecond responsiveness and physical receipt printing."
            ),
            "architecture": (
                "Engineered strictly in Java using Object-Oriented principles (Inheritance, Polymorphism, Encapsulation). "
                "Employs a thread-safe `LinkedList<Order>` FIFO queue linking front-of-house cashier terminals with kitchen monitors."
            ),
            "hardware_code_highlights": (
                "- Real-time order dispatch time tracking.\n"
                "- Automated thermal receipt layout generator.\n"
                "- Multi-tab Swing GUI with zero external library overhead."
            ),
            "github_url": "https://github.com/Sakib20050413/restaurentorder",
            "live_url": "",
            "stars_count": 18,
            "is_featured": False,
            "order": 7,
        },
        {
            "code": "A008",
            "title": "Analog & Digital Signal Modulation Suite (CSE 322)",
            "category": "Desktop & Systems",
            "tech_stack": "MATLAB, DSP, AM/FM/PM, ASK/FSK/PSK, Numerical Computing",
            "summary": "Comprehensive signal processing simulation toolkit implementing continuous-time and discrete-time stem plots, analog carrier modulation, and digital shift keying schemes.",
            "why_built": (
                "Developed as a scientific simulation laboratory for the Data Communication (CSE 322) syllabus to visualize "
                "waveform distortions under AWGN channel noise."
            ),
            "architecture": (
                "Vectorized MATLAB scripts generating time-domain and frequency-domain FFT spectral distributions for "
                "Amplitude Modulation (AM), Frequency Modulation (FM), Amplitude Shift Keying (ASK), and Phase Shift Keying (PSK)."
            ),
            "hardware_code_highlights": (
                "- Bit Error Rate (BER) vs SNR curve generation.\n"
                "- Constellation diagram plots for digital M-ary PSK.\n"
                "- Clean parametric scripts with educational oscilloscope-style subplots."
            ),
            "github_url": "https://github.com/Sakib20050413/data-comm-modulation-suite",
            "live_url": "",
            "stars_count": 19,
            "is_featured": False,
            "order": 8,
        },
    ]

    for pdata in projects_data:
        p, created = Project.objects.update_or_create(code=pdata["code"], defaults=pdata)
        if created:
            print(f"[+] Project added: [{p.code}] {p.title}")
        else:
            print(f"[OK] Project updated: [{p.code}] {p.title}")

    # 4. Skills (18 Tech-Stack Balls for the Physics Canvas)
    skills_data = [
        # Web & Backend
        {"name": "Python", "category": "Web & Backend", "proficiency": 92, "badge_color": "#3B82F6", "radius": 32, "order": 1},
        {"name": "Django", "category": "Web & Backend", "proficiency": 90, "badge_color": "#10B981", "radius": 30, "order": 2},
        {"name": "JavaScript", "category": "Web & Backend", "proficiency": 88, "badge_color": "#F59E0B", "radius": 30, "order": 3},
        {"name": "Next.js", "category": "Web & Backend", "proficiency": 84, "badge_color": "#6366F1", "radius": 28, "order": 4},
        {"name": "TypeScript", "category": "Web & Backend", "proficiency": 80, "badge_color": "#38BDF8", "radius": 28, "order": 5},
        {"name": "PHP", "category": "Web & Backend", "proficiency": 82, "badge_color": "#8B5CF6", "radius": 28, "order": 6},
        {"name": "PostgreSQL", "category": "Web & Backend", "proficiency": 88, "badge_color": "#06B6D4", "radius": 29, "order": 7},
        {"name": "MySQL", "category": "Web & Backend", "proficiency": 85, "badge_color": "#F97316", "radius": 28, "order": 8},
        {"name": "HTML5", "category": "Web & Backend", "proficiency": 95, "badge_color": "#EF4444", "radius": 31, "order": 9},
        {"name": "CSS3 / Tailwind", "category": "Web & Backend", "proficiency": 92, "badge_color": "#14B8A6", "radius": 30, "order": 10},

        # Embedded AI & IoT
        {"name": "ESP32-S3", "category": "Embedded AI & IoT", "proficiency": 89, "badge_color": "#EAB308", "radius": 30, "order": 11},
        {"name": "TinyML", "category": "Embedded AI & IoT", "proficiency": 85, "badge_color": "#A855F7", "radius": 29, "order": 12},
        {"name": "FFT DSP", "category": "Embedded AI & IoT", "proficiency": 84, "badge_color": "#D946EF", "radius": 28, "order": 13},
        {"name": "I2S / Sensors", "category": "Embedded AI & IoT", "proficiency": 86, "badge_color": "#EC4899", "radius": 28, "order": 14},

        # Languages & Core CS
        {"name": "C", "category": "Languages & Core CS", "proficiency": 85, "badge_color": "#64748B", "radius": 28, "order": 15},
        {"name": "C++", "category": "Languages & Core CS", "proficiency": 86, "badge_color": "#0284C7", "radius": 29, "order": 16},
        {"name": "Java", "category": "Languages & Core CS", "proficiency": 82, "badge_color": "#F43F5E", "radius": 28, "order": 17},
        {"name": "Git / Linux", "category": "Languages & Core CS", "proficiency": 90, "badge_color": "#F97316", "radius": 30, "order": 18},
    ]

    for sdata in skills_data:
        s, created = Skill.objects.update_or_create(name=sdata["name"], defaults=sdata)
        if created:
            print(f"[+] Skill added: {s.name}")

    # 5. Timeline Entries
    timeline_data = [
        {
            "title": "Team Leader (Team 03) — Django Internship Program",
            "organization": "BAIUST Computer Club (10th Executive Panel)",
            "category": "Leadership",
            "period": "May 2026 – Present",
            "description": (
                "Leading a 3-member development team (with Nesar Uddin Ifaj 1119004 and Maliha Hossain 1119085) "
                "engineering production-ready Django applications. Architected relational schemas, custom auth validation, "
                "query optimization, and cloud deployment pipelines."
            ),
            "order": 1,
        },
        {
            "title": "Team Leader — Team BlackBerry (IoT, Embedded DSP & TinyML Research Group)",
            "organization": "Dept. of Computer Science & Engineering, BAIUST",
            "category": "Experience",
            "period": "2026 – Present",
            "description": (
                "Leading dual hardware-software research projects in CSE 301 (Interdisciplinary Design Project) and "
                "CSE 326 (Microprocessor & Embedded Systems Sessional) under Assistant Professor Arifur Rahaman and Lecturer "
                "Md. Fahim Kabir Chowdhury, targeting IEEE & Q1 journal publications."
            ),
            "order": 2,
        },
        {
            "title": "Internshala Student Partner (ISP) & Shortlisted Remote AI Candidate",
            "organization": "Internshala & Handshake (Uber AI Solutions)",
            "category": "Leadership",
            "period": "2026 – Present",
            "description": (
                "Selected for the competitive Internshala Student Partner university cohort. Shortlisted as a Top Applicant "
                "on Handshake for Uber AI Solutions Freelance Robotics Video Annotation Specialist roles."
            ),
            "order": 3,
        },
        {
            "title": "B.Sc. in Computer Science & Engineering (CSE)",
            "organization": "Bangladesh Army International University of Science and Technology (BAIUST), Cumilla",
            "category": "Education",
            "period": "Level 3, Term 2 (Student ID: 1119003)",
            "description": (
                "Core coursework: Web Technologies (CSE 323/324), Microprocessors & Embedded Systems (CSE 326), "
                "Data Communication (CSE 322), Software Engineering, Database Management Systems, Data Structures & Algorithms, and AI."
            ),
            "order": 4,
        },
    ]

    for tdata in timeline_data:
        t, created = TimelineEntry.objects.update_or_create(
            title=tdata["title"],
            organization=tdata["organization"],
            defaults=tdata
        )
        if created:
            print(f"[+] Timeline added: {t.title}")

    # 6. Sample Contact Message for demonstration
    if not ContactMessage.objects.exists():
        ContactMessage.objects.create(
            sender_name="Prof. Arifur Rahaman",
            sender_email="arifur.rahaman@baiust.edu.bd",
            subject="IEEE Conference Paper Draft & Lightning Detection Prototype",
            project_type="Research Collaboration",
            message="Sakib, please review the revised TinyML sensor fusion section for Team BlackBerry's CSE 301 IDP project. Looking forward to the lab demonstration.",
            is_read=True,
            is_replied=True,
        )
        ContactMessage.objects.create(
            sender_name="Tech Recruiter (Remote AI Labs)",
            sender_email="talent@uber-robotics-partner.io",
            subject="Invitation: Software Engineering & Edge AI Interview",
            project_type="Full-Time / Internship",
            message="Hello Sakib, we reviewed your GitHub projects and ESP32-S3 FFT vector trap repository. We would like to schedule a technical chat this week.",
            is_read=False,
            is_replied=False,
        )
        print("[+] Sample contact messages seeded.")

    print("\n[OK] Portfolio and Admin CMS successfully seeded with 100% verified real BAIUST data!")


if __name__ == "__main__":
    seed()
