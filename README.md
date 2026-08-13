# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2543**
- Today's entries: **28**
- Today's note: `notes/2026-08-13.md`

### Latest Entry

- Timestamp: `2026-08-13T22:53:32+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 128
- `Databases`: 128
- `Security`: 128
- `Testing`: 128
- `Accessibility`: 127

### Recent Timeline

- `2026-08-13T22:53:32+08:00` | **Design for idempotency** (APIs)
- `2026-08-13T22:29:01+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-13T21:47:14+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-13T21:09:48+08:00` | **Write one behavior per test** (Testing)
- `2026-08-13T20:32:12+08:00` | **Use virtual environments by default** (Python)
- `2026-08-13T20:00:40+08:00` | **Prefer small focused commits** (Git)
- `2026-08-13T19:30:56+08:00` | **Write decisions down** (Leadership)
- `2026-08-13T19:06:50+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-13T18:38:07+08:00` | **Measure before tuning** (Performance)
- `2026-08-13T18:09:08+08:00` | **Fail fast on lint and tests** (CI/CD)
