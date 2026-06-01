# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1507**
- Today's entries: **3**
- Today's note: `notes/2026-06-02.md`

### Latest Entry

- Timestamp: `2026-06-02T07:36:56+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 76
- `Architecture`: 76
- `Backend`: 76
- `Databases`: 76
- `Frontend`: 76

### Recent Timeline

- `2026-06-02T07:36:56+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-02T06:56:37+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-02T06:05:33+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-01T21:25:22+08:00` | **Log with stable keys** (Observability)
- `2026-06-01T19:19:24+08:00` | **Design for idempotency** (APIs)
- `2026-06-01T17:24:51+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-01T15:29:15+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-01T13:42:31+08:00` | **Write one behavior per test** (Testing)
- `2026-06-01T11:52:36+08:00` | **Use virtual environments by default** (Python)
- `2026-06-01T10:28:13+08:00` | **Prefer small focused commits** (Git)
