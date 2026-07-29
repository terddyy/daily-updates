# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2267**
- Today's entries: **1**
- Today's note: `notes/2026-07-30.md`

### Latest Entry

- Timestamp: `2026-07-30T06:39:21+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 114
- `Architecture`: 114
- `Backend`: 114
- `Databases`: 114
- `Frontend`: 114

### Recent Timeline

- `2026-07-30T06:39:21+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-29T21:24:01+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-29T19:39:40+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-29T17:21:29+08:00` | **Log with stable keys** (Observability)
- `2026-07-29T14:18:30+08:00` | **Design for idempotency** (APIs)
- `2026-07-29T11:39:14+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-29T08:03:59+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-29T06:58:32+08:00` | **Write one behavior per test** (Testing)
- `2026-07-28T22:40:12+08:00` | **Use virtual environments by default** (Python)
- `2026-07-28T20:13:11+08:00` | **Prefer small focused commits** (Git)
