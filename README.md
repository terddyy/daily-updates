# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1831**
- Today's entries: **2**
- Today's note: `notes/2026-06-27.md`

### Latest Entry

- Timestamp: `2026-06-27T07:29:19+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 92
- `Architecture`: 92
- `Backend`: 92
- `Code Quality`: 92
- `Databases`: 92

### Recent Timeline

- `2026-06-27T07:29:19+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-27T06:14:51+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-26T22:57:34+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-26T21:48:54+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-26T20:59:22+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-26T20:01:36+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-26T19:04:18+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-26T17:46:26+08:00` | **Log with stable keys** (Observability)
- `2026-06-26T16:26:03+08:00` | **Design for idempotency** (APIs)
- `2026-06-26T15:02:25+08:00` | **Add indexes for real query patterns** (Databases)
