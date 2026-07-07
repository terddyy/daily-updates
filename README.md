# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1987**
- Today's entries: **16**
- Today's note: `notes/2026-07-07.md`

### Latest Entry

- Timestamp: `2026-07-07T22:18:26+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 100
- `Architecture`: 100
- `Backend`: 100
- `Databases`: 100
- `Frontend`: 100

### Recent Timeline

- `2026-07-07T22:18:26+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-07T21:17:44+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-07T20:22:53+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-07T19:28:06+08:00` | **Log with stable keys** (Observability)
- `2026-07-07T18:26:03+08:00` | **Design for idempotency** (APIs)
- `2026-07-07T17:11:04+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-07T15:46:26+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-07T14:23:34+08:00` | **Write one behavior per test** (Testing)
- `2026-07-07T12:47:54+08:00` | **Use virtual environments by default** (Python)
- `2026-07-07T11:15:23+08:00` | **Prefer small focused commits** (Git)
