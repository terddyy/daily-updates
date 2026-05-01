# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **523**
- Today's entries: **251**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:07:38+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 27
- `Databases`: 27
- `Security`: 27
- `Testing`: 27
- `Accessibility`: 26

### Recent Timeline

- `2026-05-01T09:07:38+08:00` | **Design for idempotency** (APIs)
- `2026-05-01T09:07:37+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-01T09:07:36+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-01T09:07:35+08:00` | **Write one behavior per test** (Testing)
- `2026-05-01T09:07:34+08:00` | **Use virtual environments by default** (Python)
- `2026-05-01T09:07:33+08:00` | **Prefer small focused commits** (Git)
- `2026-05-01T09:07:32+08:00` | **Write decisions down** (Leadership)
- `2026-05-01T09:07:31+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-01T09:07:30+08:00` | **Measure before tuning** (Performance)
- `2026-05-01T09:07:29+08:00` | **Fail fast on lint and tests** (CI/CD)
