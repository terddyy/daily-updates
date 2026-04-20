# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **85**
- Today's entries: **17**
- Today's note: `notes/2026-04-20.md`

### Latest Entry

- Timestamp: `2026-04-20T18:33:28+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 5
- `Architecture`: 5
- `Databases`: 5
- `Observability`: 5
- `Security`: 5

### Recent Timeline

- `2026-04-20T18:33:28+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-20T17:35:06+08:00` | **Log with stable keys** (Observability)
- `2026-04-20T16:43:59+08:00` | **Design for idempotency** (APIs)
- `2026-04-20T15:35:07+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-20T14:42:50+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-20T13:02:01+08:00` | **Write one behavior per test** (Testing)
- `2026-04-20T11:03:09+08:00` | **Use virtual environments by default** (Python)
- `2026-04-20T09:33:57+08:00` | **Prefer small focused commits** (Git)
- `2026-04-20T08:21:58+08:00` | **Write decisions down** (Leadership)
- `2026-04-20T07:11:13+08:00` | **Keyboard support is a baseline** (Accessibility)
