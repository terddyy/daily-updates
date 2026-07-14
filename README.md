# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2103**
- Today's entries: **12**
- Today's note: `notes/2026-07-14.md`

### Latest Entry

- Timestamp: `2026-07-14T14:54:54+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 106
- `Databases`: 106
- `Security`: 106
- `Testing`: 106
- `Accessibility`: 105

### Recent Timeline

- `2026-07-14T14:54:54+08:00` | **Design for idempotency** (APIs)
- `2026-07-14T13:58:55+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-14T13:02:45+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-14T11:47:34+08:00` | **Write one behavior per test** (Testing)
- `2026-07-14T10:39:05+08:00` | **Use virtual environments by default** (Python)
- `2026-07-14T09:36:00+08:00` | **Prefer small focused commits** (Git)
- `2026-07-14T08:49:15+08:00` | **Write decisions down** (Leadership)
- `2026-07-14T08:04:04+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-14T07:33:20+08:00` | **Measure before tuning** (Performance)
- `2026-07-14T07:06:21+08:00` | **Fail fast on lint and tests** (CI/CD)
