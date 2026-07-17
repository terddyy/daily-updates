# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2167**
- Today's entries: **10**
- Today's note: `notes/2026-07-17.md`

### Latest Entry

- Timestamp: `2026-07-17T13:05:37+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 109
- `Architecture`: 109
- `Backend`: 109
- `Databases`: 109
- `Frontend`: 109

### Recent Timeline

- `2026-07-17T13:05:37+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-17T11:50:13+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-17T10:39:38+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-17T09:37:13+08:00` | **Log with stable keys** (Observability)
- `2026-07-17T08:53:49+08:00` | **Design for idempotency** (APIs)
- `2026-07-17T08:06:59+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-17T07:34:24+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-17T07:06:54+08:00` | **Write one behavior per test** (Testing)
- `2026-07-17T06:34:28+08:00` | **Use virtual environments by default** (Python)
- `2026-07-17T06:08:22+08:00` | **Prefer small focused commits** (Git)
