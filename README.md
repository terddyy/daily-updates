# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2091**
- Today's entries: **17**
- Today's note: `notes/2026-07-13.md`

### Latest Entry

- Timestamp: `2026-07-13T22:18:33+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 105
- `Architecture`: 105
- `Backend`: 105
- `Code Quality`: 105
- `Databases`: 105

### Recent Timeline

- `2026-07-13T22:18:33+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-13T21:18:07+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-13T20:16:45+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-13T19:06:01+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-13T17:55:51+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-13T16:42:46+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-13T15:40:41+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-13T14:26:38+08:00` | **Log with stable keys** (Observability)
- `2026-07-13T13:12:45+08:00` | **Design for idempotency** (APIs)
- `2026-07-13T11:45:36+08:00` | **Add indexes for real query patterns** (Databases)
