# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1627**
- Today's entries: **3**
- Today's note: `notes/2026-06-11.md`

### Latest Entry

- Timestamp: `2026-06-11T07:48:49+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 82
- `Architecture`: 82
- `Backend`: 82
- `Databases`: 82
- `Frontend`: 82

### Recent Timeline

- `2026-06-11T07:48:49+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-11T07:05:08+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-11T06:25:54+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-10T22:49:06+08:00` | **Log with stable keys** (Observability)
- `2026-06-10T21:44:18+08:00` | **Design for idempotency** (APIs)
- `2026-06-10T20:24:55+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-10T19:03:17+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-10T17:31:56+08:00` | **Write one behavior per test** (Testing)
- `2026-06-10T16:10:06+08:00` | **Use virtual environments by default** (Python)
- `2026-06-10T14:32:49+08:00` | **Prefer small focused commits** (Git)
