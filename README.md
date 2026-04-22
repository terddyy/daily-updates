# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **125**
- Today's entries: **12**
- Today's note: `notes/2026-04-22.md`

### Latest Entry

- Timestamp: `2026-04-22T12:56:24+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 7
- `Architecture`: 7
- `Databases`: 7
- `Observability`: 7
- `Security`: 7

### Recent Timeline

- `2026-04-22T12:56:24+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-22T11:02:58+08:00` | **Log with stable keys** (Observability)
- `2026-04-22T09:33:36+08:00` | **Design for idempotency** (APIs)
- `2026-04-22T08:20:57+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-22T07:13:36+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-22T06:14:26+08:00` | **Write one behavior per test** (Testing)
- `2026-04-22T05:15:33+08:00` | **Use virtual environments by default** (Python)
- `2026-04-22T04:17:38+08:00` | **Prefer small focused commits** (Git)
- `2026-04-22T03:27:45+08:00` | **Write decisions down** (Leadership)
- `2026-04-22T02:21:32+08:00` | **Keyboard support is a baseline** (Accessibility)
