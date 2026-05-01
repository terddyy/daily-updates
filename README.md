# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **691**
- Today's entries: **419**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:10:26+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 35
- `Architecture`: 35
- `Backend`: 35
- `Code Quality`: 35
- `Databases`: 35

### Recent Timeline

- `2026-05-01T09:10:26+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-01T09:10:25+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-01T09:10:24+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-01T09:10:23+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-01T09:10:22+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-01T09:10:21+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-01T09:10:20+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-01T09:10:19+08:00` | **Log with stable keys** (Observability)
- `2026-05-01T09:10:18+08:00` | **Design for idempotency** (APIs)
- `2026-05-01T09:10:17+08:00` | **Add indexes for real query patterns** (Databases)
