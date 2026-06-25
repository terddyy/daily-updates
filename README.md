# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1811**
- Today's entries: **14**
- Today's note: `notes/2026-06-25.md`

### Latest Entry

- Timestamp: `2026-06-25T20:20:51+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 91
- `Architecture`: 91
- `Backend`: 91
- `Code Quality`: 91
- `Databases`: 91

### Recent Timeline

- `2026-06-25T20:20:51+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-25T19:27:30+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-25T18:28:01+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-25T17:25:13+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-25T16:10:42+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-25T14:47:49+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-25T13:25:19+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-25T11:46:46+08:00` | **Log with stable keys** (Observability)
- `2026-06-25T10:22:04+08:00` | **Design for idempotency** (APIs)
- `2026-06-25T09:18:35+08:00` | **Add indexes for real query patterns** (Databases)
