# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2863**
- Today's entries: **1**
- Today's note: `notes/2026-09-05.md`

### Latest Entry

- Timestamp: `2026-09-05T17:11:31+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 144
- `Databases`: 144
- `Security`: 144
- `Testing`: 144
- `Accessibility`: 143

### Recent Timeline

- `2026-09-05T17:11:31+08:00` | **Design for idempotency** (APIs)
- `2026-08-31T08:50:59+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-31T06:39:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-30T21:08:09+08:00` | **Write one behavior per test** (Testing)
- `2026-08-30T15:16:31+08:00` | **Use virtual environments by default** (Python)
- `2026-08-30T07:20:13+08:00` | **Prefer small focused commits** (Git)
- `2026-08-29T18:04:24+08:00` | **Write decisions down** (Leadership)
- `2026-08-29T11:10:01+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-28T17:54:46+08:00` | **Measure before tuning** (Performance)
- `2026-08-28T07:54:01+08:00` | **Fail fast on lint and tests** (CI/CD)
