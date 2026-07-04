# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1943**
- Today's entries: **12**
- Today's note: `notes/2026-07-04.md`

### Latest Entry

- Timestamp: `2026-07-04T22:16:04+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 98
- `Databases`: 98
- `Security`: 98
- `Testing`: 98
- `Accessibility`: 97

### Recent Timeline

- `2026-07-04T22:16:04+08:00` | **Design for idempotency** (APIs)
- `2026-07-04T19:46:24+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-04T19:06:40+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-04T17:31:22+08:00` | **Write one behavior per test** (Testing)
- `2026-07-04T16:39:48+08:00` | **Use virtual environments by default** (Python)
- `2026-07-04T15:40:33+08:00` | **Prefer small focused commits** (Git)
- `2026-07-04T13:19:05+08:00` | **Write decisions down** (Leadership)
- `2026-07-04T11:46:01+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-04T09:19:22+08:00` | **Measure before tuning** (Performance)
- `2026-07-04T08:42:50+08:00` | **Fail fast on lint and tests** (CI/CD)
