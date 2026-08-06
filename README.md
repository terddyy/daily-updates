# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2345**
- Today's entries: **19**
- Today's note: `notes/2026-08-06.md`

### Latest Entry

- Timestamp: `2026-08-06T21:22:05+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 118
- `Architecture`: 118
- `Databases`: 118
- `Observability`: 118
- `Security`: 118

### Recent Timeline

- `2026-08-06T21:22:05+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-06T20:45:11+08:00` | **Log with stable keys** (Observability)
- `2026-08-06T19:56:19+08:00` | **Design for idempotency** (APIs)
- `2026-08-06T19:06:12+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-06T18:12:41+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-06T17:13:33+08:00` | **Write one behavior per test** (Testing)
- `2026-08-06T16:04:52+08:00` | **Use virtual environments by default** (Python)
- `2026-08-06T15:10:55+08:00` | **Prefer small focused commits** (Git)
- `2026-08-06T14:09:47+08:00` | **Write decisions down** (Leadership)
- `2026-08-06T13:05:35+08:00` | **Keyboard support is a baseline** (Accessibility)
