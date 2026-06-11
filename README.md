# Meraki 🧭

> **Status: Work in Progress** — actively in development.

A career intelligence tool for developers. You define your current stack and target role — Meraki analyzes the real job market, extracts patterns from hundreds of actual job postings, and gives you a clear picture of what you need to learn and how to get there.

Not generic roadmaps. Real data, right now.

---

## The Problem

Every developer knows the feeling: you want to level up or switch roles, but the advice you find is either too generic ("learn Python!") or too old ("top skills for 2024"). Nobody tells you what companies in your city are actually hiring for, at what level, and how far you are from being hireable.

Meraki fills that gap. It scrapes real job postings, extracts the stack they require, and maps it against your current profile — so you know exactly what to learn next.

---

## How It Works

1. **You define your profile** — current stack, skill levels, and target role (e.g. Backend Engineer, Data Engineer)
2. **Meraki analyzes the market** — scrapes real postings from Infojobs and extracts structured data with AI
3. **You see the gap** — which technologies the market demands vs what you already know
4. **You get a learning path** — curated resources (courses, certifications, docs) mapped to your exact gaps
5. **The data stays fresh** — the scheduler runs automatically so market stats are always up to date

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + FastAPI |
| Database | PostgreSQL |
| Job sources | Infojobs API (multi-connector architecture) |
| AI extraction | Gemini 1.5 Flash |
| Authentication | JWT |
| Scheduler | APScheduler |
| Notifications | SMTP Email |
| Frontend | React |
| Deploy | Railway |
| CI/CD | GitHub Actions |

---

## Project Structure

```
Meraki/
├── backend/
│   ├── app/
│   │   ├── api/routes/        # auth, users, roles, stack, offers
│   │   ├── core/              # config, security, database
│   │   ├── models/            # user, rol, global_stack, personal_stack, offert, resource
│   │   ├── schemas/           # Pydantic models
│   │   ├── services/
│   │   │   └── connectors/    # base, infojobs (extensible)
│   │   └── scheduler/         # APScheduler tasks
│   ├── migrations/            # Alembic
│   └── tests/
├── frontend/
├── docker-compose.yml
└── README.md
```

---

## Getting Started

### Requirements
- Docker Desktop
- Python 3.11+
- Node.js 18+

### Run the database

```bash
docker-compose up -d
```

### Verify connection

```bash
docker exec -it postgres_db psql -U your_user -d meraki
```

---

## Development Plan

| Week | Focus |
|------|-------|
| S1 | Project structure · Docker · PostgreSQL ✅ |
| S2 | Database models · Alembic migrations |
| S3 | Auth: register · login · JWT middleware |
| S4 | Infojobs connector · multi-connector architecture |
| S5 | AI extraction with Gemini · offer text → structured JSON |
| S6 | Market analysis engine · gap analysis · stats |
| S7 | Learning center · resources mapped to gaps |
| S8 | React frontend · dashboard · roadmap |
| S9 | Deploy · GitHub Actions CI/CD · technical README |

---

## Current Progress

- [x] Project structure and Docker setup
- [x] PostgreSQL running via Docker Compose
- [ ] Database models and migrations
- [ ] Authentication
- [ ] Infojobs connector
- [ ] AI extraction
- [ ] Market analysis
- [ ] Learning center
- [ ] Frontend
- [ ] Deploy

---

## Author

**Yuna Espejo** — Junior Consultant @ Timestamp Group  
[yunaespejo.com](https://yunaespejo.com) · [GitHub](https://github.com/yuna-espejo)