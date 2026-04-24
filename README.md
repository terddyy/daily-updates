# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **185**
- Today's entries: **3**
- Today's note: `notes/2026-04-25.md`

### Latest Entry

- Timestamp: `2026-04-25T02:13:50+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 10
- `Architecture`: 10
- `Databases`: 10
- `Observability`: 10
- `Security`: 10

### Recent Timeline

- `2026-04-25T02:13:50+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-25T01:19:34+08:00` | **Log with stable keys** (Observability)
- `2026-04-25T00:19:39+08:00` | **Design for idempotency** (APIs)
- `2026-04-24T23:26:23+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-24T22:32:50+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-24T21:31:45+08:00` | **Write one behavior per test** (Testing)
- `2026-04-24T20:19:25+08:00` | **Use virtual environments by default** (Python)
- `2026-04-24T19:24:48+08:00` | **Prefer small focused commits** (Git)
- `2026-04-24T18:31:00+08:00` | **Write decisions down** (Leadership)
- `2026-04-24T17:33:06+08:00` | **Keyboard support is a baseline** (Accessibility)
