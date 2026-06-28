# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1850**
- Today's entries: **10**
- Today's note: `notes/2026-06-28.md`

### Latest Entry

- Timestamp: `2026-06-28T19:53:07+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 93
- `Architecture`: 93
- `Backend`: 93
- `Code Quality`: 93
- `Databases`: 93

### Recent Timeline

- `2026-06-28T19:53:07+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-28T15:59:55+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-28T14:30:59+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-28T12:51:52+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-28T11:13:40+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-28T09:49:12+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-28T08:56:33+08:00` | **Log with stable keys** (Observability)
- `2026-06-28T07:25:35+08:00` | **Design for idempotency** (APIs)
- `2026-06-28T06:50:35+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-28T06:25:41+08:00` | **Rotate credentials on schedule** (Security)
