# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2207**
- Today's entries: **5**
- Today's note: `notes/2026-07-21.md`

### Latest Entry

- Timestamp: `2026-07-21T15:19:58+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 111
- `Architecture`: 111
- `Backend`: 111
- `Databases`: 111
- `Frontend`: 111

### Recent Timeline

- `2026-07-21T15:19:58+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-21T12:32:02+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-21T09:09:29+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-21T07:40:28+08:00` | **Log with stable keys** (Observability)
- `2026-07-21T06:39:14+08:00` | **Design for idempotency** (APIs)
- `2026-07-20T22:38:10+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-20T20:16:32+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-20T17:45:21+08:00` | **Write one behavior per test** (Testing)
- `2026-07-20T14:34:41+08:00` | **Use virtual environments by default** (Python)
- `2026-07-20T11:39:32+08:00` | **Prefer small focused commits** (Git)
