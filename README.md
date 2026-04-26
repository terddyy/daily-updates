# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **223**
- Today's entries: **18**
- Today's note: `notes/2026-04-26.md`

### Latest Entry

- Timestamp: `2026-04-26T19:15:09+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 12
- `Databases`: 12
- `Security`: 12
- `Testing`: 12
- `Accessibility`: 11

### Recent Timeline

- `2026-04-26T19:15:09+08:00` | **Design for idempotency** (APIs)
- `2026-04-26T18:15:25+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-26T17:19:39+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-26T16:26:05+08:00` | **Write one behavior per test** (Testing)
- `2026-04-26T15:31:33+08:00` | **Use virtual environments by default** (Python)
- `2026-04-26T14:36:56+08:00` | **Prefer small focused commits** (Git)
- `2026-04-26T13:01:39+08:00` | **Write decisions down** (Leadership)
- `2026-04-26T11:03:12+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-26T09:33:35+08:00` | **Measure before tuning** (Performance)
- `2026-04-26T08:23:45+08:00` | **Fail fast on lint and tests** (CI/CD)
