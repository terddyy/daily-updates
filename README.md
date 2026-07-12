# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2065**
- Today's entries: **6**
- Today's note: `notes/2026-07-12.md`

### Latest Entry

- Timestamp: `2026-07-12T09:40:22+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 104
- `Architecture`: 104
- `Databases`: 104
- `Observability`: 104
- `Security`: 104

### Recent Timeline

- `2026-07-12T09:40:22+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-12T08:57:12+08:00` | **Log with stable keys** (Observability)
- `2026-07-12T07:34:17+08:00` | **Design for idempotency** (APIs)
- `2026-07-12T07:05:04+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-12T06:31:34+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-12T06:04:31+08:00` | **Write one behavior per test** (Testing)
- `2026-07-11T22:38:47+08:00` | **Use virtual environments by default** (Python)
- `2026-07-11T21:32:42+08:00` | **Prefer small focused commits** (Git)
- `2026-07-11T20:49:20+08:00` | **Write decisions down** (Leadership)
- `2026-07-11T20:22:12+08:00` | **Keyboard support is a baseline** (Accessibility)
