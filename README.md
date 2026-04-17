# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **8**
- Today's entries: **4**
- Today's note: `notes/2026-04-17.md`

### Latest Entry

- Timestamp: `2026-04-17T08:23:23+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 1
- `Architecture`: 1
- `Backend`: 1
- `Databases`: 1
- `Frontend`: 1

### Recent Timeline

- `2026-04-17T08:23:23+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-17T07:14:41+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-17T06:13:24+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-17T05:42:48+08:00` | **Log with stable keys** (Observability)
- `2026-04-16T20:07:44+08:00` | **Design for idempotency** (APIs)
- `2026-04-16T16:53:00+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-16T16:09:27+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-16T15:43:03+08:00` | **Write one behavior per test** (Testing)
