# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1807**
- Today's entries: **10**
- Today's note: `notes/2026-06-25.md`

### Latest Entry

- Timestamp: `2026-06-25T16:10:42+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 91
- `Architecture`: 91
- `Backend`: 91
- `Databases`: 91
- `Frontend`: 91

### Recent Timeline

- `2026-06-25T16:10:42+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-25T14:47:49+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-25T13:25:19+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-25T11:46:46+08:00` | **Log with stable keys** (Observability)
- `2026-06-25T10:22:04+08:00` | **Design for idempotency** (APIs)
- `2026-06-25T09:18:35+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-25T08:10:35+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-25T07:40:31+08:00` | **Write one behavior per test** (Testing)
- `2026-06-25T07:08:50+08:00` | **Use virtual environments by default** (Python)
- `2026-06-25T06:31:04+08:00` | **Prefer small focused commits** (Git)
