# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2165**
- Today's entries: **8**
- Today's note: `notes/2026-07-17.md`

### Latest Entry

- Timestamp: `2026-07-17T10:39:38+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 109
- `Architecture`: 109
- `Databases`: 109
- `Observability`: 109
- `Security`: 109

### Recent Timeline

- `2026-07-17T10:39:38+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-17T09:37:13+08:00` | **Log with stable keys** (Observability)
- `2026-07-17T08:53:49+08:00` | **Design for idempotency** (APIs)
- `2026-07-17T08:06:59+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-17T07:34:24+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-17T07:06:54+08:00` | **Write one behavior per test** (Testing)
- `2026-07-17T06:34:28+08:00` | **Use virtual environments by default** (Python)
- `2026-07-17T06:08:22+08:00` | **Prefer small focused commits** (Git)
- `2026-07-16T22:45:53+08:00` | **Write decisions down** (Leadership)
- `2026-07-16T21:57:12+08:00` | **Keyboard support is a baseline** (Accessibility)
