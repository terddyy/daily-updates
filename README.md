# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1690**
- Today's entries: **11**
- Today's note: `notes/2026-06-16.md`

### Latest Entry

- Timestamp: `2026-06-16T20:16:19+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 85
- `Architecture`: 85
- `Backend`: 85
- `Code Quality`: 85
- `Databases`: 85

### Recent Timeline

- `2026-06-16T20:16:19+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-16T18:16:40+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-16T16:21:53+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-16T14:12:41+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-16T12:13:32+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-16T10:42:01+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-16T09:36:42+08:00` | **Log with stable keys** (Observability)
- `2026-06-16T08:17:35+08:00` | **Design for idempotency** (APIs)
- `2026-06-16T07:40:52+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-16T06:56:32+08:00` | **Rotate credentials on schedule** (Security)
