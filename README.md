# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1730**
- Today's entries: **12**
- Today's note: `notes/2026-06-19.md`

### Latest Entry

- Timestamp: `2026-06-19T22:10:50+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 87
- `Architecture`: 87
- `Backend`: 87
- `Code Quality`: 87
- `Databases`: 87

### Recent Timeline

- `2026-06-19T22:10:50+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-19T20:57:07+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-19T19:35:51+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-19T17:53:04+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-19T16:13:56+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-19T14:03:10+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-19T12:13:41+08:00` | **Log with stable keys** (Observability)
- `2026-06-19T10:42:19+08:00` | **Design for idempotency** (APIs)
- `2026-06-19T09:39:07+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-19T08:15:37+08:00` | **Rotate credentials on schedule** (Security)
