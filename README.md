# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1331**
- Today's entries: **10**
- Today's note: `notes/2026-05-20.md`

### Latest Entry

- Timestamp: `2026-05-20T16:12:54+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 67
- `Architecture`: 67
- `Backend`: 67
- `Code Quality`: 67
- `Databases`: 67

### Recent Timeline

- `2026-05-20T16:12:54+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-20T14:49:42+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-20T13:26:21+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-20T11:47:20+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-20T10:22:43+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-20T09:19:37+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-20T08:09:45+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-20T07:40:15+08:00` | **Log with stable keys** (Observability)
- `2026-05-20T07:09:21+08:00` | **Design for idempotency** (APIs)
- `2026-05-20T06:31:02+08:00` | **Add indexes for real query patterns** (Databases)
