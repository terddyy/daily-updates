# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **371**
- Today's entries: **99**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:05:06+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 19
- `Architecture`: 19
- `Backend`: 19
- `Code Quality`: 19
- `Databases`: 19

### Recent Timeline

- `2026-05-01T09:05:06+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-01T09:05:05+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-01T09:05:04+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-01T09:05:03+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-01T09:05:02+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-01T09:05:01+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-01T09:05:00+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-01T09:04:59+08:00` | **Log with stable keys** (Observability)
- `2026-05-01T09:04:58+08:00` | **Design for idempotency** (APIs)
- `2026-05-01T09:04:57+08:00` | **Add indexes for real query patterns** (Databases)
