# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2007**
- Today's entries: **20**
- Today's note: `notes/2026-07-08.md`

### Latest Entry

- Timestamp: `2026-07-08T22:35:36+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 101
- `Architecture`: 101
- `Backend`: 101
- `Databases`: 101
- `Frontend`: 101

### Recent Timeline

- `2026-07-08T22:35:36+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-08T21:38:17+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-08T20:49:36+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-08T20:03:00+08:00` | **Log with stable keys** (Observability)
- `2026-07-08T19:23:26+08:00` | **Design for idempotency** (APIs)
- `2026-07-08T18:30:41+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-08T17:33:53+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-08T16:38:31+08:00` | **Write one behavior per test** (Testing)
- `2026-07-08T15:37:25+08:00` | **Use virtual environments by default** (Python)
- `2026-07-08T14:36:28+08:00` | **Prefer small focused commits** (Git)
