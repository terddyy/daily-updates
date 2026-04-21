# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **107**
- Today's entries: **17**
- Today's note: `notes/2026-04-21.md`

### Latest Entry

- Timestamp: `2026-04-21T17:32:24+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 6
- `Architecture`: 6
- `Backend`: 6
- `Databases`: 6
- `Frontend`: 6

### Recent Timeline

- `2026-04-21T17:32:24+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-21T16:35:36+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-21T15:33:05+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-21T14:36:11+08:00` | **Log with stable keys** (Observability)
- `2026-04-21T13:48:40+08:00` | **Design for idempotency** (APIs)
- `2026-04-21T12:57:51+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-21T11:02:43+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-21T09:33:37+08:00` | **Write one behavior per test** (Testing)
- `2026-04-21T08:23:39+08:00` | **Use virtual environments by default** (Python)
- `2026-04-21T07:15:15+08:00` | **Prefer small focused commits** (Git)
