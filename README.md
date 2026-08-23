# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2783**
- Today's entries: **10**
- Today's note: `notes/2026-08-23.md`

### Latest Entry

- Timestamp: `2026-08-23T18:32:42+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 140
- `Databases`: 140
- `Security`: 140
- `Testing`: 140
- `Accessibility`: 139

### Recent Timeline

- `2026-08-23T18:32:42+08:00` | **Design for idempotency** (APIs)
- `2026-08-23T17:35:44+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-23T15:47:02+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-23T15:05:13+08:00` | **Write one behavior per test** (Testing)
- `2026-08-23T13:44:33+08:00` | **Use virtual environments by default** (Python)
- `2026-08-23T12:22:09+08:00` | **Prefer small focused commits** (Git)
- `2026-08-23T10:44:26+08:00` | **Write decisions down** (Leadership)
- `2026-08-23T09:18:30+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-23T07:45:30+08:00` | **Measure before tuning** (Performance)
- `2026-08-23T06:20:57+08:00` | **Fail fast on lint and tests** (CI/CD)
