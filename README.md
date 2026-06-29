# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1865**
- Today's entries: **13**
- Today's note: `notes/2026-06-29.md`

### Latest Entry

- Timestamp: `2026-06-29T21:46:48+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 94
- `Architecture`: 94
- `Databases`: 94
- `Observability`: 94
- `Security`: 94

### Recent Timeline

- `2026-06-29T21:46:48+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-29T20:00:37+08:00` | **Log with stable keys** (Observability)
- `2026-06-29T18:14:13+08:00` | **Design for idempotency** (APIs)
- `2026-06-29T16:41:22+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-29T14:53:54+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-29T13:05:57+08:00` | **Write one behavior per test** (Testing)
- `2026-06-29T11:15:25+08:00` | **Use virtual environments by default** (Python)
- `2026-06-29T09:51:54+08:00` | **Prefer small focused commits** (Git)
- `2026-06-29T08:57:51+08:00` | **Write decisions down** (Leadership)
- `2026-06-29T07:54:12+08:00` | **Keyboard support is a baseline** (Accessibility)
