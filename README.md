# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2611**
- Today's entries: **2**
- Today's note: `notes/2026-08-16.md`

### Latest Entry

- Timestamp: `2026-08-16T06:51:40+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 131
- `Architecture`: 131
- `Backend`: 131
- `Code Quality`: 131
- `Databases`: 131

### Recent Timeline

- `2026-08-16T06:51:40+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-16T06:23:56+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-15T22:52:05+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-15T22:39:06+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-15T22:23:52+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-15T22:06:32+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-15T21:43:54+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-15T21:28:48+08:00` | **Log with stable keys** (Observability)
- `2026-08-15T21:13:03+08:00` | **Design for idempotency** (APIs)
- `2026-08-15T20:06:50+08:00` | **Add indexes for real query patterns** (Databases)
