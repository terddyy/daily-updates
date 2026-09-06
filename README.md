# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2923**
- Today's entries: **7**
- Today's note: `notes/2026-09-07.md`

### Latest Entry

- Timestamp: `2026-09-07T07:34:52+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 147
- `Databases`: 147
- `Security`: 147
- `Testing`: 147
- `Accessibility`: 146

### Recent Timeline

- `2026-09-07T07:34:52+08:00` | **Design for idempotency** (APIs)
- `2026-09-07T07:20:54+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-09-07T07:09:21+08:00` | **Rotate credentials on schedule** (Security)
- `2026-09-07T06:48:09+08:00` | **Write one behavior per test** (Testing)
- `2026-09-07T06:34:43+08:00` | **Use virtual environments by default** (Python)
- `2026-09-07T06:22:00+08:00` | **Prefer small focused commits** (Git)
- `2026-09-07T06:10:03+08:00` | **Write decisions down** (Leadership)
- `2026-09-06T22:35:06+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-09-06T22:22:04+08:00` | **Measure before tuning** (Performance)
- `2026-09-06T21:21:17+08:00` | **Fail fast on lint and tests** (CI/CD)
