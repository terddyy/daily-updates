# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **83**
- Today's entries: **15**
- Today's note: `notes/2026-04-20.md`

### Latest Entry

- Timestamp: `2026-04-20T16:43:59+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 5
- `Databases`: 5
- `Security`: 5
- `Testing`: 5
- `Accessibility`: 4

### Recent Timeline

- `2026-04-20T16:43:59+08:00` | **Design for idempotency** (APIs)
- `2026-04-20T15:35:07+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-20T14:42:50+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-20T13:02:01+08:00` | **Write one behavior per test** (Testing)
- `2026-04-20T11:03:09+08:00` | **Use virtual environments by default** (Python)
- `2026-04-20T09:33:57+08:00` | **Prefer small focused commits** (Git)
- `2026-04-20T08:21:58+08:00` | **Write decisions down** (Leadership)
- `2026-04-20T07:11:13+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-20T06:08:07+08:00` | **Measure before tuning** (Performance)
- `2026-04-20T05:10:38+08:00` | **Fail fast on lint and tests** (CI/CD)
