# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **811**
- Today's entries: **39**
- Today's note: `notes/2026-05-02.md`

### Latest Entry

- Timestamp: `2026-05-02T08:38:44+08:00`
- Title: **Keep runbooks close to code**
- Category: `Documentation`
- Source: https://sre.google/workbook/
- Summary: Version-controlled operational runbooks age better than external docs and stay aligned with implementation changes.

### Top Categories

- `APIs`: 41
- `Architecture`: 41
- `Backend`: 41
- `Code Quality`: 41
- `Databases`: 41

### Recent Timeline

- `2026-05-02T08:38:44+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-02T08:38:43+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-02T08:38:42+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-02T08:38:41+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-02T08:38:40+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-02T08:38:39+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-02T08:38:38+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-02T08:38:37+08:00` | **Log with stable keys** (Observability)
- `2026-05-02T08:38:36+08:00` | **Design for idempotency** (APIs)
- `2026-05-02T08:38:35+08:00` | **Add indexes for real query patterns** (Databases)
