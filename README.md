# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **667**
- Today's entries: **395**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:10:02+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 34
- `Architecture`: 34
- `Backend`: 34
- `Databases`: 34
- `Frontend`: 34

### Recent Timeline

- `2026-05-01T09:10:02+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-01T09:10:01+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-01T09:10:00+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-01T09:09:59+08:00` | **Log with stable keys** (Observability)
- `2026-05-01T09:09:58+08:00` | **Design for idempotency** (APIs)
- `2026-05-01T09:09:57+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-01T09:09:56+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-01T09:09:55+08:00` | **Write one behavior per test** (Testing)
- `2026-05-01T09:09:54+08:00` | **Use virtual environments by default** (Python)
- `2026-05-01T09:09:53+08:00` | **Prefer small focused commits** (Git)
