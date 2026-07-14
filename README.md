# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2107**
- Today's entries: **16**
- Today's note: `notes/2026-07-14.md`

### Latest Entry

- Timestamp: `2026-07-14T18:09:52+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 106
- `Architecture`: 106
- `Backend`: 106
- `Databases`: 106
- `Frontend`: 106

### Recent Timeline

- `2026-07-14T18:09:52+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-14T17:16:45+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-14T16:29:49+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-14T15:36:52+08:00` | **Log with stable keys** (Observability)
- `2026-07-14T14:54:54+08:00` | **Design for idempotency** (APIs)
- `2026-07-14T13:58:55+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-14T13:02:45+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-14T11:47:34+08:00` | **Write one behavior per test** (Testing)
- `2026-07-14T10:39:05+08:00` | **Use virtual environments by default** (Python)
- `2026-07-14T09:36:00+08:00` | **Prefer small focused commits** (Git)
