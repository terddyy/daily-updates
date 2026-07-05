# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1951**
- Today's entries: **8**
- Today's note: `notes/2026-07-05.md`

### Latest Entry

- Timestamp: `2026-07-05T15:38:13+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 98
- `Architecture`: 98
- `Backend`: 98
- `Code Quality`: 98
- `Databases`: 98

### Recent Timeline

- `2026-07-05T15:38:13+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-05T14:19:39+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-05T11:16:16+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-05T08:08:09+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-05T07:36:39+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-05T07:07:07+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-05T06:35:03+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-05T06:06:42+08:00` | **Log with stable keys** (Observability)
- `2026-07-04T22:16:04+08:00` | **Design for idempotency** (APIs)
- `2026-07-04T19:46:24+08:00` | **Add indexes for real query patterns** (Databases)
