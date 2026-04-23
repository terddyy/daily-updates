# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **151**
- Today's entries: **15**
- Today's note: `notes/2026-04-23.md`

### Latest Entry

- Timestamp: `2026-04-23T15:33:41+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 8
- `Architecture`: 8
- `Backend`: 8
- `Code Quality`: 8
- `Databases`: 8

### Recent Timeline

- `2026-04-23T15:33:41+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-23T14:36:47+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-23T13:50:49+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-23T12:59:16+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-23T11:02:36+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-23T09:33:38+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-23T08:26:14+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-23T07:17:01+08:00` | **Log with stable keys** (Observability)
- `2026-04-23T06:15:12+08:00` | **Design for idempotency** (APIs)
- `2026-04-23T05:17:05+08:00` | **Add indexes for real query patterns** (Databases)
