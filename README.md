# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1911**
- Today's entries: **14**
- Today's note: `notes/2026-07-02.md`

### Latest Entry

- Timestamp: `2026-07-02T20:43:48+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 96
- `Architecture`: 96
- `Backend`: 96
- `Code Quality`: 96
- `Databases`: 96

### Recent Timeline

- `2026-07-02T20:43:48+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-02T19:50:55+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-02T18:56:36+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-02T17:47:31+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-02T16:30:09+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-02T15:25:38+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-02T14:07:31+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-02T12:40:44+08:00` | **Log with stable keys** (Observability)
- `2026-07-02T11:11:09+08:00` | **Design for idempotency** (APIs)
- `2026-07-02T09:45:41+08:00` | **Add indexes for real query patterns** (Databases)
