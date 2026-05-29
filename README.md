# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1467**
- Today's entries: **14**
- Today's note: `notes/2026-05-29.md`

### Latest Entry

- Timestamp: `2026-05-29T21:49:21+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 74
- `Architecture`: 74
- `Backend`: 74
- `Databases`: 74
- `Frontend`: 74

### Recent Timeline

- `2026-05-29T21:49:21+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-29T20:33:13+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-29T19:25:54+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-29T18:09:35+08:00` | **Log with stable keys** (Observability)
- `2026-05-29T16:32:16+08:00` | **Design for idempotency** (APIs)
- `2026-05-29T15:03:10+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-29T13:31:57+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-29T11:47:17+08:00` | **Write one behavior per test** (Testing)
- `2026-05-29T10:23:16+08:00` | **Use virtual environments by default** (Python)
- `2026-05-29T09:21:02+08:00` | **Prefer small focused commits** (Git)
