# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **309**
- Today's entries: **37**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:04:04+08:00`
- Title: **Name intent, not mechanics**
- Category: `Code Quality`
- Source: https://martinfowler.com/books/clean-code.html
- Summary: Readable names should communicate business intent so maintainers understand why code exists before how it works.

### Top Categories

- `APIs`: 16
- `Architecture`: 16
- `Backend`: 16
- `Code Quality`: 16
- `Databases`: 16

### Recent Timeline

- `2026-05-01T09:04:04+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-01T09:04:03+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-01T09:04:02+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-01T09:04:01+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-01T09:04:00+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-01T09:03:59+08:00` | **Log with stable keys** (Observability)
- `2026-05-01T09:03:58+08:00` | **Design for idempotency** (APIs)
- `2026-05-01T09:03:57+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-01T09:03:56+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-01T09:03:55+08:00` | **Write one behavior per test** (Testing)
