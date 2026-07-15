# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2131**
- Today's entries: **17**
- Today's note: `notes/2026-07-15.md`

### Latest Entry

- Timestamp: `2026-07-15T19:35:18+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 107
- `Architecture`: 107
- `Backend`: 107
- `Code Quality`: 107
- `Databases`: 107

### Recent Timeline

- `2026-07-15T19:35:18+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-15T18:56:59+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-15T18:12:42+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-15T17:15:49+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-15T16:16:47+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-15T15:16:40+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-15T14:16:41+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-15T13:19:27+08:00` | **Log with stable keys** (Observability)
- `2026-07-15T12:17:55+08:00` | **Design for idempotency** (APIs)
- `2026-07-15T11:11:29+08:00` | **Add indexes for real query patterns** (Databases)
