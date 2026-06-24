# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1791**
- Today's entries: **10**
- Today's note: `notes/2026-06-24.md`

### Latest Entry

- Timestamp: `2026-06-24T15:46:39+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 90
- `Architecture`: 90
- `Backend`: 90
- `Code Quality`: 90
- `Databases`: 90

### Recent Timeline

- `2026-06-24T15:46:39+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-24T14:23:18+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-24T12:53:40+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-24T11:25:12+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-24T10:02:32+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-24T09:13:54+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-24T08:06:27+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-24T07:37:13+08:00` | **Log with stable keys** (Observability)
- `2026-06-24T07:09:18+08:00` | **Design for idempotency** (APIs)
- `2026-06-24T06:35:28+08:00` | **Add indexes for real query patterns** (Databases)
