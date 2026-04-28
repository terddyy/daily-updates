# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **271**
- Today's entries: **1**
- Today's note: `notes/2026-04-29.md`

### Latest Entry

- Timestamp: `2026-04-29T00:35:09+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 14
- `Architecture`: 14
- `Backend`: 14
- `Code Quality`: 14
- `Databases`: 14

### Recent Timeline

- `2026-04-29T00:35:09+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-28T23:47:35+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-28T21:34:24+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-28T20:33:48+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-28T19:32:58+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-28T18:39:17+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-28T17:46:23+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-28T16:48:25+08:00` | **Log with stable keys** (Observability)
- `2026-04-28T15:46:59+08:00` | **Design for idempotency** (APIs)
- `2026-04-28T14:52:42+08:00` | **Add indexes for real query patterns** (Databases)
