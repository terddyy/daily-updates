# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1587**
- Today's entries: **6**
- Today's note: `notes/2026-06-08.md`

### Latest Entry

- Timestamp: `2026-06-08T09:26:25+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 80
- `Architecture`: 80
- `Backend`: 80
- `Databases`: 80
- `Frontend`: 80

### Recent Timeline

- `2026-06-08T09:26:25+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-08T08:09:45+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-08T07:38:21+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-08T07:10:13+08:00` | **Log with stable keys** (Observability)
- `2026-06-08T06:40:59+08:00` | **Design for idempotency** (APIs)
- `2026-06-08T06:13:26+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-07T22:26:16+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-07T20:48:45+08:00` | **Write one behavior per test** (Testing)
- `2026-06-07T19:22:02+08:00` | **Use virtual environments by default** (Python)
- `2026-06-07T17:39:28+08:00` | **Prefer small focused commits** (Git)
