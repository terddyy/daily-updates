# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1511**
- Today's entries: **7**
- Today's note: `notes/2026-06-02.md`

### Latest Entry

- Timestamp: `2026-06-02T11:50:35+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 76
- `Architecture`: 76
- `Backend`: 76
- `Code Quality`: 76
- `Databases`: 76

### Recent Timeline

- `2026-06-02T11:50:35+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-02T10:26:51+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-02T09:26:54+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-02T08:10:51+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-02T07:36:56+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-02T06:56:37+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-02T06:05:33+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-01T21:25:22+08:00` | **Log with stable keys** (Observability)
- `2026-06-01T19:19:24+08:00` | **Design for idempotency** (APIs)
- `2026-06-01T17:24:51+08:00` | **Add indexes for real query patterns** (Databases)
