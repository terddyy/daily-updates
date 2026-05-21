# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1345**
- Today's entries: **8**
- Today's note: `notes/2026-05-21.md`

### Latest Entry

- Timestamp: `2026-05-21T13:29:44+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 68
- `Architecture`: 68
- `Databases`: 68
- `Observability`: 68
- `Security`: 68

### Recent Timeline

- `2026-05-21T13:29:44+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-21T11:47:40+08:00` | **Log with stable keys** (Observability)
- `2026-05-21T10:23:26+08:00` | **Design for idempotency** (APIs)
- `2026-05-21T09:22:11+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-21T08:14:15+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-21T07:43:58+08:00` | **Write one behavior per test** (Testing)
- `2026-05-21T07:10:49+08:00` | **Use virtual environments by default** (Python)
- `2026-05-21T06:37:42+08:00` | **Prefer small focused commits** (Git)
- `2026-05-20T22:43:00+08:00` | **Write decisions down** (Leadership)
- `2026-05-20T21:40:31+08:00` | **Keyboard support is a baseline** (Accessibility)
