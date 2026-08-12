# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2511**
- Today's entries: **24**
- Today's note: `notes/2026-08-12.md`

### Latest Entry

- Timestamp: `2026-08-12T20:31:56+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 126
- `Architecture`: 126
- `Backend`: 126
- `Code Quality`: 126
- `Databases`: 126

### Recent Timeline

- `2026-08-12T20:31:56+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-12T20:00:38+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-12T19:31:18+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-12T19:07:12+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-12T18:37:36+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-12T18:08:58+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-12T17:39:49+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-12T17:09:43+08:00` | **Log with stable keys** (Observability)
- `2026-08-12T16:32:04+08:00` | **Design for idempotency** (APIs)
- `2026-08-12T15:49:31+08:00` | **Add indexes for real query patterns** (Databases)
