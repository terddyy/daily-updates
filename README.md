# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **145**
- Today's entries: **9**
- Today's note: `notes/2026-04-23.md`

### Latest Entry

- Timestamp: `2026-04-23T08:26:14+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 8
- `Architecture`: 8
- `Databases`: 8
- `Observability`: 8
- `Security`: 8

### Recent Timeline

- `2026-04-23T08:26:14+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-23T07:17:01+08:00` | **Log with stable keys** (Observability)
- `2026-04-23T06:15:12+08:00` | **Design for idempotency** (APIs)
- `2026-04-23T05:17:05+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-23T04:19:06+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-23T03:28:48+08:00` | **Write one behavior per test** (Testing)
- `2026-04-23T02:21:54+08:00` | **Use virtual environments by default** (Python)
- `2026-04-23T01:20:57+08:00` | **Prefer small focused commits** (Git)
- `2026-04-23T00:23:15+08:00` | **Write decisions down** (Leadership)
- `2026-04-22T23:27:50+08:00` | **Keyboard support is a baseline** (Accessibility)
