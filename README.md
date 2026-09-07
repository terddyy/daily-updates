# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2925**
- Today's entries: **9**
- Today's note: `notes/2026-09-07.md`

### Latest Entry

- Timestamp: `2026-09-07T08:37:19+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 147
- `Architecture`: 147
- `Databases`: 147
- `Observability`: 147
- `Security`: 147

### Recent Timeline

- `2026-09-07T08:37:19+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-09-07T07:48:32+08:00` | **Log with stable keys** (Observability)
- `2026-09-07T07:34:52+08:00` | **Design for idempotency** (APIs)
- `2026-09-07T07:20:54+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-09-07T07:09:21+08:00` | **Rotate credentials on schedule** (Security)
- `2026-09-07T06:48:09+08:00` | **Write one behavior per test** (Testing)
- `2026-09-07T06:34:43+08:00` | **Use virtual environments by default** (Python)
- `2026-09-07T06:22:00+08:00` | **Prefer small focused commits** (Git)
- `2026-09-07T06:10:03+08:00` | **Write decisions down** (Leadership)
- `2026-09-06T22:35:06+08:00` | **Keyboard support is a baseline** (Accessibility)
