# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1930**
- Today's entries: **17**
- Today's note: `notes/2026-07-03.md`

### Latest Entry

- Timestamp: `2026-07-03T21:22:30+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 97
- `Architecture`: 97
- `Backend`: 97
- `Code Quality`: 97
- `Databases`: 97

### Recent Timeline

- `2026-07-03T21:22:30+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-03T20:42:32+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-03T19:49:48+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-03T18:56:37+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-03T17:45:58+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-03T16:32:59+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-03T15:24:03+08:00` | **Log with stable keys** (Observability)
- `2026-07-03T14:03:05+08:00` | **Design for idempotency** (APIs)
- `2026-07-03T12:33:47+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-03T11:14:43+08:00` | **Rotate credentials on schedule** (Security)
