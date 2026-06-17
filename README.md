# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1703**
- Today's entries: **12**
- Today's note: `notes/2026-06-17.md`

### Latest Entry

- Timestamp: `2026-06-17T21:32:49+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 86
- `Databases`: 86
- `Security`: 86
- `Testing`: 86
- `Accessibility`: 85

### Recent Timeline

- `2026-06-17T21:32:49+08:00` | **Design for idempotency** (APIs)
- `2026-06-17T20:12:32+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-17T18:40:53+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-17T16:56:24+08:00` | **Write one behavior per test** (Testing)
- `2026-06-17T15:01:53+08:00` | **Use virtual environments by default** (Python)
- `2026-06-17T13:13:36+08:00` | **Prefer small focused commits** (Git)
- `2026-06-17T11:26:12+08:00` | **Write decisions down** (Leadership)
- `2026-06-17T10:04:51+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-17T09:02:01+08:00` | **Measure before tuning** (Performance)
- `2026-06-17T07:47:37+08:00` | **Fail fast on lint and tests** (CI/CD)
