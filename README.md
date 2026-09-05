# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2865**
- Today's entries: **3**
- Today's note: `notes/2026-09-05.md`

### Latest Entry

- Timestamp: `2026-09-05T17:48:18+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 144
- `Architecture`: 144
- `Databases`: 144
- `Observability`: 144
- `Security`: 144

### Recent Timeline

- `2026-09-05T17:48:18+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-09-05T17:24:25+08:00` | **Log with stable keys** (Observability)
- `2026-09-05T17:11:31+08:00` | **Design for idempotency** (APIs)
- `2026-08-31T08:50:59+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-31T06:39:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-30T21:08:09+08:00` | **Write one behavior per test** (Testing)
- `2026-08-30T15:16:31+08:00` | **Use virtual environments by default** (Python)
- `2026-08-30T07:20:13+08:00` | **Prefer small focused commits** (Git)
- `2026-08-29T18:04:24+08:00` | **Write decisions down** (Leadership)
- `2026-08-29T11:10:01+08:00` | **Keyboard support is a baseline** (Accessibility)
