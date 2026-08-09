# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2423**
- Today's entries: **26**
- Today's note: `notes/2026-08-09.md`

### Latest Entry

- Timestamp: `2026-08-09T22:25:47+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 122
- `Databases`: 122
- `Security`: 122
- `Testing`: 122
- `Accessibility`: 121

### Recent Timeline

- `2026-08-09T22:25:47+08:00` | **Design for idempotency** (APIs)
- `2026-08-09T21:34:17+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-09T21:07:17+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-09T19:56:07+08:00` | **Write one behavior per test** (Testing)
- `2026-08-09T19:09:57+08:00` | **Use virtual environments by default** (Python)
- `2026-08-09T18:11:27+08:00` | **Prefer small focused commits** (Git)
- `2026-08-09T17:45:56+08:00` | **Write decisions down** (Leadership)
- `2026-08-09T17:16:21+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-09T16:15:41+08:00` | **Measure before tuning** (Performance)
- `2026-08-09T15:23:12+08:00` | **Fail fast on lint and tests** (CI/CD)
