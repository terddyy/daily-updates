# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1565**
- Today's entries: **7**
- Today's note: `notes/2026-06-06.md`

### Latest Entry

- Timestamp: `2026-06-06T15:41:25+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 79
- `Architecture`: 79
- `Databases`: 79
- `Observability`: 79
- `Security`: 79

### Recent Timeline

- `2026-06-06T15:41:25+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-06T14:39:05+08:00` | **Log with stable keys** (Observability)
- `2026-06-06T13:22:05+08:00` | **Design for idempotency** (APIs)
- `2026-06-06T11:47:02+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-06T10:21:27+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-06T08:09:26+08:00` | **Write one behavior per test** (Testing)
- `2026-06-06T06:29:13+08:00` | **Use virtual environments by default** (Python)
- `2026-06-05T22:41:07+08:00` | **Prefer small focused commits** (Git)
- `2026-06-05T21:35:33+08:00` | **Write decisions down** (Leadership)
- `2026-06-05T20:26:52+08:00` | **Keyboard support is a baseline** (Accessibility)
