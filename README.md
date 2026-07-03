# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1925**
- Today's entries: **12**
- Today's note: `notes/2026-07-03.md`

### Latest Entry

- Timestamp: `2026-07-03T16:32:59+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 97
- `Architecture`: 97
- `Databases`: 97
- `Observability`: 97
- `Security`: 97

### Recent Timeline

- `2026-07-03T16:32:59+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-03T15:24:03+08:00` | **Log with stable keys** (Observability)
- `2026-07-03T14:03:05+08:00` | **Design for idempotency** (APIs)
- `2026-07-03T12:33:47+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-03T11:14:43+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-03T09:56:33+08:00` | **Write one behavior per test** (Testing)
- `2026-07-03T09:00:42+08:00` | **Use virtual environments by default** (Python)
- `2026-07-03T08:09:07+08:00` | **Prefer small focused commits** (Git)
- `2026-07-03T07:39:08+08:00` | **Write decisions down** (Leadership)
- `2026-07-03T07:10:10+08:00` | **Keyboard support is a baseline** (Accessibility)
