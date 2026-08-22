# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2765**
- Today's entries: **8**
- Today's note: `notes/2026-08-22.md`

### Latest Entry

- Timestamp: `2026-08-22T16:29:17+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 139
- `Architecture`: 139
- `Databases`: 139
- `Observability`: 139
- `Security`: 139

### Recent Timeline

- `2026-08-22T16:29:17+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-22T12:48:58+08:00` | **Log with stable keys** (Observability)
- `2026-08-22T12:05:38+08:00` | **Design for idempotency** (APIs)
- `2026-08-22T11:25:17+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-22T10:40:16+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-22T09:42:56+08:00` | **Write one behavior per test** (Testing)
- `2026-08-22T07:32:22+08:00` | **Use virtual environments by default** (Python)
- `2026-08-22T06:33:01+08:00` | **Prefer small focused commits** (Git)
- `2026-08-21T22:42:36+08:00` | **Write decisions down** (Leadership)
- `2026-08-21T21:58:03+08:00` | **Keyboard support is a baseline** (Accessibility)
