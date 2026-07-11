# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2051**
- Today's entries: **10**
- Today's note: `notes/2026-07-11.md`

### Latest Entry

- Timestamp: `2026-07-11T16:23:16+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 103
- `Architecture`: 103
- `Backend`: 103
- `Code Quality`: 103
- `Databases`: 103

### Recent Timeline

- `2026-07-11T16:23:16+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-11T15:41:12+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-11T15:00:02+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-11T13:05:19+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-11T10:39:42+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-11T09:36:44+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-11T08:51:59+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-11T08:06:23+08:00` | **Log with stable keys** (Observability)
- `2026-07-11T07:34:47+08:00` | **Design for idempotency** (APIs)
- `2026-07-11T06:08:53+08:00` | **Add indexes for real query patterns** (Databases)
