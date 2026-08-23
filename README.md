# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2790**
- Today's entries: **1**
- Today's note: `notes/2026-08-24.md`

### Latest Entry

- Timestamp: `2026-08-24T06:20:33+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 140
- `Architecture`: 140
- `Backend`: 140
- `Code Quality`: 140
- `Databases`: 140

### Recent Timeline

- `2026-08-24T06:20:33+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-23T22:22:38+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-23T21:53:35+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-23T21:20:06+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-23T20:38:43+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-23T19:28:28+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-23T18:59:40+08:00` | **Log with stable keys** (Observability)
- `2026-08-23T18:32:42+08:00` | **Design for idempotency** (APIs)
- `2026-08-23T17:35:44+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-23T15:47:02+08:00` | **Rotate credentials on schedule** (Security)
