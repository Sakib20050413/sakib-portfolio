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
            site_name="Sakib // AI & Systems",
            full_name="Md Najmus Sakib Rahatul",
            role_title="AI/ML Engineer & Full-Stack AI Systems Architect",
            hero_headline="Engineering Sovereign Local Multi-Model AI Runtimes, Self-Evolving Neural Nodes & High-Scale Web Platforms.",
            bio_summary=(
                "AI/ML Engineer and Full-Stack Systems Builder focused on Large Language Models, "
                "Multimodal AI orchestration, Edge TinyML, and resilient web platforms. My flagship research "
                "architects a locally resident Master AI Orchestrator across PC and mobile memory pools "
                "(CPU System RAM, GPU VRAM, and NPU) that dynamically queues ~1 GB specialized micro-models "
                "for code, image, and video synthesis while executing in-place single-node continual self-training."
            ),
            photo_url="https://avatars.githubusercontent.com/u/166808901?v=4",
            location="Cumilla / Dhaka, Bangladesh (UTC+6)",
            availability_text="Open to AI/ML Engineering Roles, Global Remote Contracts & Research",
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

    if AIArchitectureNode.objects.count() == 0:
        nodes = [
            (
                "MASTER-00",
                "Always-Resident Master AI Router & Prompt Dispatcher",
                "~420 MB Resident in Unified RAM",
                "CPU System RAM + NPU Control Plane",
                "Lightweight persistent orchestrator that parses user intent, decomposes multi-step tasks, and manages unified memory paging across PC and mobile hardware.",
                "Eliminates cloud API latency and token costs by maintaining a persistent local control graph that dynamically hot-swaps specialist sub-models into active memory."
            ),
            (
                "EXPERT-CODE-1G",
                "Code-1G Specialist Sub-Model (Frontier Coding & AST Synthesis)",
                "~0.95 GB (4-Bit NF4 / GGUF Quantized)",
                "GPU VRAM / Unified CPU+NPU Memory",
                "On-demand coding and architecture specialist model loaded into RAM/VRAM when software engineering or debugging prompts arrive.",
                "Combines 4-bit NF4 quantization with AST-verified speculative decoding and Master-Router synthesis to deliver Claude/GPT-tier coding precision within a 1 GB memory envelope."
            ),
            (
                "EXPERT-PHOTO-1G",
                "Vision-Photo-1G Specialist Sub-Model (Local Image Synthesis)",
                "~1.05 GB (Latent Consistency / 4-Step Flow)",
                "GPU VRAM + NPU Tensor Cores",
                "Compact diffusion/flow-matching image generator queued into memory on demand for photorealistic and UI asset synthesis.",
                "Uses latent consistency distillation and INT8/FP16 mixed-precision attention to synthesize high-resolution images locally without cloud GPUs."
            ),
            (
                "EXPERT-VIDEO-1G",
                "Motion-Video-1G Specialist Sub-Model (Temporal Video Synthesis)",
                "~1.15 GB (Temporal Adapter + Keyframe VAE)",
                "GPU VRAM + System RAM Ring Buffer",
                "Specialized temporal motion sub-model loaded dynamically when short video generation or frame interpolation is requested.",
                "Streams latent keyframes through a sliced temporal attention window so consumer laptops and mobile devices can render video clips without OOM crashes."
            ),
            (
                "CONTINUAL-NODE",
                "In-Place Self-Evolving Single-Node Continual Learning Engine",
                "Zero Extra Node Proliferation (In-Place Delta Merge)",
                "Persistent Neural Knowledge Graph in Local Storage + RAM",
                "Autonomous self-training mechanism that refines and expands existing neural knowledge nodes in place rather than spawning duplicate checkpoints.",
                "Applies low-rank continual weight consolidation (LoRA Delta Merging + Elastic Weight Consolidation) directly inside the active node so the AI evolves continuously with zero external resource bloat."
            ),
        ]
        for idx, (nid, title, mem, hw, summ, mech) in enumerate(nodes, start=1):
            AIArchitectureNode.objects.create(
                node_id=nid, title=title, memory_budget=mem, hardware_pool=hw,
                summary=summ, mechanism_detail=mech, order=idx
            )

    if Skill.objects.count() == 0:
        skills_data = [
            ("PyTorch & PyTorch Lightning", "LLM_CORE", 95, "Core AI Stack"),
            ("Transformer Architectures (Llama, Qwen, Mistral, ViT)", "LLM_CORE", 94, "Deep Learning"),
            ("LoRA, QLoRA & PEFT Fine-Tuning", "LLM_CORE", 93, "Model Adaptation"),
            ("In-Place Continual Learning & LoRA Weight Merging", "LLM_CORE", 92, "Self-Evolving AI"),
            ("RLHF, DPO & GRPO Preference Alignment", "LLM_CORE", 90, "Alignment"),
            ("Hugging Face Ecosystem (Transformers, TRL, Datasets)", "LLM_CORE", 95, "Core AI Stack"),
            ("4-Bit NF4, INT8, GGUF, AWQ & GPTQ Quantization", "LOCAL_RUNTIME", 94, "Memory Compression"),
            ("llama.cpp, vLLM & ONNX Runtime Local Inference", "LOCAL_RUNTIME", 93, "Edge/PC Runtime"),
            ("CPU RAM + GPU VRAM + NPU Dynamic Memory Orchestration", "LOCAL_RUNTIME", 95, "Flagship Thesis"),
            ("ExecuTorch, WebGPU & Mobile NPU Deployment", "LOCAL_RUNTIME", 91, "Cross-Device AI"),
            ("Sub-1GB Micro-Model Knowledge Distillation", "LOCAL_RUNTIME", 92, "Model Compression"),
            ("Speculative Decoding & KV-Cache Paging", "LOCAL_RUNTIME", 90, "Low-Latency LLM"),
            ("Master-Worker Multi-Model Orchestration (LangGraph / MCP)", "MULTIMODAL_AGENTS", 95, "Agentic Core"),
            ("Vision-Language Models (VLMs) & Multimodal Reasoning", "MULTIMODAL_AGENTS", 93, "Multimodal AI"),
            ("Latent Diffusion & Flow-Matching (Image & Video Synthesis)", "MULTIMODAL_AGENTS", 91, "Generative Media"),
            ("Hybrid Vector + BM25 RAG & Cross-Encoder Reranking", "MULTIMODAL_AGENTS", 94, "Retrieval"),
            ("Autonomous Tool Execution & Sandbox Code Agents", "MULTIMODAL_AGENTS", 94, "Agentic Systems"),
            ("Scikit-Learn, XGBoost, LightGBM & SHAP Explainability", "MULTIMODAL_AGENTS", 93, "Classical ML"),
            ("TensorFlow Lite Micro & Int8 Edge Neural Inference", "EDGE_TINYML", 95, "Embedded AI"),
            ("ESP32-S3 Dual-Core 240MHz & PIE Vector Instructions", "EDGE_TINYML", 96, "Hardware AI"),
            ("512-Point Radix-2 FFT Bio-Acoustic Signal Processing", "EDGE_TINYML", 96, "32ms Real-Time DSP"),
            ("Multi-Stream Sensor Fusion (I2S, I2C, SPI, UART, GSM)", "EDGE_TINYML", 94, "IoT Systems"),
            ("Kaggle Dataset Engineering (HumBugDB & Wingbeats)", "EDGE_TINYML", 94, "Audio ML"),
            ("MATLAB Signal Modulation & Spectral Analysis", "EDGE_TINYML", 92, "DSP"),
            ("Python 3.12 & Asynchronous Systems Programming", "FULLSTACK_WEB", 96, "Primary Language"),
            ("Django 5 (ORM, Custom Admin CMS, Auth, REST APIs)", "FULLSTACK_WEB", 96, "Team Leader"),
            ("FastAPI (Async AI Inference Microservices & JWT Auth)", "FULLSTACK_WEB", 94, "AI Backend"),
            ("Next.js 15, React & TypeScript", "FULLSTACK_WEB", 93, "Modern Frontend"),
            ("JavaScript (ES6+), DOM Manipulation & Three.js WebGL", "FULLSTACK_WEB", 94, "Interactive 3D"),
            ("HTML5, CSS3, Tailwind CSS, Bootstrap 5 & PHP/MySQLi", "FULLSTACK_WEB", 95, "Web Core"),
            ("PostgreSQL (Neon, Supabase & pgvector)", "CLOUD_DATA", 94, "Production DB"),
            ("Prisma ORM, SQLAlchemy & Relational Schema Design", "CLOUD_DATA", 93, "Data Layer"),
            ("Docker, Docker Compose & Containerized Microservices", "CLOUD_DATA", 92, "DevOps"),
            ("Vercel & Render Cloud Deployment Pipelines", "CLOUD_DATA", 95, "Live Cloud"),
            ("C, C++ (STL/OOP) & Java Desktop Systems", "CLOUD_DATA", 93, "Systems Core"),
            ("Git, GitHub Actions & Linux CLI Automation", "CLOUD_DATA", 95, "Version Control"),
        ]
        for idx, (name, dom, prof, tag) in enumerate(skills_data, start=1):
            Skill.objects.create(name=name, domain=dom, proficiency=prof, highlight_tag=tag, order=idx)

    if Project.objects.count() == 0:
        projects_data = [
            {
                "code": "01",
                "title": "NexusLocal — Sovereign Local Master AI Orchestrator & Self-Training Neural Engine",
                "slug": "nexuslocal-master-ai-orchestrator",
                "category": "AI_LLM",
                "status_label": "Flagship R&D & Capstone System",
                "tagline": "Always-resident local Master AI that dynamically routes ~1 GB coding, photo, and video sub-models across CPU RAM, GPU VRAM, and NPU memory with in-place single-node continual self-training.",
                "description": (
                    "Designed to run 100% locally on consumer PCs and mobile devices without cloud API lock-in. "
                    "A lightweight Master AI Router stays resident in system RAM and dynamically queues specialized ~1 GB "
                    "4-bit quantized sub-models (Code-1G, Photo-1G, Video-1G, Reason-1G) on demand while updating its own "
                    "persistent neural node in place rather than spawning redundant checkpoints."
                ),
                "architecture_breakdown": (
                    "1. Resident Control Plane (~420 MB RAM): Intent parser + unified CPU/GPU/NPU memory pager.\n"
                    "2. On-Demand ~1 GB Expert Queue: Hot-swaps GGUF/NF4 quantized models in <400ms.\n"
                    "3. In-Place Self-Evolving Node: Applies continual LoRA delta merging and Elastic Weight Consolidation inside a single persistent neural graph."
                ),
                "tech_stack_csv": "PyTorch, 4-Bit NF4 QLoRA, llama.cpp / ONNX, CPU/GPU/NPU Pager, Continual Self-Training, FastAPI",
                "live_server_url": "",
                "github_repo_url": "https://github.com/Sakib20050413",
                "bento_col_span": 7,
                "upvotes": 64,
                "is_ongoing": True,
                "order": 1,
            },
            {
                "code": "02",
                "title": "Aloron Shop — Next.js, TypeScript & Prisma Full-Stack E-Commerce Platform",
                "slug": "aloron-shop-nextjs-ecommerce",
                "category": "FULLSTACK",
                "status_label": "Live on Vercel",
                "tagline": "Ground-zero full-stack e-commerce rebuild featuring Next.js App Router, TypeScript, Prisma ORM, pure JWT authentication, dynamic CMS, and unified reactive cart state.",
                "description": (
                    "Production e-commerce platform engineered with Next.js and TypeScript (98.9%). Includes a custom "
                    "dynamic CMS for catalog and banner management, pure JWT session security, Prisma ORM relational "
                    "queries, and automated testing."
                ),
                "architecture_breakdown": (
                    "1. Frontend & SSR: Next.js App Router + TypeScript + Tailwind CSS.\n"
                    "2. Data & Auth Layer: Prisma ORM + Pure JWT token rotation (`auth.ts`).\n"
                    "3. Cloud Edge Deployment: Live production hosting on Vercel (`aloron-shop.vercel.app`)."
                ),
                "tech_stack_csv": "Next.js, TypeScript, Prisma ORM, Pure JWT Auth, Dynamic CMS, Tailwind CSS, Vercel",
                "live_server_url": "https://aloron-shop.vercel.app",
                "github_repo_url": "https://github.com/Sakib20050413/aloron-shop",
                "bento_col_span": 5,
                "upvotes": 48,
                "is_ongoing": False,
                "order": 2,
            },
            {
                "code": "03",
                "title": "Campus Lost & Found — Automated Multi-Factor Matching Web Platform",
                "slug": "baiust-campus-lost-and-found",
                "category": "FULLSTACK",
                "status_label": "Live on Vercel",
                "tagline": "Automated item recovery platform powered by a 0–100% multi-factor similarity scoring algorithm (`items/matching.py`) and secret-mark verification workflow.",
                "description": (
                    "Full-stack Django platform deployed live on Vercel that automates lost and found item matching. "
                    "Computes weighted similarity scores across category (30%), campus zone (25%), date proximity (15%), "
                    "and keyword overlap (30%), paired with a multi-stage claim review pipeline."
                ),
                "architecture_breakdown": (
                    "1. Matching Engine (`items/matching.py`): 4-factor weighted similarity scorer.\n"
                    "2. Verification Pipeline (`claims/`): Hidden ownership verification + staff audit dashboard.\n"
                    "3. Serverless WSGI Deployment: Live on Vercel (`baiust-campus-lost-and-found.vercel.app`)."
                ),
                "tech_stack_csv": "Python, Django 5, Multi-Factor Matching Algorithm, PostgreSQL / SQLite, Bootstrap 5, Vercel",
                "live_server_url": "https://baiust-campus-lost-and-found.vercel.app",
                "github_repo_url": "https://github.com/Sakib20050413/baiust-campus-lost-and-found",
                "bento_col_span": 6,
                "upvotes": 53,
                "is_ongoing": False,
                "order": 3,
            },
            {
                "code": "04",
                "title": "NexusCode AI — Polyglot Bite-Sized Coding & 3D Simulation Platform",
                "slug": "nexuscode-ai-3d-coding-platform",
                "category": "AI_LLM",
                "status_label": "Live on Vercel",
                "tagline": "Minimalist LLM-style interactive programming and empirical telemetry platform across 12 languages with 45-second Flash Notes and reactive 3D simulation.",
                "description": (
                    "Full-stack interactive coding and research telemetry platform replacing 2.5-hour video lectures with "
                    "45-second Feynman mental models, 30-second micro-tasks, and a 60 FPS 3D Cyber-Rover, DOM Hologram, "
                    "and SQL Data-Vault simulation engine."
                ),
                "architecture_breakdown": (
                    "1. Polyglot AST & Loop Sandbox: Deterministic in-browser compiler across 12 languages.\n"
                    "2. 3D Simulation Engine: 18-part articulated 3D Rover + DOM/SQL visual stage.\n"
                    "3. IEEE Research Telemetry: Tracks Time-to-Comprehension (TTC) and exports CSV/JSON datasets."
                ),
                "tech_stack_csv": "Django 5, Three.js / 3D Canvas, JavaScript ES6+ AST, 12 Languages, Research Telemetry, Vercel",
                "live_server_url": "https://codequest-bd.vercel.app",
                "github_repo_url": "https://github.com/Sakib20050413/codequest-bd",
                "bento_col_span": 6,
                "upvotes": 58,
                "is_ongoing": False,
                "order": 4,
            },
            {
                "code": "05",
                "title": "Bio-Acoustic Mosquito Vector AI Trap (`ESP32-S3 TinyML & 512-Pt FFT`)",
                "slug": "bio-acoustic-mosquito-ai-trap",
                "category": "EDGE_TINYML",
                "status_label": "Hardware + Edge AI Repo",
                "tagline": "32 ms real-time acoustic wingbeat classifier on ESP32-S3 separating female Aedes/Anopheles vectors (350–600 Hz) from beneficial pollinators (100–250 Hz).",
                "description": (
                    "Edge AI and digital signal processing system utilizing an INMP441 I2S digital microphone, "
                    "Hann-windowed 512-point Radix-2 FFT at 16 kHz, and Kaggle Wingbeats / Oxford HumBugDB spectral "
                    "profiles to trigger selective high-speed PWM MOSFET suction only on disease vectors."
                ),
                "architecture_breakdown": (
                    "1. I2S DMA Audio Capture: INMP441 at 16 kHz -> 512-sample frame (32 ms window, 31.25 Hz bin width).\n"
                    "2. Harmonic Classifier: Isolates female vector fundamental frequencies (350–600 Hz) while sparing bees.\n"
                    "3. Web Telemetry Dashboard: Real-time species counter and spectral monitor."
                ),
                "tech_stack_csv": "ESP32-S3, C++, Python, 512-Pt Radix-2 FFT, INMP441 I2S, Kaggle Wingbeats & HumBugDB, Web Dashboard",
                "live_server_url": "",
                "github_repo_url": "https://github.com/Sakib20050413/Bio-Acoustic-Mosquito-AI-Trap",
                "bento_col_span": 4,
                "upvotes": 49,
                "is_ongoing": False,
                "order": 5,
            },
            {
                "code": "06",
                "title": "IoT 3-Stream TinyML Rural Lightning Early Warning System + Web GIS",
                "slug": "iot-rural-lightning-early-warning-system",
                "category": "EDGE_TINYML",
                "status_label": "Hardware + Web GIS Repo",
                "tagline": "3-stream TinyML storm nowcasting node combining AS3935 500 kHz RF sensing, sky IR thermometry, and SIM800L cellular telemetry with a live Web GIS map.",
                "description": (
                    "Cross-verifies local atmospheric readings (AS3935 RF strike distance 1–40 km, BMP280 pressure drop, "
                    "BH1750 lux, MLX90614 sky IR temperature) with cellular weather API telemetry over SIM800L GSM to "
                    "eliminate false alarms and trigger 3-zone visual/audio evacuation alerts."
                ),
                "architecture_breakdown": (
                    "1. Stream 1 (Local Sky & Barometric Array): BH1750 + MLX90614 + BMP280 + DHT22.\n"
                    "2. Stream 2 (RF Lightning Detector): AS3935 500 kHz strike distance estimator.\n"
                    "3. Stream 3 (Cellular GIS Sync): SIM800L GSM/GPRS pushing live coordinates to the Web GIS dashboard."
                ),
                "tech_stack_csv": "ESP32-S3, TinyML Sensor Fusion, AS3935 RF, SIM800L GSM, Leaflet Web GIS, C++, HTML/JS",
                "live_server_url": "",
                "github_repo_url": "https://github.com/Sakib20050413/IoT-Rural-Lightning-Early-Warning-System",
                "bento_col_span": 4,
                "upvotes": 44,
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
                    "Built for the ICT Fest Hackathon Preliminary. Implements strict multi-tenant organization isolation, "
                    "role-based access control (Admin, Staff, Member), automated booking conflict detection, and "
                    "1-command Docker Compose deployment."
                ),
                "architecture_breakdown": (
                    "1. API Layer: Python 3.11 + FastAPI + Pydantic v2 validation.\n"
                    "2. Auth & ORM: JWT access/refresh tokens (HS256) + SQLAlchemy ORM.\n"
                    "3. Containerization: Production `Dockerfile` + `docker-compose.yml`."
                ),
                "tech_stack_csv": "Python 3.11, FastAPI, SQLAlchemy, JWT Auth, Docker, Docker Compose, Pytest",
                "live_server_url": "",
                "github_repo_url": "https://github.com/Sakib20050413/ICT_Fest_Hackathon_Preliminary",
                "bento_col_span": 4,
                "upvotes": 39,
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
                    "1. SmartSpend (`smartspend_core`): Finance app with category analytics and budget alerts.\n"
                    "2. Library Management System: Book inventory, member borrowing ledger, and fine calculation."
                ),
                "tech_stack_csv": "Python, Django, Relational DB, Chart.js, HTML5/CSS3, Git",
                "live_server_url": "",
                "github_repo_url": "https://github.com/Sakib20050413/smartspend_core",
                "bento_col_span": 12,
                "upvotes": 35,
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
                "Selected campus technology representative and shortlisted applicant for multimodal AI/robotics video annotation."
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
                "Designing a local Master AI Orchestrator that routes ~1 GB quantized coding, image, and video models across CPU RAM, GPU VRAM, and NPU memory with in-place single-node continual self-training.",
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
    print("Seeded Sakib Portfolio V7.0 successfully!")
