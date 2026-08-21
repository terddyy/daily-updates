# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2745**
- Today's entries: **10**
- Today's note: `notes/2026-08-21.md`

### Latest Entry

- Timestamp: `2026-08-21T13:47:38+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 138
- `Architecture`: 138
- `Databases`: 138
- `Observability`: 138
- `Security`: 138

### Recent Timeline

- `2026-08-21T13:47:38+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-21T13:04:19+08:00` | **Log with stable keys** (Observability)
- `2026-08-21T12:22:54+08:00` | **Design for idempotency** (APIs)
- `2026-08-21T11:36:33+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-21T10:43:57+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-21T09:16:39+08:00` | **Write one behavior per test** (Testing)
- `2026-08-21T07:52:12+08:00` | **Use virtual environments by default** (Python)
- `2026-08-21T07:27:58+08:00` | **Prefer small focused commits** (Git)
- `2026-08-21T06:56:23+08:00` | **Write decisions down** (Leadership)
- `2026-08-21T06:27:17+08:00` | **Keyboard support is a baseline** (Accessibility)
