# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2725**
- Today's entries: **13**
- Today's note: `notes/2026-08-20.md`

### Latest Entry

- Timestamp: `2026-08-20T15:48:50+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 137
- `Architecture`: 137
- `Databases`: 137
- `Observability`: 137
- `Security`: 137

### Recent Timeline

- `2026-08-20T15:48:50+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-20T14:58:48+08:00` | **Log with stable keys** (Observability)
- `2026-08-20T13:58:55+08:00` | **Design for idempotency** (APIs)
- `2026-08-20T13:30:08+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-20T12:52:55+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-20T12:10:22+08:00` | **Write one behavior per test** (Testing)
- `2026-08-20T11:29:25+08:00` | **Use virtual environments by default** (Python)
- `2026-08-20T10:30:54+08:00` | **Prefer small focused commits** (Git)
- `2026-08-20T09:12:53+08:00` | **Write decisions down** (Leadership)
- `2026-08-20T07:47:01+08:00` | **Keyboard support is a baseline** (Accessibility)
