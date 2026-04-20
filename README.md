# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **87**
- Today's entries: **19**
- Today's note: `notes/2026-04-20.md`

### Latest Entry

- Timestamp: `2026-04-20T20:22:31+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 5
- `Architecture`: 5
- `Backend`: 5
- `Databases`: 5
- `Frontend`: 5

### Recent Timeline

- `2026-04-20T20:22:31+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-20T19:29:58+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-20T18:33:28+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-20T17:35:06+08:00` | **Log with stable keys** (Observability)
- `2026-04-20T16:43:59+08:00` | **Design for idempotency** (APIs)
- `2026-04-20T15:35:07+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-20T14:42:50+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-20T13:02:01+08:00` | **Write one behavior per test** (Testing)
- `2026-04-20T11:03:09+08:00` | **Use virtual environments by default** (Python)
- `2026-04-20T09:33:57+08:00` | **Prefer small focused commits** (Git)
