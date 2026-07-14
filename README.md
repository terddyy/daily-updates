# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2111**
- Today's entries: **20**
- Today's note: `notes/2026-07-14.md`

### Latest Entry

- Timestamp: `2026-07-14T20:42:40+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 106
- `Architecture`: 106
- `Backend`: 106
- `Code Quality`: 106
- `Databases`: 106

### Recent Timeline

- `2026-07-14T20:42:40+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-14T20:09:48+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-14T19:31:48+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-14T18:52:53+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-14T18:09:52+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-14T17:16:45+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-14T16:29:49+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-14T15:36:52+08:00` | **Log with stable keys** (Observability)
- `2026-07-14T14:54:54+08:00` | **Design for idempotency** (APIs)
- `2026-07-14T13:58:55+08:00` | **Add indexes for real query patterns** (Databases)
