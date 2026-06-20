# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1745**
- Today's entries: **2**
- Today's note: `notes/2026-06-21.md`

### Latest Entry

- Timestamp: `2026-06-21T07:31:56+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 88
- `Architecture`: 88
- `Databases`: 88
- `Observability`: 88
- `Security`: 88

### Recent Timeline

- `2026-06-21T07:31:56+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-21T06:29:17+08:00` | **Log with stable keys** (Observability)
- `2026-06-20T22:31:42+08:00` | **Design for idempotency** (APIs)
- `2026-06-20T21:37:18+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-20T19:27:31+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-20T18:38:09+08:00` | **Write one behavior per test** (Testing)
- `2026-06-20T17:40:12+08:00` | **Use virtual environments by default** (Python)
- `2026-06-20T16:23:44+08:00` | **Prefer small focused commits** (Git)
- `2026-06-20T15:06:09+08:00` | **Write decisions down** (Leadership)
- `2026-06-20T13:33:59+08:00` | **Keyboard support is a baseline** (Accessibility)
