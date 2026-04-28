# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **265**
- Today's entries: **16**
- Today's note: `notes/2026-04-28.md`

### Latest Entry

- Timestamp: `2026-04-28T17:46:23+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 14
- `Architecture`: 14
- `Databases`: 14
- `Observability`: 14
- `Security`: 14

### Recent Timeline

- `2026-04-28T17:46:23+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-28T16:48:25+08:00` | **Log with stable keys** (Observability)
- `2026-04-28T15:46:59+08:00` | **Design for idempotency** (APIs)
- `2026-04-28T14:52:42+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-28T13:07:05+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-28T11:04:02+08:00` | **Write one behavior per test** (Testing)
- `2026-04-28T09:34:31+08:00` | **Use virtual environments by default** (Python)
- `2026-04-28T08:27:19+08:00` | **Prefer small focused commits** (Git)
- `2026-04-28T07:18:18+08:00` | **Write decisions down** (Leadership)
- `2026-04-28T06:16:24+08:00` | **Keyboard support is a baseline** (Accessibility)
