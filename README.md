# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1687**
- Today's entries: **8**
- Today's note: `notes/2026-06-16.md`

### Latest Entry

- Timestamp: `2026-06-16T14:12:41+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 85
- `Architecture`: 85
- `Backend`: 85
- `Databases`: 85
- `Frontend`: 85

### Recent Timeline

- `2026-06-16T14:12:41+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-16T12:13:32+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-16T10:42:01+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-16T09:36:42+08:00` | **Log with stable keys** (Observability)
- `2026-06-16T08:17:35+08:00` | **Design for idempotency** (APIs)
- `2026-06-16T07:40:52+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-16T06:56:32+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-16T06:04:16+08:00` | **Write one behavior per test** (Testing)
- `2026-06-15T20:52:05+08:00` | **Use virtual environments by default** (Python)
- `2026-06-15T18:40:50+08:00` | **Prefer small focused commits** (Git)
