# JobRadar 🎯

> **Status: Work in Progress** — actively in development.

A personalized job aggregator that monitors job boards automatically, extracts the real tech stack from each offer using AI, and presents everything in a filterable catalog. Multi-user: each person defines their own search parameters and gets their own feed.

---

## The Problem

Job searching is noisy. You open LinkedIn, Infojobs, or any job board and get flooded with offers that don't match — wrong seniority, wrong stack, wrong location. You end up reading dozens of descriptions manually just to find three relevant ones.

JobRadar does the filtering for you. Define your keywords, location, max experience, and words to exclude — the system runs searches automatically, analyzes each offer with AI, and only shows you what actually fits.

---

## How It Works

1. **You define your search parameters** — keywords, location, max years of experience, salary floor, words to exclude
2. **The scheduler runs searches automatically** — every few hours, per user
3. **AI extracts structured data** — tech stack, seniority level, salary, remote/on-site
4. **Your catalog updates** — new matching offers appear, you get an email notification
5. **You manage your pipeline** — mark offers as saved, applied, or discarded

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
JobRadar/
├── backend/
│   ├── app/
│   │   ├── api/routes/        # auth, users, searches, jobs
│   │   ├── core/              # config, security, database
│   │   ├── models/            # user, search, job, job_status
│   │   ├── schemas/           # Pydantic models
│   │   ├── services/
│   │   │   └── connectors/    # base, infojobs (extensible)
│   │   └── scheduler/         # APScheduler tasks
│   ├── migrations/            # Alembic
│   └── tests/
├── frontend/
├── docker-compose.yml
└── README.md

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
docker exec -it postgres_db psql -U your_user -d jobradar
```

---

## Development Plan

| Week | Focus |
|------|-------|
| S1 | Project structure · Docker · database models · Alembic |
| S2 | Auth: register · login · JWT middleware |
| S3 | Infojobs connector · multi-connector architecture · deduplication |
| S4 | AI extraction with Gemini · job text → structured JSON |
| S5 | Full REST API · filters · pagination · tests |
| S6 | Scheduler · email notifications per user |
| S7 | React frontend · catalog · filters · job status |
| S8 | Deploy · GitHub Actions CI/CD · technical README |

---

## Current Progress

- [x] Project structure and Docker setup
- [x] PostgreSQL running via Docker Compose
- [ ] Database models and migrations
- [ ] Authentication
- [ ] Infojobs connector
- [ ] AI extraction
- [ ] REST API
- [ ] Frontend
- [ ] Deploy

---

## Author

**Yuna Espejo** — Junior Consultant @ Timestamp Group  
[GitHub](https://github.com/yuna-espejo)