# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1365**
- Today's entries: **13**
- Today's note: `notes/2026-05-22.md`

### Latest Entry

- Timestamp: `2026-05-22T19:41:19+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 69
- `Architecture`: 69
- `Databases`: 69
- `Observability`: 69
- `Security`: 69

### Recent Timeline

- `2026-05-22T19:41:19+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-22T18:33:46+08:00` | **Log with stable keys** (Observability)
- `2026-05-22T17:26:19+08:00` | **Design for idempotency** (APIs)
- `2026-05-22T16:10:47+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-22T14:49:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-22T13:26:07+08:00` | **Write one behavior per test** (Testing)
- `2026-05-22T11:47:27+08:00` | **Use virtual environments by default** (Python)
- `2026-05-22T10:22:47+08:00` | **Prefer small focused commits** (Git)
- `2026-05-22T09:18:36+08:00` | **Write decisions down** (Leadership)
- `2026-05-22T08:09:22+08:00` | **Keyboard support is a baseline** (Accessibility)
