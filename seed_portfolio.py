import os
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_project.settings")
    django.setup()


def run_seed():
    from django.contrib.auth.models import User
    from core.models import (
        ProfileConfig,
        AIArchitectureNode,
        Skill,
        Project,
        CourseCertification,
        TimelineEntry,
    )

    if not User.objects.filter(username="sakib_admin").exists():
        User.objects.create_superuser("sakib_admin", "mdnajmussakib2003@gmail.com", "baiust1119003")

    if ProfileConfig.objects.count() == 0:
        ProfileConfig.objects.create(
            site_name="SAKIB // AI & SYSTEMS",
            full_name="Md Najmus Sakib Rahatul",
            role_title="AI/ML Systems Engineer • Edge TinyML Researcher • Full-Stack Architect",
            hero_headline="Engineering Sovereign Local AI Runtimes, Real-Time Edge TinyML Hardware & High-Scale Full-Stack Web Platforms.",
            bio_summary=(
                "AI/ML Engineer, Embedded TinyML Researcher, and Full-Stack Systems Architect (Django, FastAPI, Next.js). "
                "My research and engineering focus on locally resident multi-model AI runtimes across unified CPU RAM, GPU VRAM, "
                "and NPU memory, 32 ms real-time bio-acoustic & RF digital signal processing on ESP32-S3 hardware, and "
                "production cloud platforms deployed on Vercel."
            ),
            photo_url="https://avatars.githubusercontent.com/u/166808901?v=4",
            location="Cumilla / Dhaka, Bangladesh (UTC+6)",
            availability_text="Available for AI/ML Engineering Roles, Global Remote Contracts & IEEE/Q1 Research",
            primary_email="mdnajmussakib2003@gmail.com",
            secondary_email="md.najmus.sakib.rahatul.2005@gmail.com",
            github_url="https://github.com/Sakib20050413",
            linkedin_url="https://www.linkedin.com/in/md-najmus-sakib-rahatul-559a85285/",
            kaggle_url="https://www.kaggle.com/sakib20050413",
            twitter_url="https://x.com/Rahatul2005",
            facebook_url="https://www.facebook.com/Sakib200513",
            instagram_url="https://www.instagram.com/sakib200513/",
            default_theme="dark",
        )

    # Always refresh AIArchitectureNode if old PHOTO/VIDEO nodes exist
    if AIArchitectureNode.objects.filter(node_id__icontains="PHOTO").exists() or AIArchitectureNode.objects.count() == 0:
        AIArchitectureNode.objects.all().delete()
        nodes = [
            (
                "ROUTER-CORE",
                "Always-Resident Local Master AI Dispatcher & Memory Pager",
                "~420 MB Resident in Unified RAM",
                "CPU System RAM + NPU Control Plane",
                "Persistent local orchestrator that parses engineering prompts, schedules sub-1GB quantized specialist models, and eliminates cloud API latency.",
                "Maintains a zero-overhead control graph in system RAM with deterministic memory paging across CPU, GPU VRAM, and NPU."
            ),
            (
                "CODE-AST-1G",
                "Code-AST-1G Specialist (Full-Stack & Systems Code Synthesis)",
                "~0.95 GB (4-Bit NF4 / GGUF Quantized)",
                "GPU VRAM + Unified System Memory",
                "Specialized 4-bit quantized coding and AST verification micro-model hot-swapped into memory for Python, C++, TypeScript, and SQL generation.",
                "Uses speculative AST decoding and QLoRA adapters to achieve frontier coding accuracy inside a sub-1GB memory envelope."
            ),
            (
                "RAG-REASON-1G",
                "Hybrid-RAG & Scientific Reasoning Sub-Model",
                "~0.92 GB (4-Bit Quantized + Cross-Encoder)",
                "CPU System RAM + pgvector / FAISS Index",
                "On-demand retrieval and analytical reasoning engine combining dense vector embeddings with BM25 lexical search.",
                "Grounds every generated answer in verified local documentation, codebases, and IEEE research papers with zero hallucination."
            ),
            (
                "EDGE-DSP-TINYML",
                "Real-Time Edge TinyML & 512-Point FFT Signal Classifier",
                "~180 KB Int8 TFLite Micro / C++ DSP Kernel",
                "ESP32-S3 Dual-Core 240 MHz + PIE Vector Unit",
                "Ultra-low-latency acoustic and RF sensor-fusion kernel executing 512-point Radix-2 FFT spectral classification in 32 ms.",
                "Powers the Bio-Acoustic Mosquito Vector Trap (350–600 Hz harmonic isolation) and the 3-Stream Rural Lightning Early Warning System."
            ),
            (
                "CONTINUAL-LORA",
                "In-Place Single-Node Continual Self-Training Engine (LoRA ΔW)",
                "Zero Extra Checkpoint Bloat (In-Place Delta Merge)",
                "Persistent Local Neural Graph in RAM + NVMe",
                "Autonomous continual learning mechanism that updates and refines the active neural node in place without spawning duplicate model files.",
                "Applies Elastic Weight Consolidation (EWC) and low-rank ΔW = B·A weight merging directly into the resident node."
            ),
        ]
        for idx, (nid, title, mem, hw, summ, mech) in enumerate(nodes, start=1):
            AIArchitectureNode.objects.create(
                node_id=nid, title=title, memory_budget=mem, hardware_pool=hw,
                summary=summ, mechanism_detail=mech, order=idx
            )

    if Skill.objects.count() == 0:
        skills_data = [
            ("PyTorch & Deep Neural Architectures", "LLM_CORE", 96, "Core AI"),
            ("Transformers (Llama, Qwen, Mistral)", "LLM_CORE", 95, "LLM Core"),
            ("LoRA, QLoRA & PEFT Fine-Tuning", "LLM_CORE", 94, "Adaptation"),
            ("In-Place Continual Learning (LoRA ΔW)", "LLM_CORE", 93, "Self-Evolving"),
            ("RLHF, DPO & Preference Alignment", "LLM_CORE", 91, "Alignment"),
            ("Hugging Face (Transformers, TRL, Datasets)", "LLM_CORE", 95, "Ecosystem"),
            ("4-Bit NF4, INT8, GGUF & AWQ Quantization", "LOCAL_RUNTIME", 95, "Compression"),
            ("llama.cpp, vLLM & ONNX Runtime", "LOCAL_RUNTIME", 94, "Local Inference"),
            ("CPU RAM + GPU VRAM + NPU Memory Paging", "LOCAL_RUNTIME", 96, "Flagship R&D"),
            ("ExecuTorch & Edge Neural Deployment", "LOCAL_RUNTIME", 92, "Cross-Device"),
            ("Sub-1GB Knowledge Distillation", "LOCAL_RUNTIME", 93, "Micro-Models"),
            ("Speculative Decoding & KV-Cache Paging", "LOCAL_RUNTIME", 91, "Low Latency"),
            ("Multi-Agent Orchestration (LangGraph / MCP)", "MULTIMODAL_AGENTS", 95, "Agentic AI"),
            ("Hybrid Vector + BM25 RAG & Reranking", "MULTIMODAL_AGENTS", 95, "Retrieval"),
            ("Autonomous Code & Sandbox Tool Agents", "MULTIMODAL_AGENTS", 94, "Agents"),
            ("Scikit-Learn, XGBoost, LightGBM & SHAP", "MULTIMODAL_AGENTS", 94, "Tabular ML"),
            ("Feature Engineering & Statistical Modeling", "MULTIMODAL_AGENTS", 93, "Data Science"),
            ("Empirical Telemetry & IEEE Dataset Design", "MULTIMODAL_AGENTS", 94, "Research"),
            ("TensorFlow Lite Micro & Int8 Quantization", "EDGE_TINYML", 96, "TinyML"),
            ("ESP32-S3 Dual-Core 240MHz Firmware", "EDGE_TINYML", 96, "Embedded AI"),
            ("512-Point Radix-2 FFT Bio-Acoustic DSP", "EDGE_TINYML", 96, "32ms Real-Time"),
            ("Multi-Stream Sensor Fusion (I2S, I2C, SPI, GSM)", "EDGE_TINYML", 95, "IoT Hardware"),
            ("Kaggle HumBugDB & Wingbeats Audio ML", "EDGE_TINYML", 95, "Spectral ML"),
            ("MATLAB Spectral & Signal Analysis", "EDGE_TINYML", 92, "DSP"),
            ("Python 3.12 & Async Systems Engineering", "FULLSTACK_WEB", 97, "Primary"),
            ("Django 5 (ORM, Custom CMS, Auth, REST)", "FULLSTACK_WEB", 96, "Team Lead"),
            ("FastAPI (Async Microservices & JWT HS256)", "FULLSTACK_WEB", 95, "API Architect"),
            ("Next.js 15, React & TypeScript", "FULLSTACK_WEB", 94, "Frontend"),
            ("JavaScript ES6+, DOM & Three.js WebGL", "FULLSTACK_WEB", 95, "Interactive 3D"),
            ("HTML5, CSS3, Tailwind CSS & PHP/MySQLi", "FULLSTACK_WEB", 95, "Web Core"),
            ("PostgreSQL (Neon, Supabase & pgvector)", "CLOUD_DATA", 94, "Database"),
            ("Prisma ORM & SQLAlchemy", "CLOUD_DATA", 94, "ORM Layer"),
            ("Docker & Containerized Microservices", "CLOUD_DATA", 93, "DevOps"),
            ("Vercel & Render Cloud CI/CD", "CLOUD_DATA", 96, "Production"),
            ("C, C++ (STL/OOP) & Java Systems", "CLOUD_DATA", 94, "Systems"),
            ("Git, GitHub Actions & Linux Automation", "CLOUD_DATA", 96, "Tooling"),
        ]
        for idx, (name, dom, prof, tag) in enumerate(skills_data, start=1):
            Skill.objects.create(name=name, domain=dom, proficiency=prof, highlight_tag=tag, order=idx)

    if Project.objects.count() == 0:
        projects_data = [
            {
                "code": "01",
                "title": "NexusLocal — Sovereign Local Master AI Orchestrator & Continual Learning Runtime",
                "slug": "nexuslocal-master-ai-orchestrator",
                "category": "AI_LLM",
                "status_label": "Flagship AI/ML Research",
                "tagline": "Always-resident ~420 MB Master AI Router that dynamically pages ~1 GB 4-bit quantized coding, RAG, and DSP models across CPU RAM, GPU VRAM, and NPU memory with in-place LoRA self-training.",
                "description": (
                    "Architected to eliminate cloud API latency and memory bloat on consumer laptops and edge devices. "
                    "A persistent Master Router dispatches tasks to compact ~1 GB quantized specialist sub-models (Code-AST-1G, "
                    "RAG-Reason-1G, Edge-DSP) while consolidating continual weight updates (ΔW = B·A) in place."
                ),
                "architecture_breakdown": (
                    "1. Resident Control Plane (~420 MB RAM): Intent parser + unified CPU/GPU/NPU memory pager.\n"
                    "2. On-Demand ~1 GB Specialist Queue: Hot-swaps 4-bit NF4 / GGUF models in <380 ms.\n"
                    "3. In-Place Continual Learning: Elastic Weight Consolidation + LoRA delta merge inside a single node."
                ),
                "tech_stack_csv": "PyTorch, 4-Bit NF4 QLoRA, llama.cpp, ONNX Runtime, CPU/GPU/NPU Pager, FastAPI",
                "live_server_url": "",
                "github_repo_url": "https://github.com/Sakib20050413",
                "bento_col_span": 6,
                "upvotes": 72,
                "is_ongoing": True,
                "order": 1,
            },
            {
                "code": "02",
                "title": "Aloron Shop — Next.js, TypeScript & Prisma Full-Stack E-Commerce Platform",
                "slug": "aloron-shop-nextjs-ecommerce",
                "category": "FULLSTACK",
                "status_label": "Live on Vercel",
                "tagline": "Production full-stack e-commerce platform built with Next.js App Router, TypeScript (98.9%), Prisma ORM, pure JWT authentication, and a dynamic CMS.",
                "description": (
                    "Ground-zero full-stack rebuild featuring type-safe Prisma relational queries, pure JWT session rotation, "
                    "dynamic banner/catalog CMS, reactive cart state synchronization, and Vitest automated testing."
                ),
                "architecture_breakdown": (
                    "1. Frontend & SSR: Next.js App Router + TypeScript + Tailwind CSS.\n"
                    "2. Data & Security: Prisma ORM + Pure JWT token verification (`auth.ts`).\n"
                    "3. Live Cloud Edge: Hosted on Vercel (`aloron-shop.vercel.app`)."
                ),
                "tech_stack_csv": "Next.js, TypeScript, Prisma ORM, Pure JWT Auth, Dynamic CMS, Vercel",
                "live_server_url": "https://aloron-shop.vercel.app",
                "github_repo_url": "https://github.com/Sakib20050413/aloron-shop",
                "bento_col_span": 6,
                "upvotes": 54,
                "is_ongoing": False,
                "order": 2,
            },
            {
                "code": "03",
                "title": "Campus Lost & Found — Automated Multi-Factor Matching Web Platform",
                "slug": "baiust-campus-lost-and-found",
                "category": "FULLSTACK",
                "status_label": "Live on Vercel",
                "tagline": "Full-stack Django recovery platform powered by a 0–100% multi-factor similarity scoring algorithm (`items/matching.py`) and ownership verification workflow.",
                "description": (
                    "Computes weighted similarity scores across item category (30%), campus zone (25%), date proximity (15%), "
                    "and keyword intersection (30%) to automatically pair lost reports with found items."
                ),
                "architecture_breakdown": (
                    "1. Matching Engine (`items/matching.py`): 4-factor weighted similarity algorithm.\n"
                    "2. Verification Pipeline (`claims/`): Secret-mark ownership verification + staff audit panel.\n"
                    "3. Live Deployment: Production WSGI server on Vercel (`baiust-campus-lost-and-found.vercel.app`)."
                ),
                "tech_stack_csv": "Python, Django 5, Multi-Factor Matching Algorithm, PostgreSQL / SQLite, Vercel",
                "live_server_url": "https://baiust-campus-lost-and-found.vercel.app",
                "github_repo_url": "https://github.com/Sakib20050413/baiust-campus-lost-and-found",
                "bento_col_span": 6,
                "upvotes": 61,
                "is_ongoing": False,
                "order": 3,
            },
            {
                "code": "04",
                "title": "CodeRealm 3D — Multi-World 3D Visual Programming & IEEE Telemetry Platform",
                "slug": "nexuscode-ai-3d-coding-platform",
                "category": "AI_LLM",
                "status_label": "Live on Vercel",
                "tagline": "Interactive polyglot programming and empirical research platform featuring 5 playable 3D simulation worlds (3D Fractal Tree, Solar Gravity, Neural Helix, Wave Drone, Cyber Boss) across 12 languages.",
                "description": (
                    "Replaces 2.5-hour passive coding videos with 45-second Feynman flash concepts and 5 distinct 60 FPS 3D "
                    "visual simulation games, while capturing empirical Time-to-Comprehension (TTC) telemetry for IEEE research."
                ),
                "architecture_breakdown": (
                    "1. 5 Playable 3D Worlds: Procedural 3D Fractal Tree, Orbital Physics, Neural Helix, Wave Drone & Boss Defense.\n"
                    "2. Polyglot AST Transpiler: Executes Python, JS, HTML/CSS, C, C++, PHP, SQL, TS, Java, Rust & Go.\n"
                    "3. IEEE Research Export: Live `/api/telemetry/export.csv` and `.json` endpoints."
                ),
                "tech_stack_csv": "Django 5, 60FPS 3D Canvas Engine, 12 Languages, IEEE Telemetry CSV/JSON, Vercel",
                "live_server_url": "https://codequest-bd.vercel.app",
                "github_repo_url": "https://github.com/Sakib20050413/codequest-bd",
                "bento_col_span": 6,
                "upvotes": 68,
                "is_ongoing": False,
                "order": 4,
            },
            {
                "code": "05",
                "title": "Bio-Acoustic Mosquito Vector AI Trap (`ESP32-S3 TinyML & 512-Pt FFT`)",
                "slug": "bio-acoustic-mosquito-ai-trap",
                "category": "EDGE_TINYML",
                "status_label": "Edge AI + Hardware Repo",
                "tagline": "32 ms real-time acoustic wingbeat classifier on ESP32-S3 separating female Aedes/Anopheles vectors (350–600 Hz) from beneficial pollinators (100–250 Hz).",
                "description": (
                    "Uses an INMP441 I2S digital microphone and Hann-windowed 512-point Radix-2 FFT at 16 kHz trained on "
                    "Kaggle Wingbeats and Oxford HumBugDB spectral profiles to trigger selective PWM MOSFET capture."
                ),
                "architecture_breakdown": (
                    "1. I2S DMA Audio Capture: INMP441 at 16 kHz -> 512-sample frame (32 ms window, 31.25 Hz bin resolution).\n"
                    "2. Spectral Classifier: Isolates female vector fundamental frequencies (350–600 Hz) while sparing bees.\n"
                    "3. Live Telemetry UI: Real-time FFT spectrum and species counter."
                ),
                "tech_stack_csv": "ESP32-S3, C++, Python, 512-Pt Radix-2 FFT, INMP441 I2S, Kaggle Wingbeats & HumBugDB",
                "live_server_url": "",
                "github_repo_url": "https://github.com/Sakib20050413/Bio-Acoustic-Mosquito-AI-Trap",
                "bento_col_span": 6,
                "upvotes": 57,
                "is_ongoing": False,
                "order": 5,
            },
            {
                "code": "06",
                "title": "IoT 3-Stream TinyML Rural Lightning Early Warning System + Web GIS",
                "slug": "iot-rural-lightning-early-warning-system",
                "category": "EDGE_TINYML",
                "status_label": "Edge AI + Web GIS Repo",
                "tagline": "3-stream TinyML storm nowcasting node combining AS3935 500 kHz RF sensing, sky IR thermometry, and SIM800L cellular telemetry with a live Web GIS map.",
                "description": (
                    "Cross-verifies local atmospheric readings (AS3935 RF strike distance 1–40 km, BMP280 pressure drop, "
                    "BH1750 lux, MLX90614 sky IR temperature) with cellular weather telemetry over SIM800L GSM."
                ),
                "architecture_breakdown": (
                    "1. Stream 1 (Atmospheric Array): BH1750 + MLX90614 + BMP280 + DHT22.\n"
                    "2. Stream 2 (RF Lightning Sensor): AS3935 500 kHz strike distance estimator.\n"
                    "3. Stream 3 (Cellular GIS): SIM800L GSM pushing live alert zones to Leaflet Web GIS."
                ),
                "tech_stack_csv": "ESP32-S3, TinyML Sensor Fusion, AS3935 RF, SIM800L GSM, Leaflet Web GIS, C++",
                "live_server_url": "",
                "github_repo_url": "https://github.com/Sakib20050413/IoT-Rural-Lightning-Early-Warning-System",
                "bento_col_span": 6,
                "upvotes": 52,
                "is_ongoing": False,
                "order": 6,
            },
            {
                "code": "07",
                "title": "CoWork — Multi-Tenant Coworking Space Booking API (`FastAPI + Docker`)",
                "slug": "cowork-fastapi-docker-hackathon",
                "category": "API_SYSTEMS",
                "status_label": "Hackathon Preliminary",
                "tagline": "Containerized FastAPI + SQLAlchemy REST API managing multi-tenant organization rooms, JWT HS256 token rotation, conflict-free slot booking, and analytics.",
                "description": (
                    "Built for the ICT Fest Hackathon Preliminary. Implements strict multi-tenant isolation, "
                    "role-based access control (Admin, Staff, Member), automated booking conflict detection, and Docker Compose deployment."
                ),
                "architecture_breakdown": (
                    "1. API Layer: Python 3.11 + FastAPI + Pydantic v2 schemas.\n"
                    "2. Auth & ORM: JWT access/refresh tokens (HS256) + SQLAlchemy ORM.\n"
                    "3. Containerization: Production `Dockerfile` + `docker-compose.yml`."
                ),
                "tech_stack_csv": "Python 3.11, FastAPI, SQLAlchemy, JWT Auth, Docker, Docker Compose, Pytest",
                "live_server_url": "",
                "github_repo_url": "https://github.com/Sakib20050413/ICT_Fest_Hackathon_Preliminary",
                "bento_col_span": 6,
                "upvotes": 46,
                "is_ongoing": False,
                "order": 7,
            },
            {
                "code": "08",
                "title": "SmartSpend Core & Library Management System (`Django Full-Stack`)",
                "slug": "smartspend-and-library-management",
                "category": "FULLSTACK",
                "status_label": "Production GitHub Repos",
                "tagline": "Full-stack Django expense intelligence (`smartspend_core`) and automated library circulation/catalog management platforms.",
                "description": (
                    "Two complete Django web applications featuring relational database modeling, category budget "
                    "analytics, interactive visual charts, book circulation workflows, and responsive UI templates."
                ),
                "architecture_breakdown": (
                    "1. SmartSpend (`smartspend_core`): Expense analytics and budget alerts.\n"
                    "2. Library Management System: Book inventory, member borrowing ledger, and fine calculation."
                ),
                "tech_stack_csv": "Python, Django, Relational DB, Chart.js, HTML5/CSS3, Git",
                "live_server_url": "",
                "github_repo_url": "https://github.com/Sakib20050413/smartspend_core",
                "bento_col_span": 6,
                "upvotes": 41,
                "is_ongoing": False,
                "order": 8,
            },
        ]
        for p in projects_data:
            Project.objects.create(**p)

    if CourseCertification.objects.count() == 0:
        courses_data = [
            (
                "Team Leader (Team 03) — Full-Stack Python & Django Internship",
                "BAIUST Computer Club (10th Executive Panel)",
                "2026",
                "https://github.com/Sakib20050413/baiust-campus-lost-and-found",
                "Led a 3-engineer team designing, building, and deploying full-stack Django web applications with production database architectures."
            ),
            (
                "Getting Started with Cisco Packet Tracer & Network Simulation",
                "Cisco Networking Academy (NetAcad)",
                "Oct 2026",
                "https://www.netacad.com/",
                "Completed practical network topology design, packet-level routing inspection, and IoT gateway simulation."
            ),
            (
                "ICT Fest Hackathon Preliminary — FastAPI & Docker Microservices",
                "ICT Fest Competitive Programming & Engineering",
                "2026",
                "https://github.com/Sakib20050413/ICT_Fest_Hackathon_Preliminary",
                "Engineered and containerized a multi-tenant coworking booking REST API using FastAPI, SQLAlchemy, JWT, and Docker."
            ),
            (
                "Applied Bio-Acoustic Machine Learning & Spectral Dataset Engineering",
                "Kaggle (`Wingbeats` & Oxford `HumBugDB` Audio Research)",
                "2026",
                "https://github.com/Sakib20050413/Bio-Acoustic-Mosquito-AI-Trap",
                "Conducted FFT spectral feature engineering and edge quantization on mosquito wingbeat audio datasets for real-time ESP32-S3 inference."
            ),
            (
                "CMST Dynamic Certificate Verification System & Online Portal",
                "Community Medicine Science & Technology (`cmst.com.bd`)",
                "2026",
                "https://github.com/Sakib20050413",
                "Architected an online diploma/certificate generator and QR/serial verification system."
            ),
            (
                "Internshala Student Partner (ISP) & Shortlisted AI/Robotics Specialist",
                "Internshala & Handshake (Uber AI Solutions)",
                "2026",
                "https://www.linkedin.com/in/md-najmus-sakib-rahatul-559a85285/",
                "Selected campus technology representative and shortlisted applicant for multimodal AI/robotics annotation."
            ),
        ]
        for idx, (t, iss, dt, url, take) in enumerate(courses_data, start=1):
            CourseCertification.objects.create(
                title=t, issuer=iss, completion_date=dt, credential_url=url, key_takeaways=take, order=idx
            )

    if TimelineEntry.objects.count() == 0:
        timeline_data = [
            (
                "AI/ML Systems Architect & Lead Developer — NexusLocal Research",
                "Independent AI/ML & Capstone Research",
                "2026 – Present",
                "Designing a local Master AI Orchestrator that routes ~1 GB quantized coding, RAG, and DSP models across CPU RAM, GPU VRAM, and NPU memory with in-place continual learning.",
                "~1 GB Modular Sub-Models"
            ),
            (
                "Team Leader (Team 03) — Full-Stack Django Internship",
                "BAIUST Computer Club",
                "May 2026 – Present",
                "Directed architecture, database modeling, and Vercel cloud deployment for the Campus Lost & Found automated matching platform.",
                "Live on Vercel"
            ),
            (
                "Lead Embedded AI & TinyML Developer — Team BlackBerry",
                "Dept. of CSE Research Group, BAIUST",
                "2026 – Present",
                "Engineered dual ESP32-S3 hardware-software systems: the 512-Point FFT Bio-Acoustic Mosquito AI Trap and the 3-Stream TinyML Rural Lightning Early Warning System.",
                "32 ms Edge FFT"
            ),
            (
                "B.Sc. in Computer Science & Engineering (CSE)",
                "Bangladesh Army International University of Science and Technology (BAIUST)",
                "Level 3, Term 2 -> Level 4 Capstone Track",
                "Focusing on Artificial Intelligence, Machine Learning, Deep Neural Architectures, Computer Networks, and Full-Stack Systems Engineering.",
                "AI/ML Track"
            ),
        ]
        for idx, (r, org, per, imp, bdg) in enumerate(timeline_data, start=1):
            TimelineEntry.objects.create(role=r, organization=org, period=per, impact_summary=imp, badge_metric=bdg, order=idx)


if __name__ == "__main__":
    run_seed()
    print("Seeded Sakib Portfolio V9.0 (Zero Videography, 100% Real AI/ML & Systems) successfully!")
