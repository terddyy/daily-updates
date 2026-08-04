# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2307**
- Today's entries: **1**
- Today's note: `notes/2026-08-05.md`

### Latest Entry

- Timestamp: `2026-08-05T06:28:53+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 116
- `Architecture`: 116
- `Backend`: 116
- `Databases`: 116
- `Frontend`: 116

### Recent Timeline

- `2026-08-05T06:28:53+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-04T20:18:21+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-04T18:09:21+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-04T15:23:56+08:00` | **Log with stable keys** (Observability)
- `2026-08-04T12:30:32+08:00` | **Design for idempotency** (APIs)
- `2026-08-04T09:06:21+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-04T07:35:33+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-04T06:17:30+08:00` | **Write one behavior per test** (Testing)
- `2026-08-03T21:40:44+08:00` | **Use virtual environments by default** (Python)
- `2026-08-03T18:54:29+08:00` | **Prefer small focused commits** (Git)
