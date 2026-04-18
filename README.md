# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **45**
- Today's entries: **23**
- Today's note: `notes/2026-04-18.md`

### Latest Entry

- Timestamp: `2026-04-18T23:12:58+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 3
- `Architecture`: 3
- `Databases`: 3
- `Observability`: 3
- `Security`: 3

### Recent Timeline

- `2026-04-18T23:12:58+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-18T22:14:21+08:00` | **Log with stable keys** (Observability)
- `2026-04-18T21:26:40+08:00` | **Design for idempotency** (APIs)
- `2026-04-18T20:10:00+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-18T19:12:45+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-18T18:14:01+08:00` | **Write one behavior per test** (Testing)
- `2026-04-18T17:16:28+08:00` | **Use virtual environments by default** (Python)
- `2026-04-18T16:13:28+08:00` | **Prefer small focused commits** (Git)
- `2026-04-18T15:26:02+08:00` | **Write decisions down** (Leadership)
- `2026-04-18T14:24:38+08:00` | **Keyboard support is a baseline** (Accessibility)
