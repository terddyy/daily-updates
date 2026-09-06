# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2903**
- Today's entries: **24**
- Today's note: `notes/2026-09-06.md`

### Latest Entry

- Timestamp: `2026-09-06T16:31:46+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 146
- `Databases`: 146
- `Security`: 146
- `Testing`: 146
- `Accessibility`: 145

### Recent Timeline

- `2026-09-06T16:31:46+08:00` | **Design for idempotency** (APIs)
- `2026-09-06T16:14:50+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-09-06T15:48:21+08:00` | **Rotate credentials on schedule** (Security)
- `2026-09-06T15:35:28+08:00` | **Write one behavior per test** (Testing)
- `2026-09-06T15:25:42+08:00` | **Use virtual environments by default** (Python)
- `2026-09-06T15:12:01+08:00` | **Prefer small focused commits** (Git)
- `2026-09-06T14:44:12+08:00` | **Write decisions down** (Leadership)
- `2026-09-06T14:19:00+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-09-06T13:48:33+08:00` | **Measure before tuning** (Performance)
- `2026-09-06T13:34:59+08:00` | **Fail fast on lint and tests** (CI/CD)
