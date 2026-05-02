# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1167**
- Today's entries: **395**
- Today's note: `notes/2026-05-02.md`

### Latest Entry

- Timestamp: `2026-05-02T08:44:40+08:00`
- Title: **Set realistic timeouts everywhere**
- Category: `Backend`
- Source: https://sre.google/sre-book/addressing-cascading-failures/
- Summary: Explicit timeouts on outbound calls prevent thread exhaustion and keep cascading failures contained.

### Top Categories

- `APIs`: 59
- `Architecture`: 59
- `Backend`: 59
- `Databases`: 59
- `Frontend`: 59

### Recent Timeline

- `2026-05-02T08:44:40+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-02T08:44:39+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-02T08:44:38+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-02T08:44:37+08:00` | **Log with stable keys** (Observability)
- `2026-05-02T08:44:36+08:00` | **Design for idempotency** (APIs)
- `2026-05-02T08:44:35+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-02T08:44:34+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-02T08:44:33+08:00` | **Write one behavior per test** (Testing)
- `2026-05-02T08:44:32+08:00` | **Use virtual environments by default** (Python)
- `2026-05-02T08:44:31+08:00` | **Prefer small focused commits** (Git)
