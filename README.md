# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1391**
- Today's entries: **6**
- Today's note: `notes/2026-05-24.md`

### Latest Entry

- Timestamp: `2026-05-24T17:42:10+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 70
- `Architecture`: 70
- `Backend`: 70
- `Code Quality`: 70
- `Databases`: 70

### Recent Timeline

- `2026-05-24T17:42:10+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-24T15:46:57+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-24T14:43:57+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-24T09:20:00+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-24T08:07:00+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-24T06:34:19+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-23T22:35:38+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-23T21:55:18+08:00` | **Log with stable keys** (Observability)
- `2026-05-23T21:11:15+08:00` | **Design for idempotency** (APIs)
- `2026-05-23T20:38:18+08:00` | **Add indexes for real query patterns** (Databases)
