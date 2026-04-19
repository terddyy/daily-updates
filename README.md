# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **71**
- Today's entries: **3**
- Today's note: `notes/2026-04-20.md`

### Latest Entry

- Timestamp: `2026-04-20T02:11:39+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 4
- `Architecture`: 4
- `Backend`: 4
- `Code Quality`: 4
- `Databases`: 4

### Recent Timeline

- `2026-04-20T02:11:39+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-20T01:11:47+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-20T00:10:17+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-19T23:13:17+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-19T22:14:28+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-19T21:26:08+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-19T20:09:52+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-19T19:13:14+08:00` | **Log with stable keys** (Observability)
- `2026-04-19T18:13:32+08:00` | **Design for idempotency** (APIs)
- `2026-04-19T17:16:42+08:00` | **Add indexes for real query patterns** (Databases)
