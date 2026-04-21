# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **105**
- Today's entries: **15**
- Today's note: `notes/2026-04-21.md`

### Latest Entry

- Timestamp: `2026-04-21T15:33:05+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 6
- `Architecture`: 6
- `Databases`: 6
- `Observability`: 6
- `Security`: 6

### Recent Timeline

- `2026-04-21T15:33:05+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-21T14:36:11+08:00` | **Log with stable keys** (Observability)
- `2026-04-21T13:48:40+08:00` | **Design for idempotency** (APIs)
- `2026-04-21T12:57:51+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-21T11:02:43+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-21T09:33:37+08:00` | **Write one behavior per test** (Testing)
- `2026-04-21T08:23:39+08:00` | **Use virtual environments by default** (Python)
- `2026-04-21T07:15:15+08:00` | **Prefer small focused commits** (Git)
- `2026-04-21T06:14:45+08:00` | **Write decisions down** (Leadership)
- `2026-04-21T05:15:54+08:00` | **Keyboard support is a baseline** (Accessibility)
