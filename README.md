# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2145**
- Today's entries: **10**
- Today's note: `notes/2026-07-16.md`

### Latest Entry

- Timestamp: `2026-07-16T13:04:50+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 108
- `Architecture`: 108
- `Databases`: 108
- `Observability`: 108
- `Security`: 108

### Recent Timeline

- `2026-07-16T13:04:50+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-16T11:50:15+08:00` | **Log with stable keys** (Observability)
- `2026-07-16T10:39:33+08:00` | **Design for idempotency** (APIs)
- `2026-07-16T09:36:32+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-16T08:50:59+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-16T08:06:27+08:00` | **Write one behavior per test** (Testing)
- `2026-07-16T07:35:30+08:00` | **Use virtual environments by default** (Python)
- `2026-07-16T07:07:09+08:00` | **Prefer small focused commits** (Git)
- `2026-07-16T06:35:25+08:00` | **Write decisions down** (Leadership)
- `2026-07-16T06:08:10+08:00` | **Keyboard support is a baseline** (Accessibility)
