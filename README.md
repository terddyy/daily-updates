# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2525**
- Today's entries: **10**
- Today's note: `notes/2026-08-13.md`

### Latest Entry

- Timestamp: `2026-08-13T12:24:45+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 127
- `Architecture`: 127
- `Databases`: 127
- `Observability`: 127
- `Security`: 127

### Recent Timeline

- `2026-08-13T12:24:45+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-13T11:32:26+08:00` | **Log with stable keys** (Observability)
- `2026-08-13T10:37:07+08:00` | **Design for idempotency** (APIs)
- `2026-08-13T09:34:18+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-13T08:52:09+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-13T08:27:01+08:00` | **Write one behavior per test** (Testing)
- `2026-08-13T07:46:27+08:00` | **Use virtual environments by default** (Python)
- `2026-08-13T07:16:25+08:00` | **Prefer small focused commits** (Git)
- `2026-08-13T06:46:22+08:00` | **Write decisions down** (Leadership)
- `2026-08-13T06:16:28+08:00` | **Keyboard support is a baseline** (Accessibility)
