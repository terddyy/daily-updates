# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1989**
- Today's entries: **2**
- Today's note: `notes/2026-07-08.md`

### Latest Entry

- Timestamp: `2026-07-08T06:49:15+08:00`
- Title: **Name intent, not mechanics**
- Category: `Code Quality`
- Source: https://martinfowler.com/books/clean-code.html
- Summary: Readable names should communicate business intent so maintainers understand why code exists before how it works.

### Top Categories

- `APIs`: 100
- `Architecture`: 100
- `Backend`: 100
- `Code Quality`: 100
- `Databases`: 100

### Recent Timeline

- `2026-07-08T06:49:15+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-08T06:15:34+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-07T22:18:26+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-07T21:17:44+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-07T20:22:53+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-07T19:28:06+08:00` | **Log with stable keys** (Observability)
- `2026-07-07T18:26:03+08:00` | **Design for idempotency** (APIs)
- `2026-07-07T17:11:04+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-07T15:46:26+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-07T14:23:34+08:00` | **Write one behavior per test** (Testing)
