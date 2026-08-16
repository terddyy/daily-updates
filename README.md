# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2625**
- Today's entries: **16**
- Today's note: `notes/2026-08-16.md`

### Latest Entry

- Timestamp: `2026-08-16T16:57:49+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 132
- `Architecture`: 132
- `Databases`: 132
- `Observability`: 132
- `Security`: 132

### Recent Timeline

- `2026-08-16T16:57:49+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-16T16:43:10+08:00` | **Log with stable keys** (Observability)
- `2026-08-16T16:24:53+08:00` | **Design for idempotency** (APIs)
- `2026-08-16T15:54:09+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-16T14:47:13+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-16T14:09:49+08:00` | **Write one behavior per test** (Testing)
- `2026-08-16T13:54:18+08:00` | **Use virtual environments by default** (Python)
- `2026-08-16T12:44:52+08:00` | **Prefer small focused commits** (Git)
- `2026-08-16T12:26:01+08:00` | **Write decisions down** (Leadership)
- `2026-08-16T12:00:40+08:00` | **Keyboard support is a baseline** (Accessibility)
