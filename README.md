# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2147**
- Today's entries: **12**
- Today's note: `notes/2026-07-16.md`

### Latest Entry

- Timestamp: `2026-07-16T15:05:52+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 108
- `Architecture`: 108
- `Backend`: 108
- `Databases`: 108
- `Frontend`: 108

### Recent Timeline

- `2026-07-16T15:05:52+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-16T14:03:29+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-16T13:04:50+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-16T11:50:15+08:00` | **Log with stable keys** (Observability)
- `2026-07-16T10:39:33+08:00` | **Design for idempotency** (APIs)
- `2026-07-16T09:36:32+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-16T08:50:59+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-16T08:06:27+08:00` | **Write one behavior per test** (Testing)
- `2026-07-16T07:35:30+08:00` | **Use virtual environments by default** (Python)
- `2026-07-16T07:07:09+08:00` | **Prefer small focused commits** (Git)
