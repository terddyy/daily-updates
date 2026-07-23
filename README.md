# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2223**
- Today's entries: **5**
- Today's note: `notes/2026-07-23.md`

### Latest Entry

- Timestamp: `2026-07-23T15:18:25+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 112
- `Databases`: 112
- `Security`: 112
- `Testing`: 112
- `Accessibility`: 111

### Recent Timeline

- `2026-07-23T15:18:25+08:00` | **Design for idempotency** (APIs)
- `2026-07-23T12:36:48+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-23T09:13:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-23T07:41:25+08:00` | **Write one behavior per test** (Testing)
- `2026-07-23T06:33:07+08:00` | **Use virtual environments by default** (Python)
- `2026-07-22T22:00:13+08:00` | **Prefer small focused commits** (Git)
- `2026-07-22T19:55:52+08:00` | **Write decisions down** (Leadership)
- `2026-07-22T17:58:52+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-22T15:21:51+08:00` | **Measure before tuning** (Performance)
- `2026-07-22T12:34:00+08:00` | **Fail fast on lint and tests** (CI/CD)
