# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2470**
- Today's entries: **16**
- Today's note: `notes/2026-08-11.md`

### Latest Entry

- Timestamp: `2026-08-11T14:02:45+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 124
- `Architecture`: 124
- `Backend`: 124
- `Code Quality`: 124
- `Databases`: 124

### Recent Timeline

- `2026-08-11T14:02:45+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-11T13:39:49+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-11T13:13:55+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-11T12:43:46+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-11T12:01:22+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-11T11:22:37+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-11T10:44:28+08:00` | **Log with stable keys** (Observability)
- `2026-08-11T09:55:14+08:00` | **Design for idempotency** (APIs)
- `2026-08-11T09:10:49+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-11T08:32:33+08:00` | **Rotate credentials on schedule** (Security)
