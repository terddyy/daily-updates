# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1590**
- Today's entries: **9**
- Today's note: `notes/2026-06-08.md`

### Latest Entry

- Timestamp: `2026-06-08T13:39:54+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 80
- `Architecture`: 80
- `Backend`: 80
- `Code Quality`: 80
- `Databases`: 80

### Recent Timeline

- `2026-06-08T13:39:54+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-08T11:49:25+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-08T10:26:09+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-08T09:26:25+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-08T08:09:45+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-08T07:38:21+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-08T07:10:13+08:00` | **Log with stable keys** (Observability)
- `2026-06-08T06:40:59+08:00` | **Design for idempotency** (APIs)
- `2026-06-08T06:13:26+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-07T22:26:16+08:00` | **Rotate credentials on schedule** (Security)
