# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2171**
- Today's entries: **14**
- Today's note: `notes/2026-07-17.md`

### Latest Entry

- Timestamp: `2026-07-17T16:49:35+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 109
- `Architecture`: 109
- `Backend`: 109
- `Code Quality`: 109
- `Databases`: 109

### Recent Timeline

- `2026-07-17T16:49:35+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-17T15:55:57+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-17T15:02:47+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-17T14:03:08+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-17T13:05:37+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-17T11:50:13+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-17T10:39:38+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-17T09:37:13+08:00` | **Log with stable keys** (Observability)
- `2026-07-17T08:53:49+08:00` | **Design for idempotency** (APIs)
- `2026-07-17T08:06:59+08:00` | **Add indexes for real query patterns** (Databases)
