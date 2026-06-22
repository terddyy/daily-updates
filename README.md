# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1767**
- Today's entries: **1**
- Today's note: `notes/2026-06-23.md`

### Latest Entry

- Timestamp: `2026-06-23T06:13:21+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 89
- `Architecture`: 89
- `Backend`: 89
- `Databases`: 89
- `Frontend`: 89

### Recent Timeline

- `2026-06-23T06:13:21+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-22T21:40:10+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-22T19:40:56+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-22T17:30:59+08:00` | **Log with stable keys** (Observability)
- `2026-06-22T15:18:25+08:00` | **Design for idempotency** (APIs)
- `2026-06-22T13:18:34+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-22T11:26:40+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-22T10:05:52+08:00` | **Write one behavior per test** (Testing)
- `2026-06-22T09:02:08+08:00` | **Use virtual environments by default** (Python)
- `2026-06-22T07:47:09+08:00` | **Prefer small focused commits** (Git)
