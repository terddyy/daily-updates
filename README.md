# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2030**
- Today's entries: **6**
- Today's note: `notes/2026-07-10.md`

### Latest Entry

- Timestamp: `2026-07-10T09:42:57+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 102
- `Architecture`: 102
- `Backend`: 102
- `Code Quality`: 102
- `Databases`: 102

### Recent Timeline

- `2026-07-10T09:42:57+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-10T08:58:27+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-10T08:10:55+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-10T07:41:43+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-10T07:09:53+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-10T06:32:26+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-09T22:44:51+08:00` | **Log with stable keys** (Observability)
- `2026-07-09T21:42:51+08:00` | **Design for idempotency** (APIs)
- `2026-07-09T19:44:35+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-09T18:42:07+08:00` | **Rotate credentials on schedule** (Security)
