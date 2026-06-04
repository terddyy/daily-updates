# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1545**
- Today's entries: **2**
- Today's note: `notes/2026-06-05.md`

### Latest Entry

- Timestamp: `2026-06-05T07:09:51+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 78
- `Architecture`: 78
- `Databases`: 78
- `Observability`: 78
- `Security`: 78

### Recent Timeline

- `2026-06-05T07:09:51+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-05T06:34:16+08:00` | **Log with stable keys** (Observability)
- `2026-06-04T22:13:30+08:00` | **Design for idempotency** (APIs)
- `2026-06-04T21:12:36+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-04T19:46:49+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-04T18:43:38+08:00` | **Write one behavior per test** (Testing)
- `2026-06-04T17:25:04+08:00` | **Use virtual environments by default** (Python)
- `2026-06-04T15:53:11+08:00` | **Prefer small focused commits** (Git)
- `2026-06-04T13:58:30+08:00` | **Write decisions down** (Leadership)
- `2026-06-04T12:12:46+08:00` | **Keyboard support is a baseline** (Accessibility)
