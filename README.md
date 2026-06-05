# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1547**
- Today's entries: **4**
- Today's note: `notes/2026-06-05.md`

### Latest Entry

- Timestamp: `2026-06-05T08:12:20+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 78
- `Architecture`: 78
- `Backend`: 78
- `Databases`: 78
- `Frontend`: 78

### Recent Timeline

- `2026-06-05T08:12:20+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-05T07:41:59+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-05T07:09:51+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-05T06:34:16+08:00` | **Log with stable keys** (Observability)
- `2026-06-04T22:13:30+08:00` | **Design for idempotency** (APIs)
- `2026-06-04T21:12:36+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-04T19:46:49+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-04T18:43:38+08:00` | **Write one behavior per test** (Testing)
- `2026-06-04T17:25:04+08:00` | **Use virtual environments by default** (Python)
- `2026-06-04T15:53:11+08:00` | **Prefer small focused commits** (Git)
