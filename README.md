# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2645**
- Today's entries: **2**
- Today's note: `notes/2026-08-17.md`

### Latest Entry

- Timestamp: `2026-08-17T06:50:53+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 133
- `Architecture`: 133
- `Databases`: 133
- `Observability`: 133
- `Security`: 133

### Recent Timeline

- `2026-08-17T06:50:53+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-17T06:29:38+08:00` | **Log with stable keys** (Observability)
- `2026-08-16T22:52:21+08:00` | **Design for idempotency** (APIs)
- `2026-08-16T22:39:01+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-16T22:24:13+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-16T21:53:39+08:00` | **Write one behavior per test** (Testing)
- `2026-08-16T21:30:34+08:00` | **Use virtual environments by default** (Python)
- `2026-08-16T20:47:16+08:00` | **Prefer small focused commits** (Git)
- `2026-08-16T20:25:45+08:00` | **Write decisions down** (Leadership)
- `2026-08-16T19:51:13+08:00` | **Keyboard support is a baseline** (Accessibility)
