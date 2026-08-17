# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2665**
- Today's entries: **22**
- Today's note: `notes/2026-08-17.md`

### Latest Entry

- Timestamp: `2026-08-17T22:27:14+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 134
- `Architecture`: 134
- `Databases`: 134
- `Observability`: 134
- `Security`: 134

### Recent Timeline

- `2026-08-17T22:27:14+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-17T21:45:29+08:00` | **Log with stable keys** (Observability)
- `2026-08-17T20:59:09+08:00` | **Design for idempotency** (APIs)
- `2026-08-17T19:59:18+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-17T19:40:24+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-17T19:02:03+08:00` | **Write one behavior per test** (Testing)
- `2026-08-17T18:36:22+08:00` | **Use virtual environments by default** (Python)
- `2026-08-17T17:57:05+08:00` | **Prefer small focused commits** (Git)
- `2026-08-17T17:00:18+08:00` | **Write decisions down** (Leadership)
- `2026-08-17T16:06:36+08:00` | **Keyboard support is a baseline** (Accessibility)
