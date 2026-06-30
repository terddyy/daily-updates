# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1870**
- Today's entries: **5**
- Today's note: `notes/2026-06-30.md`

### Latest Entry

- Timestamp: `2026-06-30T08:09:00+08:00`
- Title: **Use exponential backoff with jitter**
- Category: `Reliability`
- Source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Summary: Backoff plus jitter avoids retry storms and improves recovery behavior when downstream systems are degraded.

### Top Categories

- `APIs`: 94
- `Architecture`: 94
- `Backend`: 94
- `Code Quality`: 94
- `Databases`: 94

### Recent Timeline

- `2026-06-30T08:09:00+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-30T07:36:57+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-30T07:07:55+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-30T06:37:57+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-30T06:09:17+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-29T21:46:48+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-29T20:00:37+08:00` | **Log with stable keys** (Observability)
- `2026-06-29T18:14:13+08:00` | **Design for idempotency** (APIs)
- `2026-06-29T16:41:22+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-29T14:53:54+08:00` | **Rotate credentials on schedule** (Security)
