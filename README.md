# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2390**
- Today's entries: **19**
- Today's note: `notes/2026-08-08.md`

### Latest Entry

- Timestamp: `2026-08-08T19:01:13+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 120
- `Architecture`: 120
- `Backend`: 120
- `Code Quality`: 120
- `Databases`: 120

### Recent Timeline

- `2026-08-08T19:01:13+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-08T18:25:54+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-08T18:10:31+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-08T17:47:07+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-08T17:01:23+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-08T15:22:10+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-08T14:17:16+08:00` | **Log with stable keys** (Observability)
- `2026-08-08T13:17:26+08:00` | **Design for idempotency** (APIs)
- `2026-08-08T12:48:20+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-08T12:15:32+08:00` | **Rotate credentials on schedule** (Security)
