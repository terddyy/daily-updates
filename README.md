# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2323**
- Today's entries: **17**
- Today's note: `notes/2026-08-05.md`

### Latest Entry

- Timestamp: `2026-08-05T20:23:41+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 117
- `Databases`: 117
- `Security`: 117
- `Testing`: 117
- `Accessibility`: 116

### Recent Timeline

- `2026-08-05T20:23:41+08:00` | **Design for idempotency** (APIs)
- `2026-08-05T19:30:42+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-05T18:38:53+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-05T17:38:48+08:00` | **Write one behavior per test** (Testing)
- `2026-08-05T16:39:04+08:00` | **Use virtual environments by default** (Python)
- `2026-08-05T15:39:31+08:00` | **Prefer small focused commits** (Git)
- `2026-08-05T14:36:53+08:00` | **Write decisions down** (Leadership)
- `2026-08-05T13:31:00+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-05T12:22:36+08:00` | **Measure before tuning** (Performance)
- `2026-08-05T11:11:19+08:00` | **Fail fast on lint and tests** (CI/CD)
