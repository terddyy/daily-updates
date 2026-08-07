# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2369**
- Today's entries: **23**
- Today's note: `notes/2026-08-07.md`

### Latest Entry

- Timestamp: `2026-08-07T22:00:01+08:00`
- Title: **Name intent, not mechanics**
- Category: `Code Quality`
- Source: https://martinfowler.com/books/clean-code.html
- Summary: Readable names should communicate business intent so maintainers understand why code exists before how it works.

### Top Categories

- `APIs`: 119
- `Architecture`: 119
- `Backend`: 119
- `Code Quality`: 119
- `Databases`: 119

### Recent Timeline

- `2026-08-07T22:00:01+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-07T21:29:17+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-07T20:48:19+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-07T20:18:38+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-07T19:46:39+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-07T19:18:08+08:00` | **Log with stable keys** (Observability)
- `2026-08-07T18:47:49+08:00` | **Design for idempotency** (APIs)
- `2026-08-07T18:20:27+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-07T17:49:07+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-07T17:23:40+08:00` | **Write one behavior per test** (Testing)
