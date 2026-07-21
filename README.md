# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2205**
- Today's entries: **3**
- Today's note: `notes/2026-07-21.md`

### Latest Entry

- Timestamp: `2026-07-21T09:09:29+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 111
- `Architecture`: 111
- `Databases`: 111
- `Observability`: 111
- `Security`: 111

### Recent Timeline

- `2026-07-21T09:09:29+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-21T07:40:28+08:00` | **Log with stable keys** (Observability)
- `2026-07-21T06:39:14+08:00` | **Design for idempotency** (APIs)
- `2026-07-20T22:38:10+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-20T20:16:32+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-20T17:45:21+08:00` | **Write one behavior per test** (Testing)
- `2026-07-20T14:34:41+08:00` | **Use virtual environments by default** (Python)
- `2026-07-20T11:39:32+08:00` | **Prefer small focused commits** (Git)
- `2026-07-20T07:57:05+08:00` | **Write decisions down** (Leadership)
- `2026-07-20T06:52:30+08:00` | **Keyboard support is a baseline** (Accessibility)
