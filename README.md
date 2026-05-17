# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1285**
- Today's entries: **7**
- Today's note: `notes/2026-05-17.md`

### Latest Entry

- Timestamp: `2026-05-17T17:22:01+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 65
- `Architecture`: 65
- `Databases`: 65
- `Observability`: 65
- `Security`: 65

### Recent Timeline

- `2026-05-17T17:22:01+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-17T16:32:56+08:00` | **Log with stable keys** (Observability)
- `2026-05-17T15:38:31+08:00` | **Design for idempotency** (APIs)
- `2026-05-17T10:21:37+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-17T09:17:00+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-17T07:04:50+08:00` | **Write one behavior per test** (Testing)
- `2026-05-17T06:30:52+08:00` | **Use virtual environments by default** (Python)
- `2026-05-16T21:11:13+08:00` | **Prefer small focused commits** (Git)
- `2026-05-16T20:39:06+08:00` | **Write decisions down** (Leadership)
- `2026-05-16T20:03:48+08:00` | **Keyboard support is a baseline** (Accessibility)
