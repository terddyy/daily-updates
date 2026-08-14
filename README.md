# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2565**
- Today's entries: **22**
- Today's note: `notes/2026-08-14.md`

### Latest Entry

- Timestamp: `2026-08-14T19:30:15+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 129
- `Architecture`: 129
- `Databases`: 129
- `Observability`: 129
- `Security`: 129

### Recent Timeline

- `2026-08-14T19:30:15+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-14T19:05:37+08:00` | **Log with stable keys** (Observability)
- `2026-08-14T18:35:36+08:00` | **Design for idempotency** (APIs)
- `2026-08-14T18:08:32+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-14T17:37:26+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-14T17:09:06+08:00` | **Write one behavior per test** (Testing)
- `2026-08-14T16:30:12+08:00` | **Use virtual environments by default** (Python)
- `2026-08-14T15:49:02+08:00` | **Prefer small focused commits** (Git)
- `2026-08-14T15:11:12+08:00` | **Write decisions down** (Leadership)
- `2026-08-14T14:32:38+08:00` | **Keyboard support is a baseline** (Accessibility)
