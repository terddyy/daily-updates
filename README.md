# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1983**
- Today's entries: **12**
- Today's note: `notes/2026-07-07.md`

### Latest Entry

- Timestamp: `2026-07-07T18:26:03+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 100
- `Databases`: 100
- `Security`: 100
- `Testing`: 100
- `Accessibility`: 99

### Recent Timeline

- `2026-07-07T18:26:03+08:00` | **Design for idempotency** (APIs)
- `2026-07-07T17:11:04+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-07T15:46:26+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-07T14:23:34+08:00` | **Write one behavior per test** (Testing)
- `2026-07-07T12:47:54+08:00` | **Use virtual environments by default** (Python)
- `2026-07-07T11:15:23+08:00` | **Prefer small focused commits** (Git)
- `2026-07-07T09:56:45+08:00` | **Write decisions down** (Leadership)
- `2026-07-07T09:03:29+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-07T08:09:15+08:00` | **Measure before tuning** (Performance)
- `2026-07-07T07:38:46+08:00` | **Fail fast on lint and tests** (CI/CD)
