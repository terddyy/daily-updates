# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **43**
- Today's entries: **21**
- Today's note: `notes/2026-04-18.md`

### Latest Entry

- Timestamp: `2026-04-18T21:26:40+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 3
- `Databases`: 3
- `Security`: 3
- `Testing`: 3
- `Accessibility`: 2

### Recent Timeline

- `2026-04-18T21:26:40+08:00` | **Design for idempotency** (APIs)
- `2026-04-18T20:10:00+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-18T19:12:45+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-18T18:14:01+08:00` | **Write one behavior per test** (Testing)
- `2026-04-18T17:16:28+08:00` | **Use virtual environments by default** (Python)
- `2026-04-18T16:13:28+08:00` | **Prefer small focused commits** (Git)
- `2026-04-18T15:26:02+08:00` | **Write decisions down** (Leadership)
- `2026-04-18T14:24:38+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-18T13:32:22+08:00` | **Measure before tuning** (Performance)
- `2026-04-18T12:46:15+08:00` | **Fail fast on lint and tests** (CI/CD)
