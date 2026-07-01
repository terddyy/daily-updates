# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1887**
- Today's entries: **5**
- Today's note: `notes/2026-07-01.md`

### Latest Entry

- Timestamp: `2026-07-01T09:23:31+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 95
- `Architecture`: 95
- `Backend`: 95
- `Databases`: 95
- `Frontend`: 95

### Recent Timeline

- `2026-07-01T09:23:31+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-01T08:09:10+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-01T07:35:16+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-01T06:58:43+08:00` | **Log with stable keys** (Observability)
- `2026-07-01T06:29:38+08:00` | **Design for idempotency** (APIs)
- `2026-06-30T22:37:24+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-30T21:39:03+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-30T20:46:28+08:00` | **Write one behavior per test** (Testing)
- `2026-06-30T19:46:19+08:00` | **Use virtual environments by default** (Python)
- `2026-06-30T18:44:51+08:00` | **Prefer small focused commits** (Git)
