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
| Database | PostgreSQL 16 |
| ORM / Migrations | SQLAlchemy + Alembic |
| Job sources | Infojobs API (multi-connector architecture) |
| AI extraction | Gemini 1.5 Flash |
| Authentication | JWT (python-jose + passlib/bcrypt) |
| Scheduler | APScheduler |
| Notifications | SMTP Email |
| Frontend | React |
| Deploy | Railway |
| CI/CD | GitHub Actions |

---

## Database Design

Meraki uses a relational PostgreSQL database with 10 tables designed around the core concept of gap analysis between a user's current stack and market demand.

**Core tables:** `users`, `rol`, `global_stack`, `personal_stack`, `offer`, `resource`

**Junction tables (N:M relationships):** `rol_stack`, `offer_stack`, `resource_stack`

```
users ──< personal_stack >── global_stack ──< rol_stack >── rol
                                    │                         │
                              offer_stack ──────────────── offer
                                    │
                             resource_stack >── resource
```

Key design decisions:
- `global_stack` stores market-wide technologies, separate from `personal_stack` which tracks each user's skills and self-assessed level
- `offer.rol_id` references a normalized `rol` table — raw job titles are mapped to standard roles by Gemini during ingestion, enabling clean market statistics
- Users can define multiple target roles (1:N), each mapped to the technologies the market requires
- Schema versioned and managed with Alembic migrations

---

## Authentication

Meraki implements stateless authentication using JWT, following the standard OAuth2 password bearer flow.

```
register → password hashed (bcrypt) → stored in DB
   ↓
login → password verified → JWT issued (signed, expires in 30 min)
   ↓
protected route → middleware decodes JWT → loads user → grants access
```

- Passwords are never stored in plain text (`passlib` + `bcrypt`)
- Tokens are signed with a secret key and validated on every protected request
- `get_current_user` dependency (in `api/deps.py`) centralizes auth logic so any route can be protected with a single line:

```python
@router.get("/me", response_model=UserResponse)
def get_my_profile(current_user: User = Depends(get_current_user)):
    return current_user
```

---

## Project Structure

```
Meraki/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/        # auth, users, roles, stack, offers
│   │   │   └── deps.py        # get_db, get_current_user
│   │   ├── core/              # config, security, database
│   │   ├── models/            # user, rol, global_stack, personal_stack, offer, resource
│   │   ├── schemas/           # Pydantic models
│   │   ├── services/
│   │   │   └── connectors/    # base, infojobs (extensible)
│   │   └── scheduler/         # APScheduler tasks
│   ├── migrations/            # Alembic
│   ├── requirements.txt
│   └── tests/
├── frontend/
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## Getting Started

### Requirements
- Docker Desktop
- Python 3.11+
- Node.js 18+

### 1. Clone the repo

```bash
git clone https://github.com/yuna-espejo/Meraki.git
cd Meraki
```

### 2. Set up environment variables

```bash
cp .env.example .env
```

Fill in your values in `.env`:

```
DATABASE_URL=postgresql://user:password@localhost:5432/meraki
SECRET_JWT=your-secret-key
ALG_JWT=HS256
EXPIRE_MIN_JWT=30
```

### 3. Run the database

```bash
docker-compose up -d
```

### 4. Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
alembic upgrade head
```

### 6. Start the server

```bash
uvicorn app.main:app --reload
```

### 7. Explore the API

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Auth

| Method | Endpoint | Auth required | Description |
|--------|----------|----------------|-------------|
| POST | `/auth/register` | No | Register a new user |
| POST | `/auth/login` | No | Authenticate and receive a JWT |
| GET | `/auth/me` | Yes | Get the authenticated user's profile |

---

## Development Plan

| Sprint | Focus |
|--------|-------|
| S1 | Project structure · Docker · PostgreSQL · database models · Alembic ✅ |
| S2 | Auth: register · login · JWT middleware ✅ |
| S3 | User profile: current stack · target role |
| S4 | Infojobs connector · multi-connector architecture |
| S5 | AI extraction with Gemini · offer text → structured JSON |
| S6 | Market analysis engine · gap analysis · stats |
| S7 | Learning center · resources mapped to gaps |
| S8 | React frontend · dashboard · roadmap · resources |
| S9 | Deploy · GitHub Actions CI/CD · technical README |

---

## Current Progress

- [x] Project structure and Docker setup
- [x] PostgreSQL running via Docker Compose
- [x] Database models designed and implemented (10 tables)
- [x] Alembic migrations configured and applied
- [x] User registration with hashed passwords
- [x] Login with JWT token generation
- [x] JWT middleware protecting routes (`get_current_user`)
- [ ] User profile and stack definition
- [ ] Infojobs connector
- [ ] AI extraction with Gemini
- [ ] Market analysis engine
- [ ] Learning center
- [ ] React frontend
- [ ] Deploy

---

## Author

**Yuna Espejo** — Junior Consultant @ Timestamp Group  
[yunaespejo.com](https://yunaespejo.com) · [GitHub](https://github.com/yuna-espejo)