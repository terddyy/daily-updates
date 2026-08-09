# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2407**
- Today's entries: **10**
- Today's note: `notes/2026-08-09.md`

### Latest Entry

- Timestamp: `2026-08-09T10:30:27+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 121
- `Architecture`: 121
- `Backend`: 121
- `Databases`: 121
- `Frontend`: 121

### Recent Timeline

- `2026-08-09T10:30:27+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-09T08:54:29+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-09T08:28:48+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-09T07:56:20+08:00` | **Log with stable keys** (Observability)
- `2026-08-09T07:42:20+08:00` | **Design for idempotency** (APIs)
- `2026-08-09T07:26:14+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-09T07:11:07+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-09T06:57:44+08:00` | **Write one behavior per test** (Testing)
- `2026-08-09T06:24:53+08:00` | **Use virtual environments by default** (Python)
- `2026-08-09T06:07:55+08:00` | **Prefer small focused commits** (Git)
