# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2531**
- Today's entries: **16**
- Today's note: `notes/2026-08-13.md`

### Latest Entry

- Timestamp: `2026-08-13T16:33:01+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 127
- `Architecture`: 127
- `Backend`: 127
- `Code Quality`: 127
- `Databases`: 127

### Recent Timeline

- `2026-08-13T16:33:01+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-13T15:49:54+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-13T15:11:11+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-13T14:33:56+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-13T13:47:53+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-13T13:08:27+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-13T12:24:45+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-13T11:32:26+08:00` | **Log with stable keys** (Observability)
- `2026-08-13T10:37:07+08:00` | **Design for idempotency** (APIs)
- `2026-08-13T09:34:18+08:00` | **Add indexes for real query patterns** (Databases)
