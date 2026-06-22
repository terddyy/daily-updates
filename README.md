# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1763**
- Today's entries: **9**
- Today's note: `notes/2026-06-22.md`

### Latest Entry

- Timestamp: `2026-06-22T15:18:25+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 89
- `Databases`: 89
- `Security`: 89
- `Testing`: 89
- `Accessibility`: 88

### Recent Timeline

- `2026-06-22T15:18:25+08:00` | **Design for idempotency** (APIs)
- `2026-06-22T13:18:34+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-22T11:26:40+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-22T10:05:52+08:00` | **Write one behavior per test** (Testing)
- `2026-06-22T09:02:08+08:00` | **Use virtual environments by default** (Python)
- `2026-06-22T07:47:09+08:00` | **Prefer small focused commits** (Git)
- `2026-06-22T07:11:41+08:00` | **Write decisions down** (Leadership)
- `2026-06-22T06:41:11+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-22T06:10:31+08:00` | **Measure before tuning** (Performance)
- `2026-06-21T22:16:56+08:00` | **Fail fast on lint and tests** (CI/CD)
