# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2785**
- Today's entries: **12**
- Today's note: `notes/2026-08-23.md`

### Latest Entry

- Timestamp: `2026-08-23T19:28:28+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 140
- `Architecture`: 140
- `Databases`: 140
- `Observability`: 140
- `Security`: 140

### Recent Timeline

- `2026-08-23T19:28:28+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-23T18:59:40+08:00` | **Log with stable keys** (Observability)
- `2026-08-23T18:32:42+08:00` | **Design for idempotency** (APIs)
- `2026-08-23T17:35:44+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-23T15:47:02+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-23T15:05:13+08:00` | **Write one behavior per test** (Testing)
- `2026-08-23T13:44:33+08:00` | **Use virtual environments by default** (Python)
- `2026-08-23T12:22:09+08:00` | **Prefer small focused commits** (Git)
- `2026-08-23T10:44:26+08:00` | **Write decisions down** (Leadership)
- `2026-08-23T09:18:30+08:00` | **Keyboard support is a baseline** (Accessibility)
