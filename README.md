# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2429**
- Today's entries: **5**
- Today's note: `notes/2026-08-10.md`

### Latest Entry

- Timestamp: `2026-08-10T07:25:14+08:00`
- Title: **Name intent, not mechanics**
- Category: `Code Quality`
- Source: https://martinfowler.com/books/clean-code.html
- Summary: Readable names should communicate business intent so maintainers understand why code exists before how it works.

### Top Categories

- `APIs`: 122
- `Architecture`: 122
- `Backend`: 122
- `Code Quality`: 122
- `Databases`: 122

### Recent Timeline

- `2026-08-10T07:25:14+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-10T07:09:23+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-10T06:47:05+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-10T06:28:50+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-10T06:12:57+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-09T22:45:13+08:00` | **Log with stable keys** (Observability)
- `2026-08-09T22:25:47+08:00` | **Design for idempotency** (APIs)
- `2026-08-09T21:34:17+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-09T21:07:17+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-09T19:56:07+08:00` | **Write one behavior per test** (Testing)
