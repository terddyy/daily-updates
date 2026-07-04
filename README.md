# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1947**
- Today's entries: **4**
- Today's note: `notes/2026-07-05.md`

### Latest Entry

- Timestamp: `2026-07-05T07:36:39+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 98
- `Architecture`: 98
- `Backend`: 98
- `Databases`: 98
- `Frontend`: 98

### Recent Timeline

- `2026-07-05T07:36:39+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-05T07:07:07+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-05T06:35:03+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-05T06:06:42+08:00` | **Log with stable keys** (Observability)
- `2026-07-04T22:16:04+08:00` | **Design for idempotency** (APIs)
- `2026-07-04T19:46:24+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-04T19:06:40+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-04T17:31:22+08:00` | **Write one behavior per test** (Testing)
- `2026-07-04T16:39:48+08:00` | **Use virtual environments by default** (Python)
- `2026-07-04T15:40:33+08:00` | **Prefer small focused commits** (Git)
