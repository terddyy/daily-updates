# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2245**
- Today's entries: **1**
- Today's note: `notes/2026-07-27.md`

### Latest Entry

- Timestamp: `2026-07-27T06:12:18+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 113
- `Architecture`: 113
- `Databases`: 113
- `Observability`: 113
- `Security`: 113

### Recent Timeline

- `2026-07-27T06:12:18+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-26T22:14:47+08:00` | **Log with stable keys** (Observability)
- `2026-07-26T20:37:24+08:00` | **Design for idempotency** (APIs)
- `2026-07-26T19:18:53+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-26T17:46:24+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-25T22:46:50+08:00` | **Write one behavior per test** (Testing)
- `2026-07-25T19:46:16+08:00` | **Use virtual environments by default** (Python)
- `2026-07-25T18:26:49+08:00` | **Prefer small focused commits** (Git)
- `2026-07-25T14:39:57+08:00` | **Write decisions down** (Leadership)
- `2026-07-25T07:32:10+08:00` | **Keyboard support is a baseline** (Accessibility)
