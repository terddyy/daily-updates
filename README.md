# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1487**
- Today's entries: **7**
- Today's note: `notes/2026-05-31.md`

### Latest Entry

- Timestamp: `2026-05-31T19:10:28+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 75
- `Architecture`: 75
- `Backend`: 75
- `Databases`: 75
- `Frontend`: 75

### Recent Timeline

- `2026-05-31T19:10:28+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-31T18:27:21+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-31T17:32:01+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-31T16:20:51+08:00` | **Log with stable keys** (Observability)
- `2026-05-31T13:35:16+08:00` | **Design for idempotency** (APIs)
- `2026-05-31T06:35:27+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-31T06:08:04+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-30T22:36:14+08:00` | **Write one behavior per test** (Testing)
- `2026-05-30T20:31:02+08:00` | **Use virtual environments by default** (Python)
- `2026-05-30T19:45:57+08:00` | **Prefer small focused commits** (Git)
