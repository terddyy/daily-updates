# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1325**
- Today's entries: **4**
- Today's note: `notes/2026-05-20.md`

### Latest Entry

- Timestamp: `2026-05-20T08:09:45+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 67
- `Architecture`: 67
- `Databases`: 67
- `Observability`: 67
- `Security`: 67

### Recent Timeline

- `2026-05-20T08:09:45+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-20T07:40:15+08:00` | **Log with stable keys** (Observability)
- `2026-05-20T07:09:21+08:00` | **Design for idempotency** (APIs)
- `2026-05-20T06:31:02+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-19T22:25:49+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-19T21:28:14+08:00` | **Write one behavior per test** (Testing)
- `2026-05-19T20:03:59+08:00` | **Use virtual environments by default** (Python)
- `2026-05-19T18:49:36+08:00` | **Prefer small focused commits** (Git)
- `2026-05-19T17:32:14+08:00` | **Write decisions down** (Leadership)
- `2026-05-19T16:13:34+08:00` | **Keyboard support is a baseline** (Accessibility)
