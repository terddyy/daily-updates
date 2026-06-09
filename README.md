# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1603**
- Today's entries: **8**
- Today's note: `notes/2026-06-09.md`

### Latest Entry

- Timestamp: `2026-06-09T13:27:08+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 81
- `Databases`: 81
- `Security`: 81
- `Testing`: 81
- `Accessibility`: 80

### Recent Timeline

- `2026-06-09T13:27:08+08:00` | **Design for idempotency** (APIs)
- `2026-06-09T11:46:45+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-09T10:21:58+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-09T09:17:45+08:00` | **Write one behavior per test** (Testing)
- `2026-06-09T08:11:57+08:00` | **Use virtual environments by default** (Python)
- `2026-06-09T07:42:38+08:00` | **Prefer small focused commits** (Git)
- `2026-06-09T07:10:42+08:00` | **Write decisions down** (Leadership)
- `2026-06-09T06:35:05+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-08T22:10:04+08:00` | **Measure before tuning** (Performance)
- `2026-06-08T20:32:29+08:00` | **Fail fast on lint and tests** (CI/CD)
