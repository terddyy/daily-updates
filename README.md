# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1907**
- Today's entries: **10**
- Today's note: `notes/2026-07-02.md`

### Latest Entry

- Timestamp: `2026-07-02T16:30:09+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 96
- `Architecture`: 96
- `Backend`: 96
- `Databases`: 96
- `Frontend`: 96

### Recent Timeline

- `2026-07-02T16:30:09+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-02T15:25:38+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-02T14:07:31+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-02T12:40:44+08:00` | **Log with stable keys** (Observability)
- `2026-07-02T11:11:09+08:00` | **Design for idempotency** (APIs)
- `2026-07-02T09:45:41+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-02T08:54:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-02T07:46:08+08:00` | **Write one behavior per test** (Testing)
- `2026-07-02T07:10:34+08:00` | **Use virtual environments by default** (Python)
- `2026-07-02T06:32:21+08:00` | **Prefer small focused commits** (Git)
