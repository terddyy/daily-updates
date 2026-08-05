# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2311**
- Today's entries: **5**
- Today's note: `notes/2026-08-05.md`

### Latest Entry

- Timestamp: `2026-08-05T08:36:06+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 116
- `Architecture`: 116
- `Backend`: 116
- `Code Quality`: 116
- `Databases`: 116

### Recent Timeline

- `2026-08-05T08:36:06+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-05T07:49:36+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-05T07:24:14+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-05T06:54:13+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-05T06:28:53+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-04T20:18:21+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-04T18:09:21+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-04T15:23:56+08:00` | **Log with stable keys** (Observability)
- `2026-08-04T12:30:32+08:00` | **Design for idempotency** (APIs)
- `2026-08-04T09:06:21+08:00` | **Add indexes for real query patterns** (Databases)
