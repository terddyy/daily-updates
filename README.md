# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2447**
- Today's entries: **23**
- Today's note: `notes/2026-08-10.md`

### Latest Entry

- Timestamp: `2026-08-10T18:56:30+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 123
- `Architecture`: 123
- `Backend`: 123
- `Databases`: 123
- `Frontend`: 123

### Recent Timeline

- `2026-08-10T18:56:30+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-10T18:30:09+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-10T17:47:39+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-10T17:10:51+08:00` | **Log with stable keys** (Observability)
- `2026-08-10T16:35:03+08:00` | **Design for idempotency** (APIs)
- `2026-08-10T15:54:37+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-10T15:11:13+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-10T14:33:01+08:00` | **Write one behavior per test** (Testing)
- `2026-08-10T13:45:20+08:00` | **Use virtual environments by default** (Python)
- `2026-08-10T13:03:14+08:00` | **Prefer small focused commits** (Git)
