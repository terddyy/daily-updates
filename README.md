# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2887**
- Today's entries: **8**
- Today's note: `notes/2026-09-06.md`

### Latest Entry

- Timestamp: `2026-09-06T10:49:12+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 145
- `Architecture`: 145
- `Backend`: 145
- `Databases`: 145
- `Frontend`: 145

### Recent Timeline

- `2026-09-06T10:49:12+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-09-06T10:40:06+08:00` | **Optimize first contentful view** (Frontend)
- `2026-09-06T10:17:08+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-09-06T08:37:49+08:00` | **Log with stable keys** (Observability)
- `2026-09-06T06:48:01+08:00` | **Design for idempotency** (APIs)
- `2026-09-06T06:34:34+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-09-06T06:20:56+08:00` | **Rotate credentials on schedule** (Security)
- `2026-09-06T06:09:45+08:00` | **Write one behavior per test** (Testing)
- `2026-09-05T22:48:14+08:00` | **Use virtual environments by default** (Python)
- `2026-09-05T22:34:55+08:00` | **Prefer small focused commits** (Git)
