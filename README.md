# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2705**
- Today's entries: **16**
- Today's note: `notes/2026-08-19.md`

### Latest Entry

- Timestamp: `2026-08-19T17:48:49+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 136
- `Architecture`: 136
- `Databases`: 136
- `Observability`: 136
- `Security`: 136

### Recent Timeline

- `2026-08-19T17:48:49+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-19T17:04:06+08:00` | **Log with stable keys** (Observability)
- `2026-08-19T16:16:50+08:00` | **Design for idempotency** (APIs)
- `2026-08-19T15:43:25+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-19T14:57:17+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-19T13:58:33+08:00` | **Write one behavior per test** (Testing)
- `2026-08-19T13:29:29+08:00` | **Use virtual environments by default** (Python)
- `2026-08-19T12:51:55+08:00` | **Prefer small focused commits** (Git)
- `2026-08-19T12:10:31+08:00` | **Write decisions down** (Leadership)
- `2026-08-19T11:29:23+08:00` | **Keyboard support is a baseline** (Accessibility)
