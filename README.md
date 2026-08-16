# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2631**
- Today's entries: **22**
- Today's note: `notes/2026-08-16.md`

### Latest Entry

- Timestamp: `2026-08-16T18:24:23+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 132
- `Architecture`: 132
- `Backend`: 132
- `Code Quality`: 132
- `Databases`: 132

### Recent Timeline

- `2026-08-16T18:24:23+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-16T18:06:16+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-16T17:53:27+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-16T17:41:04+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-16T17:25:52+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-16T17:11:07+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-16T16:57:49+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-16T16:43:10+08:00` | **Log with stable keys** (Observability)
- `2026-08-16T16:24:53+08:00` | **Design for idempotency** (APIs)
- `2026-08-16T15:54:09+08:00` | **Add indexes for real query patterns** (Databases)
