# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2127**
- Today's entries: **13**
- Today's note: `notes/2026-07-15.md`

### Latest Entry

- Timestamp: `2026-07-15T16:16:47+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 107
- `Architecture`: 107
- `Backend`: 107
- `Databases`: 107
- `Frontend`: 107

### Recent Timeline

- `2026-07-15T16:16:47+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-15T15:16:40+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-15T14:16:41+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-15T13:19:27+08:00` | **Log with stable keys** (Observability)
- `2026-07-15T12:17:55+08:00` | **Design for idempotency** (APIs)
- `2026-07-15T11:11:29+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-15T09:58:14+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-15T09:11:56+08:00` | **Write one behavior per test** (Testing)
- `2026-07-15T08:32:16+08:00` | **Use virtual environments by default** (Python)
- `2026-07-15T07:48:02+08:00` | **Prefer small focused commits** (Git)
