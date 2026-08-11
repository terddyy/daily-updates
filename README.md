# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2485**
- Today's entries: **31**
- Today's note: `notes/2026-08-11.md`

### Latest Entry

- Timestamp: `2026-08-11T21:30:59+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 125
- `Architecture`: 125
- `Databases`: 125
- `Observability`: 125
- `Security`: 125

### Recent Timeline

- `2026-08-11T21:30:59+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-11T20:48:26+08:00` | **Log with stable keys** (Observability)
- `2026-08-11T20:24:00+08:00` | **Design for idempotency** (APIs)
- `2026-08-11T19:59:49+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-11T19:31:15+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-11T19:03:36+08:00` | **Write one behavior per test** (Testing)
- `2026-08-11T18:32:51+08:00` | **Use virtual environments by default** (Python)
- `2026-08-11T18:06:58+08:00` | **Prefer small focused commits** (Git)
- `2026-08-11T17:35:42+08:00` | **Write decisions down** (Leadership)
- `2026-08-11T17:08:02+08:00` | **Keyboard support is a baseline** (Accessibility)
