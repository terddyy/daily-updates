# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1883**
- Today's entries: **1**
- Today's note: `notes/2026-07-01.md`

### Latest Entry

- Timestamp: `2026-07-01T06:29:38+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 95
- `Databases`: 95
- `Security`: 95
- `Testing`: 95
- `Accessibility`: 94

### Recent Timeline

- `2026-07-01T06:29:38+08:00` | **Design for idempotency** (APIs)
- `2026-06-30T22:37:24+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-30T21:39:03+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-30T20:46:28+08:00` | **Write one behavior per test** (Testing)
- `2026-06-30T19:46:19+08:00` | **Use virtual environments by default** (Python)
- `2026-06-30T18:44:51+08:00` | **Prefer small focused commits** (Git)
- `2026-06-30T17:31:50+08:00` | **Write decisions down** (Leadership)
- `2026-06-30T16:14:30+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-30T14:52:30+08:00` | **Measure before tuning** (Performance)
- `2026-06-30T13:27:49+08:00` | **Fail fast on lint and tests** (CI/CD)
