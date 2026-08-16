# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2627**
- Today's entries: **18**
- Today's note: `notes/2026-08-16.md`

### Latest Entry

- Timestamp: `2026-08-16T17:25:52+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 132
- `Architecture`: 132
- `Backend`: 132
- `Databases`: 132
- `Frontend`: 132

### Recent Timeline

- `2026-08-16T17:25:52+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-16T17:11:07+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-16T16:57:49+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-16T16:43:10+08:00` | **Log with stable keys** (Observability)
- `2026-08-16T16:24:53+08:00` | **Design for idempotency** (APIs)
- `2026-08-16T15:54:09+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-16T14:47:13+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-16T14:09:49+08:00` | **Write one behavior per test** (Testing)
- `2026-08-16T13:54:18+08:00` | **Use virtual environments by default** (Python)
- `2026-08-16T12:44:52+08:00` | **Prefer small focused commits** (Git)
