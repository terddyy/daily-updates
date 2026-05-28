# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1451**
- Today's entries: **12**
- Today's note: `notes/2026-05-28.md`

### Latest Entry

- Timestamp: `2026-05-28T19:02:46+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 73
- `Architecture`: 73
- `Backend`: 73
- `Code Quality`: 73
- `Databases`: 73

### Recent Timeline

- `2026-05-28T19:02:46+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-28T17:33:23+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-28T16:08:22+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-28T14:31:58+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-28T12:59:01+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-28T11:27:12+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-28T10:00:37+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-28T09:12:29+08:00` | **Log with stable keys** (Observability)
- `2026-05-28T08:08:16+08:00` | **Design for idempotency** (APIs)
- `2026-05-28T07:30:58+08:00` | **Add indexes for real query patterns** (Databases)
