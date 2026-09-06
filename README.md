# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2905**
- Today's entries: **26**
- Today's note: `notes/2026-09-06.md`

### Latest Entry

- Timestamp: `2026-09-06T17:24:40+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 146
- `Architecture`: 146
- `Databases`: 146
- `Observability`: 146
- `Security`: 146

### Recent Timeline

- `2026-09-06T17:24:40+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-09-06T16:48:57+08:00` | **Log with stable keys** (Observability)
- `2026-09-06T16:31:46+08:00` | **Design for idempotency** (APIs)
- `2026-09-06T16:14:50+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-09-06T15:48:21+08:00` | **Rotate credentials on schedule** (Security)
- `2026-09-06T15:35:28+08:00` | **Write one behavior per test** (Testing)
- `2026-09-06T15:25:42+08:00` | **Use virtual environments by default** (Python)
- `2026-09-06T15:12:01+08:00` | **Prefer small focused commits** (Git)
- `2026-09-06T14:44:12+08:00` | **Write decisions down** (Leadership)
- `2026-09-06T14:19:00+08:00` | **Keyboard support is a baseline** (Accessibility)
