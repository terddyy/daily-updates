# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1463**
- Today's entries: **10**
- Today's note: `notes/2026-05-29.md`

### Latest Entry

- Timestamp: `2026-05-29T16:32:16+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 74
- `Databases`: 74
- `Security`: 74
- `Testing`: 74
- `Accessibility`: 73

### Recent Timeline

- `2026-05-29T16:32:16+08:00` | **Design for idempotency** (APIs)
- `2026-05-29T15:03:10+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-29T13:31:57+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-29T11:47:17+08:00` | **Write one behavior per test** (Testing)
- `2026-05-29T10:23:16+08:00` | **Use virtual environments by default** (Python)
- `2026-05-29T09:21:02+08:00` | **Prefer small focused commits** (Git)
- `2026-05-29T08:10:26+08:00` | **Write decisions down** (Leadership)
- `2026-05-29T07:36:10+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-29T06:58:59+08:00` | **Measure before tuning** (Performance)
- `2026-05-29T06:21:15+08:00` | **Fail fast on lint and tests** (CI/CD)
