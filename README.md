# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2045**
- Today's entries: **4**
- Today's note: `notes/2026-07-11.md`

### Latest Entry

- Timestamp: `2026-07-11T08:51:59+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 103
- `Architecture`: 103
- `Databases`: 103
- `Observability`: 103
- `Security`: 103

### Recent Timeline

- `2026-07-11T08:51:59+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-11T08:06:23+08:00` | **Log with stable keys** (Observability)
- `2026-07-11T07:34:47+08:00` | **Design for idempotency** (APIs)
- `2026-07-11T06:08:53+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-10T22:18:18+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-10T21:25:28+08:00` | **Write one behavior per test** (Testing)
- `2026-07-10T20:36:17+08:00` | **Use virtual environments by default** (Python)
- `2026-07-10T19:41:45+08:00` | **Prefer small focused commits** (Git)
- `2026-07-10T18:35:10+08:00` | **Write decisions down** (Leadership)
- `2026-07-10T17:28:15+08:00` | **Keyboard support is a baseline** (Accessibility)
