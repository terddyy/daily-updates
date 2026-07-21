# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2211**
- Today's entries: **1**
- Today's note: `notes/2026-07-22.md`

### Latest Entry

- Timestamp: `2026-07-22T06:36:18+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 111
- `Architecture`: 111
- `Backend`: 111
- `Code Quality`: 111
- `Databases`: 111

### Recent Timeline

- `2026-07-22T06:36:18+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-21T22:13:37+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-21T19:59:58+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-21T18:01:21+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-21T15:19:58+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-21T12:32:02+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-21T09:09:29+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-21T07:40:28+08:00` | **Log with stable keys** (Observability)
- `2026-07-21T06:39:14+08:00` | **Design for idempotency** (APIs)
- `2026-07-20T22:38:10+08:00` | **Add indexes for real query patterns** (Databases)
