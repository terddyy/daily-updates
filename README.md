# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1405**
- Today's entries: **9**
- Today's note: `notes/2026-05-25.md`

### Latest Entry

- Timestamp: `2026-05-25T13:37:32+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 71
- `Architecture`: 71
- `Databases`: 71
- `Observability`: 71
- `Security`: 71

### Recent Timeline

- `2026-05-25T13:37:32+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-25T11:47:45+08:00` | **Log with stable keys** (Observability)
- `2026-05-25T10:23:01+08:00` | **Design for idempotency** (APIs)
- `2026-05-25T09:21:22+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-25T08:08:43+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-25T07:37:31+08:00` | **Write one behavior per test** (Testing)
- `2026-05-25T07:07:22+08:00` | **Use virtual environments by default** (Python)
- `2026-05-25T06:36:27+08:00` | **Prefer small focused commits** (Git)
- `2026-05-25T06:06:16+08:00` | **Write decisions down** (Leadership)
- `2026-05-24T22:34:18+08:00` | **Keyboard support is a baseline** (Accessibility)
