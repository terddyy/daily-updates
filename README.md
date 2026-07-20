# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2203**
- Today's entries: **1**
- Today's note: `notes/2026-07-21.md`

### Latest Entry

- Timestamp: `2026-07-21T06:39:14+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 111
- `Databases`: 111
- `Security`: 111
- `Testing`: 111
- `Accessibility`: 110

### Recent Timeline

- `2026-07-21T06:39:14+08:00` | **Design for idempotency** (APIs)
- `2026-07-20T22:38:10+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-20T20:16:32+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-20T17:45:21+08:00` | **Write one behavior per test** (Testing)
- `2026-07-20T14:34:41+08:00` | **Use virtual environments by default** (Python)
- `2026-07-20T11:39:32+08:00` | **Prefer small focused commits** (Git)
- `2026-07-20T07:57:05+08:00` | **Write decisions down** (Leadership)
- `2026-07-20T06:52:30+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-19T22:41:23+08:00` | **Measure before tuning** (Performance)
- `2026-07-19T21:42:33+08:00` | **Fail fast on lint and tests** (CI/CD)
