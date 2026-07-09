# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2023**
- Today's entries: **16**
- Today's note: `notes/2026-07-09.md`

### Latest Entry

- Timestamp: `2026-07-09T21:42:51+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 102
- `Databases`: 102
- `Security`: 102
- `Testing`: 102
- `Accessibility`: 101

### Recent Timeline

- `2026-07-09T21:42:51+08:00` | **Design for idempotency** (APIs)
- `2026-07-09T19:44:35+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-09T18:42:07+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-09T17:35:47+08:00` | **Write one behavior per test** (Testing)
- `2026-07-09T16:18:38+08:00` | **Use virtual environments by default** (Python)
- `2026-07-09T14:57:54+08:00` | **Prefer small focused commits** (Git)
- `2026-07-09T13:39:57+08:00` | **Write decisions down** (Leadership)
- `2026-07-09T12:10:35+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-09T10:44:38+08:00` | **Measure before tuning** (Performance)
- `2026-07-09T09:43:12+08:00` | **Fail fast on lint and tests** (CI/CD)
