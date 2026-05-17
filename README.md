# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1291**
- Today's entries: **1**
- Today's note: `notes/2026-05-18.md`

### Latest Entry

- Timestamp: `2026-05-18T06:05:09+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 65
- `Architecture`: 65
- `Backend`: 65
- `Code Quality`: 65
- `Databases`: 65

### Recent Timeline

- `2026-05-18T06:05:09+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-17T21:10:55+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-17T20:06:18+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-17T19:42:30+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-17T18:43:57+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-17T18:04:27+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-17T17:22:01+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-17T16:32:56+08:00` | **Log with stable keys** (Observability)
- `2026-05-17T15:38:31+08:00` | **Design for idempotency** (APIs)
- `2026-05-17T10:21:37+08:00` | **Add indexes for real query patterns** (Databases)
