# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **347**
- Today's entries: **75**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:04:42+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 18
- `Architecture`: 18
- `Backend`: 18
- `Databases`: 18
- `Frontend`: 18

### Recent Timeline

- `2026-05-01T09:04:42+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-01T09:04:41+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-01T09:04:40+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-01T09:04:39+08:00` | **Log with stable keys** (Observability)
- `2026-05-01T09:04:38+08:00` | **Design for idempotency** (APIs)
- `2026-05-01T09:04:37+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-01T09:04:36+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-01T09:04:35+08:00` | **Write one behavior per test** (Testing)
- `2026-05-01T09:04:34+08:00` | **Use virtual environments by default** (Python)
- `2026-05-01T09:04:33+08:00` | **Prefer small focused commits** (Git)
