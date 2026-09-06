# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2910**
- Today's entries: **31**
- Today's note: `notes/2026-09-06.md`

### Latest Entry

- Timestamp: `2026-09-06T19:09:19+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 146
- `Architecture`: 146
- `Backend`: 146
- `Code Quality`: 146
- `Databases`: 146

### Recent Timeline

- `2026-09-06T19:09:19+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-09-06T18:48:24+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-09-06T18:34:40+08:00` | **Automate rollback paths** (DevOps)
- `2026-09-06T18:22:44+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-09-06T18:10:27+08:00` | **Optimize first contentful view** (Frontend)
- `2026-09-06T17:24:40+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-09-06T16:48:57+08:00` | **Log with stable keys** (Observability)
- `2026-09-06T16:31:46+08:00` | **Design for idempotency** (APIs)
- `2026-09-06T16:14:50+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-09-06T15:48:21+08:00` | **Rotate credentials on schedule** (Security)
