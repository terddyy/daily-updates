# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2349**
- Today's entries: **3**
- Today's note: `notes/2026-08-07.md`

### Latest Entry

- Timestamp: `2026-08-07T09:34:55+08:00`
- Title: **Name intent, not mechanics**
- Category: `Code Quality`
- Source: https://martinfowler.com/books/clean-code.html
- Summary: Readable names should communicate business intent so maintainers understand why code exists before how it works.

### Top Categories

- `APIs`: 118
- `Architecture`: 118
- `Backend`: 118
- `Code Quality`: 118
- `Databases`: 118

### Recent Timeline

- `2026-08-07T09:34:55+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-07T08:16:00+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-07T06:09:43+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-06T22:17:13+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-06T21:22:05+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-06T20:45:11+08:00` | **Log with stable keys** (Observability)
- `2026-08-06T19:56:19+08:00` | **Design for idempotency** (APIs)
- `2026-08-06T19:06:12+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-06T18:12:41+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-06T17:13:33+08:00` | **Write one behavior per test** (Testing)
