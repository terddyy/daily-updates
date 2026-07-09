# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2025**
- Today's entries: **1**
- Today's note: `notes/2026-07-10.md`

### Latest Entry

- Timestamp: `2026-07-10T06:32:26+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 102
- `Architecture`: 102
- `Databases`: 102
- `Observability`: 102
- `Security`: 102

### Recent Timeline

- `2026-07-10T06:32:26+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-09T22:44:51+08:00` | **Log with stable keys** (Observability)
- `2026-07-09T21:42:51+08:00` | **Design for idempotency** (APIs)
- `2026-07-09T19:44:35+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-09T18:42:07+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-09T17:35:47+08:00` | **Write one behavior per test** (Testing)
- `2026-07-09T16:18:38+08:00` | **Use virtual environments by default** (Python)
- `2026-07-09T14:57:54+08:00` | **Prefer small focused commits** (Git)
- `2026-07-09T13:39:57+08:00` | **Write decisions down** (Leadership)
- `2026-07-09T12:10:35+08:00` | **Keyboard support is a baseline** (Accessibility)
