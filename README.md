# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2465**
- Today's entries: **11**
- Today's note: `notes/2026-08-11.md`

### Latest Entry

- Timestamp: `2026-08-11T11:22:37+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 124
- `Architecture`: 124
- `Databases`: 124
- `Observability`: 124
- `Security`: 124

### Recent Timeline

- `2026-08-11T11:22:37+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-11T10:44:28+08:00` | **Log with stable keys** (Observability)
- `2026-08-11T09:55:14+08:00` | **Design for idempotency** (APIs)
- `2026-08-11T09:10:49+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-11T08:32:33+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-11T08:00:39+08:00` | **Write one behavior per test** (Testing)
- `2026-08-11T07:44:38+08:00` | **Use virtual environments by default** (Python)
- `2026-08-11T07:16:41+08:00` | **Prefer small focused commits** (Git)
- `2026-08-11T06:59:11+08:00` | **Write decisions down** (Leadership)
- `2026-08-11T06:31:25+08:00` | **Keyboard support is a baseline** (Accessibility)
