# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2551**
- Today's entries: **8**
- Today's note: `notes/2026-08-14.md`

### Latest Entry

- Timestamp: `2026-08-14T10:36:49+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 128
- `Architecture`: 128
- `Backend`: 128
- `Code Quality`: 128
- `Databases`: 128

### Recent Timeline

- `2026-08-14T10:36:49+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-14T09:34:15+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-14T08:53:07+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-14T08:27:26+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-14T07:46:17+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-14T07:16:29+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-14T06:46:20+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-14T06:16:47+08:00` | **Log with stable keys** (Observability)
- `2026-08-13T22:53:32+08:00` | **Design for idempotency** (APIs)
- `2026-08-13T22:29:01+08:00` | **Add indexes for real query patterns** (Databases)
