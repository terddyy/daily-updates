# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2545**
- Today's entries: **2**
- Today's note: `notes/2026-08-14.md`

### Latest Entry

- Timestamp: `2026-08-14T06:46:20+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 128
- `Architecture`: 128
- `Databases`: 128
- `Observability`: 128
- `Security`: 128

### Recent Timeline

- `2026-08-14T06:46:20+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-14T06:16:47+08:00` | **Log with stable keys** (Observability)
- `2026-08-13T22:53:32+08:00` | **Design for idempotency** (APIs)
- `2026-08-13T22:29:01+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-13T21:47:14+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-13T21:09:48+08:00` | **Write one behavior per test** (Testing)
- `2026-08-13T20:32:12+08:00` | **Use virtual environments by default** (Python)
- `2026-08-13T20:00:40+08:00` | **Prefer small focused commits** (Git)
- `2026-08-13T19:30:56+08:00` | **Write decisions down** (Leadership)
- `2026-08-13T19:06:50+08:00` | **Keyboard support is a baseline** (Accessibility)
