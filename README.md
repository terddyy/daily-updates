# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2331**
- Today's entries: **5**
- Today's note: `notes/2026-08-06.md`

### Latest Entry

- Timestamp: `2026-08-06T08:06:46+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 117
- `Architecture`: 117
- `Backend`: 117
- `Code Quality`: 117
- `Databases`: 117

### Recent Timeline

- `2026-08-06T08:06:46+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-06T07:34:25+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-06T07:08:13+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-06T06:37:44+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-06T06:11:10+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-05T22:50:41+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-05T21:55:33+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-05T21:05:44+08:00` | **Log with stable keys** (Observability)
- `2026-08-05T20:23:41+08:00` | **Design for idempotency** (APIs)
- `2026-08-05T19:30:42+08:00` | **Add indexes for real query patterns** (Databases)
