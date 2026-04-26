# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **227**
- Today's entries: **22**
- Today's note: `notes/2026-04-26.md`

### Latest Entry

- Timestamp: `2026-04-26T23:14:30+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 12
- `Architecture`: 12
- `Backend`: 12
- `Databases`: 12
- `Frontend`: 12

### Recent Timeline

- `2026-04-26T23:14:30+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-26T22:15:51+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-26T21:28:41+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-26T20:13:04+08:00` | **Log with stable keys** (Observability)
- `2026-04-26T19:15:09+08:00` | **Design for idempotency** (APIs)
- `2026-04-26T18:15:25+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-26T17:19:39+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-26T16:26:05+08:00` | **Write one behavior per test** (Testing)
- `2026-04-26T15:31:33+08:00` | **Use virtual environments by default** (Python)
- `2026-04-26T14:36:56+08:00` | **Prefer small focused commits** (Git)
