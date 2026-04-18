# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **47**
- Today's entries: **2**
- Today's note: `notes/2026-04-19.md`

### Latest Entry

- Timestamp: `2026-04-19T01:11:56+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 3
- `Architecture`: 3
- `Backend`: 3
- `Databases`: 3
- `Frontend`: 3

### Recent Timeline

- `2026-04-19T01:11:56+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-19T00:10:26+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-18T23:12:58+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-18T22:14:21+08:00` | **Log with stable keys** (Observability)
- `2026-04-18T21:26:40+08:00` | **Design for idempotency** (APIs)
- `2026-04-18T20:10:00+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-18T19:12:45+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-18T18:14:01+08:00` | **Write one behavior per test** (Testing)
- `2026-04-18T17:16:28+08:00` | **Use virtual environments by default** (Python)
- `2026-04-18T16:13:28+08:00` | **Prefer small focused commits** (Git)
