# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2743**
- Today's entries: **8**
- Today's note: `notes/2026-08-21.md`

### Latest Entry

- Timestamp: `2026-08-21T12:22:54+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 138
- `Databases`: 138
- `Security`: 138
- `Testing`: 138
- `Accessibility`: 137

### Recent Timeline

- `2026-08-21T12:22:54+08:00` | **Design for idempotency** (APIs)
- `2026-08-21T11:36:33+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-21T10:43:57+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-21T09:16:39+08:00` | **Write one behavior per test** (Testing)
- `2026-08-21T07:52:12+08:00` | **Use virtual environments by default** (Python)
- `2026-08-21T07:27:58+08:00` | **Prefer small focused commits** (Git)
- `2026-08-21T06:56:23+08:00` | **Write decisions down** (Leadership)
- `2026-08-21T06:27:17+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-20T22:45:11+08:00` | **Measure before tuning** (Performance)
- `2026-08-20T21:59:28+08:00` | **Fail fast on lint and tests** (CI/CD)
