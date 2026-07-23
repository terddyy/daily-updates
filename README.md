# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2225**
- Today's entries: **7**
- Today's note: `notes/2026-07-23.md`

### Latest Entry

- Timestamp: `2026-07-23T19:55:01+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 112
- `Architecture`: 112
- `Databases`: 112
- `Observability`: 112
- `Security`: 112

### Recent Timeline

- `2026-07-23T19:55:01+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-23T17:57:45+08:00` | **Log with stable keys** (Observability)
- `2026-07-23T15:18:25+08:00` | **Design for idempotency** (APIs)
- `2026-07-23T12:36:48+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-23T09:13:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-23T07:41:25+08:00` | **Write one behavior per test** (Testing)
- `2026-07-23T06:33:07+08:00` | **Use virtual environments by default** (Python)
- `2026-07-22T22:00:13+08:00` | **Prefer small focused commits** (Git)
- `2026-07-22T19:55:52+08:00` | **Write decisions down** (Leadership)
- `2026-07-22T17:58:52+08:00` | **Keyboard support is a baseline** (Accessibility)
