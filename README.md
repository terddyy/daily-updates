# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2027**
- Today's entries: **3**
- Today's note: `notes/2026-07-10.md`

### Latest Entry

- Timestamp: `2026-07-10T07:41:43+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 102
- `Architecture`: 102
- `Backend`: 102
- `Databases`: 102
- `Frontend`: 102

### Recent Timeline

- `2026-07-10T07:41:43+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-10T07:09:53+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-10T06:32:26+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-09T22:44:51+08:00` | **Log with stable keys** (Observability)
- `2026-07-09T21:42:51+08:00` | **Design for idempotency** (APIs)
- `2026-07-09T19:44:35+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-09T18:42:07+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-09T17:35:47+08:00` | **Write one behavior per test** (Testing)
- `2026-07-09T16:18:38+08:00` | **Use virtual environments by default** (Python)
- `2026-07-09T14:57:54+08:00` | **Prefer small focused commits** (Git)
