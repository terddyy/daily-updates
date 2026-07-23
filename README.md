# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2227**
- Today's entries: **1**
- Today's note: `notes/2026-07-24.md`

### Latest Entry

- Timestamp: `2026-07-24T06:32:40+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 112
- `Architecture`: 112
- `Backend`: 112
- `Databases`: 112
- `Frontend`: 112

### Recent Timeline

- `2026-07-24T06:32:40+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-23T21:59:31+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-23T19:55:01+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-23T17:57:45+08:00` | **Log with stable keys** (Observability)
- `2026-07-23T15:18:25+08:00` | **Design for idempotency** (APIs)
- `2026-07-23T12:36:48+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-23T09:13:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-23T07:41:25+08:00` | **Write one behavior per test** (Testing)
- `2026-07-23T06:33:07+08:00` | **Use virtual environments by default** (Python)
- `2026-07-22T22:00:13+08:00` | **Prefer small focused commits** (Git)
