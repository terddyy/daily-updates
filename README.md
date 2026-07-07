# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1991**
- Today's entries: **4**
- Today's note: `notes/2026-07-08.md`

### Latest Entry

- Timestamp: `2026-07-08T07:48:44+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 100
- `Architecture`: 100
- `Backend`: 100
- `Code Quality`: 100
- `Databases`: 100

### Recent Timeline

- `2026-07-08T07:48:44+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-08T07:22:13+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-08T06:49:15+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-08T06:15:34+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-07T22:18:26+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-07T21:17:44+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-07T20:22:53+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-07T19:28:06+08:00` | **Log with stable keys** (Observability)
- `2026-07-07T18:26:03+08:00` | **Design for idempotency** (APIs)
- `2026-07-07T17:11:04+08:00` | **Add indexes for real query patterns** (Databases)
