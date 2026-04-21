# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **103**
- Today's entries: **13**
- Today's note: `notes/2026-04-21.md`

### Latest Entry

- Timestamp: `2026-04-21T13:48:40+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 6
- `Databases`: 6
- `Security`: 6
- `Testing`: 6
- `Accessibility`: 5

### Recent Timeline

- `2026-04-21T13:48:40+08:00` | **Design for idempotency** (APIs)
- `2026-04-21T12:57:51+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-21T11:02:43+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-21T09:33:37+08:00` | **Write one behavior per test** (Testing)
- `2026-04-21T08:23:39+08:00` | **Use virtual environments by default** (Python)
- `2026-04-21T07:15:15+08:00` | **Prefer small focused commits** (Git)
- `2026-04-21T06:14:45+08:00` | **Write decisions down** (Leadership)
- `2026-04-21T05:15:54+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-21T04:14:29+08:00` | **Measure before tuning** (Performance)
- `2026-04-21T03:24:50+08:00` | **Fail fast on lint and tests** (CI/CD)
