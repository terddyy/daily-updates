# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1845**
- Today's entries: **5**
- Today's note: `notes/2026-06-28.md`

### Latest Entry

- Timestamp: `2026-06-28T09:49:12+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 93
- `Architecture`: 93
- `Databases`: 93
- `Observability`: 93
- `Security`: 93

### Recent Timeline

- `2026-06-28T09:49:12+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-28T08:56:33+08:00` | **Log with stable keys** (Observability)
- `2026-06-28T07:25:35+08:00` | **Design for idempotency** (APIs)
- `2026-06-28T06:50:35+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-28T06:25:41+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-27T22:51:50+08:00` | **Write one behavior per test** (Testing)
- `2026-06-27T22:08:13+08:00` | **Use virtual environments by default** (Python)
- `2026-06-27T21:17:55+08:00` | **Prefer small focused commits** (Git)
- `2026-06-27T20:09:18+08:00` | **Write decisions down** (Leadership)
- `2026-06-27T19:33:18+08:00` | **Keyboard support is a baseline** (Accessibility)
