# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1707**
- Today's entries: **3**
- Today's note: `notes/2026-06-18.md`

### Latest Entry

- Timestamp: `2026-06-18T07:36:07+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 86
- `Architecture`: 86
- `Backend`: 86
- `Databases`: 86
- `Frontend`: 86

### Recent Timeline

- `2026-06-18T07:36:07+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-18T06:51:58+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-18T06:12:03+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-17T22:43:17+08:00` | **Log with stable keys** (Observability)
- `2026-06-17T21:32:49+08:00` | **Design for idempotency** (APIs)
- `2026-06-17T20:12:32+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-17T18:40:53+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-17T16:56:24+08:00` | **Write one behavior per test** (Testing)
- `2026-06-17T15:01:53+08:00` | **Use virtual environments by default** (Python)
- `2026-06-17T13:13:36+08:00` | **Prefer small focused commits** (Git)
