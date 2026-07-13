# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2085**
- Today's entries: **11**
- Today's note: `notes/2026-07-13.md`

### Latest Entry

- Timestamp: `2026-07-13T15:40:41+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 105
- `Architecture`: 105
- `Databases`: 105
- `Observability`: 105
- `Security`: 105

### Recent Timeline

- `2026-07-13T15:40:41+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-13T14:26:38+08:00` | **Log with stable keys** (Observability)
- `2026-07-13T13:12:45+08:00` | **Design for idempotency** (APIs)
- `2026-07-13T11:45:36+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-13T10:18:31+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-13T09:15:18+08:00` | **Write one behavior per test** (Testing)
- `2026-07-13T08:40:04+08:00` | **Use virtual environments by default** (Python)
- `2026-07-13T07:48:00+08:00` | **Prefer small focused commits** (Git)
- `2026-07-13T07:19:54+08:00` | **Write decisions down** (Leadership)
- `2026-07-13T06:47:15+08:00` | **Keyboard support is a baseline** (Accessibility)
