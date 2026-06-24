# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1785**
- Today's entries: **4**
- Today's note: `notes/2026-06-24.md`

### Latest Entry

- Timestamp: `2026-06-24T08:06:27+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 90
- `Architecture`: 90
- `Databases`: 90
- `Observability`: 90
- `Security`: 90

### Recent Timeline

- `2026-06-24T08:06:27+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-24T07:37:13+08:00` | **Log with stable keys** (Observability)
- `2026-06-24T07:09:18+08:00` | **Design for idempotency** (APIs)
- `2026-06-24T06:35:28+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-23T22:19:47+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-23T21:16:29+08:00` | **Write one behavior per test** (Testing)
- `2026-06-23T20:02:56+08:00` | **Use virtual environments by default** (Python)
- `2026-06-23T18:48:49+08:00` | **Prefer small focused commits** (Git)
- `2026-06-23T17:31:54+08:00` | **Write decisions down** (Leadership)
- `2026-06-23T16:14:18+08:00` | **Keyboard support is a baseline** (Accessibility)
