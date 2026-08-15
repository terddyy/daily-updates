# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2590**
- Today's entries: **19**
- Today's note: `notes/2026-08-15.md`

### Latest Entry

- Timestamp: `2026-08-15T13:53:25+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 130
- `Architecture`: 130
- `Backend`: 130
- `Code Quality`: 130
- `Databases`: 130

### Recent Timeline

- `2026-08-15T13:53:25+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-15T13:25:00+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-15T12:43:14+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-15T12:26:00+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-15T12:10:46+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-15T11:47:13+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-15T11:26:45+08:00` | **Log with stable keys** (Observability)
- `2026-08-15T11:03:10+08:00` | **Design for idempotency** (APIs)
- `2026-08-15T10:36:36+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-15T10:10:44+08:00` | **Rotate credentials on schedule** (Security)
