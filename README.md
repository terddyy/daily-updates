# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **267**
- Today's entries: **18**
- Today's note: `notes/2026-04-28.md`

### Latest Entry

- Timestamp: `2026-04-28T19:32:58+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 14
- `Architecture`: 14
- `Backend`: 14
- `Databases`: 14
- `Frontend`: 14

### Recent Timeline

- `2026-04-28T19:32:58+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-28T18:39:17+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-28T17:46:23+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-28T16:48:25+08:00` | **Log with stable keys** (Observability)
- `2026-04-28T15:46:59+08:00` | **Design for idempotency** (APIs)
- `2026-04-28T14:52:42+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-28T13:07:05+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-28T11:04:02+08:00` | **Write one behavior per test** (Testing)
- `2026-04-28T09:34:31+08:00` | **Use virtual environments by default** (Python)
- `2026-04-28T08:27:19+08:00` | **Prefer small focused commits** (Git)
