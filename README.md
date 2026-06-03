# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1523**
- Today's entries: **6**
- Today's note: `notes/2026-06-03.md`

### Latest Entry

- Timestamp: `2026-06-03T10:42:08+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 77
- `Databases`: 77
- `Security`: 77
- `Testing`: 77
- `Accessibility`: 76

### Recent Timeline

- `2026-06-03T10:42:08+08:00` | **Design for idempotency** (APIs)
- `2026-06-03T09:36:51+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-03T08:18:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-03T07:40:45+08:00` | **Write one behavior per test** (Testing)
- `2026-06-03T06:56:23+08:00` | **Use virtual environments by default** (Python)
- `2026-06-03T06:08:25+08:00` | **Prefer small focused commits** (Git)
- `2026-06-02T21:40:47+08:00` | **Write decisions down** (Leadership)
- `2026-06-02T20:09:47+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-02T18:36:43+08:00` | **Measure before tuning** (Performance)
- `2026-06-02T16:49:17+08:00` | **Fail fast on lint and tests** (CI/CD)
