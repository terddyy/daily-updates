# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2807**
- Today's entries: **18**
- Today's note: `notes/2026-08-24.md`

### Latest Entry

- Timestamp: `2026-08-24T20:55:27+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 141
- `Architecture`: 141
- `Backend`: 141
- `Databases`: 141
- `Frontend`: 141

### Recent Timeline

- `2026-08-24T20:55:27+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-24T19:56:19+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-24T19:28:00+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-24T18:53:07+08:00` | **Log with stable keys** (Observability)
- `2026-08-24T18:03:30+08:00` | **Design for idempotency** (APIs)
- `2026-08-24T17:04:18+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-24T16:10:33+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-24T15:20:14+08:00` | **Write one behavior per test** (Testing)
- `2026-08-24T14:03:08+08:00` | **Use virtual environments by default** (Python)
- `2026-08-24T13:24:58+08:00` | **Prefer small focused commits** (Git)
