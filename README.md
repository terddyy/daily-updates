# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1665**
- Today's entries: **8**
- Today's note: `notes/2026-06-14.md`

### Latest Entry

- Timestamp: `2026-06-14T15:12:22+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 84
- `Architecture`: 84
- `Databases`: 84
- `Observability`: 84
- `Security`: 84

### Recent Timeline

- `2026-06-14T15:12:22+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-14T13:38:39+08:00` | **Log with stable keys** (Observability)
- `2026-06-14T11:50:37+08:00` | **Design for idempotency** (APIs)
- `2026-06-14T09:28:37+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-14T08:09:28+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-14T07:40:05+08:00` | **Write one behavior per test** (Testing)
- `2026-06-14T07:09:47+08:00` | **Use virtual environments by default** (Python)
- `2026-06-14T06:12:38+08:00` | **Prefer small focused commits** (Git)
- `2026-06-13T22:30:05+08:00` | **Write decisions down** (Leadership)
- `2026-06-13T21:36:54+08:00` | **Keyboard support is a baseline** (Accessibility)
