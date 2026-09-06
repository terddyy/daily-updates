# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2885**
- Today's entries: **6**
- Today's note: `notes/2026-09-06.md`

### Latest Entry

- Timestamp: `2026-09-06T10:17:08+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 145
- `Architecture`: 145
- `Databases`: 145
- `Observability`: 145
- `Security`: 145

### Recent Timeline

- `2026-09-06T10:17:08+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-09-06T08:37:49+08:00` | **Log with stable keys** (Observability)
- `2026-09-06T06:48:01+08:00` | **Design for idempotency** (APIs)
- `2026-09-06T06:34:34+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-09-06T06:20:56+08:00` | **Rotate credentials on schedule** (Security)
- `2026-09-06T06:09:45+08:00` | **Write one behavior per test** (Testing)
- `2026-09-05T22:48:14+08:00` | **Use virtual environments by default** (Python)
- `2026-09-05T22:34:55+08:00` | **Prefer small focused commits** (Git)
- `2026-09-05T22:21:42+08:00` | **Write decisions down** (Leadership)
- `2026-09-05T22:10:14+08:00` | **Keyboard support is a baseline** (Accessibility)
