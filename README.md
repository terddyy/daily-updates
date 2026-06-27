# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1843**
- Today's entries: **3**
- Today's note: `notes/2026-06-28.md`

### Latest Entry

- Timestamp: `2026-06-28T07:25:35+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 93
- `Databases`: 93
- `Security`: 93
- `Testing`: 93
- `Accessibility`: 92

### Recent Timeline

- `2026-06-28T07:25:35+08:00` | **Design for idempotency** (APIs)
- `2026-06-28T06:50:35+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-28T06:25:41+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-27T22:51:50+08:00` | **Write one behavior per test** (Testing)
- `2026-06-27T22:08:13+08:00` | **Use virtual environments by default** (Python)
- `2026-06-27T21:17:55+08:00` | **Prefer small focused commits** (Git)
- `2026-06-27T20:09:18+08:00` | **Write decisions down** (Leadership)
- `2026-06-27T19:33:18+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-27T15:10:41+08:00` | **Measure before tuning** (Performance)
- `2026-06-27T13:48:30+08:00` | **Fail fast on lint and tests** (CI/CD)
