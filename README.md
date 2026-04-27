# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **247**
- Today's entries: **20**
- Today's note: `notes/2026-04-27.md`

### Latest Entry

- Timestamp: `2026-04-27T21:32:56+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 13
- `Architecture`: 13
- `Backend`: 13
- `Databases`: 13
- `Frontend`: 13

### Recent Timeline

- `2026-04-27T21:32:56+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-27T20:29:47+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-27T19:33:21+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-27T18:38:32+08:00` | **Log with stable keys** (Observability)
- `2026-04-27T17:44:57+08:00` | **Design for idempotency** (APIs)
- `2026-04-27T16:49:43+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-27T15:46:54+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-27T14:50:55+08:00` | **Write one behavior per test** (Testing)
- `2026-04-27T13:04:24+08:00` | **Use virtual environments by default** (Python)
- `2026-04-27T11:04:03+08:00` | **Prefer small focused commits** (Git)
