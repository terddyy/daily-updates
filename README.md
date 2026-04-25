# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **211**
- Today's entries: **6**
- Today's note: `notes/2026-04-26.md`

### Latest Entry

- Timestamp: `2026-04-26T05:11:25+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 11
- `Architecture`: 11
- `Backend`: 11
- `Code Quality`: 11
- `Databases`: 11

### Recent Timeline

- `2026-04-26T05:11:25+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-26T04:10:55+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-26T03:17:06+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-26T02:12:27+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-26T01:14:03+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-26T00:11:47+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-25T23:14:17+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-25T22:16:17+08:00` | **Log with stable keys** (Observability)
- `2026-04-25T21:28:24+08:00` | **Design for idempotency** (APIs)
- `2026-04-25T20:11:53+08:00` | **Add indexes for real query patterns** (Databases)
