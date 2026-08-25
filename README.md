# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2825**
- Today's entries: **16**
- Today's note: `notes/2026-08-25.md`

### Latest Entry

- Timestamp: `2026-08-25T18:32:14+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 142
- `Architecture`: 142
- `Databases`: 142
- `Observability`: 142
- `Security`: 142

### Recent Timeline

- `2026-08-25T18:32:14+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-25T17:51:19+08:00` | **Log with stable keys** (Observability)
- `2026-08-25T17:08:14+08:00` | **Design for idempotency** (APIs)
- `2026-08-25T16:23:33+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-25T15:42:40+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-25T14:46:27+08:00` | **Write one behavior per test** (Testing)
- `2026-08-25T13:47:32+08:00` | **Use virtual environments by default** (Python)
- `2026-08-25T13:04:59+08:00` | **Prefer small focused commits** (Git)
- `2026-08-25T12:23:07+08:00` | **Write decisions down** (Leadership)
- `2026-08-25T11:31:07+08:00` | **Keyboard support is a baseline** (Accessibility)
