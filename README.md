# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2607**
- Today's entries: **36**
- Today's note: `notes/2026-08-15.md`

### Latest Entry

- Timestamp: `2026-08-15T22:23:52+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 131
- `Architecture`: 131
- `Backend`: 131
- `Databases`: 131
- `Frontend`: 131

### Recent Timeline

- `2026-08-15T22:23:52+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-15T22:06:32+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-15T21:43:54+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-15T21:28:48+08:00` | **Log with stable keys** (Observability)
- `2026-08-15T21:13:03+08:00` | **Design for idempotency** (APIs)
- `2026-08-15T20:06:50+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-15T19:50:53+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-15T19:37:12+08:00` | **Write one behavior per test** (Testing)
- `2026-08-15T18:51:49+08:00` | **Use virtual environments by default** (Python)
- `2026-08-15T18:39:25+08:00` | **Prefer small focused commits** (Git)
