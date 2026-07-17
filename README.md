# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2163**
- Today's entries: **6**
- Today's note: `notes/2026-07-17.md`

### Latest Entry

- Timestamp: `2026-07-17T08:53:49+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 109
- `Databases`: 109
- `Security`: 109
- `Testing`: 109
- `Accessibility`: 108

### Recent Timeline

- `2026-07-17T08:53:49+08:00` | **Design for idempotency** (APIs)
- `2026-07-17T08:06:59+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-17T07:34:24+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-17T07:06:54+08:00` | **Write one behavior per test** (Testing)
- `2026-07-17T06:34:28+08:00` | **Use virtual environments by default** (Python)
- `2026-07-17T06:08:22+08:00` | **Prefer small focused commits** (Git)
- `2026-07-16T22:45:53+08:00` | **Write decisions down** (Leadership)
- `2026-07-16T21:57:12+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-16T21:12:03+08:00` | **Measure before tuning** (Performance)
- `2026-07-16T20:37:11+08:00` | **Fail fast on lint and tests** (CI/CD)
