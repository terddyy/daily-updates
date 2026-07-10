# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2043**
- Today's entries: **2**
- Today's note: `notes/2026-07-11.md`

### Latest Entry

- Timestamp: `2026-07-11T07:34:47+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 103
- `Databases`: 103
- `Security`: 103
- `Testing`: 103
- `Accessibility`: 102

### Recent Timeline

- `2026-07-11T07:34:47+08:00` | **Design for idempotency** (APIs)
- `2026-07-11T06:08:53+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-10T22:18:18+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-10T21:25:28+08:00` | **Write one behavior per test** (Testing)
- `2026-07-10T20:36:17+08:00` | **Use virtual environments by default** (Python)
- `2026-07-10T19:41:45+08:00` | **Prefer small focused commits** (Git)
- `2026-07-10T18:35:10+08:00` | **Write decisions down** (Leadership)
- `2026-07-10T17:28:15+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-10T16:12:06+08:00` | **Measure before tuning** (Performance)
- `2026-07-10T14:57:56+08:00` | **Fail fast on lint and tests** (CI/CD)
