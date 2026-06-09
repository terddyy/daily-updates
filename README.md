# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1605**
- Today's entries: **10**
- Today's note: `notes/2026-06-09.md`

### Latest Entry

- Timestamp: `2026-06-09T16:15:44+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 81
- `Architecture`: 81
- `Databases`: 81
- `Observability`: 81
- `Security`: 81

### Recent Timeline

- `2026-06-09T16:15:44+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-09T14:50:42+08:00` | **Log with stable keys** (Observability)
- `2026-06-09T13:27:08+08:00` | **Design for idempotency** (APIs)
- `2026-06-09T11:46:45+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-09T10:21:58+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-09T09:17:45+08:00` | **Write one behavior per test** (Testing)
- `2026-06-09T08:11:57+08:00` | **Use virtual environments by default** (Python)
- `2026-06-09T07:42:38+08:00` | **Prefer small focused commits** (Git)
- `2026-06-09T07:10:42+08:00` | **Write decisions down** (Leadership)
- `2026-06-09T06:35:05+08:00` | **Keyboard support is a baseline** (Accessibility)
