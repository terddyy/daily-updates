# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **443**
- Today's entries: **171**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:06:18+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 23
- `Databases`: 23
- `Security`: 23
- `Testing`: 23
- `Accessibility`: 22

### Recent Timeline

- `2026-05-01T09:06:18+08:00` | **Design for idempotency** (APIs)
- `2026-05-01T09:06:17+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-01T09:06:16+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-01T09:06:15+08:00` | **Write one behavior per test** (Testing)
- `2026-05-01T09:06:14+08:00` | **Use virtual environments by default** (Python)
- `2026-05-01T09:06:13+08:00` | **Prefer small focused commits** (Git)
- `2026-05-01T09:06:12+08:00` | **Write decisions down** (Leadership)
- `2026-05-01T09:06:11+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-01T09:06:10+08:00` | **Measure before tuning** (Performance)
- `2026-05-01T09:06:09+08:00` | **Fail fast on lint and tests** (CI/CD)
