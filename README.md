# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **225**
- Today's entries: **20**
- Today's note: `notes/2026-04-26.md`

### Latest Entry

- Timestamp: `2026-04-26T21:28:41+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 12
- `Architecture`: 12
- `Databases`: 12
- `Observability`: 12
- `Security`: 12

### Recent Timeline

- `2026-04-26T21:28:41+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-26T20:13:04+08:00` | **Log with stable keys** (Observability)
- `2026-04-26T19:15:09+08:00` | **Design for idempotency** (APIs)
- `2026-04-26T18:15:25+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-26T17:19:39+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-26T16:26:05+08:00` | **Write one behavior per test** (Testing)
- `2026-04-26T15:31:33+08:00` | **Use virtual environments by default** (Python)
- `2026-04-26T14:36:56+08:00` | **Prefer small focused commits** (Git)
- `2026-04-26T13:01:39+08:00` | **Write decisions down** (Leadership)
- `2026-04-26T11:03:12+08:00` | **Keyboard support is a baseline** (Accessibility)
