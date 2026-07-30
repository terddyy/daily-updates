# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2271**
- Today's entries: **5**
- Today's note: `notes/2026-07-30.md`

### Latest Entry

- Timestamp: `2026-07-30T15:12:19+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 114
- `Architecture`: 114
- `Backend`: 114
- `Code Quality`: 114
- `Databases`: 114

### Recent Timeline

- `2026-07-30T15:12:19+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-30T12:20:17+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-30T09:02:29+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-30T07:42:12+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-30T06:39:21+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-29T21:24:01+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-29T19:39:40+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-29T17:21:29+08:00` | **Log with stable keys** (Observability)
- `2026-07-29T14:18:30+08:00` | **Design for idempotency** (APIs)
- `2026-07-29T11:39:14+08:00` | **Add indexes for real query patterns** (Databases)
